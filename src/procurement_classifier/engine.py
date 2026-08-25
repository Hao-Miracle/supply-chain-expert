from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Mapping

from .models import Classification
from .taxonomy import SUBCATEGORIES


@dataclass(frozen=True)
class Rule:
    rule_id: str
    pattern: str
    sub_category: str
    priority: int = 80
    exclude: str = ""


RULES = (
    Rule("network-switch", r"交换机", "交换机", 95),
    Rule("router-wireless", r"路由器|无线AP|无线控制器", "路由及无线", 95),
    Rule("network-security", r"防火墙|网闸|入侵防御|堡垒机", "网络安全", 95),
    Rule("optical-transmission", r"光模块|光端机|光纤收发器", "光传输", 95),
    Rule("camera", r"摄像机|摄像头|枪机|球机|半球", "摄像机", 95, r"照相机"),
    Rule("video-storage", r"NVR|DVR|硬盘录像机|视频存储", "录像存储", 95),
    Rule("access-control", r"门禁控制器|磁力锁|电控锁|读卡器", "门禁控制", 95),
    Rule("patrol", r"巡更|电子巡查", "访客巡更", 95),
    Rule("server-storage", r"服务器|磁盘阵列|网络存储|NAS\b|SAN\b", "服务器及存储", 95),
    Rule("computer", r"台式电脑|台式计算机|笔记本电脑|工作站", "电脑", 90, r"监控工作站|楼宇.*工作站"),
    Rule("printer", r"打印机|复印机", "打印复印", 90),
    Rule("ups", r"\bUPS\b|不间断电源", "UPS不间断电源", 95),
    Rule("cabinet", r"服务器机柜|网络机柜|标准机柜", "机柜及配电", 95),
    Rule("fiber-cable", r"光缆|网线|双绞线|尾纤|跳线", "网线及光纤", 90),
    Rule("conduit", r"桥架|线槽|JDG|镀锌钢管|金属线管", "桥架线管", 90),
    Rule("patch-panel", r"配线架|理线架", "配线设备", 90),
    Rule("management-software", r"管理软件|管理平台|数据库软件", "管理平台", 85),
    Rule("electrical", r"浪涌保护器|接地线|配电箱|断路器", "电气材料", 90),
    Rule("building-control", r"温度传感器|湿度传感器|压差开关|CO2传感器|楼宇自控", "BAS系统", 90),
    Rule("energy-meter", r"智能电表|电能表|远传水表|能耗监测", "能耗监测", 95),
)

NON_ITEM = re.compile(r"^(?:预算)?(?:合计|小计|总计)|^序号$|^设备名称$")


def normalize_text(value: object) -> str:
    text = "" if value is None else str(value)
    text = text.strip().lower().replace("（", "(").replace("）", ")")
    text = re.sub(r"[\s\u3000]+", "", text)
    return text.replace("×", "x").replace("–", "-").replace("—", "-")


class ClassificationEngine:
    def __init__(self, reviewed: Mapping[str, str] | None = None):
        self.reviewed = dict(reviewed or {})

    def classify(self, name: object, spec: object = "", remark: object = "") -> Classification:
        clean_name = normalize_text(name)
        combined = normalize_text(f"{name} {spec} {remark}")
        if not clean_name or NON_ITEM.search(clean_name):
            return self._empty("insufficient-or-non-item")

        reviewed_sub = self.reviewed.get(f"{clean_name}|{normalize_text(spec)}") or self.reviewed.get(f"{clean_name}|")
        if reviewed_sub in SUBCATEGORIES:
            return self._result(reviewed_sub, 1.0, "reviewed-history", ("reviewed-history",), (), False)

        hits = [r for r in RULES if re.search(r.pattern, combined, re.I) and not (r.exclude and re.search(r.exclude, combined, re.I))]
        if not hits:
            return self._empty("no-rule-above-threshold")

        hits.sort(key=lambda r: (r.priority, len(r.pattern)), reverse=True)
        top = hits[0]
        alternatives = tuple(dict.fromkeys(r.sub_category for r in hits[1:] if r.sub_category != top.sub_category))
        same_priority_conflict = any(r.priority == top.priority and r.sub_category != top.sub_category for r in hits[1:])
        confidence = min(0.97, 0.85 + (top.priority - 80) / 150)
        if same_priority_conflict:
            confidence = min(confidence, 0.79)
        return self._result(top.sub_category, round(confidence, 3), "rule-suggestion", tuple(f"rule:{r.rule_id}" for r in hits[:3]), alternatives[:3], True)

    @staticmethod
    def _result(sub: str, confidence: float, source: str, evidence: tuple[str, ...], alternatives: tuple[str, ...], needs_review: bool) -> Classification:
        system, code = SUBCATEGORIES[sub]
        label = "high" if confidence >= 0.98 else "medium" if confidence >= 0.80 else "low"
        return Classification(system, sub, code, confidence, label, source, evidence, alternatives, needs_review)

    @staticmethod
    def _empty(reason: str) -> Classification:
        return Classification("", "", "", 0.0, "no-match", "", (reason,), (), True)

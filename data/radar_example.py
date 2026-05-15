"""
Пример построения радиальной диаграммы для одного объекта.
Аналог оригинального кода, адаптированный под классы магазина электроники.
"""
import math
from data.baseline_samples import BASELINE_RESISTOR, BASELINE_TRANSISTOR
from data.indicator_config import INDICATOR_CONFIG


# Диапазоны нормировки [min, max] для числовых показателей по каждому классу.
# В реальном приложении вычисляются по всему каталогу; здесь — типичные рыночные.
RANGES: dict[str, dict[str, tuple[float, float]]] = {
    "Resistor": {
        "power_w":          (0.125, 5.0),
        "accuracy_percent": (0.1,  20.0),
        "price_rub":        (0.5,  50.0),
    },
    "Transistor": {
        "max_current_a": (0.05, 30.0),
        "voltage_v":     (10.0, 600.0),
        "price_rub":     (3.0,  200.0),
    },
}


def normalize(value: float, lo: float, hi: float, inverse: bool) -> float:
    """Нормировать значение в [0, 1]; при inverse=True меньше → ближе к 1."""
    if hi == lo:
        return 1.0
    score = (value - lo) / (hi - lo)
    score = max(0.0, min(1.0, score))
    return 1.0 - score if inverse else score


def radar_scores(obj, class_name: str) -> dict[str, float]:
    """Вернуть нормированные баллы по каждому показателю (0..1)."""
    config = INDICATOR_CONFIG[class_name]
    result: dict[str, float] = {}
    for field, meta in config.items():
        raw = float(getattr(obj, field))
        if meta["binary"]:
            result[field] = raw          # уже 0.0 или 1.0
        else:
            lo, hi = RANGES[class_name][field]
            result[field] = normalize(raw, lo, hi, meta["inverse"])
    return result


def weighted_score(scores: dict[str, float], class_name: str) -> float:
    """Итоговый взвешенный балл объекта (0..1)."""
    config = INDICATOR_CONFIG[class_name]
    return sum(scores[f] * config[f]["weight"] for f in scores)


if __name__ == "__main__":
    for obj, name in [
        (BASELINE_RESISTOR,   "Resistor"),
        (BASELINE_TRANSISTOR, "Transistor"),
    ]:
        scores = radar_scores(obj, name)
        total  = weighted_score(scores, name)
        print(f"\n{name}")
        for field, val in scores.items():
            w = INDICATOR_CONFIG[name][field]["weight"]
            inv = " (инв.)" if INDICATOR_CONFIG[name][field]["inverse"] else ""
            print(f"  {field:<25} {val:.3f}  × {w}{inv}")
        print(f"  {'ИТОГО':<25} {total:.3f}")

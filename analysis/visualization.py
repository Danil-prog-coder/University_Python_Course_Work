"""
Визуализация результатов оценки технического уровня.

Реализует два типа диаграмм для сравнения образцов внутри группы:
  - Столбчатая: относительный технический уровень каждого образца
    (значение базового образца = 1.0), столбцы отсортированы по убыванию.
  - Радиальная (лепестковая): профиль унифицированных показателей каждого образца.

Технический уровень образца — среднее арифметическое унифицированных показателей.
Унифицирование: q_i / q_base (higher-is-better) или q_base / q_i (lower-is-better).
Бинарные признаки используются «как есть» (0.0 / 1.0) и могут быть исключены
через exclude_binary=True.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Sample:
    name: str
    indicators: dict  # {indicator_name: numeric_value}


@dataclass
class IndicatorSpec:
    name: str
    higher_is_better: bool = True
    is_binary: bool = False


# ─── computation ────────────────────────────────────────────────────────────

def _unify(value: float, base_value: float, higher_is_better: bool) -> float:
    if base_value == 0:
        return 1.0
    return (value / base_value) if higher_is_better else (base_value / value)


def compute_relative_levels(
    samples: list,
    specs: list,
    base_index: int = 0,
    exclude_binary: bool = False,
) -> tuple:
    """
    Returns (names, tech_levels, ind_names, norm_values).
    norm_values: {sample_name: [q̃_1, q̃_2, ...]}
    """
    active    = [s for s in specs if not (exclude_binary and s.is_binary)]
    ind_names = [s.name for s in active]
    base      = samples[base_index]

    names, tech_levels, norm_values = [], [], {}
    for sample in samples:
        row = []
        for spec in active:
            val  = float(sample.indicators[spec.name])
            bval = float(base.indicators[spec.name])
            if spec.is_binary:
                row.append(val)
            else:
                row.append(_unify(val, bval, spec.higher_is_better))
        norm_values[sample.name] = row
        tech_levels.append(sum(row) / len(row) if row else 1.0)
        names.append(sample.name)

    return names, tech_levels, ind_names, norm_values


# ─── charts ─────────────────────────────────────────────────────────────────

def create_bar_chart_relative(
    group_name: str,
    names: list,
    tech_levels: list,
    base_name: str,
    save_path: Optional[str] = None,
) -> None:
    """Столбчатая диаграмма: относительный техуровень, сортировка по убыванию."""
    pairs    = sorted(zip(tech_levels, names), reverse=True)
    s_levels = [p[0] for p in pairs]
    s_names  = [p[1] for p in pairs]
    colors   = ['#ff7f0e' if n == base_name else '#1f77b4' for n in s_names]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(s_names, s_levels, color=colors, edgecolor='white', linewidth=0.8)
    ax.axhline(1.0, color='red', linestyle='--', linewidth=1.2, label='Базовый уровень (1.0)')

    for bar, lv in zip(bars, s_levels):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            f'{lv:.2f}',
            ha='center', va='bottom', fontsize=9,
        )

    ax.set_title(f'Относительный технический уровень — {group_name}')
    ax.set_ylabel('Технический уровень')
    ax.set_ylim(0, max(s_levels) * 1.18 + 0.1)
    ax.legend()
    plt.tight_layout()
    _save_or_show(fig, save_path)


def create_radial_relative(
    group_name: str,
    names: list,
    ind_names: list,
    norm_values: dict,
    save_path: Optional[str] = None,
) -> None:
    """Радиальная (лепестковая) диаграмма: профиль показателей каждого образца."""
    N = len(ind_names)
    if N < 3:
        print(f'  [предупреждение] Радиальная диаграмма требует ≥ 3 показателей, получено {N}.')
        return

    angles        = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles_closed = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    colors  = plt.cm.tab10.colors

    for i, name in enumerate(names):
        vals = norm_values[name] + norm_values[name][:1]
        ax.plot(angles_closed, vals, 'o-', linewidth=1.8,
                color=colors[i % 10], label=name)
        ax.fill(angles_closed, vals, alpha=0.10, color=colors[i % 10])

    ax.set_xticks(angles)
    ax.set_xticklabels(ind_names, fontsize=9)
    ax.set_title(f'Профиль показателей — {group_name}', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15))
    plt.tight_layout()
    _save_or_show(fig, save_path, bbox_inches='tight')


def _save_or_show(fig, save_path, **kwargs):
    if save_path:
        fig.savefig(save_path, dpi=150, **kwargs)
        print(f'  Сохранено: {save_path}')
    else:
        plt.show()
    plt.close(fig)


# ─── convenience ────────────────────────────────────────────────────────────

def visualize_group(
    group_name: str,
    samples: list,
    specs: list,
    base_index: int = 0,
    exclude_binary: bool = False,
    save_dir: Optional[str] = None,
) -> None:
    """Строит обе диаграммы для группы объектов."""
    names, tech_levels, ind_names, norm_values = compute_relative_levels(
        samples, specs, base_index, exclude_binary,
    )
    base_name = samples[base_index].name
    slug      = group_name.lower().replace(' ', '_').replace('/', '_')

    bar_path = f'{save_dir}/{slug}_bar.png' if save_dir else None
    rad_path = f'{save_dir}/{slug}_radial.png' if save_dir else None

    create_bar_chart_relative(group_name, names, tech_levels, base_name, bar_path)
    create_radial_relative(group_name, names, ind_names, norm_values, rad_path)

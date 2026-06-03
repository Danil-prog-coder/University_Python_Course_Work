"""
Визуализация КТУ: радарные и столбчатые диаграммы по категориям.
"""

import math
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for environments without display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from analysis.technical_level import KTUResult


_COLORS = [
    "#2196F3", "#FF5722", "#4CAF50", "#9C27B0",
    "#FF9800", "#00BCD4", "#E91E63",
]


def plot_radar(results: list, title: str, save_path: str | None = None) -> None:
    """Radial (spider/radar) chart for a list of KTUResult objects."""
    if not results:
        return

    # Collect all unique labels (from first result — same class)
    labels = [ind.label for ind in results[0].indicators]
    N = len(labels)
    # Check all results have the same number of indicators
    if any(len(r.indicators) != N for r in results):
        # Mixed classes: fall back to bar which handles mixed counts
        plot_bar(results, title, save_path)
        return
    if N < 3:
        # Radar needs >= 3 axes; fall back to bar
        plot_bar(results, title, save_path)
        return

    angles = np.linspace(0, 2 * math.pi, N, endpoint=False).tolist()
    angles += angles[:1]  # close polygon

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"polar": True})
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=8)

    # Reference circle at 1.0
    ref_vals = [1.0] * N + [1.0]
    ax.plot(angles, ref_vals, "k--", linewidth=1, label="Эталон (1.0)")
    ax.fill(angles, ref_vals, alpha=0.05, color="gray")

    for idx, res in enumerate(results):
        vals = [ind.q_value for ind in res.indicators]
        vals += vals[:1]
        color = _COLORS[idx % len(_COLORS)]
        ax.plot(angles, vals, color=color, linewidth=2, label=f"{res.object_name}  T={res.total_T:.2f}")
        ax.fill(angles, vals, alpha=0.12, color=color)

    ax.set_title(title, pad=20, fontsize=12, fontweight="bold")
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=8)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=120, bbox_inches="tight")
        print(f"  Сохранено: {save_path}")
    else:
        plt.show()
    plt.close()


def plot_bar(results: list, title: str, save_path: str | None = None) -> None:
    """Grouped bar chart for a list of KTUResult objects."""
    if not results:
        return

    # Check if all results have same number of indicators (same class)
    first_N = len(results[0].indicators)
    mixed = any(len(r.indicators) != first_N for r in results)

    if mixed:
        # Mixed classes: one subplot per object
        n_objs = len(results)
        fig, axes = plt.subplots(1, n_objs, figsize=(max(6, n_objs * 5), 5))
        if n_objs == 1:
            axes = [axes]
        fig.suptitle(title, fontsize=12, fontweight="bold")
        for idx, (res, ax) in enumerate(zip(results, axes)):
            labels = [ind.label for ind in res.indicators]
            q_vals = [ind.q_value for ind in res.indicators]
            x = np.arange(len(labels))
            color = _COLORS[idx % len(_COLORS)]
            bars = ax.bar(x, q_vals, color=color, alpha=0.8, edgecolor="white")
            for bar, val in zip(bars, q_vals):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                        f"{val:.2f}", ha="center", va="bottom", fontsize=7)
            ax.axhline(y=1.0, color="black", linestyle="--", linewidth=1.0)
            ax.set_xticks(x)
            ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
            ax.set_title(f"{res.object_name}  T={res.total_T:.2f}", fontsize=9)
            ax.set_ylim(bottom=0)
        plt.tight_layout()
    else:
        labels = [ind.label for ind in results[0].indicators]
        N = len(labels)
        n_objs = len(results)
        x = np.arange(N)
        width = 0.8 / n_objs

        fig, ax = plt.subplots(figsize=(max(8, N * 1.5), 5))

        for idx, res in enumerate(results):
            q_vals = [ind.q_value for ind in res.indicators]
            offset = (idx - n_objs / 2 + 0.5) * width
            bars = ax.bar(x + offset, q_vals, width, label=f"{res.object_name}  T={res.total_T:.2f}",
                          color=_COLORS[idx % len(_COLORS)], alpha=0.8, edgecolor="white")
            for bar, val in zip(bars, q_vals):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                        f"{val:.2f}", ha="center", va="bottom", fontsize=7)

        # Reference line at 1.0
        ax.axhline(y=1.0, color="black", linestyle="--", linewidth=1.2, label="Эталон (1.0)")

        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
        ax.set_ylabel("q_i (относит. значение)", fontsize=10)
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.legend(fontsize=8)
        ax.set_ylim(bottom=0)

        plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=120, bbox_inches="tight")
        print(f"  Сохранено: {save_path}")
    else:
        plt.show()
    plt.close()


def show_category(
    category: str,
    results: list,
    chart_type: str = "radar",
    save_dir: str | None = None,
) -> None:
    """Show radar or bar chart for one category."""
    title = f"КТУ — {category}"
    save_path = None
    if save_dir:
        safe_name = category.replace(" ", "_").replace("/", "-")
        ext = "png"
        save_path = f"{save_dir}/{safe_name}_{chart_type}.{ext}"

    if chart_type == "bar":
        plot_bar(results, title, save_path)
    else:
        plot_radar(results, title, save_path)

"""
Анализ оптимальной закупки методами линейного программирования.

Задача: выбрать объёмы закупки x_i >= 0 у каждого из n поставщиков так,
чтобы при минимальных суммарных затратах обеспечить заданную целевую прибыль.

Целевая функция (минимизация затрат на закупку):
    min Z = sum_{i=1}^{n} c_i * x_i

Ограничение на прибыль (выручка − затраты >= целевая прибыль):
    sum_{i=1}^{n} (p − c_i) * x_i >= target_profit
    <=>  −sum_{i=1}^{n} (p − c_i) * x_i <= −target_profit   [форма для linprog]

Ограничения по ёмкости поставщиков:
    0 <= x_i <= cap_i

Решается тремя методами HiGHS (аналогично pt_7/Task17.ipynb):
    'highs'     — автовыбор (препроцессинг + симплекс или IPM)
    'highs-ds'  — двойственный симплекс
    'highs-ipm' — метод внутренней точки (барьерный)
"""
import time
from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy.optimize import linprog


@dataclass
class Supplier:
    name: str
    cost_per_unit: float
    max_capacity: float


@dataclass
class SupplierResult:
    name: str
    units: float
    cost_per_unit: float
    total_cost: float
    contribution_to_profit: float


@dataclass
class MethodResult:
    method: str
    success: bool
    total_cost: Optional[float]
    solve_time_ms: float


@dataclass
class PurchaseAnalysisResult:
    success: bool
    category: str
    selling_price: float
    target_profit: float
    total_units: float
    total_revenue: float
    total_cost: float
    actual_profit: float
    supplier_plan: list
    methods: list


class OptimalPurchaseAnalysis:
    """
    Решает задачу оптимальной закупки.
    Использует scipy.optimize.linprog (решатель HiGHS), аналогично pt_7/Task17.ipynb.
    """

    METHODS = ['highs', 'highs-ds', 'highs-ipm']

    def __init__(self, category: str, selling_price: float,
                 target_profit: float, suppliers: list) -> None:
        if selling_price <= 0:
            raise ValueError("Цена продажи должна быть положительной")
        if target_profit <= 0:
            raise ValueError("Целевая прибыль должна быть положительной")
        if not suppliers:
            raise ValueError("Список поставщиков не может быть пустым")
        self.category      = category
        self.selling_price = selling_price
        self.target_profit = target_profit
        self.suppliers     = suppliers

    def _build_lp(self):
        costs   = np.array([s.cost_per_unit for s in self.suppliers], dtype=np.float64)
        margins = self.selling_price - costs
        caps    = np.array([s.max_capacity  for s in self.suppliers], dtype=np.float64)
        # min sum(c_i * x_i)
        c_obj = costs.copy()
        # −sum(margin_i * x_i) <= −target_profit
        A_ub  = np.array([-margins], dtype=np.float64)
        b_ub  = np.array([-self.target_profit], dtype=np.float64)
        bounds = [(0.0, float(cap)) for cap in caps]
        return c_obj, A_ub, b_ub, bounds

    def _run_method(self, method, c_obj, A_ub, b_ub, bounds):
        t0  = time.perf_counter()
        res = linprog(c=c_obj, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method=method)
        dt  = (time.perf_counter() - t0) * 1000
        return MethodResult(
            method=method,
            success=res.success,
            total_cost=float(res.fun) if res.success else None,
            solve_time_ms=dt,
        ), res

    def analyze(self) -> PurchaseAnalysisResult:
        c_obj, A_ub, b_ub, bounds = self._build_lp()
        method_results = []
        primary_raw    = None

        for m in self.METHODS:
            mr, raw = self._run_method(m, c_obj, A_ub, b_ub, bounds)
            method_results.append(mr)
            if m == 'highs':
                primary_raw = raw

        if not primary_raw.success:
            return PurchaseAnalysisResult(
                success=False, category=self.category,
                selling_price=self.selling_price, target_profit=self.target_profit,
                total_units=0, total_revenue=0, total_cost=0, actual_profit=0,
                supplier_plan=[], methods=method_results,
            )

        x             = primary_raw.x
        total_cost    = float(np.dot(x, [s.cost_per_unit for s in self.suppliers]))
        total_units   = float(np.sum(x))
        total_revenue = self.selling_price * total_units
        actual_profit = total_revenue - total_cost

        plan = [
            SupplierResult(
                name=s.name, units=float(xi),
                cost_per_unit=s.cost_per_unit,
                total_cost=float(xi * s.cost_per_unit),
                contribution_to_profit=float(xi * (self.selling_price - s.cost_per_unit)),
            )
            for xi, s in zip(x, self.suppliers)
        ]

        return PurchaseAnalysisResult(
            success=True,
            category=self.category,
            selling_price=self.selling_price,
            target_profit=self.target_profit,
            total_units=total_units,
            total_revenue=total_revenue,
            total_cost=total_cost,
            actual_profit=actual_profit,
            supplier_plan=plan,
            methods=method_results,
        )

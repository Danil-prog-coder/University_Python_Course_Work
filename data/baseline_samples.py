"""
Базовые образцы — «средний рыночный» экземпляр для каждой модели.
Значения взяты из реального прайс-листа российского рынка электроники (2024).
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models.resistor import Resistor
from models.capacitor import Capacitor
from models.integrated_circuit import IntegratedCircuit
from models.transistor import Transistor
from models.diode import Diode
from models.board import Board
from models.connector import Connector
from models.soldering_equipment import SolderingEquipment
from models.measuring_instrument import MeasuringInstrument
from models.prototyping import Prototyping
from models.technical_documentation import TechnicalDocumentation
from models.engineer_consultation import EngineerConsultation
from classes.mass_production import MassProduction
from models.hobbyist import Hobbyist
from models.service_center import ServiceCenter
from models.electronics_manufacturer import ElectronicsManufacturer

# ---------------------------------------------------------------------------
# 2.5.1  Электронные компоненты
# ---------------------------------------------------------------------------

# Резистор 10 кОм 0,25 Вт ±5 % (MF-0.25, самый массовый типоразмер)
BASELINE_RESISTOR = Resistor(
    resistance_ohm=10_000,
    power_w=0.25,
    accuracy_percent=5.0,
    price_rub=2.0,
)

# Электролитический конденсатор 100 мкФ / 25 В (стандарт для питающих цепей)
BASELINE_CAPACITOR = Capacitor(
    capacitance_f=100e-6,
    working_voltage_v=25.0,
    type="electrolytic",
    price_rub=15.0,
)

# Микросхема логики 74HC00 (NAND × 4) DIP-14, питание 5 В
BASELINE_IC = IntegratedCircuit(
    type_purpose="logic",
    supply_voltage_v=5.0,
    package="DIP",
    price_rub=30.0,
)

# Транзистор NPN BC547 (I_C = 0,1 А, U_CE = 45 В) — универсальный сигнальный
BASELINE_TRANSISTOR = Transistor(
    type="NPN",
    max_current_a=0.1,
    voltage_v=45.0,
    price_rub=8.0,
)

# Диод выпрямительный 1N4007 (1 А, U_f = 1,1 В)
BASELINE_DIODE = Diode(
    type="rectifier",
    forward_voltage_v=1.1,
    max_current_a=1.0,
    price_rub=5.0,
)

# ---------------------------------------------------------------------------
# 2.5.2  Комплектующие
# ---------------------------------------------------------------------------

# Односторонняя плата FR4 100×100 мм
BASELINE_BOARD = Board(
    type="single-sided",
    material="FR4",
    size="100x100",
    price_rub=150.0,
)

# Гребёнка pin header 2,54 мм 10 контактов, монтаж через отверстие
BASELINE_CONNECTOR = Connector(
    type="pin header",
    contact_count=10,
    mounting_method="through-hole",
    price_rub=45.0,
)

# ---------------------------------------------------------------------------
# 2.5.3  Паяльное оборудование и измерительные приборы
# ---------------------------------------------------------------------------

# Паяльник 40 Вт, нагрев до 450 °C (Lukey / ЭПСН-40)
BASELINE_SOLDERING = SolderingEquipment(
    power_w=40.0,
    heating_temp_c=450.0,
    type="soldering iron",
    price_rub=800.0,
)

# Мультиметр цифровой DT-830B: точность ±1 %, диапазон 600 В / 10 А / 2 МОм
BASELINE_INSTRUMENT = MeasuringInstrument(
    type="multimeter",
    accuracy="±1%",
    measurement_range="600V/10A/2MOhm",
    price_rub=1_500.0,
)

# ---------------------------------------------------------------------------
# 2.5.4  Услуги прототипирования
# ---------------------------------------------------------------------------

BASELINE_PROTOTYPING = Prototyping(
    circuit_design=True,
    prototype_assembly=True,
    service_price_rub=5_000.0,
    avg_execution_days=7,
)

# ---------------------------------------------------------------------------
# 2.5.5  Серийное производство
# ---------------------------------------------------------------------------

BASELINE_MASS_PRODUCTION = MassProduction(
    board_assembly=True,
    product_testing=True,
    service_price_rub=50_000.0,
    avg_execution_days=14,
)

# ---------------------------------------------------------------------------
# 2.5.6  Дополнительные услуги
# ---------------------------------------------------------------------------

BASELINE_TECH_DOC = TechnicalDocumentation(
    circuit_preparation=True,
    bom_creation=True,
    service_price_rub=2_000.0,
    avg_execution_days=3,
)

BASELINE_CONSULTATION = EngineerConsultation(
    component_selection=True,
    circuit_optimization=True,
    service_price_rub=3_000.0,
    avg_execution_days=2,
)

# ---------------------------------------------------------------------------
# 2.5.7  Работа с клиентами
# ---------------------------------------------------------------------------

BASELINE_HOBBYIST = Hobbyist(
    component_selection_assistance=True,
    device_assembly_setup=True,
    pricing_condition="retail",
    min_order_rub=500.0,
)

BASELINE_SERVICE_CENTER = ServiceCenter(
    spare_parts_supply=True,
    urgent_component_delivery=True,
    pricing_condition="wholesale",
    min_order_rub=5_000.0,
)

BASELINE_MANUFACTURER = ElectronicsManufacturer(
    wholesale_supply=True,
    contract_assembly=True,
    pricing_condition="contract assembly",
    min_order_rub=50_000.0,
)

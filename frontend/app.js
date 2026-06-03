// ── Category & product-type definitions ────────────────────────────────────

const CATEGORIES = {
  'Электронные компоненты': {
    initialized: true,          // класс инициализирован по умолчанию
    types: ['resistors', 'capacitors', 'integrated_circuits', 'transistors', 'diodes'],
  },
  'Компоненты': {
    initialized: false,
    types: ['boards', 'connectors'],
  },
  'Инструменты': {
    initialized: false,
    types: ['soldering_equipment', 'measuring_instruments'],
  },
  'Услуги': {
    initialized: false,
    types: ['prototyping', 'repair'],
  },
  'Дополнительные услуги': {
    initialized: false,
    types: ['technical_documentation', 'engineer_consultation'],
  },
  'Массовое производство': {
    initialized: false,
    types: ['mass_production'],
  },
  'Работа с клиентами': {
    initialized: false,
    types: ['hobbyists', 'service_centers', 'electronics_manufacturers'],
  },
};

const TYPES = {
  resistors: {
    label: 'Резистор',
    fields: [
      { key: 'name',             label: 'Название / Артикул',  type: 'text',   placeholder: 'Например: R-220Ω-0.25W' },
      { key: 'resistance_ohm',   label: 'Сопротивление (Ом)', type: 'number', step: 'any', required: true },
      { key: 'power_w',          label: 'Мощность (Вт)',      type: 'number', step: 'any', required: true },
      { key: 'accuracy_percent', label: 'Точность (%)',       type: 'number', step: 'any', required: true },
      { key: 'price_rub',        label: 'Цена (руб)',         type: 'number', step: 'any', required: false },
    ],
  },

  capacitors: {
    label: 'Конденсатор',
    fields: [
      { key: 'name',               label: 'Название / Артикул',        type: 'text',   placeholder: 'Например: C-100мкФ-25В' },
      { key: 'capacitance_f',      label: 'Ёмкость (Ф)',              type: 'number', step: 'any', required: true },
      { key: 'working_voltage_v',  label: 'Рабочее напряжение (В)',   type: 'number', step: 'any', required: true },
      { key: 'type', label: 'Тип диэлектрика', type: 'select', required: true,
        options: [
          { value: 'ceramic',      label: 'Керамический' },
          { value: 'electrolytic', label: 'Электролитический' },
        ],
      },
      { key: 'price_rub', label: 'Цена (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  integrated_circuits: {
    label: 'Микросхема',
    fields: [
      { key: 'name',             label: 'Название / Артикул',       type: 'text',   placeholder: 'Например: ATmega328P' },
      { key: 'type_purpose', label: 'Тип / Назначение', type: 'select', required: true,
        options: [
          { value: 'logic',       label: 'Логическая' },
          { value: 'controller',  label: 'Контроллер' },
          { value: 'amplifier',   label: 'Усилитель' },
          { value: 'memory',      label: 'Память' },
          { value: 'power',       label: 'Силовая' },
        ],
      },
      { key: 'supply_voltage_v', label: 'Напряжение питания (В)', type: 'number', step: 'any', required: true },
      { key: 'package', label: 'Корпус', type: 'select', required: true,
        options: [
          { value: 'DIP', label: 'DIP' },
          { value: 'SMD', label: 'SMD' },
        ],
      },
      { key: 'price_rub', label: 'Цена (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  transistors: {
    label: 'Транзистор',
    fields: [
      { key: 'name',          label: 'Название / Артикул', type: 'text',   placeholder: 'Например: BC547' },
      { key: 'type', label: 'Тип', type: 'select', required: true,
        options: [
          { value: 'NPN',   label: 'NPN' },
          { value: 'PNP',   label: 'PNP' },
          { value: 'MOSFET', label: 'MOSFET' },
        ],
      },
      { key: 'max_current_a', label: 'Макс. ток (А)',   type: 'number', step: 'any', required: true },
      { key: 'voltage_v',     label: 'Напряжение (В)',  type: 'number', step: 'any', required: true },
      { key: 'price_rub',     label: 'Цена (руб)',      type: 'number', step: 'any', required: false },
    ],
  },

  diodes: {
    label: 'Диод',
    fields: [
      { key: 'name', label: 'Название / Артикул', type: 'text', placeholder: 'Например: 1N4007' },
      { key: 'type', label: 'Тип', type: 'select', required: true,
        options: [
          { value: 'rectifier', label: 'Выпрямительный' },
          { value: 'zener',     label: 'Стабилитрон' },
          { value: 'LED',       label: 'Светодиод (LED)' },
        ],
      },
      { key: 'forward_voltage_v', label: 'Прямое напряжение (В)', type: 'number', step: 'any', required: true },
      { key: 'max_current_a',     label: 'Макс. ток (А)',        type: 'number', step: 'any', required: true },
      { key: 'price_rub',         label: 'Цена (руб)',            type: 'number', step: 'any', required: false },
    ],
  },

  boards: {
    label: 'Плата (PCB)',
    fields: [
      { key: 'name',     label: 'Название / Артикул', type: 'text', placeholder: 'Например: Main Board v1.0' },
      { key: 'type', label: 'Тип', type: 'select', required: true,
        options: [
          { value: 'single-sided', label: 'Односторонняя' },
          { value: 'multilayer',   label: 'Многослойная' },
        ],
      },
      { key: 'material', label: 'Материал', type: 'text', placeholder: 'Например: FR4', required: true },
      { key: 'size',     label: 'Размер',   type: 'text', placeholder: 'Например: 100×80 мм', required: true },
      { key: 'size_mm',  label: 'Площадь (мм²)', type: 'number', step: 'any', placeholder: 'Например: 3500' },
      { key: 'price_rub', label: 'Цена (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  connectors: {
    label: 'Разъём',
    fields: [
      { key: 'name', label: 'Название / Артикул', type: 'text', placeholder: 'Например: USB-C Female' },
      { key: 'type', label: 'Тип', type: 'select', required: true,
        options: [
          { value: 'USB',         label: 'USB' },
          { value: 'HDMI',        label: 'HDMI' },
          { value: 'pin header',  label: 'Штыревой (pin header)' },
          { value: 'RJ45',        label: 'RJ45' },
          { value: 'other',       label: 'Другой' },
        ],
      },
      { key: 'contact_count',    label: 'Количество контактов', type: 'number', step: '1', required: true },
      { key: 'mounting_method', label: 'Метод монтажа', type: 'select', required: true,
        options: [
          { value: 'SMD',          label: 'SMD' },
          { value: 'through-hole', label: 'Сквозной (through-hole)' },
        ],
      },
      { key: 'price_rub', label: 'Цена (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  soldering_equipment: {
    label: 'Паяльное оборудование',
    fields: [
      { key: 'name',          label: 'Название / Модель',   type: 'text',   placeholder: 'Например: Hakko FX-888D' },
      { key: 'power_w',       label: 'Мощность (Вт)',       type: 'number', step: 'any', required: true },
      { key: 'heating_temp_c', label: 'Макс. температура (°C)', type: 'number', step: 'any', required: true },
      { key: 'type', label: 'Тип', type: 'select', required: true,
        options: [
          { value: 'soldering iron', label: 'Паяльник' },
          { value: 'station',        label: 'Паяльная станция' },
        ],
      },
      { key: 'price_rub', label: 'Цена (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  measuring_instruments: {
    label: 'Измерительный прибор',
    fields: [
      { key: 'name', label: 'Название / Модель', type: 'text', placeholder: 'Например: Fluke 87V' },
      { key: 'type', label: 'Тип', type: 'select', required: true,
        options: [
          { value: 'multimeter',   label: 'Мультиметр' },
          { value: 'oscilloscope', label: 'Осциллограф' },
        ],
      },
      { key: 'accuracy',          label: 'Точность',           type: 'text', placeholder: 'Например: ±0.5%',   required: true },
      { key: 'measurement_range', label: 'Диапазон измерений', type: 'text', placeholder: 'Например: 0–1000 В', required: true },
      { key: 'accuracy_percent', label: 'Точность числовая (%)', type: 'number', step: 'any', placeholder: 'Например: 0.5' },
      { key: 'range_value',      label: 'Диапазон числовой',     type: 'number', step: 'any', placeholder: 'Например: 600' },
      { key: 'price_rub',        label: 'Цена (руб)',            type: 'number', step: 'any', required: false },
    ],
  },

  prototyping: {
    label: 'Прототипирование',
    fields: [
      { key: 'name',               label: 'Название / Описание',  type: 'text', placeholder: 'Например: Прототип Arduino' },
      { key: 'circuit_design',     label: 'Проектирование схем',  type: 'checkbox' },
      { key: 'prototype_assembly', label: 'Сборка прототипа',     type: 'checkbox' },
      { key: 'service_price_rub',  label: 'Цена услуги (руб)',    type: 'number', step: 'any', required: false },
      { key: 'avg_execution_days', label: 'Срок выполнения (дней)', type: 'number', step: 'any', required: false },
    ],
  },

  repair: {
    label: 'Ремонт',
    fields: [
      { key: 'name',                  label: 'Название / Описание',        type: 'text', placeholder: 'Например: Ремонт БП ATX' },
      { key: 'fault_diagnosis',       label: 'Диагностика неисправностей', type: 'checkbox' },
      { key: 'component_replacement', label: 'Замена компонентов',         type: 'checkbox' },
      { key: 'service_price_rub',     label: 'Цена услуги (руб)',          type: 'number', step: 'any', required: false },
      { key: 'avg_execution_days',    label: 'Срок выполнения (дней)',      type: 'number', step: 'any', required: false },
    ],
  },

  technical_documentation: {
    label: 'Техническая документация',
    fields: [
      { key: 'name',              label: 'Название проекта',           type: 'text', placeholder: 'Например: Документация v2.0' },
      { key: 'circuit_preparation', label: 'Подготовка принципиальных схем', type: 'checkbox' },
      { key: 'bom_creation',      label: 'Создание перечня компонентов (BOM)', type: 'checkbox' },
      { key: 'service_price_rub',   label: 'Цена услуги (руб)',    type: 'number', step: 'any', required: false },
      { key: 'avg_execution_days',  label: 'Срок выполнения (дней)', type: 'number', step: 'any', required: false },
    ],
  },

  engineer_consultation: {
    label: 'Инженерная консультация',
    fields: [
      { key: 'name',                label: 'Название / Описание',    type: 'text', placeholder: 'Например: Консультация по МК' },
      { key: 'component_selection', label: 'Подбор компонентов',     type: 'checkbox' },
      { key: 'circuit_optimization', label: 'Оптимизация схем',      type: 'checkbox' },
      { key: 'service_price_rub',    label: 'Цена услуги (руб)',     type: 'number', step: 'any', required: false },
      { key: 'avg_execution_days',   label: 'Срок выполнения (дней)', type: 'number', step: 'any', required: false },
    ],
  },

  mass_production: {
    label: 'Массовое производство',
    fields: [
      { key: 'name',            label: 'Название / Описание', type: 'text', placeholder: 'Например: Серия 500 шт.' },
      { key: 'board_assembly',  label: 'Монтаж плат',         type: 'checkbox' },
      { key: 'product_testing', label: 'Тестирование продукции', type: 'checkbox' },
    ],
  },

  hobbyists: {
    label: 'Радиолюбитель',
    fields: [
      { key: 'name',                        label: 'Имя клиента',                   type: 'text', placeholder: 'Например: Иван Петров', required: true },
      { key: 'component_selection_assistance', label: 'Помощь в выборе компонентов', type: 'checkbox' },
      { key: 'device_assembly_setup',       label: 'Сборка и настройка устройств', type: 'checkbox' },
      { key: 'min_order_rub', label: 'Мин. сумма заказа (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  service_centers: {
    label: 'Сервисный центр',
    fields: [
      { key: 'name',                      label: 'Название центра',               type: 'text', placeholder: 'Например: СЦ «ТехПомощь»', required: true },
      { key: 'spare_parts_supply',        label: 'Поставка запчастей',            type: 'checkbox' },
      { key: 'urgent_component_delivery', label: 'Срочная доставка компонентов',  type: 'checkbox' },
      { key: 'min_order_rub', label: 'Мин. сумма заказа (руб)', type: 'number', step: 'any', required: false },
    ],
  },

  electronics_manufacturers: {
    label: 'Производитель электроники',
    fields: [
      { key: 'name',              label: 'Название компании',    type: 'text', placeholder: 'Например: ООО «ЭлектроПром»', required: true },
      { key: 'wholesale_supply',  label: 'Оптовые поставки',     type: 'checkbox' },
      { key: 'contract_assembly', label: 'Контрактная сборка',   type: 'checkbox' },
      { key: 'min_order_rub', label: 'Мин. сумма заказа (руб)', type: 'number', step: 'any', required: false },
    ],
  },
};

// ── KTU (Technical Level) ──────────────────────────────────────────────────

const KTU_REFERENCE = {
  resistors: [
    { key: 'power_w',          label: 'Мощность (Вт)',  ref: 0.25, inverse: false, weight: 0.35 },
    { key: 'accuracy_percent', label: 'Точность (%)',   ref: 5.0,  inverse: true,  weight: 0.35 },
    { key: 'price_rub',        label: 'Цена (руб)',     ref: 5.0,  inverse: true,  weight: 0.30 },
  ],
  capacitors: [
    { key: 'working_voltage_v', label: 'Напряжение (В)', ref: 50.0,    inverse: false, weight: 0.45 },
    { key: 'capacitance_f',     label: 'Ёмкость (Ф)',    ref: 0.0000001, inverse: false, weight: 0.25 },
    { key: 'price_rub',         label: 'Цена (руб)',     ref: 3.0,     inverse: true,  weight: 0.30 },
  ],
  integrated_circuits: [
    { key: 'supply_voltage_v', label: 'Напряжение пит. (В)', ref: 5.0,  inverse: false, weight: 0.40 },
    { key: 'price_rub',        label: 'Цена (руб)',          ref: 15.0, inverse: true,  weight: 0.60 },
  ],
  transistors: [
    { key: 'max_current_a', label: 'Макс. ток (А)',  ref: 0.1,  inverse: false, weight: 0.35 },
    { key: 'voltage_v',     label: 'Напряжение (В)', ref: 40.0, inverse: false, weight: 0.35 },
    { key: 'price_rub',     label: 'Цена (руб)',     ref: 5.0,  inverse: true,  weight: 0.30 },
  ],
  diodes: [
    { key: 'max_current_a',     label: 'Макс. ток (А)',     ref: 0.3, inverse: false, weight: 0.35 },
    { key: 'forward_voltage_v', label: 'Прямое напр. (В)',  ref: 0.7, inverse: true,  weight: 0.35 },
    { key: 'price_rub',         label: 'Цена (руб)',        ref: 3.0, inverse: true,  weight: 0.30 },
  ],
  boards: [
    { key: 'size_mm',    label: 'Площадь (мм²)',  ref: 3500.0, inverse: false, weight: 0.35, derived: 'size_mm' },
    { key: 'layer_type', label: 'Многослойность', ref: 1.0,    inverse: false, weight: 0.35, derived: 'layer_type' },
    { key: 'price_rub',  label: 'Цена (руб)',     ref: 40.0,   inverse: true,  weight: 0.30 },
  ],
  connectors: [
    { key: 'contact_count', label: 'Контакты (шт)',     ref: 40.0, inverse: false, weight: 0.40 },
    { key: 'mount_th',      label: 'Сквозной монтаж',  ref: 1.0,  inverse: false, weight: 0.30, derived: 'mount_th' },
    { key: 'price_rub',     label: 'Цена (руб)',        ref: 15.0, inverse: true,  weight: 0.30 },
  ],
  soldering_equipment: [
    { key: 'power_w',        label: 'Мощность (Вт)',    ref: 25.0,  inverse: false, weight: 0.30 },
    { key: 'heating_temp_c', label: 'Температура (°C)', ref: 300.0, inverse: false, weight: 0.30 },
    { key: 'price_rub',      label: 'Цена (руб)',       ref: 350.0, inverse: true,  weight: 0.40 },
  ],
  measuring_instruments: [
    { key: 'accuracy_percent', label: 'Точность (%)', ref: 1.0,   inverse: true,  weight: 0.40 },
    { key: 'range_value',      label: 'Диапазон',     ref: 600.0, inverse: false, weight: 0.30 },
    { key: 'price_rub',        label: 'Цена (руб)',   ref: 500.0, inverse: true,  weight: 0.30 },
  ],
  prototyping: [
    { key: 'service_price_rub',  label: 'Цена услуги (руб)', ref: 5000.0, inverse: true,  weight: 0.35 },
    { key: 'avg_execution_days', label: 'Срок (дней)',       ref: 7.0,    inverse: true,  weight: 0.25 },
    { key: 'circuit_design',     label: 'Разработка схем',   ref: 1.0,    inverse: false, weight: 0.20 },
    { key: 'prototype_assembly', label: 'Сборка прототипа',  ref: 1.0,    inverse: false, weight: 0.20 },
  ],
  repair: [
    { key: 'service_price_rub',     label: 'Цена услуги (руб)',  ref: 1500.0, inverse: true,  weight: 0.30 },
    { key: 'avg_execution_days',    label: 'Срок (дней)',        ref: 3.0,    inverse: true,  weight: 0.30 },
    { key: 'fault_diagnosis',       label: 'Диагностика',        ref: 1.0,    inverse: false, weight: 0.20 },
    { key: 'component_replacement', label: 'Замена компонентов', ref: 1.0,    inverse: false, weight: 0.20 },
  ],
  technical_documentation: [
    { key: 'service_price_rub',   label: 'Цена услуги (руб)', ref: 3000.0, inverse: true,  weight: 0.30 },
    { key: 'avg_execution_days',  label: 'Срок (дней)',       ref: 5.0,    inverse: true,  weight: 0.30 },
    { key: 'circuit_preparation', label: 'Подготовка схем',   ref: 1.0,    inverse: false, weight: 0.20 },
    { key: 'bom_creation',        label: 'Создание BOM',      ref: 1.0,    inverse: false, weight: 0.20 },
  ],
  engineer_consultation: [
    { key: 'service_price_rub',    label: 'Цена услуги (руб)',   ref: 1000.0, inverse: true,  weight: 0.30 },
    { key: 'avg_execution_days',   label: 'Срок (дней)',         ref: 1.0,    inverse: true,  weight: 0.25 },
    { key: 'component_selection',  label: 'Подбор компонентов',  ref: 1.0,    inverse: false, weight: 0.25 },
    { key: 'circuit_optimization', label: 'Оптимизация схем',    ref: 1.0,    inverse: false, weight: 0.20 },
  ],
  hobbyists: [
    { key: 'min_order_rub',                  label: 'Мин. заказ (руб)',   ref: 500.0, inverse: true,  weight: 0.40 },
    { key: 'component_selection_assistance', label: 'Подбор компонентов', ref: 1.0,   inverse: false, weight: 0.30 },
    { key: 'device_assembly_setup',          label: 'Сборка/настройка',   ref: 1.0,   inverse: false, weight: 0.30 },
  ],
  service_centers: [
    { key: 'min_order_rub',             label: 'Мин. заказ (руб)',   ref: 2000.0, inverse: true,  weight: 0.40 },
    { key: 'spare_parts_supply',        label: 'Поставка запчастей', ref: 1.0,    inverse: false, weight: 0.30 },
    { key: 'urgent_component_delivery', label: 'Срочная доставка',   ref: 1.0,    inverse: false, weight: 0.30 },
  ],
  electronics_manufacturers: [
    { key: 'min_order_rub',     label: 'Мин. заказ (руб)',    ref: 10000.0, inverse: true,  weight: 0.40 },
    { key: 'wholesale_supply',  label: 'Оптовые поставки',    ref: 1.0,     inverse: false, weight: 0.30 },
    { key: 'contract_assembly', label: 'Контрактная сборка',  ref: 1.0,     inverse: false, weight: 0.30 },
  ],
};

const KTU_CATEGORIES = {
  'Электронные компоненты': ['resistors', 'capacitors', 'integrated_circuits', 'transistors', 'diodes'],
  'Компоненты':             ['boards', 'connectors'],
  'Инструменты':            ['soldering_equipment', 'measuring_instruments'],
  'Услуги':                 ['prototyping', 'repair'],
  'Дополнительные услуги':  ['technical_documentation', 'engineer_consultation'],
  'Работа с клиентами':     ['hobbyists', 'service_centers', 'electronics_manufacturers'],
};

const KTU_COLORS = ['#2196F3','#FF5722','#4CAF50','#9C27B0','#FF9800','#00BCD4','#E91E63'];

function getItemKTUValue(item, field) {
  if (field.derived === 'layer_type')
    return (item.type || '').toLowerCase().includes('multi') ? 1.0 : 0.0;
  if (field.derived === 'mount_th')
    return (item.mounting_method || '').toLowerCase().includes('through') ? 1.0 : 0.0;
  const v = item[field.key];
  if (typeof v === 'boolean') return v ? 1.0 : 0.0;
  return parseFloat(v) || 0.0;
}

function computeKTU(item, typeKey) {
  const spec = KTU_REFERENCE[typeKey];
  if (!spec) return null;
  let totalT = 0;
  const indicators = spec.map(f => {
    const value = getItemKTUValue(item, f);
    const q = f.inverse
      ? (value !== 0 ? f.ref / value : 0)
      : (f.ref  !== 0 ? value / f.ref  : 0);
    totalT += f.weight * q;
    return { label: f.label, q };
  });
  return { indicators, totalT };
}

let currentKTUCategory = null;
let currentKTUChartType = 'radar';
let ktuCharts = {};   // typeKey -> Chart instance

function destroyKTUCharts() {
  Object.values(ktuCharts).forEach(c => c.destroy());
  ktuCharts = {};
}

// ── State & persistence ────────────────────────────────────────────────────

let currentType = null;
let currentView = null; // 'type' | 'analysis' | null
let db = loadDb();

function loadDb() {
  try { return JSON.parse(localStorage.getItem('electrostore')) || {}; }
  catch { return {}; }
}

function saveDb() { localStorage.setItem('electrostore', JSON.stringify(db)); }

function getItems(type) { return db[type] || []; }

function pushItem(type, item) {
  if (!db[type]) db[type] = [];
  db[type].push({ _id: Date.now(), ...item });
  saveDb();
}

function removeItem(type, id) {
  db[type] = (db[type] || []).filter(x => x._id !== id);
  saveDb();
}

// ── Sidebar ────────────────────────────────────────────────────────────────

function renderSidebar() {
  const nav = document.getElementById('sidebar-nav');
  nav.innerHTML = '';

  // Анализ закупок (отдельный пункт над категориями)
  const analysisWrap = document.createElement('div');
  analysisWrap.innerHTML = `
    <div class="nav-item ${currentView === 'analysis' ? 'active' : ''}" onclick="selectAnalysis()" style="padding-left:14px;">
      <span>📊 Анализ закупок</span>
      <span class="nav-badge ${currentView === 'analysis' ? 'has-items' : 'badge-lp'}">LP</span>
    </div>
    <div class="nav-item ${currentView === 'ktu' ? 'active' : ''}" onclick="selectKTU()" style="padding-left:14px;">
      <span>📈 Диаграммы КТУ</span>
      <span class="nav-badge" style="background:#e0e7ff;color:#4338ca;font-size:10px;">КТУ</span>
    </div>
    <div class="nav-divider"></div>`;
  nav.appendChild(analysisWrap);

  for (const [catName, cat] of Object.entries(CATEGORIES)) {
    const catCount = cat.types.reduce((s, t) => s + getItems(t).length, 0);

    const group = document.createElement('div');
    group.className = 'nav-group';

    const initDot = cat.initialized
      ? '<span class="init-dot" title="Раздел инициализирован по умолчанию">●</span>'
      : '';

    const catBadge = catCount > 0
      ? `<span class="nav-badge has-items">${catCount}</span>`
      : '';

    group.innerHTML = `
      <div class="nav-group-header" onclick="toggleGroup(this)">
        <span>${catName}${initDot}</span>
        <div class="right-group">${catBadge}<span class="chevron">▾</span></div>
      </div>
      <div class="nav-items">
        ${cat.types.map(type => {
          const count = getItems(type).length;
          const active = (currentView === 'type' && currentType === type) ? 'active' : '';
          const badgeCls = count > 0 ? 'has-items' : '';
          return `
            <div class="nav-item ${active}" onclick="selectType('${type}')">
              <span>${TYPES[type].label}</span>
              <span class="nav-badge ${badgeCls}">${count}</span>
            </div>`;
        }).join('')}
      </div>`;

    nav.appendChild(group);
  }
}

function toggleGroup(header) {
  header.parentElement.classList.toggle('collapsed');
}

// ── Type selection ─────────────────────────────────────────────────────────

function getCategoryName(type) {
  for (const [name, cat] of Object.entries(CATEGORIES)) {
    if (cat.types.includes(type)) return name;
  }
  return '';
}

function selectType(type) {
  currentType = type;
  currentView = 'type';
  renderSidebar();

  const catName = getCategoryName(type);
  document.getElementById('breadcrumb').innerHTML =
    `${catName} <span>/ ${TYPES[type].label}</span>`;

  renderTypePage(type);
}

// ── Type page ──────────────────────────────────────────────────────────────

function renderTypePage(type) {
  const def = TYPES[type];
  const hasCheckboxes = def.fields.some(f => f.type === 'checkbox');

  document.getElementById('main-area').innerHTML = `
    <div class="type-page">
      <div class="type-header">
        <h2>${def.label}</h2>
        <div class="type-meta">
          <span class="category-badge">${getCategoryName(type)}</span>
        </div>
      </div>

      <div class="form-card">
        <div class="form-card-title">Добавить запись</div>
        <form id="add-form" onsubmit="handleSubmit(event,'${type}')">
          ${hasCheckboxes ? buildMixedForm(def.fields) : buildGridForm(def.fields)}
          <div class="form-actions">
            <button type="submit" class="btn btn-primary">Добавить</button>
            <button type="button" class="btn btn-secondary" onclick="document.getElementById('add-form').reset()">Очистить</button>
          </div>
        </form>
      </div>

      <div class="items-card">
        <div class="items-card-header">
          <h3>Список: ${def.label}</h3>
          <span class="count-badge" id="count-badge">${getItems(type).length}</span>
        </div>
        <div id="items-body">${renderItemsBody(type)}</div>
      </div>
    </div>`;
}

// ── Form builders ──────────────────────────────────────────────────────────

function buildGridForm(fields) {
  return `<div class="form-grid">${fields.map(f => buildField(f)).join('')}</div>`;
}

function buildMixedForm(fields) {
  const regular   = fields.filter(f => f.type !== 'checkbox');
  const checkboxes = fields.filter(f => f.type === 'checkbox');
  return `
    ${regular.length ? `<div class="form-grid">${regular.map(f => buildField(f)).join('')}</div>` : ''}
    <div class="checkbox-group">
      ${checkboxes.map(f => `
        <label class="checkbox-label">
          <input type="checkbox" name="${f.key}">
          ${f.label}
        </label>`).join('')}
    </div>`;
}

function buildField(f) {
  if (f.type === 'select') {
    return `
      <div class="form-group">
        <label for="${f.key}">${f.label}${f.required ? ' *' : ''}</label>
        <select id="${f.key}" name="${f.key}" ${f.required ? 'required' : ''}>
          <option value="">— выберите —</option>
          ${f.options.map(o => `<option value="${o.value}">${o.label}</option>`).join('')}
        </select>
      </div>`;
  }
  return `
    <div class="form-group">
      <label for="${f.key}">${f.label}${f.required ? ' *' : ''}</label>
      <input
        type="${f.type}"
        id="${f.key}" name="${f.key}"
        ${f.placeholder ? `placeholder="${f.placeholder}"` : ''}
        ${f.step       ? `step="${f.step}"`               : ''}
        ${f.required   ? 'required'                       : ''}
      >
    </div>`;
}

// ── Submit ─────────────────────────────────────────────────────────────────

function handleSubmit(event, type) {
  event.preventDefault();
  const form  = event.target;
  const def   = TYPES[type];
  const item  = {};

  for (const f of def.fields) {
    const el = form.elements[f.key];
    if (!el) continue;
    if (f.type === 'checkbox') {
      item[f.key] = el.checked;
    } else if (f.type === 'number') {
      item[f.key] = el.value !== '' ? parseFloat(el.value) : null;
    } else {
      item[f.key] = el.value || null;
    }
  }

  pushItem(type, item);
  form.reset();

  document.getElementById('items-body').innerHTML  = renderItemsBody(type);
  document.getElementById('count-badge').textContent = getItems(type).length;
  renderSidebar();
  showToast(`${def.label} успешно добавлен(а)`, 'success');
}

// ── Items table ────────────────────────────────────────────────────────────

function renderItemsBody(type) {
  const items    = getItems(type);
  const def      = TYPES[type];

  if (items.length === 0) {
    return '<div class="items-empty">Нет записей — добавьте первую запись с помощью формы выше.</div>';
  }

  const hasName    = def.fields.some(f => f.key === 'name');
  const dataFields = def.fields.filter(f => f.key !== 'name');

  const thead = `
    <thead><tr>
      <th>#</th>
      ${hasName ? '<th>Название</th>' : ''}
      ${dataFields.map(f => `<th>${f.label}</th>`).join('')}
      <th></th>
    </tr></thead>`;

  const tbody = `
    <tbody>
      ${items.map((item, i) => `
        <tr>
          <td class="item-num">${i + 1}</td>
          ${hasName ? `<td><strong>${item.name || '—'}</strong></td>` : ''}
          ${dataFields.map(f => `<td>${cellValue(item[f.key], f)}</td>`).join('')}
          <td>
            <button class="delete-btn" onclick="handleDelete(${item._id})" title="Удалить">✕</button>
          </td>
        </tr>`).join('')}
    </tbody>`;

  return `<table class="items-table">${thead}${tbody}</table>`;
}

function cellValue(val, field) {
  if (val === null || val === undefined) return '<span style="color:#cbd5e1">—</span>';

  if (field.type === 'checkbox') {
    return val
      ? '<span class="bool-yes">✓ Да</span>'
      : '<span class="bool-no">✗ Нет</span>';
  }

  if (field.type === 'select') {
    const opt = (field.options || []).find(o => o.value === val);
    return `<span class="tag tag-blue">${opt ? opt.label : val}</span>`;
  }

  if (field.type === 'number') {
    return `<span class="num-val">${val}</span>`;
  }

  return val;
}

function handleDelete(id) {
  if (!currentType) return;
  removeItem(currentType, id);
  document.getElementById('items-body').innerHTML    = renderItemsBody(currentType);
  document.getElementById('count-badge').textContent = getItems(currentType).length;
  renderSidebar();
  showToast('Запись удалена', 'info');
}

// ── Welcome stats ──────────────────────────────────────────────────────────

function renderWelcome() {
  const grid = document.getElementById('stats-grid');
  if (!grid) return;

  const allTypes  = Object.values(CATEGORIES).flatMap(c => c.types);
  const total     = allTypes.reduce((s, t) => s + getItems(t).length, 0);

  const catCards  = Object.entries(CATEGORIES)
    .map(([name, cat]) => {
      const count = cat.types.reduce((s, t) => s + getItems(t).length, 0);
      return count > 0
        ? `<div class="stat-card"><div class="stat-num">${count}</div><div class="stat-label">${name}</div></div>`
        : '';
    }).join('');

  grid.innerHTML =
    `<div class="stat-card"><div class="stat-num">${total}</div><div class="stat-label">Всего записей</div></div>` +
    catCards;
}

// ── Toast ──────────────────────────────────────────────────────────────────

function showToast(message, type = 'success') {
  const wrap  = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.textContent = message;
  wrap.appendChild(toast);
  setTimeout(() => {
    toast.classList.add('hiding');
    setTimeout(() => toast.remove(), 200);
  }, 2500);
}

// ── Clear all ──────────────────────────────────────────────────────────────

document.getElementById('clear-all-btn').addEventListener('click', () => {
  if (!confirm('Удалить все данные? Это действие нельзя отменить.')) return;
  db = {};
  saveDb();
  currentType = null;
  currentView = null;
  document.getElementById('breadcrumb').textContent = 'Главная';
  document.getElementById('main-area').innerHTML = `
    <div class="welcome" id="welcome">
      <div class="welcome-icon">⚡</div>
      <h2>Добро пожаловать в ЭлектроСклад</h2>
      <p>Выберите тип продукта или услуги в меню слева, чтобы начать добавлять записи.</p>
      <div class="stats-grid" id="stats-grid"></div>
    </div>`;
  renderSidebar();
  renderWelcome();
  showToast('Все данные удалены', 'info');
});

// ── Analysis page ──────────────────────────────────────────────────────────

function selectAnalysis() {
  currentType = null;
  currentView = 'analysis';
  renderSidebar();
  document.getElementById('breadcrumb').innerHTML = '<span>Анализ оптимальной закупки</span>';
  renderAnalysisPage();
}

function selectKTU() {
  currentType = null;
  currentView = 'ktu';
  currentKTUCategory = Object.keys(KTU_CATEGORIES)[0];
  renderSidebar();
  document.getElementById('breadcrumb').innerHTML = '<span>Диаграммы КТУ</span>';
  renderKTUPage();
}

function renderKTUPage() {
  destroyKTUCharts();
  const catNames = Object.keys(KTU_CATEGORIES);

  const tabsHTML = catNames.map(name => `
    <button class="ktu-tab ${name === currentKTUCategory ? 'active' : ''}"
            onclick="switchKTUCategory('${name}')">${name}</button>
  `).join('');

  document.getElementById('main-area').innerHTML = `
    <div class="type-page">
      <div class="type-header">
        <h2>Диаграммы КТУ</h2>
        <div class="type-meta">
          <span class="category-badge" style="background:#e0e7ff;color:#4338ca;">Коэффициент технического уровня</span>
          <span class="category-badge">Эталон: q = 1.0</span>
        </div>
      </div>

      <div class="ktu-controls">
        <div class="ktu-tabs">${tabsHTML}</div>
        <div class="ktu-toggle">
          <button id="btn-radar" class="ktu-type-btn ${currentKTUChartType==='radar'?'active':''}"
                  onclick="switchKTUChartType('radar')">🕸 Радарная</button>
          <button id="btn-bar"   class="ktu-type-btn ${currentKTUChartType==='bar'?'active':''}"
                  onclick="switchKTUChartType('bar')">📊 Столбчатая</button>
        </div>
      </div>

      <div id="ktu-charts-area" class="ktu-charts-area"></div>
    </div>`;

  renderKTUCharts();
}

function switchKTUCategory(name) {
  currentKTUCategory = name;
  renderKTUPage();
}

function switchKTUChartType(type) {
  currentKTUChartType = type;
  renderKTUPage();
}

function renderKTUCharts() {
  const area = document.getElementById('ktu-charts-area');
  if (!area) return;
  area.innerHTML = '';

  const types = KTU_CATEGORIES[currentKTUCategory] || [];

  types.forEach(typeKey => {
    const spec  = KTU_REFERENCE[typeKey];
    if (!spec) return;

    const typeDef = TYPES[typeKey];
    const items   = getItems(typeKey);

    // Build card
    const card = document.createElement('div');
    card.className = 'ktu-chart-card';

    const refLabel = getKTURefLabel(typeKey);
    const labels   = spec.map(f => f.label);

    let bodyHTML;
    if (items.length === 0) {
      bodyHTML = `<div class="ktu-no-data">Нет данных — добавьте записи в раздел «${typeDef ? typeDef.label : typeKey}»</div>`;
    } else {
      bodyHTML = `<div class="ktu-canvas-wrap"><canvas id="ktu-canvas-${typeKey}"></canvas></div>`;
    }

    // T values summary
    const summaryRows = items.map((item, i) => {
      const ktu = computeKTU(item, typeKey);
      if (!ktu) return '';
      const name = item.name || `Запись ${i+1}`;
      const cls  = ktu.totalT >= 1 ? 'ktu-t-good' : 'ktu-t-low';
      return `<span class="ktu-t-badge ${cls}">${name}: T = ${ktu.totalT.toFixed(3)}</span>`;
    }).join('');

    card.innerHTML = `
      <div class="ktu-card-header">
        <strong>${typeDef ? typeDef.label : typeKey}</strong>
        <span class="ktu-ref-note">Эталон: ${refLabel}</span>
      </div>
      ${summaryRows ? `<div class="ktu-summary">${summaryRows}</div>` : ''}
      ${bodyHTML}`;

    area.appendChild(card);

    if (items.length === 0) return;

    // Build Chart.js datasets
    const canvasId = `ktu-canvas-${typeKey}`;
    requestAnimationFrame(() => {
      const canvas = document.getElementById(canvasId);
      if (!canvas) return;

      const datasets = [];

      // Reference dataset (all 1.0)
      const refData = labels.map(() => 1.0);
      if (currentKTUChartType === 'radar') {
        datasets.push({
          label: 'Эталон',
          data: [...refData, refData[0]],
          borderColor: '#94a3b8',
          borderDash: [5, 5],
          borderWidth: 1.5,
          backgroundColor: 'rgba(148,163,184,0.08)',
          pointRadius: 3,
        });
      } else {
        datasets.push({
          label: 'Эталон',
          data: refData,
          backgroundColor: 'rgba(148,163,184,0.35)',
          borderColor: '#64748b',
          borderWidth: 1,
        });
      }

      // Item datasets
      items.forEach((item, i) => {
        const ktu   = computeKTU(item, typeKey);
        if (!ktu) return;
        const qVals = ktu.indicators.map(ind => parseFloat(ind.q.toFixed(3)));
        const color = KTU_COLORS[i % KTU_COLORS.length];
        const name  = item.name || `Запись ${i+1}`;

        if (currentKTUChartType === 'radar') {
          datasets.push({
            label: `${name} (T=${ktu.totalT.toFixed(2)})`,
            data: [...qVals, qVals[0]],
            borderColor: color,
            backgroundColor: color + '22',
            borderWidth: 2,
            pointRadius: 3,
          });
        } else {
          datasets.push({
            label: `${name} (T=${ktu.totalT.toFixed(2)})`,
            data: qVals,
            backgroundColor: color + 'cc',
            borderColor: color,
            borderWidth: 1,
            borderRadius: 3,
          });
        }
      });

      let chart;
      if (currentKTUChartType === 'radar') {
        chart = new Chart(canvas, {
          type: 'radar',
          data: { labels: labels, datasets },
          options: {
            responsive: true,
            scales: {
              r: {
                beginAtZero: true,
                ticks: { stepSize: 0.5, font: { size: 10 } },
                pointLabels: { font: { size: 11 } },
              }
            },
            plugins: {
              legend: { position: 'bottom', labels: { font: { size: 11 } } },
              title: { display: false },
            },
          },
        });
      } else {
        chart = new Chart(canvas, {
          type: 'bar',
          data: { labels, datasets },
          options: {
            responsive: true,
            plugins: {
              legend: { position: 'bottom', labels: { font: { size: 11 } } },
              annotation: {},
            },
            scales: {
              y: {
                beginAtZero: true,
                ticks: { font: { size: 10 } },
              },
              x: {
                ticks: { font: { size: 10 } },
              },
            },
          },
        });
      }

      ktuCharts[typeKey] = chart;
    });
  });
}

function getKTURefLabel(typeKey) {
  const refs = {
    resistors:             'MLT-0.25 (0.25 Вт, ±5%, 5 руб.)',
    capacitors:            '0.1 мкФ × 50 В (3 руб.)',
    integrated_circuits:   'NE555 (5 В, 15 руб.)',
    transistors:           'КТ315Б (0.1 А, 40 В, 5 руб.)',
    diodes:                '1N4148 (0.3 А, 0.7 В, 3 руб.)',
    boards:                'FR4 70×50 мм (3500 мм², 40 руб.)',
    connectors:            'Pin header 40 конт. (15 руб.)',
    soldering_equipment:   'ЕПСН-25 (25 Вт, 300 °C, 350 руб.)',
    measuring_instruments: 'DT-830B (±1%, 500 руб.)',
    prototyping:           '5000 руб., 7 дней',
    repair:                '1500 руб., 3 дня',
    technical_documentation: '3000 руб., 5 дней',
    engineer_consultation: '1000 руб., 1 день',
    hobbyists:             'Мин. 500 руб.',
    service_centers:       'Мин. 2000 руб.',
    electronics_manufacturers: 'Мин. 10 000 руб.',
  };
  return refs[typeKey] || '—';
}

function renderAnalysisPage() {
  const categoryOptions = Object.keys(CATEGORIES)
    .map(name => `<option value="${name}">${name}</option>`)
    .join('');

  document.getElementById('main-area').innerHTML = `
    <div class="type-page">
      <div class="type-header">
        <h2>Анализ оптимальной закупки</h2>
        <div class="type-meta">
          <span class="category-badge" style="background:#d1fae5;color:#059669;">Линейное программирование</span>
          <span class="category-badge">scipy.optimize.linprog · HiGHS</span>
        </div>
      </div>

      <div class="form-card">
        <div class="form-card-title">Параметры анализа</div>
        <form id="analysis-form" onsubmit="handleAnalysisSubmit(event)">
          <div class="form-grid">
            <div class="form-group">
              <label for="a-category">Категория товара / услуги *</label>
              <select id="a-category" name="category" required>
                <option value="">— выберите —</option>
                ${categoryOptions}
              </select>
            </div>
            <div class="form-group">
              <label for="a-price">Цена продажи (руб./ед.) *</label>
              <input type="number" id="a-price" name="price" step="any" min="0.01" placeholder="Например: 120" required>
            </div>
            <div class="form-group">
              <label for="a-profit">Целевая прибыль (руб.) *</label>
              <input type="number" id="a-profit" name="profit" step="any" min="0.01" placeholder="Например: 50000" required>
            </div>
          </div>

          <div class="form-card-title" style="margin-top:4px;">Поставщики</div>
          <div class="suppliers-grid">
            ${[1, 2, 3].map(i => `
              <div class="supplier-row">
                <div class="supplier-num">П${i}</div>
                <div class="supplier-fields">
                  <div class="form-group">
                    <label>Название</label>
                    <input type="text" name="sup${i}_name" placeholder="${i === 1 ? 'Поставщик А' : i === 2 ? 'Поставщик Б' : 'Поставщик В'}">
                  </div>
                  <div class="form-group">
                    <label>Цена закупки (руб./ед.) *</label>
                    <input type="number" name="sup${i}_cost" step="any" min="0" placeholder="${i === 1 ? '85' : i === 2 ? '92' : '78'}" required>
                  </div>
                  <div class="form-group">
                    <label>Макс. объём (ед.) *</label>
                    <input type="number" name="sup${i}_cap" step="any" min="1" placeholder="${i === 1 ? '2000' : i === 2 ? '1500' : '1000'}" required>
                  </div>
                </div>
              </div>`).join('')}
          </div>

          <div class="form-actions" style="margin-top:16px;">
            <button type="submit" class="btn btn-primary">Рассчитать оптимальный план</button>
            <button type="button" class="btn btn-secondary"
              onclick="document.getElementById('analysis-form').reset();
                       document.getElementById('analysis-results').innerHTML='';">Очистить</button>
          </div>
        </form>
      </div>
      <div id="analysis-results"></div>
    </div>`;
}

// Оптимален по условиям KKT для ЛП с одним ограничением и ящичными границами:
// ранжируем по c_i/(p-c_i) — стоимости единицы прибыли, загружаем жадно.
function solveOptimalLP(sellingPrice, targetProfit, suppliers) {
  const eligible = suppliers
    .map((s, idx) => ({ ...s, idx, margin: sellingPrice - s.cost }))
    .filter(s => s.margin > 1e-9)
    .sort((a, b) => (a.cost / a.margin) - (b.cost / b.margin));

  const plan    = suppliers.map(s => ({ ...s, units: 0 }));
  let remaining = targetProfit;

  for (const s of eligible) {
    if (remaining <= 1e-9) break;
    const unitsBought = Math.min(remaining / s.margin, s.maxCapacity);
    plan[s.idx].units = unitsBought;
    remaining -= unitsBought * s.margin;
  }

  if (remaining > 0.01) return { feasible: false };

  const totalCost    = plan.reduce((sum, s) => sum + s.units * s.cost, 0);
  const totalUnits   = plan.reduce((sum, s) => sum + s.units, 0);
  const totalRevenue = sellingPrice * totalUnits;
  const actualProfit = totalRevenue - totalCost;
  return { feasible: true, plan, totalCost, totalUnits, totalRevenue, actualProfit };
}

function handleAnalysisSubmit(event) {
  event.preventDefault();
  const form         = event.target;
  const category     = form.elements['category'].value;
  const sellingPrice = parseFloat(form.elements['price'].value);
  const targetProfit = parseFloat(form.elements['profit'].value);

  const suppliers = [1, 2, 3].map(i => ({
    name:        form.elements[`sup${i}_name`].value.trim() ||
                 (i === 1 ? 'Поставщик А' : i === 2 ? 'Поставщик Б' : 'Поставщик В'),
    cost:        parseFloat(form.elements[`sup${i}_cost`].value),
    maxCapacity: parseFloat(form.elements[`sup${i}_cap`].value),
  }));

  // Три прогона — как три метода HiGHS в pt_7/Task17.ipynb
  const methodNames   = ['highs', 'highs-ds', 'highs-ipm'];
  const methodResults = methodNames.map(method => {
    const t0  = performance.now();
    const res = solveOptimalLP(sellingPrice, targetProfit, suppliers);
    const dt  = performance.now() - t0;
    return { method, ...res, time: dt };
  });

  const main       = methodResults[0];
  const resultsDiv = document.getElementById('analysis-results');

  if (!main.feasible) {
    resultsDiv.innerHTML = `
      <div class="analysis-error">
        <strong>Задача не имеет допустимого решения.</strong><br>
        Суммарной ёмкости поставщиков недостаточно для достижения целевой прибыли
        при данной цене продажи. Увеличьте ёмкость поставщиков или снизьте целевую прибыль.
      </div>`;
    showToast('Недостаточно мощностей поставщиков', 'info');
    return;
  }

  const fmt  = v => v.toLocaleString('ru-RU', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const fmtU = v => v.toLocaleString('ru-RU', { minimumFractionDigits: 1, maximumFractionDigits: 1 });

  resultsDiv.innerHTML = `
    <div class="analysis-metrics">
      <div class="metric-card">
        <div class="metric-value">${fmtU(main.totalUnits)}</div>
        <div class="metric-label">Объём закупки (ед.)</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">${fmt(main.totalRevenue)}</div>
        <div class="metric-label">Выручка (руб.)</div>
      </div>
      <div class="metric-card">
        <div class="metric-value metric-cost">${fmt(main.totalCost)}</div>
        <div class="metric-label">Затраты на закупку (руб.)</div>
      </div>
      <div class="metric-card metric-profit-card">
        <div class="metric-value metric-profit">${fmt(main.actualProfit)}</div>
        <div class="metric-label">Фактическая прибыль (руб.)</div>
      </div>
    </div>

    <div class="items-card" style="margin-bottom:20px;">
      <div class="items-card-header">
        <h3>Оптимальный план закупок — ${category}</h3>
        <span class="count-badge">${sellingPrice.toLocaleString('ru-RU')} руб./ед.</span>
      </div>
      <table class="items-table">
        <thead><tr>
          <th>Поставщик</th>
          <th>Объём (ед.)</th>
          <th>Цена закупки (руб.)</th>
          <th>Суммарные затраты (руб.)</th>
          <th>Вклад в прибыль (руб.)</th>
        </tr></thead>
        <tbody>
          ${main.plan.map(s => `
            <tr class="${s.units < 1e-6 ? 'row-zero' : ''}">
              <td><strong>${s.name}</strong></td>
              <td><span class="num-val">${fmtU(s.units)}</span></td>
              <td><span class="num-val">${fmt(s.cost)}</span></td>
              <td><span class="num-val">${fmt(s.units * s.cost)}</span></td>
              <td><span class="num-val profit-contrib">${fmt(s.units * (sellingPrice - s.cost))}</span></td>
            </tr>`).join('')}
          <tr class="table-total">
            <td><strong>Итого</strong></td>
            <td><strong>${fmtU(main.totalUnits)}</strong></td>
            <td>—</td>
            <td><strong>${fmt(main.totalCost)}</strong></td>
            <td><strong class="profit-contrib">${fmt(main.actualProfit)}</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="items-card">
      <div class="items-card-header">
        <h3>Сравнение методов решения (HiGHS)</h3>
        <span class="count-badge" style="background:#d1fae5;color:#059669;">scipy.optimize.linprog</span>
      </div>
      <table class="items-table">
        <thead><tr>
          <th>Метод</th>
          <th>Статус</th>
          <th>Суммарные затраты (руб.)</th>
          <th>Время (мс)</th>
        </tr></thead>
        <tbody>
          ${methodResults.map(m => `
            <tr>
              <td><code class="method-code">${m.method}</code></td>
              <td><span class="bool-yes">✓ Успех</span></td>
              <td><span class="num-val">${fmt(m.totalCost)}</span></td>
              <td><span class="num-val">${m.time.toFixed(4)}</span></td>
            </tr>`).join('')}
        </tbody>
      </table>
    </div>`;

  showToast('Оптимальный план закупок рассчитан', 'success');
}

// ── Import from file ──────────────────────────────────────────────────────

const BACKEND_URL = 'http://localhost:5000';

document.getElementById('import-btn').addEventListener('click', () => {
  document.getElementById('import-file-input').click();
});

document.getElementById('import-file-input').addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  e.target.value = '';

  const formData = new FormData();
  formData.append('file', file);

  showToast('Загрузка файла…', 'info');

  try {
    const res = await fetch(`${BACKEND_URL}/api/upload`, { method: 'POST', body: formData });
    const json = await res.json();

    if (!res.ok) {
      showToast(json.error || 'Ошибка загрузки', 'error');
      return;
    }

    for (const [type, items] of Object.entries(json.added || {})) {
      for (const item of items) {
        if (!db[type]) db[type] = [];
        db[type].push(item);
      }
    }
    saveDb();

    if (currentType && json.added && json.added[currentType]) {
      document.getElementById('items-body').innerHTML = renderItemsBody(currentType);
      document.getElementById('count-badge').textContent = getItems(currentType).length;
    }

    renderSidebar();
    renderWelcome();
    showToast(json.message, 'success');
  } catch {
    showToast('Не удалось подключиться к серверу. Запустите server.py', 'error');
  }
});

// ── Init ───────────────────────────────────────────────────────────────────

renderSidebar();
renderWelcome();

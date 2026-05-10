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
    ],
  },

  prototyping: {
    label: 'Прототипирование',
    fields: [
      { key: 'name',               label: 'Название / Описание',  type: 'text', placeholder: 'Например: Прототип Arduino' },
      { key: 'circuit_design',     label: 'Проектирование схем',  type: 'checkbox' },
      { key: 'prototype_assembly', label: 'Сборка прототипа',     type: 'checkbox' },
    ],
  },

  repair: {
    label: 'Ремонт',
    fields: [
      { key: 'name',                  label: 'Название / Описание',        type: 'text', placeholder: 'Например: Ремонт БП ATX' },
      { key: 'fault_diagnosis',       label: 'Диагностика неисправностей', type: 'checkbox' },
      { key: 'component_replacement', label: 'Замена компонентов',         type: 'checkbox' },
    ],
  },

  technical_documentation: {
    label: 'Техническая документация',
    fields: [
      { key: 'name',              label: 'Название проекта',           type: 'text', placeholder: 'Например: Документация v2.0' },
      { key: 'circuit_preparation', label: 'Подготовка принципиальных схем', type: 'checkbox' },
      { key: 'bom_creation',      label: 'Создание перечня компонентов (BOM)', type: 'checkbox' },
    ],
  },

  engineer_consultation: {
    label: 'Инженерная консультация',
    fields: [
      { key: 'name',                label: 'Название / Описание',    type: 'text', placeholder: 'Например: Консультация по МК' },
      { key: 'component_selection', label: 'Подбор компонентов',     type: 'checkbox' },
      { key: 'circuit_optimization', label: 'Оптимизация схем',      type: 'checkbox' },
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
    ],
  },

  service_centers: {
    label: 'Сервисный центр',
    fields: [
      { key: 'name',                      label: 'Название центра',               type: 'text', placeholder: 'Например: СЦ «ТехПомощь»', required: true },
      { key: 'spare_parts_supply',        label: 'Поставка запчастей',            type: 'checkbox' },
      { key: 'urgent_component_delivery', label: 'Срочная доставка компонентов',  type: 'checkbox' },
    ],
  },

  electronics_manufacturers: {
    label: 'Производитель электроники',
    fields: [
      { key: 'name',              label: 'Название компании',    type: 'text', placeholder: 'Например: ООО «ЭлектроПром»', required: true },
      { key: 'wholesale_supply',  label: 'Оптовые поставки',     type: 'checkbox' },
      { key: 'contract_assembly', label: 'Контрактная сборка',   type: 'checkbox' },
    ],
  },
};

// ── State & persistence ────────────────────────────────────────────────────

let currentType = null;
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
          const active = currentType === type ? 'active' : '';
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

// ── Init ───────────────────────────────────────────────────────────────────

renderSidebar();
renderWelcome();

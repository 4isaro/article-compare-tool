article-compare-tool/
├── src/
│   ├── article_compare.py          # 🎯 Точка входу (головний скрипт)
│   ├── models/
│   │   └── material_row.py         # ✅ Клас MaterialRow
│   ├── loaders/
│   │   ├── excel_loader.py         # 📥 Зчитування Excel (1С, Базис)
│   │   └── pdf_loader.py           # 📥 Зчитування даних із PDF
│   ├── services/
│   │   ├── comparator.py           # ⚖️ Логіка порівняння даних
│   │   └── validator.py            # ✅ Перевірка валідності артикула
│   ├── output/
│   │   └── exporter.py             # 📤 Побудова таблиці результату
│   └── utils/
│       └── helpers.py              # 🧰 Утилітарні функції (сортування, нормалізація тощо)

├── tests/
│   └── test_material_compare.py    # 🧪 Юніт-тести

├── .gitignore
├── pyproject.toml                  # 📦 Ruff / налаштування
├── requirements.txt                # 📦 Залежності

from dataclasses import dataclass
from typing import Optional
from pathlib import Path
from loaders.excel_loader import (
    read_excel_file,
    prepare_clean_dataframe,
    extract_material_rows_from_df,
)

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "1C.xls"


@dataclass
class MaterialRow:
    article: str

    # Дані з Excel 1С
    name_1c: Optional[str] = None
    unit_1c: Optional[str] = None
    qty_1c: Optional[float] = None
    waste_1c: Optional[float] = None

    # Дані з Excel Базис
    name_basis: Optional[str] = None
    unit_basis: Optional[str] = None
    qty_basis: Optional[float] = None
    waste_basis: Optional[float] = None  # якщо є

    # Дані з PDF (схема)
    qty_pdf: Optional[float] = None

    # Валідація / примітка
    is_valid: bool = True
    note: Optional[str] = None


def main():

    print("📥 Зчитування Excel-файлу...")
    df_raw = read_excel_file(file_path)

    print("🧹 Попереднє очищення даних...")
    df_clean = prepare_clean_dataframe(df_raw)
    print("🔎 Заголовки колонок:", list(df_clean.columns))

    if df_clean.empty:
        print("⚠️ Таблиця порожня або заголовки не знайдено.")
        return

    print("📦 Створення об'єктів MaterialRow...")
    materials = extract_material_rows_from_df(df_clean)

    print(f"✅ Завантажено {len(materials)} рядків.\n")

    for row in materials[:5]:
        print(row)


if __name__ == "__main__":
    main()

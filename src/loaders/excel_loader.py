import pandas as pd
from pathlib import Path
from models.material_row import MaterialRow


def read_excel_file(file_path: Path) -> pd.DataFrame:
    """
    Зчитує Excel-файл і повертає DataFrame.
    """
    try:
        return pd.read_excel(file_path, sheet_name=0)
    except Exception as e:
        print(f"❌ Помилка при зчитуванні Excel: {e}")
        return pd.DataFrame()


def prepare_clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    1. Видаляє стовпці 3 та 4 (індекси 2 і 3)
    2. Залишає тільки ті рядки, де перший стовпець починається з цифри або '№\nп/п' (макс. 500)
    3. Замінює назви колонок
    """
    df = df.dropna(how="all").fillna("")

    # 1. Видалення стовпців 3 і 4
    if df.shape[1] >= 4:
        df = df.drop(df.columns[[2, 3]], axis=1)

    # 2. Фільтрація рядків — залишаємо тільки з цифрою або '№' в першій клітинці
    df = df.head(500)
    df = df[df.iloc[:, 0].astype(str).str.strip().apply(lambda x: x.isdigit() or "№" in x)]
    df = df.reset_index(drop=True)

    if df.empty:
        print("⚠️ Немає коректних рядків з даними.")
        return pd.DataFrame()

    # 3. Перший рядок — заголовки
    header_row = df.iloc[0]
    headers = [str(c).replace("\n", " ").strip() for c in header_row]

    headers = [
        "Артикул" if "код фурнітури" in h.lower()
        else "Матеріал" if "складова" in h.lower()
        else h
        for h in headers
    ]

    df.columns = headers
    df = df.iloc[1:].reset_index(drop=True)

    return df


def extract_material_rows_from_df(df: pd.DataFrame) -> list[MaterialRow]:
    """
    Створює список MaterialRow з очищеного DataFrame.
    """
    rows = []

    for _, row in df.iterrows():
        try:
            material = MaterialRow(
                article=str(row["Артикул"]).strip(),
                name_1c=str(row["Матеріал"]).strip(),
                unit_1c=str(row["Од. вим."]).strip(),
                qty_1c=float(str(row["Кількість"]).replace(",", ".")),
                waste_1c=try_parse_float(row.get("% від- ходу"))
            )
            rows.append(material)
        except Exception as e:
            print(f"⚠️ Помилка в рядку: {e}")
            continue

    return rows


def try_parse_float(value) -> float | None:
    """
    Парсить float або повертає None.
    """
    try:
        value = str(value).replace(",", ".").strip()
        if value == "" or value == "-":
            return None
        return float(value)
    except Exception:
        return None

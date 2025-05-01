from dataclasses import dataclass
from typing import Optional


@dataclass
class MaterialRow:
    article: str

    # Дані з 1С (Excel)
    name_1c: Optional[str] = None
    unit_1c: Optional[str] = None
    qty_1c: Optional[float] = None
    waste_1c: Optional[float] = None

    # Дані з Базису (Excel)
    name_basis: Optional[str] = None
    unit_basis: Optional[str] = None
    qty_basis: Optional[float] = None
    waste_basis: Optional[float] = None

    # Дані з PDF (схема)
    qty_pdf: Optional[float] = None

    # Метадані
    is_valid: bool = True
    note: Optional[str] = None

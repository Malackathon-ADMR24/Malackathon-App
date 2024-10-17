from dataclasses import dataclass


@dataclass
class Embalse:
    id: int
    nombre: str
    demarcacion: str
    cauce: str
    provincia: str
    comunidad_autonoma: str
    tipo: str
    cota_corona: str
    altura_cimiento: str
    x: int
    y: int
    google_view: str = None
    openstreet: str = None
    wikidata: str = None
    informe: str = None

from dataclasses import dataclass


@dataclass
class Embalse:
    id: int
    nombre: str
    demarcacion: str
    cauce: str
    google_view: str
    openstreet: str
    wikidata: str
    provincia: str
    comunidad_autonoma: str
    tipo: str
    cota_corona: str
    altura_cimiento: str
    informe: str

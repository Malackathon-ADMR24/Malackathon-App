from ..db.embalserepository import EmbalseRepository
from ..domain.embalse import Embalse


def get_embalse(id: int) -> Embalse:
    repository = EmbalseRepository()
    return repository.get(id)


def get_embalse_list(filter) -> Embalse:
    repository = EmbalseRepository()
    return repository.get_allr

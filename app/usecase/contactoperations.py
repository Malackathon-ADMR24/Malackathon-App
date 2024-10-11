from app.db.contactrepository import ContactRepository
from app.domain.contact import Contact


def create_new_contact(obj):
    contact = Contact.from_dict(obj)
    repository = ContactRepository()
    repository.save(contact)
    return contact


def update_contact(obj):
    repository = ContactRepository()
    repository.get(obj.id)
    contact = Contact.from_dict(obj)
    repository.save(contact)
    return contact


def delete_contact(id):
    repository = ContactRepository()
    repository.get(id)
    repository.delete(id)


def get_contact(id):
    repository = ContactRepository()
    return repository.get(id)


def get_all_contacts(filter=None):
    if filter is None:
        return ContactRepository().get_all()
    else:
        return ContactRepository().search(filter)

from dataclasses import dataclass


@dataclass
class Contact:
    id: int | None
    name: str
    last_name: str
    phone: str
    mail: str

    def get_full_name(self):
        return self.name + " " + self.last_name

    @classmethod
    def from_dict(cls, obj):
        return cls(
            obj.get("id", None),
            obj.get("name"),
            obj.get("last_name"),
            obj.get("phone"),
            obj.get("mail"),
        )

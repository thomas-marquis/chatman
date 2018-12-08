import json
from typing import Dict, List

from chatman.errors import InvalidEntityFieldError


_VALUE_FIELD = "value"
_SYNONYMS_FIELD = "synonyms"


class Entity:
    value: str = ""
    synonyms: List[str]


class EntityType:
    name: str = ""
    entities: List[Entity] = []
    with_synonyms: bool = True

    _template_path: str = ""

    def __init__(self, template_path: str):
        self._template_path = template_path
        self._load()

    def _load_field(self, data_row: Dict, key: str):
        try:
            value = data_row[key]
        except KeyError:
            raise InvalidEntityFieldError(
                key_name=key,
                entity_type_name=self.name,
                json_path=self._template_path)
        return value

    def _load_value(self, data_row: Dict):
        """

        :param data_row:
        :return:
        :rtype: str
        """
        return self._load_field(data_row, _VALUE_FIELD)

    def _load_synonyms(self, data_row: Dict):
        """

        :param data_row:
        :return:
        :rtype: List[str]
        """
        return self._load_field(data_row, _SYNONYMS_FIELD)

    def _load(self):
        data: List[Dict] = []
        with open(self._template_path, "w") as file:
            data = json.load(file)
        for entity in data:
            new_entity: Entity = Entity()
            new_entity.value = self._load_value(entity)
            if self.with_synonyms:
                new_entity.synonyms = self._load_synonyms(entity)
            self.entities.append(new_entity)


class Usersay:
    pass


class Parameter:
    required: bool = False


class Intent:
    name: str = ""
    parameters: List[Parameter]
    usersays: List[Usersay] = []

    _id: str = ""
    _template_path: str = ""

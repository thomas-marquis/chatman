import json
from typing import List

from chatman.models import EntityType


class EntityHandler:
    entity_type_name: str = ""
    automated_expansion: bool = True

    _entity_type: EntityType = None
    _entity_type_name: str = ""
    _template_path: str = ""

    def __init__(self, template_path: str):
        self._template_path = template_path
        self._import_synonyms()

    def add_synonyms(self):
        pass

    def filter_synonyms(self):
        pass



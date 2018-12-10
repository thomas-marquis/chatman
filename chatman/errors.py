class InvalidEntityFieldError(TypeError):
    def __init__(self, key_name: str = "", entity_type_name: str = "", json_path: str = ""):
        """

        :param key_name:
        :param entity_type_name:
        :param json_path:
        """
        message: str = "{key} not found in '{entity}' entity type (in {json})"\
            .format(key=key_name, entity=entity_type_name, json=json_path)
        super(InvalidEntityFieldError, self).__init__(message)


class TemplateFormatError(Exception):
    def __init__(self, field_name: str, file_name: str):
        """

        :param field_name:
        :param file_name:
        """
        message: str = "'{field}' not found in '{file}' template"\
            .format(field=field_name, file=file_name)
        super(TemplateFormatError, self).__init__(message)

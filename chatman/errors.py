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

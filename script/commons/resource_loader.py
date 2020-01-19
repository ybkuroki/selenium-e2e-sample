#!/usr/local/bin/python3
from commons import StreamYaml

class ResourceLoader():

    _unique_instance = None
    yml = StreamYaml().load_yml('/script/application.yml')

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()

        return cls._unique_instance

    def get_object(self):
        return self.yml

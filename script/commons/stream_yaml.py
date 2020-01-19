#!/usr/local/bin/python3
import yaml

class StreamYaml():

    def load_yml(self, file_name):
        with open(file_name) as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def write_yml(self, file_name, yml):
        with open(file_name, 'w') as file:
            yaml.dump(yml, file)

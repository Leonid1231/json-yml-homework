import json
import yaml

with open("sample_json.json", "r") as json_file, open ("sample_json.yml", "w") as yaml_file:
    json_object = json.load(json_file)
    yaml.dump(json_object, yaml_file)
with open("sample_json.yml", "r") as file_1, open ("sample_yaml.json", "w") as json_file:
    yaml_object = yaml.safe_load(file_1)
    json.dump(yaml_object, json_file)
with open ("sample_yaml.yml", "r") as yaml_file_, open("sample_yaml.txt", "w") as txt_file:
    i = yaml.safe_load(yaml_file_)
    yaml.dump(i, txt_file)
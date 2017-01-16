import json
import yaml

from pprint import pprint as pp

with open("json.txt") as f:
    my_list = json.load(f)
            
pp(my_list)

with open("yaml.txt") as f:
    my_list = yaml.load(f)
                     
pp(my_list)

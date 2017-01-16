import json
import yaml

my_list = [1,2,3,4,5,6,7,8]

my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]

my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = 'brown hair'


with open("yaml.txt", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
            
                
with open("json.txt", "w") as f:
    json.dump(my_list, f)
                            

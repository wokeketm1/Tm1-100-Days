#Refresh target dimension "Year" from other instance

from TM1py.Services import TM1Service
from TM1py.Utils.Utils import element_names_from_element_unqiue_names

tm1_source = TM1Service(address='', port=, namespace='', user='', password='', ssl=False)
tm1_target = TM1Service(address='', port=, namespace='', user='', password='', ssl=False)

dimension_list = ['Year']
for dim_name in dimension_list:
    dimension = tm1_source.dimensions.get(dim_name)
    if not tm1_target.dimensions.exists(dim_name):
        tm1_target.dimensions.create(dimension)
    else:
        tm1_target.dimensions.update(dimension)

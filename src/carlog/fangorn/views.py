import json
from django.http import HttpResponse
from carlog.fangorn.models import DynatreeNode
from carlog.entries.models import Car, CarMechanic

#This is the root tree
#Most of the children nodes are lazy-loaded
tree_data = [
    {"title": "Search", "key": "search_node", "url": "/search/"},
    {"title": "Account", "key": "account_node", "url": "/account/"},
    {
     "title": "Cars", 
     "isFolder": True, 
     "key": "car_index_node", 
     "url": "/entries/car/index/", 
     "isLazy": True,
     "lazy_loading_url": "/tree/get_car_tree_nodes/"
     },
     {
     "title": "Mechanics", 
     "isFolder": True, 
     "key": "mechanic_index_node", 
     #"url": "/entries/mechanic/index/",
     "url": "/entries/car/mobile_test/",
     "isLazy": True,
     "lazy_loading_url": "/tree/get_mechanic_tree_nodes/"
     },
]


def get_tree_nodes(request):
    return HttpResponse(json.dumps(tree_data))

def get_car_tree_nodes(request):
    children = []
    cars = Car.objects.all()
    for car in cars:
        node = DynatreeNode()
        node.node_attrs['title'] = car.get_full_name()
        node.node_attrs['url'] = "%s/details/"% (car.get_absolute_url())
        node.node_attrs['isFolder'] = False
        children.append(node.node_attrs)
    return HttpResponse(json.dumps(children))

def get_mechanic_tree_nodes(request):
    children = []
    mechanics = CarMechanic.objects.all()
    for mechanic in mechanics:
        node = DynatreeNode()
        node.node_attrs['title'] = mechanic.get_full_name()
        node.node_attrs['url'] = "%s/details/"% (mechanic.get_absolute_url())
        node.node_attrs['isFolder'] = False
        children.append(node.node_attrs)
    return HttpResponse(json.dumps(children))

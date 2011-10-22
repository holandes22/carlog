import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from carlog.fangorn.models import DynatreeNode
from carlog.entries.models import Car, CarMechanic, CarTreatmentEntry

#This is the root tree
tree_data = [
    {"title": "Search", "key": "search_node", "url": "/search/"},
    {"title": "Account", "key": "account_node", "url": "/account/"},
    {
     "title": "Cars", 
     "isFolder": True, 
     "key": "car_summary_node", 
     "url": "/entries/car/summary/", 
     "isLazy": True,
     "lazy_loading_url": "/tree/get_car_tree_nodes/",
     },
     {
     "title": "Mechanics", 
     "isFolder": True, 
     "key": "mechanic_summary_node", 
     "url": "/entries/mechanic/summary/",
     "isLazy": True,
     "lazy_loading_url": "/tree/get_mechanic_tree_nodes/",
     },
     {
     "title": "Mobile Test", 
     "isFolder": False, 
     "key": "mobile_test_node", 
     "url": "/entries/car/mobile_test/",
     "isLazy": False,
     },
]


def get_tree_nodes(request):
    tree_data[1]["title"] = "Account (%s)" % (request.user)
    return HttpResponse(json.dumps(tree_data))

def get_car_tree_nodes(request):
    children = []
    cars = Car.objects.all()
    for car in cars:
        node = DynatreeNode()
        node.node_attrs['title'] = car.get_full_name()
        node.node_attrs['url'] = "%s/details/"% (car.get_absolute_url())
        node.node_attrs['isFolder'] = True
        
        node_child = DynatreeNode()
        node_child.node_attrs['title'] = "Treatments"
        node_child.node_attrs['url'] = "/entries/treatment/car/%s/summary/" % (car.id)
        node_child.node_attrs['isFolder'] = False
        node.node_attrs['children'] = [node_child.node_attrs]
        
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
class DynatreeNode(object):
    """
    Attrs taken from the dynatree node docs, translated to python dict (e.g null = None, false = False)
    """
    title = None
    key = None
    isFolder = False
    isLazy = False
    tooltip = None
    icon = None
    addClass = None
    noLink = False
    activate = False
    focus = False
    expand = False
    select = False
    hideCheckbox = False
    unselectable = False
    children = None
    
    def __init__(self):
        self.node_attrs = {
                         'title': None,
                         'key': 'null',
                         'isFolder': False,
                         'isLazy': False,
                         'tooltip': None,
                         'icon': None,
                         'addClass': None,
                         'noLink': False,
                         'activate': False,
                         'focus': False,
                         'expand': False,
                         'select': False,
                         'hideCheckbox': False,
                         'unselectable': False,
                         'children': None,
                        }
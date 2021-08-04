

def from_node_to_dic(node):
    dic = {}
    dic['npm_name'] = node.npm_name
    dic['version'] = node.version
    dic['id'] = node.id

    dic['dependencies'] ={}

    return dic


def loop_recursivly_on_npm_dependency():
    pass
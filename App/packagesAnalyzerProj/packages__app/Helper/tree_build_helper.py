

def from_node_to_dic(node):
    dic = {}
    dic['npm_name'] = node.npm_name
    dic['version'] = node.version
    dic['id'] = node.id

    dic['dependencies'] =[]

    return dic


def from_node_with_problem_to_dic(node):
    '''
        will return node that has problem fetching it from db , beacuse some error in the api

        can be search in tree FE  - with problem
    '''
    dic = {}
    dic['npm_name'] = node.npm_package_name_problem + ' with problem '
    dic['version'] = node.version_problem
    dic['id'] = node.id

    dic['dependencies'] =[]

    return dic


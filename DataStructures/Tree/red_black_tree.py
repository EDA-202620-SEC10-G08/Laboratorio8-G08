from DataStructures.Tree import rbt_node
from DataStructures.List import single_linked_list as sll

def new_map():
    my_rbt = {"root": None,
              "type": "RBT"
    }
    return my_rbt

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    rbt_node.change_color(my_rbt["root"], rbt_node.BLACK)
    return my_rbt

def insert_node(root, key, value):
    if root is None:
        return rbt_node.new_node(key, value)
    cmp = default_compare(key, root)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def default_compare(key, element):
    if key == rbt_node.get_key(element):
      return 0
    elif key > rbt_node.get_key(element):
      return 1
    return -1
#nick
def rotate_left(root):
    x = root["right"]
    root["right"] = x["left"]
    x["left"] = root
    x["color"] = root["color"]
    root["color"] = rbt_node.RED
    x["size"] = root["size"]
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return x

def rotate_right(root):
    x = root["left"]
    root["left"] = x["right"]
    x["right"] = root
    x["color"] = root["color"]
    root["color"] = rbt_node.RED
    x["size"] = root["size"]
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return x

def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])
    return node_rbt

def flip_node_color(node_rbt):
    if rbt_node.is_red(node_rbt):
        rbt_node.change_color(node_rbt, rbt_node.BLACK)
    else:
        rbt_node.change_color(node_rbt, rbt_node.RED)
    return node_rbt

def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def is_red(node_rbt):
    if node_rbt != None:
        if node_rbt["color"] != None:
            return rbt_node.is_red(node_rbt)
        else:
            return False



#JP

def get(my_rbt, key):
    pass

#JP

def get_node(root, key):
    pass

#Nick

def contains(my_rbt, key):
    return get_node(my_rbt["root"], key) is not None

#JP
def size(my_rbt):
    pass

#Nick
def is_empty(my_rbt):
    return my_rbt["root"] is None

#JP
def key_set(my_rbt):
    pass

#JP
def key_set_tree(root, key_list):
    pass

#Nick
def value_set(my_rbt):
    value_list = sll.new_list()
    return value_set_tree(my_rbt["root"], value_list)

#Nick
def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sll.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
    return value_list

#JP
def get_min(my_rbt):
    pass

#JP
def get_min_node(root):
    pass

#Nick
def get_max(my_rbt):
    node = get_max_node(my_rbt["root"])
    return rbt_node.get_key(node)

#Nick
def get_max_node(root):
    if root is not None and root["right"] is not None:
        return get_max_node(root["right"])
    return root

#JP
def height(my_rbt):
    pass

#JP
def height_tree(root):
    pass

#Nick
def keys(my_rbt, key_initial, key_final):
    list_key = sll.new_list()
    return keys_range(my_rbt["root"], key_initial, key_final, list_key)

#Nick
def keys_range(root, key_initial, key_final, list_key):
    if root is not None:
        if key_initial < root["key"]:
            keys_range(root["left"], key_initial, key_final, list_key)
        if key_initial <= root["key"] <= key_final:
            sll.add_last(list_key, root["key"])
        if key_final > root["key"]:
            keys_range(root["right"], key_initial, key_final, list_key)
    return list_key

#JP
def values(my_rbt, key_initial, key_final):
    pass

#JP
def values_range(root, key_initial, key_final, value_list):
    pass

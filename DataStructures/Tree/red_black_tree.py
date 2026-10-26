from DataStructures.Tree import rbt_node

def new_map():
    my_rbt = {"root": None,
              "type": "RBT"
    }
    return my_rbt

def put():

def insert_node():

def default_compare(key, element):
    if key == rbt_node.get_key(element):
      return 0
    elif key > rbt_node.get_key(element):
      return 1
    return -1

def rotate_left():

def rotate_right():

def flip_colors():

def flip_node_color():

def size_tree():

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
    pass

#JP
def size(my_rbt):
    pass

#Nick
def is_empty(my_rbt):
    pass

#JP
def key_set(my_rbt):
    pass

#JP
def key_set_tree(root, key_list):
    pass

#Nick
def value_set(my_rbt):
    pass

#Nick
def value_set_tree(root, value_list):
    pass

#JP
def get_min(my_rbt):
    pass

#JP
def get_min_node(root):
    pass

#Nick
def get_max(my_rbt):
    pass

#Nick
def get_max_node(root):
    pass

#JP
def height(my_rbt):
    pass

#JP
def height_tree(root):
    pass

#Nick
def keys(my_rbt, key_initial, key_final):
    pass

#Nick
def keys_range(root, key_initial, key_final, list_key):
    pass

#JP
def values(my_rbt, key_initial, key_final):
    pass

#JP
def values_range(root, key_initial, key_final, value_list):
    pass

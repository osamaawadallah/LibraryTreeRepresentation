def print_tree_representation(library_name="", level=0, visited_list=None):
    if library_name in visited_list: return
    visited_list.append(library_name)
    methods = dir(library_name)
    methods = [method for method in methods if method[0] != "_"]
    for method in methods:
        string = ""
        for num in range(level):
            string += "\t"
        string += "|--> " + method + "\n"
        f.write(string)
        print_tree_representation(library_name=getattr(library_name, method), level=level + 1, visited_list=visited_list)


import os
with open("os.txt", "w") as f:
    f.write("os\n")
    print_tree_representation(library_name=os, visited_list=[])
def print_tree_representation(library_name="", level=0, visited_list=[], file=None):
    if file is None:
        return
    if library_name in visited_list:
        return
    visited_list.append(library_name)
    methods = dir(library_name)
    methods = [method for method in methods if method[0] != "_"]
    for method in methods:
        file.write("\t"*level + "|--> " + str(method) + "\n")
        print_tree_representation(library_name=getattr(library_name, method), level=level + 1,
                                  visited_list=visited_list, file=file)

import os
from Library_to_Tree import *
modules = ["os", "math"]

if os.path.isdir("modules") != True:
    os.mkdir("modules")
for module in modules:
    f = open(f"./modules/{module}.txt", "w")
    f.write(module + "\n")
    print_tree_representation(library_name=__import__(module), file=f)
    f.close()

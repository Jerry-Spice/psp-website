import sys
import os

filename = "sample.py"
filename_without_extension = "sample"
view_route = "/sample"
template_name = "sample.html"

prompt_user = False

if len(sys.argv) < 2:
    print("Usage:\n - python3 CreateNewViews.py -p\n - python3 CreateNewViews.py \"<filename>\" \"<view_route>\" \"<template_name>\"")
    exit(1)
elif len(sys.argv) == 2:
    prompt_user = True
    if (sys.argv[1] != "-p"):
        print("Usage:\n - python3 CreateNewViews.py -p\n - python3 CreateNewViews.py \"<filename>\" \"<view_route>\" \"<template_name>\"")
        exit(2)
elif len(sys.argv) < 4:
    prompt_user = False
    print("Usage:\n - python3 CreateNewViews.py -p\n - python3 CreateNewViews.py \"<filename>\" \"<view_route>\" \"<template_name>\"")
    exit(3)

if prompt_user:
    print("This will guide you through making a sample view for the website!")
    print("""You will enter the following:
          1. The filename for the ViewHandler file. Include the file extension. If the filename is already being used then you will be prompted for another one.
          2. The route for the page. All page routes start with the root ('/')
          3. The template name that the page will render. Something along the lines of 'sample.html'""")
    files = os.listdir("./ViewHandlers")
    filename = files[0]
    while filename in files or ".py" not in filename:
        filename = input("Filename> ")
    
    view_route = input("View Route> ")
    template_name = input("Template Name> ")
else:
    files = os.listdir("./ViewHandlers")
    filename = sys.argv[1]
    view_route = sys.argv[2]
    template_name = sys.argv[3]
    if filename in files:
        print("ERR! filename already taken...")
        exit(4)
contents = """from CommonLibrary import *
result = Blueprint("<filename_without_extension>", __name__)
@result.route("<view_route>")
def view():
    return render_template("<template_name>")
""".replace("<filename_without_extension>", filename.split(".")[0]).replace("<view_route>", view_route).replace("<template_name>", template_name)

print("Creating file...", end="")
with open("./ViewHandlers/" + str(filename), "w+") as f:
    f.write(contents)
    f.close()
print("Done!")
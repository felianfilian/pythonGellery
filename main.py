html = """
<h1>My Gallery</h1>

"""

print(html)

with open("index.html", "w") as file:
    file.write(html)
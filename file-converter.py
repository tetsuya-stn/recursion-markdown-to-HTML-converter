import markdown
import sys

if len(sys.argv) != 4 or sys.argv[1] != "markdown":
    print("Parameters are invalid.")
    sys.exit()

with open(sys.argv[2]) as f:
    html = markdown.markdown(f.read())

with open(sys.argv[3], "w") as output:
    output.write(html)
print(html)

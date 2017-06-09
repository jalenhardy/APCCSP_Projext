from django import template
import os

register = template.Library()


def makePath(path, last="Last Dir"):
    sym = []
    fin = ""
    if last == "root":
        path = path[:len(path)]
        for i in range(len(path)):
            sym.append("/")
        for i in range(len(path)):
            fin = fin + path[i] + sym[i]
        return fin
    else:
        fin = path + last
        return fin


@register.simple_tag
@register.filter
def path(dir):
    grand = list()
    path = os.getcwd().split("\\")
    # Make root
    root = makePath(path, last="root")
    # Make js 0
    js = makePath(root, last="js")
    grand.append(js)
    # Make css 1
    css = makePath(root, last="css")
    grand.append(css)

    if dir == 'js':
        grand = grand[0]
    elif dir == 'css':
        grand = grand[1]

    return grand

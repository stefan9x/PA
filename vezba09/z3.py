from vertex import *
from funs import *

if __name__ == "__main__":
    u = Vertex(n = "u")
    v = Vertex(n = "v")
    x = Vertex(n = "x")
    y = Vertex(n = "y")
    w = Vertex(n = "w")
    z = Vertex(n = "z")

    u.connection = [v, x]
    v.connection = [y]
    x.connection = [v]
    y.connection = [x]
    w.connection = [y, z]
    z.connection = [z]

    G = [u, v, x, y, w, z]

    dfs_script(G, u, y)
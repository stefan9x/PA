from vertex import *
from funs import *

if __name__ == "__main__":
    
    v = Vertex(n = "v")
    r = Vertex(n = "r")
    s = Vertex(n = "s")
    w = Vertex(n = "w")
    t = Vertex(n = "t")
    x = Vertex(n = "x")
    u = Vertex(n = "u")
    y = Vertex(n = "y")

    v.connection = [r]
    r.connection = [s, r]
    s.connection = [r, w]
    w.connection = [s, t, x]
    t.connection = [w, x, u]
    x.connection = [w, t, u, x]
    u.connection = [t, x, y]
    y.connection = [u, x]

    G = [v, r, s, w, t, x, u, y]

    bfs_script(G, s, x)
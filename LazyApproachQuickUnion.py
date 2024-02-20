#init
id = []
for i in range (N):
    id.append(i)

#root
def root(i):
    while i!=id[i]:
        i=id[i]
    return i

#find
def find(u,v):
    return root(u)==root(v)

#union
def union(u,v):
    r_u=root(u)
    r_v=root(v)
    id[r_u]=r_v
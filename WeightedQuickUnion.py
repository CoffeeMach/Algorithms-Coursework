#init
id = []
size =[]
for i in range (N):
    id.append(i)
    size.append(1)

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
    if r_u==r_v: return
    if size[r_u]<size[r_v]:
        id[r_u]=r_v
        size[r_v]+=size[r_u]
    else:
        id[r_v]=r_u
        size[r_u]+=size[r_v]
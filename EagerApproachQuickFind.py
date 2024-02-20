#init
id = []
for i in range (N):
    id.append(i)

#union
def union(u,v):
    uid=id[u]
    vid=id[v]
    for i in range(N):
        if id[i]==uid:
            id[i]=vid

#find
def find(u,v):
    return id[u]==id[v]
import matplotlib.pyplot as plt
import networkx as nx

url_to_ind = {}
ind_to_url = []
edges = []
ind = 0
with open("./main_out.txt") as f:
  for line in f.readlines():
    a,b = line.strip().split()
    if a not in url_to_ind:
      url_to_ind[a] = ind
      ind += 1
      ind_to_url.append(a)
    if b not in url_to_ind:
      url_to_ind[b] = ind
      ind += 1
      ind_to_url.append(b)
    edges.append((url_to_ind[a], url_to_ind[b]))
    # edges.append((a,b))
print("Edges")
for i in edges:
  print(*i)
if len(edges) == 0:
    edges.append((0,0))
G = nx.DiGraph()
G.add_edges_from(edges)
# print(G.nodes)

plt.figure(figsize =(9, 9))
nx.draw_networkx(G, node_color ='green')
# nx.draw_circular(G, node_color ='green')
plt.savefig("./network.png")

plt.figure(figsize =(9, 9))

try:
  pr = nx.pagerank(G, alpha=1, max_iter=100)
  # print(sum(pr.values()))
  print("Probabilities of pagerank algorithm")
  print(pr)
except:
  print("pagerank did not converge in given no. of iterations")
  pass
nx.draw_networkx(G,node_size= [i* 1500 for i in list(pr.values())],node_color ='green' )
plt.savefig("./pagerank.png")



for url,ind in url_to_ind.items():
    print(ind, url)

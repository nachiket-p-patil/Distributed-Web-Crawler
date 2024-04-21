#!/usr/bin/python3
import os
import sys

graph_pth = sys.argv[1]
output_file = sys.argv[2]

stoi_map = {}
itos_map = {}

neighbors = {}

node_count = 0
with open(graph_pth, 'r') as f:
    # read each line if not empty
    for line in f:
        if line != '\n' and line != ' ' and line != '\t':
            line = line.strip().split(' ')
            node = line[0]
            neighbor = line[1]
            if node not in stoi_map:
                stoi_map[node] = node_count+1
                itos_map[node_count+1] = node
                node_count += 1
            

            if neighbor not in stoi_map:
                stoi_map[neighbor] = node_count+1
                itos_map[node_count+1] = neighbor
                node_count += 1

            if stoi_map[node] not in neighbors:
                neighbors[stoi_map[node]] = []
            if stoi_map[neighbor] not in neighbors[stoi_map[node]]:
                neighbors[stoi_map[node]].append(stoi_map[neighbor])

os.system("rm -rf ./" + output_file)
os.system(f"touch ./{output_file}")
inp_mapred_file = open("./" + output_file, "w")

for i in range(1, node_count+1):
    s = str(i)+"\t"
    s += str(node_count) + " "
    s += str(1/node_count)+" "
    if i in neighbors:
        s += str(len(neighbors[i]))+" "
        for j in neighbors[i]:
            s += str(j)+" "
        
    else:
        s += str(node_count) + " "
        for j in range(1, node_count + 1):
            s += str(j)+" "
    inp_mapred_file.write(s+"\n")
        

inp_mapred_file.close()

with open("itos_map.txt", "w") as f:
    for i in itos_map:
        f.write(str(i) + " " + itos_map[i] + "\n")
#!/usr/bin/python3

# format : page_id \t page_rank \t num_outlinks \t outlink1 \t outlink2 \t ...
# or page_id \t part_page_rank

# Reducer logic for pagerank algo with damping factor = 0.85

import sys

map_sum = {}
map_page = {}


N = 0

for line in sys.stdin:
    
    line = line.strip()
    if line == "":
        continue
    line = line.split('\t')
    page = line[0]
    
    line = line[1].split()
    line.insert(0, page)
    
    if page not in map_sum:
        map_sum[page] = 0

    N = int(line[1])
    if(len(line)>=4):
        map_page[page] = line[1:]
    else:
        map_sum[page] += float(line[2])


for k in map_sum:
    new_page_rank = 0.15/N + 0.85*map_sum[k]
    new_page = str(N) + " " +  str(new_page_rank) + " "
    new_page += map_page[k][2] + " "
    for i in range(3, len(map_page[k])):
        new_page += map_page[k][i] + " "
    print(k + "\t" + new_page)
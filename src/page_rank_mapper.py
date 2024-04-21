#!/usr/bin/python3

# format : page_id \t page_rank \t num_outlinks \t outlink1 \t outlink2 \t ...
# Mapper logic for pagerank algo with damping factor = 0.85

import sys

# read the input from the mapper
for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    print(line)
    line = line.split('\t')
    page = line[0]
    
    line = line[1].split()
    line.insert(0, page)
    
    page_rank = line[2]
    
    num_outlinks = line[3]
    outlinks = line[4:]

    out_page_rank = float(page_rank)/int(num_outlinks)
    for outlink in outlinks:
        print(outlink + '\t' + line[1] + " " + str(out_page_rank))

    
    
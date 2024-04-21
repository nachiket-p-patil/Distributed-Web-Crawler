page_rank = {}

with open("./page_rank_out.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        line = line.split('\t')
        page_rank[line[0]] = line[1].split()[1]

# sort the page rank in descending order
page_rank = sorted(page_rank.items(), key=lambda x: x[0])

itos_map = {}
with open("./itos_map.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        itos_map[int(line[0])] = line[1]

# print all pages
for id in page_rank:
    print(itos_map[int(id[0])], id[1])
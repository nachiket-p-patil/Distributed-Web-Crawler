#!/usr/bin/python3
import os
import sys

# os.system("load module hdfs")

def run_command(cmd):
    print("running: {}".format(cmd))
    os.system(cmd)
if len(sys.argv) > 1:
    jar_file, input_file_local, input_dir, mapper_dir, reducer_dir = sys.argv[1:]
else:
    jar_file, input_file_local, input_dir, mapper_dir, reducer_dir = './hadoop-streaming-3.3.1.jar', './input.txt', '/a/inp', './', './'

# Reading the data from the input file
with open(input_file_local) as f:
    input_url, depth = f.read().strip().split()
    depth = int(depth)

# creating new file to give to mapper
input_file_local = os.path.join(os.path.dirname(input_file_local), "data.txt")
with open(input_file_local, "w") as f:
    f.write(input_url + " 0")

# copying the input file to hdfs
# input_name = os.path.basename(input_file_local)
# run_command(f"hdfs dfs -rm -r {output_dir}")
run_command(f"hdfs dfs -rm -r {input_dir}")
run_command(f"hdfs dfs -mkdir -p {input_dir}")
run_command(f"hdfs dfs -copyFromLocal -f {input_file_local} {input_dir}")
run_command(f"chmod +x {os.path.join(mapper_dir, '*.py')}")
run_command(f"chmod +x {os.path.join(reducer_dir, '*.py')}")
pyth = "/opt/hvenv/bin/python3"

run_command(f"hdfs dfs -rm -r /output_*")


def run_hadoop(input_dir, output_dir, mapper, reducer):
    run_command(f"hadoop jar {jar_file} -input {input_dir} -output {output_dir} -mapper '{pyth} {os.path.join(mapper_dir, mapper)}' -reducer '{pyth} {os.path.join(reducer_dir, reducer)}' -file {os.path.join(mapper_dir, mapper)} -file {os.path.join(reducer_dir, reducer)}")
    
    

for d in range(depth):
    run_command(f"hdfs dfs -rm -r /input_1")
    run_hadoop(input_dir, "/input_1", "mapper.py", "reducer.py")
    run_command(f"hdfs dfs -rm -r {input_dir}")
    # run_command(f"hdfs dfs -rm -r /input_1/_*")
    run_hadoop("/input_1", input_dir, "mapper_2.py", "reducer_2.py")
    run_command(f"hdfs dfs -rm -r /output_{d}")
    run_hadoop("/input_1", f"/output_{d}", "mapper_2.py", "reducer_3.py")
run_command(f"hdfs dfs -cat /output_*/p* > main_out.txt")
run_command(f"hdfs dfs -rm -r {input_dir}")
run_command(f"{pyth} graph.py")


# run_command(f"python3 {os.path.join(mapper_dir, 'mapper.py')} < {input_file_local} | sort | python3 {os.path.join(reducer_dir, 'reducer.py')} ")
# run_command(f"hadoop jar {jar_file} -input {os.path.join(input_dir, input_name)} -output {output_dir} -mapper 'python3 {os.path.join(mapper_dir, 'mapper.py')}' -reducer 'python3 {os.path.join(reducer_dir, 'reducer.py')}' -file {os.path.join(mapper_dir, 'mapper.py')} -file {os.path.join(reducer_dir, 'reducer.py')}")
# run_command(f"hdfs dfs -cat {os.path.join(output_dir, 'part-00000')}")
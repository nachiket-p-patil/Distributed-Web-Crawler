# Readme

## Instructions to run the code:

+ Give input in the input file. It has two inputs., url and depth. Write them with space.
    Example https://www.iiit.ac.in 2
+ Start the docker containers by running:       
```cd docker-hadoop && docker-compose up -d```
+ To exec into the namenode, run `docker exec -it namenode bash`
+ Change the current working directory to the source code directory by running `cd /hadoop/dfs/data/src`
+ To run the code run the following command  
    ``` ./runner_script.py --path_to_HadoopStreamingJar-- --path_to_InputFile-- --input_Directory-- --path_to_MapperDirectory-- --path_to_ReducerDirectory--```

    ```./runner_script.py``` also works if you don't want to give these parameters
+ We get the graph in `network.png`.
+ The outputs are in `main_out.txt`, `result.txt`, and `page_rank_result.txt`.
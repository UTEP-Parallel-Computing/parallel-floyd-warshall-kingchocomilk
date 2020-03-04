# Parallel-Floyd-Warshall

For this assignment you will write a parallel all pairs shortest paths 
algorithm using the Floyd Warshall algorithm. The program will traverse 
an adjacency matrix and determine the shortest path between each pair 
of nodes. You should have functions for determining the starting and 
stopping row for a particular process. 

https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

fwTest.txt is an example input matrix, the result matrix is fwTestResult.txt

Hints: 

* It may be easier to load the files containing text before entering the processing region 
* You will have to work out how to break apart the work, otherwise each mpi program will be performing duplicate work 
* Ideally the rows are split between threads, for example if there are 4 rows and 2 threads thread 0 gets rows 1 and 2 and thread 2 gets 3 and 4
* Example of a serial floyd warshall https://www-m9.ma.tum.de/graph-algorithms/spp-floyd-warshall/index_en.html

## Requirements 

The code should use reasonable decomposition, use reasonable variable names,
and should generally follow good coding standards. 
Important, your assignment should include your name. 

The program shall use the floyd warshal algorithm 
The program shall use mpi to do the work in parallel 
The program shall use an adjacency matrix 
The program shall split work among multiple mpi processes 
The program shall display a portion of the input and final matrices 

#!/usr/bin/env python3

'''
    Author: Jose Eduardo Soto kingchocomilk

    Description: Finds the shortest paths available between all points an and 
    outputs a matrix.
'''

from mpi4py import MPI
import matrixUtils
import argparse

def main():
    parser = argparse.ArgumentParser(description=
                        'Generates the matrix of the shortest paths of a graph.')
    parser.add_argument('-g','--graph', type=str, help=
                        'graph file matrix of numbers for input')
    parser.add_argument('-o','--outputfile', help=
                        'output filename. matrix of shortest paths saved here')
    args = parser.parse_args()
    
    if (args.graph is None):
        print('Missing Graph file. Try --help')
    else:
        print(args.graph)
        finished_matrix,rank = run(matrixUtils.readFromFile(args.graph))
        if (args.outputfile is None):
            matrixUtils.printSubarray(finished_matrix)
        else:
            if (rank == 0):
                print(f'Writing matrix to {args.outputfile}')
                matrixUtils.writeToFile(finished_matrix, args.outputfile);

def run(graph):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    print(rank)
    print(size)
    # num rows / # of threads
    # Its assumed that the graph is a square.
    n = len(graph)
    magnitude = n / size
    begin = int(rank * magnitude)
    end = int((rank + 1) * magnitude)
    for k in range(1, n+1):
        owner = int((size / n) * (k - 1))
        graph[k-1] = comm.bcast(graph[k-1], root=owner)
        for i in range(begin, end):
            if ((i+1) != k):
                for j in range(0, n):
                    if ((j+1) != k):
                        graph[i][j] = min(graph[i][j],
                                          graph[i][k-1] + graph[k-1][j])
    for k in range(1, n+1):
        owner = int((size / n) * (k - 1))
        graph[k-1] = comm.bcast(graph[k-1], root=owner)
    return graph,rank

if __name__ == '__main__':
    main()

from mpi4py import MPI

# simple hello world example

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

print("Hello from process {} of {}!".format(rank, size))

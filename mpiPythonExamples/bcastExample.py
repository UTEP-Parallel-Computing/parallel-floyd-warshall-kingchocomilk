from mpi4py import MPI

# simple broadcast example for mpi

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

msg = "Nothing here"

bcast_sender = 0  # AKA root

if rank is 0:
    msg = "Hi Everybody!"

# broadcast message from root to everyone
recv_msg = comm.bcast(msg, root=bcast_sender)

print(f'Thread {rank} from {bcast_sender} received: {recv_msg}')

    

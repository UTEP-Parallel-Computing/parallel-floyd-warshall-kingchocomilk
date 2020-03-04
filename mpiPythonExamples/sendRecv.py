from mpi4py import MPI

# simple example to show sending and receiving messages

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

# the message to send
msg = "Hello thread 1!"

# thread 0 sends the message
if rank is 0:
    print('Thread 0 sending message')
    # send message to thread 1, with tag of 42
    # tag doesn't matter so much
    comm.send(msg, dest=1, tag=42)
# thread 1 receives it
elif rank is 1:
    # receive a message from thread 0 with tag of 42
    data = comm.recv(source=0, tag=42)
    print('Thread 1 received message')
    print(data)
    

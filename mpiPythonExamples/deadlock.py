from mpi4py import MPI

# mpi example showing send receive deadlock

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

# both threads 

if rank is 0:
    msg = "Hello from thread 0!"

    # wait for a message from thread 1
    print('Thread 0 receving message')
    recvd_msg = comm.recv(source=1, tag=1)
    print(f'Thread 0 received message: {recvd_msg}')

    # send a message to thread 2
    print('Thread 0 sending message')
    comm.send(msg, dest=1, tag=1)
    
elif rank is 1:
    msg = "Hello from thread 1!"

    # wait for a message from thread 0
    print('Thread 1 receving message')
    recvd_msg = comm.recv(source=0, tag=1)
    print(f'Thread 1 received message: {recvd_msg}')

    # send a message to thread 0
    print('Thread 1 sending message')
    comm.send(msg, dest=0, tag=1)
    


    

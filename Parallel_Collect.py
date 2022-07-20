from mpi4py import MPI
import h5py
import psutil
from datetime import datetime
import time
import numpy as np

central_comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.rank

## -- Init Operation -- #
# Start File #
file = h5py.File('parallel_test.hdf5', 'w', driver='mpio', comm=central_comm)

# Rank 0 Clear Data #
if rank == 0:
    file.clear()

# Create First Group - Must #
group = file.create_group('ClusterPi')
sub_group = group.create_group(f"Database of {rank}")

# Test Random Array #
data_arr = np.arange(0,100)
sub_group.create_dataset(f"Dataset of {rank}",data=data_arr)

# Flush Data #
file.flush()
file.close()
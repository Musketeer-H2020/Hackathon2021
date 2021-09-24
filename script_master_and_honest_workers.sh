#!/bin/bash

# This shell script launch the master node with no defences and the eight of the ten workers that are not malicious

 
# First we kill the processes that could be crashed from previous executions
pkill -9 -f "python3 master_hackathon.py"
pkill -9 -f "python3 worker_hackathon.py"

# Secondly, we launch the master node and wait some seconds in order to be ready to receive the worker connections
python3 master_hackathon.py --user masteruser --password masteruser --task_name $1 --scenario 1 &

sleep 15

# Finally, we run eight non malicious workers
python3 worker_hackathon.py --user workeruser0 --password workeruser0 --task_name $1 --id 0 &
python3 worker_hackathon.py --user workeruser1 --password workeruser0 --task_name $1 --id 1 &
python3 worker_hackathon.py --user workeruser2 --password workeruser0 --task_name $1 --id 2 &
python3 worker_hackathon.py --user workeruser3 --password workeruser0 --task_name $1 --id 3 &
python3 worker_hackathon.py --user workeruser4 --password workeruser0 --task_name $1 --id 4 &
python3 worker_hackathon.py --user workeruser5 --password workeruser0 --task_name $1 --id 5 &
python3 worker_hackathon.py --user workeruser6 --password workeruser0 --task_name $1 --id 6 &
python3 worker_hackathon.py --user workeruser7 --password workeruser0 --task_name $1 --id 7 

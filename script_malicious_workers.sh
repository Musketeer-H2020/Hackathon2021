#!/bin/bash

# this script must be executed once before the script_master_and_honest_workers has been executed. It run the two malicious workers.

# First we kill the processes that could be crashed from previous executions
pkill -9 -f "python3 worker_hackathon.py --attack_id"

# Then, we run two malicious workers
python3 worker_hackathon.py  --attack_id 1 --user workeruser8 --password workeruser0 --task_name $1 --attack 1 --id 8 &
python3 worker_hackathon.py  --attack_id 2 --user workeruser9 --password workeruser0 --task_name $1 --attack 2 --id 9 

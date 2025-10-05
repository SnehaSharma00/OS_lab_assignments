# OS Lab Assignment 2: System Startup, Process Creation, and Termination Simulation

# Import required modules
import multiprocessing
import time
import logging


# Sub-Task 1: Initialize Logging

# Setup logger to record timestamped messages with process names
logging.basicConfig(
    filename='process_log.txt',      # Log file name
    level=logging.INFO,              # Log level
    format='%(asctime)s - %(processName)s - %(message)s'
)

# Sub-Task 2: Define a Dummy Process Task

def system_process(task_name):
    """
    Simulates a system process performing a task.
    Logs start and end times with process name.
    """
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate processing delay
    logging.info(f"{task_name} ended")


# Sub-Task 3 & 4: Create Processes, Start, Join, and Shutdown

if __name__ == '__main__':
    print("System Starting...")  # Simulate system boot

    # Create two child processes
    process1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    process2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start processes concurrently
    process1.start()
    process2.start()

    # Wait for processes to finish 
    process1.join()
    process2.join()

    print("System Shutdown.")  # Simulate system shutdown



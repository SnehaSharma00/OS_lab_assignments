"""
Experiment Title: Process Creation and Management Using Python OS Module
Author: [Your Name]
Date: [Date]
"""

import os
import time
import subprocess

# ------------------- Task 1: Process Creation Utility -------------------
def task1_create_processes(n=3):
    print("\n--- Task 1: Process Creation ---")
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}, Message='Hello from child process {i+1}'")
            os._exit(0)
    for _ in range(n):
        os.wait()


# ------------------- Task 2: Command Execution Using exec() -------------------
def task2_execute_commands(commands=["ls", "date"]):
    print("\n--- Task 2: Command Execution using execvp() ---")
    for cmd in commands:
        pid = os.fork()
        if pid == 0:
            print(f"\nExecuting command: {cmd}")
            os.execvp(cmd, [cmd])
        else:
            os.wait()


# ------------------- Task 3: Zombie & Orphan Processes -------------------
def task3_zombie_orphan():
    print("\n--- Task 3: Zombie & Orphan Simulation ---")

    # Zombie Process
    print("\nCreating Zombie Process:")
    pid = os.fork()
    if pid == 0:
        print(f"Zombie Child: PID={os.getpid()}, Parent PID={os.getppid()}")
        os._exit(0)
    else:
        print("Parent sleeping to create zombie...")
        time.sleep(5)
        os.wait()

    # Orphan Process
    print("\nCreating Orphan Process:")
    pid = os.fork()
    if pid == 0:
        time.sleep(3)
        print(f"Orphan Child: PID={os.getpid()}, New Parent PID={os.getppid()}")
        os._exit(0)
    else:
        print("Parent exiting before child completes (child becomes orphan)")
        os._exit(0)


# ------------------- Task 4: Inspecting Process Info from /proc -------------------
def task4_inspect_process(pid):
    print("\n--- Task 4: Inspect Process Info ---")
    try:
        with open(f"/proc/{pid}/status", "r") as f:
            lines = f.readlines()
        name = [l for l in lines if l.startswith("Name:")][0].strip()
        state = [l for l in lines if l.startswith("State:")][0].strip()
        memory = [l for l in lines if l.startswith("VmSize:")][0].strip()
        print(f"{name}\n{state}\n{memory}")

        exe = os.readlink(f"/proc/{pid}/exe")
        print(f"Executable Path: {exe}")

        fds = os.listdir(f"/proc/{pid}/fd")
        print(f"Open File Descriptors: {fds}")
    except Exception as e:
        print(f"Error reading /proc info: {e}")


# ------------------- Task 5: Process Prioritization -------------------
def cpu_task(duration=3):
    start = time.time()
    while time.time() - start < duration:
        pass  # Busy loop to simulate CPU usage

def task5_priority_demo():
    print("\n--- Task 5: Process Prioritization using nice() ---")
    pids = []
    for i, nice_val in enumerate([0, 5, 10]):
        pid = os.fork()
        if pid == 0:
            os.nice(nice_val)
            print(f"Child {i+1} (nice={nice_val}) started, PID={os.getpid()}")
            start = time.time()
            cpu_task()
            print(f"Child {i+1} (nice={nice_val}) finished in {time.time()-start:.2f}s")
            os._exit(0)
        else:
            pids.append(pid)
    for _ in pids:
        os.wait()


# ------------------- Main Driver -------------------
if __name__ == "__main__":
    print("=== OS LAB: Process Creation & Management Simulation ===")

    # Task 1
    task1_create_processes(2)

    # Task 2
    task2_execute_commands(["date", "whoami"])

    # Task 3 (Run separately — terminates parent)
    # Uncomment for demo one by one:
    # task3_zombie_orphan()

    # Task 4
    current_pid = os.getpid()
    task4_inspect_process(current_pid)

    # Task 5
    task5_priority_demo()

    print("\n=== End of Experiment ===")

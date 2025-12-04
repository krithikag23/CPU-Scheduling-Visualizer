from schedulers.fcfs import fcfs
from schedulers.sjf import sjf
from schedulers.rr import rr
from utils.visualize import gantt_chart
from utils.metrics import calculate_metrics

# Sample process list: (process_id, burst_time, arrival_time)
processes = [
    ('P1', 5, 0),
    ('P2', 3, 1),
    ('P3', 8, 2),
    ('P4', 6, 3)
]

print("\n--- CPU Scheduling Visualizer ---")
print("1. FCFS")
print("2. SJF")
print("3. Round Robin")

choice = int(input("Choose Algorithm: "))

if choice == 1:
    schedule = fcfs(processes)
elif choice == 2:
    schedule = sjf(processes)
elif choice == 3:
    quantum = int(input("Enter Quantum: "))
    schedule = rr(processes, quantum)

print("\nTimeline:", schedule)
gantt_chart(schedule)
calculate_metrics(schedule)
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
def calculate_metrics(schedule):
    waiting = {}
    turnaround = {}

    first_occurrence = {}
    finish_time = {}

    for pid, start, end in schedule:
        if pid not in first_occurrence:
            first_occurrence[pid] = start
        finish_time[pid] = end

    burst = {}
    for pid, start, end in schedule:
        burst[pid] = burst.get(pid, 0) + (end-start)

    for pid in burst:
        turnaround[pid] = finish_time[pid] - 0  # arrival = 0 for simplicity
        waiting[pid] = turnaround[pid] - burst[pid]

    print("\nProcess\tWaiting\tTurnaround")
    for pid in burst:
        print(f"{pid}\t{waiting[pid]}\t{turnaround[pid]}")

def sjf(processes):
    time = 0
    completed = []
    schedule = []

    while len(completed) < len(processes):
        available = [p for p in processes if p not in completed and p[2] <= time]
        if not available:
            time += 1
            continue
        pid, bt, at = min(available, key=lambda x: x[1])
        schedule.append((pid, time, time + bt))
        time += bt
        completed.append((pid, bt, at))
    return schedule

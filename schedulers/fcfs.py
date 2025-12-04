def fcfs(processes):
    time = 0
    schedule = []
    for pid, bt, at in processes:
        if time < at:
            time = at
        schedule.append((pid, time, time + bt))
        time += bt
    return schedule

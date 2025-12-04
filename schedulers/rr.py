def rr(processes, quantum):
    queue = [(pid, bt, at) for pid, bt, at in processes]
    time = 0
    schedule = []
    ready = []

    while queue or ready:
        ready += [p for p in queue if p[2] <= time]
        queue = [p for p in queue if p[2] > time]

        if not ready:
            time += 1
            continue
        
        pid, bt, at = ready.pop(0)
        exec_time = min(bt, quantum)
        schedule.append((pid, time, time + exec_time))
        if bt > quantum:
            ready.append((pid, bt - quantum, time + exec_time))
        time += exec_time
    return schedule

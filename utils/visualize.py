import matplotlib.pyplot as plt

def gantt_chart(schedule):
    for pid, start, end in schedule:
        plt.barh(1, end-start, left=start, edgecolor='black')
        plt.text((start + end)/2, 1, pid, ha='center', va='center')

    plt.title("Gantt Chart")
    plt.xlabel("Time")
    plt.yticks([])
    plt.show()

# ============================================================
# Lab Assignment-1 | Operating System Lab ENCA252
# BCA (AI & DS) | CPU Scheduling: FCFS & SJF
# RAKESH G  2401201064  BCA (AI & DS) - 'B'
# ============================================================

import os

# ============================================================
# TASK 1: Process Class & Input Handling
# ============================================================

class Process:
    """Represents an OS process with PID, Arrival Time, Burst Time."""
    def __init__(self, pid, at, bt):
        self.pid = pid          # Process ID
        self.at  = at           # Arrival Time
        self.bt  = bt           # Burst Time
        self.ct  = 0            # Completion Time
        self.tat = 0            # Turnaround Time
        self.wt  = 0            # Waiting Time

def get_processes():
    """Accept process input from the user (minimum 4-5 processes)."""
    processes = []
    print("\n" + "="*55)
    print("         CPU SCHEDULING SIMULATOR")
    print("="*55)
    print("\nEnter number of processes (minimum 4): ", end="")
    n = int(input())
    while n < 4:
        print("Please enter at least 4 processes: ", end="")
        n = int(input())

    print()
    for i in range(n):
        print(f"  Process {i+1}:")
        pid = input(f"    PID        : ")
        at  = int(input(f"    Arrival Time: "))
        bt  = int(input(f"    Burst Time  : "))
        processes.append(Process(pid, at, bt))
        print()

    return processes

def display_input_table(processes):
    """Display processes in tabular format (Task 1 output)."""
    print("\n" + "-"*45)
    print("  PROCESS INPUT TABLE")
    print("-"*45)
    print(f"  {'PID':<8} {'Arrival Time':<16} {'Burst Time'}")
    print("-"*45)
    for p in processes:
        print(f"  {p.pid:<8} {p.at:<16} {p.bt}")
    print("-"*45)

def display_results_table(processes, title):
    """Display scheduling results in tabular format."""
    print(f"\n  {'PID':<8} {'AT':<6} {'BT':<6} {'CT':<6} {'TAT':<6} {'WT'}")
    print("  " + "-"*40)
    for p in processes:
        print(f"  {p.pid:<8} {p.at:<6} {p.bt:<6} {p.ct:<6} {p.tat:<6} {p.wt}")
    print("  " + "-"*40)

    avg_tat = sum(p.tat for p in processes) / len(processes)
    avg_wt  = sum(p.wt  for p in processes) / len(processes)
    print(f"  Average TAT : {avg_tat:.2f}")
    print(f"  Average WT  : {avg_wt:.2f}")
    return avg_tat, avg_wt


# ============================================================
# TASK 2: FCFS Scheduling
# ============================================================

def fcfs(processes):
    """
    First Come First Serve (Non-Preemptive) Scheduling.
    Sorts processes by Arrival Time and executes in order.
    """
    import copy
    procs = copy.deepcopy(processes)

    # Sort by Arrival Time
    procs.sort(key=lambda p: p.at)

    current_time = 0
    gantt = []  # For Gantt chart

    for p in procs:
        # Handle CPU idle if no process has arrived yet
        if current_time < p.at:
            gantt.append(("IDLE", current_time, p.at))
            current_time = p.at

        start_time = current_time
        current_time += p.bt          # Execute process
        p.ct  = current_time          # Completion Time
        p.tat = p.ct - p.at           # Turnaround Time
        p.wt  = p.tat - p.bt          # Waiting Time
        gantt.append((p.pid, start_time, p.ct))

    return procs, gantt


# ============================================================
# TASK 3: SJF Scheduling (Non-Preemptive)
# ============================================================

def sjf(processes):
    """
    Shortest Job First (Non-Preemptive) Scheduling.
    At each step, picks the arrived process with smallest Burst Time.
    """
    import copy
    procs = copy.deepcopy(processes)

    completed  = []
    remaining  = list(procs)
    current_time = 0
    gantt = []

    while remaining:
        # Filter processes that have arrived by current_time
        available = [p for p in remaining if p.at <= current_time]

        if not available:
            # CPU idle — jump to next arriving process
            next_at = min(p.at for p in remaining)
            gantt.append(("IDLE", current_time, next_at))
            current_time = next_at
            continue

        # Pick process with shortest burst time (SJF selection)
        shortest = min(available, key=lambda p: p.bt)
        remaining.remove(shortest)

        start_time   = current_time
        current_time += shortest.bt
        shortest.ct  = current_time
        shortest.tat = shortest.ct - shortest.at
        shortest.wt  = shortest.tat - shortest.bt
        gantt.append((shortest.pid, start_time, shortest.ct))
        completed.append(shortest)

    return completed, gantt


# ============================================================
# TASK 4: Gantt Chart Representation
# ============================================================

def draw_gantt_chart(gantt, title):
    """Draw a text-based Gantt chart showing execution timeline."""
    print(f"\n  GANTT CHART — {title}")
    print("  " + "-"*60)

    # Top bar (process boxes)
    bar = "  |"
    for (pid, start, end) in gantt:
        label = str(pid).center(max(end - start, len(str(pid)) + 2))
        bar += label + "|"
    print(bar)

    # Timeline row
    timeline = "  "
    prev_end = None
    for (pid, start, end) in gantt:
        width = max(end - start, len(str(pid)) + 2)
        if prev_end is None:
            timeline += str(start).ljust(width + 1)
        else:
            timeline += str(start).center(width + 1)
        prev_end = end
    timeline += str(gantt[-1][2])
    print(timeline)
    print("  " + "-"*60)


# ============================================================
# TASK 5: Performance Analysis & Comparison
# ============================================================

def compare_algorithms(fcfs_procs, sjf_procs):
    """Compare FCFS and SJF based on Avg WT and Avg TAT."""
    fcfs_avg_tat = sum(p.tat for p in fcfs_procs) / len(fcfs_procs)
    fcfs_avg_wt  = sum(p.wt  for p in fcfs_procs) / len(fcfs_procs)
    sjf_avg_tat  = sum(p.tat for p in sjf_procs)  / len(sjf_procs)
    sjf_avg_wt   = sum(p.wt  for p in sjf_procs)  / len(sjf_procs)

    print("\n" + "="*55)
    print("  PERFORMANCE COMPARISON: FCFS vs SJF")
    print("="*55)
    print(f"  {'Metric':<28} {'FCFS':>8}   {'SJF':>8}")
    print("  " + "-"*44)
    print(f"  {'Average Turnaround Time':<28} {fcfs_avg_tat:>8.2f}   {sjf_avg_tat:>8.2f}")
    print(f"  {'Average Waiting Time':<28} {fcfs_avg_wt:>8.2f}   {sjf_avg_wt:>8.2f}")
    print("  " + "-"*44)

    print("\n  ANALYSIS:")
    if sjf_avg_wt < fcfs_avg_wt:
        diff = fcfs_avg_wt - sjf_avg_wt
        print(f"  SJF is BETTER than FCFS.")
        print(f"  SJF reduces Average Waiting Time by {diff:.2f} units.")
        print(f"\n  WHY?")
        print("  SJF always picks the shortest available job, minimizing")
        print("  the time longer processes wait. FCFS executes in arrival")
        print("  order, which can cause the 'convoy effect' — short jobs")
        print("  stuck behind long ones — leading to higher waiting time.")
    else:
        print("  FCFS performs similarly or better for this input.")
        print("  This can happen when processes arrive in order of BT.")

    print("\n  TRADE-OFFS:")
    print("  FCFS : Simple, fair, no starvation. Poor avg WT.")
    print("  SJF  : Optimal avg WT, but needs BT prediction &")
    print("         can cause starvation of long processes.")
    print("="*55)


# ============================================================
# MAIN — Run all tasks
# ============================================================

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    # ---------- TASK 1: Input ----------
    print("\n>>> TASK 1: Process Input")
    processes = get_processes()
    display_input_table(processes)

    # ---------- TASK 2: FCFS ----------
    print("\n\n>>> TASK 2: FCFS Scheduling")
    print("="*55)
    fcfs_result, fcfs_gantt = fcfs(processes)
    print("  FCFS RESULTS:")
    fcfs_avg_tat, fcfs_avg_wt = display_results_table(fcfs_result, "FCFS")

    # ---------- TASK 3: SJF ----------
    print("\n\n>>> TASK 3: SJF Scheduling (Non-Preemptive)")
    print("="*55)
    sjf_result, sjf_gantt = sjf(processes)
    print("  SJF RESULTS:")
    sjf_avg_tat, sjf_avg_wt = display_results_table(sjf_result, "SJF")

    # ---------- TASK 4: Gantt Charts ----------
    print("\n\n>>> TASK 4: Gantt Chart Representation")
    print("="*55)
    draw_gantt_chart(fcfs_gantt, "FCFS")
    draw_gantt_chart(sjf_gantt,  "SJF")

    # ---------- TASK 5: Comparison ----------
    print("\n\n>>> TASK 5: Performance Analysis & Comparison")
    compare_algorithms(fcfs_result, sjf_result)

    print("\n  Done! Submit this file + screenshots to LMS.\n")


if __name__ == "__main__":
    main()
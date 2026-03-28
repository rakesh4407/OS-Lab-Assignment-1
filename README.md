# 🖥️ OS Lab Assignment 1 — CPU Scheduling Algorithms (FCFS & SJF)

**Course:** Operating System Lab — ENCA252  
**Program:** BCA (AI & DS) (Research)  
**School:** School of Engineering and Technology  

---

## 📌 Problem Statement

Implementation and Analysis of CPU Scheduling Algorithms — **First Come First Serve (FCFS)** and **Shortest Job First (SJF)**.

---

## 🎯 Learning Objectives

- Understand CPU scheduling concepts and process attributes
- Implement FCFS and SJF scheduling algorithms using Python
- Calculate Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT)
- Visualize execution order using Gantt charts
- Analyze and compare performance of scheduling algorithms

---

## 🛠️ Tools & Technology

| Tool | Details |
|------|---------|
| Language | Python 3.x |
| Libraries | `os`, `copy` (built-in) |
| IDE | Visual Studio Code |
| Platform | Windows 11 |

---

## 📁 Repository Structure

```
OS-Lab-Assignment-1/
│
├── Cpu_scheduling.py                  # Main Python source code
├── OS_Lab_Assignment1_Report.pdf      # Summary report
├── Steps.md                           # Steps to run the program
│
├── Task 1 — Process input values.jpeg # Screenshot: process input
├── Task 1 — Process input table.png   # Screenshot: input table
├── Task 2 — FCFS results.png          # Screenshot: FCFS output
├── Task 3 — SJF results.png           # Screenshot: SJF output
├── Task 4 — Gantt charts.png          # Screenshot: Gantt charts
├── Task 5 — Comparison & analysis.png # Screenshot: performance comparison
│
└── README.md                          # This file
```

---

## ▶️ How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/rakesh4407/OS-Lab-Assignment-1.git
cd OS-Lab-Assignment-1
```

**2. Run the Python script:**
```bash
python Cpu_scheduling.py
```

**3. Enter process details when prompted:**
```
Enter number of processes (minimum 4): 5

Process 1:
  PID        : P1
  Arrival Time: 0
  Burst Time  : 6
...
```

---

## 📊 Sample Input & Output

### Process Input Table

| PID | Arrival Time (AT) | Burst Time (BT) |
|-----|-------------------|-----------------|
| P1  | 0                 | 6               |
| P2  | 2                 | 8               |
| P3  | 4                 | 7               |
| P4  | 6                 | 3               |
| P5  | 8                 | 4               |

---

### Task 2 — FCFS Results

| PID | AT | BT | CT | TAT | WT |
|-----|----|----|----|-----|----|
| P1  | 0  | 6  | 6  | 6   | 0  |
| P2  | 2  | 8  | 14 | 12  | 4  |
| P3  | 4  | 7  | 21 | 17  | 10 |
| P4  | 6  | 3  | 24 | 18  | 15 |
| P5  | 8  | 4  | 28 | 20  | 16 |

**Average TAT = 14.60 | Average WT = 9.00**

**Gantt Chart:**
```
| P1 | P2 | P3 | P4 | P5 |
0    6    14   21   24   28
```

---

### Task 3 — SJF Results

| PID | AT | BT | CT | TAT | WT |
|-----|----|----|----|-----|----|
| P1  | 0  | 6  | 6  | 6   | 0  |
| P4  | 6  | 3  | 9  | 3   | 0  |
| P5  | 8  | 4  | 13 | 5   | 1  |
| P3  | 4  | 7  | 21 | 17  | 10 |
| P2  | 2  | 8  | 28 | 26  | 18 |

**Average TAT = 11.40 | Average WT = 5.80**

**Gantt Chart:**
```
| P1 | P4 | P5 | P3 | P2 |
0    6    9    13   21   28
```

---

### Task 5 — Performance Comparison

| Metric              | FCFS   | SJF    |
|---------------------|--------|--------|
| Avg Turnaround Time | 14.60  | 11.40  |
| Avg Waiting Time    | 9.00   | 5.80   |
| Starvation Risk     | No     | Yes    |
| Complexity          | Simple | Moderate |

**✅ SJF is better** — it reduces Average Waiting Time by **3.20 units** compared to FCFS.

---

## 🧠 Code Structure

| Function | Description |
|----------|-------------|
| `Process` class | Stores PID, AT, BT, CT, TAT, WT |
| `get_processes()` | Takes user input for N processes |
| `fcfs()` | Implements FCFS scheduling |
| `sjf()` | Implements SJF scheduling (non-preemptive) |
| `draw_gantt_chart()` | Displays Gantt chart with timeline |
| `compare_algorithms()` | Compares performance of both algorithms |
| `main()` | Controls execution flow of all tasks |

---

## 📝 Conclusion

This assignment successfully implemented and analyzed FCFS and SJF scheduling algorithms. SJF provides better performance by minimizing average waiting and turnaround time, but may cause starvation for longer processes.

---

## 👤 Author

**Rakesh** — BCA (AI & DS) | ENCA252 Operating System Lab

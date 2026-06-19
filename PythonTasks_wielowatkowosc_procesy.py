"""
    Zadania z pliku PythonTasks - wielawątkowość i procesy
"""

#   INPUT
import time
import threading
import multiprocessing


"""def task(number):
    print(f"Start zadania {number}")
    time.sleep(1)
    print(f"Koniec zadania {number}")


start = time.perf_counter()
threads = []

for i in range(1, 6):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"Czas wykonania: {end - start:.2f} sekund")



start = time.perf_counter()
counter = 0
threads = []
lock = threading.Lock()

def increment():
    with lock:
        global counter

        for _ in range(10_000):
            temp = counter
            time.sleep(0.000001)
            counter = temp + 1

for i in range(9):
    thread = threading.Thread(target=increment())
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"Czas wykonania: {end - start:.2f} sekund")

print(counter)
print("\n\n")



processes = []

if __name__ == "__main__":
    start = time.perf_counter()

    for i in range(1, 6):
        process = multiprocessing.Process(target=task, args=(i, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end = time.perf_counter()

    print(f"Czas wykonania: {end - start:.2f} sekund")

"""

results = {}


def task(worker, rep_number):
    print(f"{worker} start")

    total = 0

    for i in range(rep_number):
        total += i * i

    print(f"{worker} koniec")


def thread_task(workers, rep_number):
    threads = []

    for i in range(1, workers + 1):
        thread = threading.Thread(target=task, args=(i, rep_number))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


workers = [1, 2, 4, 8, 16]
rep_number = [1_000_000, 100_000_000]

for rn in rep_number:
    print(f"Task for process - {rn} rep_numbers\n")
    start = time.perf_counter()

    task(1, rn)

    end = time.perf_counter()
    results[rn] = f"{end - start:.5f}"
    print("\n")

    for w in workers:
        print(f"Thread task for {w} workers - {rn} rep_numbers\n")
        start = time.perf_counter()

        thread_task(w, rn)

        end = time.perf_counter()
        results[" - ".join([str(rn), str(w)])] = f"{end - start:.5f}"
        print("\n")



import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.axis("tight")
ax.axis("off")

tabela = ax.table(
    cellText=list(results.items()),
    colLabels=[
        "Ilość obliczeń / wątki",
        "Czas wykonania"
    ],
    loc="center",
    cellLoc="center"
)
tabela.set_fontsize(10)
tabela.scale(0.8, 1.0)
plt.show()

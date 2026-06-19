import queue
import threading
import time


kolejka = queue.Queue()

# bariera aby watki startowały w tym samym czasie
start_barrier = threading.Barrier(2)


def producent():
    start_barrier.wait()

    for i in range(1, 11):
        kolejka.put(i)
        print(f"Produkcja: {i}")
        time.sleep(0.1)


def konsument():
    start_barrier.wait()

    for _ in range(1, 11):
        item = kolejka.get()
        print(f"Konsument: {item}")
        kolejka.task_done()


thread_prod = threading.Thread(target=producent)
thread_kons = threading.Thread(target=konsument)

start = time.perf_counter()

thread_prod.start()
thread_kons.start()

thread_prod.join()
thread_kons.join()

end = time.perf_counter()
print(f"Wszystko zostało wykonane: {end - start:.4f}")


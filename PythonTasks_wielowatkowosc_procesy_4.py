import queue
import threading
import multiprocessing

def przekaz_wartosc(x, q):
    result = x + 1
    q.put(result)

q = queue.Queue()

t = threading.Thread(target=przekaz_wartosc, args=(9, q))
t.start()
t.join()

result = q.get()
print(result)

def kwadrat(x):
    return x * x

if __name__ == "__main__":
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=przekaz_wartosc, args=(9, q))
    p.start()
    p.join()

    result = q.get()
    print(result)

    with multiprocessing.Pool(4) as pool:
        result = pool.map(kwadrat, [1, 2, 3, 4])

    print(result)

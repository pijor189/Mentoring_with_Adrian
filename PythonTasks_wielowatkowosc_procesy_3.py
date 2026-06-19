import multiprocessing


counter = 0
processing = []

def increment():
    global counter

    counter += 1

if __name__ == "__main__":
    for _ in range(5):
        process = multiprocessing.Process(target=increment)
        processing.append(process)
        process.start()

    for process in processing:
        process.join()

    print(counter)

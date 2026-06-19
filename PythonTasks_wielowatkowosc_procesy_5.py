import threading
import numpy as np
import matplotlib.pyplot as plt


COLORS = [
    (255, 0, 0),    # czerwony
    (0, 255, 0),    # zielony
    (0, 0, 255),    # niebieski
    (255, 255, 0),  # żółty
    (255, 0, 255),  # magenta
    (0, 255, 255),  # cyan
    (255, 128, 0),  # pomarańczowy
    (128, 0, 255)   # fioletowy
]

img = np.zeros((1000, 1000, 3), dtype=np.uint8)

def wypelnij_obraz_kolorami(img, x_start, x_end, y_start, y_end, kolor):
    img[y_start:y_end, x_start:x_end] = kolor

threads = []
zakres = 1000 // len(COLORS)
temp = 0

for kolor in COLORS:
    y_start = temp
    temp += zakres
    y_end = temp

    t = threading.Thread(
        target=wypelnij_obraz_kolorami,
        args=(img, 0, 1000, y_start, y_end, kolor)
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()

plt.imshow(img)
plt.axis("off")
plt.show()

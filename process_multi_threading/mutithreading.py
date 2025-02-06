import threading
import time
def print_number():
    for i in range(5):
        print(i)
def print_letter():
    for ch in "grins":
        print(f"letter : {ch}");
t1 = threading.Thread(target=print_number);
t2 = threading.Thread(target=print_letter);
t = time.time()
t1.start();
t2.start();

t1.join()
t2.join()
print(time.time()-t);
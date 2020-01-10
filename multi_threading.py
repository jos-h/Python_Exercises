import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.info("Thread %s: is entering in lock mode", name)
        with self._lock:
            logging.info("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.info("Thread %s about to release lock", name)
        logging.info("Thread %s after release lock", name)
        logging.info("Thread %s: finishing update", name)


def foo(name):
    logging.info("Thread %s: start", name)
    time.sleep(2)
    logging.info("Thread %s: end", name)


def single_thread():
    logging.info("Main  : before thread creation")
    x = threading.Thread(target=foo, args=(1,), daemon=False)
    x.start()
    logging.info("Main: waiting for thread to finish")
    x.join()
    logging.info("Main: work done")


def multiple_threads():
    threads = list()
    for i in range(3):
        logging.info("Main  : create and start thread %d", i)
        x = threading.Thread(target=foo, args=(i,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main      : before joining thread %d", index)
        thread.join()
        logging.info("Main      : thread %d done", index)


def thread_pool_executor_demo():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(foo, range(3))


def fake_database_race_condition():
    db = FakeDatabase()
    logging.info("Testing update.   Starting value is %d.", db.value)

    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(2):
            executor.submit(db.update, i)
    logging.info("Testing update.   Ending value is %d", db.value)


def main():
    format_str = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # single_thread()
    # multiple_threads()
    # thread_pool_executor_demo()
    fake_database_race_condition()


if __name__ == '__main__':
    main()

############

# Streaming Payments Processor, two vendors edition.

#

# We decided to improve the payment processor from the previous

# exercise and hired two vendors. One was to implement `stream_payments()`

# function, and another `store_payments()` function.

#

# The function `process_payments_2()` is processing a large, but finite

# amount of payments in a streaming fashion.

#

# Unfortunately the vendors did not coordinate their efforts, and delivered

# their functions with incompatible APIs.

#

# TODO: Your task is to analyse the APIs of `stream_payments()` and

# `store_payments()` and to write glue code in `process_payments_2()`

# that allows us to store the payments using these vendor functions.

#

# NOTE: you need to take into account the following restrictions:

# - You are allowed only one call each to `stream_payments()` and

#      to `store_payments()`

# - You can not read from the storage.

# - You can not use disk as temporary storage.

# - Your system has limited memory that can not hold all payments.

#

############
import _thread
import threading
import time
import logging
from queue import Queue, Empty


# This is a library function, you can't modify it.

def stream_payments(callback_fn):
    """

    Reads payments from a payment processor and calls `callback_fn(amount)`

    for each payment.



    Returns when there is no more payments.

    """

    # Sample implementation to make the code run in coderpad.

    # Do not rely on this exact implementation.

    for i in range(10):
        callback_fn(i)


# This is a library function, you can't modify it.

def store_payments(amount_iterator):
    """

    Iterates over the payment amounts from amount_iterator

    and stores them to a remote system.

    """

    # Sample implementation to make the code run in coderpad.

    # Do not rely on this exact implementation.

    for i in amount_iterator:
        print(i)


def callback_example(amount):
    print(amount)

    return True


def process_payments_2():
    """

    TODO:

    Modify `process_payments_2()`, write glue code that enables

    `store_payments()` to consume payments produced by `stream_payments()`

    """

    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-9s) %(message)s', )

    BUF_SIZE = 100
    q = Queue(BUF_SIZE)

    class ProducerThread:

        def set_message(self, data):
            if not q.full():
                q.put(data)
                logging.debug(f'Queue: stream_payments: {data}')

        def get_producer(self, data):
            try:
                # self.set_message(data)
                time.sleep(0.1)
                _thread.start_new_thread(self.set_message, (data,))
            except Exception:
                raise

    class ConsumerThread(threading.Thread):
        def __init__(self, group=None, target=None, name='Consumer',
                     args=(), kwargs=None, verbose=None):
            super(ConsumerThread, self).__init__()
            self.target = target
            self.name = name
            return

        def run(self):
            amount_iterator = []
            while not q.empty():
                try:
                    data = q.get(False)
                    amount_iterator.append(data)
                except Empty:
                    pass
            logging.debug(f'Queue: store_payments: {amount_iterator}')
            store_payments(amount_iterator)

    stream_payments(ProducerThread().get_producer)
    time.sleep(1)
    ConsumerThread().run()


process_payments_2()

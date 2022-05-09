# GÉANT Basic Python assessment questions


1. Write a method that accepts an iterable of integers
   as input and returns an iterable containing all prime
   integers.


2. Write a generator method that accepts an iterable of integers
   as input and, rather than pre-computing an entire 
   list before returning, yields prime values one-by-one
   as they are discovered (maybe you already did this
   in your solution to #1)


3. Write a method that distributes the above work
   over a specified number of threads.  As a hint (you don't
   need to use this method), here's a bit of
   copy/pasted from the Python 3 documentation
   (cf. [Queue.join()](https://docs.python.org/3/library/queue.html#queue.Queue.join)):
```json
      import threading, queue
      
      q = queue.Queue()
      
      def worker():
          while True:
              item = q.get()
              print(f'Working on {item}')
              print(f'Finished {item}')
              q.task_done()
      
      # Turn-on the worker thread.
      threading.Thread(target=worker, daemon=True).start()
      
      # Send thirty task requests to the worker.
      for item in range(30):
          q.put(item)
      
      # Block until all tasks are done.
      q.join()
      print('All work completed')
```

import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from monkey import Monkey

path = 'folder path to search for images'

monkey = Monkey()
observer = Observer()
observer.schedule(monkey, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from poster import postBot
from description_dictionary import description


path = 'folder path to search for images'
posts_folder = 'folder path to put the renamed images'


class Monkey(FileSystemEventHandler):

    """Just a Monkey that search for new files and calls the Post Bot."""

    def on_modified(self, event):
        self.i = 1
        time.sleep(5)
        for filename in os.listdir(path):
            print("Verifying files.")
            new_name = "post_" + str (self.i) + ".jpg"
            exists = True

            while exists:
                file_exists = os.path.isfile(posts_folder + "/" + new_name)
                if file_exists:
                    print("Default name in use, trying another.")
                    self.i += 1
                    new_name = "post_" + str (self.i) + ".jpg"
                
                else:
                    exists = False

            src = path + "/" + filename
            print(f'The file {filename} has been renamed as {new_name}.')
            new_src = posts_folder + "/" + new_name
            os.rename(src, new_src)
            post_description = description[new_name]

            postBot(new_src, post_description)

#!/usr/bin/env python3

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
import os
import json
import time

class Watcher:
    folder_to_track = 'C:/Users/marcu/Desktop/firsttest'

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = MyHandler()
        self.observer.schedule(event_handler, self.folder_to_track, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(10)

        except KeyboardInterrupt:
            print('stop')
            self.observer.stop()


class MyHandler(FileSystemEventHandler):
    folder_destination = 'C:/Users/marcu/Desktop/secondtest'
    folder_to_track = 'C:/Users/marcu/Desktop/firsttest'

    def on_modified(self, event):
        print ("!!!new modification")
        for filename in os.listdir(self.folder_to_track):
            txt_extension = "txt"
            excel_extension = "xlsx"
            if txt_extension in filename:
                print ("its .%s extension type: " %(txt_extension))
                src = self.folder_to_track + "/" + filename
                new_destination = self.folder_destination + "/" + filename
                os.rename(src, new_destination)
                print ("moved to the folder: %s \nEND\n" %(self.folder_destination + "/"))                
            elif excel_extension in filename:
                print ("its .%s extension type: " %(excel_extension))
                src = self.folder_to_track + "/" + filename
                new_destination = self.folder_destination + "/exce/" + filename
                os.rename(src, new_destination)            
                print ("moved to the folder: %s \nEND\n" %(self.folder_destination + "/exce/"))                
            else:
                print ("file not moved, extension unknown\nEND\n")


if __name__ == '__main__':
    w = Watcher()
    w.run()

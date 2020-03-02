import sys
import os.path
import threading
import time
import base64
import binascii
import re


from work.image_viewer_mod import image_show_API 



class imageSelector():

    def __init__(self):
        
        self.string = ''
        self.stop_thread = False
        self.image_selector()


            
            

    def image_selector(self):
        while(True):

            self.string = input("What picture to display: ")
        #    self.input_by_file()
          #  print(self.string)
            if self.check_if_base64():
                print("base64")
                self.base64_to_image()
                self.string = 'tempImage'

            if os.path.isfile('assets/' + self.string + '.jpg'):
                stop_thread = True
                time.sleep(0.1)
                stop_thread = False        
                arg = "assets/" + self.string + ".jpg"
                self.thread = threading.Thread(target=image_show_API, args=(arg,lambda : stop_thread),daemon=True)
                self.thread.start()
                
            elif(self.string == "cancel"):
                stop_thread = True
                self.thread.join()

            elif(self.string == "quit"):
                stop_thread = True
                self.thread.join()
                break

            else:
                print("Try again")


    def base64_to_image(self):
        with open("assets/tempImage.jpg", "wb") as fh:
            fh.write(base64.decodebytes(self.string.encode('utf-8')))

    def check_if_base64(self):
        return re.search("==$", self.string)


    def input_by_file(self):
            # with open("assets/string.txt", "w") as file_string:
            #     file_string.write(input("What picture to display: "))
            input("base 64 image")
            with open("assets/string.txt", "r") as file_string:
                self.string = file_string.read()



img = imageSelector()
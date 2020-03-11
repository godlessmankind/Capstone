#!~/capstone/venv_capstone/bin/python
import sys
import os.path
import concurrent.futures
import time
import base64
import binascii
import re


import threading


from work.image_viewer_mod import image_show_API 
import work.bluetooth_server as bluetooth_server


class imageSelector():

    def __init__(self):
        
        self.__correct_folder()
        self.string = ''
        self.bt = bluetooth_server.bt_server()
        self.image_selector()
        



    def image_selector(self):
                
        while(True):

            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            f1 = executor.submit(self.bt.recive_data)
            self.string = f1.result()


           # self.string = input("What picture to display: ")
           # self.input_by_file()
           # print(self.string)

            
            if self.check_if_base64():
                print("base64")
                self.base64_to_image()
                self.string = 'tempImage'

            if os.path.isfile(f'assets/{self.string}.jpg'):
                stop_thread = True
                time.sleep(0.1)
                stop_thread = False        
                arg = f'assets/{self.string}.jpg'
                
                
                thread = threading.Thread(target=image_show_API, args=(arg,lambda : stop_thread),daemon=True)
                thread.start()
                


            elif(self.string == "cancel"):
                stop_thread = True
                thread.join()
                executor.shutdown()

            elif(self.string == "quit"):
                stop_thread = True
                thread.join()
                executor.shutdown()
                break

            else:
                print("Try again")

    def base64_to_image(self):
        with open("assets/tempImage.jpg", "wb") as fh:
            fh.write(base64.decodebytes(self.string.encode('utf-8')))

    def check_if_base64(self):
        return re.search("==$", self.string)

    def input_by_file(self):
            input("base 64 image")
            with open("assets/string.txt", "r") as file_string:
                self.string = file_string.read()


    def __correct_folder(self):
        PRJ_FLDR = os.path.dirname(os.path.realpath(__file__))
        if os.getcwd() != PRJ_FLDR:
            os.chdir(PRJ_FLDR)


def main():
     imageSelector()

if __name__ == '__main__':
    main()       
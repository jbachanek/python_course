import os
import shutil as sht

source_dir="/home/kuba/PycharmProjects/python_course/resources/lab2/files"
output_dir="/home/kuba/PycharmProjects/python_course/mysolution/lab3_trening"

for file in os.listdir(source_dir):
    if os.path.isfile(source_dir+os.sep+file):
        with open(source_dir+os.sep+file, "r") as read_file:
            folder_name= read_file.read().replace(" ","").split(":")[1]
            if not os.path.exists(output_dir+os.sep+folder_name):
                os.mkdir(output_dir+os.sep+folder_name)
            sht.copy(source_dir+os.sep+file, output_dir+os.sep+folder_name+os.sep+file)
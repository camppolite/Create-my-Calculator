import os

file_dir = os.getcwd()
for root, dirs, files in os.walk(file_dir):  
    for file in files:
        print(file) #��ǰ·�������з�Ŀ¼���ļ�  

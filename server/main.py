#Antar Chandra Nath
import glob
import shutil
import os
from zipfile import ZipFile
import time

source_path = '../source/*'
destination_path = '../destination'

postfix = [1, 2, 3]

while True:
    
    source_object = glob.glob(source_path) # ['../source\\some.txt'] 

    # print(source_object)

    for object_path in source_object:


        print(source_object)

        if len(source_object) > 0:

            # object_path = source_object[0]  # '../source\\some.txt'
            # print(object_path)
            shutil.copy(object_path, '.')

            lines = None
            with open(object_path.split('\\')[-1], 'r') as file:
                lines = file.readlines()


            object_name = object_path.split('\\')[-1].split('.')  #['some', 'txt']

            prefix = object_name[0]
            postfix2 = object_name[1]

            if postfix2 == 'txt':

                j=1
                for item in range(len(postfix)):
                    file_name = prefix + '_' + str(item+1) + '.' + postfix2
                    with open(file_name, 'w') as file:
                        i = 0
                        for line in lines:
                            
                            if j==1 and i==10:
                                break
                            elif j==2 and i==20:
                                break
                            elif j==3 and i==30:
                                break
                            file.write(line)
                            i+=1
                        j+=1

                all_txt_file_path = []

                for item in range(len(postfix)):
                    filename = prefix + '_' + str(item+1) + '.' + postfix2
                    # print(filename)
                    all_txt_file_path.append(filename)
                    shutil.copy(filename, f'{destination_path}/{filename}')
                Zipfile = prefix+'.'+'zip'
                with ZipFile( Zipfile, 'w') as zip:
                    for path in all_txt_file_path:
                        zip.write(path)

                shutil.move(Zipfile, f'{destination_path}/{Zipfile}')



                os.remove(object_path)
                os.remove(object_path.split('\\')[-1])

                for item in range(len(postfix)):
                    filename = prefix + '_' + str(item+1) + '.' + postfix2
                    os.remove(filename)
            else:
                try:
                    exec(open(object_path).read())
                except:
                    print("This python file is some error")
                os.remove(object_path)
                os.remove(object_path.split('\\')[-1])
   

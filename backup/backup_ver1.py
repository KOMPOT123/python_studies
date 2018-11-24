#py\backup\backup_ver1.py
''' This is my first programm. This module backup your file and folder'''

import os
import time
import zipfile



source = 'D:\\Backup'
#список файлов и папок для резервной копии

target_dir = 'D:\\Backup'
#переменная пути для хранения

z = zipfile.ZipFile('dildo.zip', 'w')
#создание архива

for root, dirs, files in os.walk(source):

    for file in files:
    z.write(os.path.join(root,file))

z.close()



'''
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# просвоение архиву имени с текущей датой и временем

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# команда zip для помещения файлов в архив

if os.system(zip_command) == 0:
    print('Копия создана в ', target)
else:
    print('Копия не удалась')
'''

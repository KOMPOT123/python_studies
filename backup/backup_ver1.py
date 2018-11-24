#py\backup\backup_ver1.py
''' This is my first programm. This module backup your file and folder'''

import os
import zipfile

z = zipfile.ZipFile('dildo1.zip', 'w')
#создание архива и открытие для записи

z.write('D:\\Backup\\for.py')
#помещение файлов  в архив

z.close()
#закрытие архива

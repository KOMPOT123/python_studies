import pickle

shoplistfile = 'shoplist.data'
#имя файла, в котором зранится обьект
shoplist = "('список', 'из', 'миллиона', 'строк', 'или других обьектов')"

#запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)#помещаем обьект в файл
f.close()

del shoplist #уничтожает shoplist

#считывание
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

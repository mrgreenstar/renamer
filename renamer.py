#!usr/bin/python
import os
import sys
'''
    Для быстрого удаления какой-либо части из названия файла.
    Первый параметр – часть, которую нужно удалить из названия всех файлов.
    Второй параметр - путь к папке, в которой расположены файлы.
'''
def removePart(name, path = os.getcwd()):
    allFiles = os.listdir(path)
    os.chdir(path)
    print("\nТекущая директория: ", os.getcwd())
    print("Содержимое:")
    i = 1
    for oneFile in allFiles:
        # .DS_Store - файл, автоматически создаваемый Finder'ом на Mac Os
        if os.path.isfile(oneFile) and oneFile != ".DS_Store":
            print("{}. {}".format(i, oneFile))
            i += 1
            nameParts = oneFile.split(name)
            if len(nameParts) > 1:
                newName = ""
                for part in nameParts:
                    newName += part
                print("Имя после переименования: ", newName)
                os.rename(path + oneFile, path + newName)
        elif os.path.isdir(oneFile):
            removePart(name, os.getcwd() + "/" + str(oneFile) + "/")
            os.chdir("/Users/mrgreenstar/" + path)

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 1:
        removePart("(https://radiola.audio)")
    elif len(arguments) == 2:
        removePart(arguments[1])
    else:
        removePart(arguments[1], arguments[2])

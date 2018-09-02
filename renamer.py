#!usr/bin/python
import os
import sys
import mp3_tagger
'''
    Для быстрого удаления какой-либо части в названии трека.
    Добавлено удаление этой части из ID3 тегов в mp3 файлах.
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
            newName = ""
            for part in nameParts:
                newName += part
            os.rename(path + oneFile, path + newName)
            if os.path.splitext(oneFile)[1] == ".mp3":
                try:
                    mp3 = mp3_tagger.MP3File(oneFile)
                    mp3.comment = ""
                    mp3.song = newName.split(".mp3")[0]
                    print("Имя трека:", mp3.song)
                    mp3.save()
                except FileNotFoundError:
                    pass
        elif os.path.isdir(oneFile):
            removePart(name, os.getcwd() + "/" + str(oneFile) + "/")
            os.chdir(path)

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 1:
        removePart("(https://radiola.audio)")
    elif len(arguments) == 2:
        removePart(arguments[1])
    else:
        removePart(arguments[1], arguments[2])

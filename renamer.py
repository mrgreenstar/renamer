#!usr/bin/python
import os
import sys
import mp3_tagger

'''
    Script for fast deleting part of the song name.
    Script deletes part from ID3 tags.
    First param - str, which must be deleted from the files name.
    Second param - path to the folred.
'''

def removePart(name, path = os.getcwd()):
    allFiles = os.listdir(path)
    os.chdir(path)
    print("\nCurrent directory: ", os.getcwd())
    print("Content:")
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
                    print("Song name:", mp3.song)
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

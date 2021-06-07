import os

def mkfolder(mfname):
    path = f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{mfname}'
    os.mkdir(path)

def name():
    mkname = input()
    a = mkname
    return a
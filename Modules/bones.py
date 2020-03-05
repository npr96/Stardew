from Modules import Dict
from Modules import cutscenes
import winsound


def start():
    print(Dict.welcome[1])
    name = input('What is your name?: ')
    print(Dict.welcome[2])
    _ = input('press [enter] to continue')
    return name


def parser(imp):
    parsimp = imp.split()
    return parsimp


def interpreter(parsimp):
    pass

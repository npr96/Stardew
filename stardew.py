from Modules import Settings
from Modules import bones
from Modules import Dict
from Modules import cutscenes

class Player:
    start = 0

    def __init__(self, invent=Settings.inventory, health=Settings.health, wallet=Settings.wallet, name='',
                 farm_name=''):
        self.inv = invent
        self.heal = health
        self.wall = wallet
        self.name = name
        self.farm_name = farm_name

    def engine(self):
        if Player.start == 0:
            self.name = bones.start()
            Player.start = 1
        else:
            pass
        if Dict.dict_of_flags['Open cutscene'] == 0:
            self.farm_name = cutscenes.open_cutscene(self.name)
            Dict.dict_of_flags['Open cutscene'] = 1
        else:
            pass
        imp = input('-' + self.farm_name + '-')
        bones.interpreter(bones.parser(imp))


player1 = Player()

if __name__ == "__main__":
    player1.engine()

class People:
    def __init__(self, role):
        self.role = role
        self.aggressivity = role['aggressivity']
        self.life = role['life']

    def get_info(self):
        print('您选择的游戏人物是\n{}' .format(self.role))

    def set_aggressivity(self, aggressivity):
        self.aggressivity += aggressivity

    def set_life(self, life):
        self.life += life

    def get_aggressivity(self):
        return self.aggressivity

    def get_life(self):
        return self.life




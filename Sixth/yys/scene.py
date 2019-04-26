class Scene:
    def __init__(self, people):
        self.people = people
        pass

    def yin_jie_lie_feng(self):
        if self.people.aggressivity < 220 or self.people.life < 2000:
            return False
        else:
            self.people.set_aggressivity(-220)
            self.people.set_life(-2000)
            return True

    def gui_wang_feng_yin(self):
        if self.people.aggressivity < 3100 or self.people.life < 3000:
            return False
        else:
            self.people.set_aggressivity(-3100)
            self.people.set_life(-3000)
            return True



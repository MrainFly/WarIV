dragon_ph = 0
dragon_atk = 0

renzhe_ph = 0
renzhe_atk = 0

iceman_ph = 0
iceman_atk = 0

lion_ph = 0
lion_atk = 0

wolf_ph = 0
wolf_atk = 0


def warrior_init_ph(*ph):
    global dragon_ph, renzhe_ph, iceman_ph, lion_ph, wolf_ph
    dragon_ph = ph[0]
    renzhe_ph = ph[1]
    iceman_ph = ph[2]
    lion_ph = ph[3]
    wolf_ph = ph[4]


def warrior_init_atk(*atk):
    global dragon_atk, renzhe_atk, iceman_atk, lion_atk, wolf_atk
    dragon_atk = atk[0]
    renzhe_atk = atk[1]
    iceman_atk = atk[2]
    lion_atk = atk[3]
    wolf_atk = atk[4]


class Warrior(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, wid, camp, ph):
        self.atk = None
        self.ph = None
        self.wid = wid
        self.camp = camp

    def strick(self):
        return self.atk

    def strick_back(self):
        return self.atk/2

    def move(self):
        pass

    def bear(self, atk):
        self.ph -= atk
        # 阵亡
        if self.ph <= 0:
            return -1
        else:
            return 0


class Dragon(Warrior):
    def __new__(cls, *args, **kwargs):
        global dragon_ph
        if args[2] < dragon_ph:
            return None
        else:
            return Warrior.__new__(cls)

    def __init__(self, wid, camp, ph):
        global dragon_ph, dragon_atk
        Warrior.__init__(self, wid, camp, ph)
        self.__initiative = False
        self.ph = dragon_ph
        self.atk = dragon_atk

    def strick(self):
        self.__initiative = True
        return super().strick()

    def strick_back(self):
        self.__initiative = False
        return super().strick_back()

    def bear(self, atk):
        ret = Warrior.bear(atk)
        # 阵亡
        if ret == -1:
            pass
        else:
            # cheer
            self.cheer()
        return ret

    def cheer(self):
        # TODO
        print()


class Renzhe(Warrior):
    def __new__(cls, *args, **kwargs):
        global renzhe_ph
        if args[2] < renzhe_ph:
            return None
        else:
            return Warrior.__new__(cls)

    def __init__(self, wid, camp, ph):
        global renzhe_ph, renzhe_atk
        Warrior.__init__(wid, camp, ph)
        self.ph = renzhe_ph
        self.atk = renzhe_atk

    def strick_back(self):
        return 0


class Iceman(Warrior):
    def __new__(cls, *args, **kwargs):
        global iceman_ph
        if args[2] < iceman_ph:
            return None
        else:
            return Warrior.__new__(cls)

    def __init__(self, wid, camp, ph):
        global iceman_ph, iceman_atk
        Warrior.__init__(wid, camp, ph)
        self.__step = 0
        self.ph = iceman_ph
        self.atk = iceman_atk

    def move(self):
        self.__step += 1
        # 当移动两部后会生命少10，攻击力增加20
        if self.__step % 2 == 0:
            # 如果生命小于10，则扣除到1
            if self.ph <= 10:
                self.ph = 1
            else:
                self.ph -= 10
            self.atk += 20


class Lion(Warrior):
    def __new__(cls, *args, **kwargs):
        global lion_ph
        if args[2] < lion_ph:
            return None
        else:
            return Warrior.__new__(cls)

    def __init__(self, wid, camp, ph):
        global lion_ph, lion_atk
        Warrior.__init__(wid, camp, ph)
        self.ph = lion_ph
        self.atk = lion_atk
        self.preph = self.ph

    def bear(self, atk):
        self.preph = self.ph
        return super(Lion, self).bear(atk)

    def siphon_soul(self):
        return self.preph


class Wolf(Warrior):
    def __new__(cls, *args, **kwargs):
        global wolf_ph
        if args[2] < wolf_ph:
            return None
        else:
            return Warrior.__new__(cls)

    def __init__(self, wid, camp, ph):
        global wolf_ph, wolf_atk
        Warrior.__init__(wid, camp, ph)
        self.ph = wolf_ph
        self.atk = wolf_atk
        self.kill = 0

    def bloodthirsty(self):
        if self.kill % 2 == 0 and self.kill != 0:
            self.atk *= 2
            self.ph *= 2


if __name__ == "__main__":
    warrior_init_ph(90, 20, 30, 10, 20)
    warrior_init_atk(20, 50, 20, 40, 30)

    # Dragon test ######################
    # Dragon born
    dragon = Dragon(1, "blue", 1000)
    # Dragon born failed
    # dragon = Dragon(2, "red", 10)
    # Dragon attack
    print("Dragon attack ", dragon.strick())
    # Dragon strick back
    print("Dragon strick back ", dragon.strick_back())
    while True:
        pass

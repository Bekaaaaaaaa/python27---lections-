"============================== Ассоцияция ============================="
# АССОЦИАЦИЯ - принцип ООП, в котором два клвасса идут друг с другом связаны

# ассоциация делится на два принципа :
# 1. АГРЕГАЦИЯ (более слабая связь)
# 2. композиция (более сильная свзяь)
class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def init(self, color):
        self.color = color
        self.battery = Battery()
        # когда мы создаем объект от другого класса прям внутри другого - композиция

# iphone = Iphone('золотой')
# print(iphone.battery.power)

# del iphone

# print(iphone)


class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery

battery = Battery()
nokia = Nokia('lback', battery)

del nokia
print(nokia.battery)
print(battery.power)
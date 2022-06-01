class Unit:
    # Constructor __init__
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")


marine = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


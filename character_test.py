from character import Enemy

captainHook = Enemy("Captain Hook", "Mainpulative and cruel")
captainHook.describe()

captainHook.set_conversation("Come closer. I can't see you!")
captainHook.talk()

captainHook.set_weakness("sword")
print("What will you fight with? ")
fight_with = input()
captainHook.fight(fight_with)


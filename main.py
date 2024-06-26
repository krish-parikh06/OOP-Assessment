from character import Enemy, Friend
from island import Island

mainIsland = Island("Main Island")
mainIsland.set_description("Welcome to the beginning of the journey.")

coconutIsland = Island("Coconut Island")
coconutIsland.set_description("Welcome to Coconut Island.")

locusMaris = Island("Locus Maris")
locusMaris.set_description("Welcome to Locus Maris.")

daggerReef = Island("Dagger Reef")
daggerReef.set_description("Welcome to Dagger Reef.")

atlantisArchipelago = Island("Atlantis Archipelago")
atlantisArchipelago.set_description("Welcome to Atlantis Archipelago.")

bananaSanctuary = Island("Banana Sanctuary")
bananaSanctuary.set_description("Welcome to Banana Sanctuary.")

jurassicPark = Island("Jurassic Park")
jurassicPark.set_description("Welcome to Jurassic Park.")

kingfishersRock = Island("Kingfisher's Rock")
kingfishersRock.set_description("Welcome to Kingfisher's Rock.")

anaposRock= Island("Anapos Rock")
anaposRock.set_description("Welcome to Anapos Rock.")

avalonsAcre = Island("Avalon's Acre")
avalonsAcre.set_description("Welcome to Avalon's Acre.")

goldenTooth = Island("Golden Tooth")
goldenTooth.set_description("Welcome to Golden Tooth.")

mainIsland.link_island(locusMaris, "south")

locusMaris.link_island(daggerReef, "east")
locusMaris.link_island(coconutIsland, "west")

daggerReef.link_island(locusMaris, "west")

coconutIsland.link_island(locusMaris, "east")
coconutIsland.link_island(jurassicPark, "south")

jurassicPark.link_island(coconutIsland, "north")
jurassicPark.link_island(bananaSanctuary, "east")
jurassicPark.link_island(kingfishersRock, "west")

kingfishersRock.link_island(jurassicPark, "east")

bananaSanctuary.link_island(jurassicPark, "west")
bananaSanctuary.link_island(atlantisArchipelago, "east")
bananaSanctuary.link_island(avalonsAcre, "south")

atlantisArchipelago.link_island(bananaSanctuary, "west")

avalonsAcre.link_island(bananaSanctuary, "north")
avalonsAcre.link_island(goldenTooth, "west")
avalonsAcre.link_island(anaposRock, "east")

goldenTooth.link_island(avalonsAcre, "east")

anaposRock.link_island(avalonsAcre, "west")

captainHook = Enemy("Captain Hook", "Mainpulative and cruel")
captainHook.set_conversation("Where are you? Come closer!")
captainHook.set_weakness("sword")

maui = Friend("Maui", "A friendly Fijian")
maui.set_conversation("Bula")
coconutIsland.set_character(maui)

current_island = daggerReef
daggerReef.set_character(captainHook)

dead = False
while dead == False:
    print("\n")
    current_island.get_details()
    inhabitant = current_island.get_character()

    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_island = current_island.move(command)

    if command in current_island.linked_islands:
        current_island = current_island.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):

            print("What will you fight with? ")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Bravo, hero you won the fight.")
                current_island.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
                print("That's the end of the game")
                dead = True

        else:
            print("There is no one here to fight with.")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :( ")


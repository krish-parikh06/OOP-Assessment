from character import Enemy
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
captainHook.set_conversation("Hangry…Hanggrry")
captainHook.set_weakness("vegemite")

current_island = mainIsland
while True:
    print("\n")
    current_island.get_details()
    inhabitant = current_island.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_island = current_island.move(command)


daggerReef.set_character()


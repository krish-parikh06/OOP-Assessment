class Island:
    def __init__(self, island_name):
        self.name = island_name
        self.linked_islands = {}
        self.character = None

    def get_description(self):
        return self.description

    def set_description(self, island_description):
        self.description = island_description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, island_name):
        self.name = island_name

    def link_island(self, island_to_link, direction):
        self.linked_islands[direction] = island_to_link

    def get_details(self):
        for direction in self.linked_islands:
            island = self.linked_islands[direction]
            print("The", island.get_name(), "is", direction)

    def move(self, direction):
        if direction in self.linked_islands:
            return self.linked_islands[direction]
        else:
            print("You can't go that way!")
            return self

    def set_character(self, character_name):
        self.character = character_name

    def get_character(self):
        return self.character






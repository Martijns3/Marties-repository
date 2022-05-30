# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"

# Add your code after this line


def main():

    print(p1.introduce())
    print(p1.strength())
    print(ray.name)
    print(commentator.sum_player(p2))
    print(ray.compare_players(alice, bob, "speed"))


# from turtle import speed


class Player:
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        if (
            (0 < self.speed <= 1)
            and (0 < self.endurance <= 1)
            and (0 < self.accuracy <= 1)
        ):
            pass
        else:
            raise ValueError

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        strength_data = {
            "speed": self.speed,
            "endurance": self.endurance,
            "accuracy": self.accuracy,
        }
        max_values = dict()
        strength_max = max(strength_data.values())

        for key, value in strength_data.items():
            if value == strength_max:

                max_values[key] = strength_max
            for i in max_values:
                output = (i, max_values[i])

                return output


p1 = Player("Kees", 0.8, 1.0, 0.8)


# _________________________________________________________________________________________________


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, PlayerData):

        speed = getattr(PlayerData, "speed")
        endurance = getattr(PlayerData, "endurance")
        accuracy = getattr(PlayerData, "accuracy")
        sum_strength = speed + endurance + accuracy
        return sum_strength

    def compare_players(self, PlayerData1, PlayerData2, DataCompare):
        name1 = getattr(PlayerData1, "name")
        name2 = getattr(PlayerData2, "name")

        DataCompare1 = getattr(PlayerData1, DataCompare)
        DataCompare2 = getattr(PlayerData2, DataCompare)

        strength1 = Player.strength(PlayerData1)
        strength2 = Player.strength(PlayerData2)

        if DataCompare1 > DataCompare2:
            return name1
        elif DataCompare2 > DataCompare1:
            return name2
        else:
            if strength1 > strength2:
                return name1
            elif strength2 > strength1:
                return name2
            else:
                if commentator.sum_player(PlayerData1) > commentator.sum_player(
                    PlayerData2
                ):
                    return name1
                elif commentator.sum_player(PlayerData2) > commentator.sum_player(
                    PlayerData1
                ):
                    return name2
                elif commentator.sum_player(PlayerData1) == commentator.sum_player(
                    PlayerData2
                ):
                    return "These two players might as well be twins!"


commentator = Commentator("name")

ray = Commentator("Ray Hudson")
p2 = Player("Joost", 1.0, 0.8, 0.7)

alice = Player("Alice", 0.9, 0.3, 0.8)
bob = Player("Bob", 0.9, 0.3, 0.8)


if __name__ == "__main__":
    main()

__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


def main():
    # ----> find the cheapest specialist:
    print(Candice.find_specialist())


class Homeowner:
    def __init__(self, name, address, needs):

        self.name = name
        self.address = address
        self.needs = needs

    def find_specialist(self):

        final_list = [f'Hi {self.name.split(" ")[0]}!']

        class_list = []
        for x in self.needs:
            if x == "painter":
                class_list.append(Painter)
            if x == "plumber":
                class_list.append(Plumber)
            if x == "electrician":
                class_list.append(Electrician)

        for q in class_list:
            sorted_specialist = []

            for item in Specialist_list:
                if isinstance(item, q):
                    sorted_specialist.append((item.name, item.tarif))

            sorted_lst_specialist = sorted(
                sorted_specialist, key=lambda x: (x[1], x[0])
            )

            cheapest_specialist = []
            try:
                cheapest_specialist = sorted_lst_specialist[0]
            except IndexError:
                pass
            zz = str(q).lower()
            zz = zz[:-2]
            if len(cheapest_specialist):
                cs = cheapest_specialist[1]
                recommend = f'- The cheapest {zz.split(".")[1]} we\'ve found, is {cheapest_specialist[0]} for € {format(cs, ".2f")} per hour.'
                final_list.append(recommend)
            else:
                none_available = f'- Unfortunately at this moment we have no {zz.split(".")[1]} available'
                final_list.append(none_available)
                
        if len(cheapest_specialist):
            final_list.append(f"The specialist(s) will visit you at your address: {self.address}.")
        else:
            pass
        data = "\n".join((item[0:] for item in final_list))
        return data


class Plumber:
    def __init__(self, name, tarif):
        self.name = name
        self.tarif = tarif


class Electrician:
    def __init__(self, name, tarif):
        self.name = name
        self.tarif = tarif


class Painter:
    def __init__(self, name, tarif):
        self.name = name
        self.tarif = tarif


Specialist_list = [
    (Plumber("Craig Craigsville", 20)),
    (Electrician("Alice Aliceville", 18)),
    (Plumber("Bruce Willis", 16)),
    (Electrician("Eve Adams", 17.65)),
    (Plumber("Maddy Madison", 15)),
    (Painter("Babe Babylon", 20)),
    (Painter("Bob Bobsville", 17.50)),
]
# ---> add a specialist with this line:
Specialist_list.append(Plumber("Ira Plumbersson", 8))

# ---> add a homeowner with this line:
Alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber", "electrician"])
Bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
Candice = Homeowner("Candice Candicedottir", "Candicelane 312", ["electrician", "painter", "plumber"])


if __name__ == "__main__":
    main()


# --------------------------------------old code----------------------------------------
# alice_name = "Alice Aliceville"
# alice_profession = "electrician"
# bob_name = "Bob Bobsville"
# bob_profession = "painter"
# craig_name = "Craig Craigsville"
# craig_profession = "plumber"

# alfred_name = "Alfred Alfredson"
# alfred_address = "Alfredslane 123"
# alfred_needs = ["painter", "plumber"]
# bert_name = "Bert Bertson"
# bert_address = "Bertslane 231"
# bert_needs = ["plumber"]
# candice_name = "Candice Candicedottir"
# candice_address = "Candicelane 312"
# candice_needs = ["electrician", "painter"]

# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

# print("Alfred's contracts:", alfred_contracts)
# print("Bert's contracts:", bert_contracts)
# print("Candice's contracts:", candice_contracts)

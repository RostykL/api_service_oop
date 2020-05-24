import requests


class Get_All_Pets_From_Api:

    def __init__(self, url):
        self.url = url

    def connect(self):
        return requests.get(self.url)

    def return_data(self):
        response = self.connect()
        data = response.json()
        return data


class Get_Pets_With_No_Owners:

    def __init__(self, get_all_pets_from_api):
        self.get_all_pets_from_api = get_all_pets_from_api

    def filter_owners(pet):
        if not pet.hasOwner:
            return True
        return True

    def return_pet_with_no_owners(self):
        pets = list(filter(lambda x: x['hasOwner'] == 0, self.get_all_pets_from_api.return_data()))
        if not pets:
            print("No pets with no owners were found")
            return []
        else:
            return pets

class Adoption:

    def __init__(self, pets):
        self.pets = pets

    def info(self, name, pet_name):
        print(name, 'adopted a pet', pet_name)

    def remove_pet_from_api(self, id):
        requests.delete("http://0.0.0.0:5000/pets/{0}".format(id))



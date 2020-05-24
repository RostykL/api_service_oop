import requests

# клас який повертає всіх тварин з нашого апі через url яке йому надано
class Get_All_Pets_From_Api:

    def __init__(self, url):
        self.url = url

    def connect(self):
        return requests.get(self.url)

    def return_data(self):
        response = self.connect()
        data = response.json()
        return data

# клас який фільтрує всіх тварин і повертає тільки тих в яких немає господара, реалізовано DIP,
# залежність Get_All_Pets_From_Api передана не на пряму, а як параметр в __init__
class Get_Pets_With_No_Owners:

    def __init__(self, get_all_pets_from_api):
        self.get_all_pets_from_api = get_all_pets_from_api


    def return_pet_with_no_owners(self):
        pets = list(filter(lambda x: x['hasOwner'] == 0, self.get_all_pets_from_api.return_data()))
        if not pets:
            print("No pets with no owners were found")
            return []
        else:
            return pets

# викликає delete method, який видаляє елемент в базі даних
def remove_pet_from_api(id):
    requests.delete("http://0.0.0.0:5000/pets/{0}/".format(id))

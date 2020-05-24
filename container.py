import dependency_injector.containers as containers
import dependency_injector.providers as providers


from ioc.FoundOwner import Get_All_Pets_From_Api, Get_Pets_With_No_Owners, remove_pet_from_api

# Ioc Контейнер
class Container(containers.DeclarativeContainer):
    # тут зберігаються всі наші тварити
    all_pets = providers.Singleton(Get_All_Pets_From_Api,
                                   url='http://localhost:5000/pets')
    # всі тварини, які не мають господара
    pets_with_no_owners = providers.Singleton(Get_Pets_With_No_Owners,
                                              get_all_pets_from_api=all_pets)
    # викликаємо це, якщо ми хочемо взяти соб тварину, воно викликає функцію, яка видаляє елемент з бази даних
    adoption = providers.Callable(remove_pet_from_api)


# if __name__ == '__main__':
#     container = Container()
#     all_pets = container.all_pets()  # all available pets in api
#     no_owners = container.pets_with_no_owners()  # pets from api with no owners, available for adoption
#     try:
#         no_owners.return_pet_with_no_owners()[0]
#         print(no_owners.return_pet_with_no_owners()[0], '- pets with no owners')
#         container.adoption(no_owners.return_pet_with_no_owners()[0]['name'],no_owners.return_pet_with_no_owners()[0]['id'])
#     except IndexError:
#         print("No pets are found")

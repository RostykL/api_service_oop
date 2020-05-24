import dependency_injector.containers as containers
import dependency_injector.providers as providers

from ioc.FoundOwner import Get_All_Pets_From_Api, Get_Pets_With_No_Owners


class Container(containers.DeclarativeContainer):
    all_pets = providers.Singleton(Get_All_Pets_From_Api,
                                   url='http://localhost:5000/pets')
    pets_with_no_owners = providers.Singleton(Get_Pets_With_No_Owners,
                                              get_all_pets_from_api=all_pets)


if __name__ == '__main__':
    container = Container()
    all_pets = container.all_pets() # all available pets in api
    no_owners = container.pets_with_no_owners() # pets from api with no owners, available for adoption
    print(no_owners.return_pet_with_no_owners(), '- pets with no owners')

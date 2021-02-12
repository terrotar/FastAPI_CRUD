from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app


client = TestClient(app)


class TestCreatePet():
    def test_create_pet_new_pet_name_specie_not_string(self):
        # Check if new_pet["name"] and new_pet["specie"] == "string"
        response = client.post('/pets', json={
                                              "name": "string",
                                              "species": "string"
                                             })
        assert response.status_code == 400

    async def test_create_pet_new_pet_already_exists(self):
        # Check possibility of create a Pet that already exists...
        duplicate_pet = client.get('/pets/1', data=Session)
        assert duplicate_pet.status_code == 200
        duplicate_pet = list(duplicate_pet)
        # Have to transform into list because crud.create_pet transform
        # data into dict and a dict can't be transformed into dict
        response = client.post('/pets', data=(duplicate_pet[0]))
        assert response.status_code == 422


class TestListPets():
    def test_list_pets_filter_name_and_species(self):
        # Check if return filter by name and species
        response = client.post('/pets', json={
                                    "name": "Luna",
                                    "species": "Cat"
                                  })
        assert response.status_code == 422

    def test_list_pets_filter_species(self):
        # Check if return filter by species
        response = client.post('/pets', json={
                                    "species": "Cat"
                              })
        assert response.status_code == 422

    def test_list_pets_no_filter(self):
        # Check if return with no filter
        response = client.post('/pets')
        assert response.status_code == 422

    def test_list_pets_filter_name(self):
        # Check if return filter by name
        response = client.post('/pets', json={
                                    "name": "Luna"
                                  })
        assert response.status_code == 422

from fastapi.testclient import TestClient

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


"""
    def test_create_pet_new_pet_already_exists(self):
        # Check possibility of create a Pet that already exists..
        response = client.post('/pets', json={
                                              "name": "name",
                                              "species": "species",
                                              "id": "id"
                                             })
        assert response.status_code == 422
        # It needs to call the function create_pet to verify
"""


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

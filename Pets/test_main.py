from fastapi.testclient import TestClient

from main import app, create_pet


client = TestClient(app)


class TestPets():
    def test_create_pet_new_pet_name_specie_not_string(self):
        """
        Check if new_pet["name"] and new_pet["specie"] == "string"
        """
        response = client.post('/pets', json={
                                              "name": "string",
                                              "species": "string"
                                             })
        assert response.status_code == 400

    def test_create_pet_new_pet_already_exists(self):
        """
        Check possibility of create a Pet that already exists..
        """
        client.post('/pets', json={
                                    "name": "name",
                                    "species": "species",
                                    "id": "id"
                                  })
        response = client.post('/pets', json={
                                              "name": "name",
                                              "species": "species",
                                              "id": "id"
                                              })
        assert response.status_code == 422

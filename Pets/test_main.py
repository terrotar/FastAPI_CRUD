from fastapi.testclient import TestClient

from main import app, create_pet, PETS_LIST


client = TestClient(app)


class TestPets():
    def test_create_pet_new_pet_name_specie_not_string(self):
        """
        Check if new_pet["name"] and new_pet["specie"] "= "string"
        """
        new_pet = {"name": "string", "species": "string"}
        create_pet(new_pet)
        assert create_pet(new_pet)

    def test_create_pet_new_pet_already_exists(self):
        """
        Check possibility of create a Pet that already exists..
        If so, raise an HTTPException(status_code=422)
        """
        response = client.post('/pets')
        new_pet = PETS_LIST[-1]
        PETS_LIST.append(new_pet)
        assert response.status_code == 422

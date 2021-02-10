from fastapi.testclient import TestClient

from main import app, PETS_LIST, ID_COUNTER


client = TestClient(app)


class TestPets():
    def test_create_pet_new_pet_already_exists(self):
        """
        Check possibility of create a Pet that already exists..
        If so, raise an HTTPException(status_code=422)
        """
        response = client.post('/pets')
        new_pet = PETS_LIST[-1]
        PETS_LIST.append(new_pet)
        assert response.status_code == 422

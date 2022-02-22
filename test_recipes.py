from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_recipes_id():
    """
    This method tests the response by recipe id requests.
    """
    response = client.get("/2")
    assert response.status_code == 200
    assert response.json() == {
        "status":200,
        "recipe":{"id":2,"name":"Applesauce Bread I Recipe","total_duration":80,"ingredients":["raisin","baking soda","white sugar","applesauce","sour cream","flour","egg","baking powder","vegetable oil","cinnamon"],"directions":"Preheat oven to 350 degrees F (175 degrees C).  Grease and flour two 9 x 5 inch loaf pans.Beat together eggs, sugar, and oil.  Blend in applesauce, and then sour cream or buttermilk.  Mix in flour, baking powder, soda, and cinnamon. Stir in raisins. Pour batter into prepared pans.Bake for 80 minutes.  Cool on wire racks."}
    }

def test_recipes_id_not_found():
    """
    This method tests the response from invalid requests.
    """
    response = client.get("/16000")
    assert response.status_code == 200
    assert response.json() == {
        "status":404,
        "message":"recipe not found"
    }
    
def test_unprocessable_entity():
    """
    This method tests respose from Unprocessable Entity requests.
    """
    response = client.get("/wrong_request")
    assert response.status_code == 422

    
     

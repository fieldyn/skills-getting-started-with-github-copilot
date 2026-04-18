from src import app as app_module


def test_signup_then_unregister_restores_participant_state(client):
    # Arrange
    activity_name = "Science Club"
    email = "flow-student@mergington.edu"
    endpoint_path = f"/activities/{activity_name}/signup"

    # Act
    signup_response = client.post(endpoint_path, params={"email": email})
    unregister_response = client.delete(endpoint_path, params={"email": email})

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert email not in app_module.activities[activity_name]["participants"]

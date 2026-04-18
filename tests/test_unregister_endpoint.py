from src import app as app_module


def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = app_module.activities[activity_name]["participants"][0]
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in app_module.activities[activity_name]["participants"]


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "student@mergington.edu"
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_rejects_non_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not-registered@mergington.edu"
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}

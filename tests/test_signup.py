def test_signup_adds_new_participant(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "new-student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": student_email})
    activities_response = client.get("/activities")
    activities_data = activities_response.json()

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {student_email} for {activity_name}"
    assert student_email in activities_data[activity_name]["participants"]


def test_signup_rejects_duplicate_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_student_email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": existing_student_email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_returns_not_found_for_unknown_activity(client):
    # Arrange
    unknown_activity_name = "Unknown Activity"
    student_email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{unknown_activity_name}/signup",
        params={"email": student_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

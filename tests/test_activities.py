def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_status_code = 200

    # Act
    response = client.get("/activities")
    response_data = response.json()

    # Assert
    assert response.status_code == expected_status_code
    assert isinstance(response_data, dict)
    assert len(response_data) > 0


def test_get_activities_includes_expected_activity_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    response_data = response.json()

    # Assert
    for activity_details in response_data.values():
        assert required_fields.issubset(activity_details.keys())


def test_root_redirects_to_static_index(client):
    # Arrange
    expected_redirect_status_code = 307
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == expected_redirect_status_code
    assert response.headers["location"] == expected_location

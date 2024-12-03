import pytest
from tracker_backend.models import TrackerDevice, LocationRecord, User

class TestTrackerDevice:
    def test_tracker_device_attributes(self):
        tracker_device = TrackerDevice(
            tracker_id="12345",
            activation_status=True,
            owner_info="John Doe",
            factory_registration_date="2023-01-01",
            last_reported_location="Location A",
            battery_level=85,
            firmware_version="1.0.0"
        )
        assert tracker_device.tracker_id == "12345"
        assert tracker_device.activation_status == True
        assert tracker_device.owner_info == "John Doe"
        assert tracker_device.factory_registration_date == "2023-01-01"
        assert tracker_device.last_reported_location == "Location A"
        assert tracker_device.battery_level == 85
        assert tracker_device.firmware_version == "1.0.0"

class TestLocationRecord:
    def test_location_record_attributes(self):
        location_record = LocationRecord(
            tracker_id="12345",
            timestamp="2023-01-01T12:00:00Z",
            latitude=37.7749,
            longitude=-122.4194,
            battery_level=85,
            signal_strength=75,
            ttl=259200
        )
        assert location_record.tracker_id == "12345"
        assert location_record.timestamp == "2023-01-01T12:00:00Z"
        assert location_record.latitude == 37.7749
        assert location_record.longitude == -122.4194
        assert location_record.battery_level == 85
        assert location_record.signal_strength == 75
        assert location_record.ttl == 259200

class TestUser:
    def test_user_attributes(self):
        user = User(
            user_id="user123",
            email="user@example.com",
            hashed_password="hashed_password",
            created_date="2023-01-01",
            last_login="2023-01-02",
            owned_tracker_ids=["12345", "67890"]
        )
        assert user.user_id == "user123"
        assert user.email == "user@example.com"
        assert user.hashed_password == "hashed_password"
        assert user.created_date == "2023-01-01"
        assert user.last_login == "2023-01-02"
        assert user.owned_tracker_ids == ["12345", "67890"]

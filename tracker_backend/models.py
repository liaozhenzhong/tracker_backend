from pydantic import BaseModel
from typing import List

class TrackerDevice(BaseModel):
    tracker_id: str
    activation_status: bool
    owner_info: str
    factory_registration_date: str
    last_reported_location: str
    battery_level: int
    firmware_version: str

class LocationRecord(BaseModel):
    tracker_id: str
    timestamp: str
    latitude: float
    longitude: float
    battery_level: int
    signal_strength: int
    ttl: int

class User(BaseModel):
    user_id: str
    email: str
    hashed_password: str
    created_date: str
    last_login: str
    owned_tracker_ids: List[str]

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List, Optional, Set


class SpotType(str, Enum):
    COMPACT = "Compact"
    LARGE = "Large"
    HANDICAPPED = "Handicapped"


class VehicleType(str, Enum):
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"


@dataclass(frozen=True)
class Vehicle:
    license_plate: str
    vehicle_type: VehicleType


class Car(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate=license_plate, vehicle_type=VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate=license_plate, vehicle_type=VehicleType.TRUCK)


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate=license_plate, vehicle_type=VehicleType.MOTORCYCLE)


DEFAULT_ALLOWED_VEHICLES: Dict[SpotType, Set[VehicleType]] = {
    SpotType.COMPACT: {VehicleType.CAR, VehicleType.MOTORCYCLE},
    SpotType.LARGE: {VehicleType.CAR, VehicleType.TRUCK, VehicleType.MOTORCYCLE},
    SpotType.HANDICAPPED: {VehicleType.CAR, VehicleType.MOTORCYCLE},
}


class ParkingSpot:
    def __init__(
        self,
        spot_id: str,
        spot_type: SpotType,
        allowed_vehicle_types: Optional[Iterable[VehicleType]] = None,
    ) -> None:
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.allowed_vehicle_types = set(
            allowed_vehicle_types or DEFAULT_ALLOWED_VEHICLES[spot_type]
        )
        self.parked_vehicle: Optional[Vehicle] = None

    @property
    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def can_park(self, vehicle: Vehicle) -> bool:
        return self.is_available and vehicle.vehicle_type in self.allowed_vehicle_types

    def park(self, vehicle: Vehicle) -> bool:
        if not self.can_park(vehicle):
            return False
        self.parked_vehicle = vehicle
        return True

    def unpark(self) -> Optional[Vehicle]:
        vehicle = self.parked_vehicle
        self.parked_vehicle = None
        return vehicle


class ParkingLot:
    def __init__(self, spots: List[ParkingSpot]) -> None:
        self.spots = spots
        self._spot_by_vehicle_license: Dict[str, ParkingSpot] = {}

    def park_vehicle(self, vehicle: Vehicle) -> Optional[str]:
        if vehicle.license_plate in self._spot_by_vehicle_license:
            return None

        for spot in self.spots:
            if spot.park(vehicle):
                self._spot_by_vehicle_license[vehicle.license_plate] = spot
                return spot.spot_id
        return None

    def unpark_vehicle(self, license_plate: str) -> bool:
        spot = self._spot_by_vehicle_license.pop(license_plate, None)
        if spot is None:
            return False
        spot.unpark()
        return True

    def check_availability(self, spot_type: Optional[SpotType] = None):
        if spot_type is not None:
            return sum(
                1 for spot in self.spots if spot.spot_type == spot_type and spot.is_available
            )

        availability = {spot_kind: 0 for spot_kind in SpotType}
        for spot in self.spots:
            if spot.is_available:
                availability[spot.spot_type] += 1
        return availability

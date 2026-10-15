import unittest

from parking_lot import (
    Car,
    Motorcycle,
    ParkingLot,
    ParkingSpot,
    SpotType,
    Truck,
)


class ParkingLotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parking_lot = ParkingLot(
            [
                ParkingSpot("C1", SpotType.COMPACT),
                ParkingSpot("C2", SpotType.COMPACT),
                ParkingSpot("L1", SpotType.LARGE),
                ParkingSpot("H1", SpotType.HANDICAPPED),
            ]
        )

    def test_park_and_check_availability(self) -> None:
        self.assertEqual(self.parking_lot.park_vehicle(Car("CAR-1")), "C1")
        self.assertEqual(self.parking_lot.park_vehicle(Truck("TRUCK-1")), "L1")
        self.assertEqual(self.parking_lot.check_availability(SpotType.COMPACT), 1)
        self.assertEqual(self.parking_lot.check_availability(SpotType.LARGE), 0)

    def test_cannot_park_when_no_matching_spot_available(self) -> None:
        self.assertEqual(self.parking_lot.park_vehicle(Truck("TRUCK-1")), "L1")
        self.assertIsNone(self.parking_lot.park_vehicle(Truck("TRUCK-2")))

    def test_unpark_releases_spot(self) -> None:
        self.assertEqual(self.parking_lot.park_vehicle(Motorcycle("MOTO-1")), "C1")
        self.assertTrue(self.parking_lot.unpark_vehicle("MOTO-1"))
        self.assertEqual(self.parking_lot.check_availability(SpotType.COMPACT), 2)
        self.assertFalse(self.parking_lot.unpark_vehicle("MOTO-1"))

    def test_check_availability_for_all_spot_types(self) -> None:
        self.parking_lot.park_vehicle(Car("CAR-1"))
        availability = self.parking_lot.check_availability()
        self.assertEqual(availability[SpotType.COMPACT], 1)
        self.assertEqual(availability[SpotType.LARGE], 1)
        self.assertEqual(availability[SpotType.HANDICAPPED], 1)


if __name__ == "__main__":
    unittest.main()

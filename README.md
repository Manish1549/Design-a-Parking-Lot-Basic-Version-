# Parking Lot - Low Level Design (LLD)

A clean, Object-Oriented C++ implementation of a Basic Parking Lot system. This project demonstrates core Low-Level Design (LLD) principles, encapsulation, and class relationships.

## System Architecture & Core Entities

Based on the system requirements, the architecture is divided into three main entities:

*   **Vehicle**
    *   Represents the vehicle to be parked.
    *   **Attributes:** `licensePlate` (string), `VehicleType` (enum)
*   **ParkingSpot**
    *   Represents a single parking space in the lot.
    *   **Attributes:** `id` (int), `SpotType` (enum), `occupied` (bool), `currentVehicle` (Vehicle*)
    *   **Behaviors:** Knows how to check if a specific vehicle fits (`canFit()`), park a vehicle, and free up the spot.
*   **ParkingLot**
    *   The main manager class handling the collection of spots.
    *   **Attributes:** `vector<ParkingSpot*> spots`
    *   **Behaviors:** Handles searching for available spots, parking, unparking via license plate, and tracking overall capacity.

## Enums Used
To ensure type safety and avoid magic numbers, the system uses explicit enums:
*   **VehicleType:** `MOTORCYCLE`, `CAR`, `TRUCK`
*   **SpotType:** `COMPACT`, `LARGE`, `HANDICAPPED`

## Key Features
*   **Dynamic Initialization:** The lot automatically distributes parking spots during initialization (e.g., 20% Handicapped, 50% Compact, 30% Large).
*   **Smart Fitting Logic:** Uses a fail-closed `switch` statement to ensure vehicles only park in valid spots (e.g., Trucks can only fit in Large spots, Motorcycles fit anywhere).
*   **O(N) Park & Unpark Operations:** Safely assigns vehicles to the first available valid spot and frees them up using license plate lookups.
*   **Live Capacity Tracking:** Real-time checking of available spots via `getAvailableSpots()`.

## How to Run

1. Compile the code using any standard C++ compiler:
   ```bash
   g++ -o parking_lot main.cpp

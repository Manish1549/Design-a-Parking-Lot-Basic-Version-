#include <iostream>
#include <vector>
#include <string>
using namespace std;

enum VehicleType { MOTORCYCLE, CAR, TRUCK };
enum SpotType { COMPACT, LARGE, HANDICAPPED };

class Vehicle {
protected:
    string licensePlate;
    VehicleType type;
public:
    Vehicle(string plate, VehicleType t) : licensePlate(plate), type(t) {}
    VehicleType getType() { return type; }
    string getPlate() { return licensePlate; }
};

class ParkingSpot {
private:
    int id;
    SpotType type;
    bool occupied;
    Vehicle* currentVehicle;
    
public:
    ParkingSpot(int id, SpotType type) : id(id), type(type), occupied(false), currentVehicle(nullptr) {}
    
    bool isAvailable() { return !occupied; }
    
    bool canFit(Vehicle* vehicle) {
        // Check if vehicle fits
        if(vehicle->getType==TRUCK && type!=LARGE){
            return false;
        }
        else if(vehicle->getType==CAR && type==HANDICAPPED){
            return false;
        }
        else if(vehicle->getType==MOTORCYCLE){
            return true;
        }
        else{
            //default
            return false;
        }
    }
    
    void parkVehicle(Vehicle* vehicle) {
        // Park the vehicle
           occupied = true;
           currentVehicle = vehicle;
    }
    
    void removeVehicle() {
        // Remove vehicle
        occupied = false;
        currentVehicle = nullptr;
    }
    Vehicle* getCurrentVehicle(){
        return currentVehicle;
    }
};

class ParkingLot {
private:
    vector<ParkingSpot*> spots;
    
public:
    ParkingLot(int numSpots) {
        // Initialize parking spots
        for(int i=0;i<numSpots;i++){
            if(i<numSpots*0.2){
                spots.push_back(new ParkingSpot(i,HANDICAPPED));
            }
            else if(i<numSpots*0.7){
                spots.push_back(new ParkingSpot(i,COMPACT));
            }
            else{
                spots.push_back(new ParkingSpot(i,LARGE));
            }
        }
    }
    
    bool parkVehicle(Vehicle* vehicle) {
        // Find and park vehicle
        //search for available parkingSpot in parkingLot
        for(auto &spot:spots){
            if(spot->isAvailable() && spot->canFit(vehicle)){
                spot->parkVehicle(vehicle);
                return true;
            }
        }
        return false;
    }
    
    bool unparkVehicle(string licensePlate) {
        // Find and unpark vehicle
        //find those occupied spots which have this vehicle is
        for(auto &spot:spots){
            if(!spot->isAvailable()){
                if(spot->currentVehicle->getPlate==licensePlate){
                    spot->removeVehicle;
                    return true;
                }
            }
        }
        return false;
    }
    
    int getAvailableSpots() {
        // Count available spots
        int count = 0;
        for(auto &spot: spots){
            if(spot->isAvailable()){
                count++;
            }
        }
        return count;
    }
};

int main() {
    // Test your implementation
    return 0;
}

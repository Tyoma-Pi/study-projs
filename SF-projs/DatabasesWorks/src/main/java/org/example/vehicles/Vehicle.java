package org.example.vehicles;

public class Vehicle {
    private String model;
    private String maker;
    private vehicleType type;

    public enum vehicleType {
        Car,
        Motorcycle,
        Bicycle
    };

    public Vehicle(String inputModel, String inputMaker, vehicleType inputType)
    {
        model = inputModel;
        maker = inputMaker;
        type = inputType;
    }
}
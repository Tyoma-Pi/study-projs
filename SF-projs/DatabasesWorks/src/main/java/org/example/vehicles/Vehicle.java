package org.example.vehicles;

public class Vehicle {
    private String maker;
    private String model;
    private String type;

    public Vehicle(String inputMaker, String inputModel, String inputType) {
        this.maker = inputMaker;
        this.model = inputModel;
        this.type = inputType;
    }

    public String getAttribute(String attribute) {
        switch (attribute) {
            case "maker": return this.maker;
            case "model": return this.model;
            case "type": return this.type;
            default: return "";
        }
    }

    @Override
    public String toString() {
        return String.format("%-15s %-15s %s", this.maker, this.model, this.type);
    }
}
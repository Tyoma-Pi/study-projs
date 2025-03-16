package org.example.vehicles;

import java.math.BigDecimal;

public class Motorcycle {
    private String vin;
    private String model;
    private BigDecimal engineCapacity;
    private Integer horsepower;
    private BigDecimal price;
    private enum type {
        Sport,
        Cruiser,
        Touring
    }
}
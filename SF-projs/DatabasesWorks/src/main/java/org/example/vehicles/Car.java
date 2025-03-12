package org.example.vehicles;

import java.math.BigDecimal;

public class Car {
    private String vin;
    private String model;
    private BigDecimal engineCapacity;
    private Integer horsepower;
    private BigDecimal price;
    private enum transmission {
        Automatic,
        Manual
    }
}
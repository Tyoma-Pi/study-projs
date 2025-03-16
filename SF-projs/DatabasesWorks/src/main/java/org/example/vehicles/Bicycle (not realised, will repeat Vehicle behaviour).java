package org.example.vehicles;

import java.math.BigDecimal;

public class Bicycle {
    private String serialNumber;
    private String model;
    private Integer gearCount;
    private BigDecimal price;
    private enum type {
        Mountain,
        Road,
        Hybrid
    }
}
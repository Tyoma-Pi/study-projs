package org.example.booking;

import java.math.BigDecimal;

public class Room {
    private Integer roomID;
    private Integer hotelID;
    private enum roomType {
        Single,
        Double,
        Suite
    }
    private BigDecimal price;
    private Integer capacity;
}
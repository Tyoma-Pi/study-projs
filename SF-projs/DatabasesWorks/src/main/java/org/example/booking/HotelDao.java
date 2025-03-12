package org.example.booking;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class HotelDao implements Dao<Hotel> {
    @Override
    public Optional<Hotel> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Hotel> getAll() {
        return null;
    }
    
    @Override
    public void save(Hotel hotel) {
    }
    
    @Override
    public void update(Hotel hotel, String[] params) {
    }
    
    @Override
    public void delete(Hotel hotel) {
    }
}

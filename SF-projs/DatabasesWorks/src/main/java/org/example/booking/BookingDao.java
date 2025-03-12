package org.example.booking;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class BookingDao implements Dao<Booking> {
    @Override
    public Optional<Booking> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Booking> getAll() {
        return null;
    }
    
    @Override
    public void save(Booking booking) {
    }
    
    @Override
    public void update(Booking booking, String[] params) {
    }
    
    @Override
    public void delete(Booking booking) {
    }
}

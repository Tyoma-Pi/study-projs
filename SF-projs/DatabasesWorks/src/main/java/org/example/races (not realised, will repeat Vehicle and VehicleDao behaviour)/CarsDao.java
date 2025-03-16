package org.example.races;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class CarsDao implements Dao<Cars> {
    @Override
    public Optional<Cars> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Cars> getAll() {
        return null;
    }
    
    @Override
    public void save(Cars car) {
    }
    
    @Override
    public void update(Cars car, String[] params) {
    }
    
    @Override
    public void delete(Cars car) {
    }
}
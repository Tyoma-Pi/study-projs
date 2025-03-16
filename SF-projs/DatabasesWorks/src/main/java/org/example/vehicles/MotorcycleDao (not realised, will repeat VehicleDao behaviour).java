package org.example.vehicles;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class MotorcycleDao implements Dao<Motorcycle> {
    @Override
    public Optional<Motorcycle> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Motorcycle> getAll() {
        return null;
    }
    
    @Override
    public void save(Motorcycle motorcycle) {
    }
    
    @Override
    public void update(Motorcycle motorcycle, String[] params) {
    }
    
    @Override
    public void delete(Motorcycle motorcycle) {
    }
}
package org.example.vehicles;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class CarDao implements Dao<Car> {
    @Override
    public Optional<Car> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Car> getAll() {
        return null;
    }
    
    @Override
    public void save(Car car) {
    }
    
    @Override
    public void update(Car car, String[] params) {
    }
    
    @Override
    public void delete(Car car) {
    }
}
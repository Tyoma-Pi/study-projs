package org.example.vehicles;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class VehicleDao implements Dao<Vehicle> {
    @Override
    public Optional<Vehicle> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Vehicle> getAll() {
        return null;
    }
    
    @Override
    public void save(Vehicle vehicle) {
    }
    
    @Override
    public void update(Vehicle vehicle, String[] params) {
    }
    
    @Override
    public void delete(Vehicle vehicle) {
    }
}
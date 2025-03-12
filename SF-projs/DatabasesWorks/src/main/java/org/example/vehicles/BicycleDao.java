package org.example.vehicles;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class BicycleDao implements Dao<Bicycle> {
    @Override
    public Optional<Bicycle> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Bicycle> getAll() {
        return null;
    }
    
    @Override
    public void save(Bicycle bicycle) {
    }
    
    @Override
    public void update(Bicycle bicycle, String[] params) {
    }
    
    @Override
    public void delete(Bicycle bicycle) {
    }
}
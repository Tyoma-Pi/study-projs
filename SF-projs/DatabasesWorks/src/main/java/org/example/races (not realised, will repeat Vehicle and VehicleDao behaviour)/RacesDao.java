package org.example.races;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class RacesDao implements Dao<Races> {
    @Override
    public Optional<Races> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Races> getAll() {
        return null;
    }
    
    @Override
    public void save(Races race) {
    }
    
    @Override
    public void update(Races race, String[] params) {
    }
    
    @Override
    public void delete(Races race) {
    }
}
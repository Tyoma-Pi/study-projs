package org.example.races;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class ResultsDao implements Dao<Results> {
    @Override
    public Optional<Results> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Results> getAll() {
        return null;
    }
    
    @Override
    public void save(Results result) {
    }
    
    @Override
    public void update(Results result, String[] params) {
    }
    
    @Override
    public void delete(Results result) {
    }
}
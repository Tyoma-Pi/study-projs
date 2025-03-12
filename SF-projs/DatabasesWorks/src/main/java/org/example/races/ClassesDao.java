package org.example.races;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class ClassesDao implements Dao<Classes> {
    @Override
    public Optional<Classes> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Classes> getAll() {
        return null;
    }
    
    @Override
    public void save(Classes currentClass) {
    }
    
    @Override
    public void update(Classes currentClass, String[] params) {
    }
    
    @Override
    public void delete(Classes currentClass) {
    }
}
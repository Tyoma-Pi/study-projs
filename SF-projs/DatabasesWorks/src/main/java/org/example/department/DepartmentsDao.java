package org.example.department;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class DepartmentsDao implements Dao<Departments> {
    @Override
    public Optional<Departments> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Departments> getAll() {
        return null;
    }
    
    @Override
    public void save(Departments department) {
    }
    
    @Override
    public void update(Departments department, String[] params) {
    }
    
    @Override
    public void delete(Departments department) {
    }
}

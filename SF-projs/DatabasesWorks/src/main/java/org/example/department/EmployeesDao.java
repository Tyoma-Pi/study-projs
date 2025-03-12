package org.example.department;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class EmployeesDao implements Dao<Employees> {
    @Override
    public Optional<Employees> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Employees> getAll() {
        return null;
    }
    
    @Override
    public void save(Employees employee) {
    }
    
    @Override
    public void update(Employees employee, String[] params) {
    }
    
    @Override
    public void delete(Employees employee) {
    }
}

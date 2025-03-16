package org.example.department;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class RolesDao implements Dao<Roles> {
    @Override
    public Optional<Roles> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Roles> getAll() {
        return null;
    }
    
    @Override
    public void save(Roles role) {
    }
    
    @Override
    public void update(Roles role, String[] params) {
    }
    
    @Override
    public void delete(Roles role) {
    }
}

package org.example.department;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class ProjectsDao implements Dao<Projects> {
    @Override
    public Optional<Projects> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Projects> getAll() {
        return null;
    }
    
    @Override
    public void save(Projects project) {
    }
    
    @Override
    public void update(Projects project, String[] params) {
    }
    
    @Override
    public void delete(Projects project) {
    }
}

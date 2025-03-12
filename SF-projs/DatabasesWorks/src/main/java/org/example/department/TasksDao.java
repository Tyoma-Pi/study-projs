package org.example.department;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class TasksDao implements Dao<Tasks> {
    @Override
    public Optional<Tasks> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Tasks> getAll() {
        return null;
    }
    
    @Override
    public void save(Tasks task) {
    }
    
    @Override
    public void update(Tasks task, String[] params) {
    }
    
    @Override
    public void delete(Tasks task) {
    }
}

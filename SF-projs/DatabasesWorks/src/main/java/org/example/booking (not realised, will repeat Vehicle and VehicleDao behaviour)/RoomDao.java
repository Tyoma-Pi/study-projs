package org.example.booking;

import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class RoomDao implements Dao<Room> {
    @Override
    public Optional<Room> get(long id) {
        return Optional.empty();
    }
    
    @Override
    public List<Room> getAll() {
        return null;
    }
    
    @Override
    public void save(Room room) {
    }
    
    @Override
    public void update(Room room, String[] params) {
    }
    
    @Override
    public void delete(Room room) {
    }
}

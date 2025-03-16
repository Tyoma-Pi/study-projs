package org.example;

import java.sql.Connection;
import java.util.List;
import java.util.Optional;

public interface Dao<T> {
    Optional<T> get(String identifier, Connection DBConnection);

    List<T> getAll(Connection DBConnection);

    void save(T t, Connection DBConnection);

    void update(T t, String[] params, Connection DBConnection);

    void delete(T t, Connection DBConnection);
}
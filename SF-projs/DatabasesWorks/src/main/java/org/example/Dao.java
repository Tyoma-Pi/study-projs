package org.example;

import java.sql.Connection;
import java.sql.ResultSet;
import java.util.List;

public interface Dao<T> {
    ResultSet get(Connection DBConnection, String identifier);

    List<T> getAll(Connection DBConnection);

    void save(Connection DBConnection, T t);

    void update(Connection DBConnection, T t, String[] params);

    void delete(Connection DBConnection, T t);
}
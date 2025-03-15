package org.example.vehicles;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class VehicleDao implements Dao<Vehicle> {
    @Override
    public Vehicle get(Connection DBConnection, String identifier) {
        // executeQuery()
        String SQLQuery = "SELECT * FROM Vehicle WHERE model=?";
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            SQLStatement.setString(1, SQLQuery);
            ResultSet SQLData =  SQLStatement.executeQuery();
            while (SQLData.next()) {
                return new Vehicle()
            }
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
            return null;
        }
    }
    
    @Override
    public List<Vehicle> getAll(Connection DBConnection) {
        // executeQuery()
        try () {
            
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
    
    @Override
    public void save(Connection DBConnection, Vehicle vehicle) {
        // executeUpdate()
        try () {
            
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
    
    @Override
    public void update(Vehicle vehicle, String[] params) {
        // executeUpdate()
        try () {
            
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
    
    @Override
    public void delete(Vehicle vehicle) {
        // executeUpdate()
        try () {
            
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
}
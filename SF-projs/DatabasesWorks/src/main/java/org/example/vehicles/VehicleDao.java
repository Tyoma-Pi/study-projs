package org.example.vehicles;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.example.Dao;

public class VehicleDao implements Dao<Vehicle> {
    @Override
    public Optional<Vehicle> get(String identifier, Connection DBConnection) {
        String SQLQuery = "SELECT * FROM Vehicles WHERE model=?";
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            SQLStatement.setString(1, identifier);
            ResultSet SQLData = SQLStatement.executeQuery();
            while (SQLData.next()) {
                return Optional.of(new Vehicle(SQLData.getString(1), SQLData.getString(2), SQLData.getString(3)));
            }
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
        return Optional.empty();
    }
    
    @Override
    public List<Vehicle> getAll(Connection DBConnection) {
        String SQLQuery = "SELECT * FROM Vehicles";
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            List<Vehicle> vehicleList = new ArrayList<>();
            ResultSet SQLData = SQLStatement.executeQuery();
            while (SQLData.next()) {
                vehicleList.add(new Vehicle(SQLData.getString(1), SQLData.getString(2), SQLData.getString(3)));
            }
            return vehicleList;
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
        return null;
    }
    
    @Override
    public void save(Vehicle vehicle, Connection DBConnection) {
        String SQLQuery = "INSERT INTO Vehicles (maker, model, type) VALUES (?, ?, ?)";
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            SQLStatement.setString(1, vehicle.getAttribute("maker"));
            SQLStatement.setString(2, vehicle.getAttribute("model"));
            SQLStatement.setString(3, vehicle.getAttribute("type"));
            SQLStatement.executeUpdate();
            System.out.println(String.format("Добавлена запись:\n%s", vehicle));
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
    
    @Override
    public void update(Vehicle vehicle, String[] params, Connection DBConnection) {
        // executeUpdate()
        String SQLQuery = "UPDATE Vehicles SET (maker, model, type)=(?, ?, ?) WHERE maker = ? AND model = ?";
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            SQLStatement.setString(1, params[0]);
            SQLStatement.setString(2, params[1]);
            SQLStatement.setString(3, params[2]);
            SQLStatement.setString(4, vehicle.getAttribute("maker"));
            SQLStatement.setString(5, vehicle.getAttribute("model"));
            SQLStatement.executeUpdate();
            System.out.println(String.format("Запись\n%s\nбыла заменена на\n%-15s %-15s %s", vehicle, params[0], params[1], params[2]));
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
    
    @Override
    public void delete(Vehicle vehicle, Connection DBConnection) {
        // executeUpdate()
        String SQLQuery = "DELETE FROM Vehicles WHERE model=?";
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            SQLStatement.setString(1, vehicle.getAttribute("model"));
            SQLStatement.executeUpdate();
            System.out.println(String.format("Удалена запись:\n%s", vehicle));
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
}
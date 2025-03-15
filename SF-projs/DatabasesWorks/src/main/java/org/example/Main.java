package org.example;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Main {
    private final static String HOST = "localhost";
    private final static String DATABASENAME = "task1";
    private final static String USERNAME = "root";
    private final static String PASSWORD = "";
    public static void main(String[] args) {
        String url = "jdbc:mysql://" + HOST + "/" + DATABASENAME + "?user=" + USERNAME + "&password=" + PASSWORD;
        try (Connection DBConnection = DriverManager.getConnection(url)) {
            if (DBConnection == null) {
                System.err.println("Нет соединения с БД.");
            } else {
                System.out.println("Соединение с БД установлено.");
                String SQLQuery = "SELECT * FROM Vehicle";
                PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery);
                // boolean isExecuted = SQLStatement.execute(SQLQuery);
                // if (isExecuted) {
                //     System.out.println("Selected all the vehicles.");
                // }
                ResultSet SQLData = SQLStatement.executeQuery(SQLQuery);
                while (SQLData.next()) {
                    if (SQLData.wasNull()) {
                        System.out.println("NULL");
                    } else {
                        System.out.println(SQLData.getString("maker")+"\t"+SQLData.getString("model"));
                    }
                }
                SQLStatement.close();
            }
        } catch (SQLException throwables) {
            System.out.println("Ошибка при подключении к БД");
            throwables.printStackTrace();
        }
    }
}
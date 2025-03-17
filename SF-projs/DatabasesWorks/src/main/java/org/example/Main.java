package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.Scanner;

public class Main {
    private final static String HOST = "localhost";
    private static String DATABASENAME;
    private final static String USERNAME = "postgres";
    private final static String PASSWORD = "postgres";
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        System.out.println("Выберите базу данных: test1, test2, test3 или test4");
        DATABASENAME = new Scanner(System.in).next();
        String url = "jdbc:postgresql://" + HOST + "/" + DATABASENAME + "?user=" + USERNAME + "&password=" + PASSWORD;
        try (Connection DBConnection = DriverManager.getConnection(url)) {
            if (DBConnection == null) {
                System.err.println("Нет соединения с БД.");
            } else {
                System.out.println("Соединение с БД установлено.");
                switch (DATABASENAME) {
                    case "test1":
                        System.out.println("Введите номер выполняемого запроса на поиск данных - от 1 до 2");
                        break;
                    case "test2":
                        System.out.println("Введите номер выполняемого запроса на поиск данных - от 1 до 5");
                        break;
                    case "test3":
                        System.out.println("Введите номер выполняемого запроса на поиск данных - от 1 до 3");
                        break;
                    case "test4":
                        System.out.println("Введите номер выполняемого запроса на поиск данных - от 1 до 3");
                        break;
                    default:
                        System.out.println("Данной базы данных нет.");
                }
                int queryNumber = new Scanner(System.in).nextInt();
                getSetFromDatabase(DATABASENAME, queryNumber, DBConnection);
            }
        } catch (SQLException throwables) {
            System.out.println("Ошибка при подключении к БД");
            throwables.printStackTrace();
        }
    }

    public static void getSetFromDatabase(String databaseName, int taskNumber, Connection DBConnection) {
        String SQLQuery = "";
        switch (databaseName) {
            case "test1":
                DATABASENAME = "test1";
                switch (taskNumber) {
                    case 1:
                        SQLQuery = "SELECT * FROM Task1";
                        break;
                    case 2:
                        SQLQuery = "SELECT * FROM Task2";
                        break;
                    default:
                        System.out.println("Данного запроса нет.");
                }
                break;
            case "test2":
                DATABASENAME = "test2";
                switch (taskNumber) {
                    case 1:
                        SQLQuery = "SELECT * FROM Task1";
                        break;
                    case 2:
                        SQLQuery = "SELECT * FROM Task2";
                        break;
                    case 3:
                        SQLQuery = "SELECT * FROM Task3";
                        break;
                    case 4:
                        SQLQuery = "SELECT * FROM Task4";
                        break;
                    case 5:
                        SQLQuery = "SELECT * FROM Task5";
                        break;
                    default:
                        System.out.println("Данного запроса нет.");
                }
                break;
            case "test3":
                DATABASENAME = "test3";
                switch (taskNumber) {
                    case 1:
                        SQLQuery = "SELECT * FROM Task1";
                        break;
                    case 2:
                        SQLQuery = "SELECT * FROM Task2";
                        break;
                    case 3:
                        SQLQuery = "SELECT * FROM Task3";
                        break;
                    default:
                        System.out.println("Данного запроса нет.");
                }
                break;
            case "test4":
                DATABASENAME = "test4";
                switch (taskNumber) {
                    case 1:
                        SQLQuery = "SELECT * FROM Task1";
                        break;
                    case 2:
                        SQLQuery = "SELECT * FROM Task2";
                        break;
                    case 3:
                        SQLQuery = "SELECT * FROM Task3";
                        break;
                    default:
                        System.out.println("Данного запроса нет.");
                }
                break;
            default:
                System.out.println("Данной базы данных нет.");
        }
        try (PreparedStatement SQLStatement = DBConnection.prepareStatement(SQLQuery)) {
            ResultSet SQLData = SQLStatement.executeQuery();
            ResultSetMetaData metaData = SQLData.getMetaData();
            int columnsCount = metaData.getColumnCount();
            while (SQLData.next()) {
                for (int i = 1; i <= columnsCount; i++) {
                    if (i > 1) System.out.print("\t");
                    System.out.print(SQLData.getString(i));
                }
                System.out.println();
            }
        } catch (SQLException throwables) {
            System.out.println("Ошибка при выполнении запроса.");
            throwables.printStackTrace();
        }
    }
}
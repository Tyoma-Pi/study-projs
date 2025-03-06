package org.example;
import java.util.Scanner;

public class Main {
    public static ChessBoard buildBoard() {
        ChessBoard board = new ChessBoard("White");

        board.board[0][0] = new Rook("White");
        board.board[0][1] = new Horse("White");
        board.board[0][2] = new Bishop("White");
        board.board[0][3] = new Queen("White");
        board.board[0][4] = new King("White");
        board.board[0][5] = new Bishop("White");
        board.board[0][6] = new Horse("White");
        board.board[0][7] = new Rook("White");
        board.board[1][0] = new Pawn("White");
        board.board[1][1] = new Pawn("White");
        board.board[1][2] = new Pawn("White");
        board.board[1][3] = new Pawn("White");
        board.board[1][4] = new Pawn("White");
        board.board[1][5] = new Pawn("White");
        board.board[1][6] = new Pawn("White");
        board.board[1][7] = new Pawn("White");

        board.board[7][0] = new Rook("Black");
        board.board[7][1] = new Horse("Black");
        board.board[7][2] = new Bishop("Black");
        board.board[7][3] = new Queen("Black");
        board.board[7][4] = new King("Black");
        board.board[7][5] = new Bishop("Black");
        board.board[7][6] = new Horse("Black");
        board.board[7][7] = new Rook("Black");
        board.board[6][0] = new Pawn("Black");
        board.board[6][1] = new Pawn("Black");
        board.board[6][2] = new Pawn("Black");
        board.board[6][3] = new Pawn("Black");
        board.board[6][4] = new Pawn("Black");
        board.board[6][5] = new Pawn("Black");
        board.board[6][6] = new Pawn("Black");
        board.board[6][7] = new Pawn("Black");
        return board;
    }

    public static void main(String[] args) {
        ChessBoard board = buildBoard();
        Scanner scanner = new Scanner(System.in);
        board.printBoard();
        while (true) {
            String command = scanner.nextLine().trim().toLowerCase();
            switch (command) {
                case "exit":
                    break;
                case "replay":
                    System.out.println("Заново");
                    board = buildBoard();
                    board.printBoard();
                    break;
                case "castling0":
                case "castling7":
                    handleCastling(board, command);
                    break;
                case "":
                    break;
                default:
                    handleMove(board, command);
            }
            if (command.equals("exit")) break;
        }
        scanner.close();
    }

    private static void handleCastling(ChessBoard board, String command) {
        int column = (command.equals("castling0")) ? 0 : 7;
        boolean castling = column == 0 ? board.castling0() : board.castling7();
        if (castling) {
            System.out.println("Рокировка удалась");
            board.printBoard();
        } else {
            String reason = board.getCastlingError(column);
            System.out.println("Рокировка не удалась: " + reason);
        }
    }


    private static void handleMove(ChessBoard board, String command) {
        String[] parts = command.split(" ");
        if (parts.length != 5 || !parts[0].equals("move")) {
            System.out.println("Неверный формат команды. Используйте 'move x y z w'");
            return;
        }

        try {
            int startLine = Integer.parseInt(parts[1]);
            int startColumn = Integer.parseInt(parts[2]);
            int endLine = Integer.parseInt(parts[3]);
            int endColumn = Integer.parseInt(parts[4]);

            if (!board.checkPos(startLine) || !board.checkPos(startColumn) || !board.checkPos(endLine) || !board.checkPos(endColumn)) {
                System.out.println("Координаты должны быть в диапазоне от 0 до 7.");
                return;
            }

            if (board.moveToPosition(startLine, startColumn, endLine, endColumn)) {
                System.out.println("Успешно передвинулись");
                board.printBoard();
            } else {
                System.out.println("Передвижение не удалось. Возможно, ход невозможен или фигура не принадлежит текущему игроку.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Неверный формат координат. Используйте целые числа.");
        }
    }
}
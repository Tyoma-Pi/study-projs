package org.example;

public class ChessBoard {
    public ChessPiece[][] board = new ChessPiece[8][8]; // creating a field for game
    String nowPlayer;

    public ChessBoard(String nowPlayer) {
        this.nowPlayer = nowPlayer;
    }

    public String nowPlayerColor() {
        return this.nowPlayer;
    }

    public boolean moveToPosition(int startLine, int startColumn, int endLine, int endColumn) {
        if (checkPos(startLine) && checkPos(startColumn) && checkPos(endLine) && checkPos(endColumn)) {
            ChessPiece piece = board[startLine][startColumn];
            if (piece == null || !nowPlayer.equals(piece.getColor())) return false;

            if (piece.canMoveToPosition(this, startLine, startColumn, endLine, endColumn)) {
                board[endLine][endColumn] = piece;
                board[startLine][startColumn] = null;
                this.nowPlayer = this.nowPlayerColor().equals("White") ? "Black" : "White";

                if ((piece instanceof King || piece instanceof Rook) && piece.check) {
                    piece.check = false;
                }
                return true;
            } else return false;
        } else return false;
    }

    public void printBoard() {
        System.out.println("Turn " + nowPlayer);
        System.out.println();
        System.out.println("Player 2(Black)");
        System.out.println();
        System.out.println("\t0\t1\t2\t3\t4\t5\t6\t7");

        for (int i = 7; i > -1; i--) {
            System.out.print(i + "\t");
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == null) {
                    System.out.print(".." + "\t");
                } else {
                    System.out.print(board[i][j].getSymbol() + board[i][j].getColor().substring(0, 1).toLowerCase() + "\t");
                }
            }
            System.out.println();
            System.out.println();
        }
        System.out.println("Player 1(White)");
    }

    public boolean checkPos(int pos) {
        return pos >= 0 && pos <= 7;
    }

    public boolean castling0() {
        return castling(0);
    }

    public boolean castling7() {
        return castling(7);
    }

    private boolean castling(int rookColumn) {
        String color = nowPlayer;
        int row = (color.equals("White")) ? 0 : 7;
        int kingColumn = 4;
        int newKingColumn = (rookColumn == 0) ? 2 : 6;
        int newRookColumn = (rookColumn == 0) ? 3 : 5;

        // Проверки:
        if (board[row][rookColumn] == null || board[row][kingColumn] == null) return false;
        ChessPiece rook = board[row][rookColumn];
        ChessPiece king = board[row][kingColumn];

        if (!rook.getSymbol().equals("R") || !king.getSymbol().equals("K") ||
                !rook.getColor().equals(color) || !king.getColor().equals(color) ||
                !rook.check || !king.check) return false;

        for (int i = Math.min(rookColumn, kingColumn) + 1; i < Math.max(rookColumn, kingColumn); i++) {
            if (board[row][i] != null) return false;
        }

        if (new King(color).isUnderAttack(this, row, kingColumn)) return false; //Проверка на атаку перед рокировкой

        board[row][kingColumn] = null;
        board[row][newKingColumn] = king;
        king.check = false;
        board[row][rookColumn] = null;
        board[row][newRookColumn] = rook;
        rook.check = false;
        nowPlayer = (color.equals("White")) ? "Black" : "White";
        return true;
    }

    public String getCastlingError(int column) {
        String color = nowPlayer;
        int row = (color.equals("White")) ? 0 : 7;
        int kingColumn = 4;

        if (board[row][column] == null || board[row][kingColumn] == null) return "Ладья или король отсутствуют.";
        ChessPiece rook = board[row][column];
        ChessPiece king = board[row][kingColumn];

        if (!rook.getSymbol().equals("R") || !king.getSymbol().equals("K") ||
                !rook.getColor().equals(color) || !king.getColor().equals(color) ||
                !rook.check || !king.check) return "Ладья или король уже двигались.";


        for (int i = Math.min(column, kingColumn) + 1; i < Math.max(column, kingColumn); i++) {
            if (board[row][i] != null) return "Путь к ладье заблокирован.";
        }

        if (new King(color).isUnderAttack(this, row, kingColumn)) return "Король находится под шахом.";

        return "Неизвестная ошибка.";
    }
}
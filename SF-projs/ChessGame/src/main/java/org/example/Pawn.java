package org.example;

public class Pawn extends ChessPiece {

    public Pawn(String color) {
        super(color);
    }

    @Override
    public String getColor() {
        return super.getColor();
    }

    @Override
    public boolean canMoveToPosition(ChessBoard chessBoard, int line, int column, int toLine, int toColumn) {
        if (!chessBoard.checkPos(toLine) || !chessBoard.checkPos(toColumn)) return false;

        if (line == toLine && column == toColumn) return false;

        int direction = getColor().equals("White") ? 1 : -1; // 1 для белых, -1 для черных
        int deltaLine = toLine - line;

        boolean isFirstMove = (getColor().equals("White") && line == 1) || (getColor().equals("Black") && line == 6);
        boolean isTwoStepMove = deltaLine == 2 * direction && column == toColumn;

        boolean isOneStepMove = deltaLine == direction && column == toColumn;

        return (isFirstMove && isTwoStepMove) || isOneStepMove;
    }

    @Override
    public String getSymbol() {
        return "P";
    }
}


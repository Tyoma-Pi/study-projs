using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace Reflection.Differentiation
{
    public static class Algebra
    {
        public static Expression<Func<double, double>> Differentiate(Expression<Func<double, double>> expr) =>
            Expression.Lambda<Func<double, double>>(GetDifferentiate(expr.Body), expr.Parameters);

        private static Expression GetDifferentiate(Expression expr)
        {
            switch (expr.NodeType)
            {
                case ExpressionType.Call: return GetDifferentiate(expr as MethodCallExpression);
                case ExpressionType.Multiply: return DiffMultiply(expr as BinaryExpression);
                case ExpressionType.Add: return DiffAdd(expr as BinaryExpression);
                case ExpressionType.Parameter: return Expression.Constant(1.0);
                case ExpressionType.Constant: return Expression.Constant(0.0);
                default: throw new ArgumentException(expr.ToString());
            }
        }

        static Expression GetDifferentiate(MethodCallExpression calledExpr) =>
            (calledExpr.Method.Name == nameof(Math.Cos)) ? DiffSinCos(calledExpr, "Sin", -1.0) :
            (calledExpr.Method.Name == nameof(Math.Sin)) ? DiffSinCos(calledExpr, "Cos") :
            throw new ArgumentException(calledExpr.ToString());

        private static Expression DiffAdd(BinaryExpression binExpr) =>
        Expression.Add(GetDifferentiate(binExpr.Left), GetDifferentiate(binExpr.Right));

        private static Expression DiffMultiply(BinaryExpression binExpr) =>
        Expression.Add(
            Expression.Multiply(GetDifferentiate(binExpr.Left), binExpr.Right),
            Expression.Multiply(GetDifferentiate(binExpr.Right), binExpr.Left));

        private static Expression DiffSinCos(MethodCallExpression calledExpr, string name, double sign = 1.0) =>
        Expression.Multiply(
            Expression.Multiply(Expression.Constant(sign),
                Expression.Call(typeof(Math).GetMethod(name), calledExpr.Arguments.First())),
            GetDifferentiate(calledExpr.Arguments.First()));
    }
}

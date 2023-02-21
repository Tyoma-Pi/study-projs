using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Incapsulation.RationalNumbers
{
    public class Rational
    {
        public int Numerator;
        public int Denominator;

        public bool IsNan
        {
            get
            {
                return Denominator == 0;
            }
        }
        
        public Rational(int numerat, int denominat = 1)
        {
            Numerator = numerat;
            Denominator = denominat;
            UpdateSign();
            ReduceFract();
        }

        private void UpdateSign()
        {
            var sign = Numerator < 0 ^ Denominator < 0 ? -1 : 1;
            Numerator = sign * Math.Abs(Numerator);
            Denominator = Math.Abs(Denominator);
        }

        private void ReduceFract()
        {
            int gcd = (int)BigInteger.GreatestCommonDivisor(Numerator, Denominator);
            if (gcd > 1)
            { 
                Numerator /= gcd;
                Denominator /= gcd; 
            }
        }

        public static Rational operator +(Rational R1, Rational R2)
        {
            return new Rational(
                R1.Numerator * R2.Denominator + R1.Denominator * R2.Numerator,
                R1.Denominator * R2.Denominator);
        }

        public static Rational operator -(Rational R1, Rational R2)
        {
            return new Rational(
                R1.Numerator * R2.Denominator - R1.Denominator * R2.Numerator,
                R1.Denominator * R2.Denominator);
        }

        public static Rational operator *(Rational R1, Rational R2)
        {
            return new Rational(R1.Numerator * R2.Numerator, R1.Denominator * R2.Denominator);
        }

        public static Rational operator /(Rational R1, Rational R2)
        {
            return R2.Denominator != 0 ?
                new Rational(R1.Numerator * R2.Denominator, R1.Denominator * R2.Numerator) :
                new Rational(R2.Numerator, R2.Denominator);
        }

        public static implicit operator Rational(int R)
        {
            return new Rational(R);
        }

        public static implicit operator double(Rational R)
        {
            return !R.IsNan ? (double)R.Numerator / (double)R.Denominator : double.NaN;
        }

        public static explicit operator int(Rational R)
        {
            return R.Denominator == 1 ? R.Numerator : throw new ArgumentException();
        }
    }
}

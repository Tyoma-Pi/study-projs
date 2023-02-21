using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Incapsulation.Weights
{
    public class Indexer
    {
        private readonly double[] indexes;
        private readonly int start;
        private readonly int length;

        public int Length
        {
            get
            {
                return length;
            }
        }

        public Indexer(double[] indexes, int start, int length)
        {
            if (start < 0 || length < 0 || (start + length) > indexes.Length)
            {
                throw new ArgumentException();
            }
            this.indexes = indexes;
            this.start = start;
            this.length = length;
        }

        public int Check(int val)
        {
            if (val < 0 || val >= Length) throw new IndexOutOfRangeException();
            return val;
        }

        public double this[int n]
        {
            get
            {
                return indexes[start + Check(n)];
            }
            set
            {
                indexes[start + Check(n)] = value;
            }
        }
    }
}
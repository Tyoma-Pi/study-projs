using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Delegates.PairsAnalysis
{
    public static class Analysis
    {
        public static IEnumerable<Tuple<T, T>> Pairs<T>(this IEnumerable<T> data)
        {
            var enumeratedData = data.GetEnumerator();
            enumeratedData.MoveNext();

            var previous = enumeratedData.Current;

            while (enumeratedData.MoveNext())
            {
                yield return Tuple.Create(previous, enumeratedData.Current);
                previous = enumeratedData.Current;
            }
        }

        public static int MaxIndex<T>(this IEnumerable<T> data) =>
            data.Select((val, id) => new { Index = id, Value = val }).
            OrderByDescending(elem => elem.Value).First().Index;

        public static int FindMaxPeriodIndex(params DateTime[] dates)
        {
            return dates.Pairs().Select(datePair => datePair.Item2 - datePair.Item1).MaxIndex();
        }

        public static double FindAverageRelativeDifference(params double[] data)
        {
            return (data.Length < 2) ? throw new InvalidOperationException() :
                data.Pairs().Select(dataPair => (dataPair.Item2 - dataPair.Item1) / dataPair.Item1).First();
        }
    }
}

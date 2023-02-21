using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace Reflection.Randomness
{
    public class FromDistribution : Attribute
    {
        public IContinuousDistribution Distribution { get; set; }

        public FromDistribution(Type distribType, params object[] prms)
        {
            if (!distribType.GetConstructors().Any(z => z.GetParameters().Count() == prms.Length))
                throw new ArgumentException(distribType.ToString());

            Distribution = Activator.CreateInstance(distribType, prms) as IContinuousDistribution;
        }
    }

    public class Generator<T> where T : new()
    {
        public Dictionary<PropertyInfo, FromDistribution> Items;

        public Generator()
        {
            Items = typeof(T).GetProperties().
                Where(item => item.GetCustomAttributes().
                OfType<FromDistribution>().Count() > 0).
                ToDictionary(item => item, item => item.GetCustomAttributes().OfType<FromDistribution>().First());
        }

        public T Generate(Random data)
        {
            var result = new T();

            foreach (var i in Items)
                i.Key.SetValue(result, i.Value.Distribution.Generate(data));

            return result;
        }
    }
}

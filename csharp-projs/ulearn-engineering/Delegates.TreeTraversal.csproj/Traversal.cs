using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Delegates.TreeTraversal
{
    public static class Traversal
    {
        public static IEnumerable<R> ProcessCurrentPoint<T, R>(
            T point,
            Func<T, R> valuesSelector,
            Func<T, IEnumerable<T>> childrenSelector)
        {
            R value = valuesSelector(point);
            if (!Equals(value, default(R))) yield return value;

            foreach (T childPoint in childrenSelector(point))
                foreach (R childValue in ProcessCurrentPoint(childPoint, valuesSelector, childrenSelector))
                    yield return childValue;
        }

        public static IEnumerable<Product> GetProducts(ProductCategory rootCategory) =>
            ProcessCurrentPoint(rootCategory, prod => prod.Products, prod => prod.Categories).SelectMany(r => r);

        public static IEnumerable<Job> GetEndJobs(Job rootJob)
        {
            return ProcessCurrentPoint(rootJob,
                job =>
                {
                    if (job.Subjobs.Count != 0 && job.Subjobs != null) return null;
                    return job;
                },
                job => job.Subjobs);
        }

        public static IEnumerable<T> GetBinaryTreeValues<T>(BinaryTree<T> rootOfBinaryTree)
        {
            return ProcessCurrentPoint(rootOfBinaryTree,
                tree => 
                {
                    if (tree.Left == null && tree.Right == null) return tree.Value;
                    return default;
                },
                tree =>
                {
                    var stick = new List<BinaryTree<T>>();
                    if (tree.Left != null) stick.Add(tree.Left);
                    if (tree.Right != null) stick.Add(tree.Right);
                    return stick;
                });
        }
    }
}

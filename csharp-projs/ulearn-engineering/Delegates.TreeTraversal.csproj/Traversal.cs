using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Delegates.TreeTraversal
{
    public static class Traversal
    {
        public static IEnumerable<R> ProcessCurrentNode<T, R>(
            T node,
            Func<T, R> valuesSelector,
            Func<T, IEnumerable<T>> childrenSelector)
        {
            R value = valuesSelector(node);
            if (!Equals(value, default(R))) yield return value;

            foreach (T childNode in childrenSelector(node))
                foreach (R childValue in ProcessCurrentNode(childNode, valuesSelector, childrenSelector))
                    yield return childValue;
        }

        public static IEnumerable<Product> GetProducts(ProductCategory prodsCatsRoot) =>
            ProcessCurrentNode(prodsCatsRoot, prod => prod.Products, prod => prod.Categories).SelectMany(r => r);

        public static IEnumerable<Job> GetEndJobs(Job jobsRoot) =>
            ProcessCurrentNode(jobsRoot,
                job => job.Subjobs.Count != 0 && job.Subjobs != null ? null : job,
                job => job.Subjobs);

        public static IEnumerable<T> GetBinaryTreeValues<T>(BinaryTree<T> binaryTreeRoot) =>
            ProcessCurrentNode(binaryTreeRoot,
                tree => tree.Left == null && tree.Right == null ? tree.Value : default,
                tree => {
                    var stick = new List<BinaryTree<T>>();
                    if (tree.Left != null) stick.Add(tree.Left);
                    if (tree.Right != null) stick.Add(tree.Right);
                    return stick;
                });
    }
}

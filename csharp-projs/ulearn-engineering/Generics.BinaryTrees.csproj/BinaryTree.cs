using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics.BinaryTrees
{
    public class BinaryTree<T> : IEnumerable<T>
        where T : IComparable
    {
        public BinaryTree<T> Left;
        public BinaryTree<T> Right;
        public SortedSet<T> Tree;
        public T Value;

        public BinaryTree()
        {
            Tree = new SortedSet<T>();
            Value = default;
        }

        public void Add(T element)
        {
            if (Tree.Count == 0)
            {
                Value = element;
            }
            else if (Value.CompareTo(element) >= 0)
            {
                if (Left == null) Left = new BinaryTree<T>();
                Left.Add(element);
            }
            else
            {
                if (Right == null) Right = new BinaryTree<T>();
                Right.Add(element);
            }
            Tree.Add(element);
        }

        public IEnumerator<T> GetEnumerator()
        {
            return Tree.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return Tree.GetEnumerator();
        }
    }

    public class BinaryTree
    {
        public static BinaryTree<T> Create<T>(params T[] numbers) where T : IComparable
        {
            var binaryTree = new BinaryTree<T>();
            for (var i = 0; i < numbers.Length; i++)
            {
                binaryTree.Add(numbers[i]);
            }
            return binaryTree;
        }
    }
}

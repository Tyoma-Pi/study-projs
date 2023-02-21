using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance.DataStructure
{
    public class Category : IComparable
    {
        public string prodName;
        public MessageType type;
        public MessageTopic topic;

        public Category(string prodName, MessageType type, MessageTopic topic)
        {
            this.prodName = prodName;
            this.type = type;
            this.topic = topic;
        }

        public int CompareTo(object obj)
        {
            if (obj == null || obj.GetType() != this.GetType()) return 1;
            Category cat = (Category)obj;
            if (Equals(obj)) return 0;
            var prodCompare = string.Compare(prodName, cat.prodName);
            var typeCompare = type.CompareTo(cat.type);
            var topicCompare = topic.CompareTo(cat.topic);
            if (prodCompare != 0) return prodCompare;
            if (typeCompare != 0) return typeCompare;
            if (topicCompare != 0) return topicCompare;
            return 0;
        }

        public static bool operator <(Category C1, Category C2)
        {
            return C1.CompareTo(C2) == -1;
        }

        public static bool operator >(Category C1, Category C2)
        {
            return C1.CompareTo(C2) == 1;
        }

        public static bool operator <=(Category C1, Category C2)
        {
            return C1.CompareTo(C2) <= 0;
        }

        public static bool operator >=(Category C1, Category C2)
        {
            return C1.CompareTo(C2) >= 0;
        }

        public override bool Equals(object obj)
        {
            if (obj == null) return false;
            return obj.GetHashCode() == this.GetHashCode();
        }

        public override int GetHashCode()
        {
            if (prodName == null) return base.GetHashCode();
            var hashCode = 10;
            hashCode = hashCode * 5 + prodName.GetHashCode();
            hashCode = hashCode * 4 + topic.GetHashCode();
            hashCode = hashCode * 3 + type.GetHashCode();
            return hashCode;
        }

        public override string ToString()
        {
            return prodName + '.' + type + '.' + topic;
        }
    }
}
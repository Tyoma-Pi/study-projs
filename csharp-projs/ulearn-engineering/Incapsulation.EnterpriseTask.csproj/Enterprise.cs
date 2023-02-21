using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Incapsulation.EnterpriseTask
{
    public class Enterprise
    {
        public readonly Guid guid;

        public Guid Guid
        {
            get
            {
                return guid;
            }
        }

        //public Guid getGuid() { return guid; }
        public Enterprise(Guid guid)
        {
            this.guid = guid;
        }

        public string Name { get; set; }

        //public string getName() { return name; }
        //public void setName(string name) { this.name = name; }

        public string Inn
        {
            get
            {
                return Inn;
            }
            set
            {
                if (Inn.Length != 10 || !Inn.All(z => char.IsDigit(z)))
                    throw new ArgumentException();
                Inn = value;
            }
        }

        //public string getINN() { return inn; }
        //public void setINN(string inn)
        //{
        //    if (inn.Length != 10 || !inn.All(z => char.IsDigit(z)))
        //        throw new ArgumentException();
        //    this.inn = inn;
        //}

        public DateTime EstablishDate { get; set; }

        //public DateTime getEstablishDate()
        //{
        //    return establishDate;
        //}
        //public void setEstablishDate(DateTime establishDate)
        //{
        //    this.establishDate = establishDate;
        //}

        public TimeSpan ActiveTimeSpan
        {
            get
            {
                return DateTime.Now - EstablishDate;
            }
        }

        //public TimeSpan getActiveTimeSpan()
        //{
        //    return DateTime.Now - establishDate;
        //}

        //public double TotalTransactionsAmount
        //{
        //    get
        //    {
        //        DataBase.OpenConnection();
        //        var amount = 0.0;
        //        foreach (Transaction t in DataBase.Transactions().Where(z => z.EnterpriseGuid == Guid))
        //            amount += t.Amount;
        //        return amount;
        //    }
        //}

        public double getTotalTransactionsAmount()
        {
            DataBase.OpenConnection();
            var amount = 0.0;
            foreach (Transaction t in DataBase.Transactions().Where(z => z.EnterpriseGuid == Guid))
                amount += t.Amount;
            return amount;
        }
    }
}

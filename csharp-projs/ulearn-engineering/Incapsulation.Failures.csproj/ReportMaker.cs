using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Incapsulation.Failures
{
    public class Common
    {
        public static int IsEarlier(object[] v, int day, int month, int year)
        {
            int vYear = (int)v[2];
            int vMonth = (int)v[1];
            int vDay = (int)v[0];
            if (vYear < year) return 1;
            if (vYear > year) return 0;
            if (vMonth < month) return 1;
            if (vMonth > month) return 0;
            if (vDay < day) return 1;
            return 0;
        }

        public static int IsFailureSerious(int failureType)
        {
            if (failureType % 2 == 0) return 1;
            return 0;
        }
    }

    public class Device
    {
        public int Id
        {
            get
            {
                return Id;
            }
            set
            {
                Id = value;
            }
        }
        public string Name
        {
            get
            {
                return Name;
            }
            set
            {
                Name = value;
            }
        }
        public Failure Failure
        {
            get
            {
                return Failure;
            }
            set
            {
                Failure = value;
            }
        }
    }

    public class Failure
    {
        private FailureType type;
        private DateTime date;

        public FailureType Type // Св-во на перемнной type (она в get/set + изначально прописана)
        {
            get
            {
                return type; // Failure myFail = new Failure(); Console.WriteLine(myFail.Type);
            }
            set
            {
                type = value;
            }
        }
        public DateTime Date
        {
            get
            {
                return date;
            }
            set
            {
                date = value;
            }
        }
        public static int IsEarlier(DateTime date1, DateTime date2)
        {
            int comparingValue = date1.CompareTo(date2);
            if (comparingValue < 0)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }

        public static int IsSerious(FailureType types)
        {
            if ((int)types % 2 == 0) return 1;
            return 0;
        }
    }

    public enum FailureType
    {
        Unexpected_shutdown = 0,
        Short_non_responding = 1,
        Hardware_failures = 2,
        Connection_problems = 3,
    }

    public class ReportMaker
    {
        public static List<string> FindDevicesFailedBeforeDate(DateTime date, Device[] devices)
        {
            var problematicDevices = new HashSet<int>();
            for (int i = 0; i < devices.Length; i++)
                if (Failure.IsEarlier(devices[i].Failure.Date, date) == 1
                    && Failure.IsSerious(devices[i].Failure.Type) == 1)
                    problematicDevices.Add(devices[i].Id);
            var result = new List<string>();
            foreach (var device in devices)
                if (problematicDevices.Contains(device.Id))
                    result.Add(device.Name);
            return result;
        }

        public static List<string> FindDevicesFailedBeforeDateObsolete(
            int day,
            int month,
            int year,
            int[] failureTypes,
            int[] deviceId,
            object[][] times,
            List<Dictionary<string, object>> devices)
        {
            var problematicDevices = new HashSet<int>();
            for (int i = 0; i < failureTypes.Length; i++)
                if (Common.IsEarlier(times[i], day, month, year) == 1 && Common.IsFailureSerious(failureTypes[i]) == 1)
                    problematicDevices.Add(deviceId[i]);

            var result = new List<string>();
            foreach (var device in devices)
                if (problematicDevices.Contains((int)device["DeviceId"]))
                    result.Add(device["Name"] as string);
            return result;
        }
    }
}
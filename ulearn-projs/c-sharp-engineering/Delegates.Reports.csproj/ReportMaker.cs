using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Delegates.Reports
{
    public class ReportMaker
    {
        readonly Func<string, string> makeCaption;
        readonly Func<string> beginList;
        readonly Func<string, string, string> makeItem;
        readonly Func<string> endList;
        readonly Func<IEnumerable<double>, object> makeStatistic;

        readonly string caption;

        public ReportMaker(
            string captionOld,
            Func<IEnumerable<double>, object> makeStatisticOld,
            Func<string, string> makeCaptionOld,
            Func<string> beginListOld,
            Func<string, string, string> makeItemOld,
            Func<string> endListOld
            )
        {
            caption = captionOld;

            makeStatistic = makeStatisticOld;
            makeCaption = makeCaptionOld;
            makeItem = makeItemOld;
            beginList = beginListOld;
            endList = endListOld;
        }

        public string MakeReport(IEnumerable<Measurement> measurements)
        {
            var data = measurements.ToList();
            var result = new StringBuilder();
            result.Append(makeCaption(caption));
            result.Append(beginList());
            result.Append(makeItem("Temperature", makeStatistic(data.Select(z => z.Temperature)).ToString()));
            result.Append(makeItem("Humidity", makeStatistic(data.Select(z => z.Humidity)).ToString()));
            result.Append(endList());
            return result.ToString();
        }
    }

    public static class ReportMakerHelper
    {
		public static string MakeHTMLCaption(string caption) => $"<h1>{caption}</h1>";

        public static string BeginHTMLList() => "<ul>";

        public static string MakeHTMLItem(string valueType, string entry) => $"<li><b>{valueType}</b>: {entry}";

        public static string EndHTMLList() => "</ul>";

        public static string MakeMarkdownCaption(string caption) => $"## {caption}\n\n";
        
        public static string BeginAndEndMarkdownList() => "";

        public static string MakeMarkdownItem(string valueType, string entry) => $" * **{valueType}**: {entry}\n\n";

        public static object GetMedianStatistics(IEnumerable<double> data)
        {
            var list = data.OrderBy(z => z).ToList();
            if (list.Count % 2 == 0)
                return (list[list.Count / 2] + list[list.Count / 2 - 1]) / 2;

            return list[list.Count / 2];
        }

        public static object GetMeanAndStdStatistics(IEnumerable<double> data)
        {
            var ldata = data.ToList();
            var mean = ldata.Average();
            var std = Math.Sqrt(data.Select(z => Math.Pow(z - mean, 2)).Sum() / (ldata.Count - 1));

            return new MeanAndStd
            {
                Mean = mean,
                Std = std
            };
        }

        public static string MeanAndStdHtmlReport(IEnumerable<Measurement> data) =>
            new ReportMaker(
                "Mean and Std",
				GetMeanAndStdStatistics,
                MakeHTMLCaption,
				BeginHTMLList,
				MakeHTMLItem,
				EndHTMLList).
			MakeReport(data);

        public static string MedianMarkdownReport(IEnumerable<Measurement> data) =>
            new ReportMaker(
                "Median",
				GetMedianStatistics,
                MakeMarkdownCaption,
				BeginAndEndMarkdownList,
				MakeMarkdownItem,
				BeginAndEndMarkdownList).
            MakeReport(data);


        public static string MeanAndStdMarkdownReport(IEnumerable<Measurement> data) =>
            new ReportMaker(
                "Mean and Std",
				GetMeanAndStdStatistics,
				MakeMarkdownCaption,
				BeginAndEndMarkdownList,
				MakeMarkdownItem,
				BeginAndEndMarkdownList).
            MakeReport(data);

        public static string MedianHtmlReport(IEnumerable<Measurement> data) =>
            new ReportMaker(
                "Median",
				GetMedianStatistics,
				MakeHTMLCaption,
				BeginHTMLList,
				MakeHTMLItem,
				EndHTMLList).
            MakeReport(data);
    }
}

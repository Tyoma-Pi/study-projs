using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics.Tables
{
    //public class Table<TRow, TCol, TValue>
    //{
    //    public List<TRow> Rows = new List<TRow>();
    //    public List<TCol> Columns = new List<TCol>();
    //    private TableDictionary<TRow, TableDictionary<TCol, TValue>> tableGrid;

    //    public Table<TRow, TCol, TValue> Open
    //    {
    //        get
    //        {
    //            return this;
    //        }
    //    }

    //    public void AddRow(TRow row)
    //    {
    //        if (!this.RowExists(row))
    //        {
    //            this.Rows.Add(row);
    //        }
    //    }

    //    public void AddColumn(TCol column)
    //    {
    //        if (!this.ColExists(column))
    //        {
    //            this.Columns.Add(column);
    //        }
    //    }

    //    public TValue this[TRow row, TCol col]
    //    {
    //        get
    //        {
    //            return this.tableGrid[row][col];
    //        }
    //        set
    //        {
    //            if (value.GetType() != typeof(TValue))
    //            {
    //                throw new ArgumentException();
    //            }
    //            this.AddRow(row);
    //            this.AddColumn(col);
    //            this.tableGrid[row][col] = value;
    //        }
    //    }

    //    public bool RowExists(TRow row)
    //    {
    //        return Rows.IndexOf(row) > -1 && Rows.Count > 0;
    //    }

    //    public bool ColExists(TCol col)
    //    {
    //        return Columns.IndexOf(col) > -1 && Columns.Count > 0;
    //    }

    //    public bool Exists(TRow row, TCol col)
    //    {
    //        return RowExists(row) && ColExists(col);
    //    }

    //    public TableAccessor<TRow, TCol, TValue> Existed
    //    {
    //        get
    //        {
    //            return new TableAccessor<TRow, TCol, TValue>(this);
    //        }
    //    }
    //}

    //public class TableDictionary<TRow, TCol>
    //{
    //    private Dictionary<TRow, TCol> dictionary = new Dictionary<TRow, TCol>();
    //    public TCol this[TRow row]
    //    {
    //        get
    //        {
    //            if (!dictionary.ContainsKey(row))
    //            {
    //                dictionary.Add(row, Activator.CreateInstance<TCol>());
    //            }
    //            return dictionary[row];
    //        }
    //        set
    //        {
    //            dictionary[row] = value;
    //        }
    //    }
    //}

    //public class TableAccessor<TRow, TCol, TValue>
    //{
    //    private Table<TRow, TCol, TValue> table;

    //    public TValue this[TRow row, TCol col]
    //    {
    //        get
    //        {
    //            if (!table.Exists(row, col))
    //            {
    //                throw new ArgumentException();
    //            }

    //            return table[row, col];
    //        }
    //        set
    //        {
    //            if (!table.Exists(row, col) || value.GetType() != typeof(TValue))
    //            {
    //                throw new ArgumentException();
    //            }

    //            table[row, col] = value;
    //        }
    //    }

    //    public TableAccessor(Table<TRow, TCol, TValue> table)
    //    {
    //        this.table = table;
    //    }
    //}

    public class Table<Row, Column, Value>
    {
        public List<Row> Rows = new List<Row>();
        public List<Column> Columns = new List<Column>();
        public Dictionary<Tuple<Row, Column>, Value> table = new Dictionary<Tuple<Row, Column>, Value>();

        public Existed<Row, Column, Value> Existed { get; }
        public Open<Row, Column, Value> Open { get; }

        public Table()
        {
            Open = new Open<Row, Column, Value>(this);
            Existed = new Existed<Row, Column, Value>(this);
        }

        public void AddRow(Row row)
        {
            if (!Rows.Contains(row))
                Rows.Add(row);
        }

        public void AddColumn(Column col)
        {
            if (!Columns.Contains(col))
                Columns.Add(col);
        }
    }

    public class Existed<Row, Column, Value>
    {
        private readonly Table<Row, Column, Value> Table;

        public Existed(Table<Row, Column, Value> table)
        {
            Table = table;
        }

        public Value this[Row row, Column column]
        {
            set
            {
                Tuple<Row, Column> cell = new Tuple<Row, Column>(row, column);
                if (Table.Rows.Contains(row) & Table.Columns.Contains(column))
                {
                    Table.table[cell] = value;
                }
                else
                    throw new ArgumentException();
            }
            get
            {
                Tuple<Row, Column> cell = new Tuple<Row, Column>(row, column);
                if (Table.Rows.Contains(row) & Table.Columns.Contains(column))
                {
                    if (Table.table.ContainsKey(cell))
                        return Table.table[cell];
                    return default;
                }
                else
                    throw new ArgumentException();
            }
        }
    }

    public class Open<Row, Column, Value>
    {
        private readonly Table<Row, Column, Value> Table;

        public Open(Table<Row, Column, Value> table)
        {
            Table = table;
        }

        public Value this[Row row, Column column]
        {
            set
            {
                Tuple<Row, Column> cell = new Tuple<Row, Column>(row, column);
                if (Table.table.ContainsKey(cell))
                    Table.table[cell] = value;
                else
                {
                    if (!Table.Columns.Contains(column))
                        Table.AddColumn(column);
                    if (!Table.Rows.Contains(row))
                        Table.AddRow(row);
                    Table.table.Add(cell, value);
                }
            }
            get
            {
                Tuple<Row, Column> set = new Tuple<Row, Column>(row, column);
                if (Table.table.ContainsKey(set))
                    return Table.table[set];
                else
                    return default;
            }
        }
    }
}
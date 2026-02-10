The index is essentially the "address" or label for each row in a DataFrame or Series.

**Key Characteristics**
- **Row Identification:** It provides a way to uniquely identify and access specific rows of data.
- **Default State:** If you don't specify one, pandas automatically creates a numeric index starting at 0 (called a RangeIndex).
- **Flexible Types:** An index can be integers, strings (like names), or even dates (essential for time-series data).
- **Data Alignment:** It ensures that when you perform operations between two DataFrames, pandas aligns the data based on these labels rather than just their position.

**How to Use It**
- `df.set_index('column_name')`: Converts an existing column into the row index to make lookups easier.
- `df.loc[label]`: Uses the index labels to select specific rows.
- `df.reset_index()`: Converts the current index back into a regular column and restores the default numeric index.

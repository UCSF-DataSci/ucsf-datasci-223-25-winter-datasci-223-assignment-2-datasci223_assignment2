# Cohort Analysis Hints

## General Approach
1. Understand the data structure from the sample data
2. Plan the analysis steps before coding
3. Test with a small subset of data first
4. Verify the output format matches requirements

## Progressive Hints

### Hint 1: Data Loading and Conversion
- How do you convert CSV to Parquet format?
- What are the advantages of Parquet for this analysis?
- How do you use polars' lazy evaluation?
- What's the difference between `pl.read_csv()` and `pl.scan_csv()`?

### Hint 2: BMI Filtering
- How do you filter out BMI outliers (< 10 or > 60)?
- Where should the filtering happen in the query pipeline?
- Why is early filtering important for performance?
- How do you use polars' filter expressions?

### Hint 3: BMI Binning
- How do you create BMI ranges using `cut()`?
- What are the bin boundaries and labels?
- How do you handle the interval boundaries?
- What does `left_closed=True` mean?

### Hint 4: Aggregation
- How do you group by BMI range?
- What aggregations are needed for each column?
- How do you alias columns to match the expected output?
- How do you ensure the columns are in the correct order?

### Hint 5: Streaming Execution
- How do you execute the query with streaming?
- What are the benefits of streaming for large datasets?
- How do you collect the results?
- How do you handle memory constraints?

## Testing Tips
1. Start with a small CSV file (100 rows)
2. Verify each step of the pipeline separately
3. Check the output format matches exactly
4. Test with edge cases (all values in one bin, empty bins)
5. Monitor memory usage with larger datasets 
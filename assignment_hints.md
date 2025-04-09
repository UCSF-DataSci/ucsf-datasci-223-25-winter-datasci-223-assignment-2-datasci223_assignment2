# Assignment Hints

This document provides hints and guidance for completing the assignment. For detailed hints on each component, refer to the specific hint files:

- [Patient Data Cleaner Hints](patient_data_cleaner_hints.md)
- [Medication Dosage Calculator Hints](med_dosage_hints.md)
- [Cohort Analysis Hints](cohort_analysis_hints.md)

## General Debugging Tips

1. **Start Small**: Begin with a small dataset or test case
2. **Incremental Testing**: Test each function separately
3. **Print Statements**: Add print statements to inspect variables
4. **Debugger**: Use a debugger to step through code
5. **Documentation**: Read the function docstrings carefully

## Part 1: Debugging

### Common Debugging Techniques

1. **Print Statements**: Add print statements to inspect variables
   ```python
   print(f"Variable value: {variable}")
   ```

2. **pdb**: Use Python's debugger
   ```python
   import pdb; pdb.set_trace()
   ```

3. **VS Code Debugger**: Set breakpoints and inspect variables

4. **Logging**: Use Python's logging module
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   logging.debug(f"Variable value: {variable}")
   ```

### Bug Documentation Format

When documenting bugs, use these comment formats:

```python
# BUG: Description of the bug
# FIX: Description of how you fixed it
```

## Part 2: Big Data Analysis

### Polars Basics

1. **Reading Data**:
   ```python
   # Eager evaluation
   df = pl.read_csv("file.csv")
   
   # Lazy evaluation
   lf = pl.scan_csv("file.csv")
   ```

2. **Filtering**:
   ```python
   # Eager
   df_filtered = df.filter(pl.col("column") > value)
   
   # Lazy
   lf_filtered = lf.filter(pl.col("column") > value)
   ```

3. **Grouping and Aggregation**:
   ```python
   # Eager
   df_grouped = df.groupby("column").agg([
       pl.col("value").mean().alias("avg_value"),
       pl.count().alias("count")
   ])
   
   # Lazy
   lf_grouped = lf.groupby("column").agg([
       pl.col("value").mean().alias("avg_value"),
       pl.count().alias("count")
   ])
   ```

4. **Executing Lazy Queries**:
   ```python
   # Without streaming
   df_result = lf.collect()
   
   # With streaming
   df_result = lf.collect(streaming=True)
   ```

### Performance Tips

1. **Early Filtering**: Filter data as early as possible in the pipeline
2. **Column Selection**: Select only needed columns
3. **Streaming**: Use streaming for large datasets
4. **Parquet Format**: Convert CSV to Parquet for better performance

## Submission Checklist

Before submitting, ensure:

1. All tests pass
2. Bug documentation is complete
3. Code is clean and well-commented
4. Output format matches requirements exactly
5. Files are named correctly 
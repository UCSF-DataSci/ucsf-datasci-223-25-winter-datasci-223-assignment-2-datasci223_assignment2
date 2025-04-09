# Assignment Walkthrough Example

This document shows how I would approach the assignment and use a debugger to find and fix issues.

## Part 1: Debugging

### Patient Data Cleaner

1. **Initial Approach**:
   - Run the script with sample data
   - Set a breakpoint at the start of `clean_patient_data()`
   - Examine the input data structure

2. **Using the Debugger**:
   - Step through the function line by line
   - Inspect variables after each operation
   - Watch for unexpected values or type mismatches

3. **Finding Bugs**:
   - Bug 1: Name capitalization issue
     - Set a breakpoint before name processing
     - Inspect the 'name' field
     - Notice the typo in the key ('nage' instead of 'name')
     - Fix: Change 'nage' to 'name'

   - Bug 2: Age conversion issue
     - Set a breakpoint before age conversion
     - Inspect the age value and its type
     - Notice incorrect method name (fill_na vs fillna)
     - Fix: Change fill_na to fillna

   - Bug 3: Duplicate detection issue
     - Set a breakpoint before duplicate detection
     - Inspect the data structure
     - Notice typo in method name (drop_duplcates vs drop_duplicates)
     - Fix: Change drop_duplcates to drop_duplicates

   - Bug 4: Age comparison issue
     - Set a breakpoint at the age comparison
     - Inspect the comparison operation
     - Notice incorrect operator (= vs ==)
     - Fix: Change = to ==

   - Bug 5: Age filtering logic issue
     - Set a breakpoint at the age filtering
     - Inspect the condition and result
     - Notice logic error (keeps patients under 18 instead of filtering them)
     - Fix: Change the condition to filter out patients under 18

4. **Verification**:
   - Run the script with test data
   - Set breakpoints at key points to verify fixes
   - Check the output matches expected format

### Medication Dosage Calculator

1. **Initial Approach**:
   - Run the script with sample data
   - Set a breakpoint at the start of `calculate_dosage()`
   - Examine the input parameters

2. **Using the Debugger**:
   - Step through the function line by line
   - Inspect variables after each calculation
   - Watch for division by zero or type mismatches

3. **Finding Bugs**:
   - Bug 1: Medication name handling
     - Set a breakpoint before medication name processing
     - Inspect the medication name
     - Notice case sensitivity issues
     - Fix: Normalize medication names

   - Bug 2: Dosage factor calculation
     - Set a breakpoint before factor calculation
     - Inspect the factor value
     - Notice incorrect key construction (adding 's')
     - Fix: Remove the 's' suffix

   - Bug 3: Loading dose calculation
     - Set a breakpoint before loading dose calculation
     - Inspect the loading dose condition
     - Notice incorrect condition check
     - Fix: Correct the loading dose condition

   - Bug 4: Warning generation
     - Set a breakpoint before warning generation
     - Inspect the medication name
     - Notice typos in medication names
     - Fix: Correct medication name typos

4. **Verification**:
   - Run the script with test data
   - Set breakpoints at key points to verify fixes
   - Check the output matches expected format

## Part 2: Big Data Analysis

### Cohort Analysis

1. **Initial Approach**:
   - Run the script with a small subset of data
   - Set a breakpoint at the start of `analyze_patient_cohorts()`
   - Examine the data loading process

2. **Using the Debugger**:
   - Step through the function line by line
   - Inspect the data at each transformation
   - Watch for memory usage with larger datasets

3. **Implementation Steps**:
   - Step 1: CSV to Parquet conversion
     - Set a breakpoint after data loading
     - Inspect the DataFrame structure
     - Verify the conversion worked correctly

   - Step 2: BMI filtering
     - Set a breakpoint after filtering
     - Inspect the filtered DataFrame
     - Verify outliers are removed

   - Step 3: BMI binning
     - Set a breakpoint after binning
     - Inspect the binned values
     - Verify bins are created correctly

   - Step 4: Aggregation
     - Set a breakpoint after aggregation
     - Inspect the aggregated DataFrame
     - Verify column names and order

   - Step 5: Streaming execution
     - Set a breakpoint before collection
     - Monitor memory usage
     - Verify results are collected correctly

4. **Verification**:
   - Run the script with test data
   - Set breakpoints at key points to verify each step
   - Check the output matches expected format

## Debugging Tips Used

1. **Breakpoints**:
   - Set at function entry points
   - Set before critical operations
   - Set after data transformations

2. **Variable Inspection**:
   - Check variable types
   - Check variable values
   - Check data structures

3. **Step-by-Step Execution**:
   - Step over function calls
   - Step into functions when needed
   - Step out of functions when done

4. **Conditional Breakpoints**:
   - Set when specific conditions are met
   - Useful for finding edge cases
   - Helpful for large datasets

5. **Watch Expressions**:
   - Monitor specific variables
   - Track complex expressions
   - Evaluate conditions

## Common Debugging Patterns

1. **Data Loading**:
   - Verify file paths
   - Check data structure
   - Validate data types

2. **Data Transformation**:
   - Check input and output
   - Verify transformation logic
   - Handle edge cases

3. **Calculation**:
   - Verify mathematical operations
   - Check for division by zero
   - Handle type conversions

4. **Output Generation**:
   - Verify output format
   - Check column names
   - Validate data types 
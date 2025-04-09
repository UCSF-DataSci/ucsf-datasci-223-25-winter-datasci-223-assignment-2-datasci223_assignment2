# Patient Data Cleaner Hints

## General Approach
1. Start by examining the input data format
2. Identify the cleaning rules from the documentation
3. Test each cleaning rule individually
4. Check for edge cases in the data

## Progressive Hints

### Hint 1: Data Loading
- How is the JSON data being loaded?
- Are there any file path issues?
- Is the data structure as expected?

### Hint 2: Name Capitalization
- How are names being processed?
- Check for multi-word names
- Are special characters handled correctly?
- Is the capitalization consistent?

### Hint 3: Age Conversion
- How are age values being converted from strings to integers?
- Are there any non-numeric age values?
- How are invalid ages being handled?
- Is the age filtering working correctly?

### Hint 4: Duplicate Detection
- How are duplicates being identified?
- What fields are used to determine uniqueness?
- Is the comparison case-sensitive?
- Are all fields being considered?

### Hint 5: Data Validation
- Are all required fields present?
- How are missing fields handled?
- Are field types consistent?
- Is the output format correct?

## Testing Tips
1. Create a small test dataset with known issues
2. Test each cleaning rule in isolation
3. Check edge cases (empty strings, null values, etc.)
4. Verify the output matches the expected format
5. Test with a variety of input data 
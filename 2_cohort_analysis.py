import polars as pl

def analyze_patient_cohorts(input_file: str) -> pl.DataFrame:
    """
    Analyze patient cohorts based on BMI ranges.
    
    Args:
        input_file: Path to the input CSV file
        
    Returns:
        DataFrame containing cohort analysis results with columns:
        - bmi_range: The BMI range (e.g., "Underweight", "Normal", "Overweight", "Obese")
        - avg_glucose: Mean glucose level by BMI range
        - patient_count: Number of patients by BMI range
        - avg_age: Mean age by BMI range
    """
    # TODO: Convert CSV to Parquet for efficient processing
    # Hint: Use pl.read_csv().write_parquet() as shown in lecture
    # Example:
    # pl.read_csv(input_file).write_parquet("patients_large.parquet")
    
    # TODO: Create a lazy query to analyze cohorts
    # Hint: Use pl.scan_parquet() with:
    #     - Early filtering (remove BMI outliers: < 10 or > 60)
    #         pl.col("BMI").filter((pl.col("BMI") >= 10) & (pl.col("BMI") <= 60))
    #     - Select needed columns (BMI, Glucose, Age)
    #         pl.col(["BMI", "Glucose", "Age"])
    #     - Create BMI ranges using pl.col("BMI").cut():
    #         bins = [10, 18.5, 25, 30, 60]  # Note: filtered outliers
    #         labels = ["Underweight", "Normal", "Overweight", "Obese"]
    #         # Example of how to use cut():
    #         pl.col("BMI").cut(
    #             breaks=bins,
    #             labels=labels,
    #             left_closed=True  # intervals are [a, b) except last which is [a, b]
    #         ).alias("bmi_range")
    #     - Group by BMI range and calculate exactly these columns in this order:
    #         .groupby("bmi_range")
    #         .agg([
    #             pl.col("Glucose").mean().alias("avg_glucose"),
    #             pl.count().alias("patient_count"),
    #             pl.col("Age").mean().alias("avg_age")
    #         ])
    
    # TODO: Execute the query with streaming
    # Hint: Use collect(streaming=True)
    
    return cohort_results

def main():
    # Input file
    input_file = "patients_large.csv"
    
    # Run analysis
    results = analyze_patient_cohorts(input_file)
    
    # Print summary statistics
    print("\nCohort Analysis Summary:")
    print(results)

if __name__ == "__main__":
    main() 
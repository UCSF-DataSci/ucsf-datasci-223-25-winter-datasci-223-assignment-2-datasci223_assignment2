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
    # Convert CSV to Parquet for efficient processing
    pl.read_csv(input_file).write_parquet("patients_large.parquet", compression="zstd")

    # Analyze cohorts using Polars' lazy API and streaming execution
    cohort_results = (
        pl.scan_parquet("patients_large.parquet")
        .filter((pl.col("BMI") >= 10) & (pl.col("BMI") <= 60))
        .with_columns([
            pl.col("BMI").cut(
                breaks=[10, 18.5, 25, 30, 60],
                labels=["Underweight", "Normal", "Overweight", "Obese"],
                left_closed=True
            ).alias("bmi_range")
        ])
        .groupby("bmi_range")
        .agg([
            pl.col("Glucose").mean().alias("avg_glucose"),
            pl.count().alias("patient_count"),
            pl.col("Age").mean().alias("avg_age")
        ])
        .sort("bmi_range")
        .collect(streaming=True)
    )

    return cohort_results

def main():
    input_file = "patients_large.csv"
    results = analyze_patient_cohorts(input_file)

    print("\nCohort Analysis Summary:")
    print(results)

if __name__ == "__main__":
    main()

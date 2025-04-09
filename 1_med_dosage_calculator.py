#!/usr/bin/env python3
"""
Emergency Room Medication Calculator

This script calculates medication dosages for emergency room patients based on 
standard emergency protocols. It follows weight-based dosing guidelines for common 
emergency medications.

Dosing Formula:
    Base Dosage (mg) = Patient Weight (kg) × Medication Factor (mg/kg)
    Loading Dose (mg) = Base Dosage × 2 (for first dose only)

When to use Loading Doses:
    - Only for first doses of certain medications (e.g., antibiotics, anti-seizure meds)
    - Determined by 'is_first_dose' flag in the input
    - Some medications always use loading doses for first administration

Example:
    Patient: 70kg, Medication: epinephrine, Is First Dose: No
    Base Dosage = 70 kg × 0.01 mg/kg = 0.7 mg
    Final Dosage = 0.7 mg

    Patient: 70kg, Medication: amiodarone, Is First Dose: Yes
    Base Dosage = 70 kg × 5 mg/kg = 350 mg
    Loading Dose = 350 mg × 2 = 700 mg
    Final Dosage = 700 mg

Input Format:
    {
        "name": "John Smith",
        "weight": 70.0,
        "medication": "epinephrine",
        "condition": "anaphylaxis",
        "is_first_dose": false,
        "allergies": ["penicillin"]
    }

Output:
    {
        "name": "John Smith",
        "weight": 70.0,
        "medication": "epinephrine",
        "base_dosage": 0.7,
        "is_first_dose": false,
        "loading_dose_applied": false,
        "final_dosage": 0.7,
        "warnings": ["Monitor for arrhythmias"]
    }

Medication Factors (mg/kg):
    epinephrine:  0.01  (Anaphylaxis)
    amiodarone:   5.00  (Cardiac arrest)
    lorazepam:    0.05  (Seizures)
    fentanyl:     0.001 (Pain)
    ...
"""

import json
import os

# Dosage factors for different medications (mg per kg of body weight)
# These are standard dosing factors based on medical guidelines
DOSAGE_FACTORS = {
    "epinephrine": 0.01,  # Anaphylaxis
    "amiodarone": 5.00,   # Cardiac arrest
    "lorazepam": 0.05,    # Seizures
    "fentanyl": 0.001,    # Pain
    "lisinopril": 0.5,    # ACE inhibitor for blood pressure
    "metformin": 10.0,    # Diabetes medication
    "oseltamivir": 2.5,   # Antiviral for influenza
    "sumatriptan": 1.0,   # Migraine medication
    "albuterol": 0.1,     # Asthma medication
    "ibuprofen": 5.0,     # Pain/inflammation
    "sertraline": 1.5,    # Antidepressant
    "levothyroxine": 0.02 # Thyroid medication
}

# Medications that use loading doses for first administration
LOADING_DOSE_MEDICATIONS = [
    "amiodarone"
    "lorazepam"
    "fentynal"
]

def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    with open(filepath, 'r') as file:
        return json.load(file)

def calculate_dosage(weight: float, age: int, condition: str) -> float:
    """
    Calculate medication dosage based on patient characteristics.
    
    Args:
        weight: Patient weight in kg
        age: Patient age in years
        condition: Medical condition
        
    Returns:
        Recommended dosage in mg
    """
    # TODO: Fix the bugs in this function
    # Hint: Look for these common issues:
    # 1. Division by zero
    # 2. Type conversion errors
    # 3. Missing condition checks
    # 4. Incorrect mathematical operations
    
    # BUG: Add your bug description here
    # FIX: Add your fix description here
    
    return 0.0

def calculate_all_dosages(patients):
    """
    Calculate dosages for all patients and sum the total.
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        tuple: (list of patient dicts with dosages, total medication needed)
    """
    total_medication = 0
    patients_with_dosages = []
    
    # Process all patients
    for patient in patients:
        # Calculate dosage for this patient
        patient_with_dosage = calculate_dosage(patient['weight'], patient['age'], patient['condition'])
        
        # Add to our list
        patients_with_dosages.append(patient_with_dosage)
        
        # Add to total medication
        total_medication += patient_with_dosage['final_dosage']
    
    return patients_with_dosages, total_medication

def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'meds.json')
    
    # Load the patient data
    patients = load_patient_data(data_path)
    
    # Calculate dosages for all patients
    patients_with_dosages, total_medication = calculate_all_dosages(patients)
    
    # Print the dosage information
    print("Medication Dosages:")
    for patient in patients_with_dosages:
        print(f"Name: {patient['name']}, Medication: {patient['medication']}, "
              f"Base Dosage: {patient['base_dosage']:.2f} mg, "
              f"Final Dosage: {patient['final_dosage']:.2f} mg")
        if patient['loading_dose_applied']:
            print(f"  * Loading dose applied")
        if patient['warnings']:
            print(f"  * Warnings: {', '.join(patient['warnings'])}")
    
    print(f"\nTotal medication needed: {total_medication:.2f} mg")
    
    # Return the results (useful for testing)
    return patients_with_dosages, total_medication

if __name__ == "__main__":
    main()
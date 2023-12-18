# Read input

period = int(input())
treated_patients = 0
untreated_patients = 0
total_treated_patients = 0
total_untreated_patients = 0
doctors = 7
# Logic
for day in range(1, period + 1):
    patients = int(input())
    if day % 3 == 0:
        if total_untreated_patients > total_treated_patients:
            doctors += 1
    if patients >= doctors:
        treated_patients = doctors
        untreated_patients = patients - doctors
    elif patients < doctors:
        treated_patients = patients
        untreated_patients = 0

    total_treated_patients += treated_patients
    total_untreated_patients += untreated_patients


# Print output
print(f'Treated patients: {total_treated_patients}.')
print(f'Untreated patients: {total_untreated_patients}.')

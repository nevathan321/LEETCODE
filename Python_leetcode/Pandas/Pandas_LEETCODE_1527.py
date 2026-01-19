import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    contains = patients['conditions'].str.contains(r"(^|\s)DIAB1", na = False)
    return patients.loc[contains, ['patient_id', 'patient_name', 'conditions']]

    
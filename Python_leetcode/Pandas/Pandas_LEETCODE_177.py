import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(salaries) < N or 0 >= N:
        nth = None
    else: 
        nth = salaries.iloc[N - 1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth]})

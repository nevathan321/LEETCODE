import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    ans = employees.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()
    ans1 = ans.rename(columns={'event_day': 'day'})
    return ans1[['day', 'emp_id', 'total_time']]

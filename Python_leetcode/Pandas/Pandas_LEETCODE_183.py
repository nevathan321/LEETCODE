import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filter_id = orders['customerId']
    Overall_Filter = customers[~(customers['id'].isin(filter_id))]
    return Overall_Filter[['name']].rename(columns={'name': 'Customers'})


    
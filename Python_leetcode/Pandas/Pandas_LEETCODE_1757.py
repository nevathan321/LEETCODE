import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    Products_Filter = products[
        (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    ]
    return Products_Filter[['product_id']]

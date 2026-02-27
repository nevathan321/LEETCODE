import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    union1 = products[['product_id']]
    union1['store'] = "store1"
    union1["price"] = products["store1"]

    union2 = products[['product_id']]
    union2['store'] = "store2"
    union2["price"] = products["store2"]


    union3 = products[['product_id']]
    union3['store'] = "store3"
    union3["price"] = products["store3"]

    final_union = pd.concat([union1, union2, union3], ignore_index=True).dropna(subset=['price'])

    return final_union 


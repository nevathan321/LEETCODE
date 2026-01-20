import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
        # 1) keep smallest id per email
    keep = person.groupby("email")["id"].transform("min") == person["id"]

    # 2) drop the others IN PLACE by filtering then overwriting the same df
    person.drop(person.index[~keep], inplace=True)
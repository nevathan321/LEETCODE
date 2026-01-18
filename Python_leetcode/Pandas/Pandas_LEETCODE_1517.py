import pandas as pd

#Option 1
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    #every letter to the @ should have the rules constricted to it 
    has_at = users["mail"].str.contains("@", na=False)
    parts = users['mail'].str.split("@", n = 1, expand = True)
    prefix = parts[0]
    domain = parts[1]
    valid_prefix = prefix.str.match(r"^[A-Za-z][A-Za-z0-9_.-]*$", na = False)
    valid_domain = domain.eq("leetcode.com")
    valid = valid_prefix & valid_domain
    return users[valid & has_at]

# Option 2
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    mask = users['mail'].str.match(pattern, na=False)
    return users[mask]
     


    
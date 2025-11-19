# 1. Import the library
from edgar import *

# 2. Tell the SEC who you are (required by SEC regulations)
set_identity("purblindstocks@gmail.com")

# 3. Find a company
company = Company("HTLD")  # Heartland Express

# 4. Get company filings
filings = company.get_filings() 

# 5. Filter by form 
# insider_filings = filings.filter(form="4")  # Insider transactions

# 6. Get the latest filing
# insider_filing = insider_filings[0]

# 7. Convert to a data object
# ownership = insider_filing.obj()
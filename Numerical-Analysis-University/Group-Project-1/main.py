import numpy as np
accounts = 100 + (100000-100) * np.random.rand(50000, 1)
accounts = np.floor(100*accounts)/100
# The code above creates 50 thousand accounts
# each acct has a balance from $100 <= X <= 100000


# The following code increases the balance by (3/365)% a day
# and changes the accounts to reflect this growth
daily_interest = (5 / (365 * 100))
daily_growth = 1 + daily_interest
new_accounts = accounts * daily_growth

# The code below truncates the accounts and adds the
# truncated amount to an illegal account

truncated_accounts = np.floor(new_accounts * 100) / 100
illegal_account = np.sum(new_accounts - truncated_accounts)
accounts = truncated_accounts

# These lines redefine vars before while loop
illegal_account = 0.0
days = 0


# This is the while loop to put at least 1,000,000 in illegal
while illegal_account < 1000000:
    new_accounts = accounts * daily_growth
    truncated_accounts = np.floor(new_accounts * 100) / 100
    illegal_account += np.sum(new_accounts - truncated_accounts)
    accounts
    days += 1
print(f"days needed to hit 1 mil is {days}")

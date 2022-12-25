import pyetrade


CONSUMER_KEY = "425576b33e50260f22e51b54db985122"
CONSUMER_SECRET = "3fa71ec58dece09bcd2850719ad5b55d5a19156bb3c55d2be3b2ca88d035229f"

oauth = pyetrade.ETradeOAuth(CONSUMER_KEY, CONSUMER_SECRET)
print(oauth.get_request_token())  # Use the printed URL

verifier_code = input("Enter verification code: ")
tokens = oauth.get_access_token(verifier_code)

print(tokens)

accounts = pyetrade.accounts.ETradeAccounts(client_key=CONSUMER_KEY, client_secret=CONSUMER_SECRET, resource_owner_key= tokens['oauth_token'], resource_owner_secret= tokens['oauth_token_secret'])

print(accounts.list_accounts())
account_id = input("Enter account id: ")
print(accounts.get_account_balance(account_id))
print("End of file")
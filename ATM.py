withdraw,balance=map(float,input().split())
if withdraw % 5 == 0 and withdraw + 0.5 <= balance :
    balance = balance - withdraw - 0.5
else:
    balance
print(balance)

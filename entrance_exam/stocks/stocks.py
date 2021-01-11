file = open("new.csv", "r")

can_buy = True

stocks = 0
portfolio_price = 0
finances = int(input("finances: "))
limit = int(input("transactions limit: "))
period = 17000 # minutes

increase = 0
decrease = 0
previous_price = 0

statistics = []

i = 0
transactions = 0
for line in file:
  if (transactions == limit):
    break
  if (i == 0):
    i += 1
    continue
  elif (i == 1):
    previous_price = int(float(line.split(',')[3]))
    i += 1
    continue

  i += 1
  tokens = [s for s in line.split(',')]
  date = tokens[1]
  date = date[6:] + '.' + date[4:6] + '.' + date[:4]
  time = tokens[2]
  time = time[:2] + ':' + time[2:4]
  price = int(float(tokens[3]))

  portfolio_price = stocks * price
  if(i % 60 == 0):
    print("[{0} {1}] portfolio: {2} actives: {3}".format(
        date, time, portfolio_price, portfolio_price + finances))

  if (i % period > 0):
    continue

  

  if (previous_price < price):
    increase += 1
    decrease = 0
  elif (previous_price > price):
    increase = 0
    decrease += 1
  
  if (increase == 3 and stocks > 0):
    can_buy = True
    increase = 0
    transactions += 1
    finances += portfolio_price
    stocks = 0
    portfolio_price = 0
    statistics.append(finances)
    print("####################################")
    print('['+date, time + "] - SALE -", transactions)
    print("stocks:", stocks)
    print("portfolio:", portfolio_price)
    print("finances:", finances)
    print("actives:", finances + portfolio_price)
    print("####################################")
    
  
  if (decrease == 3 and finances//2 > price and can_buy):
    can_buy = False
    decrease = 0
    transactions += 1
    stocks = (finances//2)//price
    portfolio_price = stocks * price
    finances -= portfolio_price
    statistics.append(finances + portfolio_price)
    print("####################################")
    print('['+date, time + "] - PURCHASE -", transactions)
    print("stocks:", stocks)
    print("portfolio:", portfolio_price)
    print("finances:", finances)
    print("actives:", finances + portfolio_price)
    print("####################################")
    
  previous_price = price

print("actives:", finances + portfolio_price)

file.close()
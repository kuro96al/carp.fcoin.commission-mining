from fcoin import Fcoin

fcoin = Fcoin()
fcoin.auth('6b709e792d484932a06298e0f408692b', '8fc3e8dc802548788f2c55287c16d021')

balance = fcoin.get_balance()

FT_USDT_QTY = 10
FT_ETH_QTY = 10

ETH_USDT_QTY = 10
'''

balance_ft = 0
balance_usdt = 0
balance_eth = 0

for data in balance["data"]:
    if(data["currency"] == "usdt"):
        balance_usdt = float(data["available"])
    if(data["currency"] == "ft"):
        balance_ft = float(data["available"])
    if(data["currency"] == "eth"):
        balance_eth = float(data["available"])


print("balance-FT  :"+str(balance_ft))
print("balance-USDT:"+str(balance_usdt))
print("balance-ETH  :"+str(balance_eth))
'''
depth_ftusdt = fcoin.get_market_depth("L20", "ftusdt")
depth_fteth = fcoin.get_market_depth("L20", "fteth")
depth_ethusdt = fcoin.get_market_depth("L20", "ethusdt")

#float('%.4g' % (balance_ft))
max = 0
min = 10000
index_max = -1
index_min = -1

####### buy algo #######
if(depth_ftusdt["data"]["asks"][0] < min):
    min = depth_ftusdt["data"]["asks"][0]
    index_min = 1 
if(depth_fteth["data"]["asks"][0]*depth_ethusdt["data"]["asks"][0] < min):
    min = depth_fteth["data"]["asks"][0]*depth_ethusdt["data"]["asks"][0]
    index_min = 2 

####### sell algo #######
if(depth_ftusdt["data"]["bids"][0] > max):
    max = depth_ftusdt["data"]["bids"][0]
    index_max = 1 
if(depth_fteth["data"]["bids"][0]*depth_ethusdt["data"]["bids"][0] > max):
    max = depth_fteth["data"]["bids"][0]*depth_ethusdt["data"]["bids"][0]
    index_max = 2 


####### order algo(buy) #######
if(max>min):
    if (index_min == 1):
        fcoin.market_buy("ftusdt",FT_USDT_QTY)

    elif (index_min == 2):
        fcoin.market_buy("ethusdt",ETH_USDT_QTY)

print("直接買う(index:1):price"+str(depth_ftusdt["data"]["asks"][0]))
print("eth経由で買う(index:2):price"+str(depth_fteth["data"]["asks"][0]*depth_ethusdt["data"]["asks"][0]))

print("直接売る(index:1):price"+str(depth_ftusdt["data"]["bids"][0]))
print("eth経由で売る(index:2)price:"+str(depth_fteth["data"]["bids"][0]*depth_ethusdt["data"]["bids"][0]))


print("buy index"+str(index_min))
print("sell index"+str(index_max))
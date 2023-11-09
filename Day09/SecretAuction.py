bidList = {}
highestBid = 0
continueOrNot = 'yes'

while(continueOrNot == 'yes'):
    name = input("What's your name? ")
    bid = float(input("Enter your bid: $"))
    continueOrNot = input("Type 'yes' to continue; 'no' t0 terminate: ").lower()

    bidList[name] = bid

for key in bidList:
    if(bidList[key] > highestBid):
        highestBid = bidList[key]

def highestBidder(bidList):
    for key in bidList:
        if(bidList[key] == highestBid):
            return key
        
print(f"The winner of the auction is: {highestBidder(bidList)}")
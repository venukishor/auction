import auctions.models

all = auctions.models.auctionlist.objects.all()

def info():
    for item in all:
        print(item.title)
        print(item.desc)
        print(item.starting_bid)
        print(item.image_url)
        print(item.category + "\n")

        
info()
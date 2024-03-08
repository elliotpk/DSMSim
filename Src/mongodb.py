from Database import API_Handling
import pymongo
def mongo(buyerID, score, eco, fairness, buyerCity, buyerCountry, buyerClosest, sellers):
    list =[]
    try:
        for i in range (0,len(sellers)):
            try:
                currentSeller = sellers[i]
                sellerData = currentSeller[1]
                listedSeller = (str(sellerData)).split(" ")
                sellerID = listedSeller[0]
                sellerLocation = listedSeller[1]
                sellerLocList = (str(sellerLocation)).split(",")
                stad = sellerLocList[0]
                land = sellerLocList[1]
                sellerClosest =API_Handling.closestWarehouse(stad, land)
                list.append([sellerID, stad, land, sellerClosest])
            except:
                print('Bidder has not won a bid on current seller')
    except:
        print("no sellers found for buyer")
        
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]
        customer_data = {
            "BuyerID": buyerID,
            "Score": score,
            "Eco": eco,
            "Fairness": fairness,
            "LocationBuyerCity": buyerCity,
            "LocationBuyerCountry": buyerCountry,
            "LocationBuyerWarehouse": buyerClosest,
            
        }
        for d in range(0, len(list)):
            customer_data["sellerID"+str(d)] = list[d][0]
            customer_data["sellerCity"+str(d)] = list[d][1]
            customer_data["sellerCountry"+str(d)] = list[d][2]
            customer_data["sellerClosest"+str(d)] = list[d][3]
        
        x = mycol.insert_one(customer_data)
        print("Document inserted with ID:", x.inserted_id)

    except Exception as e:
        print("An error occurred:", e)
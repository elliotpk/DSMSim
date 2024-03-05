import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

customer_data = {
    "SellerID": 0,
    "BuyerID": 0,
    "Score": 0.5,
    "Eco": 0.5,
    "Fairness": 0.5,
    "LocationBuyerCity": "City",
    "LocationBuyerCountry": "Country",
    "LocationBuyerWarehouse": "ClosestWarehouse",
    "LocationSellerCity": "City",
    "LocationSellerCountry": "Country",
    "LocationSellerWarehouse": "ClosestWarehouse",

}


x = mycol.insert_one(customer_data)
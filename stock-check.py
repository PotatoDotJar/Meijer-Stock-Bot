import sys
import requests

def getProductName(data):
    return data["name"]

def isInStock(data):
    if(data["stock"]["stockLevelStatus"] == "inStock"):
        return True
    else:
        return False

STORE_CODE = 43
PRODUCT_UPC_CODE = 84223440349

if(__name__ == "__main__"):
    arglen = len(sys.argv)
    if(arglen < 3):
        print("Invalid arguments\npython stock-check.py <store ID> <product UPC code>")
        exit(1)
    else:
        STORE_CODE = int(sys.argv[1])
        PRODUCT_UPC_CODE = int(sys.argv[2])

cookies = { 'meijer-store': str(STORE_CODE) }

# API will not respond without User-Agent header lol
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

url = "https://www.meijer.com/bin/meijer/product?upc=" + str(PRODUCT_UPC_CODE)

res = requests.get(url, cookies=cookies, headers=headers, timeout=5)

if(res.status_code == 200):
    data = res.json()

    product_name = getProductName(data)
    in_stock = isInStock(data)
    
    print("Name: {product_name}\nIn Stock: {in_stock}"
        .format(product_name=product_name, in_stock=in_stock))
else:
    print("Shit hit the fan " + str(res.status_code))
import requests
import ast
def callSIAAPI():
    url = "https://apigw.singaporeair.com/appchallenge/api/inventory/item"

    payload = "{\"item\":\"JCL large round plate\",\"station\":\"CPH\"}"
    headers = {
        'content-type': "application/json",
        'apikey': "aghk73f4x5haxeby7z24d2rc",
        'cache-control': "no-cache",
        'postman-token': "dfeb8ca7-91ce-0bdb-6f02-0dea12cb3c8a"
        }

    response1 = requests.request("POST", url, data=payload, headers=headers)
    dictForWarehouseInventory=ast.literal_eval(response1.text)
    quantityInWarehouse=int(dictForWarehouseInventory['response']['availableStock'])



    url = "https://apigw.singaporeair.com/appchallenge/api/equipment/loadplan"

    payload = "{\"aircraftType\":\"773\",\"route\":\"SIN/CPH\"}"
    headers = {
        'content-type': "application/json",
        'apikey': "aghk73f4x5haxeby7z24d2rc",
        'cache-control': "no-cache",
       'postman-token': "2f7e3e92-5a31-533e-0d81-c60e3f5e31cf"
        }

    response2 = requests.request("POST", url, data=payload, headers=headers)
    dictForFlightInventory=ast.literal_eval(response2.text)
    quantityInFlight=int(dictForFlightInventory['response']['loadingItemList'][0]['quantity'])
    return quantityInWarehouse,quantityInFlight
    

if __name__ == '__main__':
    AccordionApp().run()

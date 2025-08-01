import requests
from pprint import pprint


def valyuta_to_see(text: str): 
    val1,val2,val3 = text.split("-") 
    
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    responce = requests.get(url=url)

    if responce.status_code == 200:
        values = responce.json()
      
        for value in values:
            if str(value['Ccy']).lower() == val1.lower():
                qiymat1 = float(value['Rate'])
           
            if str(value['Ccy']).lower() == val2.lower():
                qiymat2 = float(value['Rate'])
    
    result = qiymat1 * float(val3) / qiymat2
    
    return f"{val3} {val1} =  {result:.2f} {val2} ga teng"
        

                
        
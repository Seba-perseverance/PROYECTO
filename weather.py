import requests

class clima:
    def __init__(self,city):
        self.city=city
        
    def mostrar_clima(self):    
        
        url = f"https://es.wttr.in/'{self.city}'?format=j1"

        response = requests.get(url)
        weather_dic = response.json()
        temp_c = weather_dic["current_condition"][0]["temp_C"]
        desc_temp = weather_dic["current_condition"][0]["lang_es"]
        desc_temp=desc_temp[0]["value"]
        print(f"La temperatura actual de {self.city} es {temp_c}°C. {desc_temp}. ")

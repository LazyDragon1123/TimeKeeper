import json

import requests

from .cfgs import api

suffix = '\033['
tail = '\033[0m'

class Collector:

    def __init__(self):
        pass

    def __call__(self):
        self.show()

    def collect(self):
        pass

    def show(self):
        pass


class Weather(Collector):
    def __init__(self):
        self.url = api.wurl
        self.params = {"q":"Boston","appid":api.key}
        
    def collect(self):
        return requests.get(self.url,params=self.params).json()
    
    def show(self):
        data = self.prepare_data()
        print(' ** Weather ** ')
        print('')
        print('{}{}m{}{}'.format(suffix,str(96), str(data['Low']), tail), '{}{}m{}{}'.format(suffix,str(99), str(data['Now']), tail), '{}{}m{}{}'.format(suffix,str(91), str(data['High']), tail), '{}{}m{}{}'.format(suffix,str(99), str(data['Rain ?']), tail))
        print('')
        
        
    def prepare_data(self):
        jsontexts = self.collect()
        dic = {'t':[],
               'tmin': [],
               'tmax': [],
               'weat': [],
               }
        for i in range(0,4):
            extracted = self.extract(jsontexts['list'][i])
            dic['t'].append(extracted[0])
            dic['tmin'].append(extracted[1])
            dic['tmax'].append(extracted[2])
            dic['weat'].append(extracted[3])

        return {'Now': dic['t'][0], 'Low': min(dic['tmin']), 'High': max(dic['tmax']), 'Rain ?': self.israin(dic['weat'])}

    @staticmethod
    def israin(weat):
        if ("Rain" in weat) or ("Rainy" in weat) or ("Rains" in weat):
            return "Rain"
        else:
            return ""
    
    def extract(self, jsontext):
        t = self.convert_temp(jsontext["main"]["temp"])
        tmin = self.convert_temp(jsontext["main"]["temp_min"])
        tmax = self.convert_temp(jsontext["main"]["temp_max"])
        weather = jsontext["weather"][0]["main"]
        return t, tmin, tmax, weather

    @staticmethod
    def convert_temp(temp):
        return round(temp - 273.15)


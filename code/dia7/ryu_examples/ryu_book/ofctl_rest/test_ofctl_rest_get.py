import argparse
import json
import requests


class NetworkElements():
    def __init__(self, url = "http://localhost:8080" ):

        self.url = url
        self.switches = self.obtenerSwitches()


    def obtenerSwitches(self):
        resp = requests.get(self.url + '/stats/switches')
        '''
        if resp.status_codes['o/'] == 0:
            print '200 - OK'
        else:
            print 'Oh y ahora quien poda ayudarme'
        '''
        # print resp.json()
        return resp.json()   # Retorna una lista

    def obtenerConfiguracion(self, lSw):
        for dpid in lSw:
            resp = requests.get(self.url + '/stats/desc/' + str(dpid))
            resp_dic = resp.json()
            print(type(resp.json().values()),len(resp.json().values())) # Como barrer un json???
            for caracteristica in resp.json().values():
                print(str(caracteristica))


if __name__ == "__main__":
    net_test = NetworkElements()
    net_test.obtenerConfiguracion([1])


'''       
        r.text
        r.status_code == requests.codes.ok
        Todo
        bien

        r.status_code
        requests.codes['o/'] == 0

        print
        r.json


URI = {'get_sw':'/stats/switches',
       'desc'}

Get all switches
/stats/switches


Get the desc stats

/stats/desc/<dpid>

Get all flows stats
/stats/flow/<dpid>

IDEAS:
https://github.com/cgiraldo/mininetRest/blob/master/mininet_rest.py
https://realpython.com/api-integration-in-python/


'''
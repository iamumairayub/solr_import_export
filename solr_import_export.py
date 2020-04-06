# -*- coding: utf-8 -*-
import json
import requests

start = 0
inc = 10000

while 1:
    q = 'https://www.solr.com/solr/from_solr/select?q=*:*&wt=json&start=%s&rows=%s'%(start, inc)
    print(q)
    test = requests.get(q, auth=('userName', 'passWord'))
    test = json.loads(test.text)
    
    if len(test['response']['docs']):
        for a in test['response']['docs']:
            del a['_version_']

        response = requests.post('https://www.solr.com/solr/to_solr/update?commit=true', 
                                 headers={'Content-Type':'application/json'},
                                 auth=('userName', 'Password'),
                                 data=json.dumps(test['response']['docs']))
        print(response.text)
        
        start = start + inc
    else:
        print('all done')
        break

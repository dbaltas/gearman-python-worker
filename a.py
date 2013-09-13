import simplejson
js = '{"sleepFor":1,"name":"Dimitris"}'

data = simplejson.loads(js)
print data['name']

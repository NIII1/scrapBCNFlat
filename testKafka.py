import sys
import datetime
from buildJson import buildjson
from mesScrap import Producer, Consumer

bjson = buildjson()
i = bjson.txt('hola', 'que', 'tal?')

prod = Producer()
cons = Consumer()



#prod.SendMsg('test04', 'hola')
cons.Read('test04')

print ('ole manole!!')

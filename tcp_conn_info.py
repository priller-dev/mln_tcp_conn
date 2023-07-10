import psutil
import os

initial = frozenset(psutil.net_connections(kind='tcp'))

msg = 'show'
while msg == 'show' or not msg:
    msg = input('->')
    if not msg:
        os.system('clear')
    current = frozenset(psutil.net_connections(kind='tcp'))
    print(current.difference(initial))

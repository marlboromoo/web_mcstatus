#!/usr/bin/env python

from json import JSONEncoder
from mcstatus.minecraft_query import MinecraftQuery
from bottle import get, run, default_app

@get('/')
def index():
    """docstring for index"""
    return JSONEncoder().encode({'methods' : ['status', 'rules']})

@get('')
def status():
    """show status"""
    query = MinecraftQuery("localhost", 25565)
    return JSONEncoder().encode(query.get_status())

@get('/rules')
def rules():
    """show full status"""
    query = MinecraftQuery("localhost", 25565)
    return JSONEncoder().encode(query.get_rules())

if __name__ == '__main__':
    run(host='127.0.1.1', port=80, debug=True, reloader=True)
else:
    application = default_app()

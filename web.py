#!/usr/bin/env python

from json import JSONEncoder
from mcstatus.minecraft_query import MinecraftQuery
from bottle import get, request, response, run, default_app
import js

MC_HOST="localhost"
MC_PORT=25565
QUERY_TYPE='rules'
BIND_HOST='127.0.1.1'
BIND_PORT=80
CONTAINER='web_mcstatus-container'


@get('/')
def index():
    """docstring for index"""
    return JSONEncoder().encode({'methods' : ['status', 'rules']})

def mc_query(mqfun):
    """Wrapper for MinecraftQuery - return json/jsonp data"""
    #. create connection
    q = request.query
    host = q.get('host') if 'host' in q.keys() else MC_HOST
    port = q.get('port') if 'port' in q.keys() else MC_PORT
    try:
        query = MinecraftQuery(host, int(port))
    except Exception:
        query = MinecraftQuery(host, MC_PORT)
    #. get infos
    fun = getattr(query, mqfun)
    data = JSONEncoder().encode(fun())
    #. return results
    if request.query.get('callback'):
        response.headers['Content-Type'] = 'text/javascript'
        return "%s ( %s )" % (request.query.get('callback'), data)
    else:
        response.headers['Content-Type'] = 'application/json'
        return data

@get('/status')
def return_status():
    """show status"""
    return mc_query('get_status')

@get('/rules')
def return_rules():
    """show full status"""
    return mc_query('get_rules')

@get('/web_mcstatus.js')
def return_js():
    """dynamic create java script file for widget use"""
    q = request.query
    scheme = request.urlparts.scheme
    netloc = request.urlparts.netloc
    host = q.get('host') if 'host' in q.keys() else MC_HOST
    port = q.get('port') if 'port' in q.keys() else MC_PORT
    type_ = q.get('type') if 'type' in q.keys() else QUERY_TYPE
    cname = "%s-%s" % (CONTAINER, q.get('cname')) \
            if 'cname' in q.keys() else CONTAINER
    response.headers['Content-Type'] = 'text/javascript'
    return js.make_js(scheme, netloc, host, port, cname, type_)

@get('/favicon.ico')
def return_favicon():
    """empty favicon.ico"""
    return ""

if __name__ == '__main__':
    run(host=BIND_HOST, port=BIND_PORT, debug=True, reloader=True)
else:
    application = default_app()

#!/usr/bin/env python

import base64
import os
import slimit

CACHE_DIR='/tmp/web_mcstatus_js'

TEMPLATE= """
/****** reference:  http://alexmarandon.com/articles/web_widget_jquery/ ******/

    (function() {

    // Localize jQuery variable
    var jQuery;

    /******** Load jQuery if not present *********/
    if (window.jQuery === undefined || window.jQuery.fn.jquery !== '1.9.1') {
        var script_tag = document.createElement('script');
        script_tag.setAttribute("type","text/javascript");
        script_tag.setAttribute("src",
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js");
        if (script_tag.readyState) {
          script_tag.onreadystatechange = function () { // For old versions of IE
              if (this.readyState == 'complete' || this.readyState == 'loaded') {
                  scriptLoadHandler();
              }
          };
        } else {
          script_tag.onload = scriptLoadHandler;
        }
        // Try to find the head, otherwise default to the documentElement
        (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);
    } else {
        // The jQuery version on the window is the one we want to use
        jQuery = window.jQuery;
        main();
    }

    /******** Called once jQuery has loaded ******/
    function scriptLoadHandler() {
        // Restore $ and window.jQuery to their previous values and store the
        // new jQuery in our local jQuery variable
        jQuery = window.jQuery.noConflict(true);
        // Call our main function
        main(); 
    }

    /******** Our main function ********/
    function main() { 
        jQuery(document).ready(function($) { 
            /******* Load CSS
            var css_link = $("<link>", { 
                rel: "stylesheet", 
                type: "text/css", 
                href: "style.css" 
            });
            css_link.appendTo('head');          
            *******/

            /******* Load HTML *******/
            var jsonp_url = "$SCHEMA://$NETLOC/rules?host=$HOST&port=$PORT&callback=?";
            $.getJSON(jsonp_url, function(data) {
                $('#$CNAME').empty();
                $('#$CNAME').html(
                    "Edition: " + data.game_id + "<br/>" +
                    "Players: " + data.numplayers + "/" + data.maxplayers + "<br/>" +
                    "Gametype: " + data.gametype + "<br/>" +
                    "Version: " + data.version + "<br/>" +
                    "Plugins: " + data.plugins + "<br/>"
                    );
            });
        });
    }

    })(); // We call our anonymous function immediately
"""

def __replace(template, old, new):
    """docstring for replace"""
    return template.replace(old, new)

def hash_name(host, port):
    """docstring for hash_name"""
    return base64.urlsafe_b64encode("%s:%s" % (host, port))

def cache_path(host, port):
    """docstring for cache_path"""
    return os.path.join(CACHE_DIR, hash_name(host, port))

def create_cache_dir():
    """crate cache directory"""
    try:
        if not os.path.exists(CACHE_DIR):
            os.mkdir(CACHE_DIR)
    except Exception:
        pass

def make_cache(host, port, js):
    """create cache file"""
    create_cache_dir()
    try:
        with open(cache_path(host, port), 'w') as f:
            f.writelines(js)
    except Exception, e:
        print e

def get_cache(host, port):
    """get cache file"""
    try:
        with open(cache_path(host, port), 'r') as f:
            cache = f.readlines()
    except Exception, e:
        print e
        cache = None
    return cache

def make_js(scheme, netloc, host, port, cname):
    """
    Get java script from cache file if present, 
    otherwise generate java script with customize attrs and write to disk.

    """
    js = get_cache(host, port)
    if not js:
        js = TEMPLATE
        js = __replace(js, '$SCHEMA', str(scheme))
        js = __replace(js, '$NETLOC', str(netloc))
        js = __replace(js, '$HOST', str(host))
        js = __replace(js, '$PORT', str(port))
        js = __replace(js, '$CNAME', str(cname))
        js = slimit.minify(js, mangle=True, mangle_toplevel=True)
        make_cache(host, port, js)
    return js


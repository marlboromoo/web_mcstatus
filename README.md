# web_mcstatus

WEB API to query Minecraft status.

## Requirments 
 - Python
 - [mcstatus] [1]
 - [Bottle] [2]
 - [uWSGI] [3] (option)
 - [nginx] [4] (option)
                                                                                
## Install

### Build-in server
```
cd /var/www/
git clone https://github.com/marlboromoo/web_mcstatus.git
cd web_mcstatus
git submodule update --recursive --init
sudo python ./web.py
```

### nginx + uWSGI
```
#. ubuntu 12.04
sudo apt-get install uwsgi uwsgi-plugin-python nginx 
cd /var/www/
git clone https://github.com/marlboromoo/web_mcstatus.git
cd web_mcstatus 
git submodule update --recursive --init
#. uWSGI config
\cp doc/uwsgi.xml /etc/uwsgi/apps-available/web_mcstatus.xml
\ln -s  /etc/uwsgi/apps-available/web_mcstatus.xml /etc/uwsgi/apps-enabled/
/etc/init.d/uwsgi restart
#. nginx config
\cp doc/nginx.conf /etc/nginx/sites-available/web_mcstatus
\ln -s /etc/nginx/sites-available/web_mcstatus /etc/nginx/sites-enabled/
/etc/init.d/nginx restart
```

## Usage
```
curl http://127.0.1.1/ 
curl http://127.0.1.1/status 
curl http://127.0.1.1/rules #. full status
```

## Author                                                                       
Timothy.Lee a.k.a MarlboroMoo.                                                  
                                                                                
## License                                                                      
Released under the [MIT License] [5].                                           
                                                                                
  [1]: https://github.com/Dinnerbone/mcstatus "mcstatus"
  [2]: http://bottlepy.org "Bottle"
  [3]: http://curl.haxx.se/ "uWSGI"
  [4]: http://nginx.org/ "Nginx"
  [5]: http://opensource.org/licenses/MIT "MIT License"


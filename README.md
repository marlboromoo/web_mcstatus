# web_mcstatus

WEB API/Widget to query Minecraft status.

## Requirments 
 - Python
 - [mcstatus] [1]
 - [Bottle] [2]
 - [SlimIt] [7]
 - [uWSGI] [3] (option)
 - [nginx] [4] (option)
                                                                                
## Install

### Build-in server
```
sudo su -
cd /var/www/
git clone https://github.com/marlboromoo/web_mcstatus.git
cd web_mcstatus
git submodule update --recursive --init
pip install bottle
python ./web.py
```

### Nginx + uWSGI
```
#. ubuntu 12.04
sudo su -
apt-get install uwsgi uwsgi-plugin-python nginx 
pip install bottle
cd /var/www/
git clone https://github.com/marlboromoo/web_mcstatus.git
cd web_mcstatus 
git submodule update --recursive --init
#. uWSGI config
cp doc/uwsgi.xml /etc/uwsgi/apps-available/web_mcstatus.xml
ln -s  /etc/uwsgi/apps-available/web_mcstatus.xml /etc/uwsgi/apps-enabled/
/etc/init.d/uwsgi restart
#. nginx config
cp doc/nginx.conf /etc/nginx/sites-available/web_mcstatus
ln -s /etc/nginx/sites-available/web_mcstatus /etc/nginx/sites-enabled/
/etc/init.d/nginx restart
```

## Upgrade
```
cd /var/www/web_mcstatus
git pull
rm -rf /tmp/web_mcstatus_js/* #. clean JS cache files
```

## Usage

### API
```
curl http://127.0.1.1/ 
curl http://127.0.1.1/status 
curl http://127.0.1.1/rules #. full status
```

### WIDGET
see [web_mcstatus.html] [5].

## TODO
 - Configuation system
 - ...

## Author                                                                       
Timothy.Lee a.k.a MarlboroMoo.                                                  
                                                                                
## License                                                                      
Released under the [MIT License] [6].                                           
                                                                                
  [1]: https://github.com/Dinnerbone/mcstatus "mcstatus"
  [2]: http://bottlepy.org "Bottle"
  [3]: http://projects.unbit.it/uwsgi/ "uWSGI"
  [4]: http://nginx.org/ "Nginx"
  [5]: https://github.com/marlboromoo/web_mcstatus/blob/master/doc/web_mcstatus.html "web_mcstatus.html"
  [6]: http://opensource.org/licenses/MIT "MIT License"
  [7]: https://github.com/rspivak/slimit "SlimIt"


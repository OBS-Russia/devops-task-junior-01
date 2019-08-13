# devops-task-junior-01

This repository contains dummy __Python 3.7__ HTTP service with single JSON-RPC 
endpoint available thought HTTP GET request via URL 
`http://{host_ip_address}/hello`.

Service is run by executing `app.py` file. Ensure, that proper Python 
interpreter is configured and all necessary requirements are installed. 
By default service starts on `0.0.0.0:8000`, but it could be changed via 
configuration options in `settings.py` file.

The task is to build virtual machine (VM) image compatible with latest 
[VirtualBox](https://www.virtualbox.org/). Image must be based on any available
Linux distributive with Docker installed. Any VM, based on that image, must on
boot load [Docker Service](https://docs.docker.com/get-started/part3/) based
on two containers:
1. NGINX
2. dummy app

In that Docker Service NGINX must be configured to proxy traffic to dummy app 
container. Dummy app must be availiable only via NGINX proxy.

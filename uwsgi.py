[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = voteo.sock
chmod-socket = 660
vacuum = true

die-on-term = true
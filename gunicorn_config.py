command = "/srv/www/py.nashe.menu/htdocs/env/bin/gunicorn"
pythonpath = "/srv/www/py.nashe.menu/htdocs/menushka"
bind = "0.0.0.0:8000"
workers = 2
user = "root"
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = ["DJANGO_SETTINGS_MODULE=menushka.dev_settings"]

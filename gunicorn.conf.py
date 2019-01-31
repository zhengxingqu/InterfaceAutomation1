import multiprocessing

bind = "172.16.165.129:8082"
workers = 2  
errorlog = '/gunicorn.error.log'
#accesslog = './gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'gunicorn_blog_project'

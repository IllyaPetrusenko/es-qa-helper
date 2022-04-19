
def get_host(env):
    if env == 'dev':
        host = 'http://10.0.20.126:8900/api/v1/'
        credentials = 'Basic dXNlcjpwYXNzd29yZA=='
        return host
    elif env == 'sandbox':
        host = 'http://10.0.10.116:8900/api/v1/'
        credentials = 'Basic dXNlcjpwYXNzd29yZA=='
        return host


def get_host(env):
    if env == 'dev':
        host = 'http://10.0.20.126:8900/api/v1/'
        credentials = 'Basic dXNlcjpwYXNzd29yZA=='
        document = 'b5802bf4-b838-431e-831b-7d0ef5ed9437-1593170692555'
        public_point = 'http://dev.public.eprocurement.systems/tenders/'
        return host, credentials, document, public_point
    elif env == 'sandbox':
        host = 'http://10.0.10.116:8900/api/v1/'
        credentials = 'Basic dXNlcjpwYXNzd29yZA=='
        document = '21a5d5ef-84c0-4730-892c-338db4e3e98d-1631521816681'
        public_point = 'http://public.eprocurement.systems/tenders/'
        return host, credentials, document, public_point

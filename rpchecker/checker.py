from http.client import HTTPConnection

def site_is_online(url, timeout=2):
    '''Return True is the target is online.

    Raise an exception Otherwise.
    '''
    error = Exception("unknown error")
    host=url
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
        raise error

from http.client import HTTPConnection, HTTPSConnection
from urllib.parse import urlparse


def site_is_online(url, timeout=2):
    """Return True when the target is reachable over HTTP(S)."""
    parsed = urlparse(url if "://" in url else f"http://{url}")
    host = parsed.hostname or parsed.netloc
    if not host:
        raise ValueError(f"Invalid URL: {url}")

    if parsed.scheme == "https":
        ports = [parsed.port or 443]
        connection_cls = HTTPSConnection
    elif parsed.scheme == "http":
        ports = [parsed.port or 80]
        connection_cls = HTTPConnection
    else:
        ports = [80, 443]
        connection_cls = HTTPConnection

    for port in ports:
        connection = connection_cls(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception:
            continue
        finally:
            connection.close()

    return False

from urllib.parse import urlparse
o = urlparse(request.base_url)
host = o.hostname

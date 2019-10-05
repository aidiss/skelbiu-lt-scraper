from w3lib.http import basic_auth_header

class CustomProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://212.24.110.68:1338"

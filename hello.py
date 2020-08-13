def app(environ, start_response):
    status = '200 Ok'
    headers = [
        ('Content-type', 'text/plain')
    ]
    body = [
        bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')
    ]
    start_response(status, headers)
    return body

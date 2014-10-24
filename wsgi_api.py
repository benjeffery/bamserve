import arraybuffer
import bamread
from gzipstream import gzip

def application(request, start_response):
    print request
    result_set = bamread.fetch()
    data = gzip(data=''.join(arraybuffer.encode_array_set(result_set)))
    status = '200 OK'
    response_headers = [('Access-Control-Allow-Origin', '*'),
                        ('Content-type', 'text/plain'),
                        ('Content-Length', str(len(data))),
                        ('Content-Encoding', 'gzip'),
                        ('Server', 'BamServe')
                        ]
    start_response(status, response_headers)
    yield data

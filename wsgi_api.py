import arraybuffer
import bamread
from gzipstream import gzip
import yaml
import sys
import os

with open(sys.argv[-1], 'r') as f:
    config = yaml.load(f)

sets = config['sets']

def return_404(start_response):
    start_response('404 Not Found', (('Access-Control-Allow-Origin', '*'),))

def application(request, start_response):
    #TODO Could allow listing of files
    try:
        bam, set, bam_id, chrom, start, end = request['PATH_INFO'].split('/')[1:]
        start, end = int(start), int(end)
        start = max(0, start)
    except ValueError:
        return_404(start_response)
        return
    if bam != 'bam':
        return_404(start_response)
        return

    try:
        set = sets[set]
    except KeyError:
        return_404(start_response)
        return

    bam_dir = os.path.join(set['path'], bam_id)
    bam_file = os.path.join(bam_dir, bam_id+'.bam')
    if not (os.path.isdir(bam_dir) and os.path.isfile(bam_file)):
        return_404(start_response)
        return

    result_set = bamread.fetch(bam_file, chrom, start, end)
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

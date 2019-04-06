# encoding: utf8
import base64
from sys import stderr
from urllib.parse import urlencode
from werkzeug.wrappers import BaseResponse


SCRIPT_NAME = ''
SERVER_PORT = '80'
SERVER_PROTOCOL = 'HTTP/1.1'
SERVER_SOFTWARE = 'serverlessplus'
URL_SCHEME = 'http'
WSGI_VERSION = (1, 0)


def create_environ(event: dict, context: dict):
    method = event['httpMethod'] if 'httpMethod' in event else 'GET'
    path = event['path'] if 'path' in event else '/'
    query = event['queryString'] if 'queryString' in event else {}
    query_string = urlencode(query, True)
    headers = event['headers'] if 'headers' in event else {}
    server_name = headers['host'] if 'host' in headers else '127.0.0.1'
    body = event['body'] if 'body' in event else ''
    request_context = event['requestContext'] if 'requestContext' in event else {}
    remote_addr = request_context.get('sourceIp', '127.0.0.1')

    environ = {
        'PATH_INFO': path,
        'QUERY_STRING': query_string,
        'REMOTE_ADDR': remote_addr,
        # 'REMOTE_PORT': '',
        'REQUEST_METHOD': method,
        'SCRIPT_NAME': SCRIPT_NAME,
        'SERVER_NAME': server_name,
        'SERVER_PORT': SERVER_PORT,
        'SERVER_PROTOCOL': SERVER_PROTOCOL,
        'SERVER_SOFTWARE': SERVER_SOFTWARE,
        'wsgi.version': WSGI_VERSION,
        'wsgi.url_scheme': URL_SCHEME,
        'wsgi.input': body,
        'wsgi.errors': stderr,
        'wsgi.multiprocess': False,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
    }

    for name, value in headers.items():
        canonical_name = f"HTTP_{name.upper().replace('-', '_')}"
        environ[canonical_name] = value

    return environ


def create_app(name: str):
    module, app_name = name.split(':')
    return getattr(__import__(module), app_name)


def get_response(app: callable, environ: dict):
    return BaseResponse.from_app(app, environ)


def wrap_response(response: BaseResponse, options: dict):
    headers = {}
    for name, value in response.headers:
        headers[name] = value
    headers['x-powered-by'] = 'serverlessplus'

    binary_mime_types = options.get('binary_mime_types', [])
    encoded = headers.get('content-type', 'text/plain') in binary_mime_types
    if encoded:
        body = base64.b64encode(response.data).decode('utf-8')
    else:
        body = response.get_data(as_text=True)

    data = {
        'isBase64Encoded': encoded,
        'statusCode': response.status_code,
        'headers': headers,
        'body': body,
    }
    return data

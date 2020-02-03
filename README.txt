B"H.


flupfcgiwrap is akin to fcgiwrap, however, instead of providing a FastCGI interface for a CGI application, it provides a FastCGI interface for a WSGI application.

It is currently designed to be used with spawn-fcgi or similar.

Example usage: /usr/bin/spawn-fcgi -s /tmp/socket_dir/supysonic_fcgi.socket -- /usr/local/bin/python3 /flupfcgiwrap.py /app/supysonic/cgi-bin/supysonic.wsgi application


Currently licensed BSD.

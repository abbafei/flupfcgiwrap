#!/usr/bin/env python2
#B"H.
'''for use with fcgiwrap and the like'''
import imp


if __name__ == '__main__':
    import sys
    try:
        from flup.server.fcgi import WSGIServer
    except ImportError:
        sys.stderr.write('flup was not found\n')
        exit(1)

    if len(sys.argv) < 2:
        sys.stderr.write('usage: {0} <python-file> <app_varname>\n'.format(sys.argv[0]))
        exit(1)
    else:
        mod = imp.load_source('', sys.argv[1])
        appy = getattr(mod, sys.argv[2])
        WSGIServer(appy).run()

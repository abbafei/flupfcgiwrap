#!/usr/bin/env python
#B"H.
'''like fcgiwrap, for wsgi applications. for use with spawn-fcgi and the like.'''
import sys
if sys.version_info.major < 3:
    import imp
else:
    import importlib.util
    import importlib.machinery


def _imported_source(file_path, out_module_name):
    if sys.version_info.major < 3:
        return imp.load_source(out_module_name, file_path)
    else:
        #spec = importlib.util.spec_from_file_location(out_module_name, file_path) # doesn't work for files with unrecognized file extensions
        # via https://stackoverflow.com/a/19011259
        loader = importlib.machinery.SourceFileLoader(out_module_name, file_path)
        spec = importlib.util.spec_from_loader(loader.name, loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module


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
        mod = _imported_source(sys.argv[1], '')
        appy = getattr(mod, sys.argv[2])
        WSGIServer(appy).run()

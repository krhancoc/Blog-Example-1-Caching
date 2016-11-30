import functools

from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError


def cache(cache_alias='default'):
    class memcache(object):
        '''
        Decorator. Caches a function's return value each time it is called.
        If called later with the same arguments, the cached value is returned
        (not reevaluated).
        '''
        def __init__(self, func):
            self.func = func
            try:
                self.cache = caches[cache_alias]
            except InvalidCacheBackendError:
                print("Invalid Cache Alias, loading default cache...")
                self.cache = caches['default']
        def __call__(self, value):
            response = self.cache.get(value)
            if response is None:
                response = self.func(value)
                self.cache.set(value, response, None)
                print("CACHE MISS >>>> " + str(response))
                return response
            else:
                print ("CACHE HIT >>>> " + str(response))
                return response

        def __repr__(self):
            '''Return the function's docstring.'''
            return self.func.__doc__

        def __get__(self, obj, objtype):
            '''Support instance methods.'''
            return functools.partial(self.__call__, obj)

    return memcache

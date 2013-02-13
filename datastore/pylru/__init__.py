
__version__ = '0.1.0'
__author__ = 'Juan Batiz-Benet'
__email__ = 'juan@benet.ai'
__doc__ = '''
pylru datastore implementation.

Tested with:
  * datastore 0.3.0
  * pylru 1.0.5

'''

import pylru
import datastore


class LRUCacheDatastore(datastore.Datastore):
  '''Represents an LRU cache datastore, backed by pylru.

     Hello World:

       >>> import datastore.pylru
       >>>
       >>> ds = datastore.pylru.LRUCacheDatastore(100)
       >>>
       >>> hello = datastore.Key('hello')
       >>> ds.put(hello, 'world')
       >>> ds.contains(hello)
       True
       >>> ds.get(hello)
       'world'
       >>> ds.delete(hello)
       >>> ds.get(hello)
       None

  '''

  def __init__(self, size):
    self._cache = pylru.lrucache(size)

  def __len__(self):
    return len(self._cache)

  def clear(self):
    self._cache.clear()

  def get(self, key):
    '''Return the object named by key.'''
    try:
      return self._cache[key]
    except KeyError, e:
      return None

  def put(self, key, value):
    '''Stores the object.'''
    self._cache[key] = value

  def delete(self, key):
    '''Removes the object.'''
    if key in self._cache:
      del self._cache[key]

  def contains(self, key):
    '''Returns whether the object is in this datastore.'''
    return key in self._cache

  def query(self, query):
    '''Returns a sequence of objects matching criteria expressed in `query`'''
    # entire dataset already in memory, so ok to apply query naively
    return query(self._cache.values())

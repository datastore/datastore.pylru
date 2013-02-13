# datastore-pylru

## datastore implementation for pylru

See [datastore](https://github.com/datastore/datastore).


### Install

From pypi (using pip):

    sudo pip install datastore.pylru

From pypi (using setuptools):

    sudo easy_install datastore.pylru

From source:

    git clone https://github.com/datastore/datastore.pylru/
    cd datastore.pylru
    sudo python setup.py install


### License

datastore.pylru is under the MIT License.

### Contact

datastore.pylru is written by [Juan Batiz-Benet](https://github.com/jbenet).
It was extracted from [datastore](https://github.com/datastore/datastore)
in Feb 2013.

Project Homepage:
[https://github.com/datastore/datastore.pylru](https://github.com/datastore/datastore.pylru)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

    >>> import pylru
    >>> import datastore.pylru
    >>>
    >>> r = pylru.pylru()
    >>> ds = datastore.pylru.pylruDatastore(r)
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

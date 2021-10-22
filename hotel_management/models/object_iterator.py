from typing import Iterable, List, Any, Iterator

from hotel_management.models.amenity import Amenity

"""
Iterator pattern is useful when you want to separate out the iteration logic which may be used at multiple
places in your code , say you want to traverse list of objects you can always use for or while loop, right?
So if you want to traverse begin to end or reverse manner you can hide the complexity of iterating inside 
iterator method, may be useful in sending notifications etc

Some people asks to use Decorator design pattern for Notification Sender but we should not use that
forcefully because the main purpose of decorator pattern is to decorate the existing behaviour
it has both has a and is a relationship with the main component (which can be a decorator itself as well)

PUB SUB model use the observer pattern!

"""


class ObjectCollection(Iterable):
    def __init__(self, collection: List[Any] = None):
        self._collection = collection or []

    def __iter__(self):
        return ObjectIterator(self._collection)

    def add_item(self, item: Amenity):
        self._collection.append(item)


class ObjectIterator(Iterator):

    def __init__(self, collection: ObjectCollection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if self._reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

    _position: int = None

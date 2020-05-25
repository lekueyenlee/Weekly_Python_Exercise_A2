import pytest
from exercise_4_my_solution import sample_method
from io import StringIO

def test_empty():
    s = StringIO()
    sample_method(s)

    s.seek(0)
    assert s.read() == ''


def test_one_person():
    s = StringIO()
    sample_method(s, a=1)

    s.seek(0)
    assert s.read() == 'a,1\n'


def test_five_people():
    s = StringIO()
    sample_method(s, a=1, b=2, c=3, d=4, e=5)

    s.seek(0)
    assert s.read() == 'a,1\nb,2\nc,3\nd,4\ne,5\n'


def test_sorted_five_people():
    s = StringIO()
    sample_method(s, a=1, d=4, b=2, c=3, e=5)

    s.seek(0)
    assert s.read() == 'a,1\nb,2\nc,3\nd,4\ne,5\n'
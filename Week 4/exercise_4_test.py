import pytest
from exercise_4_my_solution import cryptogrammer
from io import StringIO

def test_empty():
    s = StringIO()
    cryptogrammer(s)

    s.seek(0)
    assert s.read() == ''


def test_one_person():
    s = StringIO()
    cryptogrammer(s, a=1)

    s.seek(0)
    assert s.read() == 'a,1\n'


def test_five_people():
    s = StringIO()
    cryptogrammer(s, a=1, b=2, c=3, d=4, e=5)

    s.seek(0)
    assert s.read() == 'a,1\nb,2\nc,3\nd,4\ne,5\n'


def test_sorted_five_people():
    s = StringIO()
    cryptogrammer(s, a=1, d=4, b=2, c=3, e=5)

    s.seek(0)
    assert s.read() == 'a,1\nb,2\nc,3\nd,4\ne,5\n'
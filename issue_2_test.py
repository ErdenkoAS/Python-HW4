# -*- coding: utf-8 -*-
"""issue_2_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r3H-BU3pbVkGMRjGC0PfH5C4RV7kPAFW
"""

from morse import decode
import pytest


@pytest.mark.parametrize(
    "dot_dash, message",
    [('... --- ...', 'SOS'),
     ('', ''),
     ('.---- .---- .----', '111')]
)
def test_decode(dot_dash, message):
    assert decode(dot_dash) == message
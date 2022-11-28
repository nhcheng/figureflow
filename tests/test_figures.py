import os
import sys


def test_all():
    """Test all scripts in ./scripts/figures"""

    os.system('Xvfb :1 -screen 0 1600x1200x16  &')
    os.environ['DISPLAY']=':1.0'

    assert os.system("python ./scripts/figures/Figure1.py") == 0

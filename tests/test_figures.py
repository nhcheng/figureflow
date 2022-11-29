import os
import sys


def test_all():
    """Test all scripts in ./scripts/figures"""

    os.system('Xvfb :1 -screen 0 1600x1200x16  &')
    os.environ['DISPLAY']=':1.0'

    for i in range(1, 10 + 1):
        assert os.system(f"python ./scripts/figures/Figure{i}.py") == 0


import os

def test_all():
    """Test all scripts in ./scripts/figures"""
    assert os.system("python ./scripts/figures/Figure1.py") == 0
    

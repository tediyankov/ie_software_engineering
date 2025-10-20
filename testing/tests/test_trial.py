import numpy as np
import numpy.testing as npt
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from inflammation.classes import Trial

@pytest.fixture()
def trial_1():
    return Trial(1, os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'data', 'inflammation-01.csv'
    ))

class TestTrial:
    """Test class for Trial model."""

    def test_create_trial(self, trial_1):
        """Test that a Trial object is created correctly with attributes."""
        assert isinstance(trial_1.data, np.ndarray)

    def test_daily_mean(self, trial_1):
        """Test mean function works for array of zeroes and positive integers."""
        result = trial_1.daily_mean()
        assert isinstance(result, np.ndarray)
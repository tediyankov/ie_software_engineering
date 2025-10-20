"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [5, 6]),
        ([ [1.5, 2.5], [3.5, 4.5], [5.5, 6.5] ], [5.5, 6.5]),
        ([ [-1, -2], [-3, -4], [-5, -6] ], [-1, -2]),

    ])
def test_daily_max(test, expected):
    """Test max function works for array of zeroes and positive integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [1, 2]),
        ([ [1.5, 2.5], [3.5, 4.5], [5.5, 6.5] ], [1.5, 2.5]),
        ([ [-1, -2], [-3, -4], [-5, -6] ], [-5, -6]),

    ])
def test_daily_min(test, expected):
    """Test min function works for array of zeroes and positive integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        # test case with negative values - should raise ValueError
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        # test case with positive values - should work normally
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
        # test case with non-numpy array (list) - should raise TypeError
        (
            [[1, 2, 3], [4, 5, 6]],
            None,
            TypeError,
        ),
        # test case with 1D array - should raise ValueError
        (
            [1, 2, 3, 4, 5],
            None,
            ValueError,
        ),
        # test case with 3D array - should raise ValueError
        (
            [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
            None,
            ValueError,
        ),
        # test case with empty array - should raise ValueError
        (
            [],
            None,
            ValueError,
        ),
        # test case with array that has zero rows - should raise ValueError
        (
            np.array([]).reshape(0, 3),
            None,
            ValueError,
        ),
        # test case with array that has zero columns - should raise ValueError
        (
            np.array([]).reshape(3, 0),
            None,
            ValueError,
        ),
        # test case with zeros - should work
        (
            [[0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0]],
            None,
        ),
        # test case with NaN values - should normalize NaN to 0
        (
            [[1, np.nan, 3], [4, 5, 6]],
            [[0.33, 0, 1], [0.67, 0.83, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
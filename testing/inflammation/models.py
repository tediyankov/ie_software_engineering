"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np

def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)

def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """

    # checking if data is a numpy ndarray
    if not isinstance(data, np.ndarray):
        raise TypeError('Input data must be a numpy ndarray')
    
    # checking if data is 2D
    if data.ndim != 2:
        raise ValueError('Input data must be a 2D array')
    
    # checking if data has at least one row and one column
    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError('Input data must have at least one row and one column')
    
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    data_copy = data.copy()
    data_copy[data_copy < 0] = 0
    max_data = np.nanmax(data_copy, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data_copy / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    return normalised
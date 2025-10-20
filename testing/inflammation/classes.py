
import numpy as np

# class Patient
class Patient: 

    def __init__(self, id, data): 
        self.id = id 
        self.inflammation_scores = data

    def data_mean(self):
        if self.inflammation_scores.size == 0: 
            return 0
        return np.mean(self.inflammation_scores)
    
    def data_max(self):
        if self.inflammation_scores.size == 0: 
            return 0
        return np.max(self.inflammation_scores)
    
    def data_min(self):
        if self.inflammation_scores.size == 0:  
            return 0
        return np.min(self.inflammation_scores)
    
# class Trial
class Trial:

    def __init__(self, id, filename): 
        self.id = id
        self.data = self.load_csv(filename)  

    ## methods

    def load_csv(self, filename):
        """Load numpy array from CSV."""
        return np.loadtxt(fname=filename, delimiter=',')
    
    def daily_mean(self):
        """Calculate the daily mean of a 2d inflammation data array."""
        return np.mean(self.data, axis=0)


    def daily_max(self):
        """Calculate the daily max of a 2d inflammation data array."""
        return np.max(self.data, axis=0)


    def daily_min(self):
        """Calculate the daily min of a 2d inflammation data array."""
        return np.min(self.data, axis=0)

    def patient_normalise(self):
        """
        Normalise patient data from a 2D inflammation data array.

        NaN values are ignored, and normalised to 0.

        Negative values are rounded to 0.
        """

        # checking if data is a numpy ndarray
        if not isinstance(self.data, np.ndarray):
            raise TypeError('Input data must be a numpy ndarray')
        
        # checking if data is 2D
        if self.data.ndim != 2:
            raise ValueError('Input data must be a 2D array')
        
        # checking if data has at least one row and one column
        if self.data.shape[0] == 0 or self.data.shape[1] == 0:
            raise ValueError('Input data must have at least one row and one column')
        
        if np.any(self.data < 0):
            raise ValueError('Inflammation values should not be negative')

        max_data = np.nanmax(self.data, axis=1)
        with np.errstate(invalid='ignore', divide='ignore'):
            normalised = self.data / max_data[:, np.newaxis]
        normalised[np.isnan(normalised)] = 0
        normalised[normalised < 0] = 0
        return normalised
    
    def get_patient (self, patient_id):
        """Retrieve a Patient object by ID."""
        if patient_id < 0 or patient_id >= self.data.shape[0]:
            raise IndexError("Patient ID out of range.")
        patient_data = self.data[patient_id, :]
        return Patient(patient_id, patient_data)
"""Tests for the Patient model."""

import numpy as np
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

class TestPatient:

    """Test class for Patient model."""
    
    @classmethod
    def setup_class(cls):
        """Set up Patient objects for testing."""
        from inflammation.classes import Patient
        
        # first patient with normal data
        cls.patient1_id = 1
        cls.patient1_data = np.array([2, 4, 6, 8, 10])
        cls.patient1 = Patient(cls.patient1_id, cls.patient1_data)
        
        # second patient with different data including negatives
        cls.patient2_id = 2
        cls.patient2_data = np.array([-5, -2, -8, -1])
        cls.patient2 = Patient(cls.patient2_id, cls.patient2_data)

    def test_create_patient(self):
        """Test that a Patient object is created correctly with attributes."""
        from inflammation.classes import Patient
        
        patient_id = 3
        data = np.array([1, 2, 3, 4, 5])
        p = Patient(patient_id, data)

        assert p.id == patient_id
        assert np.array_equal(p.inflammation_scores, data)

    def test_patient_data_mean(self):
        """Test that patient data_mean method returns correct mean."""
        assert self.patient1.data_mean() == 6.0

    def test_patient_data_mean_single_value(self):
        """Test data_mean with single value."""
        from inflammation.classes import Patient
        
        data_single = np.array([5])
        p_single = Patient(3, data_single)
        assert p_single.data_mean() == 5.0

    def test_patient_data_mean_empty(self):
        """Test that patient data_mean returns 0 for empty data."""
        from inflammation.classes import Patient
        
        data = np.array([])
        p = Patient(4, data)
        assert p.data_mean() == 0

    def test_patient_data_max(self):
        """Test that patient data_max method returns correct maximum."""
        assert self.patient1.data_max() == 10

    def test_patient_data_max_negative(self):
        """Test data_max with negative values."""
        assert self.patient2.data_max() == -1

    def test_patient_data_max_empty(self):
        """Test that patient data_max returns 0 for empty data."""
        from inflammation.classes import Patient
        
        data = np.array([])
        p = Patient(5, data)
        assert p.data_max() == 0

    def test_patient_data_min(self):
        """Test that patient data_min method returns correct minimum."""
        assert self.patient1.data_min() == 2

    def test_patient_data_min_negative(self):
        """Test data_min with negative values."""
        assert self.patient2.data_min() == -8

    def test_patient_data_min_empty(self):
        """Test that patient data_min returns 0 for empty data."""
        from inflammation.classes import Patient
        
        data = np.array([])
        p = Patient(6, data)
        assert p.data_min() == 0

    def test_patient_with_zeros(self):
        """Test patient methods work correctly with zero values."""
        from inflammation.classes import Patient
        
        data = np.array([0, 0, 0, 0])
        p = Patient(7, data)
        
        assert p.data_mean() == 0.0
        assert p.data_max() == 0
        assert p.data_min() == 0

    def test_patient_with_float_data(self):
        """Test patient methods work correctly with float values."""
        from inflammation.classes import Patient
        
        data = np.array([1.5, 2.7, 3.2, 1.1])
        p = Patient(8, data)
        
        assert p.data_mean() == pytest.approx(2.125)
        assert p.data_max() == 3.2
        assert p.data_min() == 1.1
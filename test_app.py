import unittest
import os
import sys
from joblib import load

class TestApp(unittest.TestCase):
    
    def test_model_exists(self):
        """Test that the model file exists and can be loaded"""
        model_path = "src/models/model.joblib"
        self.assertTrue(os.path.exists(model_path), f"Model file not found at {model_path}")
        
    def test_model_loading(self):
        """Test that the model can be loaded successfully"""
        model_path = "src/models/model.joblib"
        try:
            model = load(model_path)
            self.assertIsNotNone(model, "Model should not be None after loading")
        except Exception as e:
            self.fail(f"Failed to load model: {e}")
    
    def test_model_prediction(self):
        """Test that the model can make predictions"""
        model_path = "src/models/model.joblib"
        try:
            model = load(model_path)
            # Create dummy features for testing (30 features as expected by the model)
            dummy_features = [[0.0] * 30]
            prediction = model.predict(dummy_features)
            self.assertIsNotNone(prediction, "Prediction should not be None")
            self.assertEqual(len(prediction), 1, "Should return one prediction")
        except Exception as e:
            self.fail(f"Failed to make prediction: {e}")

if __name__ == '__main__':
    unittest.main()

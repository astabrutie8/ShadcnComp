# test_shadcncomp.py
"""
Tests for ShadcnComp module.
"""

import unittest
from shadcncomp import ShadcnComp

class TestShadcnComp(unittest.TestCase):
    """Test cases for ShadcnComp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShadcnComp()
        self.assertIsInstance(instance, ShadcnComp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShadcnComp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

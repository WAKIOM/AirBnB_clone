import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel
    """

    def setUp(self):
        """
        Set up method for the test class
        """
        self.base_model = BaseModel()

    def tearDown(self) -> None:
        return super().tearDown()

    def str(self):
        """
        Test the __str__ method
        """
        self.assertIsInstance(str(self.base_model), str)

    def save(self):
        """
        Test the save method
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, initial_updated_at)

    def to_dict(self):
        """
        Test the to_dict method
        """
        self.assertIsInstance(self.base_model.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()

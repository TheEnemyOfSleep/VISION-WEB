from django.test import TestCase
from django.db.utils import IntegrityError

from page.tests.common import create_block


class CreateBlock(TestCase):
    """Unit testing block model"""

    def test_create_block_valid_data(self):
        """Test block model with valid data"""
        payload = {
            'classes': "nice_class",
            'style': "display: block",
            'name': "elem1",
            'extra_attrs': "foo='bar'",
            'sorting': 1
        }
        block = create_block(**payload)
        self.assertEqual(block.classes, "nice_class")
        self.assertEqual(block.style, "display: block")
        self.assertEqual(block.name, "elem1")
        self.assertEqual(block.extra_attrs, "foo='bar'")
        self.assertEqual(block.sorting, 1)

    def test_create_block_invalid_date(self):
        """Test bloack models with invalid data"""
        with self.assertRaises(IntegrityError):
            create_block(name="elem1")
            create_block(name="elem1")

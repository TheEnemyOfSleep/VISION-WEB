from django.test import TestCase

from page.tests.common import create_element


class CreateElement(TestCase):
    """Unit testing element model"""

    def test_create_element(self):

        payload = {
            'content': "<div>Hello world</div>",
            'classes': 'foobar',
            'style': 'margin: 0'
        }

        element = create_element(**payload)

        self.assertEqual(element.content, "<div>Hello world</div>")
        self.assertEqual(element.classes, 'foobar')
        self.assertEqual(element.style, 'margin: 0')

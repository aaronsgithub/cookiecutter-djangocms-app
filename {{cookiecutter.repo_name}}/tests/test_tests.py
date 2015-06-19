from django.conf import settings
from django.test import TestCase


class TestTestsAreWorking(TestCase):

    def test_tests_are_running(self):
        """
        Facetious test to check test run.
        """
        are_tests_running = True
        self.assertTrue(are_tests_running)

    def test_test_settings_are_being_detected(self):
        """
        Facetious test to check test_settings.py is being used in tests.
        """
        self.assertEqual(settings.ARE_THE_SETTINGS_BEING_DETECTED, True)

"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Runs once regardless of how many test methods are defined
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        """
        Runs before each test method
        """
        # Make sure database exists
        with app.app_context():
            db.create_all()

        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        """
        Runs after each test method is called
        """
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
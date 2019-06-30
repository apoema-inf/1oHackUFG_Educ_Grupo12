from flask import Flask
import unittest

from application import db, create_app
from models import Pesquisa


def populate_db():
        p = Pesquisa(project_name="test", project_coordinator="test", project_specific_area="test",
         project_academic="test", resource_origin="test", resource_value=100, members_names="names",
          category="1", keywords="keywords")
        db.session.add(p)
        db.session.commit()


class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = create_app()
        self.app.app_context().push()    
        populate_db() # Your function that adds test data.

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()

    def test_database_is_created(self):
        number_of_items = Pesquisa.query.all()
        self.assertGreater(len(number_of_items), 0, 'Table adding values right')


if __name__ == '__main__':
    unittest.main()

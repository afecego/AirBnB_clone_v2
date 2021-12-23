""" Module for testing db storage"""
import models
import MySQLdb
import unittest
from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
import inspect
import pycodestyle
from models.engine import file_storage


class Test_style(unittest.TestCase):
    """[Class created to test style and syntax requirements for the
    base_model class]
    """
    @classmethod
    def setUpClass(cls) -> None:
        """[list the functions to docstring test]
        """
        cls.methods_ds = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/engine/file_storage.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")

    def test_docstring(self):
        """[Function to test docstring of the class and the module]
        """
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertIsNot(FileStorage.__doc__, None,
                         "class needs a docstring")
        self.assertTrue(len(file_storage.__doc__) > 0,
                        "file_storage.py needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) > 0,
                        "class needs a docstring")
        for method in self.methods_ds:
            self.assertIsNot(method[1].__doc__, None,
                             f"{method[0]} needs docstring")
            self.assertTrue(len(method[1].__doc__) >
                            0, f"{method[0]} needs docstring")


class Test_DBStorage(unittest.TestCase):
    """Unittests for testing the DBStorage class."""

    @classmethod
    def setUpClass(cls):
        """DBStorage testing, Starting point 
        """

        if isinstance(models.storage, DBStorage):
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()

            cls.state = State(name="Test_state")
            cls.storage._DBStorage__session.add(cls.state)

            cls.city = City(name="Test_city", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)

            cls.user = User(email="test@gmail.com", password="test_pwd")
            cls.storage._DBStorage__session.add(cls.user)

            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="test_place")

            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="test_amenity")

            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(user_id=cls.user.id, place_id=cls.place.id,
                                text="test_review")

            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """DBStorage testing, Ending point.
        """
        if isinstance(models.storage, DBStorage):

            """Deleting from db"""
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()

            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review

            """Closing Session
            """
            cls.storage._DBStorage__session.close()
            del cls.storage

    @unittest.skipIf(isinstance(models.storage, FileStorage),
                     "Testing DB Storage")
    def test_save(self):
        """Testing save method, by testing len query got."""

        state = State(name="California")
        self.storage._DBStorage__session.add(state)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'California'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        cursor.close()
#!/usr/bin/python3
import unittest
import pep8
import json
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        del cls.user

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_all(self):
        storage = FileStorage()
        objects = storage.all()
        self.assertIsNotNone(objects)
        self.assertEqual(type(objects), dict)
        self.assertIs(objects, storage._FileStorage__objects)

    def test_new(self):
        storage = FileStorage()
        objects = storage.all()
        new_user = User()
        new_user.id = 123455
        new_user.name = "Kevin"
        storage.new(new_user)
        key = new_user.__class__.__name__ + "." + str(new_user.id)
        self.assertIn(key, objects)

    def test_reload_filestorage(self):
        self.storage.save()
        root_path = os.path.dirname(os.path.abspath("console.py"))
        file_path = os.path.join(root_path, "file.json")
        with open(file_path, 'r') as file:
            content_before = file.readlines()

        try:
            os.remove(file_path)
        except Exception:
            pass
        self.storage.save()

        with open(file_path, 'r') as file:
            content_after = file.readlines()
        self.assertEqual(content_before, content_after)

        try:
            os.remove(file_path)
        except Exception:
            pass
        with open(file_path, "w") as file:
            file.write("{}")
        with open(file_path, "r") as file:
            for line in file:
                self.assertEqual(line, "{}")
        self.assertIsNone(self.storage.reload())


if __name__ == "__main__":
    unittest.main()


from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest

class StoreTest(UnitBaseTest):

    def test_create_store(self):
        # Checks that store is created successfully
        store = StoreModel('test')
        self.assertEqual(store.name, 'test')

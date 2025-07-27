from django.test import TestCase

from accounts.models import Account
from trees.models import PlantedTree, Tree
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.account = Account.objects.create(name="Test Account")

        self.tree1 = Tree.objects.create(name="Oak", scientific_name="Quercus robur")
        self.tree2 = Tree.objects.create(name="Maple", scientific_name="Acer saccharum")

        self.location1 = (-12.9714, -38.5014)
        self.location2 = (-13.0000, -38.5100)

    def test_user_can_plant_single_tree(self):
        planted_tree = self.user.plant_tree(self.tree1, self.location1, self.account)

        self.assertIsNotNone(planted_tree)
        self.assertEqual(planted_tree.user, self.user)
        self.assertEqual(planted_tree.tree, self.tree1)
        self.assertEqual(planted_tree.account, self.account)
        self.assertEqual(planted_tree.latitude, self.location1[0])
        self.assertEqual(planted_tree.longitude, self.location1[1])

    def test_user_can_plant_multiple_trees(self):
        trees_to_plant = [
            (self.tree1, self.location1, self.account),
            (self.tree2, self.location2, self.account),
        ]

        planted_trees = self.user.plant_trees(trees_to_plant)

        self.assertEqual(len(planted_trees), 2)

        for i, planted in enumerate(planted_trees):
            self.assertIsInstance(planted, PlantedTree)
            self.assertEqual(planted.user, self.user)
            self.assertEqual(planted.tree, trees_to_plant[i][0])
            self.assertEqual(planted.latitude, trees_to_plant[i][1][0])
            self.assertEqual(planted.longitude, trees_to_plant[i][1][1])
            self.assertEqual(planted.account, self.account)

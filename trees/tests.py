from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Account, UserAccount
from trees.models import Tree, PlantedTree
from users.models import User


class PlantedTreeTemplateTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.account1 = Account.objects.create(name="Conta A")
        self.account2 = Account.objects.create(name="Conta B")

        self.user1 = User.objects.create_user(username="user1", password="pass1")
        self.user2 = User.objects.create_user(username="user2", password="pass2")
        self.user3 = User.objects.create_user(username="user3", password="pass3")

        UserAccount.objects.create(user=self.user1, account=self.account1)
        UserAccount.objects.create(user=self.user2, account=self.account1)
        UserAccount.objects.create(user=self.user3, account=self.account2)

        self.tree = Tree.objects.create(name="Ipê", scientific_name="Handroanthus")

        PlantedTree.objects.create(
            user=self.user1,
            tree=self.tree,
            account=self.account1,
            latitude=-12.97,
            longitude=-38.51,
        )
        PlantedTree.objects.create(
            user=self.user2,
            tree=self.tree,
            account=self.account1,
            latitude=-12.96,
            longitude=-38.52,
        )
        PlantedTree.objects.create(
            user=self.user3,
            tree=self.tree,
            account=self.account2,
            latitude=-13.00,
            longitude=-38.50,
        )

    def test_user_can_view_own_planted_trees(self):
        self.client.login(username="user1", password="pass1")

        response = self.client.get(reverse("view_planted_trees"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trees/planted_trees.html")

        my_trees = response.context[-1]["my_trees"]
        self.assertEqual(my_trees.count(), 1)
        self.assertEqual(my_trees.first().user, self.user1)
        self.assertContains(response, "Ipê")

from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class Account(models.Model):
  """
  A model to represent an account in the system.
  """
  name = models.CharField(max_length=255)
  created = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name


class User(AbstractUser):
  """
  A custom user model that extends the AbstractUser model.
  """
  accounts = models.ManyToManyField(Account)

  groups = models.ManyToManyField(
        'auth.Group', 
        related_name='custom_user_set', 
        blank=True, 
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
  )
  user_permissions = models.ManyToManyField(
      'auth.Permission', 
      related_name='custom_user_set', 
      blank=True, 
      help_text='Specific permissions for this user.',
      verbose_name='user permissions',
  )

  def plant_tree(self, tree, location):
        """
        Plant a tree for the user.
        """
        PlantedTree.objects.create(
            user=self,
            tree=tree,
            location=location
        )

  def plant_trees(self, plants):
    """
    Plant multiple trees for the user.
    """
    for tree, location in plants:
      self.plant_tree(tree, location)


class Profile(models.Model):
  """
  A model to represent a user profile.
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  about = models.TextField(blank=True)
  joined = models.DateTimeField(auto_now_add=True)


class PlantedTree(models.Model):
    """
    A model to represent a tree planted by a user.
    """
    age = models.IntegerField(default=0)
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    from trees.models import Tree 
    
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tree.name} plantada por {self.user.username} em {self.planted_at}"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    related_words = models.TextField()
    user = models.ForeignKey(User)


class Movement(models.Model):
    description = models.CharField(max_length=150)
    amount = models.FloatField()
    balance = models.FloatField()
    date = models.DateField()
    user = models.ForeignKey(User)
    categories = models.ManyToManyField(Category)
    # def __unicode__(self):
    #     return self.description, self.amount, self.balance, self.date, self.user

    def tag_movement(self, description, user_categories):
        """
        :param description: movement description
        :param user_categories: list of categories by user
        :return: assigns movement to user categories
        """
        description_words = description.split(' ')
        movement_categories = []
        # TODO make this algorithm faster
        for c in user_categories:
            category_related_words = c.related_words.split(';')[:-1]
            for word in description_words:
                if word in category_related_words:
                    movement_categories.append(c)
                    break

        if len(movement_categories) > 0:
            self.categories = movement_categories

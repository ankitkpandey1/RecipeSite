from django.db import models
''' Image field needs installation of pillow '''

class User(models.Model):
    user_name=models.CharField(max_length=50 ,unique=True)
    user_password=models.CharField(max_length=16)
    user_mail=models.EmailField()
    def __str__(self):
        return self.user_name
    
    
class UserRecipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name=models.CharField(max_length=50,unique=True)
    recipe_description=models.CharField(max_length=500)
    recipe_ingredients=models.CharField(max_length=500)
    recipe_steps=models.CharField(max_length=2000)
    recipe_img=models.ImageField(upload_to='images/')
    recipe_publish=models.DateField()
    recipe_edit=models.DateField()
    def __str__(self):
        return self.recipe_name
    
''' 
    Experimental feature, couldn't be deployed due to time constrain.
    
    class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    userrecipe=models.ForeignKey(UserRecipe, on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=200)
    comment_date=models.DateField()
    
    '''
    
from django.db import models

class MainMenu(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self) :
        return self.title
    
class SubMenu(models.Model):
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self) :
        return self.title
    
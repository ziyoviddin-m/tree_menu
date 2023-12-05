from django.db import models



class MenuName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    named_url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    menu_name = models.ForeignKey(MenuName, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
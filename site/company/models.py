from django.db import models
# from django.conf import settings


class Category(models.Model):

    name = models.CharField(max_length=250,
                            verbose_name="Наименование категории")
    slug = models.CharField(max_length=250,
                            verbose_name="Наименование для ссылки")
    keuw = models.CharField(max_length=250, verbose_name="Ключевые слова",
                            blank=True, null=True)
    desk = models.CharField(max_length=250, verbose_name="Краткое описание",
                            blank=True, null=True)

    def get_url(self):
        return "/category/{}/".format(self.slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


def upload_to(instance, filename):
    return "{}/{}/{}".format(instance.category.slug, instance.slug, filename)


class Tovar(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование товара")

    slug = models.CharField(max_length=250,
                            verbose_name="Наименование для ссылки")
    keuw = models.CharField(max_length=250, verbose_name="Ключевые слова",
                            blank=True, null=True)
    desk = models.CharField(max_length=250, verbose_name="Краткое описание",
                            blank=True, null=True)
    cena = models.FloatField(blank=True, null=True, verbose_name="Цена")
    ed = models.CharField(max_length=50, verbose_name="Единицы измерения",
                          blank=True, null=True)
    dostavka = models.CharField(max_length=100, blank=True, null=True,
                                verbose_name="Доставка")
    img = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.ForeignKey(Category)

    def get_url(self):
        return "/category/{}/{}/".format(self.category.slug, self.slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Page(models.Model):

    name = models.CharField(max_length=50,
                            verbose_name="Наименование страницы")
    slug = models.CharField(max_length=50, verbose_name="Имя ссылки")
    desk = models.CharField(max_length=250, blank=True, null=True,
                            verbose_name="Краткое описание страницы")
    keyw = models.CharField(max_length=250, blank=True, null=True,
                            verbose_name="Ключевые слова")

    def __str__(self):
        return self.name

    def get_url(self):
        if self.slug == "index":
            return "/"
        return "/{}/".format( self.slug)

    class Meta():
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

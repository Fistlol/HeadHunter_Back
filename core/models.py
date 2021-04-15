from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='', max_length=1000)
    city = models.CharField(max_length=300)
    address = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }

    def __str__(self):
        return f'{self.id}: {self.name} | {self.city}'


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='', max_length=1000)
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,
                                related_name='vacancies')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }

    def __str__(self):
        return f'{self.id}: {self.name} | {self.salary}$'

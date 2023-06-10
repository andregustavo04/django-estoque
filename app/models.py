from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produtos(models.Model):
	GENDER = (
			('M', 'M'),
			('F', 'F'),
			('U', 'U'),
		)
	
	user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	produto = models.CharField(max_length=40)
	preco_compra = models.CharField(max_length=20)
	preco_venda = models.CharField(max_length=20)
	quantidade = models.CharField(max_length=10)
	genero = models.CharField(max_length=1, null=True, choices=GENDER)
	anotacao = models.TextField()
	criado_em = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.produto


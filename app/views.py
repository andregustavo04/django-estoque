from django.shortcuts import render, redirect
from app.models import Produtos
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Home
@login_required(login_url='login')
def home(request):

	current_user = request.user
	produtos = Produtos.objects.all().filter(user_fk=current_user).order_by('-criado_em')

	success = request.GET.get('success', False)
	edited = request.GET.get('edited', False)
	context = {'produtos':produtos, 'success':success, 'edited':edited}

	return render(request, 'home.html', context)


# Adicionar Produtos
@login_required(login_url='login')
def adicionar(request):
	if request.method == 'POST':
		if request.POST.get('produto') \
		and request.POST.get('preco_compra') \
		and request.POST.get('preco_venda') \
		and request.POST.get('quantidade') \
		and request.POST.get('genero') \
		and request.POST.get('anotacao'):
			novo_produto = Produtos(user_fk=request.user, produto=request.POST.get('produto'), preco_compra=request.POST.get('preco_compra'), preco_venda=request.POST.get('preco_venda'), quantidade=request.POST.get('quantidade'), genero=request.POST.get('genero'), anotacao=request.POST.get('anotacao'))
			# novo_produto.user = request.user
			# novo_produto.produto = request.POST.get('produto')
			# novo_produto.preco_compra = request.POST.get('preco_compra')
			# novo_produto.preco_venda = request.POST.get('preco_venda')
			# novo_produto.quantidade = request.POST.get('quantidade')
			# novo_produto.genero = request.POST.get('genero')
			# novo_produto.anotacao = request.POST.get('anotacao') 
			novo_produto.save()
			success = True
			return redirect(f'/?success={success}')
	else:
		return render(request, 'adicionar.html')

# Ver Produto Individualmente
@login_required(login_url='login')
def ver_produto(request, id):
	current_user = request.user
	produto = Produtos.objects.get(id = id, user_fk=current_user)

	if produto != None:
		context = {'produto':produto}
		return render(request, 'editar.html', context)

# Editar Produto
@login_required(login_url='login')
def editar_produto(request):
	if request.method == "POST":
		produto = Produtos.objects.get(id = request.POST.get('id'))
		if produto != None:
			produto.produto = request.POST.get('produto')
			produto.preco_compra = request.POST.get('preco_compra')
			produto.preco_venda = request.POST.get('preco_venda')
			produto.quantidade = request.POST.get('quantidade')
			produto.genero = request.POST.get('genero')
			produto.anotacao = request.POST.get('anotacao') 
			produto.save()
			edited = True

			return redirect(f'/?edited={edited}')

# Deletar Produto
@login_required(login_url='login')
def deletar_produto(request, id):
	produto = Produtos.objects.get(id = id)
	produto.delete()
	return HttpResponseRedirect('/')


# Login
def loginUser(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('home')

	return render(request, 'login.html')


# Register
def registerUser(request):
	# form = CustomUserCreationForm()

	# if request.method == "POST":
	# 	print("REGISTER METHOD POST")
	# 	form = CustomUserCreationForm(request.POST)
	# 	if form.is_valid():
	# 		user = form.save(commit=False)
	# 		user.save()
	# 		print(user)
	# 		if user is not None:
	# 			login(request, user)
	# 			return redirect('home')
	# 	else:
	# 		print(form.errors)

	# context = {'form':form}
	# return render(request, 'register.html', context)

	if request.user.is_authenticated:
		return redirect('home')

	if request.method == "POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		password_confirm = request.POST.get('password_confirm')

		if password != password_confirm:
			error = True
			context = {'error':error}
			return render(request, 'register.html', context)

		new_user = User.objects.create_user(username, email, password)
		if new_user is not None:
			new_user.save()
			login(request, new_user)
			return redirect('home')

	return render(request, 'register.html')


# Logout
@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import RegistrationForm, ClothForm
from .models import Clothes, Category
from django.shortcuts import get_object_or_404



class MainView(View):
    def get(self, request):
        return render(request, 'outfit/base.html')


class All_ClothesView(View):
    def get(self, request):
        try:
            all_clothes = Clothes.objects.all()


            response = [
                {
                    'id': cloth.id,
                    'name': cloth.name,
                    'category': cloth.category.name,
                } for cloth in all_clothes
            ]

            return render(request, 'outfit/all_clothes.html', {'response': response})

        except Exception as e:
            return JsonResponse(data={"error": str(e)}, status=500)


class ClothView(View):
    def get(self, request, id):
        try:
            cloth = get_object_or_404(Clothes, id=id)
            return render(request, 'outfit/cloth.html', {'cloth': cloth})
        except Exception as e:
            return JsonResponse(data={"error": str(e)}, status=500)


class CategoriesView(View):
    def get(self, request):
        try:
            categories = Category.objects.all()
            response = [
                {
                    'id': category.id,
                    'name': category.name,
                } for category in categories
            ]
            return render(request, 'outfit/categories.html', {'response': response})
        except Exception as e:
            return JsonResponse(data={"error": str(e)}, status=500)


class ClothesOfCategoryView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            clothes = Clothes.objects.filter(category=category)
            response = [
                {'name': clothes.name} for clothes in clothes
            ]
            return render(request, 'outfit/category.html', {'response': response})
        except Category.DoesNotExist:
            return JsonResponse(data={"error": "Category does not exist"}, status=500)
        except Exception as e:
            return JsonResponse(data={"error": str(e)}, status=500)


class AboutUs(View):
    def get(self, request):
        return render(request, 'outfit/about.html')


@login_required
def profile(request):
    return render(request, 'outfit/profile.html', {'user': request.user})


@login_required
def add_cloth(request):
    if request.method == 'POST':
        form = ClothForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('clothes')
    else:
        form = ClothForm()
    return render(request, 'outfit/add_cloth.html', {'form': form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'outfit/change_password.html'
    success_url = reverse_lazy('profile')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('MainPage')
    else:
        form = RegistrationForm()
    return render(request, 'outfit/register.html', {'form': form})


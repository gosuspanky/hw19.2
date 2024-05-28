from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Category, Blog, Version


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Доступные категории товаров'
    }


class ContactPageView(TemplateView):
    template_name = "catalog/contacts.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            print(f'Имя - {name}\n'
                  f'Телефон - {phone}\n'
                  f'Сообщение: {message}')
        return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data = super().get_context_data(*args, **kwargs)

        for product in self.object_list:
            versions = Version.objects.filter(product_name=product)
            active_versions = versions.filter(is_active_version=True)
            if active_versions:
                product.name_version = active_versions.last().version_name
                product.number_version = active_versions.last().version_num
        context_data['object_list'] = self.object_list

        context_data['title'] = f'Категория: {category_item.name}'
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {
        'title': 'Описание продукта'
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def _get_version_formset(self):
        version_formset = inlineformset_factory(
            parent_model=self.model,
            model=Version,
            form=VersionForm,
            extra=1
        )

        if self.request.method == 'POST':
            return version_formset(self.request.POST, instance=self.object)
        else:
            return version_formset(instance=self.object)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['formset'] = self._get_version_formset()
        return context_data

    def form_valid(self, form: ProductForm):

        context = self.get_context_data()
        versions_formset = context.get('formset')

        self.object = form.save()

        if versions_formset and versions_formset.is_valid():
            versions_formset.instance = self.object
            versions_formset.save()

        return super().form_valid(form)

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner:
    #         return ProductForm
    #     if user.has_perm('catalog.can_unpublish_product') and user.has_perm(
    #             'catalog.can_edit_description_product') and user.has_perm('catalog.can_edit_category_product'):
    #         return ProductModeratorForm
    #     raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content', 'is_published')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'is_published')

    # success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

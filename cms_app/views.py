from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Page, Category

def home(request):
    """Homepage - show all published pages"""
    pages = Page.objects.filter(is_published=True)
    categories = Category.objects.all()  # Add this line
    return render(request, 'cms_app/home.html', {
        'pages': pages,
        'categories': categories  # Add this
    })

def page_detail(request, page_id):
    """Show single page details"""
    page = get_object_or_404(Page, id=page_id, is_published=True)
    return render(request, 'cms_app/page_detail.html', {'page': page})

@login_required
def create_page(request):
    """Simple page creation form"""
    categories = Category.objects.all()
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        
        category = Category.objects.get(id=category_id)
        Page.objects.create(
            title=title,
            content=content,
            category=category,
            author=request.user
        )
        return redirect('home')
    
    return render(request, 'cms_app/page_form.html', {'categories': categories})

@login_required
def admin_dash(request):
    """Simple admin dashboard"""
    user_pages = Page.objects.filter(author=request.user)
    return render(request, 'cms_app/admin_dash.html', {'pages': user_pages})

def category_pages(request, category_id):
    """Show pages by category"""
    category = get_object_or_404(Category, id=category_id)
    pages = Page.objects.filter(category=category, is_published=True)
    categories = Category.objects.all()  # Add this
    return render(request, 'cms_app/home.html', {
        'pages': pages, 
        'category': category,
        'categories': categories  # Add this
    })
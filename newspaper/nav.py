from newspaper.models import Category, Post, Tag

def navigation(request):
    trending_posts = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-views_count")[:5]

    categories = Category.objects.all()[:3]
    side_categories = Category.objects.all()[:6]
    tags = Tag.objects.all()[:12]
    return {
        "trending_posts": trending_posts,
        "categories": categories,
        "side_categories": side_categories,
        "tags": tags,
    }
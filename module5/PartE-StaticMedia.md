# Part E – Enabling Static Files and Uploaded Files

This section explains the updates made to support user-uploaded images and ensure that static and media files work correctly in the Django blog.

## 1) Update the Post Form to accept images

The post form template was updated to include the correct encoding type so browsers can send files:

    <form method="post" enctype="multipart/form-data" novalidate>

This allows Django to receive an uploaded image along with the other form fields.

## 2) Update templates to display uploaded images

Uploaded images now render where posts are shown.

### a) Post list results (thumbnail)

A small thumbnail appears for each post in the list:

    {% if post.image %}
      <img src="{{ post.image.url }}" alt="{{ post.title }}"
           style="width:100px; height:100px; object-fit:cover;" />
    {% endif %}

### b) Post detail (full width)

A larger image is shown on the post detail page:

    {% if post.image %}
      <img src="{{ post.image.url }}" alt="{{ post.title }}"
           style="max-width:100%; height:auto; margin-bottom:12px;" />
    {% endif %}

## 3) MEDIA configuration (settings and urls)

`settings.py` defines where uploaded files are stored and how they are referenced:

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

During development, `urls.py` serves uploaded files:

    from django.conf import settings
    from django.conf.urls.static import static

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## 4) Summary

- The post form accepts image uploads via `enctype="multipart/form-data"`.
- Images render in the list view (thumbnail) and the detail view (full width).
- `MEDIA_URL` and `MEDIA_ROOT` are configured, and media files are served in development.

This satisfies the requirement to “update your posts to accept and render uploaded images.”

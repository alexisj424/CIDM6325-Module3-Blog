# CIDM 6325 – Module 3: Django Blog

This repo contains my Module 3 deliverables. The running app is a simple Blog built with Django.

## What’s implemented (Feature Set 1 – 40pts)

- **Auth**: Django login/logout and @login_required guards.
- **Two related models with full CRUD**:
  - `Post` (author -> User, title, body, timestamps, is_published)
  - `Comment` (post -> Post, author -> User, text, timestamps)
- **Workflow**:
  - Only logged-in users can create posts/comments
  - Only the **post author or a staff user** can edit/delete a post
- **Bootstrap styling** for clean UI
- **Custom validation** (Part A): `PostForm.clean_title()` enforces a simple business rule
- **Accessibility notes** (WCAG 2.2): see `docs/ACCESSIBILITY.md`
- **Role-based permissions**: documented below
- **CI demo**: GitHub Actions runs Django checks on every push (`.github/workflows/ci.yml`)

## Run locally

bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
## Key folders
blog/                 - app: models, views, forms, urls, templates/blog/*
blogproject/          - project settings and root urls
templates/blog/       - base.html, post_list.html, post_detail.html, post_form.html, registration/login.html

## Role-based permissions
- Create post/comment: any authenticated user  
- Edit/Delete post: only the post author or staff (request.user.is_staff)  
- View posts: anyone (only published posts are listed)

## Schema (ER Diagram)
USER (1) ----< POST (many)
POST (1) ----< COMMENT (many)
USER (1) ----< COMMENT (many)

Entities:
- USER: id (PK), username
- POST: id (PK), author_id (FK to User), title, body, is_published, created_at, updated_at
- COMMENT: id (PK), post_id (FK to Post), author_id (FK to User), text, created_at

## Deliverables Map
Part | Requirement | Where Implemented
---- | ------------ | ----------------
A | Forms & Validation | blog/forms.py (clean_title method)
B | Multi-Model Design | Post ↔ Comment (models.py + migrations)
C | AI Reflection | docs/AI_REFLECTION.md
D | Peer Review | docs/PEER_REVIEW.md
E | Journey Critique | docs/JOURNEY_CRITIQUE.md

## Accessibility Notes (WCAG 2.2)
Accessibility compliance is documented in docs/ACCESSIBILITY.md

Highlights:
- Proper labels on form inputs
- Bootstrap ensures good color contrast
- Logical heading structure
- Buttons accessible via keyboard

## CI/CD Pipeline
A lightweight GitHub Actions workflow runs automated checks:

- Django deploy safety check  
- Migration dry-run validation

Example workflow file: `.github/workflows/ci.yml`

## Credits
Created by **Alexis Jayde Lopez**  
CIDM 6325 – Module 3 (West Texas A&M University, Fall 2025)  
Instructor: *Dr. Griffin*

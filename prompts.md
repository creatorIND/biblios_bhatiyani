# AI Prompts Documentation - Biblios Project

## Project Setup Phase

### Prompt 1: Initial Django Project Setup

**Tool**: Claude
**Purpose**: Set up Django project with virtual environment for book reading tracker
**Query**: "let's start again the first task.... since i don't have experience in django... you have to give me more details as to why we are doing what we are doing"
**Result**: Comprehensive beginner-friendly guide explaining Django concepts, virtual environments, and each package's purpose

### Prompt 2: Django Configuration Review

**Tool**: Claude  
**Purpose**: Review and validate Django configuration files
**Query**: "check these files again: asgi.py, settings.py, urls.py, wsgi.py, manage.py - if these are correct i'll commit"
**Result**: Confirmed configuration was correct, noted Django 5.2.5 usage, and identified completion of multiple tasks

### Prompt 3: Tasks Management in Monday.com

**Tool**: Claude
**Purpose**: Update task tracking workflow
**Query**: "i've moved back the first task to not started... from now onwards... when i say to start a task... move that to in progress... when i complete that task... i'll move it manually to completed"
**Result**: Established task management workflow - Claude moves tasks to "In Progress", user marks as "Completed"

### Prompt 4: Create Django Apps with Models

**Tool**: Claude
**Purpose**: Create books, accounts, and stats apps with proper structure
**Query**: "ok, let's start the next task, move it in progress and start"
**Result**: Created three Django apps with custom User model, Book model, and organized API structure

### Prompt 5: Align with Project Requirements

**Tool**: Claude
**Purpose**: Ensure apps and models match exact project specifications
**Query**: "from our previous chat, we finalised project requirements... here are they [provided requirements document]"
**Result**: Updated models and structure to match exact requirements (email/username auth, book fields, status choices, genres)

## Debugging Phase

### Prompt 6: Fix Migration History Error

**Tool**: Claude
**Purpose**: Resolve Django migration conflict with custom User model
**Query**: "I'm getting this error: django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency accounts.0001_initial"
**Result**: Provided solution to reset database and recreate migrations in correct order

### Prompt 7: Fix Book Model TypeError

**Tool**: Claude
**Purpose**: Fix NoneType comparison error in Book model
**Query**: "ok migration was successful and i ran the server... but when i click on add, i get this error: TypeError at /admin/books/book/add/ '>' not supported between instances of 'NoneType' and 'int'"
**Result**: Fixed Book model save method and properties with proper null checks

### Prompt 8: Fix User Admin Add Error

**Tool**: Claude
**Purpose**: Fix User admin form error in Django 5.2
**Query**: "ok it's working... but when trying to add a user, i get this error: TypeError at /admin/accounts/user/add/ cannot unpack non-iterable NoneType object"
**Result**: Fixed User admin configuration by properly extending BaseUserAdmin

### Prompt 9: Clarify Authentication Method

**Tool**: Claude
**Purpose**: Correct authentication approach to use username instead of email
**Query**: "you're doing the same mistake again... remember i'm now not using email as username as it was giving error... email will be there, but username will be used as login method"
**Result**: Updated User model and admin to use standard Django username authentication

### Prompt 10: Final User Admin Fix

**Tool**: Claude
**Purpose**: Fix persistent User admin error in Django 5.2
**Query**: "i can see the user list and existing user details, but when i click on add user... i get this error: TypeError at /admin/accounts/user/add/"
**Result**: Fixed by extending BaseUserAdmin fieldsets instead of replacing them

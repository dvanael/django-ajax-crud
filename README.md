# DJANGO CLASS BASED VIEWS FOR AJAX CRUD

Access the [Brazilian Portuguese Documentation](docs/README_pt-br.md).

This repository was created to address the difficulty of creating Django Function Based Views for CRUD (Create, Read, Update, Delete) operations with AJAX.

It provides mixins and views built with JsonResponse that can be processed by AJAX requests, enabling the integration of dynamic pages into web applications.

---

**Features:**
- **AJAX Mixins:** Easily add AJAX to class-based views.

- **AJAX Views:** Ready-to-use views for CRUD.

- **Simple Integration:** Designed for easy setup and use in any Django project.

- **Documentation:** Includes setup and usage instructions.

---

**Get Started:** Clone the repository and follow the documentation to add AJAX CRUD to your Django project. 

## HOW TO USE
To incorporate these classes into your Django project, follow these steps:

### Basic Configuration

Ensure that you have **jQuery** and **Bootstrap 5** included in your `base.html` file.

**base.html**
```html
<head>
  <!-- CSS  -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

  <!-- JS LIB  -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
</head>
```
---

Alternatively, you can add a script block in your `base.html`:

```html
<body>
  ...
</body>

{% block script %}{% endblock script %}
```

### Adding Files

Copy the following files of this repository into your project:
- ``app/mixin.py``: Contains the mixins from class working.

- `app/ajax.py`: Contains the classes with JsonResponse.

- `static/js/event.js`: Contains AJAX operations for CRUD, pagination, and filtering.

## LIST VIEW

### Add AjaxListView in views.py 

Utilize a model that you've defined in your project.

In `ModelList`, we define the model, template, and partial template for listing objects. 

**views.py**
```python
from .models import Model
from .ajax import AjaxListView

class ModelList(AjaxListView):
    model = Model
    template_name = 'model/model-list.html'
    partial_list = 'partials/model/list.html'
```

### Add ModelList in urls.py

In `urls.py`, create paths using the list view you've created.

Define a descriptive path name to avoid conflicts.

**urls.py**
```python
from django.urls import path
from .views import *

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
]
```

### Creating Model List Template

Create `model/model-list.html` in your `templates` directory.

Add a table with the `id="partial-table"`, and include the partial list in the tbody.

Include the `event.js` script, and don't forget to use `{% load static %}` for it to work properly.

**model-list.html**
```html
{% load static %}
<!-- Table for rendering objects -->
<table id="partial-table" class="table">
  <tbody>
      {% include "partials/model/list.html" %}
  </tbody>
</table>

<!-- Include event.js in this template -->
{% block script %}
<script src="{% static 'js/event.js' %}"></script>
{% endblock script %}
```

### Creating Model Partial List

Create `partials/model/list.html` in your `templates` directory.

Use a loop `object_list` and display the object attributes.

**list.html**
```html
{% for object in object_list %}
  <tr>
<!-- Add object attributes -->
    <th>{{object.name}}</th>
  </tr>
{% endfor %}
```

## CREATE VIEW 

### Add AjaxCreateView in views.py

Utilize a model and form that you've defined in your project.

**views.py**
```python
from .models import Model
from .forms import ModelForm
from .ajax import AJaxCreateView

class ModelCreate(AjaxCreateView):
    model = Model
    form_class = ModelForm
    template_name = 'partials/model/create.html'
    partial_list = 'partials/model/list.html'
```

### Add ModelCreate in urls.py

In `urls.py`, create paths using the list view you've created.

Define a descriptive path name to avoid conflicts.

**urls.py**
```python
from django.urls import path
from .views import ModelList, ModelCreate

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
  path('js/create/model/', ModelCreate.as_view(), name='js-create-model'),
]
```

### Add Modal Form and Create Button

In the **list template**, add a modal with the `id="model-form"`. 

Include a button with the class `.js-create`, which is used to create a new object.

Add a `data-url` attribute with your create URL; this will call your `AjaxCreateView`.

Make sure that the `event.js` script has been added in template, and don't forget to use `{% load static %}` for it to work properly.

**model-list.html**
```html
<!-- Modal for CRUD operation forms -->
<div id="modal-form" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      
    </div>
  </div>
</div>

<!-- Button to open create form -->
<button class="js-create btn btn-success" type="button" data-url="{% url 'js-create-model' %}">New model</button>
```

### Create a Form Template
Under `templates/partials/model/`, add `create.html`.

These template will contain a form with `method="post"`, an `action` pointing to the URL corresponding to the view, and the class `.js-create-form` for referencing this form in `event.js`.

**create.html**
```html
<form method="post" action="{% url 'js-create-model' %}" class="js-create-form">
  {% csrf_token %}

  <div class="modal-header">
    <h4 class="modal-title">New model</h4>
    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
  </div>

  <div class="modal-body">
    {{ form.as_p }}
  </div>

  <div class="modal-footer">
    <button type="submit" class="btn btn-success">Create</button>
    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
  </div>
</form>
```

## UPDATE VIEW 

### Add AjaxUpdateView in views.py

Utilize a model and form that you've defined in your project.

**views.py**
```python
from .models import Model
from .forms import ModelForm
from .ajax import AjaxUpdateView

class ModelUpdate(AjaxUpdateView):
    model = Model
    form_class = ModelForm
    template_name = 'partials/model/update.html'
    partial_list = 'partials/model/list.html'
```

### Add ModelUpdate in urls.py

In `urls.py`, create paths using the update view you've created.

Remember that update views require the primary key.

Define a descriptive path name to avoid conflicts.

**urls.py**
```python
from django.urls import path
from .views import *

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
  path('js/update/<int:pk>/model/', ModelUpdate.as_view(), name='js-update-model'),
]
```

### Add Modal and Update Button

Make sure that you have a ``modal-form`` in the **list template**.

Also, check that the `event.js` script has been added in template, and don't forget to use `{% load static %}` for it to work properly.

**model-list.html**
```html
<!-- Modal for CRUD operation forms -->
<div id="modal-form" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      
    </div>
  </div>
</div>
```

In the **partial list template**, include update button with `.js-update` class.

Add a `data-url` attribute with your **update URL**, referencing `object.pk`.

**list.html**
```html
{% for object in object_list %}
  <tr>
<!-- Add object attributes -->
    <th>{{object.name}}</th>

<!-- Options Buttons -->
    <th>
      <button class="js-update btn btn-secondary" data-url="{% url 'js-update-model' object.pk %}">Edit</button>
    </th>
  </tr>
{% endfor %}
```

### Create a Update Form Template

Under `templates/partials/model/`, add `update.html`

These template will contain a form with `method="post"`, an `action` pointing to the URL corresponding to the view with ``form.instance.pk``, and the``.js-update-form`` class for referencing this form in `event.js`.

**update.html**
```html
<form method="post" action="{% url 'js-update-model' form.instance.pk %}" class="js-update-form">
  {% csrf_token %}

  <div class="modal-header">
      <h4 class="modal-title">Update Model</h4>
      <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
  </div>

  <div class="modal-body">
      <h3>{{form.instance}}</h3>  
      <p class='lead'>Fill in all required fields.</p>
      {{ form.as_p }}
  </div>

  <div class="modal-footer">
      <button type="submit" class="btn btn-primary">Save</button>
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
  </div>
</form>
```

## DELETE VIEW 

### Add AjaxDeleteView in views.py

Utilize a model that you've defined in your project.

```python
from .models import Model
from .forms import ModelForm
from .ajax import AjaxDeleteView

class ModelDelete(AjaxDeleteView):
    model = Model
    template_name = 'partials/model/delete.html'
    partial_list = 'partials/model/list.html'
```

### Add ModelDelete in urls.py

In `urls.py`, create paths using the delete view you've created.

Remember that delete views require the primary key.

Define a descriptive path name to avoid conflicts.

**urls.py**
```python
from django.urls import path
from .views import ModelList, ModelDelete

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
  path('js/delete/<int:pk>/model/', ModelDelete.as_view(), name='js-delete-model'),
]
```
### Add Modal and Delete Button
Make sure that you have a ``modal-form`` in the **list template**.

Also, check that the `event.js` script has been added in template, and don't forget to use `{% load static %}` for it to work properly.

**model-list.html**
```html
<!-- Modal for CRUD operation forms -->
<div id="modal-form" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      
    </div>
  </div>
</div>
```
In the **partial list template**, include delte button with `.js-delete` class.

Add a `data-url` attribute with your **delete URL**, referencing `object.pk`.

**list.html**
```html
{% for object in object_list %}
  <tr>
<!-- Add object attributes -->
    <th>{{object.name}}</th>

<!-- Options Buttons -->
    <th>
      <button class="js-delete btn btn-secondary" data-url="{% url 'js-delete-model' object.pk %}">Delete</button>
    </th>
  </tr>
{% endfor %}
```

### Create a Delete Form Template
Under `templates/partials/model/`, add `delete.html`

These template will contain a form with `method="post"`, an `action` pointing to the URL corresponding to the view with ``object.pk``, and the``.js-delete-form`` class for referencing this form in `event.js`.

**delete.html**
```html
<form method="post" action="{% url 'js-delete-model' object.pk %}" class="js-delete-form">
  {% csrf_token %}

  <div class="modal-header">
      <h4 class="modal-title">Delete model</h4>
      <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
  </div>

  <div class="modal-body">
      <p>Delete the: <strong>{{ object }}</strong>?</p>
  </div>        

  <div class="modal-footer">
      <button type="submit" class="btn btn-danger">Delete</button>
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
  </div>
</form>
```

## USING MODEL MIXIN
If you don't wanna repeat all the varibles on classes, you can create a ``ModelMixin``, and add before the class view.

> **ATTENTION**: This is highly recommended to use.

```python
class ModelMixin:
    model = Model
    partial_list = 'partials/model/list.html'

# Views with Mixin example
class ModelList(ModelMixin, AjaxListView):
    template_name = 'model/model-list.html'

class ModelCreate(ModelMixin, AjaxCreateView):
    form_class = ModelForm
    template_name = 'partials/model/create.html'
  
class ModelUpdate(ModelMixin, AjaxUpdateView):
    form_class = ModelForm
    template_name = 'partials/model/update.html'

class ModelDelete(ModelMixin, AjaxDeleteView):
    template_name = 'partials/model/delete.html'
```
---
# DJANGO CLASS BASED VIEWS PARA CRUD COM AJAX

Este repositório é foi feito com base no problema de dificuldade na criação de Function Based Views do Django para o uso de CRUD's (Criar, Ler, Atualizar, Deletar) com AJAX. 

Neste repositório possui mixins e views criadas com JsonResponse que podem ser processadas por requisições AJAX, permitindo a integração de páginas dinamicas em uma aplicações web. 

---

**Recursos:**
- **Mixins AJAX:** Funções AJAX que são facilmente adicionadas em Class Based Views.

- **AJAX Views:** Views prontas para uso de CRUD's.

- **Integração Simples:** Projetado para uma configuração e uso simples em qualquer projeto Django.

- **Documentação:** Instruções completas de configuração e uso.

---

**Começando:** Clone o repositório e siga a documentação para incorporar funcionalidades CRUD AJAX ao seu projeto Django.

## COMO USAR

Para utilizar estas classes no seu projeto Django, siga estes passos:

### Configuração Básica

Certifique-se de incluir **jQuery** e **Bootstrap 5** no seu arquivo `base.html`. 

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
Alternativamente, você pode adicionar um bloco de script no seu `base.html`.

```html
<body>
  ...
</body>

{% block script %}{% endblock script %}
```

### Adicionando Arquivos

Copie os seguintes arquivos deste repositório para o seu projeto:
- `app/mixin.py`: Contém os mixins para funcionalidade de classe.

- `app/ajax.py`: Inclui classes com JsonResponse.

- `static/js/event.js`: Contém operações AJAX para CRUD, paginação e filtragem.

## LIST VIEW

### Adicione AjaxListView em views.py

Utilize um modelo definido no seu projeto. Em `ModelList`, defina o modelo, template e template parcial para listagem de objetos.

**views.py**
```python
from .models import Model
from .ajax import AjaxListView

class ModelList(AjaxListView):
    model = Model
    template_name = 'model/model-list.html'
    partial_list = 'partials/model/list.html'
```

### Adicione ModelList em urls.py

Crie caminhos usando a list view que você criou em `urls.py`, assegurando nomes de caminhos descritivos para evitar conflitos.

**urls.py**
```python
from django.urls import path
from .views import *

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
]
```

### Criando Template de ModelList

Crie `model/model-list.html` no seu diretório `templates`.

Adicione uma tabela com `id="partial-table"`, e inclua a lista parcial no tbody. 
 
Inclua o script `event.js` e utilize `{% load static %}` para funcionamento adequado.

**model-list.html**
```html
{% load static %}
<!-- Tabela para renderizar os objetos -->
<table id="partial-table" class="table">
  <tbody>
      {% include "partials/model/list.html" %}
  </tbody>
</table>

<!-- Inclua event.js no template -->
{% block script %}
<script src="{% static 'js/event.js' %}"></script>
{% endblock script %}
```

### Criando Parcial List de Model

Crie `partials/model/list.html` no seu diretório `templates`. 

Use um loop de `object_list` e exibir os atributos do objeto.

**list.html**
```html
{% for object in object_list %}
  <tr>
<!-- Adicione os atributos dos objetos -->
    <th>{{object.name}}</th>
  </tr>
{% endfor %}
```

## CREATE VIEW

### Adicione AjaxCreateView em views.py

Utilize um modelo e formulário definidos no seu projeto.

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

### Adicione ModelCreate em urls.py

Crie caminhos usando a view de criação que você definiu em `urls.py`, assegurando nomes de caminhos descritivos.

**urls.py**
```python
from django.urls import path
from .views import ModelList, ModelCreate

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
  path('js/create/model/', ModelCreate.as_view(), name='js-create-model'),
]
```

### Adicione o Modal e Botão de Create

No template de lista, adicione um modal com `id="model-form"`, e inclua um botão com a classe `.js-create` para criar um novo objeto. 

Adicione um atributo `data-url` com a sua URL de criação. 

Certifique-se de que o script `event.js` está adicionado e use `{% load static %}` para funcionamento adequado.

**model-list.html**
```html
<!-- Modal para operações do CRUD -->
<div id="modal-form" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      
    </div>
  </div>
</div>

<!-- Botão para abrir o Create Form -->
<button class="js-create btn btn-success" type="button" data-url="{% url 'js-create-model' %}">New model</button>
```

### Crie um Template de Formulário

Em `templates/partials/model/`, adicione `create.html` 

Esse template deve conter um formulário com `method="post"` e uma `action` apontando para a URL correspondente à view. 

Adicione a classe `.js-create-form` para referenciar este formulário em `event.js`.

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

### Adicione AjaxUpdateView em views.py

Utilize um modelo e formulário definidos no seu projeto.

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

### Adicione ModelUpdate em urls.py

Crie caminhos usando a view de atualização que você definiu em `urls.py`, assegurando nomes de caminhos descritivos.

**urls.py**
```python
from django.urls import path
from .views import *

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
  path('js/update/<int:pk>/model/', ModelUpdate.as_view(), name='js-update-model'),
]
```

### Adicione o Modal e Botão de Update

Certifique-se de que um `modal-form` está no template de lista. 

Certifique-se de que o script `event.js` está adicionado e use `{% load static %}`.

**model-list.html**
```html
<!-- Modal para operações do CRUD -->
<div id="modal-form" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      
    </div>
  </div>
</div>
```

Inclua um botão de atualização com a classe `.js-update` no template de lista parcial. 

Adicione um atributo `data-url` com a sua URL de atualização, referenciando `object.pk`. 

**list.html**
```html
{% for object in object_list %}
  <tr>
<!-- Adicione os atributos dos objetos -->
    <th>{{object.name}}</th>

<!-- Botões de Opções -->
    <th>
      <button class="js-update btn btn-secondary" data-url="{% url 'js-update-model' object.pk %}">Edit</button>
    </th>
  </tr>
{% endfor %}
```

### Crie um Template de Formulário Update

Em `templates/partials/model/`, adicione `update.html`.

Esse template deve conter um formulário com `method="post"` e uma `action` apontando para a URL correspondente à view com `form.instance.pk`. 

Adicione a classe `.js-update-form` para referenciar este formulário em `event.js`.

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

### Adicione AjaxDeleteView em views.py

Utilize um modelo definido no seu projeto.

```python
from .models import Model
from .forms import ModelForm
from .ajax import AjaxDeleteView

class ModelDelete(AjaxDeleteView):
    model = Model
    template_name = 'partials/model/delete.html'
    partial_list = 'partials/model/list.html'
```

### Adicione DeleteView em urls.py

Crie caminhos usando a view de deleção que você definiu em `urls.py`, assegurando nomes de caminhos descritivos.

**urls.py**
```python
from django.urls import path
from .views import ModelList, ModelDelete

urlpatterns = [
  path('models/', ModelList.as_view(), name='model-list'),
  path('js/delete/<int:pk>/model/', ModelDelete.as_view(), name='js-delete-model'),
]
```

### Adicione o Modal e Botão de Delete

Certifique-se de que um `modal-form` está no template de lista. 

Certifique-se de que o script `event.js` está adicionado e use `{% load static %}`.

**model-list.html**
```html
<!-- Modal para operações do CRUDs -->
<div id="modal-form" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      
    </div>
  </div>
</div>
```

Inclua um botão de deleção com a classe `.js-delete` no template de lista parcial. 

Adicione um atributo `data-url` com a sua URL de deleção, referenciando `object.pk`. 

**list.html**
```html
{% for object in object_list %}
  <tr>
<!-- Adicione os atributos dos objetos -->
    <th>{{object.name}}</th>

<!-- Botões de Opções -->
    <th>
      <button class="js-delete btn btn-secondary" data-url="{% url 'js-delete-model' object.pk %}">Delete</button>
    </th>
  </tr>
{% endfor %}
```

### Crie um Template de Formulário Delete

Em `templates/partials/model/`, adicione `delete.html`.

Esse template deve conter um formulário com `method="post"` e uma `action` apontando para a URL correspondente à view com `object.pk`. 

Adicione a classe `.js-delete-form` para referenciar este formulário em `event.js`.

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

## USANDO MIXIN DE MODELO

Para evitar repetir variáveis em classes, crie um `ModelMixin` e adicione-o antes da view da classe.

> **ATENÇÃO**: Isso é altamente recomendado.

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
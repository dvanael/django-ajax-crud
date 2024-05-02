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

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

{% extends 'layouts/main.html' %}
{% block content %}
  <h1>Something's wrong!</h1>
  <p>Fortunately we are on the job, and you can just return home!</p>
  <p><a href="{{url_for('index')}}">Back</a></p>
{% endblock %}
Using Django with Webix UI
===========================

Initialization
--------------

```
python manage.py migrate
python manage.py loaddata film
python manage.py loaddata runserver
```

Open http://localhost:8000/datatable in a browser


How it works
--------------

Server side code defines a simple REST handler, which outputs data from related model and process changes (datatable/views.py:data)

For data fetching handler returns an array of objects. For data saving handler returns a JSON object which can contain a new record id ( useful for insert operations ) or any other custom properties. 

#### CSRF

Client side code need to have the next block of a code to provide correct CSRF headers

```html
{% csrf_token %}
<script type="text/javascript">
	webix.attachEvent("onBeforeAjax", function(mode, url, data, xhr, headers){
		var key = document.querySelector("[name=csrfmiddlewaretoken]").value;
		headers["X-CSRFToken"] = key;
	});
</script>
```

License
---------

MIT
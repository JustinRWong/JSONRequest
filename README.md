# [JSONRequest](https://pypi.org/project/jsonrequest/)
Lightweight wrapper for requests library that only supports Content-Type: application/json.

This only supports `GET`, `POST`, `PATCH`, and `DELETE` http(s) request methods.

## How to Use

First, install the package
```bash
pip install jsonrequest
```

Then, you can use the package.
```python
>>> from jsonrequest.jsonrequest import RequestModel, make_request
>>> r = make_request(RequestModel(endpoint="", method='GET', url='https://google.com'))
>>> r
<Response [200]>
>>> 
```

## Note:
This data passed also only applies to `application/json` content.


Across multiple times over the past many years in my python projects, I found this codeblock repeated whenever I tried to make various http(s) requests using the requests library and thought it'd be much simpler to pass the method as a parameter instead of changing the function. [Here's a medium article](https://medium.com/@justinryanwong/creating-and-releasing-a-new-pypi-package-20218f316aef) of how I created this package as a result. Hope this helps and Happy coding :)

- by Justin
# [JSONRequest](https://pypi.org/project/jsonrequest/)
Lightweight wrapper for requests library that only supports Content-Type: application/json.

This only supports `GET`, `POST`, `PATCH`, and `DELETE` http(s) request methods.

## Note:
This data passed also only applies to `application/json` content.


Across multiple times over the past many years in my python projects, I found this codeblock repeated whenever I tried to make various http(s) requests using the requests library and thought it'd be much simpler to pass the method as a parameter instead of changing the function. I created this package as a result. Hope this helps and Happy coding :)

- by Justin
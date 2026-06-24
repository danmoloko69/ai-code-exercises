# Exercise: Contextual Learning with FastAPI

## Part 1: Framework Comparison

**Translation Table between concept in Flask to their FastAPI equivalents**

- Route decorator: for Flask is `@app.route('/x', methods=['GET'])`, for FastAPI `@app.get('/x')`, `@app.api_route('/x', methods=['GET','POST'])`

- Request object: for Flask is`from flask import request` for FastAPI is `from fastapi import Request` (Starlette `Request`)

- Response object: for Flask is `flask.Response` for fastAPI is `fastapi.Response`, `starlette.responses.*`

- Static files: for Flask is `send_from_directory()`,`app.static_folder` for FastAPI is `app.mount('/static', StaticFiles(directory='static'))`

- Config: for Flask is `app.config.from_object(...)` for FastAPI is `pydantic.BaseSettings`

- Before/after request hooks: for Flask is  `@app.before_request`, `@app.after_request`for FastAPI is`add_middleware()` or `@app.middleware('http')` for request/response hooks.

- Per-request state/context: for Flask is `flask.g` , `current_app`, for FastAPI is `request.state` or dependencies in FastAPI.

- Session handling: for Flask is`flask.session`, for FastAPI is `SessionMiddleware` + `request.session` (Starlette)

- Error handlers: for Flask is `@app.errorhandler(404)`, for FastAPI is `@app.exception_handler(HTTPException)` or raise `fastapi.HTTPException`

- URL building: for Flask is `url_for('endpoint')`, for FastAPI is `request.url_for('endpoint_name')`

- Background jobs/tasks: forFlask is external (Celery/RQ) or threading in Flask then ffor FastAPI is `BackgroundTasks` (built-in) or external task queues

- Startup/shutdown events: for Flask is `@app.before_first_request`, for FastAPI is `@app.on_event('startup')`, `@app.on_event('shutdown')`

- OpenAPI/docs generation: for Flask is external extensions (e.g., Flask-RESTX), for FastAPI is automatic OpenAPI + Swagger UI provided by FastAPI

- Testing helpers: for Flask is `app.test_client()`, for FastAPI is `TestClient` from `fastapi.testclient`

- Middleware ordering:for Flask is WSGI middleware or `@app.before_request` handlers, for FastAPI is ASGI middleware via `add_middleware()` with explicit order


## Part 2: Understanding Design Choices

- FastAPI use `pydantic` models for request and response data as it solves problem of parsing and using python annotations. Use `Depends` for clear dependency boundaries for database sessions. Orginize feature with `APIRouter`. Keep I/O-bound work in `asnc def` handlers when possible. Use startup and shutdown events for resources seettup and cleanup.

## Part 3: Applied Contextual Learning

**How does FastAPI’s approach to authentication compare to frameworks you’ve used before?**

- The token logic is implimented as reusable dependency function not just a middleware.

**What advantages does FastAPI’s dependency injection system provide for authentication?**

- Dependency allows laying authanthication cleanly through JWT. This avoids repeating tokens. 

**How does type hinting in FastAPI make security implementation clearer compared to other frameworks?**

- By documenting exactly what each step expects and returns.

**What patterns from other frameworks can you identify in the JWT implementation?**

- One way would be a token endpoint that authenticates credentials and issues.

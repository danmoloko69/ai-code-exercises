# Exercise: Understanding FastAPI Code Patterns

## Part 1: Analyzing Complex Code

**Create a clear understanding of the design patterns used in this code and why they might be beneficial**

- The use patterns in this codebase are Repository and Generic which are beneficial beacause they reduce duplication.

- With Dependency injection it makes authantication, database access and service reusable and testable.

- Role-based decorator keeps authorization separate from endpoint lgic and makes admin-only routes easy to declare. 


## Part 2: Tracing Execution Flow

**Create a step-by-step flowchart or sequence diagram of the request handling process.**

Client
  |
  v
FastAPI app
  |
  v
TimingMiddleware
  |
  v
Route match: GET /admin/users/
  |
  v
requires_role("admin") wrapper
  |
  v
get_current_user dependency
  |
  v
oauth2_scheme dependency
  |
  v
parse Authorization header -> token
  |
  v
get_db dependency
  |
  v
JWT decode & validate token
  |
  v
UserRepository.get_by_username(db, username)
  |
  v
return authenticated User
  |
  v
requires_role checks is_superuser
  |
  v
list_users route handler
  |
  v
user_repo.list(db, skip, limit)
  |
  v
return user list
  |
  v
TimingMiddleware adds X-Process-Time header
  |
  v
Response sent to client


## Part 3: Simplifying Complex Concepts

**Create a "translation guide" that explains advanced patterns in simpler terms.**

- Starting with `asynccountextmanager` is the helper that makes startup and shutdowns code easy to write, and `lifespan` is a function that runs once when the app starts and once when the app stops.

- `TimingMiddleware`is the code that runs on every request before the route gets it. It measures how long the request took. It adds that time to the response header as `X-Process-Time`.

- The have JWT Authentication Flow, its a compact token that proves a user is logged in. The app signs it so the app can trust it later. 


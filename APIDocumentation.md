# Exercise: Document a Python/Flask API

**Prompt 1: Endpoint Documentation Generation**

# API Documentation: User Registration Endpoint (Summary)

## Endpoint Overview
- **Route**: `POST /api/users/register`
- **Purpose**: Create new user account
- **Auth Required**: No
- **Content-Type**: `application/json`

---

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | String | Yes | Unique username (min 3 chars) |
| `email` | String | Yes | Valid email address (stored lowercase) |
| `password` | String | Yes | Password (min 8 characters) |

---

## Success Response (201 Created)

```json
{
  "message": "User registered successfully",
  "user": {
    "id": 123,
    "username": "johndoe",
    "email": "john@example.com",
    "created_at": "2024-06-15T10:30:45.123456",
    "role": "user"
  }
}
```

---

## Error Responses

| Status | Error | Cause | Message |
|--------|-------|-------|---------|
| 400 | Missing required field | Username/email/password missing | `{field} is required` |
| 400 | Invalid email | Email format invalid | Please provide a valid email address |
| 400 | Weak password | Password < 8 chars | Password must be at least 8 characters long |
| 409 | Username taken | Username exists | Username is already in use |
| 409 | Email exists | Email exists | An account with this email already exists |
| 500 | Server error | Database/system error | Failed to register user |

---

## Example Request

```bash
curl -X POST https://api.example.com/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "SecurePass123!"
  }'
```

---

## Example Response (Success)

```json
{
  "message": "User registered successfully",
  "user": {
    "id": 42,
    "username": "johndoe",
    "email": "john@example.com",
    "created_at": "2024-06-15T14:22:15.456789",
    "role": "user"
  }
}
```

---

## Example Response (Conflict - Email Exists)

```json
{
  "error": "Email exists",
  "message": "An account with this email already exists"
}
```

---

## Security Features

- **Password Hashing**: Uses secure hashing algorithm before storage
- **Duplicate Prevention**: Validates username and email uniqueness
- **Email Validation**: Pattern matching for valid email format
- **Password Strength**: Minimum 8 characters required
- **Case Normalization**: Email stored in lowercase
- **Error Masking**: Generic error messages prevent information disclosure

---

## Security Recommendations

1. Implement rate limiting: 5 requests per minute per IP
2. Use HTTPS for all requests
3. Enforce stronger passwords (12+ chars, mixed case, numbers, symbols)
4. Deploy CAPTCHA to prevent automated registration
5. Verify email before full account activation
6. Use Web Application Firewall (WAF)

---

## Rate Limiting (Recommended)

```
Per IP Address: 5 requests per minute
Per Username: 3 attempts per hour
Global: Monitor for unusual spikes
```

---

## Validation Order

1. Check required fields present
2. Check username doesn't exist
3. Check email doesn't exist
4. Validate email format
5. Validate password strength
6. Create user in database

---

## Email Confirmation

- Confirmation token automatically generated and sent
- Email send failures are logged but don't prevent registration
- Users should verify email to enable password reset
- Resend confirmation email option should be available

---

## Database Features

- Atomic transactions with rollback on failure
- Auto-increment user ID
- Recommended indexes:
  - `CREATE UNIQUE INDEX idx_username ON users(username)`
  - `CREATE UNIQUE INDEX idx_email ON users(email)`

---

## Integration Examples

**JavaScript (Fetch)**:
```javascript
const response = await fetch('/api/users/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'johndoe',
    email: 'john@example.com',
    password: 'SecurePass123!'
  })
});
const data = await response.json();
```

**Python (requests)**:
```python
import requests
response = requests.post('https://api.example.com/api/users/register',
  json={'username': 'johndoe', 'email': 'john@example.com', 'password': 'SecurePass123!'})
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 400 Missing field | Include all three fields (username, email, password) |
| 400 Invalid email | Use format: user@domain.com |
| 400 Weak password | Use at least 8 characters |
| 409 Username taken | Choose different username |
| 409 Email exists | Use different email or password reset |
| 500 Server error | Contact support |
| CORS error | Check CORS headers configuration |

---

## Logging & Monitoring

- Log all successful registrations
- Alert on multiple attempts from same IP
- Monitor email confirmation failures
- Track unusual registration volume spikes
- Log server errors for debugging

---

## Version & Support

- **Current Version**: 1.0.0
- **Last Updated**: June 15, 2024
- **Status**: Active & Maintained
- **Email**: api-support@example.com
- **Documentation**: https://docs.example.com


## Prompt 2: API Reference Conversion

openapi: 3.0.0
info:
  title: User Registration API
  version: 1.0.0
  contact:
    name: API Support
    email: api-support@example.com

servers:
  - url: https://api.example.com
    description: Production
  - url: http://localhost:5000
    description: Development

tags:
  - name: Users
    description: User registration endpoints

paths:
  /api/users/register:
    post:
      tags: [Users]
      summary: Register a new user
      description: Creates a new user account with validation for required fields, duplicates, email format, and password strength. Sends confirmation email on success.
      operationId: registerUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRegistrationRequest'
            examples:
              success:
                value:
                  username: johndoe
                  email: john@example.com
                  password: SecurePass123!

      responses:
        '201':
          description: User registered successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
              example:
                message: User registered successfully
                user:
                  id: 123
                  username: johndoe
                  email: john@example.com
                  created_at: '2024-06-15T10:30:45.123456'
                  role: user

        '400':
          description: Bad Request (missing field, invalid email, weak password)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                missing_field:
                  value:
                    error: Missing required field
                    message: username is required
                invalid_email:
                  value:
                    error: Invalid email
                    message: Please provide a valid email address
                weak_password:
                  value:
                    error: Weak password
                    message: Password must be at least 8 characters long

        '409':
          description: Conflict (username/email already exists)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                username_taken:
                  value:
                    error: Username taken
                    message: Username is already in use
                email_exists:
                  value:
                    error: Email exists
                    message: An account with this email already exists

        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Server error
                message: Failed to register user

components:
  schemas:
    UserRegistrationRequest:
      type: object
      required: [username, email, password]
      properties:
        username:
          type: string
          minLength: 1
          maxLength: 255
          pattern: '^[a-zA-Z0-9_-]+$'
          description: Unique username (alphanumeric, underscore, hyphen only)
          example: johndoe
        email:
          type: string
          format: email
          minLength: 5
          maxLength: 255
          description: Valid email address (stored in lowercase)
          example: john@example.com
        password:
          type: string
          minLength: 8
          maxLength: 128
          format: password
          description: Password (min 8 characters, mix of upper/lower/numbers/symbols recommended)
          example: SecurePass123!

    User:
      type: object
      required: [id, username, email, created_at, role]
      properties:
        id:
          type: integer
          format: int64
          example: 123
        username:
          type: string
          example: johndoe
        email:
          type: string
          format: email
          example: john@example.com
        created_at:
          type: string
          format: date-time
          example: '2024-06-15T10:30:45.123456'
        role:
          type: string
          enum: [user, admin, moderator]
          example: user

    SuccessResponse:
      type: object
      required: [message, user]
      properties:
        message:
          type: string
          example: User registered successfully
        user:
          $ref: '#/components/schemas/User'

    ErrorResponse:
      type: object
      required: [error, message]
      properties:
        error:
          type: string
          description: Error type/code
          example: Invalid email
        message:
          type: string
          description: Detailed error message
          example: Please provide a valid email address

  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key

security:
  - ApiKeyAuth: []

externalDocs:
  description: Full documentation
  url: https://docs.example.com/user-registration


## Prompt 3: API Usage Guide Creation

# User Registration API - Developer Guide

## Quick Start

**Endpoint**: `POST https://api.example.com/api/users/register`

**Test it now**:
```bash
curl -X POST https://api.example.com/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@example.com","password":"SecurePass123!"}'
```

---

## Authentication & Rate Limiting

- **Auth Required**: No
- **Rate Limit**: 5 requests/minute per IP
- **Optional API Key**: Include `X-API-Key: your-key` header for tracking

---

## Request Format

```json
POST /api/users/register
Content-Type: application/json

{
  "username": "johndoe",      // Required: 1-255 chars, alphanumeric/_/-
  "email": "john@example.com", // Required: valid email, stored lowercase
  "password": "SecurePass123!"  // Required: min 8 characters
}
```

---

## Response Format

### Success (201 Created)
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 123,
    "username": "johndoe",
    "email": "john@example.com",
    "created_at": "2024-06-15T10:30:45.123456",
    "role": "user"
  }
}
```

### Errors
All errors follow this format:
```json
{
  "error": "Error Type",
  "message": "Detailed explanation"
}
```

| Status | Error | Solution |
|--------|-------|----------|
| 400 | Missing required field | Include all 3 fields |
| 400 | Invalid email | Use format: user@domain.ext |
| 400 | Weak password | Min 8 characters |
| 409 | Username taken | Choose different username |
| 409 | Email exists | Use different email |
| 500 | Server error | Try again later |

---

## Code Examples

### JavaScript (Fetch)
```javascript
async function register(username, email, password) {
  try {
    const response = await fetch('https://api.example.com/api/users/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, email, password })
    });

    const data = await response.json();

    if (response.ok) {
      console.log('✅ Success:', data.user);
      return { success: true, user: data.user };
    } else {
      console.error('❌ Error:', data.message);
      return { success: false, error: data.message };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Usage
register('johndoe', 'john@example.com', 'SecurePass123!')
  .then(r => r.success ? alert('Welcome!') : alert(r.error));
```

### React Component
```javascript
import React, { useState } from 'react';

export function RegisterForm() {
  const [data, setData] = useState({ username: '', email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    const response = await fetch('https://api.example.com/api/users/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    setLoading(false);

    if (response.ok) {
      alert(`Welcome ${result.user.username}!`);
      setData({ username: '', email: '', password: '' });
    } else {
      setError(result.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="username" value={data.username} 
        onChange={e => setData({...data, username: e.target.value})} 
        placeholder="Username" required />
      <input name="email" value={data.email} 
        onChange={e => setData({...data, email: e.target.value})} 
        placeholder="Email" type="email" required />
      <input name="password" value={data.password} 
        onChange={e => setData({...data, password: e.target.value})} 
        placeholder="Password (min 8)" type="password" required />
      <button disabled={loading}>{loading ? 'Registering...' : 'Register'}</button>
      {error && <p style={{color: 'red'}}>{error}</p>}
    </form>
  );
}
```

### Python
```python
import requests

def register(username, email, password):
    url = 'https://api.example.com/api/users/register'
    payload = {'username': username, 'email': email, 'password': password}
    
    try:
        response = requests.post(url, json=payload)
        data = response.json()
        
        if response.status_code == 201:
            print(f"✅ Success! User ID: {data['user']['id']}")
            return {'success': True, 'user': data['user']}
        else:
            print(f"❌ Error: {data['message']}")
            return {'success': False, 'error': data['message']}
    except Exception as e:
        return {'success': False, 'error': str(e)}

# Usage
result = register('johndoe', 'john@example.com', 'SecurePass123!')
```

### cURL
```bash
# Basic
curl -X POST https://api.example.com/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@example.com","password":"SecurePass123!"}'

# With status code
curl -X POST https://api.example.com/api/users/register \
  -H "Content-Type: application/json" \
  -d '{...}' -w "\nStatus: %{http_code}\n"

# With API key
curl -X POST https://api.example.com/api/users/register \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-key" \
  -d '{...}'
```

---

## Best Practices

### Input Validation
```javascript
function validate(username, email, password) {
  if (!username) return 'Username required';
  if (!/^[^@]+@[^@]+\.[^@]+$/.test(email)) return 'Invalid email';
  if (password.length < 8) return 'Password min 8 chars';
  return null;
}
```

### Error Handling
```javascript
const response = await fetch(url, {...});
const data = await response.json();

switch (response.status) {
  case 201: return { success: true, user: data.user };
  case 400: return { success: false, error: data.message };
  case 409: return { success: false, error: `${data.error} - try another` };
  case 500: return { success: false, error: 'Server error, try later' };
  default: return { success: false, error: 'Unknown error' };
}
```

### Secure Handling
```javascript
// ✅ HTTPS only
await fetch('https://api.example.com/...')

// ✅ Never log passwords
// ❌ Don't send in URL params
// ❌ Don't use HTTP
```

### Rate Limit Handling
```javascript
if (response.status === 429) {
  setTimeout(() => retry(), 60000); // Wait 60 seconds
}
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 400 Missing field | Include username, email, password |
| 400 Invalid email | Format: user@domain.com |
| 400 Weak password | Use 8+ characters |
| 409 Username taken | Choose different username |
| 409 Email exists | Use different email or reset password |
| 429 Too many requests | Wait 60 seconds before retrying |
| CORS error | Use correct API URL |
| Network error | Check connection & HTTPS |

---

## Reference

**Validation Rules**:
- Username: 1-255 chars, alphanumeric/underscore/hyphen
- Email: Valid format (user@domain.ext), unique, lowercase storage
- Password: 8-128 chars, recommend mixed case + numbers + symbols

**Success Response Includes**:
- `user.id` - Store for authenticated requests
- `user.username` - For login
- `user.email` - Confirmation email sent here
- `user.created_at` - Account creation time
- `user.role` - Always "user" for new accounts

**Rate Limits**:
- 5 requests/minute per IP
- 3 attempts/hour per username
- Global monitoring for abuse

**Error Codes**:
- 201 = Success
- 400 = Bad request (fix input)
- 409 = Conflict (try different username/email)
- 500 = Server error (try again)

---

## Postman Setup

1. Create new request → Name: "Register User"
2. Method: `POST`
3. URL: `https://api.example.com/api/users/register`
4. Headers → `Content-Type: application/json`
5. Body (Raw JSON):
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```
6. Click Send → Check response

---

**Support**: api-support@example.com | Docs: https://docs.example.com | Status: https://status.example.com

**API Version**: 1.0.0 | **Last Updated**: June 15, 2024
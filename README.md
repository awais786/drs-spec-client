# OpenAPI Client Generation for LMS Instructor APIs

This guide explains how to generate an OpenAPI 3 schema for LMS instructor APIs and use the generated client to interact with the APIs. We're leveraging `drf-spectacular` in Django Rest Framework (DRF) and `openapitools/openapi-generator-cli` to automate the process.

## Prerequisites

- **Django APP**: Ensure that the application is set up with the `drf-spectacular` package.
- **Python**: Python 3.x must be installed.
- **pip**: Make sure you have pip installed for managing Python packages.

## Steps to Generate API Client

### 1. Generate OpenAPI Schema

The `drf-spectacular` package is added to the installed apps.

To generate the OpenAPI schema, run the following command inside your directory:

```bash
python manage.py spectacular --file myapp.yaml
```

### 2 Install OpenAPI Python Client Generator
The drf-spectacular library supports openapitools/openapi-generator-cli by default. You can find more information about its usage in the repository. This needs a yaml file.
Here are the steps to use it. 
```docker pull openapitools/openapi-generator-cli```
Run this command 
```
docker run --rm -v /Users/awais.qureshi/Documents/schema.yaml:/local/schema.yaml -v /Users/awais.qureshi/Documents/client:/local/out openapitools/openapi-generator-cli generate -i /local/schema.yaml -g python -o /local/out
```

### 3 Directory Structure
Once you've successfully generated the client, navigate to the generated_client directory. The directory structure will look something like this:
```
generated_client/
│
├── api/         # Contains logic to interact with API endpoints
├── models/      # Data models representing request and response schemas
└── __init__.py
```

### 5 Using the Generated Client

The generated_client is now ready to use in your project to interact with the APIs.
To modify the generated client to handle CSRF tokens and access tokens for authentication, you can 
extend the generated client by adding methods for retrieving and handling the tokens, 
ensuring that they are automatically used in requests.


# Initialize the client
```
base_url = "http://local.edly.io:8000/"
client_id = 'client-id'
client_secret = 'client-secret'

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
    'token_type': 'jwt'
}

headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
client = Client(base_url=base_url, headers=headers)
token = client.retrieve_access_token(auth_url='oauth2/access_token', data=payload)
print("Authentication works !!!!!!!! ")

client = AuthenticatedClient(
    base_url=base_url,
    token=token
)

```

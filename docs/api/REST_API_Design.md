# NexusAI REST API Design

## 1. API Overview

NexusAI exposes a RESTful API that serves as the communication layer between the frontend and backend.

The API follows resource-oriented design principles, where each business entity is represented as a resource with standard CRUD operations.

All endpoints return JSON responses in JSON format and require authentication unless explicitly marked as public.

The API is versioned using the `/api/v1` prefix to ensure backward compatibility as the platform evolves.


## 2. API Design Principles

- RESTful resource naming
- Stateless requests
- Consistent response formats
- Proper HTTP status codes
- Secure authentication
- Versioned endpoints
- Predictable URL structure

## 3. API Versioning

All endpoints are prefixed with `/api/v1`.

Example:

- `/api/v1/auth/login`
- `/api/v1/projects`
- `/api/v1/workspaces`

Future versions of the API can be introduced without breaking existing clients by exposing endpoints such as `/api/v2`.

## 4. API Resources

The API is organized around the following resources:

- Authentication
- Users
- Projects
- Workspaces
- Conversations
- Messages
- Artifacts
- Memory
- AI Interactions

## 5. Authentication APIs

The Authentication API is responsible for user registration, authentication, session management, and retrieving the currently authenticated user's information.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| POST | `/api/v1/auth/register` | Register a new user | No |
| POST | `/api/v1/auth/login` | Authenticate a user and return an access token | No |
| POST | `/api/v1/auth/logout` | Logout the current user | Yes |
| GET | `/api/v1/auth/me` | Retrieve the currently authenticated user's profile | Yes |

## 6. Project APIs

The Project API manages software projects. Each project acts as the primary container for workspaces, conversations, artifacts, memory, and AI interactions.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| GET | `/api/v1/projects` | Retrieve all projects for the authenticated user | Yes |
| POST | `/api/v1/projects` | Create a new project | Yes |
| GET | `/api/v1/projects/{project_id}` | Retrieve a specific project | Yes |
| PUT | `/api/v1/projects/{project_id}` | Update project details | Yes |
| DELETE | `/api/v1/projects/{project_id}` | Delete a project | Yes |

## 7. Workspace APIs

The Workspace API manages engineering workspaces within a project. Each workspace provides a dedicated environment for a specific software engineering activity.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| GET | `/api/v1/projects/{project_id}/workspaces` | Retrieve all workspaces for a project | Yes |
| POST | `/api/v1/projects/{project_id}/workspaces` | Create a new workspace | Yes |
| GET | `/api/v1/workspaces/{workspace_id}` | Retrieve a specific workspace | Yes |
| PUT | `/api/v1/workspaces/{workspace_id}` | Update workspace details | Yes |
| DELETE | `/api/v1/workspaces/{workspace_id}` | Delete a workspace | Yes |

## 8. Conversation APIs

The Conversation API manages chat sessions within a workspace. Each workspace can contain multiple conversations, allowing users to organize discussions by topic.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| GET | `/api/v1/workspaces/{workspace_id}/conversations` | Retrieve all conversations in a workspace | Yes |
| POST | `/api/v1/workspaces/{workspace_id}/conversations` | Create a new conversation | Yes |
| GET | `/api/v1/conversations/{conversation_id}` | Retrieve a specific conversation | Yes |
| PUT | `/api/v1/conversations/{conversation_id}` | Rename a conversation | Yes |
| DELETE | `/api/v1/conversations/{conversation_id}` | Delete a conversation | Yes |

## 9. Message APIs

The Message API manages individual messages within a conversation. Messages may be created by the user, the AI assistant, or the system.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| GET | `/api/v1/conversations/{conversation_id}/messages` | Retrieve all messages in a conversation | Yes |
| POST | `/api/v1/conversations/{conversation_id}/messages` | Send a new message | Yes |
| GET | `/api/v1/messages/{message_id}` | Retrieve a specific message | Yes |
| DELETE | `/api/v1/messages/{message_id}` | Delete a message | Yes |

## 10. Artifact APIs

The Artifact API manages engineering artifacts generated within a workspace, such as architecture documents, API specifications, database designs, code review reports, and technical documentation.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| GET | `/api/v1/workspaces/{workspace_id}/artifacts` | Retrieve all artifacts in a workspace | Yes |
| POST | `/api/v1/workspaces/{workspace_id}/artifacts` | Create a new artifact | Yes |
| GET | `/api/v1/artifacts/{artifact_id}` | Retrieve a specific artifact | Yes |
| PUT | `/api/v1/artifacts/{artifact_id}` | Update an artifact | Yes |
| DELETE | `/api/v1/artifacts/{artifact_id}` | Delete an artifact | Yes |


## 11. Memory APIs

The Memory API manages long-term project knowledge. Memory entries capture important decisions, project context, and engineering knowledge that can be reused across all workspaces.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| GET | `/api/v1/projects/{project_id}/memory` | Retrieve all memory entries for a project | Yes |
| POST | `/api/v1/projects/{project_id}/memory` | Create a new memory entry | Yes |
| GET | `/api/v1/memory/{memory_id}` | Retrieve a specific memory entry | Yes |
| PUT | `/api/v1/memory/{memory_id}` | Update a memory entry | Yes |
| DELETE | `/api/v1/memory/{memory_id}` | Delete a memory entry | Yes |

## 12. AI APIs

The AI API manages AI-powered engineering tasks, model orchestration, and interaction history. It routes requests to the most appropriate AI model based on the requested engineering task.

| Method | Endpoint | Description | Authentication Required |
|---------|----------|-------------|--------------------------|
| POST | `/api/v1/ai/chat` | Send a message to the AI assistant | Yes |
| POST | `/api/v1/ai/orchestrate` | Route an engineering task to the most suitable AI model | Yes |
| GET | `/api/v1/projects/{project_id}/ai/interactions` | Retrieve AI interaction history for a project | Yes |
| GET | `/api/v1/ai/models` | Retrieve available AI models and providers | Yes |

## 13. Standard Response Format

All successful API responses follow a consistent JSON structure.

### Success Response

```json
{
  "success": true,
  "message": "Project created successfully.",
  "data": {
    ...
  }
}
```

### Error Response

```json
{
  "success": false,
  "message": "Project not found.",
  "errors": [
    ...
  ]
}
```

This consistent response format simplifies frontend development and error handling.

## 14. Error Responses

The API uses standard HTTP status codes to indicate the result of a request.

| Status Code | Meaning |
|------------|---------|
| 200 OK | Request completed successfully |
| 201 Created | Resource created successfully |
| 400 Bad Request | Invalid request data |
| 401 Unauthorized | Authentication required |
| 403 Forbidden | User does not have permission |
| 404 Not Found | Requested resource does not exist |
| 409 Conflict | Resource already exists |
| 422 Unprocessable Entity | Validation failed |
| 500 Internal Server Error | Unexpected server error |

## 15. Authentication & Authorization

The NexusAI API secures protected endpoints using token-based authentication.

### Authentication

- Users must authenticate before accessing protected resources.
- Upon successful login, the server returns an access token.
- The access token must be included in subsequent API requests.

Example:

```http
Authorization: Bearer <access_token>
```

### Authorization

Users can only access resources they own.

Examples:

- A user can only view their own projects.
- A user can only access workspaces belonging to their projects.
- A user cannot access another user's conversations, artifacts, or memory entries.

Authorization checks are performed on every protected request before executing business logic.
# NexusAI Database Design

## 1. Database Overview

The NexusAI database is responsible for storing all persistent application data, including user accounts, projects, project memory, conversations, architecture artifacts, code reviews, and generated documentation.

The database serves as the single source of truth for the application. Every module interacts with the database through the application's business logic rather than accessing data directly.

The database is designed to support:

- Secure user management
- Multiple projects per user
- Persistent project context
- Structured engineering artifacts
- Future expansion without major schema changes

The schema follows normalization principles to minimize data duplication while maintaining efficient relationships between entities.


## 2. Database Goals

The database is designed with the following objectives:

### 2.1 Data Consistency
Ensure that all project information remains accurate and synchronized across every workspace.

### 2.2 Scalability
Support future features such as team collaboration, GitHub integration, plugins, and autonomous AI agents without requiring major schema redesign.

### 2.3 Maintainability
Keep the schema simple, modular, and easy to extend while minimizing redundancy.

### 2.4 Security
Protect user and project data through proper relationships, ownership, and access control.

### 2.5 Performance
Enable efficient retrieval of project information, conversations, memory, and engineering artifacts.


## 3. Entity Overview

The MVP consists of the following core entities:

| Entity | Purpose |
|----------|---------|
| User | Stores user accounts and profile information. |
| Project | Represents a software project created by a user. |
| Conversation | Stores chat conversations within a project. |
| Message | Stores individual chat messages. |
| Project Memory | Stores long-term project knowledge and context. |
| Architecture Artifact | Stores architecture designs and decisions. |
| Code Review | Stores submitted code and AI review results. |
| Documentation | Stores generated project documentation. |
| AI Request Log | Records AI routing decisions and request metadata. |
| AI Provider | Stores information about available AI providers and models. |


## 4. Entity Relationship Diagram (ERD)

The core relationships between entities are:

| Parent Entity | Relationship | Child Entity |
|---------------|--------------|--------------|
| User | One-to-Many | Project |
| Project | One-to-Many | Conversation |
| Conversation | One-to-Many | Message |
| Project | One-to-One | Knowledge Base |
| Project | One-to-Many | Architecture Artifact |
| Project | One-to-Many | Code Review |
| Project | One-to-Many | Documentation |
| Project | One-to-Many | AI Request Log |
| AI Provider | One-to-Many | AI Request Log |


## 5. Table Designs

### 5.1 User

| Column | Description |
|---------|-------------|
| id | Unique user identifier |
| name | User's full name |
| email | User email address |
| password_hash | Encrypted password |
| created_at | Account creation timestamp |
| updated_at | Last update timestamp |

---

### 5.2 Project

| Column | Description |
|---------|-------------|
| id | Unique project identifier |
| user_id | Owner of the project |
| name | Project name |
| description | Project description |
| created_at | Creation timestamp |
| updated_at | Last update timestamp |

---

### 5.3 Conversation

| Column | Description |
|---------|-------------|
| id | Conversation identifier |
| project_id | Parent project |
| title | Conversation title |
| created_at | Creation timestamp |

---

### 5.4 Message

| Column | Description |
|---------|-------------|
| id | Message identifier |
| conversation_id | Parent conversation |
| role | User or AI |
| content | Message content |
| created_at | Timestamp |

---

### 5.5 Knowledge Base

| Column | Description |
|---------|-------------|
| id | Knowledge Base identifier |
| project_id | Associated project |
| summary | Consolidated project knowledge |
| updated_at | Last updated timestamp |

---

### 5.6 Architecture Artifact

| Column | Description |
|---------|-------------|
| id | Artifact identifier |
| project_id | Parent project |
| title | Artifact title |
| content | Architecture document |
| created_at | Creation timestamp |

---

### 5.7 Code Review

| Column | Description |
|---------|-------------|
| id | Review identifier |
| project_id | Parent project |
| submitted_code | Submitted source code |
| review_result | AI review output |
| created_at | Review timestamp |

---

### 5.8 Documentation

| Column | Description |
|---------|-------------|
| id | Documentation identifier |
| project_id | Parent project |
| type | README, API Docs, etc. |
| content | Generated documentation |
| created_at | Creation timestamp |

---

### 5.9 AI Interaction

| Column | Description |
|---------|-------------|
| id | Interaction identifier |
| project_id | Parent project |
| provider | AI provider used |
| model | Model name |
| task_type | Architecture, Review, Chat, etc. |
| status | Success or Failed |
| created_at | Timestamp |

---

### 5.10 AI Provider

| Column | Description |
|---------|-------------|
| id | Provider identifier |
| provider_name | Provider name |
| model_name | Model name |
| availability | Active or inactive |


## 6. Relationships

| Parent | Relationship | Child |
|---------|--------------|-------|
| User | One-to-Many | Project |
| Project | One-to-Many | Workspace |
| Workspace | One-to-Many | Conversation |
| Conversation | One-to-Many | Message |
| Workspace | One-to-Many | Artifact |
| Project | One-to-Many | MemoryEntry |
| Project | One-to-Many | AIInteraction |


## 7. Indexing Strategy

The following fields should be indexed to improve query performance:

- User email
- Project owner (user_id)
- Workspace project_id
- Conversation workspace_id
- Message conversation_id
- Artifact workspace_id
- MemoryEntry project_id
- AIInteraction project_id

Additional indexes may be introduced as usage patterns evolve.


## 8. Data Integrity

To maintain consistency:

- Every project belongs to exactly one user.
- Every workspace belongs to exactly one project.
- Every conversation belongs to exactly one workspace.
- Every message belongs to exactly one conversation.
- Every artifact belongs to exactly one workspace.
- Memory entries belong to one project.
- AI interactions belong to one project.

Foreign key constraints should enforce these relationships.


## 9. Future Expansion

The schema is designed to support future additions such as:

- Team collaboration
- Roles and permissions
- GitHub integration
- Plugin ecosystem
- Autonomous AI agents
- Version history
- Project templates

These features can be introduced without major changes to the existing schema.


## 10. ADR-002

### Decision

Model the database around business entities rather than individual application features.

### Reason

Using generic entities such as Workspace, Artifact, and MemoryEntry provides greater flexibility, reduces schema complexity, and allows new features to be introduced without creating additional tables.

### Consequences

- Smaller schema
- Easier maintenance
- Better scalability
- More reusable data model
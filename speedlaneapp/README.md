# Turnstile Management API

REST API for managing lanes, turnstyles, system configuration, and access logs.

## Base URL

/api/

---

# 1. Lane API

## Get all lanes

GET /api/lanes/

Returns all lanes.

## Get a single lane

GET /api/lanes/{id}/

Example:

GET /api/lanes/1/

## Create a lane

POST /api/lanes/

Request body:

{
    "name": "Lane 1",
    "turnstyles": [1, 2],
    "created_by": "admin"
}

## Update a lane

PATCH /api/lanes/{id}/

Example:

PATCH /api/lanes/1/

Request body:

{
    "name": "Lane 1 Updated"
}

## Delete a lane

DELETE /api/lanes/{id}/

Example:

DELETE /api/lanes/1/

---

# 2. Trigger Lane

Triggers a specific lane.

PATCH /api/lanes/{id}/trigger/

Example:

PATCH /api/lanes/1/trigger/

Request body:

{
    "user": "username",
    "remarks": "Manual access"
}

### Fields

| Field   | Type   | Required | Description                            |
|---------|--------|----------|----------------------------------------|
| user    | string | No       | User who triggered the lane            |
| remarks | string | No       | Optional information about the trigger |

### Success Response

{
    "message": "Lane triggered successfully",
    "lane_id": 1
}

The trigger API also creates an access log.

The actual hardware trigger will be integrated later.

---

# 3. Turnstyle API

## Get all turnstyles

GET /api/turnstyles/

## Get a single turnstyle

GET /api/turnstyles/{id}/

Example:

GET /api/turnstyles/1/

## Create a turnstyle

POST /api/turnstyles/

Request body:

{
    "make": "CAME",
    "model": "HG 02",
    "type": "center",
    "is_left": false,
    "entry_pin": 10,
    "exit_pin": 11
}

## Update a turnstyle

PATCH /api/turnstyles/{id}/

Example:

PATCH /api/turnstyles/1/

## Delete a turnstyle

DELETE /api/turnstyles/{id}/

Example:

DELETE /api/turnstyles/1/

### Turnstyle Types

- center
- side
- differently_abled

---

# 4. System Configuration API

## Get all configurations

GET /api/system-config/

## Get a configuration

GET /api/system-config/{id}/

Example:

GET /api/system-config/1/

## Create configuration

POST /api/system-config/

Request body:

{
    "wifi_ssid": "MyWiFi",
    "wifi_password": "password123"
}

## Update configuration

PATCH /api/system-config/{id}/

Example:

PATCH /api/system-config/1/

Request body:

{
    "wifi_ssid": "NewWiFi"
}

## Delete configuration

DELETE /api/system-config/{id}/

Example:

DELETE /api/system-config/1/

---

# 5. Access Log API

Access logs contain information about lane triggers.

Each log contains:

- Lane
- User
- Remarks
- Triggered time

## Get all access logs

GET /api/access-logs/

Logs are returned with the newest entries first.

Example response:

[
    {
        "id": 5,
        "lane": 2,
        "user": "username",
        "remarks": "Manual access",
        "triggered_at": "2026-09-17T11:30:00Z"
    },
    {
        "id": 4,
        "lane": 1,
        "user": "admin",
        "remarks": "Test",
        "triggered_at": "2026-09-17T11:20:00Z"
    }
]

If there are no access logs:

[]

## Get a single access log

GET /api/access-logs/{id}/

Example:

GET /api/access-logs/1/

## Create an access log

POST /api/access-logs/

Request body:

{
    "lane": 1,
    "user": "username",
    "remarks": "Manual access"
}

## Update an access log

PATCH /api/access-logs/{id}/

## Delete an access log

DELETE /api/access-logs/{id}/

---

# API Summary

| Method |           Endpoint               | Description               |
|--------|----------------------------------|---------------------------|
| GET    | /api/lanes/                      | Get all lanes             |
| POST   | /api/lanes/                      | Create lane               |
| GET    | /api/lanes/{id}/                 | Get lane                  |
| PATCH  | /api/lanes/{id}/                 | Update lane               |
| DELETE | /api/lanes/{id}/                 | Delete lane               |
| PATCH  | /api/lanes/{id}/trigger/         | Trigger lane              |
| GET    | /api/turnstyles/                 | Get all turnstyles        |
| POST   | /api/turnstyles/                 | Create turnstyle          |
| GET    | /api/turnstyles/{id}/            | Get turnstyle             |
| PATCH  | /api/turnstyles/{id}/            | Update turnstyle          |
| DELETE | /api/turnstyles/{id}/            | Delete turnstyle          |
| GET    | /api/system-config/              | Get system configurations |
| POST   | /api/system-config/              | Create configuration      |
| GET    | /api/system-config/{id}/         | Get configuration         |
| PATCH  | /api/system-config/{id}/         | Update configuration      |
| DELETE | /api/system-config/{id}/         | Delete configuration      |
| GET    | /api/access-logs/                | Get all access logs       |
| POST   | /api/access-logs/                | Create access log         |
| GET    | /api/access-logs/{id}/           | Get access log            |
| PATCH  | /api/access-logs/{id}/           | Update access log         |
| DELETE | /api/access-logs/{id}/           | Delete access log         |

---

# Typical Frontend Flow

## 1. Load lanes

GET /api/lanes/

Frontend displays the available lanes.

## 2. User selects a lane

For example, Lane 2.

## 3. Trigger the lane

PATCH /api/lanes/2/trigger/

Request body:

{
    "user": "username",
    "remarks": "Manual trigger"
}

## 4. Backend creates the access log

Example:

Lane: Lane 2
User: username
Remarks: Manual trigger
Time: Current time

## 5. Load access history

GET /api/access-logs/

The frontend can display the access history to the user.

---

# Technologies

- Django
- Django REST Framework
- sqllite
- REST API
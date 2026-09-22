# GateTouchPro Turnstile Management API

This project exposes a REST API for managing lanes, turnstiles, system configuration, and access logs for a turnstile control system.

## Base URL

Use the following base path for all API requests:

/api/

---

## Overview

The API supports the following core resources:

- Lane groups
- Lanes
- Turnstiles
- Trigger actions for entry and exit
- System configuration
- Access logs

The documentation below outlines the available endpoints, request payloads, and example responses.

---

# 1. Lane Group API

Lane groups are used to organize lanes by area or section.

## 1.1 Get all lane groups

Request:

GET /api/lane-groups/

Returns all lane groups.

Example response:

```json
[
  {
    "id": 1,
    "name": "Main Entrance",
    "description": "Main entrance lane group"
  }
]
```

## 1.2 Get a single lane group

Request:

GET /api/lane-groups/{id}/

Example:

GET /api/lane-groups/1/

## 1.3 Create a lane group

Request:

POST /api/lane-groups/

Request body:

```json
{
  "name": "Main Entrance",
  "description": "Main entrance lane group"
}
```

## 1.4 Update a lane group

Request:

PATCH /api/lane-groups/{id}/

Example:

PATCH /api/lane-groups/1/

Request body:

```json
{
  "name": "Main Entrance Updated"
}
```

## 1.5 Delete a lane group

Request:

DELETE /api/lane-groups/{id}/

Example:

DELETE /api/lane-groups/1/

---

# 2. Lane API

Lanes represent a physical passage and may contain one or more turnstiles.

## 2.1 Get all lanes

Request:

GET /api/lanes/

Returns all lanes.

## 2.2 Get a single lane

Request:

GET /api/lanes/{id}/

Example:

GET /api/lanes/1/

## 2.3 Create a lane

Request:

POST /api/lanes/

Request body:

```json
{
  "name": "Lane 1",
  "lane_group": 1,
  "turnstyles": [
    {
      "make": "CAME",
      "model": "HG 02 S V3",
      "type": "side",
      "is_left": true
    },
    {
      "make": "CAME",
      "model": "HG 02 C V3",
      "type": "center",
      "is_left": false
    }
  ],
  "width": 60,
  "entry_pin": 17,
  "exit_pin": 18,
  "created_by": "admin"
}
```

## 2.4 Update a lane

Request:

PATCH /api/lanes/{id}/

Example:

PATCH /api/lanes/1/

Request body:

```json
{
  "name": "Lane 1 Updated",
  "turnstyles": [
    {
      "id": 5,
      "model": "HG 02 S V3",
      "is_left": true
    }
  ],
  "entry_pin": 17,
  "exit_pin": 18
}
```

Notes:

- Existing turnstiles can be updated by providing their `id`.
- If a turnstile does not include an `id`, a new turnstile is created and attached to the lane.

## 2.5 Delete a lane

Request:

DELETE /api/lanes/{id}/

Example:

DELETE /api/lanes/1/

---

# 3. Trigger Lane

This action triggers a specific lane in either the entry or exit direction.

## 3.1 Trigger entry

Request:

PATCH /api/lanes/{id}/trigger/entry/

Example:

PATCH /api/lanes/1/trigger/entry/

Request body:

```json
{
  "user": "username",
  "remarks": "Manual entry access"
}
```

Success response:

```json
{
  "message": "Lane triggered successfully",
  "lane_id": 1,
  "direction": "entry"
}
```

## 3.2 Trigger exit

Request:

PATCH /api/lanes/{id}/trigger/exit/

Example:

PATCH /api/lanes/1/trigger/exit/

Request body:

```json
{
  "user": "username",
  "remarks": "Manual exit access"
}
```

Success response:

```json
{
  "message": "Lane triggered successfully",
  "lane_id": 1,
  "direction": "exit"
}
```

### Trigger fields

| Field | Type | Required | Description |
|---|---|---:|---|
| user | string | No | User who triggered the lane |
| remarks | string | No | Optional information about the trigger |
| entry_pin | integer | Yes | GPIO pin used for entry |
| exit_pin | integer | Yes | GPIO pin used for exit |

The trigger endpoint also creates an access log entry.

---

# 4. Trigger Lane Group

This action triggers all lanes inside a lane group.

## 4.1 Trigger entry for lane group

Request:

PATCH /api/lane-groups/{id}/trigger/entry/

Example:

PATCH /api/lane-groups/1/trigger/entry/

Request body:

```json
{
  "user": "username",
  "remarks": "Manual group entry access"
}
```

Success response:

```json
{
  "message": "Lane group trigger started successfully",
  "lane_group_id": 1,
  "direction": "entry"
}
```

## 4.2 Trigger exit for lane group

Request:

PATCH /api/lane-groups/{id}/trigger/exit/

Example:

PATCH /api/lane-groups/1/trigger/exit/

Request body:

```json
{
  "user": "username",
  "remarks": "Manual group exit access"
}
```

Success response:

```json
{
  "message": "Lane group trigger started successfully",
  "lane_group_id": 1,
  "direction": "exit"
}
```

---

# 5. Turnstyle API

## 5.1 Get all turnstiles

Request:

GET /api/turnstyles/

## 5.2 Get a single turnstile

Request:

GET /api/turnstyles/{id}/

Example:

GET /api/turnstyles/1/

## 5.3 Create a turnstile

Request:

POST /api/turnstyles/

Request body:

```json
{
  "make": "CAME",
  "model": "HG 02",
  "type": "center",
  "is_left": false
}
```

## 5.4 Update a turnstile

Request:

PATCH /api/turnstyles/{id}/

Example:

PATCH /api/turnstyles/1/

## 5.5 Delete a turnstile

Request:

DELETE /api/turnstyles/{id}/

Example:

DELETE /api/turnstyles/1/

### Supported turnstile types

- center
- side
- differently_abled

---

# 6. System Configuration API

System configuration stores runtime settings such as Wi-Fi details and trigger timing.

## 6.1 Get all configurations

Request:

GET /api/system-config/

## 6.2 Get a configuration

Request:

GET /api/system-config/{id}/

Example:

GET /api/system-config/1/

## 6.3 Create a configuration

Request:

POST /api/system-config/

Request body:

```json
{
  "wifi_ssid": "MyWiFi",
  "wifi_password": "password123",
  "trigger_delay": 5000
}
```

Note: `trigger_delay` is expressed in milliseconds.

Examples:

- 5000 ms = 5 seconds
- 3000 ms = 3 seconds
- 1000 ms = 1 second

## 6.4 Update a configuration

Request:

PATCH /api/system-config/{id}/

Example:

PATCH /api/system-config/1/

Request body:

```json
{
  "wifi_ssid": "NewWiFi"
}
```

## 6.5 Delete a configuration

Request:

DELETE /api/system-config/{id}/

Example:

DELETE /api/system-config/1/

---

# 7. Access Log API

Access logs track trigger events and contain information related to lane actions.

Each log includes:

- Lane
- User
- Remarks
- Triggered time

## 7.1 Get all access logs

Request:

GET /api/access-logs/

Logs are returned with the newest entries first.

---

## Notes

- All endpoints are relative to the base URL `/api/`.
- The API uses standard HTTP methods such as `GET`, `POST`, `PATCH`, and `DELETE`.
- Trigger endpoints generate access log entries automatically.

This document serves as a reference for the current turnstile management API behavior and endpoint structure.

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

| Method |           Endpoint                   | Description               |
|--------|--------------------------------------|---------------------------|
| GET	 |  /api/lane-groups/	                | Get all lane groups       |
| POST	 |  /api/lane-groups/	                | Create lane group         |
| GET	 |  /api/lane-groups/{id}/	            | Get one lane group        |
| PATCH	 |  /api/lane-groups/{id}/	            | Update lane group         |
| DELETE |  /api/lane-groups/{id}/	            | Delete lane group         |
| GET    | /api/lanes/                          | Get all lanes             |
| POST   | /api/lanes/                          | Create lane               |
| GET    | /api/lanes/{id}/                     | Get lane                  |
| PATCH  | /api/lanes/{id}/                     | Update lane               |
| DELETE | /api/lanes/{id}/                     | Delete lane               |
| PATCH  | /api/lanes/{id}/trigger/entry/       | Trigger lane entry        |
| PATCH  | /api/lanes/{id}/trigger/exit/        | Trigger lane exit         |
| PATCH  | /api/lane-groups/{id}/trigger/entry/ | Trigger lane group entry  |
| PATCH  | /api/lane-groups/{id}/trigger/exit/  | Trigger lane group exit   |
| GET    | /api/turnstyles/                     | Get all turnstyles        |
| POST   | /api/turnstyles/                     | Create turnstyle          |
| GET    | /api/turnstyles/{id}/                | Get turnstyle             |
| PATCH  | /api/turnstyles/{id}/                | Update turnstyle          |
| DELETE | /api/turnstyles/{id}/                | Delete turnstyle          |
| GET    | /api/system-config/                  | Get system configurations |
| POST   | /api/system-config/                  | Create configuration      |
| GET    | /api/system-config/{id}/             | Get configuration         |
| PATCH  | /api/system-config/{id}/             | Update configuration      |
| DELETE | /api/system-config/{id}/             | Delete configuration      |
| GET    | /api/access-logs/                    | Get all access logs       |
| POST   | /api/access-logs/                    | Create access log         |
| GET    | /api/access-logs/{id}/               | Get access log            |
| PATCH  | /api/access-logs/{id}/               | Update access log         |
| DELETE | /api/access-logs/{id}/               | Delete access log         |

---

# Typical Frontend Flow

## 1. Load lane groups

GET /api/lane-groups/

Frontend displays the available lane groups.

## 2. Load lanes

GET /api/lanes/

Frontend displays the available lanes.

## 3. User selects a lane

For example, Lane 2.

## 4. User selects direction

The frontend provides:

- Entry
- Exit

## 5. Trigger the lane

For Entry:

PATCH /api/lanes/2/trigger/entry/

For Exit:

PATCH /api/lanes/2/trigger/exit/

Request body:

{
    "user": "username",
    "remarks": "Manual trigger"
}

## 6. Backend triggers the turnstile

The backend determines the appropriate GPIO pin from the lane configuration.

For Entry: 
lane.entry_pin is used.

For Exit: 
lane.exit_pin is used.

The trigger delay is obtained from SystemConfig.trigger_delay and is specified in milliseconds.

## 7. Backend creates the access log

Example:

Lane: Lane 2

User: username

Remarks: Manual trigger

Time: Current time

## 8. Load access history

GET /api/access-logs/

The frontend can display the access history to the user.

---

# Technologies

- Django
- Django REST Framework
- SQLite
- REST API
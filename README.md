# Turnstile Management API

REST API for managing lanes, turnstyles, system configuration, and access logs.

## Base URL

/api/

---




# 1. Lane Group API

Lane groups are used to organize lanes.

## Get all lane groups

GET /api/lane-groups/

Returns all lane groups.

Example response:

[
    {
        "id": 1,
        "name": "Main Entrance",
        "description": "Main entrance lane group"
    }
]

## Get a single lane group

GET /api/lane-groups/{id}/

Example:

GET /api/lane-groups/1/

## Create a lane group

POST /api/lane-groups/

Request body:

{
    "name": "Main Entrance",
    "description": "Main entrance lane group"
}

## Update a lane group

PATCH /api/lane-groups/{id}/

Example:

PATCH /api/lane-groups/1/

Request body:

{
    "name": "Main Entrance Updated"
}

## Delete a lane group

DELETE /api/lane-groups/{id}/

Example:

DELETE /api/lane-groups/1/

---

# 2. Lane API

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
    "lane_group": 1,
    "turnstyles": [
        {
            "make": "CAME",
            "model": "HG 02 S V3",
            "type": "side",
            "is_left": true,
            "entry_pin": 17,
            "exit_pin": 18
        },
        {
            "make": "CAME",
            "model": "HG 02 C V3",
            "type": "center",
            "is_left": false,
            "entry_pin": 22,
            "exit_pin": 23
        }
    ],
    "width": 60,
    "created_by": "admin"
}

## Update a lane

PATCH /api/lanes/{id}/

Example:

PATCH /api/lanes/1/

Request body:

{
    "name": "Lane 1 Updated",
    "turnstyles": [
        {
            "id": 5,
            "entry_pin": 25,
            "exit_pin": 46
        }
    ]
}


Existing turnstyles can be updated by providing their `id`.

If a turnstyle does not contain an `id`, a new turnstyle is created and attached to the lane.


## Delete a lane

DELETE /api/lanes/{id}/

Example:

DELETE /api/lanes/1/

---


# 3. Trigger Lane

Triggers a specific lane in either entry or exit direction.

## Trigger Entry

PATCH /api/lanes/{id}/trigger/entry/

Example:

PATCH /api/lanes/1/trigger/entry/

Request body:

{
    "user": "username",
    "remarks": "Manual entry access"
}

Success Response:

{
    "message": "Lane triggered successfully",
    "lane_id": 1,
    "direction": "entry"
}

## Trigger Exit

PATCH /api/lanes/{id}/trigger/exit/

Example:

PATCH /api/lanes/1/trigger/exit/

Request body:

{
    "user": "username",
    "remarks": "Manual exit access"
}

Success Response:

{
    "message": "Lane triggered successfully",
    "lane_id": 1,
    "direction": "exit"
}

### Fields

| Field   | Type   | Required | Description                         |
|---------|--------|----------|-------------------------------------|
| user    | string | No       | User who triggered the lane         |
| remarks | string | No       | Optional information about trigger  |

The trigger API also creates an access log.



# 4. Trigger Lane Group

Triggers all lanes belonging to a lane group.

## Trigger Entry

PATCH /api/lane-groups/{id}/trigger/entry/

Example:

PATCH /api/lane-groups/1/trigger/entry/

Request body:

{
    "user": "username",
    "remarks": "Manual group entry access"
}

Success Response:

{
    "message": "Lane group trigger started successfully",
    "lane_group_id": 1,
    "direction": "entry"
}

## Trigger Exit

PATCH /api/lane-groups/{id}/trigger/exit/

Example:

PATCH /api/lane-groups/1/trigger/exit/

Request body:

{
    "user": "username",
    "remarks": "Manual group exit access"
}

Success Response:

{
    "message": "Lane group trigger started successfully",
    "lane_group_id": 1,
    "direction": "exit"
}


# 5. Turnstyle API

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

# 6. System Configuration API

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

# 7. Access Log API

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

The backend determines the appropriate GPIO pin from the turnstyle configuration.

For Entry:
entry_pin is used.

For Exit:
exit_pin is used.

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
---
title: tft-backend v0.0.1
language_tabs:
  - javascipts: JavaScript
language_clients:
  - javascipts: ""
toc_footers: []
includes: []
search: false
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="tft-backend">tft-backend v0.0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Team Formation Tool backend documentation.

Base URLs:

* <a href="http://localhost:5000">http://localhost:5000</a>

<a href="https://github.com/sreedhara-aneesh/csc510-fall22-p1-g33/blob/main/LICENSE.md">Terms of service</a>
Web: <a href="https://github.com/sreedhara-aneesh/csc510-fall22-p1-g33">Support</a> 

<h1 id="tft-backend-default">Default</h1>

## Your GET endpoint

<a id="opIdget-user-query"></a>

> Code samples

`GET /user/query`

Query for user id by username.

> Body parameter

```json
{
  "username": "jdoe"
}
```

<h3 id="your-get-endpoint-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» username|body|string|true|User username.|

> Example responses

> OK

```json
{
  "user": "1"
}
```

<h3 id="your-get-endpoint-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="your-get-endpoint-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» user|string|true|none|User id.|

<aside class="success">
This operation does not require authentication
</aside>

## create join request

<a id="opIdpost-join_request"></a>

> Code samples

`POST /joinrequest/`

Create join request.

> Body parameter

```json
{
  "creator": "1",
  "team": "1"
}
```

<h3 id="create-join-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|Join request information.|
|» creator|body|string|true|Creator user id.|
|» team|body|string|true|Team id.|

> Example responses

> OK

```json
{
  "id": "1"
}
```

<h3 id="create-join-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|

<h3 id="create-join-request-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|true|none|ID of created join request.|

<aside class="success">
This operation does not require authentication
</aside>

## get join request

<a id="opIdget-join_request-id"></a>

> Code samples

`GET /joinrequest/{id}`

Get join request by id.

> Example responses

> OK

```json
{
  "join_request": {
    "id": "1",
    "user": "1",
    "team": "1",
    "status": "pending"
  }
}
```

<h3 id="get-join-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="get-join-request-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» join_request|object|true|none|Join request information.|
|»» id|string|true|none|Join request id.|
|»» user|string|true|none|ID of user who created join request.|
|»» team|string|true|none|ID of team that join request is for.|
|»» status|string|true|none|Status of join request.|

#### Enumerated Values

|Property|Value|
|---|---|
|status|pending|
|status|denied|
|status|accepted|
|status|withdrawn|

<aside class="success">
This operation does not require authentication
</aside>

## delete join request

<a id="opIddelete-join_request-id"></a>

> Code samples

`DELETE /joinrequest/{id}`

Delete join request by id.

WARNING: Join requests are now automatically deleted when their associated team or user is deleted. There is no reason to use this method in normal operations.

<h3 id="delete-join-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|

<aside class="success">
This operation does not require authentication
</aside>

## accept join request

<a id="opIdpatch-join_request-id-accept"></a>

> Code samples

`PATCH /joinrequest/{id}/accept`

Accept join request

<h3 id="accept-join-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|

<aside class="success">
This operation does not require authentication
</aside>

## reject join request

<a id="opIdpatch-join_request-id-reject"></a>

> Code samples

`PATCH /joinrequest/{id}/reject`

Reject join request.

<h3 id="reject-join-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|

<aside class="success">
This operation does not require authentication
</aside>

## withdraw join request

<a id="opIdpatch-join_request-id-withdraw"></a>

> Code samples

`PATCH /joinrequest/{id}/withdraw`

Withdraw join request.

<h3 id="withdraw-join-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|

<aside class="success">
This operation does not require authentication
</aside>

## create project

<a id="opIdpost-project"></a>

> Code samples

`POST /project/`

Create project.

> Body parameter

```json
{
  "creator": "1"
}
```

<h3 id="create-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» creator|body|string|true|Creator user id.|

> Example responses

> Created

```json
{
  "id": "1"
}
```

<h3 id="create-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="create-project-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|true|none|ID of created project.|

<aside class="success">
This operation does not require authentication
</aside>

## get project

<a id="opIdget-project-id"></a>

> Code samples

`GET /project/{id}`

Get project by id.

> Example responses

> OK

```json
{
  "project": {
    "id": "1",
    "teams": [
      "1"
    ],
    "users": [
      "1"
    ],
    "about": {
      "name": "Project A",
      "description": "This is project A."
    }
  }
}
```

<h3 id="get-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="get-project-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» project|object|true|none|Project information.|
|»» id|string|true|none|Project id.|
|»» teams|[string]|true|none|IDs of teams in project.|
|»» users|[string]|true|none|IDs of users in project.|
|»» about|object|true|none|Project's about fields.|
|»»» name|string|true|none|Project name.|
|»»» description|string|true|none|Project description.|

<aside class="success">
This operation does not require authentication
</aside>

## delete project

<a id="opIddelete-project-id"></a>

> Code samples

`DELETE /project/{id}`

Delete project by id.

WARNING: Projects are now deleted automatically when all users leave them. There is no reason to use this method in normal operations.

<h3 id="delete-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## add user to project

<a id="opIdpatch-project-id-users-add"></a>

> Code samples

`PATCH /project/{id}/users/add`

Add user to project.

> Body parameter

```json
{
  "user_id": "1"
}
```

<h3 id="add-user-to-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» user_id|body|string|true|User id.|

<h3 id="add-user-to-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## remove user from project

<a id="opIdpatch-project-id-users-remove"></a>

> Code samples

`PATCH /project/{id}/users/remove`

Remove user from project.

> Body parameter

```json
{
  "user_id": "1"
}
```

<h3 id="remove-user-from-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» user_id|body|string|true|User id.|

<h3 id="remove-user-from-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## edit project about

<a id="opIdpatch-project-id-about"></a>

> Code samples

`PATCH /project/{id}/about`

Edit project's about fields.

> Body parameter

```json
{
  "name": "Project A",
  "description": "This is project A."
}
```

<h3 id="edit-project-about-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|Project's new about fields.|
|» name|body|string|true|Project name.|
|» description|body|string|true|Project description.|

<h3 id="edit-project-about-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## create team

<a id="opIdpost-team"></a>

> Code samples

`POST /team/`

Create team.

> Body parameter

```json
{
  "creator": "1",
  "project": "1"
}
```

<h3 id="create-team-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|Team information.|
|» creator|body|string|true|Creator user id.|
|» project|body|string|true|Project id.|

> Example responses

> Created

```json
{
  "id": "1"
}
```

<h3 id="create-team-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="create-team-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|true|none|ID of created team.|

<aside class="success">
This operation does not require authentication
</aside>

## get team

<a id="opIdget-team-id"></a>

> Code samples

`GET /team/{id}`

Get team by id.

> Example responses

> OK

```json
{
  "team": {
    "id": "1",
    "project": "1",
    "users": [
      "1"
    ],
    "join_requests": [
      "1"
    ],
    "filled": false,
    "about": {
      "name": "Team A",
      "description": "This is Team A."
    }
  }
}
```

<h3 id="get-team-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="get-team-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» team|object|true|none|Team information.|
|»» id|string|true|none|Team id.|
|»» project|string|true|none|ID of project that team is for.|
|»» users|[string]|true|none|IDs of users in team.|
|»» join_requests|[string]|true|none|IDs of join requests to team.|
|»» filled|boolean|true|none|Whether team is filled or not.|
|»» about|object|true|none|Team's about fields.|
|»»» name|string|true|none|Team name.|
|»»» description|string|true|none|Team description.|

<aside class="success">
This operation does not require authentication
</aside>

## delete team

<a id="opIddelete-team-id"></a>

> Code samples

`DELETE /team/{id}`

Delete team by id.

WARNING: Teams are now automatically deleted when all users leave them. There is no reason to use this method in normal operations.

<h3 id="delete-team-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## remove user from team

<a id="opIdpatch-team-id-users-remove"></a>

> Code samples

`PATCH /team/{id}/users/remove`

Remove user from team.

> Body parameter

```json
{
  "user_id": "1"
}
```

<h3 id="remove-user-from-team-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» user_id|body|string|true|User id.|

<h3 id="remove-user-from-team-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## edit team about

<a id="opIdpatch-team-id-about"></a>

> Code samples

`PATCH /team/{id}/about`

Edit team's about fields.

> Body parameter

```json
{
  "name": "Team A",
  "description": "This is Team A."
}
```

<h3 id="edit-team-about-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|Team's new about fields.|
|» name|body|string|true|Team name.|
|» description|body|string|true|Team description.|

<h3 id="edit-team-about-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## set team filled

<a id="opIdpatch-team-id-filled"></a>

> Code samples

`PATCH /team/{id}/filled`

Set whether team is filled.
NOT IMPLEMENTED YET.

> Body parameter

```json
{
  "filled": true
}
```

<h3 id="set-team-filled-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» filled|body|boolean|true|Whether team is filled.|

<h3 id="set-team-filled-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>

## create user

<a id="opIdpost-user"></a>

> Code samples

`POST /user/`

Create user.

> Body parameter

```json
{
  "username": "jdoe",
  "password": "abc123",
  "about": {
    "name": "John Doe",
    "email": "jdoe@ncsu.edu",
    "phone": "9999999999",
    "bio": "I am cool."
  }
}
```

<h3 id="create-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|User information.|
|» username|body|string|true|User username.|
|» password|body|string|true|User password.|
|» about|body|object|true|User's about fields.|
|»» name|body|string|true|User name.|
|»» email|body|string|true|User email.|
|»» phone|body|string|true|User phone.|
|»» bio|body|string|true|User bio.|

> Example responses

> Created

```json
{
  "id": "1"
}
```

<h3 id="create-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict: User already exists.|None|

<h3 id="create-user-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|true|none|ID of created user.|

<aside class="success">
This operation does not require authentication
</aside>

## get user

<a id="opIdget-user-id"></a>

> Code samples

`GET /user/{id}`

Get user by id.

> Example responses

> OK

```json
{
  "user": {
    "id": "1",
    "username": "jdoe",
    "password": "abc123",
    "teams": [
      "1"
    ],
    "projects": [
      "1"
    ],
    "join_requests": [
      "1"
    ],
    "about": {
      "name": "John Doe",
      "email": "jdoe@ncsu.edu",
      "phone": "9999999999",
      "bio": "I am cool."
    }
  }
}
```

<h3 id="get-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="get-user-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» user|object|true|none|User information.|
|»» id|string|true|none|User id.|
|»» username|string|true|none|User username.|
|»» password|string|true|none|User password.|
|»» teams|[string]|true|none|IDs of teams that user is in.|
|»» projects|[string]|true|none|IDs of projects that user is in.|
|»» join_requests|[string]|true|none|IDs of join requests created by the user.|
|»» about|object|true|none|User's about fields.|
|»»» name|string|true|none|User name.|
|»»» email|string|true|none|User email.|
|»»» phone|string|true|none|User phone.|
|»»» bio|string|true|none|User bio.|

<aside class="success">
This operation does not require authentication
</aside>

## delete user

<a id="opIddelete-user-id"></a>

> Code samples

`DELETE /user/{id}`

Delete user by id.
NOT YET IMPLEMENTED.

<h3 id="delete-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|

<aside class="success">
This operation does not require authentication
</aside>

## edit user about

<a id="opIdpatch-user-id-about"></a>

> Code samples

`PATCH /user/{id}/about`

Edit user's about fields by id.

> Body parameter

```json
{
  "name": "John Doe",
  "email": "jdoe@ncsu.edu",
  "phone": "9999999999",
  "bio": "I am cool."
}
```

<h3 id="edit-user-about-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|User's new about fields.|
|» name|body|string|true|User name.|
|» email|body|string|true|User email.|
|» phone|body|string|true|User phone.|
|» bio|body|string|true|User bio.|

<h3 id="edit-user-about-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<aside class="success">
This operation does not require authentication
</aside>


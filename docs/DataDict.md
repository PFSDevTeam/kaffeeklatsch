**user_access table**
|Field          | Type         | Definition     | Nullable|
|:------------- |:---------------:|:---------------|:---------------|:---------------:|
|username|text|username provided at registration|No|
|password|text|stored hashed password provided at registration|No|

**user table**
|Field          | Type         | Definition     | Nullable|
|:------------- |:---------------:|:---------------|:---------------|:---------------:|
|username|text|username provided at registration|No|
|avatar|text|url for the selected avatar|Yes|
|first_name|text|user's provided first name|Yes|
|last_name|text|user's provided last name|Yes|
|communities|text|a list of the users followed communities|Yes|
|users_following|text|a list of the users this user is following|Yes|

**post table**
|Field          | Type         | Definition     | Nullable|
|:------------- |:---------------:|:---------------|:---------------|:---------------:|
|title|text|the title string for the post|No|
|content|text|the text content of the post|No|
|posting user|text|username of the orignal poster|No|
|posted date|text|date the original post was created ("YYYY-MM-DD HH:MM:SS.SSS")|No|
|community|text|the community id of the post if applicable|Yes|

**community table**
|Field          | Type         | Definition     | Nullable|
|:------------- |:---------------:|:---------------|:---------------|:---------------:|
|community_id|text|the id tag for a particular community|No|
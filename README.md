# Database Table Exporter API

Export any database table to CSV or Excel file.  
Just add your database connection URI to the env file and start exporting.  
You can add more than one database connection URI in json format.  
Supports large tables, the export task will be run in the background.  
Only support PostgreSQL databases for now.  

### Requirements:

```
docker
```

### Run:

```
cp config/.env.example config/.env
docker compose up --build -d
```

### Docs:

```
OpenAPI: http://localhost:8000/docs
Postman: postman_collection.json in the project root.
```

### Endpoints:

```http request
POST  /export                # start export task
GET   /status/{task_id}      # check task status
GET   /download/{file_name}  # download file
```

### Example Requests/Responses:

#### Request:
```http request
POST /export

Body:
{
    "database": "test_db",
    "table": "table1",
    "fields": ["column1", "column2"], # optional, default all fields
    "file_type": "csv"                # csv or excel, default csv
}
```

#### Response:
```json
{
    "task_id": "f50f4527-e6bb-4787-9a39-d2cac2d8d43d"
}
```

#### Request:
```http request
GET /status/f50f4527-e6bb-4787-9a39-d2cac2d8d43d
```

#### Response:
```json
{
    "status": "SUCCESS"
}
```

#### Request:
```http request
GET /download/f50f4527-e6bb-4787-9a39-d2cac2d8d43d.csv
```

#### Response (File):
```
column1,column2
a1,a2
b1,b2
```

# Mock HTTP Server

Makes it possible to integrate your service with an API that still does not exist.

## How to run

```
FLASK_APP=mock_server.py flask run
```

## Endpoints

### Generic
```
/default?sleep_seconds=1&status_code=200
```

### Examples

``` 
/timestamp
/random
```
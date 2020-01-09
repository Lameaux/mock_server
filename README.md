# Mock HTTP Server

Makes it possible to integrate your service with an API that still does not exist.

## How to run

### Localhost
```
FLASK_APP=mock_server.py FLASK_DEBUG=True flask run
```

### Heroku

https://showmax-mock-server.herokuapp.com/

## Feature Flag

Enable FF `t62161_mock_response` to route requests to Mock Server.

## DStv

### Users

| Identity Number | Customer Number | Eligibility |
|---|---|---|
| 3409045056082 | 38739503 | IsEligible |
| 7702050146087 | 38752143 | HasActiveAgreement |


### Endpoints

```
/dstvza/GetOAuthTokenAPI
/dstvza/ShowmaxExtApi/partners/showmax/ZAF/customers/<int:customer_number>/activations
/dstvza/ShowmaxExtApi/partners/showmax/ZAF/customers/<int:customer_number>/agreements/eligibility
/dstvza/ShowmaxExtApi/partners/showmax/agreements
/dstvza/ShowmaxExtApi/partners/showmax/agreements/<string:charge_token>
/dstvza/ShowmaxExtApi/partners/showmax/agreements/<string:charge_token>/charges
/dstvza/showmaxperformanceapi/zaf/customers/customer-detail/identityNumber=<int:identity_number>
```

## Demo Endpoints

### Generic
```
/generic?sleep_seconds=1&status_code=200
```

### Examples

``` 
/timestamp
/random
```
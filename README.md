# Giulia Task Python E-Com app

## How to:


### 1. Set-up local env:

```
pip install --upgrade pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r src/requirements.txt
```

### 2. Build docker image on local:

```
sudo docker build . -t giuliaioana/python_flask_app:0.1
```

### 3. Run all on local:

```
docker-compose up -d
```

### 3. Check if is running as expected:

```
docker ps -a
docker logs app
```

```
curl http://localhost:5000/
```
Expected output:
```127.0.0.1 - - [22/Oct/2021 17:55:53] "GET / HTTP/1.1" 404 -
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```
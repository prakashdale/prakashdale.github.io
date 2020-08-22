---
layout: post
title:  Performing HTTP request in Python
comments: true
categories: [Python]
excerpt: Basics of HTTP and requests library in Python to make different types of requests
---

`requests` library in Python can be used to send http *get* request (e.g. download an image), pass an argument to the request, perform *post* request

## Using GET request

You can retrieve the data from specific resource by using `request.get('url')` which returns response object.

```python
import requests
r = requests.get('http://url-to-your-resource')
```

## Downloading and saving an image

```python
import requests
resp = requests.get('https://imgs.xkcd.com/comics/making_progress.png)
with open('e:\prakash\temp\image.png', 'wb') as f:
    f.write(resp.content)
```

## Using POST request

```python
import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.text)
```
---
layout: post
title:  Video streaming with Flask
comments: true
categories: [OpenCV, Flask, Python]
excerpt: Live streaming using Flask
---

## What is streaming?

Streaming is a technique in which the server provides response to a request in chunks. This might be useful in couple of use cases.
- **Very large responses** Having to assemble a response in memory only to return it to the client can be inefficient for very large responses. An alternative would be to write response to disk and then return file with `flask.send_file()`, but that adds I/O to the mix. Providing the response in small portions is a much better solution, assuming the data can be generated in chunks.
- **Real time data** For some applications a request may need to return data that comes from a real time source. A pretty good example of this is a real time video or audio feed. A lot of security cameras use this technique to stream video to web browser.

## Code Path

https://github.com/prakashdale/prakashdale.github.io/tree/master/src/video_streaming/with_flask_opencv

## Setup

- Open anaconda command prompt
- Activate conda environment `conda activate flaskvideostream`
- Install packages using
  - `pip install -r requirements.txt`
  - `pip install -r requirements-opencv.txt`
- Set enviroment veriable on command prompt `set CAMERA=opencv`
- Run app using command `python app.py`
- Open browser and navigate to [http://localhost:5000](http://localhost:5000)

## For Production style deployment on Windows

- install `pip install waitress`
- `set CAMERA=opencv`
- Run `waitress-serve --listen=*:5000 app:app`
- Open browser and navigate to [http://localhost:5000](http://localhost:5000)



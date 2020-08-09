## To run

- Open anaconda command prompt
- Activate conda environment `conda activate flaskvideostream`
- Install packages using
  - `pip install -r requirements.txt`
  - `pip install -r requirements-opencv.txt`
- Set enviroment veriable on command prompt `set CAMERA=opencv`
- Run app using command `python app.py`
- Open browser and navigate to [http://localhost:5000](http://localhost:5000)

## For Production deployment on Windows

- install `pip install waitress`
- `set CAMERA=opencv`
- Run `waitress-serve --listen=*:5000 app:app`
- Open browser and navigate to [http://localhost:5000](http://localhost:5000)

## Docker

I could not get it to work using docker container. Please review Dockerfile and see if you find any issue. Image builds successfully but not able to run container. Perhaps issue is with sharing webcamera of the machine with docker container.

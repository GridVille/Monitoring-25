This is the code for rpi visualization/data processing.

datagen.py produses fake to the the TimeScaleDB server.

app.py runs the webpage that visualzes, the templates contain different sites for the site.
Note: to open the page with that shows data from/to open http://127.0.0.1:5000/time_range .

myenv is a python virtual enviroment. to activate it run "source myenv/bin/activate" in root folder.

CREATE TABLE sensor_data (
    time TIMESTAMPZ NOT NULL,
    sensor_1 DOUBLE PRECISION,
    sensor_2 DOUBLE PRECISION,
    sensor_3 DOUBLE PRECISION,
    sensor_4 DOUBLE PRECISION,
    sensor_5 DOUBLE PRECISION,
    sensor_6 DOUBLE PRECISION,
    sensor_7 DOUBLE PRECISION,
    sensor_8 DOUBLE PRECISION,
    sensor_9 DOUBLE PRECISION,
    sensor_10 DOUBLE PRECISION,
);

The currently used templates are index1 and time_range1. The other are older versions


-TODO:
Make dependencies for python Virtual environment.

webpages:
Check off for which sensors to get data from on time_range.
,

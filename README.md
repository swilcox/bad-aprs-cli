# BADash APRS monitoring client

## Overview

This script can monitor a filtered APRS server connection and send position locations to a BADash API server as a Geo Location "job".

## Installation and Running

Install the requirements in a Python 3.6+ virtual environment like:

```
pip install -r requirements.txt
```

You must specify several environment variables for this to work:

```
export BADASH_URL=http://my-badash-api.example.com/events
export BADASH_JOB=my-badash-job-slug
export BADASH_API_KEY=a-valid-badash-api-key
```

Then, the command structure:

```
$ python aprs_cli.py MYCALLSIGN
```

Replace `MYCALLSIGN` with your call sign with either your call or your full call plus APRS extension (e.g. -9). However, note that if you use your call sign and it's shorter (KK4SW) then longer calls could match (KK4SWC). So using a full call plus is better (KK4SW-9).

The script will stop on errors or `ctrl-c`.

## Future Enhancements

* multiple call sign prefixes
* tests
* error handling (check environment, multiple packet types, connection errors)
* configurable logging

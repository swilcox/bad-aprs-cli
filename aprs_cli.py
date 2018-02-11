"""APRS Client for BADash"""
import os
import sys

import aprslib
import requests

BADASH_API_URL = os.environ.get('BADASH_API_URL', 'http://localhost:8000/events')
BADASH_API_KEY = os.environ.get('BADASH_API_KEY', '')
BADASH_JOB = os.environ.get('BADASH_JOB', '')


def send_to_badash(packet):
    """send packet data to badash"""
    response = requests.post(
        BADASH_API_URL,
        json=packet,
        headers={'X-Api-Key': BADASH_API_KEY}
    )
    print(response)


def aprs_callback(packet):
    """callback for aprs packet being received"""
    print("received packet: ")
    print(packet)
    packet.update(
        result=0,
        job=BADASH_JOB,
        loc={
            'lng': packet['longitude'],
            'lat': packet['latitude']
        },
    )
    print("translated packet: ")
    print(packet)
    print("sending to BADash")
    send_to_badash(packet)


def main():
    """the main function"""
    print("starting listener: ")
    print(" BADASH_API_URL: {}".format(BADASH_API_URL))
    print(" BADASH_API_KEY: {}".format(BADASH_API_KEY))
    print(" BADASH_JOB: {}".format(BADASH_JOB))
    print(" CALL SIGN: {}".format(sys.argv[1]))
    aprs = aprslib.IS('N0CALL')
    aprs.set_server('rotate.aprs.net', 14580)
    aprs.set_filter('p/{}'.format(sys.argv[1]))
    aprs.connect()
    aprs.consumer(aprs_callback)


if __name__ == '__main__':
    main()

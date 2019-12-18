import argparse
import os

import strava_local_heatmap


def heatmap_service(session_id, app_instance_path):
    # param dir
    dir = os.path.join(app_instance_path, session_id)
    # param file - the filename
    file = str(session_id)
    # setup default values
    bound = [-90, 90, -180, 180]
    csv = False
    glob = '*.gpx'
    nocdist = False
    sigma = 1
    year = 'all'
    zoom = 10
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default=dir)
    parser.add_argument('--file', default=file)
    parser.add_argument('--bound', default=bound)
    parser.add_argument('--csv', default=csv)
    parser.add_argument('--glob', default=glob)
    parser.add_argument('--nocdist', default=nocdist)
    parser.add_argument('--sigma', default=sigma)
    parser.add_argument('--year', default=year)
    parser.add_argument('--zoom', default=zoom)
    args, _ = parser.parse_known_args()
    try:
        strava_local_heatmap.main(args)
    except Exception as e:
        return e
    print("Generated a image for session: " + str(session_id))
    return "Generated"

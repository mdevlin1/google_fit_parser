## File: fit_data_parser.py
## Author: Mitchell Devlin 

import argparse
import os
import ActivityData
import xml.etree.ElementTree as ET

DISTANCE_IDX=1
TIME_S_IDX=2
CALORIES_IDX=3

def main():
    parser = argparse.ArgumentParser(description='Parse google fit data')
    parser.add_argument('data_dir', help='Pass in the google fit data directory')

    args = parser.parse_args()
    activityData = parseActivities(args.data_dir)
    
def parseActivities(fitDataDir):
    totalDistanceM = 0.0
    totalTimeS = 0.0
    totalCalories = 0.0

    for filename in os.listdir(fitDataDir):
        if 'Running' or 'Treadmill' in filename:
            xmlTree = ET.parse(os.path.join(fitDataDir, filename)).getroot()
            activityList = []
            for activity in xmlTree.iter('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap'):
                totalDistanceM += float(activity[DISTANCE_IDX].text)
                totalTimeS += float(activity[TIME_S_IDX].text)
                totalCalories += float(activity[CALORIES_IDX].text)
    
    print("Total distance (meters):", totalDistanceM)
    print("Total duration (seconds):", totalTimeS)
    print("Total calories: (kcal):", totalCalories)

if __name__ == '__main__':
    main() 

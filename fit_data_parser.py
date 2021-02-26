## File: fit_data_parser.py
## Author: Mitchell Devlin 

import argparse
import os
import ActivityData
import xml.etree.ElementTree as ET

def main():
    parser = argparse.ArgumentParser(description='Parse google fit data')
    parser.add_argument('data_dir', help='Pass in the google fit data directory')

    args = parser.parse_args()
    activityData = parseRuns(args.data_dir)
    
def parseActivities(fitDataDir):
    for filename in os.listdir(fitDataDir):
        if 'Running' or 'Treadmill' in filename:
            xmlTree = ET.parse(os.path.join(fitDataDir, filename))
            activityList = []
            for activity in xmlTree.iter('Lap'):
                distance_m = activity['DistanceMeters'].text
                time_s = activity['TotalTimeSeconds'].text
                calories = activity['Calories'].text
        

if __name__ == '__main__':
    main() 

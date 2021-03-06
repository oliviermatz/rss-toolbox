#!/usr/bin/env python3

import sys
import datetime
import xml.etree.ElementTree as ET

tree = ET.parse(sys.stdin)
root = tree.getroot()

def parse_date(s):
    try:
        return datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
    except:
        return datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')

for item in root.find('channel').findall('item'):
    guidNode = item.find('guid')
    if guidNode == None:
        guidNode = item.find('link')
    sys.stdout.write(guidNode.text.strip()); sys.stdout.write('\t')
    date = item.find('pubDate').text
    timestamp = int(parse_date(date).timestamp())
    sys.stdout.write(str(timestamp)); sys.stdout.write('\t')
    sys.stdout.write(item.find('title').text.strip()); sys.stdout.write('\t')
    sys.stdout.write(item.find('enclosure').attrib['url']); sys.stdout.write('\n')

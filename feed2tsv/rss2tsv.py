#!/usr/bin/env python3

import sys
import datetime
import xml.etree.ElementTree as ET

tree = ET.parse(sys.stdin)
root = tree.getroot()

def parse_date(s):
    try:
        return datetime.datetime.strptime(s.strip(), '%a, %d %b %Y %H:%M:%S %z')
    except:
        return datetime.datetime.strptime(s.strip(), '%a, %d %b %Y %H:%M:%S %Z')

for item in root.find('channel').findall('item'):
    linkNode = item.find('link')
    if linkNode == None:
        continue
    guidNode = item.find('guid')
    if guidNode == None:
        guidNode = linkNode
    sys.stdout.write(guidNode.text.strip()); sys.stdout.write('\t')
    date = item.find('pubDate').text
    timestamp = int(parse_date(date).timestamp())
    sys.stdout.write(str(timestamp)); sys.stdout.write('\t')
    sys.stdout.write(item.find('title').text.strip()); sys.stdout.write('\t')
    sys.stdout.write(item.find('link').text.strip()); sys.stdout.write('\n')

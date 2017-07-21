import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd

xml_data = 'export.xml'


def xml2df(xml_data):
    tree = ET.parse(xml_data)
    root = tree.getroot()
    all_records = []
    headers = []
    for i, child in enumerate(root):
        record = []
        for subchild in child:
            record.append(subchild.text)
            if subchild.tag not in headers:
                headers.append(subchild.tag)
        all_records.append(record)
    print all_records
    return pd.DataFrame(all_records, columns=headers)

xml2df(xml_data).to_csv("health.csv")


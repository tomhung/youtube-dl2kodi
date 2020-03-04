import codecs
import getopt
import json
import os
import sys
from datetime import datetime
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring


def main(argv):
    filename = ""

    try:
        opts, args = getopt.getopt(argv, "h:f:", ["file="])
    except getopt.GetoptError:
        print('youtube-dl2kodi.py -f <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('youtube-dl2kodi.py -f <inputfile>')
            sys.exit()
        elif opt in ("-f", "--file"):
            filename = arg

    base_file = os.path.splitext(os.path.basename(filename))[0]
    filejson = f"{base_file}.info.json"
    with open(filejson) as data_file:
        data = json.load(data_file)

    premiered_date = datetime.strptime(data['upload_date'], '%Y%m%d').strftime('%Y-%m-%d')
    root = Element("episodedetails")
    title = SubElement(root, "title")
    episode = SubElement(root, "episode")
    premiered = SubElement(root, "premiered")
    plot = SubElement(root, "plot")

    title.text = f"{data['fulltitle']}"
    episode.text = f"{data['playlist_index']}"
    premiered.text = f"{premiered_date}"
    plot.text = f"{data['uploader_url']}\n{data['description']}\n{data['playlist_title']}"

    with codecs.open(filename=f"{base_file}.nfo", mode="w", encoding="utf-8") as file:
        file.write(prettify(root))


def prettify(elem):
    xml_string = tostring(elem, "utf-8")
    minidom_parsed = minidom.parseString(xml_string)
    return minidom_parsed.toprettyxml(indent="  ")


if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python
import sys, getopt, json, os

def main(argv):
   global nfotype
   global filemovie
   try:
      opts, args = getopt.getopt(argv,"ht:f:",["tfile=","ffile="])
   except getopt.GetoptError:
      print 'youtube-dl2kodi.py -t <inputfile> -f <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'youtube-dl2kodi.py -t <inputfile> -f <outputfile>'
         sys.exit()
      elif opt in ("-t", "--tfile"):
         nfotype = arg
      elif opt in ("-f", "--ffile"):
         filemovie = arg
         filemovie = filemovie.replace("'","")
   print 'NFO Type is "', nfotype
   print 'JSON file is "', filemovie

if __name__ == "__main__":
   main(sys.argv[1:])
filemoviefullname = filemovie
filemovie = os.path.splitext(filemovie)[0]
filemovieext = os.path.splitext(filemovie)[1]
filejson = filemovie + ".info.json"
filenfo = filemovie + ".nfo"
with open(filejson) as data_file:
    data = json.load(data_file)
#print data
video_title = data['fulltitle']
video_url = data['uploader_url']
video_plot = data['description']
video_playlist_index = data['playlist_index']
video_playlist_title = data['playlist_title']

if nfotype == "movie":
  filenfo = filemovie+"-part"+video_playlist_index + ".nfo"
  os.rename(filemoviefullname, filemovie+"-part"+video_playlist_index+"."+filemovieext)
  nfo = """<?xml version="1.0" ?>
  <movie>
    <title>%s</title>
  </movie>""" % (video_title)

if nfotype == "tvshow":
  nfo = """<?xml version=\"1.0\" ?>
  <episodedetails>
    <title>%s</title>
    <season>1</season>
    <episode>%s</episode>
    <plot>%s\n%s\n%s</plot>
  </episodedetails>""" % (video_title, video_playlist_index, video_url, video_plot, video_playlist_title)

  with open(filenfo, "w") as f:
      f.write(nfo)
os.remove(filejson)

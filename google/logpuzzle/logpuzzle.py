#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sort_last(path_name):
  match = re.search(r'\w+-\w+-(\w+)\.', path_name)
  return match.group(1) if match else path_name

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # Solution by Vignesh Durairaj

  url_list, hostname = [], filename[filename.index('_') + 1:]
  logfile = open(filename, 'r')
  for line in logfile:
    match = re.search(r'GET\s(\S+)\sHTTP', line)
    if match:
      url_path = 'http://' + hostname + match.group(1)
      if 'puzzle' in url_path and url_path not in url_list : url_list.append(url_path)
  logfile.close()

  return sorted(url_list, key=sort_last)
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # Solution by Vignesh Durairaj
  # Create the destination directory if not exists
  if not os.path.exists(dest_dir): os.makedirs(dest_dir)

  # Create the HTML file and add image in the order of specified order in IMG tag
  f = open(os.path.join(dest_dir, 'index.html'), 'w')
  f.write('<html><body>')
  for i in range(0, len(img_urls)):
    print('Downloading image # ' + str(i) + ' from : ' + img_urls[i])
    urllib.urlretrieve(img_urls[i], os.path.join(dest_dir, 'img' + str(i) + '.jpg'))
    f.write('<img src = "img' + str(i) + '.jpg">')
  
  f.write('</body</html>')
  f.close()

def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()

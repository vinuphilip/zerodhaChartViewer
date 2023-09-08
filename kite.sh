#!/bin/bash

# Open the URL in Google Chrome
#open -a "Google Chrome" "https://example.com"

# Wait for a few seconds (adjust the delay as needed)
#sleep 5  # This will wait for 5 seconds

# Close the tab using AppleScript and osascript
#osascript -e 'tell application "Google Chrome" to close (active tab of window 1)'


cat  /Users/vinuphilip/Documents/SublimeDocs/stock_url  | grep -v '^#' | while read url
do

 open -a /Applications/Google\ Chrome.app $url

 echo $url
 sleep 4

 osascript -e 'tell application "Google Chrome" to close (active tab of window 1)'
done

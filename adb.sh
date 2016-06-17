#!/bin/bash
a="hello world"
echo "this is the adb.sh $a"
adb root
adb shell chmod -R 777 /system/lib/nutlet_armtz/

adb shell ./system/lib/nutlet_armtz/nutlet_helloworld

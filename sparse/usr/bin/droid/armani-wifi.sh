#!/bin/sh

/system/bin/wcnss_service &
sleep 2
/sbin/insmod /lib/modules/3.4*/wlan.ko

#!/bin/bash

if [ "$1" != "" ]; then
	echo "joining network: $2 with interface $1"
	#sudo ifdown $1
	sudo su <<EOF
ifdown $1
#ifup $1
rm /var/run/wpa_supplicant/$1
wpa_supplicant -i $1 -c /home/pi/$1.conf -Dnl80211,wext
dhclient $1
EOF

	iwconfig
else 
	echo "Usage: join_network.sh device ssid password"
fi


#!/bin/bash
while true; do
	python scanner.py
	echo "copying"
	cp devices.db ../Server/Location0.db
	echo "waiting for 5 min, end now if you need to"
	sleep 300
done

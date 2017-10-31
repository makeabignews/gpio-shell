#!/bin/bash
if [ ! -d /sys/class/gpio_sw/gpio$1 ] ;then
  echo $1 > /sys/class/gpio_sw/export
fi
echo out > /sys/class/gpio_sw/gpio$1/direction
echo $2 > /sys/class/gpio_sw/gpio$1/value

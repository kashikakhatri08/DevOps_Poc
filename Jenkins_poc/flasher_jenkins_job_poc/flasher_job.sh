#!/bin/sh

flash_hw_ac(){

echo "-- shell_script method flash_hw_ac --"

}


flash_device(){

echo "-- shell_script method flash_device -- "
reboot_device $1 $2 $3
}


reboot_device(){

echo "-- shell_script method reboot_device --
serial_number : $1 
hardware_number : $2
product_directory_path : $3"

}


wait_for_device_boot_completed(){

echo "-- shell_script method wait_for_device_boot_completed--"

}


init_devices(){

echo "-- shell_script method init_devices"

}


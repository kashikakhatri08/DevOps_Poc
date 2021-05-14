import os
import yaml
import subprocess
import sys


def init_environment():
    global product_name
    print("--init_environment function--")
    print("\n")
    flasher_yaml_file = open("/home/kashika/Jenkins_testing/flasher_jenkins_job_poc/flasher_job.yaml")
    parsed_yaml_file = yaml.load(flasher_yaml_file, Loader=yaml.FullLoader)
    input_data = sys.argv[1]
    product_name = parsed_yaml_file[input_data]
    # cmd ='bash -c "source ~/Jenkins_testing/flasher_job.sh && flash_hw_ac {} {} {} " '.format(asterix_serial,asterix_hardware,asterix_path)
    #flasher_script_file=subprocess.getoutput(cmd)
    #rint(flasher_script_file)


def flash_hw_ac():
    print("-- python_script's flash_hw_ac function --")
    cmd = 'bash -c "source ~/Jenkins_testing/flasher_jenkins_job_poc/flasher_job.sh && flash_hw_ac " '
    flasher_script_file = subprocess.getoutput(cmd)
    print(flasher_script_file)
    print("\n")


def flash_device(strng):
    print("-- python_script's flash_device function --")
    cmd = 'bash -c "source ~/Jenkins_testing/flasher_jenkins_job_poc/flasher_job.sh && flash_device {} " '.format(strng)
    flasher_script_file = subprocess.getoutput(cmd)
    print(flasher_script_file)
    print("\n")


def reboot_device():
    print("-- python_script's reboot_device function --")
    print("\n")


def wait_for_device_boot_completed():
    print("-- python_script's wait_for_device_boot_completed function --")
    cmd = 'bash -c "source ~/Jenkins_testing/flasher_jenkins_job_poc/flasher_job.sh && wait_for_device_boot_completed " '
    flasher_script_file = subprocess.getoutput(cmd)
    print(flasher_script_file)
    print("\n")


def init_devices():
    print("-- python_script's init_devices function --")
    cmd = 'bash -c "source ~/Jenkins_testing/flasher_jenkins_job_poc/flasher_job.sh && init_devices " '
    flasher_script_file = subprocess.getoutput(cmd)
    print(flasher_script_file)
    print("\n")


def main():
    print("--main function--")
    print("\n")
    global serial
    global hardware
    global path
    init_environment()
    product_detail=list(product_name.values())
    strng=" "
    for i in range(0,3):

        strng += product_detail[i] + " "

    serial = product_detail[0]
    hardware = product_detail[1]
    path = product_detail[2]


    flash_hw_ac()
    # flash_device(serial,hardware,path)
    flash_device(strng)
    reboot_device()
    wait_for_device_boot_completed()
    init_devices()


if __name__ == '__main__':
    main()


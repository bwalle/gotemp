# gotemp
Some script and description to read the temperature of a Vernier Go!Temp Temperatur Sensor

## Setup

### Prevent usbhid from capturing the device

Create a file `/etc/modprobe.d/go_temp.conf` with following contents:

```
options usbhid options quirks=0x08f7:0x0002:0x4
```

You have to re-create your `initramfs` (on Arch Linux: `mkinitcpio -p linux`) and reboot to apply that change! If you don't have a USB keyboard and mouse, you can also unload or blacklist the `usbhid` module.

### Setup ldusb

```
# modprobe ldusb
# echo  '08f7 0002' > /sys/bus/usb/drivers/ldusb/new_id
```

## Using the Python script

After that you can run `gotemp-ldusb.py` as root. Alternatively change the permission of `/dev/ldusb0`.



%define device armani
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi 1S
%define dcd_path ./
%define pixel_ratio 1.0
%define have_modem 1
%define android_config \
#define QCOM_BSP 1\
%{nil}
%include droid-configs-device/droid-configs.inc

# Audio hook

## What is audio hook?
Audio hook is an application that 
allows you to get sound from an input device and 
record it into an audio file.

## Dependencies
> **alsa**<br>**pulse-audio**<br>**python3.10**

## How to Setup?
> **Packet managers**

+ **Apt**
  - ```bash
    sudo apt-get update
    sudo apt-get install pavucontrol 
    ```
+ **Dnf**
  - ```bash
    sudo dnf makecache
    sudo dnf -y install pavucontrol
    ```
+ **Pacman**
  - ```bash
     sudo pacman -Syy
     sudo pacman -S pavucontrol
    ```
+ **Portage**
  - ```bash
    sudo emerge --sync
    sudo emerge -s pavucontrol
    sudo emerge -pv pavucontrol
    sudo emerge pavucontrol
    ```
+ **Yum**
  - ```bash
    sudo yum makecache
    sudo yum -y install pavucontrol
    ```

> **Select default input device**

![Screenshot_20220607_182425](https://user-images.githubusercontent.com/70020258/172422911-1dc5e9d3-408c-40f8-8d70-ff917560b990.png)

## How to build?
> **Setup venv**
  - ```bash
    python3.10 -m venv venv
    ```
  - ```bash
    source venv/bin/activate
    ```
> **Setup requirements**
  - ```bash
    pip install -r requirements.txt
    ```
## Usage
> **Command list**
  - ```bash
    python3.10 main.py --help
    ```
    **Output:<br> usage: main.py [-h] [-s SPLIT_AFTER]<br>
    options: -h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit  
    -s SPLIT_AFTER, --split-after SPLIT_AFTER&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; split after this number of seconds**<br>
    **Default parameters:<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;split_after equals 30 seconds**
> **Run**
  - ```bash
    python3.10 main.py
    ```

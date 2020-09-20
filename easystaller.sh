#Colors
#-----------------
RED='\033[0;31m'
BLUE='\033[;34m'
GREEN='\033[;32m'
YELLOW='\033[1;33m'
NOCOLOR='\033[0m'
DARKGRAY='\033[1;30m'
#------------------

#APT packages installation script
echo -e "${YELLOW}Easy installation script made by:${BLUE} PierringShot${NOCOLOR}" && echo -e "${RED}Please use as a ROOT user${NOCOLOR}"
#Starting package installation.
echo -e "${GREEN}Installation started...${DARKGRAY}"
apt-get install python python3 python-pip python3-pip curl tilix xfce4 xrdp xorg nano ruby php unzip tor maltego burpsuite wireshark aircrack-ng hydra nmap beef-xss nikto gvfs gvfs-common gvfs-daemons gvfs-libs gconf-service gconf2 gconf2-common gvfs-bin psmisc gnome-tweak-tool metasploit-framework codeblocks
echo -e "${GREEN}python python3 python-pip python3-pip curl tilix xfce4 xrdp xorg nano ruby php unzip tor maltego burpsuite wireshark aircrack-ng hydra nmap beef-xss nikto gvfs gvfs-common gvfs-daemons gvfs-libs gconf-service gconf2 gconf2-common gvfs-bin psmisc gnome-tweak-tool metasploit-framework codeblocks installed succecfully.${DARKGRAY}"
#Finishing with update
echo -e "${RED}Finishing with update/upgrade/autoremove.${NOCOLOR}"
apt-get update && apt-get full-upgrade && apt autoremove
echo -e "${GREEN}Succecfully finished all installation"




























add-apt-repository --yes ppa:kicad/kicad-6.0-releases
apt update
apt install -y --install-recommends kicad
apt update
apt install -y python3 python3-pip npm
npm install -g easyeda2kicad
apt install -y libgtk2.0-dev openctm-tools

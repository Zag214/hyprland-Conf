import os
from pathlib import Path

scriptDir = Path(__file__).resolve()

os.system("git clone https://aur.archlinux.org/yay.git")
os.system(f"cd {scriptDir}/yay")
os.system("makepkg -si")
os.system(f"rm -rf {scriptDir}/yay")

os.system("yay -S zapret")
os.system("sudo pacman -S nwg-look ttf-ubuntu-mono-nerd ttf-jetbrains-mono-nerd mako nvim")

os.system(f"cp -r {scriptDir} ~/.config")
os.system(f"cd -r {scriptDir}/config /opt/zapret")
os.system("rm -rf ~/.config/install.py")
os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

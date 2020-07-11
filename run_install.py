from pathlib import Path
from lib import utils
from lib import install


# Logo
utils.printLogo('2.2')

# Home path
dir_home = Path.home()
p_vim = Path('./vimsetting/vim')
p_vimrc = Path('./vimsetting/vimrc')

# Clean current vim settings
install.cleanVimSetting(dir_home)

# Installation
install.installFitvim(dir_home, p_vim, p_vimrc)

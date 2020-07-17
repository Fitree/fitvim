import os
import sys
import shutil

from pathlib import Path
from lib import utils


def cleanVimSetting(dir_home):
    vim_exists = (dir_home/'.vim').exists()
    vimrc_exists = (dir_home/'.vimrc').exists()
    if vim_exists|vimrc_exists:
        print('Vim setting already exists!')
        if vim_exists:
            print('\t~/.vim')
        if vimrc_exists:
            print('\t~/.vimrc')
        rm = utils.askYN('Do you want to erase all and proceed?')
        if rm:
            if vim_exists:
                shutil.rmtree(dir_home/'.vim')
            if vimrc_exists:
                (dir_home/'.vimrc').unlink()
        else:
            print('Installation terminated.')
            sys.exit()


def installFitvim(dir_home, p_vim, p_vimrc):
    shutil.copytree(p_vim, dir_home/'.vim')
    shutil.copy(p_vimrc, dir_home/'.vimrc')

    os.system('curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')
    os.system('vim +PlugInstall +qall')

    print('\nInstallation done!')

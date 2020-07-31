# Quick Start Guide
## Requirements
* vim > 7.4.503 (> 8.0.0027 recommended)
    * If you use Neovim, version dosen't matter
* git (terminal version)
* Curl
* Python 3

## Recommendation
* I recommend you to use neovim with python module for the full feature.

### Neovim installation
For Ubuntu
~~~
sudo apt install neovim
~~~
For OsX
~~~
brew install neovim
~~~

### Neovim python module installation
~~~
pip install neovim
~~~
* Since this method uses python package manager **pip** to install python module for neovim, you should do this again when you reinstall or change python virtual envirionment (e.g. via pyenv).
* There are other ways to instll python moduel for neovim. See https://github.com/neovim/neovim/wiki/Installing-Neovim.


## Installation
1. Clone repository
~~~
git clone https://github.com/Fitree/fitvim.git
~~~

2. Run 'run_install.py' using python 3 and follow instructions
~~~
cd fitvim
python3 run_install.py
~~~

3. (For neovim users) Use vim setting files as neovim setting.
Add follow lines in your neovim **init.vim** file (see original documnet: https://neovim.io/doc/user/nvim.html#nvim-from-vim).
~~~
set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath
source ~/.vimrc
~~~

# Shortcuts
Just press <SPC> and fitvim displays available keybindings in popup except basic shortcusts (see below).
## Basic shortcuts
* **shift+left, rithgt:** move to the end of the line
* **shift+up, down:** half page scroll
* **ctrl+arrow:** navigate between windows
* **{:** move to the left buffer
* **}:** move to the right buffer
* **crtl-n**: JEDI-VIM's autocomplete
## <SPC>-related shortcuts
* **<SPC>-b**: buffer
   * **-d**: delete-buffer
   * **-e**: BufExplorer
   * **-n**: new-empty-buffer
   * **-s**: BufExplorerHorizontalSplit
   * **-t**: ToggleBufExplorer
   * **-v**: BufexplorerVerticalSplit
* **<SPC>-c**: code(python)
   * **-d**: goto
   * **-g**: goto-assignments
   * **-k**: show-documentation
   * **-n**: usages
   * **-r**: rename-variables
   * **-s**: stubs
* **<SPC>-f**: file
   * **-d**: open-vimrc
   * **-s**: save-current-buffer
   * **-S**: save-all-buffers
   * **-t**: toggle-NERDTree
* **<SPC>-w**: window
   * **-=**: balance-window
   * **-d**: delete-window
   * **-s**: split-window-below
   * **-v**: split-window-right
* **<SPC>-q**: quti vi

# Included plugins
* nerdtree
* vim-airline
* neomake
* vim-gitgutter
* vim-fugitive
* bullets.vim
* jedi-vim
* indentline
* vim-devicons
* vim-commentary

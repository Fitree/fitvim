# Update notes
## Ver 2.0 (20200706)
* Most of shortcuts are changed to **space** based.
   * If you want previous shortcuts, clone this version: https://github.com/Fitree/fitvim/tree/03856accbc8dee568534767d2f43f52d71080a5e. However, JEDI-VIM features are not available on this version.
* JEDI-VIM pulugin is added.
   * By default, auto-completion function of JEDI-VIM is disabled. If you want this feature, see **JEDI-VIM features** section.
## Ver 2.1 (20200707)
* Automatic function call signature pop up (JEDI-VIM feature) is disabled since it's laggy. If you want this feature, add follow line in your **.vimrc** file.
~~~
let g:jedi#show_call_signatures = 0
~~~

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
* **A-B** means press **A** and **B** sequentially.
* **A+B** means press **B** while holding **A**.
## Common
* **shift+left, rithgt:** move to the end of the line
* **shift+up, down:** half page scroll
    * This shortcut changes mode to normal mode only in insert mode.
## Normal mode
* **space-q:** save all buffers and quit vim
* **space-w:** save all buffers
* **ctrl+arrow:** move between windows
* **space+f:** toggle filetree
* **{:** move to the left buffer
* **}:** move to the right buffer
* **space-d-b:** delete current buffer
* **space-r:** run current python script
## JEDI-VIM features
* **\\-g:** typical goto function
* **\\-d:** goto definition (follow identifier as far as possible, includes imports and statements)
* **\\-s:** goto (typing) stub
* **K:** show documentation/Pydoc K (shows a popup with assignments)
* **\\-r:** renaming
* **\\-n:** usages(shows all the usages of a name)
* Open module, e.g. :Pyimport os (opens the os module)

In FITVIM, autocompletion function of jedi-vim is disabled. If you want jedi-vim autocompletion, erase follow line in .vimrc file.
~~~
let g:jedi#completions_enabled = 0
~~~
For more information about jedi-vim, see: https://github.com/davidhalter/jedi-vim

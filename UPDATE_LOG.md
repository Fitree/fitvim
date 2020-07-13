# 20200706
* Most of shortcuts are changed to **space** based.
   * If you want previous shortcuts, clone this version: https://github.com/Fitree/fitvim/tree/03856accbc8dee568534767d2f43f52d71080a5e. However, JEDI-VIM features are not available on this version.
* JEDI-VIM pulugin is added.
   * By default, auto-completion function of JEDI-VIM is disabled. If you want this feature, see **JEDI-VIM features** section.

# 20200707
* Automatic function call signature pop up (JEDI-VIM feature) is disabled since it's laggy. If you want this feature, add follow line in your **.vimrc** file.
~~~
let g:jedi#show_call_signatures = 0
~~~

# 20200711
* Automatic function call signature pop up (JEDI-VIM feature) is enabled as a default. Shows function call signature on status line.
* Colorscheme tuning.
* Change vim plugin manager from **Vundle** to **Plug**.

# 20200713
* Automatic function call signature pop up (JEDI-VIM feature) is disabled. It's still laggy.

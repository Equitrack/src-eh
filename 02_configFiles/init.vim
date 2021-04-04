"Muestra los números de lineas
set number

" Muestra el número de lineas relativo
set relativenumber

" Es el ancho de la columna, que muestra los números
set numberwidth=1

" Si se copia texto dentro del clipboard, no lo tomará el sistema operativo
set clipboard=unnamed

" Resalta texto en la sitáxis de vim
syntax on

" Mostrar los comandos que se están ejecutando
set showcmd

" Muestra siempre la posición en la barra inferior
set ruler

" El tipo de codificación
set encoding=utf-8

" Muestra el paréntesis que cierra/abre, respecto al que se sobrepone el cursor
set showmatch

" Al usar el tabulador, utiliza un número de espacios
set sw=3

" Ver siempre el status de la barra inferior
set laststatus=2

" P L U G I N S

call plug#begin('~/.config/plugged')

" IDE
" Saltar entre palabras del editor
Plug 'easymotion/vim-easymotion'
" Explorador de archivos
Plug 'scrooloose/nerdtree'
" Navegación entre el fichero
Plug 'christoomey/vim-tmux-navigator'
" Indentación
Plug 'Yggdroot/indentLine'
" Indentación para yaml
Plug 'stephpy/vim-yaml'
" Autopair
Plug 'jiangmiao/auto-pairs'
" ColorScheme
Plug 'ghifarit53/tokyonight-vim'

" Airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" T H E M S
Plug 'flazz/vim-colorschemes'

call plug#end()

" SETTINGS
let mapleader = " "
let NERDTreeQuitOnOpen = 1
let g:indentLine_char = '▏'
colorscheme gruvbox
let g:airline_theme = 'base16_gruvbox_dark_hard'
let g:airline#extensions#tabline#enabled = 1

" M A P E O _ D E _ T E C L A S
"
" Establecer dos caractéres para ir a una linea/palabra del código
nmap <Leader>s		<Plug>(easymotion-s2)
" Abrir Nerdtree
nmap <Leader>n		:NERDTreeFind<CR>
" Guardar cambios en el fichero
nmap <Leader>w		:wq<CR>
" Cerrar fichero
nmap <Leader>q		:q!<CR>

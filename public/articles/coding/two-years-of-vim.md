Two Years of Vim
===
I've been using vim for two years now and I absolutely love it.

1) **It feels good.** The experience of gradually mastering a complex tool is incredibly rewarding. The closest thing I can compare it to is learning to master a character as a competitive gamer. While you're usually blundering around at first and the inputs can be frustrating, the gradual improvement in execution of combos and movements eventually leads to 

2) I'm more productive.

<hr>
Simple Remappings
---
- \-  jk -> esc
- \-  ;  -> :
- \-  space  -> <leader>
- \-  move cursor by line j and k
- \-  unmapping arrow keys

Basic Configs
---
- \-  set ignorecase
- \-  set noswapfile
- \-  set ignorecase
- \-  set ignorecase
- \-  set ignorecase

Buffer Navigation
---
Navigating tabs and splits with ease does wonders for your workflow. I took some influence from popular internet browsers and use [Ctrl + t] to instantiate a new tab with [Ctrl + n] and [Ctrl + b] to navigate to the next and previous tab. I love using vertical splits as well [:vs], but I think it feels more natural to open a split on the right.

Easier Paste
---
Two things I changed about paste.

- 1) Move the cursor to the end of the block of text after I paste it.
- 2) Don't fuck up clipboard (CTRL + V) paste

Vundle Plugins
---
Vundle is a vim plugin manager similar to Pathogen. Simply clone the github repository into ~/.vim/plugins and list plugins in your .vimrc. If you're interested in sliding the scale a little further from text editor into an IDE, there are a ton of posts out there about "Top Vim Plugins" and etc.

Here are a few of my favorites:

- \-  CTRL-P
- \-  Surround
- \-  NerdTree


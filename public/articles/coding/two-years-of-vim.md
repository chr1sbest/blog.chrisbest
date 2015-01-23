Two Years of Vim
===
I've been using vim for two years now and I absolutely love it. 

There are a ton of different reasons that I would recommend vim -- lightweight, extendable, ubiquitous, high skillcap, etc. But there is really only one reason that I come back to it every day:

**It just feels good.** 

The experience of gradually mastering a difficult tool is incredibly rewarding. The closest thing I can compare it to is learning to master a difficult character as a competitive gamer. While you're usually blundering around at first and the inputs can be frustrating, the gradual improvement in execution of combos and movements eventually leads to a particular flow that just feels *right*. For someone learning to code, I think it is of utmost importance for the tools they use to be responsive and rewarding -- the idea that it could *feel good* to write code makes it fun and positively reinforces productivity.

The learning never stops either. Even after two years, I wouldn't by any means consider myself a master of vim. I'm still finding new tricks and keystroke combos to optimize actions every week. 

Below are my favorite customizations I've made with my [.vimrc](https://github.com/chr1sbest/dotfiles/blob/master/.vimrc) and vim-related hacks I've found over the last two years.

<hr>
**Basic Mappings**
---
**Using the keystroke "jk" to exit insert mode.** 

```
inoremap jk <esc>
```

Typing "jk" is significantly easier than reaching over and pressing ESC. With the million+ times I've probably used this mapping, I've saved my left pinky over 60 miles of moving back and forth between home row and the ESC key. The only downside is accidentally exiting insert mode when typing the ultra-rare letter combination of "jk" (i.e. writing about Dijkstra or writing this article).

**Mapping semicolon to colon for quicker colon commands.**
```
nnoremap ; :
```
It's a huge hassle to have to press shift when executing colon commands and <s>the semicolon isn't used for anything anyways</s> I haven't needed the ; due to my lack of experience with the f and t commands (thanks [TheSploogeMcDuck](http://www.reddit.com/user/TheSploogeMcDuck)!) It isn't anywhere near 60 miles worth of movement saved, but it's saved me a lot of frustration when trying to execute colon commands.

**Move cursor by line naturally with k and j in navigation mode.**
```
nnoremap j gj
nnoremap k gk
```
Computers see lines a little differently than people do. The typical mapping of k and j moves the cursor up and down lines of non-breaking text, regardless of how many visual "lines" a single line takes up. This remapping makes vim act a little more human, k and j will now simply move the cursor up and down within non-breaking lines spanning multiple visual lines.

**Quickly move to the beginning or end of a line.**
```
nnoremap H 0
nnoremap L $
```
It's pretty common to move to the beginning or end of a line and unfortunately, 0 and $ are a little tough to reach (well, relative to H and L).

**Unmapping arrow keys.**
```
map <Left> <Nop>
map <Right> <Nop>
map <Up> <Nop>
map <Down> <Nop>
```
I've actually removed this from my .vimrc because it's served it's purpose, but it was invaluable in my early days of learning vim. Arrow keys are typically how you navigate in every other text editing interface in the world -- vim is different. Unmapping the arrow keys is like taking off training wheels and forcing yourself to learn the capabilities of vim. 

**Take me to your Space Leader.**
```
let mapleader = " "
```
Once you start to install plugins you'll want quick shortcuts to execute their commands, but you'll quickly find that every key seems to already have a purpose. This is where the `<leader`> key will come into play. Space is worthless in navigation mode, impossible to "fat-finger", and in my opinion the best candidate for a leader key.

**Buffer Navigation**
---
Navigating tabs and splits with ease does wonders for your workflow. 
```
nnoremap <C-t> :tabnew<CR>
nnoremap <C-b> :tabprevious<CR>
nnoremap <C-n> :tabnext<CR>
inoremap <C-t> <Esc>:tabnew<CR>
inoremap <C-b> <Esc>:tabprevious<CR>i
inoremap <C-n> <Esc>:tabnext<CR>i
```
I took some influence from Chrome and Firefox's interfaces and instantiate new tabs with **Ctrl + t** and cycle between them with **Ctrl + n** and **Ctrl + b**. 

```
set splitright
set splitbelow

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
```
As for splits, there are two changes that have helped smooth out my workflow. The first part makes it so new splits will open on the right (instead of left) and below (instead of above). The second portion maps Ctrl + (hjkl) to move between splits, i.e. **Ctrl + h** will move me to the left split, **Ctrl + l** will move me to the right split.

<hr>
**Plugins**
---
[Vundle](https://github.com/gmarik/Vundle.vim) is a vim plugin manager similar to Pathogen, both make it super easy to install and manage your plugins. If you're interested in sliding the scale a little further from text editor into an IDE (the dark side), there are a ton of posts out there about "Top Vim Plugins" and etc. 

[Ctrl-P](https://github.com/kien/ctrlp.vim) - My favorite vim plugin period. Full path fuzzy file, buffer, etc. finder. No more **:e ../../some_dir/some_file**, just **Ctrl + p some_file**. Super useful for opening up multiple files from different directories really quickly as well.

<img src="https://camo.githubusercontent.com/0a0b4c0d24a44d381cbad420ecb285abc2aaa4cb/687474703a2f2f692e696d6775722e636f6d2f7949796e722e706e67">

[Surround](https://github.com/tpope/vim-surround) - Tim Pope is a vim plugin beast and this is my favorite of his plugins. This plugin gives simple shortcuts to surround text with whatever, particularly useful when writing HTML. If you find this useful, definitely check out his other plugins.

[NerdTree](https://github.com/scrooloose/nerdtree) - Good for those coming from an IDE. Opens up a directory tree that you can navigate and open files up from.

[Airline](https://github.com/bling/vim-airline) - Look good feel good. This one is purely aesthetic, but it plays really well other plugins nicely.

<img src="https://raw.githubusercontent.com/wiki/bling/vim-airline/screenshots/demo.gif">

<hr>
**Vimium**
---
If you like vim and you like Chrome, [vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en) is their love child. Even if you aren't a vim user (I doubt you've read this far if this is the case), this Chrome extension will revolutionize the way you browse the web. **2.2k** votes at **5 stars**? Yeah.

<div class="videoWrapper">
<iframe width="560" height="350" src="//www.youtube.com/embed/t67Sn0RGK54" frameborder="0" allowfullscreen></iframe>
</div>

**Easily and unintrusively use your .vimrc from any computer.**
---
There are a few ways to do this, but my preferred method is cloning my dotfiles repo and executing a bash script to symlink my .vimrc to my home directory. This makes sure changes stay in sync with a simple git pull and also lets me restore them with ease if I'm on a shared environment.

```
git clone http://github.com/chr1sbest/dotfiles
cd dotfiles
./symlink_dotfiles.sh
```

To restore the old dotfiles:
```
./restore_old_dotfiles.sh
```

Feel free to fork my [repository](http://github.com/chr1sbest/dotfiles) to customize your own configurations!

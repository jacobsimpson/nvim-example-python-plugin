# Example Python Plugin for Neovim

As part of the changes included in Neovim there is a new plugin model where
plugins are separate processes which Neovim communicates to using the
MessagePack protocol.

Since plugins are distinct from the Neovim process, it is possible to write
plugins in many languages.

This is a minimal example of a Python plugin. You should be able to (and feel
free to) copy this repository, rename a couple files, include the plugin in
your Vim config and see something happen.

## Making a New Plugin

The intention of this repository is to make it quick and easy to start a new
plugin. It is just enough to show how to make the basics work.

```Bash
git clone --depth 1 https://github.com/jacobsimpson/nvim-example-python-plugin ~/.vim/bundles
rm -Rf ~/.vim/bundles/nvim-example-python-plugin/.git
```

## Configuring Vim

I use NeoBundle so this is an example of how to load this plugin in NeoBundle.

```VimL
" Required:
call neobundle#begin(expand('~/.vim/bundle/'))

    " Let NeoBundle manage NeoBundle
    " Required:
    NeoBundleFetch 'Shougo/neobundle.vim'

    " You probably have a number of other plugins listed here.

    " Add this line to make your new plugin load, assuming you haven't renamed it.
    NeoBundle 'nvim-example-python-plugin'
call neobundle#end()
```

## Confirming the Plugin Loaded

There is some VimL in the plugin that will print when Neovim is starting up:

    Starting the example Python Plugin

That will confirm that the VimL portions of the plugin are loading correctly.

There is a function defined in the VimL portion of the plugin which echos some
text. You can execute the function like this:

```VimL
:exec DoItVimL()
```

The next thing to do is to initialize the manifest for the Python part of the
plugin. The manifest is a cache of the functionality implemented by the Python
part of the plugin. To initialize the manifest, execute:

```VimL
:UpdateRemotePlugins
```

Now that the manifest is initialized, it should be possible to invoke the
function defined in the Python part of the plugin. Look in \_\_init\_\_ to see
the implementation.

```VimL
:exec DoItPython()
```

## Changing the Interface

Neovim includes a process whereby the interface of the remote plugin are cached
for Neovim. 

```VimL
:UpdateRemotePlugins
```

Run this command for *every* change in the plugin interface. Without this, you
may see errors on from Neovim telling you methods are missing from your plugin.
Or the new functionality you are trying to add just won't work.

## Troubleshooting

### Python Client Log File

Define this environment variable to get output logged from your Python client.

```Bash
export NVIM_PYTHON_LOG_FILE=${HOME}/.nvim-python.log
```

The output files will have a number appended, and should be visible with this:

```Bash
ls ${HOME}/.nvim-python.log*
```

### Neovim Log File

```Bash
ls ~/.nvimlog
```

### Neovim Library

I found that the Python neovim module was not installed on my system. I didn't
see any great errors that lead me to that conclusion, so it is worth checking:

```Bash
python -c "import neovim"
```

Should execute without an error.


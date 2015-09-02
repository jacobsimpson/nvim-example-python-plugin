import neovim

@neovim.plugin
class Limit(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('DoItPython')
    def function_handler(self, args):
        self.vim.command('echo "hello"')


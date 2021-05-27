# Save Workspaces on Quit

Keep loosing your workspace state on <kbd>cmd</kbd> + <kbd>q</kbd>? This plugins closes each open workspaces before Sublime Text quits.

The plugin save workspace on <kbd>cmd</kbd> + <kbd>shift</kbd> + <kbd>w</kbd> (close window) too.

## Installing

### Using Package Control

Through Command Palette choose **Package Control: Add Repository**, paste `https://github.com/saneef/SaveWorkspacesOnQuit.git` in the text field and press <kbd>Enter</kbd>.

Then, you can search for **"SaveWorkspacesOnQuit"**, in Package Control to install.

### Using Git

Clone this git repository into your [Packages Directory](http://sublimetext.info/docs/en/basic_concepts.html):

```bash
$ git clone https://github.com/saneef/SaveWorkspacesOnQuit.git
```

## On Linux or Windows

If are on Linux or Windows add this line to your key bindings and customize the `keys`

```json
[
  { "keys": ["super+q"], "command": "save_workspaces_on_quit" },
  { "keys": ["super+shift+w"], "command": "save_workspaces_on_window_close" }
]
```

## License

This project is released under [The MIT License](http://www.opensource.org/licenses/mit-license.php).


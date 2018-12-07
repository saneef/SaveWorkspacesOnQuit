# Save Workspaces on Quit

Keep loosing your workspace state by <kbd>cmd</kbd> + <kbd>q</kbd>? This plugins closes each open workspaces and just before Sublime Text quits.

## Installing

Clone this git repository into your [Packages Directory](http://sublimetext.info/docs/en/basic_concepts.html):

```bash
$ git clone https://github.com/saneef/SaveWorkspacesOnQuit.git
```

## On Linux or Windows

If are on Linux or Windows add this line to your key bindings and customize the `keys`

```json
{ "keys": ["super+q"], "command": "save_workspaces_on_quit" }
```

## License

This project is released under [The MIT License](http://www.opensource.org/licenses/mit-license.php).


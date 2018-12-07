import sublime
import sublime_plugin

'''
	Save Workspace (Close Workspace) and Quit

	First save this file as:
	~/Library/Application Support/Sublime Text 3/Packages/User/save_workspace_and_quit.py

	To trigger the command with 'Command/Ctrl q',
	add the following to your Sublime Text > Preferences > Keybindings - User

	[
		{ "keys": ["super+q"], "command": "save_workspace_and_quit"}
	]
'''

class SaveWorkspacesOnQuitCommand(sublime_plugin.WindowCommand):
	def run(self):
		for w in sublime.windows():
			w.run_command("close_workspace")

		self.window.run_command("exit")

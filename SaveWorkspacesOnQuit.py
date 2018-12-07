import sublime
import sublime_plugin

'''
	Save Workspaces and Quit
'''

class SaveWorkspacesOnQuitCommand(sublime_plugin.WindowCommand):
	def run(self):
		for w in sublime.windows():
			w.run_command("close_workspace")

		self.window.run_command("exit")

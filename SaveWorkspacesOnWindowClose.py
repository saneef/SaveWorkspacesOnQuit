import sublime
import sublime_plugin

'''
	Close workspace (saves session) and close window
'''

class SaveWorkspacesOnWindowCloseCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("close_workspace")
		self.window.run_command("close_window")
		print('closing')

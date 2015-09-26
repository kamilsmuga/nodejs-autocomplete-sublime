import sublime
import sublime_plugin

class NodejsAutocompleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		view_sel = view.sel()
		if not view_sel:
			return

		pos = view_sel[0].begin()
		self.view.insert(edit, pos, ".doSth()")


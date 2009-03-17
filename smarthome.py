# -*- coding: utf-8 -*-
#
# Make HOME and END keys move to first/last characters on line first before
# going to the start/end of the line. (It's just a gksourceview2 property.)
#
# Copyright (C) 2009 David Lynch (kemayo@gmail.com)
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.

#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
#	GNU General Public License for more details.

#	You should have received a copy of the GNU General Public License
#	along with this program.	If not, see <http://www.gnu.org/licenses/>.

import gedit

from gtksourceview2 import SMART_HOME_END_BEFORE

class SmartHome(gedit.Plugin):
	def activate(self, window):
		for view in window.get_views():
			view.set_data("SmartHomePluginOriginalValue", view.get_property('smart-home-end'))
			view.set_property('smart-home-end', SMART_HOME_END_BEFORE)

		tab_added_id = window.connect("tab_added", lambda w, t: t.get_view().set_smart_home_end(True))
		window.set_data("SmartHomePluginHandlerId", tab_added_id)

	def deactivate(self, window):
		tab_added_id = window.get_data("SmartHomePluginHandlerId")
		window.disconnect(tab_added_id)
		window.set_data("SmartHomePluginHandlerId", None)

		for view in window.get_views():
			view.set_property('smart-home-end', view.get_data("SmartHomePluginOriginalValue"))


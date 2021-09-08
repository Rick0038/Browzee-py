#!/usr/bin/python3.8 											
# -*- coding: utf-8 -*- 									

from gi.repository import Gtk, WebKit2            			## ( To import required libery and webkit )

class Handler: 
  
  def backbutton_clicked(self, button): 
    browserholder.go_back()  			 		  			## ( clicks on the Back button, the '.go_back()'  is activated )

  def refreshbutton_clicked(self, button): 
    browserholder.reload()   			 		  			## ( '.reload()'  is activated when the 'Refresh' button is clicked. )
    
  def enterkey_clicked(self, button): 
    browserholder.load_uri(urlentry.get_text())   			## ( To '.load_uri()' input URL )
    
builder = Gtk.Builder() 						  			## ( builder specified )
builder.add_from_file("/ui/ui.glade")        	     			## ( imported the 'ui.glade' file. ) 
builder.connect_signals(Handler())       	      			## ( handeler pass through )
window = builder.get_object("window1") 			  			## ( to create a window )
browserholder = WebKit2.WebView() 				  			## ( to hold the webkit engine in app )

browserholder.set_editable(False) 				  			## ( to disallow editing the webpage. )
browserholder.load_uri("https://www.youtube.com/")      	## ( the default URL to be loaded )
urlentry = builder.get_object("entry1") 		  			## ( to take url entry from object as entry 1 )
urlentry.set_text("https://www.youtube.com") 		  		## ( to load default site in address bar )

scrolled_window = builder.get_object("scrolledwindow1")		## ( importe the scrolledwindow1 object from the ui.glade )
scrolled_window.add(browserholder)							## ( enebels scrolling function in window )
browserholder.show()										## ( to show the browser.holder and its content in window )
window.connect("delete-event", Gtk.main_quit)				## ( to kill running load when press end )
window.show_all()											## ( to show all running gtk window functions )
Gtk.main()													## ( gtk main conclude )

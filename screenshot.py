__author__ = 'Bernardo Augusto Godinho de Oliveira <@bernardogo>'

import gtk.gdk

w = gtk.gdk.get_default_root_window()
sz = w.get_size()

pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])

if (pb != None):
    pb.save("screenshot.png","png")
else:
    print "Unable to get the screenshot."

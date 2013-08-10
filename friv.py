#!/usr/bin/env python

__author__ = 'elf'

import pygtk
pygtk.require('2.0')
import gtk
import sys
import os.path
import glob


class friv:

    window = object()
    working_dir = "~"
    image_files = []
    current_image_index = 0
    image = gtk.Image()
    preloaded_image = gtk.Image()

    #fixme: change numbers to actual screen size
    screen_width, screen_height = 1920, 1080

    def next_image(self):
        pass

    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def toggle_fullscreen(self):
        pass

    def load_image(self, filename):
        self.image = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file(filename)

        width = pixbuf.get_width()
        height = pixbuf.get_height()
        aspect = float(width) / height

        if height > self.screen_height:
            height = 1080
            width = 1080 * aspect
        elif width > self.screen_width:
            width = 1920
            height = width / aspect

        pixbuf = pixbuf.scale_simple(int(width), int(height), gtk.gdk.INTERP_BILINEAR)
        self.image.set_from_pixbuf(pixbuf)
        return self.image

    def show_error(self):
        pass

    def mouse_scroll(self, widget, event):
        if event.type == 4:
            # scroll up
            pass
        elif event.type == 5:
            # scroll down
            pass

    def get_image_files_from_dir(self):
        self.image_files.extend(glob(self.working_dir+'\.jpg'))

    def __init__(self):

        # Setup main window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("delete_event", self.close_application)
        bg_color = gtk.gdk.color_parse('#000000')
        self.window.modify_bg(gtk.STATE_NORMAL, bg_color)
        self.window.fullscreen()

        # Setup main view
        hbox = gtk.HBox()
        hbox.show()
        self.window.add(hbox)

        # Quit by Escape
        accelgroup = gtk.AccelGroup()
        key, modifier = gtk.accelerator_parse('Escape')
        accelgroup.connect_group(key,
                                modifier,
                                gtk.ACCEL_VISIBLE,
                                gtk.main_quit)
        self.window.add_accel_group(accelgroup)

        #Mouse scroll
        self.window.add_events(gtk.gdk.SCROLL_MASK)
        self.window.connect("scroll-event", self.mouse_scroll)

        # Loading first file
        try:
            start_file_path = str(sys.argv[1])
            print(start_file_path)
            self.working_dir, filename = os.path.split(start_file_path)
            self.image = self.load_image(start_file_path)
            self.image.show()
            hbox.add(self.image)
        except IndexError:
            pass

        self.window.show()

    def main(self):
        gtk.main()
        return 0


if __name__ == "__main__":
    app = friv()
    app.main()






#!/usr/bin/env python

__author__ = 'elf'

import pygtk
pygtk.require('2.0')
import gtk
import sys
import os.path
import re


class friv:

    window = object()
    working_dir = "~"
    image_files = []
    image_index = 0
    image = gtk.Image()
    preloaded_image = gtk.Image()

    screen_width = gtk.gdk.screen_width()
    screen_height = gtk.gdk.screen_height()

    def next_image_pixbuf(self):
        pixbuf = self.load_pixbuf(self.working_dir + '/' + self.image_files[self.image_index])
        return pixbuf

    def image_files_in_dir(self, dir_path):
        image_file_list = [f for f in os.listdir(dir_path) if re.search(r'.*\.(jpg|png|gif)$', f)]
        return sorted(image_file_list, reverse=True)

    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def toggle_fullscreen(self):
        pass

    def load_pixbuf(self, filename):

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
        return pixbuf

    def show_error(self):
        pass

    def mouse_scroll(self, widget, event, image):

        if event.direction == gtk.gdk.SCROLL_UP:
            if self.image_index < len(self.image_files):
                self.image_index += 1
        elif event.direction == gtk.gdk.SCROLL_DOWN:
            if self.image_index > 0:
                self.image_index -= 1

        image.set_from_pixbuf(self.next_image_pixbuf())

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

        # Loading first file
        try:
            start_file_path = str(sys.argv[1])

            self.working_dir, filename = os.path.split(start_file_path)
            # print(self.working_dir)
            self.image_files.extend(self.image_files_in_dir(self.working_dir))
            # print(self.image_files)
            self.image_index = self.image_files.index(filename)
            # print(str(len(self.image_files)) + ' ' + str(self.current_image_index))
            self.image = gtk.Image()
            self.image.set_from_pixbuf(self.load_pixbuf(start_file_path))
            self.image.show()
            hbox.add(self.image)
        except IndexError:
            pass

        #Mouse scroll
        self.window.add_events(gtk.gdk.SCROLL_MASK)
        # self.image included for update image
        self.window.connect("scroll-event", self.mouse_scroll, self.image)

        self.window.show()

    def main(self):
        gtk.main()
        return 0


if __name__ == "__main__":
    app = friv()
    app.main()






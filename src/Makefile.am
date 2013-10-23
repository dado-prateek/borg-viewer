SUBDIRS = Viewer

bin_SCRIPTS = viewer
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = viewer.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g'

viewer: viewer.in Makefile
	$(do_substitution) < $(srcdir)/viewer.in > viewer
	chmod +x viewer
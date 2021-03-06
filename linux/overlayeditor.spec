Summary: X-Plane DSF overlay editor
Name: overlayeditor
Version: %{version}
Release: %{release}
License: CC-BY-NC-SA
Group: Multimedia/Graphics
URL: http://marginal.org.uk/x-planescenery
Vendor: Jonathan Harris <x-plane@marginal.org.uk>
Prefix: /usr/local
#Suse: python-wxGTK provides wxPython, python-numpy provides numpy, python-tk provides python-tkinter, python-pylzma
#Fedora: PyOpenGL provides python-opengl, tkinter provides tkinter, pyliblzma
Requires: bash, numpy, openjpeg, p7zip, python >= 2.7, python-imaging >= 1.1.6, python-opengl >= 3.0.1, python-setuptools, wxPython >= 2.8
#Sigh - Suse: python-gdal, Fedora: gdal-python
BuildArch: noarch

%description
This application edits DSF overlay scenery packages
for X-Plane 8.30 or later.

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/local/bin/overlayeditor
/usr/local/share/applications/overlayeditor.desktop
/usr/local/share/icons/hicolor/48x48/apps/overlayeditor.png
/usr/local/share/icons/hicolor/128x128/apps/overlayeditor.png
/usr/local/lib/overlayeditor
%doc /usr/local/lib/overlayeditor/OverlayEditor.html
%attr(755,root,root) /usr/local/lib/overlayeditor/linux/DSFTool


%post
gtk-update-icon-cache -f -q -t /usr/local/share/icons/hicolor &>/dev/null
exit 0	# ignore errors from updating icon cache

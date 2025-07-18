pkgname = "libportal"
pkgver = "0.9.1"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dbackend-gtk3=enabled",
    "-Dbackend-gtk4=enabled",
    "-Dbackend-qt6=enabled",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "qt6-qtbase-private-devel",  # qguiapplication_p.h
]
pkgdesc = "Flatpak portal library"
license = "LGPL-3.0-only"
url = "https://github.com/flatpak/libportal"
source = f"{url}/releases/download/{pkgver}/libportal-{pkgver}.tar.xz"
sha256 = "de801ee349ed3c255a9af3c01b1a401fab5b3fc1c35eb2fd7dfb35d4b8194d7f"


@subpackage("libportal-gtk3")
def _(self):
    self.subdesc = "Gtk+3 backend"

    return ["usr/lib/girepository-1.0/XdpGtk3*", "usr/lib/libportal-gtk3.so.*"]


@subpackage("libportal-gtk4")
def _(self):
    self.subdesc = "Gtk4 backend"

    return ["usr/lib/girepository-1.0/XdpGtk4*", "usr/lib/libportal-gtk4.so.*"]


@subpackage("libportal-qt6")
def _(self):
    self.subdesc = "Qt6 backend"

    return ["usr/lib/libportal-qt*.so.*"]


@subpackage("libportal-qt6-devel")
def _(self):
    self.depends = [self.with_pkgver("libportal-devel")]
    self.subdesc = "Qt6 development files"

    return [
        "usr/include/libportal-qt6",
        "usr/lib/libportal-qt*.so",
        "usr/lib/pkgconfig/libportal-qt6.pc",
    ]


@subpackage("libportal-devel")
def _(self):
    return self.default_devel()

pkgname = "breeze"
pkgver = "6.4.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "frameworkintegration-devel",
    "kcmutils-devel",
    "kcolorscheme-devel",
    "kcoreaddons-devel",
    "kdecoration-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = [
    self.with_pkgver("breeze-cursors"),
    "breeze-icons",
    "frameworkintegration",
]
pkgdesc = "Breeze visual style for the KDE Plasma Desktop"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/breeze"
source = f"$(KDE_SITE)/plasma/{pkgver}/breeze-{pkgver}.tar.xz"
sha256 = "4607ab451d0d15f0d0815243d07fd5f5709985f7eb2bef1bf4ca1691b470aab5"
hardening = ["vis"]
# TODO: split qt6 theme?


@subpackage("breeze-cursors")
def _(self):
    self.subdesc = "cursor themes"
    return [
        "usr/share/icons/breeze_cursors",
        "usr/share/icons/Breeze_Light",
    ]


@subpackage("breeze-devel")
def _(self):
    return self.default_devel()

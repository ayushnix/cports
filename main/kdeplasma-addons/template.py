pkgname = "kdeplasma-addons"
pkgver = "6.4.3"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# FIXME: failed tz comparison / scientific notation number e uppercase
make_check_args = ["-E", "(converterrunnertest|datetimerunnertest)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kglobalaccel-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kitemmodels-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "krunner-devel",
    "kservice-devel",
    "kunitconversion-devel",
    "kxmlgui-devel",
    "libplasma-devel",
    "plasma5support-devel",
    "purpose-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtquick3d-devel",
    "sonnet-devel",
]
depends = ["kirigami-addons", "kitemmodels", "purpose", "qt6-qtquick3d"]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Plasma addons"
license = "GPL-3.0-only AND CC0-1.0 AND LGPL-3.0-or-later"
url = "https://invent.kde.org/plasma/kdeplasma-addons"
source = f"$(KDE_SITE)/plasma/{pkgver}/kdeplasma-addons-{pkgver}.tar.xz"
sha256 = "7dad9176fee99f4e95f6573aab18326eeff6742609e8739b9b59c2e9f2aad19b"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]


@subpackage("kdeplasma-addons-devel")
def _(self):
    return self.default_devel()

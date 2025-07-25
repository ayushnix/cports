pkgname = "libpsl"
pkgver = "0.21.5"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["icu-devel", "libidn2-devel", "libunistring-devel"]
pkgdesc = "Public Suffix List library"
license = "MIT"
url = "https://rockdaboot.github.io/libpsl"
source = f"https://github.com/rockdaboot/libpsl/releases/download/{pkgver}/libpsl-{pkgver}.tar.gz"
sha256 = "1dcc9ceae8b128f3c0b3f654decd0e1e891afc6ff81098f227ef260449dae208"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpsl-devel")
def _(self):
    return self.default_devel()

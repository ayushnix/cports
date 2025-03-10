pkgname = "spice-protocol"
pkgver = "0.14.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Protocol definition for SPICE project"
license = "BSD-3-Clause"
url = "https://gitlab.freedesktop.org/spice/spice-protocol"
source = f"https://www.spice-space.org/download/releases/spice-protocol-{pkgver}.tar.xz"
sha256 = "04ffba610d9fd441cfc47dfaa135d70096e60b1046d2119d8db2f8ea0d17d912"


def post_install(self):
    self.install_license("COPYING")

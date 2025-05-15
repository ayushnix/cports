pkgname = "mcjoin"
pkgver = "2.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake"]
pkgdesc = "Multicast testing application"
license = "ISC"
url = "https://github.com/troglobit/mcjoin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "61ff39154194db69bf193ed6bde340f12b3163eef5cc22854970ed43292762be"
hardening = ["cfi", "vis"]


def install(self):
    self.install_bin("build/src/mcjoin")
    self.install_man("mcjoin.1")
    self.install_license("LICENSE")

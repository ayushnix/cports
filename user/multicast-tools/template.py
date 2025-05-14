pkgname = "multicast-tools"
pkgver = "3.2"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
pkgdesc = "Multicast msend and mrecieve tools"
license = "CC0-1.0"
url = "https://github.com/troglobit/mtools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "855bfed83318bad88fa1c0e25c52c808fa20dae25b9ae0f80bfd67f5fd4fd627"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]


def install(self):
    self.install_bin("mreceive")
    self.install_bin("msend")
    self.install_man("msend.8")
    self.install_man("mreceive.8")

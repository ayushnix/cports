pkgname = "mping"
pkgver = "2.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
checkdepends = ["iproute2", "util-linux-ns"]
pkgdesc = "Multicast ping program"
license = "MIT"
url = "https://github.com/troglobit/mping"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "36005f5520cfd078dd308e92ec18d191520afd9b6735148dfdc740dd440ec56f"
hardening = ["cfi", "vis"]


def install(self):
    self.install_bin("mping")
    self.install_man("mping.1")
    self.install_license("LICENSE")

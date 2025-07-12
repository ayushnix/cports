pkgname = "fastgron"
pkgver = "0.7.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "curl-devel", "ninja"]
pkgdesc = "JSON to greppable flattened JSON converter"
license = "MIT"
url = "https://github.com/adamritter/fastgron"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3011a3b99cd07d42648b2e964f459024b13ecc904d30501f0493fb0dc9fc33b2"


def post_install(self):
    self.install_license("LICENSE")

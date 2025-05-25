pkgname = "zuo"
pkgver = "1.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake"]
pkgdesc = "Racket variant for scripting"
license = " Apache-2.0 AND MIT"
url = "https://docs.racket-lang.org/zuo"
source = f"https://github.com/racket/zuo/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0c8a3a86365fb10961d9a1f536b1cd0d7fcdc2779af03236a340539966b33f86"
hardening = ["cfi", "vis"]


def post_install(self):
    self.install_license("LICENSE.txt")

pkgname = "mdnsd"
pkgver = "0.12"
pkgrel = 0
_commit = "5346604fcdeccd99f9943ac5ef887c3880480338"
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "pkgconf", "slibtool"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Multicast DNS Daemon"
license = "BSD-3-Clause"
url = "https://github.com/troglobit/mdnsd"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "fc12aff523fd8e1520fdec58150893930ab69af682222bf03ee7a8190a3d95ea"
hardening = ["!cfi", "!vis"]


def install(self):
    self.install_bin("build/src/.libs/mdnsd")
    self.install_bin("build/src/.libs/mquery")
    self.install_man("man/mquery.1")
    self.install_man("man/mdnsd.service.5")
    self.install_man("man/mdnsd.8")
    self.install_lib("build/libmdnsd/.libs/libmdnsd.a")
    self.install_lib("build/libmdnsd/.libs/libmdnsd.so.1.0.0")
    self.install_link("usr/lib/libmdnsd.so", "libmdnsd.so.1.0.0")
    self.install_link("usr/lib/libmdnsd.so.1", "libmdnsd.so.1.0.0")
    self.install_file("libmdnsd/1035.h", "usr/include/libmdnsd")
    self.install_file("libmdnsd/mdnsd.h", "usr/include/libmdnsd")
    self.install_file("libmdnsd/sdtxt.h", "usr/include/libmdnsd")
    self.install_file("libmdnsd/xht.h", "usr/include/libmdnsd")
    self.install_license("LICENSE")


@subpackage("mdnsd-devel")
def _(self):
    return self.default_devel()

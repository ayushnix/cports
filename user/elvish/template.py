pkgname = "elvish"
pkgver = "0.21.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
pkgdesc = "Scripting language and interactive shell"
license = "BSD-2-Clause"
url = "https://elv.sh"
source = f"https://github.com/elves/elvish/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3a4b93c3c99fe2f9847de35d64be24e2d4b9c12d429cd9831b4571993a66bb7a"
# fails
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_shell("/usr/bin/elvish")

pkgname = "diffoci"
pkgver = "0.1.6"
pkgrel = 0
build_style = "go"
make_dir = "."
make_build_args = ["./cmd/diffoci"]
hostmakedepends = ["go"]
pkgdesc = "Diff for Docker and OCI container images"
license = "Apache-2.0"
url = "https://github.com/reproducible-containers/diffoci"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "650554edbc7118e6fb7008865281e5dba6bc6d82a417a1e0e0ea05c1561ee402"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("diffoci")

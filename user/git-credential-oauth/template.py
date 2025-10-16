pkgname = "git-credential-oauth"
pkgver = "0.17.2"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Oauth credential manager for git"
license = "Apache-2.0"
url = "https://github.com/hickford/git-credential-oauth"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "23769afc87f82fe21b5519d059bb5ce56b2fad2c4abc7ecde9bff49a4e065ab6"

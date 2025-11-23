pkgname = "chibi-scheme"
pkgver = "0.11"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Scheme implementation for use as an extension language"
license = "BSD-3-Clause"
url = "https://github.com/ashinn/chibi-scheme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b4404d5304b51b243684702fa7b5f2d82f77cb7ef470bcfca1d94f8ed7660342"
hardening = ["!cfi", "!vis"]
# nothing
options = ["!check"]

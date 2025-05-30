pkgname = "perl-sub-uplevel"
pkgver = "0.2800"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
checkdepends = ["perl"]
depends = ["perl"]
pkgdesc = "Apparently run a function in a higher stack frame"
license = "Artistic-1.0-Perl"
url = "https://metacpan.org/pod/Sub::Uplevel"
source = f"$(CPAN_SITE)/Sub/Sub-Uplevel-{pkgver}.tar.gz"
sha256 = "b4f3f63b80f680a421332d8851ddbe5a8e72fcaa74d5d1d98f3c8cc4a3ece293"

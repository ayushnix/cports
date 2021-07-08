pkgname = "libxo"
version = "1.6.0"
revision = 0
bootstrap = True
build_style = "gnu_configure"
configure_args = ["--disable-gettext", "--disable-dependency-tracking"]
short_desc = "Library for generating text, XML, JSON, and HTML output"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/Juniper/libxo"
distfiles = [f"https://github.com/Juniper/{pkgname}/releases/download/{version}/{pkgname}-{version}.tar.gz"]
checksum = ["9f2f276d7a5f25ff6fbfc0f38773d854c9356e7f985501627d0c0ee336c19006"]

def post_extract(self):
    import shutil
    (self.abs_wrksrc / "libxo/sys").mkdir()
    shutil.copy(self.files_path / "queue.h", self.abs_wrksrc / "libxo/sys")

@subpackage("libxo-devel")
def _devel(self):
    self.depends = [f"{pkgname}={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    return [
        "usr/bin/libxo-config",
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/doc",
        "usr/share/man/man3"
    ]

@subpackage("libxo-progs")
def _devel(self):
    self.short_desc = short_desc + " - programs"

    return [
        "usr/bin",
    ]

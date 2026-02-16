pkgname = "continuwuity"
pkgver = "0.5.5"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "bindgen-runtime,blurhashing,brotli_compression,console,element_hacks,gzip_compression,io_uring,ldap,media_thumbnail,otlp_telemetry,release_max_log_level,sentry_telemetry,systemd,url_preview,zstd_compression",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["liburing-devel", "linux-headers", "rust-std", "zstd-devel"]
pkgdesc = "Matrix homeserver"
license = "Apache-2.0"
url = "https://continuwuity.org"
source = f"https://forgejo.ellis.link/continuwuation/continuwuity/archive/v{pkgver}.tar.gz"
sha256 = "3fd09ac9dd7bd695f8eb061f7cdd1b7a12478c6194d3d7e7805bb311074ea7df"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/conduwuit")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")

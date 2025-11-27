pkgname = "victoria-logs"
pkgver = "1.38.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/VictoriaMetrics/VictoriaMetrics/lib/buildinfo.Version=victoria-logs-v{pkgver}",
    "./app/victoria-logs",
    "./app/vlagent",
    "./app/vlogscli",
    "./app/vlogsgenerator",
]
make_check_args = [
    "-skip",
    "TestVlsingleIngestionProtocols|TestVlagentRemoteWriteReplication|"
    + "TestVlagentRemoteWrite|TestVlsingleKeyConcepts|"
    + "TestVlsingleStatsQueryPipesTimeFieldConstraints",
    "./...",
]
hostmakedepends = ["go"]
makedepends = ["zstd-devel"]
pkgdesc = "Database for logs"
license = "Apache-2.0"
url = "https://github.com/VictoriaMetrics/VictoriaLogs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a691ecc152ef2da16b076ad29c3fb3cf5be2ca2cf413e1c03040f26eb64b0a1d"


def post_prepare(self):
    self.rm("vendor/github.com/valyala/gozstd/libzstd_*", glob=True)
    self.cp(self.files_path / "libzstd.go", "vendor/github.com/valyala/gozstd")

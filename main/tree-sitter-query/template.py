pkgname = "tree-sitter-query"
pkgver = "0.6.1"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Tree-sitter query grammar for tree-sitter"
license = "Apache-2.0"
url = "https://github.com/tree-sitter-grammars/tree-sitter-query"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/nvim-treesitter/nvim-treesitter/archive/30de5e7e9486fb1b1b8c2a1e71052b13f94f1cb0.tar.gz",
    "https://github.com/nvim-treesitter/nvim-treesitter-textobjects/archive/5f9bf4b1ead7707e4e74e5319ee56bdc81fb73db.tar.gz",
]
source_paths = [
    ".",
    ".tests/nvim-treesitter",
    ".tests/nvim-treesitter-textobjects",
]
sha256 = [
    "18e158092789e4391668760e9ad1b5b4135c8f483d29163912d29e5619518d40",
    "f18e3705a55bc36ca43c8a8f64dcecf1fa04c9995046e2ed25639ee8c5e8f3c9",
    "73dcba69ae5a005451a95f2155ceaefc3e32c7bcda3f41b35d69f97f234a3198",
]


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/query.so", "../libtree-sitter-query.so.15"
    )


@subpackage("tree-sitter-query-devel")
def _(self):
    return self.default_devel()

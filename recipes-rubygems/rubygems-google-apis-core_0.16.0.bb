# SPDX-License-Identifier: MIT
SUMMARY = "RubyGem: google-apis-core"
DESCRIPTION = "Common utility and base classes for legacy Google REST clients"
HOMEPAGE = "https://github.com/google/google-api-ruby-client"

LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE.md;md5=7e6820981d59cdfac1e6538d3aacfd11"

EXTRA_DEPENDS:append = " "
EXTRA_RDEPENDS:append = " "

DEPENDS:class-native += "\
    rubygems-addressable-native \
    rubygems-googleauth-native \
    rubygems-httpclient-native \
    rubygems-mini-mime-native \
    rubygems-mutex-m-native \
    rubygems-representable-native \
    rubygems-retriable-native \
"

GEM_INSTALL_FLAGS:append = " "

SRC_URI[md5sum] = "9eaea7bf305fc0588b16a024cafddd0a"
SRC_URI[sha256sum] = "046a2c30a5ec123b2a6bc5e64348be781ce5fcd18dd4e85982e7a6a8da9d0dcc"

GEM_NAME = "google-apis-core"

inherit rubygems
inherit rubygentest
inherit pkgconfig

RDEPENDS:${PN}:class-target += "\
    rubygems-addressable \
    rubygems-googleauth \
    rubygems-httpclient \
    rubygems-mini-mime \
    rubygems-mutex-m \
    rubygems-representable \
    rubygems-retriable \
"

BBCLASSEXTEND = "native"

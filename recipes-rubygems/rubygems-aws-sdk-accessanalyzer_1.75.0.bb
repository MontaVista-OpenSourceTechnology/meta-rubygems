# SPDX-License-Identifier: MIT
SUMMARY = "RubyGem: aws-sdk-accessanalyzer"
DESCRIPTION = "Official AWS Ruby gem for Access Analyzer"
HOMEPAGE = "https://github.com/aws/aws-sdk-ruby"

LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=3b83ef96387f14655fc854ddc3c6bd57"

EXTRA_DEPENDS:append = " "
EXTRA_RDEPENDS:append = " "

DEPENDS:class-native += "\
    rubygems-aws-sdk-core-native \
    rubygems-aws-sigv4-native \
"

GEM_INSTALL_FLAGS:append = " "

SRC_URI[md5sum] = "b99d2aa7833697d68f6dab8cb5dbabf7"
SRC_URI[sha256sum] = "9ba08ae5b9a9aa14dd6ed2699cdcd6f8a64d0c4f83507c13790b43c046c11b63"

GEM_NAME = "aws-sdk-accessanalyzer"

inherit rubygems
inherit rubygentest
inherit pkgconfig

RDEPENDS:${PN}:class-target += "\
    rubygems-aws-sdk-core \
    rubygems-aws-sigv4 \
"

BBCLASSEXTEND = "native"

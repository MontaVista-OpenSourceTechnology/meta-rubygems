# SPDX-License-Identifier: MIT
SUMMARY = "RubyGem: aws-sdk-elasticloadbalancingv2"
DESCRIPTION = "Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2)"
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

SRC_URI[md5sum] = "ca1128c25756a40f6d32584d252f09b5"
SRC_URI[sha256sum] = "206aa247a12732e6c7af0df9f8082491798e921b3b81c7b98d240cfa70857a1c"

GEM_NAME = "aws-sdk-elasticloadbalancingv2"

inherit rubygems
inherit rubygentest
inherit pkgconfig

RDEPENDS:${PN}:class-target += "\
    rubygems-aws-sdk-core \
    rubygems-aws-sigv4 \
"

BBCLASSEXTEND = "native"
import os

from oelint_adv.cls_rule import Rule
from oelint_parser.cls_item import Variable
from oelint_parser.helper_files import get_layer_root


class RubygemsLicense(Rule):

    POKY_KNOWN_VALID_EXPRESSIONS = [
        "AAL",
        "AFL-1",
        "AFL-1.2",
        "AFL-2",
        "AFL-2.0",
        "AFL-2.1",
        "AFL-3.0",
        "AFLv1",
        "AFLv2",
        "AGPL-3",
        "AGPL-3.0",
        "AGPLv3",
        "AGPLv3.0",
        "ANTLR-PD",
        "APL-1.0",
        "APSL-1.0",
        "APSL-1.1",
        "APSL-1.2",
        "APSL-2.0",
        "Adobe",
        "Apache-1.0",
        "Apache-1.1",
        "Apache-2",
        "Apache-2.0",
        "Apache-2.0-with-LLVM-exception",
        "Apachev2",
        "Artistic-1",
        "Artistic-1.0",
        "Artistic-2.0",
        "Artisticv1",
        "BSD",
        "BSD-0-Clause",
        "BSD-1-Clause",
        "BSD-2-Clause",
        "BSD-2-Clause-Patent",
        "BSD-3-Clause",
        "BSD-4-Clause",
        "BSL-1.0",
        "BitstreamVera",
        "CATOSL-1.1",
        "CC-BY-1.0",
        "CC-BY-2.0",
        "CC-BY-2.5",
        "CC-BY-3.0",
        "CC-BY-NC-1.0",
        "CC-BY-NC-2.0",
        "CC-BY-NC-2.5",
        "CC-BY-NC-3.0",
        "CC-BY-NC-ND-1.0",
        "CC-BY-NC-ND-2.0",
        "CC-BY-NC-ND-2.5",
        "CC-BY-NC-ND-3.0",
        "CC-BY-NC-SA-1.0",
        "CC-BY-NC-SA-2.0",
        "CC-BY-NC-SA-2.5",
        "CC-BY-NC-SA-3.0",
        "CC-BY-ND-1.0",
        "CC-BY-ND-2.0",
        "CC-BY-ND-2.5",
        "CC-BY-ND-3.0",
        "CC-BY-SA-1.0",
        "CC-BY-SA-2.0",
        "CC-BY-SA-2.5",
        "CC-BY-SA-3.0",
        "CC-BY-SA-4.0",
        "CC0-1.0",
        "CDDL-1",
        "CDDL-1.0",
        "CDDLv1",
        "CECILL-1.0",
        "CECILL-2.0",
        "CECILL-B",
        "CECILL-C",
        "CPAL-1.0",
        "CPL-1.0",
        "CUA-OPL-1.0",
        "ClArtistic",
        "DSSSL",
        "ECL-1.0",
        "ECL-2.0",
        "EDL-1.0",
        "EFL-1.0",
        "EFL-2.0",
        "EPL-1.0",
        "EPL-2.0",
        "EPLv1.0",
        "EUDatagrid",
        "EUPL-1.0",
        "EUPL-1.1",
        "Entessa",
        "ErlPL-1.1",
        "FSF-Unlimited",
        "Fair",
        "Frameworx-1.0",
        "FreeType",
        "GFDL-1.1",
        "GFDL-1.2",
        "GFDL-1.3",
        "GPL-1",
        "GPL-1.0",
        "GPL-2",
        "GPL-2-with-bison-exception",
        "GPL-2.0",
        "GPL-2.0-with-GCC-exception",
        "GPL-2.0-with-OpenSSL-exception",
        "GPL-2.0-with-autoconf-exception",
        "GPL-2.0-with-classpath-exception",
        "GPL-2.0-with-font-exception",
        "GPL-3",
        "GPL-3.0",
        "GPL-3.0-with-GCC-exception",
        "GPL-3.0-with-autoconf-exception",
        "GPLv1",
        "GPLv1.0",
        "GPLv2",
        "GPLv2.0",
        "GPLv3",
        "GPLv3.0",
        "HPND",
        "ICU",
        "IPA",
        "IPL-1.0",
        "ISC",
        "Intel",
        "LGPL-2.0",
        "LGPL-2.1",
        "LGPL-3.0",
        "LGPL2.1",
        "LGPLv2",
        "LGPLv2.0",
        "LGPLv2.1",
        "LGPLv3",
        "LPL-1.02",
        "LPPL-1.0",
        "LPPL-1.1",
        "LPPL-1.2",
        "LPPL-1.3c",
        "Libpng",
        "MIT",
        "MIT-X",
        "MIT-style",
        "MPL-1",
        "MPL-1.0",
        "MPL-1.1",
        "MPL-2.0",
        "MPLv1",
        "MPLv1.1",
        "MPLv2",
        "MS-PL",
        "MS-RL",
        "MirOS",
        "Motosoto",
        "Multics",
        "NASA-1.3",
        "NCSA",
        "NGPL",
        "NPOSL-3.0",
        "NTP",
        "Nauman",
        "Nokia",
        "OASIS",
        "OCLC-2.0",
        "ODbL-1.0",
        "OFL-1.1",
        "OGTSL",
        "OLDAP-2.8",
        "OSL-1.0",
        "OSL-2.0",
        "OSL-3.0",
        "OpenSSL",
        "PD",
        "PHP-3.0",
        "PSF",
        "PSF-2.0",
        "PSFv2",
        "ParaTypeFFL-1.3",
        "PostgreSQL",
        "Proprietary",
        "Python-2",
        "Python-2.0",
        "QPL-1.0",
        "RHeCos-1",
        "RHeCos-1.1",
        "RPL-1.5",
        "RPSL-1.0",
        "RSCPL",
        "Ruby",
        "SAX-PD",
        "SGI-1",
        "SGIv1",
        "SMAIL_GPL",
        "SPL-1.0",
        "Simple-2.0",
        "Sleepycat",
        "SugarCRM-1",
        "SugarCRM-1.1.3",
        "UCB",
        "Unlicense",
        "VSL-1.0",
        "W3C",
        "WXwindows",
        "Watcom-1.0",
        "XFree86-1.0",
        "XFree86-1.1",
        "XSL",
        "Xnet",
        "YPL-1.1",
        "ZPL-1.1",
        "ZPL-2.0",
        "ZPL-2.1",
        "Zimbra-1.3",
        "Zlib",
        "bzip2-1.0.4",
        "bzip2-1.0.6",
        "eCos-2.0",
        "gSOAP-1",
        "gSOAP-1.3b",
        "openssl",
        "pkgconf",
        "tcl",
        "unfs3",
        "vim",
    ]

    LAYER_LICENSE_DIR = "files/licenses"

    def __init__(self):
        super().__init__(id="rubygems.license",
                         severity="error",
                         message="License '{}' isn't a valid SPDX entry")

    def __get_combined_licenses(self, _file):
        res = set(RubygemsLicense.POKY_KNOWN_VALID_EXPRESSIONS)
        __layer_root = get_layer_root(_file)
        for _, _, files in os.walk(os.path.join(__layer_root, RubygemsLicense.LAYER_LICENSE_DIR)):
            for f in files:
                _name = os.path.basename(f)
                if not _name.startswith("."):
                    res.add(_name)
        return res

    def check(self, _file, stash):
        res = []
        if "recipes-rubygems/" not in _file:
            return []
        items = stash.GetItemsFor(
            filename=_file, classifier=Variable.CLASSIFIER,
            attribute=Variable.ATTR_VAR, attributeValue="LICENSE")
        _licenses = self.__get_combined_licenses(_file)
        for item in items:
            _values = [x for x in item.VarValueStripped.replace(
                "|", " ").replace("&", " ").split(" ") if x]
            for val in _values:
                if val not in _licenses:
                    res += self.finding(item.Origin,
                                        item.InFileLine, override_msg=self.Msg.format(val))
        return res

# meta-rubygems

A layer providing gems for Ruby.

** IMPORTANT NOTE** 

> the integration with poky master is broken at the moment, due to missing support of openssl 3.x by ruby.
> See [this issue](https://github.com/priv-kweihmann/meta-rubygems/issues/255) for further details.
> In case you're working still with openssl 1.x the layer continues to work fine.
> In the meantime unfortunately there won't be any package updates.
> 
> Keeping the fingers crossed that this will be resolved soon

## Tested variants

The following variants are tested regularly:

| variant    | glibc                                                                                                                                           | musl                                                                                                                                          |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| qemux86-64 | ![[master]-[glibc]-[qemux86-64]](https://github.com/priv-kweihmann/meta-rubygems/workflows/%5Bmaster%5D-%5Bglibc%5D-%5Bqemux86-64%5D/badge.svg) | ![[master]-[musl]-[qemux86-64]](https://github.com/priv-kweihmann/meta-rubygems/workflows/%5Bmaster%5D-%5Bmusl%5D-%5Bqemux86-64%5D/badge.svg) |

Other variants most likely will work.
Feel free to contribute any needed patches.

### Tested revisions

Up to the following revisions automated checks being performed

* poky: 12ca5f7209126ea6e07b3ba93fbdb31065971454
* meta-openembedded: f2152d79043601eacb70da1a3ab36f5ac56f3e28

## Support

This layer is a rolling release.
Integration is continuously checked against the HEAD of the corresponding poky layer.
Don't expect tags or any kind of versioning.

### poky release mapping

please check the following table to pick the correct branch matching your poky version

| poky release | suggested meta-rubygems branch | ruby version |
| ------------ | ------------------------------ | ------------ |
| master       | master                         | 3.1.x        |
| honister     | hardknott                      | 3.0.x        |
| hardknott    | hardknott                      | 3.0.x        |
| gatesgarth   | dunfell                        | 2.7.x        |
| dunfell      | dunfell                        | 2.7.x        |
| zeus         | zeus                           | 2.5.x        |

## License

This layer is licensed under `MIT & BSD-2-Clause`.
Newly-added recipes are licensed exclusively under `MIT`.

## Add a new gem

Please see [the development README](scripts/README.md) for details.
Also please mind the [contribution guidelines](CONTRIBUTING.md)

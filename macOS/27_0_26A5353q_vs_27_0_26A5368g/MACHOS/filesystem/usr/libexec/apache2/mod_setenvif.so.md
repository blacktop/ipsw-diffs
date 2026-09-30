## mod_setenvif.so

> `/usr/libexec/apache2/mod_setenvif.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x175c sha256:7d90bd37b8a5f976624e3d7a87f658f1f371cda6e2da186e791d0e731c30e9ac
+888.0.0.0.0
+  __TEXT.__text: 0x1780 sha256:cd0ed32da956629d9d127fbb1be51908ce082bcaf3a41ac94764616e21ac3bd5
   __TEXT.__auth_stubs: 0x1c0 sha256:ef2d3b163aa689bee78f589b96dfb11cc1d705dbb44d3e242fd26f6fb44ba78b
-  __TEXT.__cstring: 0x3a5 sha256:68f56cba3fa8de8dde7ba9b749ed58294f2b70919b0e28f668b3d9bb9c887050
-  __TEXT.__unwind_info: 0x60 sha256:fbb0a74d2b2e363ff2af124c44d3ec1edf6be41474b27ee2726bdc45ee991540
-  __DATA_CONST.__const: 0xf0 sha256:06ce71e80f5542965c3fec5359212738f6dcc7a6e7fcce6f4e93ef8c93007164
+  __TEXT.__cstring: 0x3a5 sha256:e492fa2b8f9368921389803fbd62cf826b050f7acb7abb43f81a67a4035f8087
+  __TEXT.__unwind_info: 0x60 sha256:cd9aa506fc6876bd1aaa1866abc5e2efcd14bea53d5d6b9872f9fb1432f499f7
+  __DATA_CONST.__const: 0xf0 sha256:1edf46b3a81f434378ae577e78e18b9d15632051529b8a464e27a27114919aa3
   __DATA_CONST.__auth_got: 0xe0 sha256:7658954af2f3ac03e811a24d3571b50513f8add3abfd8223f562936069c0420e
   __DATA_CONST.__got: 0x8 sha256:3b6697522359e0a9681def183a85317eb80696e2d503838de7e927a9b8fdcf1d
-  __DATA.__data: 0x70 sha256:e4b0b5aea4ec740dd93def550f1a64e5cda5f933afbdd0bee8ec00591b59ecd2
+  __DATA.__data: 0x70 sha256:5e05fb7ab651c7a1786287b414e12ea1c6f5f8292f4001b9a560108c7f38a78e
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: D2C8FE13-4B3C-398F-98AA-33DC72E0AD64
+  UUID: 4B6F84B9-C7A6-32AB-9034-44EC4E3CD3BD
   Functions: 13
   Symbols:   45
   CStrings:  32
Functions:
~ _merge_setenvif_config : sha256 61089b46d6927b908be506ecc942960a9020f3e52f0635d2b38c8eb9b3c7ad6b -> cec406572caaa54137be8d1aacb11c853cb53836dde5f48a9b2482964a360391
~ _register_hooks : sha256 3ae9e65bea0b45ac380ac9e1116f6e9756b52dff0a19e776bff7757a99edad56 -> fc6c255df5b5f9baa5518f6256279c067f078b86455bd6b6a1c165bbeb39a613
~ _create_setenvif_config : sha256 f846a0756cc659c2df37be8d434ff7da1ab9d479fcfba4d24eef3b6222665732 -> aa763c530dbc24ce55376250c07a6d67a4f6f9767b08f9c8a97e228f4b90709f
~ _add_setenvif : sha256 6e470c859d86ab01e50610028b33073020acf6332ed3f35410a10d96cab93305 -> 1e72f754ad4bdf86f1a18b9b95ffbd8b1802d6abda2c29b1ad2de7d91a62a89a
~ _add_setenvifexpr : 484 -> 540
~ _add_browser : sha256 5e35451040189ac4c8d2dd69200071140ef152b56ff27ee11518d13da837baf6 -> cc297fc271254e03edc070a91e13979e11383b71729c5be88c3652cf7d7fdf7a
~ _add_setenvif_core : 1384 -> 1368
~ _non_regex_pattern : sha256 cb2e333198fee1cc82ea821ef24304963a233c99e0409c9e46b27c4e454622d9 -> c4ce9c719d9009b670fc8748dfc9d62c6cefc226a86bd447a2eb23f2761879c0
~ _is_header_regex : sha256 bc155cfd3adecac09feb2990289c4505fa713deb4c3e2e0969e00596faf2eccd -> 4aa37209c61b2af031d88c80c5ed2e1c14ab0e449af166108703a8f219e1fe6b
~ _add_envvars : sha256 b30d0963f117a80fa74f90369c52b904d1ad475855594332bf906f0da30e7d36 -> 5484e9d957302902980783b27661f72dc91a1a1897f1e6fe0a4b2f4689bfb396
~ _match_headers : 2504 -> 2500
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/metadata/mod_setenvif.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/metadata/mod_setenvif.c"

```

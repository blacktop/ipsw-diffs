## mod_socache_dbm.so

> `/usr/libexec/apache2/mod_socache_dbm.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x1c6c sha256:bae35dbeb02b85175e038517e7a0dacd2d71869c1e9821348e54626a750b40b1
+888.0.0.0.0
+  __TEXT.__text: 0x1c64 sha256:852b7a8468255e237b6ba74546b16c875432a958fde7d5802c8390b944e56157
   __TEXT.__auth_stubs: 0x1e0 sha256:038844fa0b78e504c752b46bafd0e6f5f2ccfd8e3c14520c696cb084b2baf4fa
-  __TEXT.__cstring: 0x563 sha256:c60687669e0346bc0171c429a1da8762f02310a3b35043aa119b58d97a661499
-  __TEXT.__unwind_info: 0x58 sha256:ca79197236270c83c616836684c7f0f0cf9166b14bcb2b8b4d2aae88d63b91d6
-  __DATA_CONST.__const: 0x50 sha256:c37d0193c03191f27ac4362948e0617805067dd3cd556ab8b2525db50a53e9e2
+  __TEXT.__cstring: 0x563 sha256:34ad6d085e3702b8cd1c018dfd2f7dc1a22b156d7bacb7f71492ca0cdabaf6f7
+  __TEXT.__unwind_info: 0x58 sha256:0bdbad667d5c4d613a98c15ae39a648d715b6a6e407bcf000d9a98e445ba196b
+  __DATA_CONST.__const: 0x50 sha256:856523cf1d602f857d06df46b2f589a65f32112c6e4511e3e3645d0bd96d7e72
   __DATA_CONST.__auth_got: 0xf0 sha256:be5be13008debb60ae1178c78928d722a573b0c5236acf9fb83ca0b51c97f195
   __DATA_CONST.__got: 0x8 sha256:8b4e04fe163f64dc20ca79541034b9e391385c2b346210828bbc6f794e8a30b7
-  __DATA.__data: 0x70 sha256:ddaba9f086aebe569d9f1f313b139265da9c5fac4c883ff3b0867407fda86f4a
+  __DATA.__data: 0x70 sha256:43f0348b5824f4087f79d123b7f0b9afd080854ebae5725088a3452d58a24f47
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: C95E1A57-08DB-375B-9781-BD28B0F5A7EF
+  UUID: 02DB3169-E141-314D-B34A-5EDFAA8BF288
   Functions: 12
   Symbols:   45
   CStrings:  33
Functions:
~ _register_hooks : sha256 d956bff1d9e4fd375897f1d105c08589050c177744b1513f1806be8aa2fc8629 -> 9a8f49ad78b883e7e4368cc2fb6397e01cef5f78180fc4a806392ad6719346cd
~ _socache_dbm_create : sha256 0e3c0d4c0285fedd4c894ed3d4db3cec315454cc7fa229b5b0ff460c5973bc59 -> 5c839c9fdafcc807967e44e620d123be09b5d2a0bc0f48a4924e1e313cce6141
~ _socache_dbm_init : sha256 191af6f7720d29c2af3f9313c61df32ea32c55bc8f1c96509744877245987ab3 -> 92d29ae51b68884879bfa483ffcee2460862f8c0ac1a440df3014991d7ffba77
~ _socache_dbm_destroy : sha256 8539d8cb1be42ce740d008c14b69121f4ec75f92d475fde2282544ae0ce1b4ed -> 421b39ba652841de100a7d58a9653e1fa227ea26302180b2c281778fc0fc8fef
~ _socache_dbm_store : sha256 20c1384d8295d3f233c70143b5087cb6853cedd9227da2ff318b1943a0115cec -> 03aa87ba86721ad120b440934283475d0b49f4c2aa6c76d2e2474637e1927765
~ _socache_dbm_retrieve : sha256 cb167a88b3bb44abe11b1de13e3e9b4971e5ac874dfeac6c719e0ab866c0f95e -> 2dc7c65d35931d3ddc7d0c9bb5d8c3d8f72b4a2d1a25d8c34d12bb559bd71746
~ _socache_dbm_remove : sha256 a78e65313f3fcdcee97a812a381c03382784050739d4e909456fd4dd5db3eec0 -> c4d6940293b6a72d49547e88471c5d997af0eba46365541523f26c5571a5d90d
~ _socache_dbm_status : sha256 654ddfd0ccc93a3cd4005f2a1955b0a636543369b2d5da01ee347940c6a439c6 -> d20f2bb7155062e7893b08c93c16e9181dc61a8547f8bbfd4630f631cdb0019a
~ _socache_dbm_iterate : sha256 7df18c794b622aab9d4fe50054d2de7fc446509c2471edb27a120affbe9ba638 -> 7bbf017614147c5e037b513463128d6bdbdc147d084bd034efafbdfd1d6841b6
~ _try_chown : sha256 17122b8fa4374225b1acf3aac54ebcaddf7c9711dfcacb0c6342d81f61c96753 -> f64410e6212e64c9a2c4b866670e5582c728c2c655481249113620136eb132b8
~ _socache_dbm_expire : 1420 -> 1412
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/cache/mod_socache_dbm.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/cache/mod_socache_dbm.c"

```

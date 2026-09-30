## mtmergeprops

> `/usr/libexec/mtmergeprops`

```diff

-9150.2.0.0.0
-  __TEXT.__text: 0xb84 sha256:8f3d11103ee514bfdf3b085894047fba986b28772c651e9d87d7f92611aa65cd
-  __TEXT.__auth_stubs: 0x3a0 sha256:e7117ca673b99daf907018323f1e1ccc69586af7f0b74366c3a39b89cda94dc7
-  __TEXT.__objc_stubs: 0x1c0 sha256:64cdb71405afed24848f9ae97dd03ec8c5503e27192ed4b3325d2db4cb48bd96
-  __TEXT.__const: 0x50 sha256:6870988c693c1fac9c8e2f9c30695676898941e4008b17c2ab6f40490d123bdb
+9170.34.1.0.0
+  __TEXT.__text: 0xb5c sha256:4e2c005bebb9cee5a7b33291f124587fe2a905a465fc706df00f3172803dc697
+  __TEXT.__auth_stubs: 0x3a0 sha256:97036ca253470e37dc87889679434529efec2ce6b67e7f38a90857a0474337e6
+  __TEXT.__objc_stubs: 0x1c0 sha256:019576259e7b9a0438c0faf8350ded459e9b415a645e25d5e18fd22ab6794bbc
+  __TEXT.__const: 0x50 sha256:1ee42775bce43df91c9b2ada53a32ff9db35975225afdacc660112f9953131d7
   __TEXT.__cstring: 0x221 sha256:147a87eb89ec7a3924ae861542f7178aa78a2172a6b859dcfb94cfe9f886b132
   __TEXT.__objc_methname: 0x13c sha256:ad915ac6d86af99a8d384cc89f36d2b2f7ca893fa73f9f3f4104d511279cdb03
-  __TEXT.__unwind_info: 0x90 sha256:9e3a2893aa1e0e50d332727a5dc3d5276407e1defd3d68d3869f4e610708d304
-  __DATA_CONST.__auth_got: 0x1d8 sha256:a91c5429a29a9f0efab018390e09e3fe878914b48a02dad1391cbd7b3181f984
-  __DATA_CONST.__got: 0x70 sha256:c5bc811c0b46dadf434d72acc46c32dffd64f41d2150abf4d7751881f293efed
-  __DATA_CONST.__const: 0x88 sha256:8b2ad8024346b79277c4f5a4b4e2e33b082ebfde3bab1ce619563e168b8f3c1b
-  __DATA_CONST.__cfstring: 0xe0 sha256:5de9e8c283f087f4e786df62a8861f22e9ebbf8d61363be5e361ca573b16abca
+  __TEXT.__unwind_info: 0x90 sha256:3a8ab05c519f36c73a904b88c6ff9403a26c7b6733413ec841c777d6cfc5fe3d
+  __DATA_CONST.__const: 0x88 sha256:801dd09d0a51f40fb864656cd066b2d818c119e91c3d57a9c4ea977c98be5dbb
+  __DATA_CONST.__cfstring: 0xe0 sha256:5a9dc11fe536ee5973717e3fd6e775c4f94a2179a362a5b88be84a61f3a9810e
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x70 sha256:ce9cf657ffd8fc0713485f1da7efe13a0c5dec1fc55a97e0433f8de78bbcb905
+  __DATA_CONST.__auth_got: 0x1d8 sha256:3e0dd9d3843dc4231bdaa386645129d04ff0e4e5a0fa3fd96db77547d4f60c93
+  __DATA_CONST.__got: 0x70 sha256:38b96cd6d8c53eff934c522db90394d58521234187e7fc7ef47e1bc867a51268
+  __DATA.__objc_selrefs: 0x70 sha256:ae8c7ca6e78cd4ef8ce4284922c378a038e6482d9bf0f524eede006a13ef1ede
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E2E9A91-4153-3491-A5C4-B2C61CD21C8C
+  UUID: D0D8EB61-68C9-378F-9FA5-150E82C8FF6B
   Functions: 10
   Symbols:   109
   CStrings:  40
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x25
Functions:
~ _MergePersonalityDictionaryFromPathWithName : 676 -> 652
~ _recursiveMerge : 276 -> 280
~ _GetMergePersonalityNameForDriver : sha256 2549669a56d9de8fd4ffee077aeb0e463eff628f006424c6cd223bcccceb1ebc -> d120fd81e22f653e5b21bb0a4106222556eee6210c2ee8839b9c330503da32fc
~ _CreateIteratorForDriverOfType : sha256 9f5b4fec26ae70a0e5e792cf356a907c18130c47ebb2dc2d636224b39481a1a5 -> fe15c3d0c0e9e8a097f016a239023904f14a7f03437271287d1eb6c84e904107
~ _DriverAppeared : sha256 a77e9baafc1ebda1f67f4cd55c1d1452d57da3371f0c3d2d7e6deede308b8287 -> 283cd312c52f801354459219c0a82047d08d4619c16277106de373b0845dd154
~ _MergePropertiesForDriver : 396 -> 400
~ _MergePropertiesWithIterator : 300 -> 284
~ _main : sha256 204e079605b9395663849e35e9d89265d05e0cefecf458a3e5f8eb17771c3a03 -> cea7a78831e84282f8cea83958f7939066938f67562ecdc64d452b6300b13f4f
~ ___main_block_invoke : sha256 8217031245712fe1330991d2f88f5e5a7055c4aee01abd3ba7f3e2f1a35d44d4 -> 03d68585866f491ba78e655e331f74f1ca2fb5fa5ce87ff765296ff237e9243e
~ ___recursiveMerge_block_invoke : 280 -> 272

```

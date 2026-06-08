## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

```diff

-250.2.0.0.0
-  __TEXT.__text: 0x65c sha256:388d6bdb8b451a28461a3550a6b55b2bdc6b03fec4ab7aecaf2256dfd18343b9
-  __TEXT.__auth_stubs: 0x240 sha256:dd3548be08af1ffb89365ea98d0a4bcd26ec42b7ccf92754b745d614d1f40ea2
-  __TEXT.__objc_stubs: 0xa0 sha256:d6a9e8daf0ca02c07fd4bf9417035d3ab3eae56e65bade8e159b413746717d51
-  __TEXT.__const: 0x58 sha256:9fa0112686595eac574f58a5277bfb473ae431703ca5c5fb713a2770380e9613
+262.0.0.0.0
+  __TEXT.__text: 0x620 sha256:48e0fc69725a3a9899a3c8d33998158e5858e8800e6cf30743570f5ec11488ab
+  __TEXT.__auth_stubs: 0x230 sha256:1c2443e2b3fa8ab856f551d9a9a89b95c90839f02eb30e32612aa05b1e6ed006
+  __TEXT.__objc_stubs: 0xa0 sha256:81b3523db397efbcbcfa1dd38dc729421221906c99dd6e3b579f4977a7cddcc4
+  __TEXT.__const: 0x58 sha256:97c4837ba95f628868585d5f5518ecc9b8d5fb311d64bb0b904e69f215f31a47
   __TEXT.__cstring: 0x8c sha256:65d069917ab41a179630143e13e85bd9f94ff27d65dc6c7c40e4b86bc10798b8
   __TEXT.__oslogstring: 0xfe sha256:43c25961192436caf144e7bd70f5406c4285e953205cb409f1623472a3c7100e
   __TEXT.__objc_methname: 0x5a sha256:ed16b671aa735114eaf2c0305c143a32db655504e196a3d6233ee333206d8c4f
-  __TEXT.__unwind_info: 0x70 sha256:d1b2b3fa6396b4dbd0dc63d3c58ba38dd8b6a302cd950dcbf718dd664cff4112
-  __DATA.__auth_got: 0x128 sha256:92b159f863c99d81135dedd2f73bbcc47ce3b354b3c12bf745f21160f657d794
-  __DATA.__got: 0x18 sha256:762637758cf91852c26d82a6256fd56a9fabd23f9d425ffce10c3ee214f3c625
-  __DATA.__const: 0x48 sha256:c1185d8cfc2914170483ca13a95ff87e182025322070b84915207865eec856ff
-  __DATA.__cfstring: 0x40 sha256:2ba1787fb46345f209a1a5beb5c749156e82446ba8bff026164bd0fe6a3574aa
+  __TEXT.__unwind_info: 0x78 sha256:9a6b8b8bdc757e259f68bdc2b6fdae780ca5f8a0f4546099d081c6f9d93ab9bc
+  __DATA.__const: 0x48 sha256:52cded82c49f096820b144e317ddd6d9ccf63ecb771b9e2984349d6bda332a97
+  __DATA.__cfstring: 0x40 sha256:332884dfca7c40c7c7e9aa291bd882a974cc6bd88c1005a1a502fe2dea2bf675
   __DATA.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x28 sha256:e305e5f6f2c763b5a234c87aa4860117c64f1900ea97f60327f9bb6a4182d770
+  __DATA.__objc_selrefs: 0x28 sha256:851c7b02f2014bd0e3bd4eddae41b6486e90c0e23e3bc821bf6dc0fb359fb411
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
+  __DATA.__auth_got: 0x120 sha256:af7e64730bc956f2b8609e1047f0f37b8cad4b5caf0dcb62349ad7584a86e65b
+  __DATA.__got: 0x18 sha256:2ef70e09a1d7a7054df1ae5305697d5819adc2fd4aae3001a5331ea02d9c4a8d
   __DATA.__bss: 0x410 sha256:256fb9c4796b15a7ec4b0d5319e9e493ca4cffda658310420bdfd31e1c59da79
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 72351F66-D5EE-3F1E-B286-19A2AAF152D0
+  UUID: 58F1B4D7-F658-3A1B-B230-A20EF3D42919
   Functions: 7
-  Symbols:   47
+  Symbols:   46
   CStrings:  22
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ _init_tailspin : 1188 -> 1160
~ sub_d0c -> sub_cf0 : 84 -> 68
~ sub_d60 -> sub_d34 : 112 -> 96
~ sub_dd0 -> sub_d94 : sha256 3f76a362a05d52ff2406934b1b7996f3350a7ce4d16c4e26de837e0300f9f40b -> d2b3803fa9380abc411a0f5b207eda3efabcdd930c6b0f12dfa59e88ab24168a
~ sub_e50 -> sub_e14 : sha256 79ac381598cc6f30529d36068fccf2ef899d738459222a9cdae5a1233e7436ef -> d79674740e6a4b40dbc3413187dab1d4b092959e0521dd0c8d9f0c43dc3475e2
~ sub_e94 -> sub_e58 : sha256 fbb6f0f12d69b39b522e4dce6d7a1562d98fb92f1d60ce0f908350d18f509e84 -> d7838571b5e2e2795d40671eaed78d60643c4ff26e6dc48e0e62de6592c3f324

```

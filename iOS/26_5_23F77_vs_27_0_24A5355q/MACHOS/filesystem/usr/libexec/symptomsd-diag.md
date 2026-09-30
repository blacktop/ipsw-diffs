## symptomsd-diag

> `/usr/libexec/symptomsd-diag`

```diff

-411.120.4.0.0
-  __TEXT.__text: 0x470 sha256:3757e9ea356c42600e8c2c8141bb4c6a26a61afa01c90eb90c45d8321abd532a
-  __TEXT.__auth_stubs: 0x1d0 sha256:e3e08f255d7b4e79a9f42eb98d2048d59d607e2c34854355e1f5511834de78b0
-  __TEXT.__objc_stubs: 0xa0 sha256:6092686f67783e54770fc0943b1a5fefbec6c78895171855a009d29fd7e4ec78
+460.0.0.0.0
+  __TEXT.__text: 0x4cc sha256:acf0f998eb81e6b53d0e9622047fb29cafe00935c1df5557115a0524dfc4641a
+  __TEXT.__auth_stubs: 0x1b0 sha256:73a7641abf16fd3ae55cd4938a4989b43d5414f802bb3f5701355888fbfbd50b
+  __TEXT.__objc_stubs: 0xc0 sha256:d70053a36e3229977e06671c7d34e59a351498130629974a1ba8e672d4a877da
   __TEXT.__const: 0x50 sha256:226a471172d90de7c6c8932b087c9fc90d4b666d730c473e04cb25c956336b4f
   __TEXT.__cstring: 0x26 sha256:c0685386f7d57d7335d125c170dbde18154b3d8e1a956f2b6950818f2e251e29
-  __TEXT.__oslogstring: 0x99 sha256:129a775dbf238cce035678cdbff96b622527cbe75585668041917b9046b1e85d
-  __TEXT.__objc_methname: 0x42 sha256:248e0f85451c2839ae3419e2d9421f42e5bee1798694ba9c60ff1ecc1fac0665
-  __TEXT.__unwind_info: 0x78 sha256:fba25dc3ed6a63df6b013cc64fd465749d8f871bb233ddd3b0002aada046b700
-  __DATA_CONST.__auth_got: 0xf0 sha256:be5be13008debb60ae1178c78928d722a573b0c5236acf9fb83ca0b51c97f195
-  __DATA_CONST.__got: 0x40 sha256:dfbb3ebb8c75985cc1924600a82707b562edf3a084bfa5c5bbfca3b922b417e3
-  __DATA_CONST.__const: 0xa0 sha256:99a9f5f19a345f4a5e8e47ee5075cf5086ce9fcbc1700f53a253b30fae9c53a8
+  __TEXT.__oslogstring: 0xcd sha256:68c9d80cd4a32cb7e7a4b9e1f9e71f35c62f45508ab1538cd4222d0b5e4dad80
+  __TEXT.__objc_methname: 0x59 sha256:5f17b661602c2b4682f48afcc1abba31872194b6508e2d9180b029b5bb6e6db6
+  __TEXT.__unwind_info: 0x70 sha256:8e6a3828866997e4e673763021553dbe9679b967f0fea3627711e5296c17c8e7
+  __DATA_CONST.__const: 0xa0 sha256:78d1e4a12c095f2249c9e00ae208b79b96630d6b6f37d67a72f7b9ed768d6e0e
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x28 sha256:52e5ac5f33ee9a1a45fba827c76b6cc22266927a3b60c4dd1f38d8be036b4bfe
+  __DATA_CONST.__auth_got: 0xe0 sha256:c465415308036f8a823b954a35adc4370fbe7d0c552e6cc369f691b932676dc6
+  __DATA_CONST.__got: 0x38 sha256:7d5cb4733693a926917398b5b278549a4812fdf73868a9bc46d35606ca253974
+  __DATA.__objc_selrefs: 0x30 sha256:ba34b68d6895c88b21011f840da4f60d78c51573a22c463d9f2ceaf62f9a6bb1
   __DATA.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F409F02C-4D3F-3558-AB32-A5D010491A2D
+  UUID: B972EBDE-4DB1-39D7-A5CE-5C61E3295274
   Functions: 9
-  Symbols:   41
-  CStrings:  12
+  Symbols:   38
+  CStrings:  14
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_100000998 : 84 -> 68
~ sub_1000009ec -> sub_1000009dc : sha256 4a55c9b0326db195001c720a992440d877c856f42dad3abecce36d5c61038498 -> a21cfe4b5e598c2b49c616dcd07c89c26df167f6174523e403b12bd989311339
~ sub_100000a30 -> sub_100000a20 : 336 -> 408
~ sub_100000b80 -> sub_100000bb8 : 316 -> 336
~ sub_100000cbc -> sub_100000d08 : sha256 460b4b8bac7a61708f0428a55b9398b021e513b7ec86728f73445407261d7723 -> 7291202f3b453f326d759f6bf295ea045f4b62c7bb2ccaceb7078965ea0d926b
~ sub_100000cc0 -> sub_100000d0c : 204 -> 224
~ sub_100000d90 -> sub_100000df0 : sha256 fa261dbf6b953a7a97cfe047f4277140f6821ae959bf5a3eca46982a9fcab177 -> 167a43a8c2a1eac66b2ca4503453764b83fa7a36419745398b169946c10c6014
~ sub_100000da4 -> sub_100000e04 : 100 -> 96
CStrings:
+ "Asked to run in unsupported environment. Bailing..."
+ "isSupportedEnvironment"

```

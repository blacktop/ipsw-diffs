## soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

-440.51.0.0.0
-  __TEXT.__text: 0x484 sha256:e44b152ba679877d30c8f8a45add21b16a1c12872157a5a2d15a867cc68158a9
-  __TEXT.__auth_stubs: 0xf0 sha256:5830acc842efe52796541d1f2219b1757884b8adad315360e894a3a8c52ef7f4
+500.151.0.0.0
+  __TEXT.__text: 0x484 sha256:1c93d73e56304ed12ce65e2e590220b9179123d5f6ce9e5488d3450483891b28
+  __TEXT.__auth_stubs: 0xf0 sha256:387479348e587b3861a6111dd8c502e861cfd4316fba56f1949aa03e6ea22559
   __TEXT.__const: 0x52 sha256:25c8df1449cdc6faf9b627c7d59b454ba4a4272f70bd0c4aba1c820f81d50d83
   __TEXT.__swift5_entry: 0x8 sha256:03f15b0e2e4129f31eccec6d60ae7912cf279df957eade52408b3f1957bdc1df
   __TEXT.__swift_as_entry: 0x8 sha256:aed2dfc4c4d295b8c758514d3bb3eff986af3ab40ac74ca5b2752598376b66f0
   __TEXT.__swift_as_ret: 0x8 sha256:87ef8032699c8469e9b12a2a89d3fa3d0a25ca9f495f9e530bf5be67e7d38d13
-  __TEXT.__unwind_info: 0x70 sha256:9aff4c3d2ceb8a58cb46629f6467a622dc51e5b00897115d5d959fbcf53d339d
-  __TEXT.__eh_frame: 0x40 sha256:fad3dd6873c7adb2e5859ef1f676be255360e07b4a92b06d35bab7b03c86aee6
+  __TEXT.__swift_as_cont: 0x8 sha256:2b0d51db706a04763641c698aaf69f1204bc731a302365c89abfaf0df58fed34
+  __TEXT.__unwind_info: 0x70 sha256:2b61de0e191c360426a7a25f1221e4387a3e0b8720b88718fa1b541c9a1e1e5e
+  __TEXT.__eh_frame: 0x40 sha256:87f7fdb3eca3890f51acffa311d38b6665927a07ed57cd65c201ba643e3a801d
+  __DATA_CONST.__const: 0x80 sha256:38723a2e5e8a17aa7950dc008209944e898f69a7bd10a23c839d341e935fd5ca
+  __DATA_CONST.__objc_imageinfo: 0x8 sha256:885ce8037a15de89b0ceb0054c31fc3de725513307f685be388961916dadcdb0
   __DATA_CONST.__auth_got: 0x78 sha256:38c345cb9cf8745099627a43c391a1581c0c6e90e4af5679a2e9737df975dec9
   __DATA_CONST.__got: 0x18 sha256:6e43aed7def9ddb6b69d883db445c2176a4db9c93c967889d35294d22f0c193c
-  __DATA_CONST.__const: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __DATA_CONST.__objc_imageinfo: 0x8 sha256:234cedc7009d98da03ca2a7ff525d0db26b82bff0e6046456f4eda918f734526
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 466F78FB-B229-3450-98EC-AF6574724A0A
+  UUID: 65A18F06-1BBE-3CE4-8071-85AAA99BF4D5
   Functions: 8
-  Symbols:   31
+  Symbols:   30
   CStrings:  0
 
Symbols:
+ _swift_release_x8
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _swift_release
Functions:
~ _main : sha256 e78cedb1fc37f3f8e7336209ed3a02d0de32dbe3db96f333b99ddd2a7cdfcb6e -> 5aa86121ca062d99513a538a482e5f4be791d82f26ee480b9ce747a7cd0fd3c7
~ sub_100000d1c -> sub_100000d24 : sha256 53d92071543c0dac26c8b4c1fa73517bae1949b36a39ec93940da0397389ba11 -> 2c62272b2d02b8c3d99eda7746988975ac5ebd9f95d364902e44b3a4da606054
~ sub_100000dc4 -> sub_100000dcc : sha256 5621e80b4a54ca95f1fac8c80122de241d670275e752a0daafdc87e284c8b9f9 -> 65db5064845949f4e3349b78df4aa386d5902067160c28389ebd5834f367a510
~ sub_100000f38 -> sub_100000f40 : sha256 cb739c0681443e893c60ffa371f6c1649868aabd75499a58a5b2312d8f2aea30 -> 0e70467f1fd30d7330a289f9c7873aba8c56221a7118f9b5bf1cac522a3973f0
~ sub_100000f70 -> sub_100000f78 : sha256 5342703aab46ca4c8e2940b14907e4993d23c2687be19107406be8a083880f83 -> d95c3a085ad9ef20a288dce60fc476c92a129e8445a99dcf83a3af94562ca348
~ sub_100000fc8 -> sub_100000fd0 : sha256 bce0106ccf9d5afdb749872be7773d5e52cbcfd7a3c9dc81ff1427ccaed2cd69 -> 07a13ac4c73a8af2d32df2ce55ee3801f91d67b7ab3272a53752f6026e6d66d8

```

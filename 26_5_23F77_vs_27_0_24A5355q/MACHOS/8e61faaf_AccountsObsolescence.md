## AccountsObsolescence

> `/System/Library/DataClassMigrators/AccountsObsolescence.migrator/AccountsObsolescence`

```diff

-1036.0.0.0.0
-  __TEXT.__text: 0x118 sha256:ac47a1ec9b24b7faf85566e749d632f8acfae0de7ed0f1e6ad2710a6445396ce
-  __TEXT.__auth_stubs: 0x90 sha256:5291925bd814eb34eec5248c708a83f9be3564462e93e034638627d57624d87b
-  __TEXT.__objc_stubs: 0x40 sha256:0e830c6fbe1429a488f415460b762e61790957030da21c38e68601a8a39886f0
+1116.0.0.0.0
+  __TEXT.__text: 0x118 sha256:5e26581c287193f9a7018d7d5e4fc008dc90c8e099a04223b1b216e2f69da124
+  __TEXT.__auth_stubs: 0x90 sha256:cc6d3999f9684b2c3dad88fc0a21939257ffdb0d92d4f659ff1991e302aee65d
+  __TEXT.__objc_stubs: 0x40 sha256:424b1a98822f880265904ac07ce612a487253118a126d0096419aef94b7f8018
   __TEXT.__objc_methlist: 0x44 sha256:f242a99745fb22f5ca78edea3ad43d4807c2c435dd7d334bcee1729b88408bd6
   __TEXT.__const: 0xc sha256:b0dbb615681305fc342278f60ae7188a9369a6beb49d394029353b01a9b5127e
   __TEXT.__cstring: 0x34 sha256:ab5d826a5206eaa9253063daba6371f8c76568a542c53515bdefbc5b341a30be
   __TEXT.__objc_classname: 0x1f sha256:9fa34fe8d7f73b7b223aaf57e55b79dca715f809774870d86115ae5041544847
   __TEXT.__objc_methname: 0x7c sha256:03ad0c75500e555ac393bc53565d489aafee59bc86be13afe743ac3486d51e1b
   __TEXT.__objc_methtype: 0x23 sha256:efe55838a6e619b3730f90db14152475f631382cf8b1e066e328ed4e62681182
-  __TEXT.__unwind_info: 0x60 sha256:b5722eae96679519b63016d596ea4448f4c98ef01ce9ff6fbbfb7c3fed2ab032
-  __DATA_CONST.__auth_got: 0x50 sha256:d0afeb17ae3c6f2bbf48f7670673900580b84d4fea07168e4558474a49f85f46
-  __DATA_CONST.__got: 0x10 sha256:5a0fb0f386214ad822fa5bd4b622dbcf2029e29dab34a6b1d05539647261a250
+  __TEXT.__unwind_info: 0x60 sha256:f75c4bf381c72603b0aa45232e62ee0670cd35481fee5c74ba5061f8c3311138
   __DATA_CONST.__const: 0x28 sha256:facffae34ade1b33dc1687b221cd432e8a6bc7363a12661ff6f289931cb8f01d
-  __DATA_CONST.__cfstring: 0x20 sha256:e03c5f617572f115541bf08f42efd49dcfa164c03293a08ab4ae5940b692722e
-  __DATA_CONST.__objc_classlist: 0x8 sha256:ee625d4ec8917ca87ccffd741ab0e149e132c4d36bee6199f697bb82cd44f59d
+  __DATA_CONST.__cfstring: 0x20 sha256:9ba3b0515962220b3bde3914b955d01a1a609d8585c9634eab209e33a1f7677d
+  __DATA_CONST.__objc_classlist: 0x8 sha256:8d933ba59ab63d8b37e396e95cb561d5d1b07fead8616203a66ec56e640bff8b
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
+  __DATA_CONST.__auth_got: 0x50 sha256:d801c89b2ebbaa06a0c4a409e06f2a9a7e2c99ca5a669533cb0b4efd44f06652
+  __DATA_CONST.__got: 0x10 sha256:1318a03dc30e2eaf73c23b66edf8fceb528b3e3350bf844fff9dbe5eadc1abd8
   __DATA.__objc_const: 0x90 sha256:6752a97078c4301a4f56b2285a79fdd26fe461757f9d6ae3f832231005d71a8b
   __DATA.__objc_selrefs: 0x30 sha256:0c5493290d0e3df8e826e800318aa3411f5a5b8768b3828a568e1ff8fabd5327
   __DATA.__objc_data: 0x50 sha256:9627c517541468b5477d227b821a36c98933a377d1c7bdc48b1aaa69cdedeb6a

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6BC4ABC-DCDE-37BA-8A8A-CE8D502380AF
+  UUID: 4000E602-87DA-3C42-9AF5-06146EC173DC
   Functions: 6
   Symbols:   20
   CStrings:  14
Symbols:
+ _objc_retain
+ _objc_retain_x2
- _objc_retain_x19
- _objc_retain_x20
Functions:
~ sub_a88 : sha256 f58dec151b6b8569dc46f1045f539ac112a6636374f479d6f1ceecc467ffb429 -> 39caab5badbc169e1e12c764b7c3e24a0aedf0d016843425d37fecba1ca8a538
~ sub_a94 : sha256 42d1263c4cfac36cfa8a559e3a1c43aec6b282ff4c7e2a70a9cb9f40ad7acb97 -> 6006bff4f83b29965ed3afc446808dd5a27eda1974a64a59036f4c66321eb26e
~ sub_ad8 : sha256 eac616dfc6abd7a9f83e73afab202a143b1992c4c8377a0ab4f170b71dabbe14 -> 9819188fcb52584a7db77b094fcf28b0daf0d6bc1024478f4a14b0956038299c

```

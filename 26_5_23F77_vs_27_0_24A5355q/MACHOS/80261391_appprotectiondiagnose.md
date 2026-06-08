## appprotectiondiagnose

> `/usr/bin/appprotectiondiagnose`

```diff

-46.4.3.0.0
-  __TEXT.__text: 0x160 sha256:c5efc1e3eb6ceeb5a51064fc3a5c91e38a378236630ecba22861e3d7b0f3400e
-  __TEXT.__auth_stubs: 0xd0 sha256:05ceaeca1689fb09b6f7835a0b73468a49c4c3c0b8fda65580e87ad4b4b38d7f
-  __TEXT.__objc_stubs: 0xa0 sha256:8916ddea9c5cb81139bb297130e5d091215a1aeebb5c1475d553d59323a17101
+54.0.0.0.0
+  __TEXT.__text: 0x158 sha256:55f51b69ce0f2697e293a7a3a5a2263c7ef374697071f95548032424d1753f1c
+  __TEXT.__auth_stubs: 0xc0 sha256:f3b5e6d194d823a716d2f6411284f997f74fbe218eb8a943c6ac7ff3f3bd7317
+  __TEXT.__objc_stubs: 0xa0 sha256:8cf7e14200b1df92cb1cee181ade3c3a806bf79b2a34958ee4c42e95b606c446
   __TEXT.__cstring: 0x2c sha256:4b7f3e7d4f568f63546b7ee1e214232beca82012d399339ab67625954c2bbf44
   __TEXT.__objc_methname: 0x64 sha256:b52e270cc1e7fa97bdd89532ebae51d82af63a9dd89936d552d270099d10da95
-  __TEXT.__unwind_info: 0x58 sha256:7411e1bd5853bd42f6afdfd9437d76e3ceca6ec074be286ca1a06d8884f8d2e7
-  __DATA_CONST.__auth_got: 0x70 sha256:801edba8c4504d4e3f4758d1823b8f8ea3bdb4f7c402aa8efb50c9bf465918f9
-  __DATA_CONST.__got: 0x18 sha256:06802842f7309d81ebe9ecec9ce28e6735efe336bf66e79cfc0008d6c0a8b484
+  __TEXT.__unwind_info: 0x58 sha256:d125df28b4b26421bb80a9dfe42c1d9ffe5ba45446801d3c8da7324b4911c87a
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x28 sha256:de8ea866c6d0e6ca9cf33ca75080ce745a86a16853dfaaf54db9d7515274d962
+  __DATA_CONST.__auth_got: 0x68 sha256:a42ed8a77a30481fc8fd0a630cfb1de6d66fcd27e534230be90ce4cdc76c60d5
+  __DATA_CONST.__got: 0x18 sha256:f26942fec4d99d75c1e4aa0297900bb87660fa77eb0afba06e5a978dba33e66b
+  __DATA.__objc_selrefs: 0x28 sha256:c6aada5aad112205c6832c2eb5e5a9cd9aaab177460f1d1f1e67ac5991e08223
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B780B740-C8D9-3E39-B40C-68FB024DF162
+  UUID: 1BC87F9D-6A36-3DC4-9171-CEA4A7EC07AF
   Functions: 1
-  Symbols:   19
+  Symbols:   18
   CStrings:  7
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
Functions:
~ sub_100000720 : 352 -> 344

```

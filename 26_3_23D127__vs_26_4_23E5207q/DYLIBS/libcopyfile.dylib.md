## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-230.0.1.0.1
-  __TEXT.__text: 0x761c
+240.0.0.0.0
+  __TEXT.__text: 0x7670
   __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x1a28
+  __TEXT.__cstring: 0x1a67
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 76E7C8D1-3829-3EC3-B583-7571927517ED
+  UUID: C28C9022-B8D2-3F9C-99E1-F991F494894F
   Functions: 37
   Symbols:   188
   CStrings:  192
Symbols:
+ ___block_descriptor_tmp.37
+ ___block_literal_global.39
- ___block_descriptor_tmp.22
- ___block_literal_global.24
Functions:
~ _copyfile : 3944 -> 3940
~ _copyfile_internal : 7612 -> 7652
~ _copyfile_open : 3784 -> 3772
~ _reset_security : 556 -> 568
~ _fcopyfile : 620 -> 660
~ _copyfile_pack : 4500 -> 4508
CStrings:
+ "/Library/Caches/com.apple.xbs/541C9472-BFB3-48CC-B4E9-3EE0991F1A40/TemporaryDirectory.KYRbJt/Sources/copyfile/copyfile.c"
- "/Library/Caches/com.apple.xbs/Sources/copyfile/copyfile.c"

```

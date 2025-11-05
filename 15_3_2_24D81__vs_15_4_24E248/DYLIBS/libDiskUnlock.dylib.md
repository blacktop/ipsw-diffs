## libDiskUnlock.dylib

> `/usr/lib/libDiskUnlock.dylib`

```diff

 68.0.0.1.0
-  __TEXT.__text: 0x2964
+  __TEXT.__text: 0x2934
   __TEXT.__auth_stubs: 0x350
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x62c
   __TEXT.__oslogstring: 0x547
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xb0
   __TEXT.__objc_methname: 0x253
   __TEXT.__objc_stubs: 0x400
   __DATA_CONST.__got: 0x90

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CDA3839D-ABFB-3768-952D-671722864378
-  Functions: 21
-  Symbols:   158
+  UUID: 5D5E13FC-4962-3862-B13B-3275B49FB0E3
+  Functions: 23
+  Symbols:   162
   CStrings:  194
 
Symbols:
+ DUKeychainItemAdd.cold.1
+ DUKeychainItemAdd.cold.2
+ __DMAPFSClass_block_invoke.cold.1
+ __DMManagerClass_block_invoke.cold.1
Functions:
~ __DUUnlockVolumeWithUserCredentialsAndOptions : 5552 -> 5540
- sub_2600096fc
~ _DUKeychainItemAdd : 1708 -> 1676
~ ___DMManagerClass_block_invoke : 120 -> 104
~ ___DMAPFSClass_block_invoke : 120 -> 104

```

## accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

-1036.0.0.0.0
-  __TEXT.__text: 0x520
-  __TEXT.__auth_stubs: 0x180
+1116.0.0.0.0
+  __TEXT.__text: 0x468
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x300
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x6e
   __TEXT.__cstring: 0xaf
   __TEXT.__objc_methname: 0x244
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__linkguard: 0x1d
+  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_selrefs: 0xc0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99E60291-1080-375C-9C1F-D8A96584E7BA
-  Functions: 5
-  Symbols:   41
+  UUID: 0CC2CE75-F0C2-30F3-B62B-6ED70431304A
+  Functions: 4
+  Symbols:   40
   CStrings:  40
 
Symbols:
+ __linkguard_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19

```

## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

```diff

-3515.3.1.0.0
-  __TEXT.__text: 0x2e88
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x11c
+3520.84.5.1.6
+  __TEXT.__text: 0x300c
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x128
   __TEXT.__const: 0x1c
   __TEXT.__cstring: 0x61a
   __TEXT.__oslogstring: 0x4df
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x6a7
+  __TEXT.__objc_methname: 0x6d4
   __TEXT.__objc_methtype: 0x20
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x4c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x248
+  __DATA.__objc_selrefs: 0x250
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C1E22E7B-C0B3-353F-9E1C-47CC968D83C5
-  Functions: 26
-  Symbols:   96
-  CStrings:  201
+  UUID: 00EC0F18-0F2D-302D-8744-AC8FA078C140
+  Functions: 27
+  Symbols:   95
+  CStrings:  202
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
CStrings:
+ "_performInternalSiriDataSharingResetIfNeeded"

```

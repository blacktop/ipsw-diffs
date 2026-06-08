## MCCleanup

> `/System/Library/DataClassMigrators/MCCleanup.migrator/MCCleanup`

```diff

-2438.120.3.0.0
-  __TEXT.__text: 0x290
+2479.0.0.0.0
+  __TEXT.__text: 0x28c
   __TEXT.__auth_stubs: 0x60
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x44

   __TEXT.__objc_methname: 0xe4
   __TEXT.__objc_methtype: 0x23
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x40
-  __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x40
+  __DATA_CONST.__got: 0x10
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x50
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E96ECE2D-4AA0-3AB9-9891-3084E04CC01D
+  UUID: 24F15315-909F-3E72-AE77-6567D8224063
   Functions: 6
   Symbols:   18
   CStrings:  36
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_be0 : 232 -> 228

```

## KeyboardMigrator

> `/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator`

```diff

-3511.100.0.0.0
-  __TEXT.__text: 0x50e4
-  __TEXT.__auth_stubs: 0x290
+3515.0.0.0.0
+  __TEXT.__text: 0x5014
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x9af
+  __TEXT.__cstring: 0x98a
   __TEXT.__oslogstring: 0x2c3
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methname: 0x893
   __TEXT.__objc_methtype: 0x18
   __TEXT.__ustring: 0x14
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x190
-  __DATA_CONST.__cfstring: 0x1420
+  __DATA_CONST.__cfstring: 0x13e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x148

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DDBCDC5F-9150-3B71-B45B-CF0D2B344B97
-  Functions: 30
-  Symbols:   95
-  CStrings:  446
+  UUID: FDC3713A-E79D-32CA-89EF-A08E165C8B5A
+  Functions: 29
+  Symbols:   94
+  CStrings:  442
 
Symbols:
- _TISolariumEnabled
Functions:
~ sub_11c0 : 8292 -> 8284
- sub_3224
~ _TIKeyboardMigratorTest : 104 -> 96
CStrings:
- "KeyboardAllowPaddle"
- "KeyboardVisceral"

```

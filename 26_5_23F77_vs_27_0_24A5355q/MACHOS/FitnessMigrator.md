## FitnessMigrator

> `/System/Library/DataClassMigrators/FitnessMigrator.migrator/FitnessMigrator`

```diff

-2026.5.4.0.0
-  __TEXT.__text: 0x43c
-  __TEXT.__auth_stubs: 0x100
+2027.0.93.0.0
+  __TEXT.__text: 0x3d4
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x18

   __TEXT.__objc_methname: 0x172
   __TEXT.__objc_methtype: 0x2b
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x50
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x70
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14074CF6-D081-34E4-87D8-7B4516EB065D
+  UUID: 1BD3D944-70A7-3AB2-9EB1-3EB50E543C1D
   Functions: 6
-  Symbols:   35
+  Symbols:   33
   CStrings:  32
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x21
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ sub_be4 : 392 -> 348
~ sub_e30 -> sub_e04 : 484 -> 424

```

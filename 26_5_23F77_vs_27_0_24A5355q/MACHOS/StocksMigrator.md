## StocksMigrator

> `/System/Library/DataClassMigrators/StocksMigrator.migrator/StocksMigrator`

```diff

 1555.1.0.0.0
-  __TEXT.__text: 0x5c4
-  __TEXT.__auth_stubs: 0x120
+  __TEXT.__text: 0x580
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x8

   __TEXT.__objc_methname: 0x134
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x98
-  __DATA_CONST.__got: 0x20
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x60
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73310F13-FB71-3BED-9864-71DA44CEA445
+  UUID: 95D2D54E-7CF4-3338-A12D-4926329ABCB5
   Functions: 2
-  Symbols:   31
+  Symbols:   28
   CStrings:  38
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
Functions:
~ sub_a44 : 1464 -> 1396

```

## CloudTabsMigrator

> `/System/Library/DataClassMigrators/CloudTabsMigrator.migrator/CloudTabsMigrator`

```diff

-7624.2.5.10.4
-  __TEXT.__text: 0x218
-  __TEXT.__auth_stubs: 0xa0
+7625.1.18.10.4
+  __TEXT.__text: 0x1e0
+  __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x8

   __TEXT.__objc_methname: 0x98
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x58
-  __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x50
+  __DATA_CONST.__got: 0x20
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x48
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4421D57-C021-3ABF-AB37-FB754B4CCB68
+  UUID: 4421DD63-97F1-3DC7-A65C-22D52076BEA0
   Functions: 2
-  Symbols:   75
+  Symbols:   73
   CStrings:  125
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_d0c : 524 -> 468

```

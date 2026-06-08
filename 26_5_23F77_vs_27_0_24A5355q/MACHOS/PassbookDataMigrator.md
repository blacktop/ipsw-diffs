## PassbookDataMigrator

> `/System/Library/DataClassMigrators/PassbookDataMigrator.migrator/PassbookDataMigrator`

```diff

-1642.6.5.0.0
-  __TEXT.__text: 0x168
-  __TEXT.__auth_stubs: 0x60
+1677.4.0.0.0
+  __TEXT.__text: 0x134
+  __TEXT.__auth_stubs: 0x50
   __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x8

   __TEXT.__objc_methname: 0x67
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x38
-  __DATA_CONST.__got: 0x10
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x30
+  __DATA_CONST.__got: 0x8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x28
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6193D7AA-5124-3C10-BE54-817105F480A5
+  UUID: BD82507E-AABF-3230-8896-8743AD82DFC2
   Functions: 2
-  Symbols:   17
+  Symbols:   15
   CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_a3c : 348 -> 296

```

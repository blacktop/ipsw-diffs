## HAENDataMigrator

> `/System/Library/DataClassMigrators/HAENDataMigrator.migrator/HAENDataMigrator`

```diff

-819.414.0.0.0
-  __TEXT.__text: 0x358
-  __TEXT.__auth_stubs: 0x140
+819.524.0.0.0
+  __TEXT.__text: 0x374
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x10

   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methname: 0x1b
   __TEXT.__objc_methtype: 0x8
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xa8
+  __TEXT.__unwind_info: 0x70
+  __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0xa0

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C6F97BE-BFF0-3842-9580-102760D369C5
+  UUID: BD344793-209E-3B47-B111-0766C8F7EDC1
   Functions: 4
-  Symbols:   44
+  Symbols:   45
   CStrings:  24
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
Functions:
~ _HAENDMLog : 68 -> 84
~ sub_bb8 -> sub_bc8 : 700 -> 712

```

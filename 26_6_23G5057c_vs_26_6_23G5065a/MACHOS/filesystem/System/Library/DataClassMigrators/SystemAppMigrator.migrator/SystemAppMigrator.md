## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-  __TEXT.__text: 0x80c8
+  __TEXT.__text: 0x80bc
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0x1660
   __TEXT.__objc_methlist: 0x614

   __TEXT.__oslogstring: 0x142
   __TEXT.__unwind_info: 0x240
   __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x328
   __DATA_CONST.__cfstring: 0x1600
   __DATA_CONST.__objc_classlist: 0x18

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 127
-  Symbols:   176
+  Symbols:   175
   CStrings:  716
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
- _kMISValidationOptionAllowLaunchWarning
Functions:
~ sub_6578 : 548 -> 536

```

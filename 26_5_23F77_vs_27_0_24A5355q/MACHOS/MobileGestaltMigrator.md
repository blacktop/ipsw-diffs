## MobileGestaltMigrator

> `/System/Library/DataClassMigrators/MobileGestaltMigrator.migrator/MobileGestaltMigrator`

```diff

-1484.120.3.0.0
-  __TEXT.__text: 0x2d4
+1608.0.0.0.0
+  __TEXT.__text: 0x2ac
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x18

   __TEXT.__objc_methname: 0x43
   __TEXT.__objc_methtype: 0x18
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x10
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x20
   __DATA.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CE235AA-C907-3976-B3B7-9A9130045009
+  UUID: 83E758EA-8AD5-37F5-8706-4B58EDB7DCC0
   Functions: 5
-  Symbols:   26
+  Symbols:   25
   CStrings:  15
 
Symbols:
+ _MGGetGlobalCache
+ __MGCacheContentsValid
- __MGCacheValid
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ sub_a1c : 424 -> 428
~ sub_bc4 -> sub_bc8 : 272 -> 228

```

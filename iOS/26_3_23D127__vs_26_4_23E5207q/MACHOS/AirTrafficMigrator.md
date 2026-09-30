## AirTrafficMigrator

> `/System/Library/DataClassMigrators/AirTrafficMigrator.migrator/AirTrafficMigrator`

```diff

-4025.400.1.0.0
-  __TEXT.__text: 0xdd8
-  __TEXT.__auth_stubs: 0x210
+4025.500.37.0.0
+  __TEXT.__text: 0xe50
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0x68
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0x5c
+  __TEXT.__gcc_except_tab: 0x60
   __TEXT.__const: 0x40
   __TEXT.__objc_methname: 0x2b2
   __TEXT.__cstring: 0x18b

   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methtype: 0x43
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x1e0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17F6A83C-E9D7-3BCB-9B8D-F2B00095A84A
+  UUID: 61A5A330-76E7-359E-A6EE-8CBA8C906647
   Functions: 11
-  Symbols:   51
+  Symbols:   50
   CStrings:  84
 
Symbols:
+ _objc_autorelease
+ _objc_release_x25
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_release_x22
- _objc_release_x28
- _objc_retain
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ sub_e2c : 192 -> 196
~ sub_eec -> sub_ef0 : 140 -> 156
~ sub_f78 -> sub_f8c : 116 -> 124
~ sub_ff8 -> sub_1014 : 2192 -> 2264
~ sub_1888 -> sub_18ec : 492 -> 508
~ sub_1a74 -> sub_1ae8 : 196 -> 200

```

## storagedatad

> `/usr/libexec/storagedatad`

```diff

-156.0.0.0.0
-  __TEXT.__text: 0x690
-  __TEXT.__auth_stubs: 0x1c0
+157.0.0.0.0
+  __TEXT.__text: 0x5cc
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__objc_methlist: 0x17c
-  __TEXT.__cstring: 0x41
+  __TEXT.__cstring: 0x43
   __TEXT.__oslogstring: 0xce
-  __TEXT.__objc_classname: 0x70
+  __TEXT.__objc_classname: 0x6e
   __TEXT.__objc_methname: 0x282
   __TEXT.__objc_methtype: 0x12d
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0x2f8
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_ivar: 0x4

   - /System/Library/PrivateFrameworks/StorageData.framework/StorageData
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4BF56BE-5C71-3A0C-BEF3-923C43F79DE1
+  UUID: 0ED35A53-3AC2-3EAA-BD73-27D207390CB3
   Functions: 10
-  Symbols:   44
+  Symbols:   42
   CStrings:  80
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_100000d18 : 84 -> 68
~ sub_100000db0 -> sub_100000da0 : 192 -> 184
~ sub_100000ed4 -> sub_100000ebc : 576 -> 508
~ sub_100001114 -> sub_1000010b8 : 344 -> 292
~ sub_100001278 -> sub_1000011e8 : 140 -> 136
~ sub_100001318 -> sub_100001284 : 144 -> 96

```

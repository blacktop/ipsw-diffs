## schooltimed

> `/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed`

```diff

-39.0.5.0.0
-  __TEXT.__text: 0x2dc
-  __TEXT.__auth_stubs: 0x140
+39.0.6.0.0
+  __TEXT.__text: 0x2a0
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x60
+  __TEXT.__cstring: 0x62
   __TEXT.__oslogstring: 0x3a
-  __TEXT.__objc_classname: 0xd
+  __TEXT.__objc_classname: 0xb
   __TEXT.__objc_methname: 0x112
   __TEXT.__objc_methtype: 0x28
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0xd0
   __DATA.__objc_selrefs: 0x68
   __DATA.__objc_ivar: 0x4

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CEA30B13-1948-3A16-B341-A76902375B68
+  UUID: FC56104D-FAA6-3E29-9E60-C12A98B59627
   Functions: 7
-  Symbols:   34
+  Symbols:   32
   CStrings:  25
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _objc_claimAutoreleasedReturnValue
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000bf0 -> sub_100000c00 : 176 -> 168
~ sub_100000ca0 -> sub_100000ca8 : 260 -> 256
~ sub_100000dbc -> sub_100000dc0 : 184 -> 136

```

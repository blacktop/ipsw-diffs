## CloudSettingsSyncAgent

> `/System/Library/CoreServices/CloudSettingsSyncAgent`

```diff

 113.0.0.0.0
-  __TEXT.__text: 0x68c
+  __TEXT.__text: 0x64c
   __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0x2c

   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methtype: 0x13
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x88
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E365FE2-3146-3CFD-9E6A-35E7D4394F61
+  UUID: 6A1AD09B-63B0-3418-A39B-64148A048953
   Functions: 6
-  Symbols:   37
+  Symbols:   36
   CStrings:  42
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000af0 : 328 -> 324
~ sub_100000d78 -> sub_100000d74 : 856 -> 800
~ sub_1000010d0 -> sub_100001094 : 100 -> 96

```

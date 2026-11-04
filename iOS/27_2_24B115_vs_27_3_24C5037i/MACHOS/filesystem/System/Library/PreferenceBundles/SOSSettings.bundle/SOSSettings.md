## SOSSettings

> `/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-670.200.1.0.0
-  __TEXT.__text: 0x13484
+670.300.21.0.0
+  __TEXT.__text: 0x134b0
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0x23e0
+  __TEXT.__objc_stubs: 0x2400
   __TEXT.__objc_methlist: 0xb20
   __TEXT.__cstring: 0xabb
   __TEXT.__objc_classname: 0x3c7
-  __TEXT.__objc_methname: 0x30c5
+  __TEXT.__objc_methname: 0x30e5
   __TEXT.__objc_methtype: 0xb50
   __TEXT.__oslogstring: 0x965
   __TEXT.__const: 0x5d4

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__auth_ptr: 0x230
   __DATA.__objc_const: 0x1498
-  __DATA.__objc_selrefs: 0xca0
+  __DATA.__objc_selrefs: 0xca8
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x670
   __DATA.__data: 0xa40

   - /System/Library/PrivateFrameworks/SOS.framework/SOS
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI
+  - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 406
-  Symbols:   293
-  CStrings:  719
+  Symbols:   294
+  CStrings:  720
 
Symbols:
+ _OBJC_CLASS_$_TUPlatformCapabilities
Functions:
~ sub_539c -> sub_540c : 3004 -> 3048
CStrings:
+ "isDualDisplayDevice"
```

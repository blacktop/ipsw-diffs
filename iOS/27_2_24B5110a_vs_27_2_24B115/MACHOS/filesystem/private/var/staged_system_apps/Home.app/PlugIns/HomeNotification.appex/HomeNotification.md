## HomeNotification

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1269.2.5.1.4
-  __TEXT.__text: 0x253a0
-  __TEXT.__auth_stubs: 0x1750
+1269.2.5.1.5
+  __TEXT.__text: 0x2550c
+  __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_stubs: 0x2dc0
   __TEXT.__objc_methlist: 0xf6c
-  __TEXT.__const: 0x8f8
-  __TEXT.__cstring: 0x17e0
+  __TEXT.__const: 0x908
+  __TEXT.__cstring: 0x1800
   __TEXT.__objc_methname: 0x3d81
   __TEXT.__objc_classname: 0x2b1
   __TEXT.__objc_methtype: 0xb82

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0xbb8
+  __DATA_CONST.__auth_got: 0xbc8
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x368
   __DATA.__objc_const: 0x1740

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 665
-  Symbols:   336
-  CStrings:  967
+  Symbols:   338
+  CStrings:  968
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_internalBuild
Functions:
~ sub_100025360 -> sub_1000253a0 : 824 -> 1188
CStrings:
+ "exclamationmark.bubble"
```

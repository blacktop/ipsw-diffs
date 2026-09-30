## ReplayKitAngel

> `/Applications/ReplayKitAngel.app/ReplayKitAngel`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 740.63.1.2.0
-  __TEXT.__text: 0x3e1c8
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_stubs: 0x2640
+  __TEXT.__text: 0x3e42c
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_stubs: 0x26a0
   __TEXT.__objc_methlist: 0x188c
   __TEXT.__const: 0x1e34
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0x1c95
-  __TEXT.__cstring: 0x1fc1
-  __TEXT.__objc_methname: 0x50f3
+  __TEXT.__oslogstring: 0x1cd5
+  __TEXT.__cstring: 0x1ff1
+  __TEXT.__objc_methname: 0x5123
   __TEXT.__objc_classname: 0x5ae
   __TEXT.__objc_methtype: 0x1b1d
   __TEXT.__swift5_typeref: 0x8ec

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x3c
-  __TEXT.__unwind_info: 0xe40
+  __TEXT.__unwind_info: 0xe48
   __TEXT.__eh_frame: 0x4e8
   __DATA_CONST.__const: 0x1b40
   __DATA_CONST.__cfstring: 0x320

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x950
+  __DATA_CONST.__auth_got: 0x960
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x400
   __DATA.__objc_const: 0x5dd8
-  __DATA.__objc_selrefs: 0x11a8
+  __DATA.__objc_selrefs: 0x11b8
   __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x16c0
   __DATA.__data: 0x1208

   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libAccessibility.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1511
-  Symbols:   577
-  CStrings:  1310
+  Symbols:   579
+  CStrings:  1314
 
Symbols:
+ _MGGetProductType
+ _objc_opt_respondsToSelector
Functions:
~ sub_100003bf0 -> sub_100003c30 : 16 -> 436
~ sub_1000085e4 -> sub_1000087c8 : 1032 -> 1052
~ sub_100008a98 -> sub_100008c90 : 388 -> 408
~ sub_100008c1c -> sub_100008e28 : 280 -> 300
~ sub_100008e00 -> sub_100009020 : 168 -> 292
~ sub_10003e538 -> sub_10003e7d4 : 2236 -> 2244
CStrings:
+ " [INFO] %{public}s:%d surface rotated, correcting orientation %ld -> %ld"
+ "-[RPCCUIVideoView currentInterfaceOrientation]"
+ "_windowInterfaceOrientation"
+ "surfaceType"
```

## NanoSleepBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/NanoSleepBridgeSetup.bundle/NanoSleepBridgeSetup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x2974
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0xe0
+7027.1.36.2.7
+  __TEXT.__text: 0x2980
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x8a
   __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methname: 0x267
+  __TEXT.__objc_methname: 0x287
   __TEXT.__objc_methtype: 0x8e
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x9e

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x150
   __TEXT.__eh_frame: 0x168
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x80
+  __DATA.__objc_selrefs: 0x88
   __DATA.__objc_data: 0x110
   __DATA.__data: 0xc8
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
+  - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
   - /System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 55
-  Symbols:   95
-  CStrings:  40
+  Symbols:   98
+  CStrings:  41
 
Symbols:
+ _OBJC_CLASS_$_HKSleepHealthStore
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ _objc_release_x22
Functions:
~ sub_16f8 -> sub_17a0 : 192 -> 204
CStrings:
+ "initWithHealthStore:"
+ "initWithIdentifier:scheduleHistoryWriter:"
- "initWithIdentifier:healthStore:"
```

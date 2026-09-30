## BatteriesWidgetIntentsExtension

> `/Applications/Batteries.app/PlugIns/BatteriesWidgetIntentsExtension.appex/BatteriesWidgetIntentsExtension`

```diff

-301.4.2.0.0
-  __TEXT.__text: 0x48ac
+314.0.0.0.0
+  __TEXT.__text: 0x48f8
   __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x18c
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x76
   __TEXT.__objc_methname: 0x417
   __TEXT.__constg_swiftt: 0x38
-  __TEXT.__swift5_typeref: 0x76
+  __TEXT.__swift5_typeref: 0xb7
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__oslogstring: 0xb5
+  __TEXT.__oslogstring: 0xac
+  __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x1df
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__eh_frame: 0x1b8
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__eh_frame: 0x1e8
   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter
   - /System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F2BAFC52-1336-371F-99CE-4E771D66CCFA
-  Functions: 50
-  Symbols:   107
+  UUID: F131A209-939F-3D42-85D2-5B2FEEEE6633
+  Functions: 55
+  Symbols:   100
   CStrings:  89
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x8
+ _objc_retain_x24
+ _swift_deallocObject
+ _swift_errorRelease
- ___chkstk_darwin
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _free
- _malloc
- _objc_retain_x22
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_release_n
CStrings:
+ "(%s) DefaultDevice|IsAutomatic : %@"
+ "(%s) connectedDevices: %s, preprocessedConnectedDevices: %s"
+ "(%s) provideDeviceOptionsCollection|IsAutomatic : %@"
- "IntentHandler|DefaultDevice|IsAutomatic : %@"
- "IntentHandler|connectedDevices: %s, preprocessedConnectedDevices: %s"
- "IntentHandler|provideDeviceOptionsCollection|IsAutomatic : %@"

```

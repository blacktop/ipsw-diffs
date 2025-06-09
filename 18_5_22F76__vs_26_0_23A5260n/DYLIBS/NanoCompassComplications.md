## NanoCompassComplications

> `/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications`

```diff

-631.5.3.0.0
-  __TEXT.__text: 0x3a630
-  __TEXT.__auth_stubs: 0xa60
+654.0.0.0.0
+  __TEXT.__text: 0x39f9c
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__delay_stubs: 0x58
+  __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0x39c4
   __TEXT.__const: 0x4d4
-  __TEXT.__cstring: 0x37f8
+  __TEXT.__cstring: 0x380e
   __TEXT.__ustring: 0xd6
   __TEXT.__oslogstring: 0x38e0
-  __TEXT.__gcc_except_tab: 0xa64
-  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__gcc_except_tab: 0xa28
   __TEXT.__constg_swiftt: 0x160
-  __TEXT.__swift5_typeref: 0x4a
+  __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_fieldmd: 0x80
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0x25
-  __TEXT.__unwind_info: 0xfd0
+  __TEXT.__unwind_info: 0xfc8
   __TEXT.__objc_classname: 0x9b2
-  __TEXT.__objc_methname: 0x84c6
+  __TEXT.__objc_methname: 0x84ab
   __TEXT.__objc_methtype: 0x11fb
-  __TEXT.__objc_stubs: 0x6dc0
+  __TEXT.__objc_stubs: 0x6da0
   __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0xb90
+  __DATA_CONST.__const: 0xb30
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2208
+  __DATA_CONST.__objc_selrefs: 0x2200
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x1110
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0x9c0
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__const: 0x9e0
   __AUTH_CONST.__cfstring: 0x2cc0
   __AUTH_CONST.__objc_const: 0x6c10
   __AUTH_CONST.__objc_doubleobj: 0x4c0

   __AUTH.__objc_data: 0x1ae8
   __AUTH.__data: 0x138
   __DATA.__objc_ivar: 0x504
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x930
+  __DATA.__data: 0x3cc
+  __DATA.__bss: 0x928
   __DATA.__common: 0x38
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications
   - /System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/MapsSync.framework/MapsSync
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
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
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4405B5E3-B987-32FC-BE1E-F9AB48FC0A00
-  Functions: 1519
-  Symbols:   660
-  CStrings:  2915
+  UUID: 25FB1CD0-7896-32FD-A8A0-36F4296103AD
+  Functions: 1527
+  Symbols:   656
+  CStrings:  2911
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ _MKBGetDeviceLockState
+ _MachContinuousTicksToMS
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _dlopen
+ _mach_timebase_info
+ _swift_arrayDestroy
- __sl_dlopen
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _abort_report_np
- _dlerror
- _dlsym
- _free
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
- "MKBDeviceUnlockedSinceBoot"
- "MKBGetDeviceLockState"
- "localizedCapitalizedString"
- "softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"

```

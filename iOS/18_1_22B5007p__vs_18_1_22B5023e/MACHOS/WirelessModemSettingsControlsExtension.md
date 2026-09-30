## WirelessModemSettingsControlsExtension

> `/System/Library/ExtensionKit/Extensions/WirelessModemSettingsControlsExtension.appex/WirelessModemSettingsControlsExtension`

```diff

-706.4.0.0.0
-  __TEXT.__text: 0xd200
+706.6.0.0.0
+  __TEXT.__text: 0xd12c
   __TEXT.__auth_stubs: 0xa80
   __TEXT.__const: 0x19f4
-  __TEXT.__cstring: 0x926
+  __TEXT.__cstring: 0x986
   __TEXT.__swift5_typeref: 0xa1e
   __TEXT.__swift5_reflstr: 0x274
   __TEXT.__swift5_assocty: 0x378

   __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x670
-  __TEXT.__eh_frame: 0x718
+  __TEXT.__eh_frame: 0x6c8
   __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x6c0
-  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 456
-  Symbols:   109
-  CStrings:  61
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 459
+  Symbols:   116
+  CStrings:  64
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_wapiCapability
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x25
- _objc_release_x28
- _objc_retain_x24
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "Could not find WLAN device"
+ "WLAN could not be powered on"
+ "WLAN tethering unsupported"

```

## DeveloperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents`

```diff

-1120.0.0.0.0
-  __TEXT.__text: 0x4a94
-  __TEXT.__auth_stubs: 0x3f0
+1122.0.0.0.0
+  __TEXT.__text: 0x4c5c
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x82e
-  __TEXT.__cstring: 0x1268
+  __TEXT.__cstring: 0x1308
   __TEXT.__swift5_typeref: 0x308
-  __TEXT.__swift5_reflstr: 0x27e
+  __TEXT.__swift5_reflstr: 0x25e
   __TEXT.__swift5_assocty: 0x118
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0xb4
-  __TEXT.__swift5_fieldmd: 0x15c
+  __TEXT.__swift5_fieldmd: 0x150
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x18
   __TEXT.__objc_methname: 0x28
   __TEXT.__unwind_info: 0x260
   __TEXT.__eh_frame: 0x1f8
-  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x418
-  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__const: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x1d8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
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
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 152
-  Symbols:   52
-  CStrings:  71
+  Symbols:   64
+  CStrings:  69
 
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
+ _objc_release_x27
CStrings:
+ "The “Network Link Conditioner” setting is in the iOS Settings app under “Developer” pane. This setting allows users to turn on or turn off network link conditioner and override cellular or WLAN connection conditions."
+ "The “Network Override” setting is in the iOS Settings app under “Developer” pane. This setting allows users to override cellular or WLAN cost."
- "Playable Content API"
- "RoutineSettings"
- "The “Playable Content API” setting is in the iOS Settings app under “Developer” pane. This setting allows users to run media player framework tests."
- "media framework test"

```

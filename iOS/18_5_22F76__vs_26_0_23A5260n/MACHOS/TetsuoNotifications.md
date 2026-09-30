## TetsuoNotifications

> `/System/Library/PreferenceBundles/TetsuoNotifications.bundle/TetsuoNotifications`

```diff

-16.120.1.0.0
-  __TEXT.__text: 0x4510
-  __TEXT.__auth_stubs: 0x580
+17.0.22.0.0
+  __TEXT.__text: 0x3e34
+  __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0xbe
-  __TEXT.__cstring: 0x1e2
+  __TEXT.__const: 0xe2
+  __TEXT.__cstring: 0x1c2
   __TEXT.__oslogstring: 0x1b9
   __TEXT.__swift5_typeref: 0x94
-  __TEXT.__objc_methname: 0x133
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x30
+  __TEXT.__objc_methname: 0xf1
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_reflstr: 0x1b
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x1a0
-  __TEXT.__eh_frame: 0x328
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x158
+  __TEXT.__eh_frame: 0x300
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x70
-  __DATA.__objc_selrefs: 0x90
+  __DATA.__objc_selrefs: 0x70
   __DATA.__objc_data: 0xc0
-  __DATA.__data: 0xe0
-  __DATA.__common: 0x20
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  __DATA.__data: 0xa8
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/StoreKit.framework/StoreKit
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion
   - /System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
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
-  UUID: 550DBA94-9411-3537-A2E2-CC8C427D61BB
-  Functions: 74
-  Symbols:   96
-  CStrings:  44
+  UUID: 4D02C397-07F4-3E72-AA66-5E95CC746553
+  Functions: 70
+  Symbols:   91
+  CStrings:  39
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x25
+ _objc_retain_x21
+ _objc_retain_x23
+ _swift_arrayDestroy
- _OBJC_CLASS_$_NSUserDefaults
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftIntents
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x20
- _objc_retain_x22
- _objc_retain_x24
CStrings:
+ "%s Error registering push notification channel:  %s / %@"
+ "%s Error unregistering push notification channel: %s / %@"
+ "%s Registering push notification channel %s"
+ "%s Unregistering push notification channel  %s"
+ "+ubhGDKlEfAAAHLUCeQW0A=="
+ "0n7oiTKlEfAAAOYe7g8NMw=="
- "%s Error registering push notification channel: %@"
- "%s Error unregistering push notification channel: %@"
- "%s Registering push notification channel"
- "%s Unregistering push notification channel"
- "boolForKey:"
- "debug.notifications.usestaging"
- "initWithSuiteName:"
- "notifications.latestNews"
- "notifications.restrictedGeo"
- "objectForKey:"
- "standardUserDefaults"

```

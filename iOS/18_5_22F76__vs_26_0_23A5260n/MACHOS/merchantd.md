## merchantd

> `/usr/libexec/merchantd`

```diff

-135.2.0.0.0
-  __TEXT.__text: 0x420
-  __TEXT.__auth_stubs: 0x1b0
+140.17.1.0.0
+  __TEXT.__text: 0x1c8
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__const: 0x4a
-  __TEXT.__objc_methname: 0x5d
-  __TEXT.__cstring: 0x20
+  __TEXT.__cstring: 0x7
+  __TEXT.__objc_methname: 0x13
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xd0
+  __TEXT.__unwind_info: 0x68
+  __DATA_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x28
-  __DATA.__common: 0x8
+  __DATA.__objc_selrefs: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  UUID: 070DDECA-ABBA-3AAD-88F0-A67BFC623728
-  Functions: 9
-  Symbols:   50
-  CStrings:  7
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 9E65A914-9475-3AA7-8558-6E0324FCFFB9
+  Functions: 5
+  Symbols:   43
+  CStrings:  3
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftsimd
- _$s10Foundation12NotificationV36_unconditionallyBridgeFromObjectiveCyACSo14NSNotificationCSgFZ
- _$s10Foundation12NotificationVMa
- _$s21ProximityReaderDaemon0C0C08shutdownC06reasons5NeverOSS_tF
- _NSCurrentLocaleDidChangeNotification
- _OBJC_CLASS_$_NSNotificationCenter
- ___chkstk_darwin
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x21
- _objc_release_x22
- _objc_retain_x22
CStrings:
- "addObserverForName:object:queue:usingBlock:"
- "defaultCenter"
- "removeObserver:"
- "v16@?0@\"NSNotification\"8"

```

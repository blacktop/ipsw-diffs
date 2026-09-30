## usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

-616.0.1.0.0
+623.0.0.0.0
   __TEXT.__text: 0x3bc4
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_stubs: 0x20

   __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 620A05C1-B389-3CFA-B7FF-810ED4DEE0D5
+  UUID: 30AA9241-6A4D-33A8-887D-605C320CC5E1
   Functions: 90
-  Symbols:   204
+  Symbols:   201
   CStrings:  113
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3

```

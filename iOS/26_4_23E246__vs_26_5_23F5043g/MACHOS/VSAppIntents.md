## VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

-593.40.9.0.0
+593.50.1.0.0
   __TEXT.__text: 0x5688
   __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_stubs: 0x120

   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x48
   __DATA.__data: 0x238

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount
   - /System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 19F81BD6-35C1-3105-9EB5-67DC0C873868
+  UUID: 4FB6CBE2-2B1B-3CED-B470-891E5FB7EC72
   Functions: 163
-  Symbols:   83
+  Symbols:   86
   CStrings:  34
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftUIKit

```

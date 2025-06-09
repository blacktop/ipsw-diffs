## SleepWidgetExtension

> `/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension`

```diff

-5200.5.1.0.0
+6074.1.2.4.0
   __TEXT.__text: 0x4e4
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
-  - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

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
-  UUID: 59DB9DD5-D47E-3BF1-A01B-75B374DD6AB5
+  UUID: 66FBAAFC-1DB5-30CA-A824-A6FD0B3CF102
   Functions: 13
-  Symbols:   54
+  Symbols:   48
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```

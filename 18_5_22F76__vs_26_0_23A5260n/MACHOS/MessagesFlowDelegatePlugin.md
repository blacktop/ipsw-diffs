## MessagesFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin`

```diff

-3405.21.1.0.0
+3500.55.4.0.0
   __TEXT.__text: 0xf8
   __TEXT.__auth_stubs: 0x60
   __TEXT.__const: 0x8a

   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_data: 0x48

   __DATA.__common: 0x10
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftVideoToolbox.dylib
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
-  UUID: 08540C46-F683-3668-A7DB-4F019D7F2DB2
+  UUID: 0C3E42D4-1847-3AD2-A6A8-54692CC5AC81
   Functions: 5
-  Symbols:   47
+  Symbols:   42
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
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

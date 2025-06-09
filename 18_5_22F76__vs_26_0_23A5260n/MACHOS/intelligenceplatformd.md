## intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd`

```diff

-124.19.0.1.0
+146.101.0.0.0
   __TEXT.__text: 0x228
   __TEXT.__auth_stubs: 0x110
   __TEXT.__const: 0xc0

   __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x8
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore
+  - /System/Library/PrivateFrameworks/IntelligencePlatformDataActions.framework/IntelligencePlatformDataActions
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
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
-  UUID: 11323289-42D2-3F38-B362-7BD91423BC09
+  UUID: 2244677E-29E5-3F44-8B78-77DD144F5894
   Functions: 5
-  Symbols:   47
+  Symbols:   46
   CStrings:  4
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```

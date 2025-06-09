## ReaderFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/ReaderFlowPlugin.bundle/ReaderFlowPlugin`

```diff

 3404.3.1.0.0
-  __TEXT.__text: 0x9f8
+  __TEXT.__text: 0xa10
   __TEXT.__auth_stubs: 0x240
   __TEXT.__const: 0x194
   __TEXT.__constg_swiftt: 0x6c

   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0xa8
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   __DATA.__bss: 0x280
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow
   - /System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents
   - /System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

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
-  UUID: F4BC2953-E058-385B-A9A3-FCA9D89CA46D
+  UUID: 5D93ADAA-3917-3D7B-BD4B-4EA31D540D72
   Functions: 43
-  Symbols:   58
+  Symbols:   53
   CStrings:  6
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_17ec -> sub_16b4 : 340 -> 368
~ sub_1940 -> sub_1824 : 572 -> 600
~ sub_1ce8 -> sub_1be8 : 80 -> 76
~ sub_1d38 -> sub_1c34 : 48 -> 32
~ sub_1d68 -> sub_1c54 : 32 -> 24
~ sub_1d88 -> sub_1c6c : 24 -> 20

```

## GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/GPNonUIExtension`

```diff

-112.0.0.0.0
-  __TEXT.__text: 0xa70
+132.3.103.0.0
+  __TEXT.__text: 0x9a4
   __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0xda

   __TEXT.__swift5_reflstr: 0x26
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__objc_methname: 0x137
+  __TEXT.__objc_methname: 0x152
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImagePlayground.framework/ImagePlayground
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

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
-  UUID: 349941DF-FCB5-3EFB-9562-8A8624B67E7B
+  UUID: ED2A8BA3-FB8F-3858-AD81-6981B3C3A138
   Functions: 16
-  Symbols:   73
+  Symbols:   69
   CStrings:  21
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x8
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x26
Functions:
~ sub_100001b6c -> sub_100001a7c : 1088 -> 884
CStrings:
+ "startGenerationWithStyle:promptElements:personalizationPolicyValue:replyHandler:batchID:"
+ "v56@0:8@\"NSString\"16@\"NSArray\"24@\"NSNumber\"32@?<v@?@\"GPImageXPCWrapper\"@\"NSError\">40@\"NSUUID\"48"
+ "v56@0:8@16@24@32@?40@48"
- "startGenerationWithStyle:promptElements:replyHandler:batchID:"
- "v48@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"GPImageXPCWrapper\"@\"NSError\">32@\"NSUUID\"40"
- "v48@0:8@16@24@?32@40"

```

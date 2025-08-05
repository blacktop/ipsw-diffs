## IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService`

```diff

-198.0.0.0.0
+200.0.0.0.0
   __TEXT.__text: 0xcc68
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x234

   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/IntelligencePlatformCompute

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 587DD39B-9B63-331B-8108-5F3D262AF87E
+  UUID: 44237747-6BFB-3807-84CA-92E1B0D599B9
   Functions: 236
-  Symbols:   232
+  Symbols:   233
   CStrings:  113
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUIKit

```

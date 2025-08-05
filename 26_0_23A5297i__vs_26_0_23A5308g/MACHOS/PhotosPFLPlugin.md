## PhotosPFLPlugin

> `/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin`

```diff

-800.32.101.0.0
+800.38.103.0.0
   __TEXT.__text: 0x2a54
   __TEXT.__auth_stubs: 0x5a0
   __TEXT.__const: 0x272

   __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0x270
+  __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Photos.framework/Photos
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis
   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4351E3AC-1DA7-3A7A-8669-61BE95E3FF34
+  UUID: 336C4CF7-8BDE-3081-9DDE-C184A45A1387
   Functions: 79
-  Symbols:   83
+  Symbols:   84
   CStrings:  11
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUIKit

```

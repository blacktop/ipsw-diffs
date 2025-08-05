## SensitiveContentAnalysisConfigurationExtension

> `/System/Library/ExtensionKit/Extensions/SensitiveContentAnalysisConfigurationExtension.appex/SensitiveContentAnalysisConfigurationExtension`

```diff

-123.0.0.0.0
+125.0.2.1.0
   __TEXT.__text: 0x236c
   __TEXT.__auth_stubs: 0x350
   __TEXT.__const: 0x788

   __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x398
-  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x208

   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 33FDA835-CD57-30C1-951C-EBC25D7FF792
+  UUID: 73963A2F-8A53-370B-B6FF-4F7CE014E5E6
   Functions: 126
-  Symbols:   57
+  Symbols:   58
   CStrings:  5
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUIKit

```

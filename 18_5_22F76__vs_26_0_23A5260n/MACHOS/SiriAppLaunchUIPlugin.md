## SiriAppLaunchUIPlugin

> `/System/Library/Snippets/UIPlugins/SiriAppLaunchUIPlugin.bundle/SiriAppLaunchUIPlugin`

```diff

-3405.10.1.0.0
+3500.19.1.0.0
   __TEXT.__text: 0xf8
   __TEXT.__auth_stubs: 0x60
   __TEXT.__cstring: 0x33

   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
   __DATA.__data: 0xa0
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents
   - /System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework
   - /System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftARKit.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSpriteKit.dylib
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
-  UUID: 5001DA09-31A2-3823-9340-6CE27F73D68D
+  UUID: D224CFF3-4275-33A1-8F96-86E9A38479DC
   Functions: 8
-  Symbols:   50
+  Symbols:   47
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftARKit
+ __swift_FORCE_LOAD_$_swiftSpriteKit
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
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

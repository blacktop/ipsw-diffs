## ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension`

```diff

-537.5.7.0.0
-  __TEXT.__text: 0x40f4
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x2a0
-  __TEXT.__const: 0x156
+571.0.0.0.0
+  __TEXT.__text: 0x3fd4
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x2c0
+  __TEXT.__const: 0x182
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__objc_methname: 0xa9e
+  __TEXT.__objc_methname: 0xb0a
   __TEXT.__cstring: 0x294
   __TEXT.__oslogstring: 0x6b
   __TEXT.__objc_classname: 0x33

   __TEXT.__swift_as_ret: 0x4
   __TEXT.__unwind_info: 0x1b8
   __TEXT.__eh_frame: 0xc0
-  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x4e8
-  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_selrefs: 0x2f8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x110
-  __DATA.__data: 0x208
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ScreenTime.framework/ScreenTime
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
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
-  UUID: FF2E41AE-91F6-3EAE-89AC-2E081776593D
-  Functions: 92
-  Symbols:   141
-  CStrings:  175
+  UUID: F9F9425F-1CA0-3112-996B-6EC50F134087
+  Functions: 95
+  Symbols:   138
+  CStrings:  180
 
Symbols:
+ _CGRectGetHeight
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
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
- _objc_retain
- _objc_retain_x23
CStrings:
+ "_canShowWhileLocked"
+ "_isSecureForRemoteViewService"
+ "bounds"
+ "setAdditionalSafeAreaInsets:"
+ "viewDidLayoutSubviews"

```

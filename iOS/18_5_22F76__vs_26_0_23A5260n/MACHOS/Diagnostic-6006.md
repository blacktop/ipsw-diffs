## Diagnostic-6006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6006.appex/Diagnostic-6006`

```diff

-820.122.1.0.0
-  __TEXT.__text: 0x33c
-  __TEXT.__auth_stubs: 0x120
+1053.0.0.0.0
+  __TEXT.__text: 0x348
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x174
   __TEXT.__const: 0x42
   __TEXT.__objc_methname: 0x247

   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methtype: 0x107
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__bss: 0x8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

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
-  UUID: A59A3939-6BB4-34E9-A5FF-53F5337EF347
+  UUID: 25199A34-B054-3858-8BC8-C5AA1E440DF5
   Functions: 8
-  Symbols:   47
+  Symbols:   41
   CStrings:  62
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x20
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x21
- _objc_retain_x8
Functions:
~ sub_100001414 -> sub_1000012dc : 168 -> 192
~ sub_1000014bc -> sub_10000139c : 364 -> 352

```

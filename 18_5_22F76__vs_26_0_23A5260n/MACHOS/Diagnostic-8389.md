## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-820.122.1.0.0
-  __TEXT.__text: 0x20044
-  __TEXT.__auth_stubs: 0xd60
+1053.0.0.0.0
+  __TEXT.__text: 0x1f474
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x534
   __TEXT.__cstring: 0x158d
   __TEXT.__objc_classname: 0x12e
   __TEXT.__objc_methname: 0xe15
   __TEXT.__objc_methtype: 0x6bb
-  __TEXT.__const: 0x3428
+  __TEXT.__const: 0x3418
   __TEXT.__constg_swiftt: 0xda0
-  __TEXT.__swift5_typeref: 0xbb5
+  __TEXT.__swift5_typeref: 0xbaf
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x682
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x8d8
-  __TEXT.__eh_frame: 0x8a0
-  __DATA_CONST.__auth_got: 0x6b8
+  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__eh_frame: 0x900
+  __DATA_CONST.__auth_got: 0x6c0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x2140
+  __DATA_CONST.__const: 0x2118
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
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
-  UUID: 1DED0046-B731-3E6D-9D53-3A302B9805E5
-  Functions: 858
-  Symbols:   169
+  UUID: 80EB79F9-B4C6-3531-9AF0-77FDE43AE85A
+  Functions: 852
+  Symbols:   164
   CStrings:  413
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_bridgeObjectRelease_n

```

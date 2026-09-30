## FeedbackRemoteView

> `/Applications/FeedbackRemoteView.app/FeedbackRemoteView`

```diff

-176.0.0.0.0
+182.0.0.0.0
   __TEXT.__text: 0x5420
   __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x818

   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E106200-30A4-32B6-99F8-DB481510B75A
+  UUID: FF41586D-A7F8-39CA-8B63-0623B8280BE7
   Functions: 123
-  Symbols:   210
+  Symbols:   208
   CStrings:  348
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3

```

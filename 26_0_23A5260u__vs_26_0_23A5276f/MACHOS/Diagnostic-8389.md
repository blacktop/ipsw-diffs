## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-1053.0.0.0.0
-  __TEXT.__text: 0x1f474
+1066.0.11.0.0
+  __TEXT.__text: 0x1f478
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x534
   __TEXT.__cstring: 0x158d
   __TEXT.__objc_classname: 0x12e
-  __TEXT.__objc_methname: 0xe15
+  __TEXT.__objc_methname: 0xe23
   __TEXT.__objc_methtype: 0x6bb
   __TEXT.__const: 0x3418
   __TEXT.__constg_swiftt: 0xda0

   __DATA_CONST.__auth_got: 0x6c0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x2118
+  __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 80EB79F9-B4C6-3531-9AF0-77FDE43AE85A
+  UUID: EC73C6BF-9677-3A96-8931-CD365D02B4A4
   Functions: 852
-  Symbols:   164
+  Symbols:   160
   CStrings:  413
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
Functions:
~ sub_100001c48 -> sub_100001b18 : 164 -> 168
CStrings:
+ "cStringUsingEncoding:"
- "cString"

```

## PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`

```diff

-150.38.0.0.0
-  __TEXT.__text: 0x7280
-  __TEXT.__auth_stubs: 0x6c0
+201.0.2.0.0
+  __TEXT.__text: 0x7aa0
+  __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x4b0
-  __TEXT.__cstring: 0xe9
-  __TEXT.__swift5_typeref: 0xd8
-  __TEXT.__oslogstring: 0x261
+  __TEXT.__const: 0x4a0
+  __TEXT.__cstring: 0x109
+  __TEXT.__swift5_typeref: 0xc0
+  __TEXT.__oslogstring: 0x2f1
   __TEXT.__constg_swiftt: 0x100
   __TEXT.__swift5_reflstr: 0x5c
   __TEXT.__swift5_fieldmd: 0x70

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0x64
+  __TEXT.__swift_as_cont: 0x88
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__eh_frame: 0x848
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__auth_ptr: 0x168
-  __DATA_CONST.__const: 0x1c0
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__eh_frame: 0x888
+  __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_ptr: 0x168
   __DATA.__objc_const: 0x120
   __DATA.__objc_selrefs: 0x10
   __DATA.__objc_data: 0x48
-  __DATA.__data: 0x1f8
+  __DATA.__data: 0x1e8
   __DATA.__bss: 0x380
-  __DATA.__common: 0x10
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4777944E-774C-371D-9C2D-EC3D0BCDEA61
-  Functions: 133
-  Symbols:   84
-  CStrings:  21
+  UUID: 3E707119-7E11-36DA-968E-720442FDF1B1
+  Functions: 137
+  Symbols:   88
+  CStrings:  23
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ _objc_release_x19
+ _objc_release_x25
+ _swift_release_x20
+ _swift_release_x8
+ _swift_retain_x20
- __swift_FORCE_LOAD_$_swiftCoreImage
- _objc_release_x21
- _swift_retain
CStrings:
+ "Client Request Interface Version: v%u.%u.%u\nCurrent TrustedML Interface Version: v%u.%u.%u\nCompatibility: Request interface is %ssupported"
+ "inference-version"

```

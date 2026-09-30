## PrivateFederatedLearning

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning`

```diff

-236.0.0.0.0
-  __TEXT.__text: 0x69b10
-  __TEXT.__auth_stubs: 0x1b50
+245.0.0.0.0
+  __TEXT.__text: 0x6d5d0
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__objc_methlist: 0xcbc
-  __TEXT.__const: 0x343c
-  __TEXT.__cstring: 0x38c5
-  __TEXT.__oslogstring: 0x1378
+  __TEXT.__const: 0x383c
+  __TEXT.__cstring: 0x3995
+  __TEXT.__oslogstring: 0x1468
   __TEXT.__ustring: 0x1e
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__swift5_typeref: 0xf06
-  __TEXT.__swift5_fieldmd: 0x1578
-  __TEXT.__constg_swiftt: 0x1ac0
+  __TEXT.__swift5_typeref: 0xfa4
+  __TEXT.__swift5_fieldmd: 0x15e4
+  __TEXT.__constg_swiftt: 0x1b64
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x1807
+  __TEXT.__swift5_reflstr: 0x1847
   __TEXT.__swift5_assocty: 0x378
-  __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x274
-  __TEXT.__swift5_types: 0x12c
+  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__swift5_proto: 0x27c
+  __TEXT.__swift5_types: 0x130
   __TEXT.__swift5_capture: 0x11c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1960
-  __TEXT.__eh_frame: 0x35c4
+  __TEXT.__unwind_info: 0x19e8
+  __TEXT.__eh_frame: 0x3808
   __TEXT.__objc_classname: 0x349
-  __TEXT.__objc_methname: 0x20b5
+  __TEXT.__objc_methname: 0x20d7
   __TEXT.__objc_methtype: 0x451
   __TEXT.__objc_stubs: 0x1d60
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__const: 0x278
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_selrefs: 0x9e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0xdb8
-  __AUTH_CONST.__auth_ptr: 0x550
-  __AUTH_CONST.__const: 0x1cd0
+  __AUTH_CONST.__auth_got: 0xe28
+  __AUTH_CONST.__auth_ptr: 0x560
+  __AUTH_CONST.__const: 0x1d18
   __AUTH_CONST.__cfstring: 0x1e20
-  __AUTH_CONST.__objc_const: 0x3ef0
+  __AUTH_CONST.__objc_const: 0x3fa0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0xa00
-  __AUTH.__data: 0x2290
+  __AUTH.__data: 0x2330
   __DATA.__objc_ivar: 0xa8
-  __DATA.__data: 0xda0
-  __DATA.__bss: 0x4870
-  __DATA.__common: 0x40
+  __DATA.__data: 0xdf8
+  __DATA.__bss: 0x47f0
+  __DATA.__common: 0x38
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1882
-  Symbols:   699
-  CStrings:  1110
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1914
+  Symbols:   708
+  CStrings:  1121
 
Symbols:
+ _CC_SHA256
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "$segmentation_point"
+ "Failed to create folder at %!s(MISSING), error: %!@(MISSING)"
+ "Failed to store PFL metrics at %!s(MISSING), error: %!@(MISSING)"
+ "Failed to store PFL result (gradients) at %!s(MISSING), error: %!@(MISSING)"
+ "Negative value is not representable"
+ "PFL metrics stored at %!s(MISSING)"
+ "PFL result (gradients) stored at %!s(MISSING)"
+ "_TtC24PrivateFederatedLearning30PopulationSegmentationInjector"
+ "dataWithJSONObject:options:error:"
+ "fileExistsAtPath:"
+ "store_task_result"
+ "userDefaults"
- "setString:forKey:"

```

## HealthBalanceDaemon

> `/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0x7c714
-  __TEXT.__auth_stubs: 0x21c0
+5200.1.3.0.0
+  __TEXT.__text: 0x7dda8
+  __TEXT.__auth_stubs: 0x2280
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__const: 0x200c
-  __TEXT.__cstring: 0x26d1
+  __TEXT.__const: 0x1ffc
+  __TEXT.__cstring: 0x26f1
   __TEXT.__constg_swiftt: 0x1068
   __TEXT.__swift5_typeref: 0xe90
   __TEXT.__swift5_reflstr: 0x13da

   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_proto: 0x120
   __TEXT.__swift5_types: 0x100
-  __TEXT.__oslogstring: 0x17a4
+  __TEXT.__oslogstring: 0x1824
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x344
-  __TEXT.__unwind_info: 0x1058
+  __TEXT.__unwind_info: 0x10a8
   __TEXT.__eh_frame: 0xe90
   __TEXT.__objc_classname: 0x259
-  __TEXT.__objc_methname: 0x20f4
+  __TEXT.__objc_methname: 0x2126
   __TEXT.__objc_methtype: 0x66c
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x808
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x850
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_protorefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x10e8
-  __AUTH_CONST.__auth_ptr: 0x548
+  __AUTH_CONST.__auth_got: 0x1148
+  __AUTH_CONST.__auth_ptr: 0x550
   __AUTH_CONST.__const: 0x1c08
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x27c8
-  __AUTH.__objc_data: 0x710
-  __AUTH.__data: 0xe98
-  __DATA.__data: 0x1598
-  __DATA.__common: 0xd0
-  __DATA.__bss: 0x1940
-  __DATA_DIRTY.__objc_data: 0x478
-  __DATA_DIRTY.__data: 0x7e8
-  __DATA_DIRTY.__bss: 0x400
-  __DATA_DIRTY.__common: 0x8
+  __AUTH.__objc_data: 0x4a8
+  __AUTH.__data: 0x798
+  __DATA.__data: 0x1068
+  __DATA.__bss: 0x16c0
+  __DATA.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__data: 0x14e8
+  __DATA_DIRTY.__common: 0x80
+  __DATA_DIRTY.__bss: 0x680
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1520
-  Symbols:   345
-  CStrings:  756
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1531
+  Symbols:   356
+  CStrings:  760
 
Symbols:
+ _HKFeatureAvailabilityContextDemoDataGeneration
+ _HKFeatureIdentifierOxygenSaturationRecording
+ _OBJC_CLASS_$_HKFeatureStatus
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "SleepingSampleAnalysisFeatureStatus"
+ "[%!{(MISSING)public}s] Error retrieving feature status: %!{(MISSING)public}@"
+ "[%!{(MISSING)public}s] Intercepting query with demo dataset, returning %!{(MISSING)public}ld summaries. Locale: %!s(MISSING)"
+ "[%!{(MISSING)public}s] Unable to find feature availability providing"
+ "featureAvailabilityProvidingForFeatureIdentifier:"
- "[%!{(MISSING)public}s] Intercepting query with demo dataset, returning %!{(MISSING)public}ld summaries"

```

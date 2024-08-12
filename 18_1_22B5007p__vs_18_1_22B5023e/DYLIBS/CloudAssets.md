## CloudAssets

> `/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets`

```diff

-2200.151.0.0.0
-  __TEXT.__text: 0x69620
-  __TEXT.__auth_stubs: 0x14c0
+2200.155.0.0.0
+  __TEXT.__text: 0x68dc0
+  __TEXT.__auth_stubs: 0x1460
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__cstring: 0x116a
-  __TEXT.__swift5_typeref: 0x186e
+  __TEXT.__cstring: 0x119a
+  __TEXT.__swift5_typeref: 0x18b0
   __TEXT.__swift5_fieldmd: 0x1244
-  __TEXT.__const: 0x5e80
+  __TEXT.__const: 0x5e70
   __TEXT.__constg_swiftt: 0x13a4
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x8dc
+  __TEXT.__swift5_reflstr: 0x8fc
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_types: 0x19c
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x5f8
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x2a4
-  __TEXT.__oslogstring: 0xabb
+  __TEXT.__swift5_capture: 0x2ac
+  __TEXT.__oslogstring: 0xafb
   __TEXT.__unwind_info: 0x2118
-  __TEXT.__eh_frame: 0x36b8
+  __TEXT.__eh_frame: 0x3660
   __TEXT.__objc_classname: 0x36
   __TEXT.__objc_methname: 0x568
   __TEXT.__objc_methtype: 0x21b
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x170
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0xa60
-  __AUTH_CONST.__auth_ptr: 0x4f0
+  __AUTH_CONST.__auth_got: 0xa30
+  __AUTH_CONST.__auth_ptr: 0x4e8
   __AUTH_CONST.__const: 0x2380
   __AUTH_CONST.__objc_const: 0x11a8
-  __AUTH.__data: 0xb8
-  __DATA.__data: 0x1a40
+  __DATA.__data: 0x1a90
   __DATA.__bss: 0xbd80
   __DATA.__common: 0x138
   __DATA_DIRTY.__objc_data: 0x408
-  __DATA_DIRTY.__data: 0x1628
+  __DATA_DIRTY.__data: 0x1708
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

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
-  Functions: 2999
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2996
   Symbols:   1239
-  CStrings:  280
+  CStrings:  281
 
Symbols:
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlF
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlFTu
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x1
+ _objc_retain_x22
- _$sScI4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTj
- _$sScI4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTjTu
- _$ss19AsyncPrefixSequenceV4basexvg
- _$ss19AsyncPrefixSequenceV5countSivg
- _$ss19AsyncPrefixSequenceV8IteratorV04baseD00aD0QzvM
- _$ss19AsyncPrefixSequenceV8IteratorV9remainingSivM
- _$ss19AsyncPrefixSequenceV8IteratorV9remainingSivg
- _$ss19AsyncPrefixSequenceV8IteratorVMn
- _$ss19AsyncPrefixSequenceV8IteratorV_5countADyx_G0aD0Qz_SitcfC
- _$ss19AsyncPrefixSequenceVMn
- _$ss19AsyncPrefixSequenceV_5countAByxGx_SitcfC
- _$ss31withCheckedThrowingContinuation8function_xSS_yScCyxs5Error_pGXEtYaKlF
- _$ss31withCheckedThrowingContinuation8function_xSS_yScCyxs5Error_pGXEtYaKlFTu
CStrings:
+ "ephemeral asset not received due to error %!@(MISSING) for request %!s(MISSING)"
+ "ephemeral asset not received for request %!s(MISSING)"
+ "process(requests:)"
+ "protectedActivity"
+ "protectedTaskMapping"
- "activity"
- "expect ephemeral asset but get %!s(MISSING)"
- "shouldn't receive skeleton here"
- "taskByRequest"

```

## VideoProcessing

> `/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing`

```diff

-1170.3.1.0.0
-  __TEXT.__text: 0x1a2f4c
-  __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0x1f8
-  __TEXT.__const: 0x25eef
-  __TEXT.__gcc_except_tab: 0x28cc
-  __TEXT.__cstring: 0x6887
-  __TEXT.__oslogstring: 0x6e6d
+1180.8.1.0.0
+  __TEXT.__text: 0x1a3c2c
+  __TEXT.__auth_stubs: 0x1ed0
+  __TEXT.__objc_methlist: 0x210
+  __TEXT.__const: 0x25eff
+  __TEXT.__gcc_except_tab: 0x292c
+  __TEXT.__cstring: 0x69b2
+  __TEXT.__oslogstring: 0x6fc3
   __TEXT.__ustring: 0xa4
-  __TEXT.__unwind_info: 0x27f8
+  __TEXT.__unwind_info: 0x2818
   __TEXT.__eh_frame: 0x438
   __TEXT.__objc_classname: 0x63
-  __TEXT.__objc_methname: 0xfcc
+  __TEXT.__objc_methname: 0x1012
   __TEXT.__objc_methtype: 0x541
-  __TEXT.__objc_stubs: 0xda0
-  __DATA_CONST.__got: 0xaf8
-  __DATA_CONST.__const: 0x1b30
+  __TEXT.__objc_stubs: 0xde0
+  __DATA_CONST.__got: 0xb20
+  __DATA_CONST.__const: 0x1b20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x7a0
-  __DATA_CONST.__objc_selrefs: 0x3a8
-  __AUTH_CONST.__const: 0x19c8
+  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_classrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__const: 0x19b8
   __AUTH_CONST.__cfstring: 0x3f20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__auth_got: 0xf78
   __AUTH.__data: 0x150
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_classrefs: 0xa8
-  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0xb20
+  __DATA.__data: 0xb30
   __DATA.__bss: 0x1e40
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
+  - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3016
-  Symbols:   1257
-  CStrings:  2019
+  Functions: 3018
+  Symbols:   1261
+  CStrings:  2034
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ _kVTCompressionPropertyKey_CalculateMeanSquaredError
+ _kVTSampleAttachmentKey_QualityMetrics
+ _kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError
+ _kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError
+ _kVTSampleAttachmentQualityMetricsKey_LumaMeanSquaredError
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
CStrings:
+ "CalculateMeanSquaredError"
+ "VCPReactionObserverSession (0x%llx): buffered capture devices are empty; re-setup\n"
+ "calculate_mse"
+ "discoverCaptureDevices"
+ "discoverCaptureDevicesAndSetupReactionObserver"
+ "quality metric does not contain ChromaBlueMeanSquaredError\n"
+ "quality metric does not contain ChromaRedMeanSquaredError\n"
+ "quality metric does not contain LumaMeanSquaredError\n"
+ "sample attachment does not contain QualityMetricsKey\n"
+ "unexpected quality metric type\n"

```

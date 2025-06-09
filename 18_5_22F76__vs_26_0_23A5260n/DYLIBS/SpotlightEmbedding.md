## SpotlightEmbedding

> `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x5258
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x36c
+2374.0.1.0.0
+  __TEXT.__text: 0x5508
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x4e6
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__oslogstring: 0x5bd
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__cstring: 0x512
+  __TEXT.__gcc_except_tab: 0x240
+  __TEXT.__oslogstring: 0x5be
+  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xc79
-  __TEXT.__objc_methtype: 0x1c7
-  __TEXT.__objc_stubs: 0xea0
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x268
+  __TEXT.__objc_methname: 0xc96
+  __TEXT.__objc_methtype: 0x1c9
+  __TEXT.__objc_stubs: 0xec0
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x610
+  __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_ivar: 0x48
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding
-  - /System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 5A24140C-68C2-30ED-B2D4-6845CC0EB573
-  Functions: 97
-  Symbols:   514
-  CStrings:  314
+  UUID: BAB0A6A5-A56E-34E2-AF55-7303D9D138BA
+  Functions: 102
+  Symbols:   533
+  CStrings:  322
 
Symbols:
+ -[SPEmbeddingModel warmedUp]
+ GCC_except_table23
+ GCC_except_table31
+ GCC_except_table6
+ _MediaAnalysisLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_SPEmbeddingModel._warmedUp
+ _SPEmbeddingModelVersion
+ ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.64
+ ___49-[SPEmbeddingModel preheatWithCompletionHandler:]_block_invoke.36
+ ___MediaAnalysisLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___getVCPMediaAnalyzerClass_block_invoke
+ ___getVCPMediaAnalyzerClass_block_invoke.cold.1
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringMediaAnalysis
+ _free
+ _getVCPMediaAnalyzerClass.softClass
+ _objc_getClass
+ _objc_msgSend$longValue
- GCC_except_table22
- GCC_except_table30
- _OBJC_CLASS_$_VCPMediaAnalyzer
- ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.65
- ___49-[SPEmbeddingModel preheatWithCompletionHandler:]_block_invoke.37
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
CStrings:
+ "%s"
+ "B"
+ "Unable to find class %s"
+ "VCPMediaAnalyzer"
+ "[qid=%ld] cancelRequestID, requestID: %d"
+ "_warmedUp"
+ "longValue"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis"
+ "warmedUp"
- "[qid=%d] cancelRequestID, requestID: %d"

```

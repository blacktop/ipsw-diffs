## AXMediaUtilities

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities`

```diff

-126.1.0.0.0
-  __TEXT.__text: 0xc3c40
+127.1.2.0.0
+  __TEXT.__text: 0xc40f0
   __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0xa648
+  __TEXT.__objc_methlist: 0xa650
   __TEXT.__const: 0x15de
-  __TEXT.__gcc_except_tab: 0x3f78
-  __TEXT.__cstring: 0xa46c
-  __TEXT.__oslogstring: 0x501d
+  __TEXT.__gcc_except_tab: 0x3fb0
+  __TEXT.__cstring: 0xa48c
+  __TEXT.__oslogstring: 0x5019
   __TEXT.__dlopen_cstrs: 0xc79
   __TEXT.__ustring: 0x422
   __TEXT.__swift5_typeref: 0x2ee

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x37bc
+  __TEXT.__unwind_info: 0x37d0
   __TEXT.__eh_frame: 0x4e8
   __TEXT.__objc_classname: 0x13bc
-  __TEXT.__objc_methname: 0x1b419
-  __TEXT.__objc_methtype: 0x3dab
-  __TEXT.__objc_stubs: 0x12460
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__const: 0x2668
+  __TEXT.__objc_methname: 0x1b4a3
+  __TEXT.__objc_methtype: 0x3dc8
+  __TEXT.__objc_stubs: 0x12480
+  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__const: 0x2690
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xedb0
-  __DATA_CONST.__objc_selrefs: 0x5cc8
+  __DATA_CONST.__objc_const: 0xedd0
+  __DATA_CONST.__objc_selrefs: 0x5cd0
   __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__cfstring: 0xc980
   __AUTH_CONST.__objc_const: 0x5238

   __AUTH.__data: 0x78
   __DATA.__got_weak: 0x10
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x840
+  __DATA.__objc_classrefs: 0x848
   __DATA.__objc_superrefs: 0x410
-  __DATA.__objc_ivar: 0xe18
+  __DATA.__objc_ivar: 0xe1c
   __DATA.__data: 0xeb0
   __DATA.__bss: 0x1cb0
   __DATA.__common: 0x20

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5230
-  Symbols:   16355
-  CStrings:  7706
+  Functions: 5232
+  Symbols:   16364
+  CStrings:  7710
 
Symbols:
+ -[AXMCaptionDetectorNode _withLock_cloneCaptionModelIfNeeded:].cold.4
+ -[AXMMediaAnalysisTextDetectorNode processResults:context:metrics:textDetectionLocales:textDetectionOptions:requestID:error:]
+ -[AXMMediaAnalysisTextDetectorNode processResults:context:metrics:textDetectionLocales:textDetectionOptions:requestID:error:].cold.1
+ -[AXMMediaAnalysisTextDetectorNode processResults:context:metrics:textDetectionLocales:textDetectionOptions:requestID:error:].cold.2
+ -[AXMMediaAnalysisTextDetectorNode processResults:context:metrics:textDetectionLocales:textDetectionOptions:requestID:error:].cold.3
+ _MLAllComputeDevicesSoft
+ _MLAllComputeDevicesSoft.cold.1
+ _OBJC_CLASS_$_MLNeuralEngineComputeDevice
+ _OBJC_IVAR_$_AXMMediaAnalysisTextDetectorNode._processResultQueue
+ _VNComputeStageMain
+ ___53-[AXMMediaAnalysisTextDetectorNode evaluate:metrics:]_block_invoke_3
+ ___block_descriptor_100_e8_32s40s48s56s64s72s80s88w_e5_v8?0lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88w_e20_v20?0i8"NSError"12ls32l8w88l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___getMLAllComputeDevicesSymbolLoc_block_invoke
+ _dgetrf$NEWLAPACK
+ _dgetri$NEWLAPACK
+ _getMLAllComputeDevicesSymbolLoc.ptr
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$processResults:context:metrics:textDetectionLocales:textDetectionOptions:requestID:error:
+ _objc_msgSend$setComputeDevice:forComputeStage:
- -[AXMEvaluationNode validateVisionKitSoftLinkSymbols]
- -[AXMEvaluationNode validateVisionKitSoftLinkSymbols].cold.1
- ___53-[AXMMediaAnalysisTextDetectorNode evaluate:metrics:]_block_invoke_2.cold.1
- ___53-[AXMMediaAnalysisTextDetectorNode evaluate:metrics:]_block_invoke_2.cold.2
- ___53-[AXMMediaAnalysisTextDetectorNode evaluate:metrics:]_block_invoke_2.cold.3
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e20_v20?0i8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___getVNProcessingDeviceClass_block_invoke
- ___getVNProcessingDeviceClass_block_invoke.cold.1
- _dgetrf_
- _dgetri_
- _getVNProcessingDeviceClass
- _getVNProcessingDeviceClass.softClass
- _objc_msgSend$defaultANEDevice
- _objc_msgSend$setProcessingDevice:
CStrings:
+ "Could not clone caption model. clonefile(%@, %@, %o) FAILED with (%d : %s) - trying copy"
+ "Could not copy caption model. %@"
+ "MLAllComputeDevices"
+ "_processResultQueue"
+ "copyItemAtPath:toPath:error:"
+ "process-results-queue-axmedia"
+ "processResults:context:metrics:textDetectionLocales:textDetectionOptions:requestID:error:"
+ "setComputeDevice:forComputeStage:"
+ "v68@0:8@16@24@32@40@48i56@60"
- "Could not clone caption model. clonefile(%@, %@, %o) FAILED with (%d : %s)"
- "Could not evaluate. VNProcessingDeviceSoft was nil"
- "VNProcessingDevice"
- "defaultANEDevice"
- "setProcessingDevice:"

```

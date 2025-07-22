## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

```diff

-659.0.0.0.4
-  __TEXT.__text: 0x1e2964
-  __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_methlist: 0xc72c
+661.0.0.0.3
+  __TEXT.__text: 0x1e4b9c
+  __TEXT.__auth_stubs: 0x1600
+  __TEXT.__objc_methlist: 0xc7fc
   __TEXT.__const: 0x2e40
-  __TEXT.__cstring: 0x26c61
-  __TEXT.__oslogstring: 0x15791
-  __TEXT.__gcc_except_tab: 0x1264
-  __TEXT.__unwind_info: 0x2cc8
+  __TEXT.__cstring: 0x26e3f
+  __TEXT.__oslogstring: 0x159e6
+  __TEXT.__gcc_except_tab: 0x1350
+  __TEXT.__unwind_info: 0x2d50
   __TEXT.__eh_frame: 0xc18
-  __TEXT.__objc_classname: 0x1572
-  __TEXT.__objc_methname: 0x218cf
-  __TEXT.__objc_methtype: 0x9175
-  __TEXT.__objc_stubs: 0xbe80
-  __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0x750
-  __DATA_CONST.__objc_classlist: 0x588
+  __TEXT.__objc_classname: 0x1582
+  __TEXT.__objc_methname: 0x21a73
+  __TEXT.__objc_methtype: 0x91c0
+  __TEXT.__objc_stubs: 0xc000
+  __DATA_CONST.__got: 0xaa8
+  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d08
+  __DATA_CONST.__objc_selrefs: 0x5d90
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0xb08
-  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__auth_got: 0xb18
+  __AUTH_CONST.__const: 0x710
   __AUTH_CONST.__cfstring: 0x6800
-  __AUTH_CONST.__objc_const: 0x1d650
-  __AUTH_CONST.__objc_intobj: 0xa08
+  __AUTH_CONST.__objc_const: 0x1d7c8
+  __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x1100
-  __AUTH.__objc_data: 0xaf0
+  __AUTH.__objc_data: 0xb40
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x167c
+  __DATA.__objc_ivar: 0x1698
   __DATA.__data: 0x11ac0
   __DATA.__common: 0x220
   __DATA.__bss: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C3DFBA3-3E15-3D6D-A2A5-EA5ABDA6C871
-  Functions: 6709
-  Symbols:   19609
-  CStrings:  11975
+  UUID: 32E605A5-74D5-38C8-A969-384701B92943
+  Functions: 6749
+  Symbols:   19734
+  CStrings:  12028
 
Symbols:
+ +[CMIFuture combine:]
+ +[CMIFuture combine:initialValue:fold:]
+ +[CMIFuture(Metal) commandBufferCompletionStatusHandler]
+ +[CMIFuture(Metal) futureErrorWithCommandBuffer:callbackQueue:]
+ +[CMIFuture(Metal) futureErrorWithSharedEvent:waitValue:listener:]
+ +[CMIFuture(Metal) futureWithCommandBuffer:callbackQueue:valueHandler:]
+ -[CMIFuture .cxx_destruct]
+ -[CMIFuture cancel]
+ -[CMIFuture flatMap:]
+ -[CMIFuture ifValue:otherwise:]
+ -[CMIFuture initWithCallbackQueue:]
+ -[CMIFuture init]
+ -[CMIFuture map:]
+ -[CMIFuture setValue:]
+ -[CMIFuture then:]
+ -[CMIFuture valueWaitingUpToTimeout:status:]
+ -[CMISmartStyleMetalRendererV1 setup].cold.6
+ -[CMIStyleEngineApplyStyle enqueueToCommandBuffer:].cold.8
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.1
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.2
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.3
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.4
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.5
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.6
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.7
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.8
+ -[CMISubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:expBias:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:].cold.9
+ GCC_except_table14
+ GCC_except_table2
+ GCC_except_table21
+ GCC_except_table3
+ _OBJC_CLASS_$_CMIFuture
+ _OBJC_IVAR_$_CMIFuture._callbackQueue
+ _OBJC_IVAR_$_CMIFuture._value
+ _OBJC_IVAR_$_CMIFuture._valueGroup
+ _OBJC_IVAR_$_CMIFuture._valueIsSet
+ _OBJC_IVAR_$_CMIFuture._valueStatus
+ _OBJC_IVAR_$_CMISmartStyleMetalRendererV1._sharedEvent
+ _OBJC_IVAR_$_CMISmartStyleMetalRendererV1._sharedEventSignal
+ _OBJC_METACLASS_$_CMIFuture
+ __OBJC_$_CLASS_METHODS_CMIFuture(Metal)
+ __OBJC_$_INSTANCE_METHODS_CMIFuture
+ __OBJC_$_INSTANCE_VARIABLES_CMIFuture
+ __OBJC_CLASS_RO_$_CMIFuture
+ __OBJC_METACLASS_RO_$_CMIFuture
+ ___17-[CMIFuture map:]_block_invoke
+ ___18-[CMIFuture then:]_block_invoke
+ ___21+[CMIFuture combine:]_block_invoke
+ ___21+[CMIFuture combine:]_block_invoke_2
+ ___21-[CMIFuture flatMap:]_block_invoke
+ ___21-[CMIFuture flatMap:]_block_invoke.2
+ ___35-[CMIFuture initWithCallbackQueue:]_block_invoke
+ ___39+[CMIFuture combine:initialValue:fold:]_block_invoke
+ ___39+[CMIFuture combine:initialValue:fold:]_block_invoke.5
+ ___56+[CMIFuture(Metal) commandBufferCompletionStatusHandler]_block_invoke
+ ___66+[CMIFuture(Metal) futureErrorWithSharedEvent:waitValue:listener:]_block_invoke
+ ___71+[CMIFuture(Metal) futureWithCommandBuffer:callbackQueue:valueHandler:]_block_invoke
+ ___block_descriptor_32_e28_16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_32_e8_16?08l
+ ___block_descriptor_40_e8_32s_e11_v24?08q16ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e11_v24?08q16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e28_v16?0"<MTLCommandBuffer>"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_16?08ls40l8s32l8
+ ___block_descriptor_48_e8_32s_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8
+ ___block_descriptor_56_e8_32r40r48r_e28_v16?0"<MTLCommandBuffer>"8lr32l8r40l8r48l8
+ ___block_descriptor_64_e8_32r40r48r56r_e11_v24?08Q16lr32l8r40l8r48l8r56l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72r80r_e11_v24?08q16ls32l8r64l8r72l8s40l8r80l8s56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72r_e11_v24?08q16ls32l8r56l8r64l8s40l8r72l8s48l8
+ _dispatch_after
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_msgSend$cancel
+ _objc_msgSend$code
+ _objc_msgSend$commandBufferCompletionStatusHandler
+ _objc_msgSend$dispatchQueue
+ _objc_msgSend$futureWithCommandBuffer:callbackQueue:valueHandler:
+ _objc_msgSend$initWithCallbackQueue:
+ _objc_msgSend$map:
+ _objc_msgSend$setValue:
+ _objc_msgSend$sharedListener
+ _objc_msgSend$signaledValue
+ _objc_msgSend$then:
+ _objc_msgSend$valueWaitingUpToTimeout:status:
- ___28-[CMMTLCommandBuffer commit]_block_invoke.1507
- ___block_descriptor_56_e8_32r40r48r_e29_v24?0"<MTLSharedEvent>"8Q16lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e28_v16?0"<MTLCommandBuffer>"8lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e28_v16?0"<MTLCommandBuffer>"8ls32l8r40l8r48l8
- ___block_literal_global.1509
- _getprogname
- _strcmp
CStrings:
+ "+[CMIFuture(Metal) commandBufferCompletionStatusHandler]_block_invoke"
+ "-[CMIFuture flatMap:]_block_invoke"
+ "-[CMIFuture initWithCallbackQueue:]_block_invoke"
+ "-[CMIFuture setValue:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture+Metal.m %s: command buffer did not complete but gave no error %ld"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture flatMap: transform() returned nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture setValue: called on already-resolved future"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture timed out"
+ "<<<< FigRegWarpPPGPU >>>> %s: Registration only found %d inlier corners"
+ "@16@?0@\"<MTLCommandBuffer>\"8"
+ "@16@?0@8"
+ "@32@0:8Q16^q24"
+ "@40@0:8@16@24@?32"
+ "@40@0:8@16Q24@32"
+ "@?16@0:8"
+ "CMIFuture"
+ "CommandBuffer <%@> | Status <%@>"
+ "Metal"
+ "_callbackQueue"
+ "_value"
+ "_valueGroup"
+ "_valueIsSet"
+ "_valueStatus"
+ "cancel"
+ "chroma"
+ "code"
+ "com.apple.coremedia.CMISmartStyleMetalRendererV1"
+ "combine:"
+ "combine:initialValue:fold:"
+ "commandBufferCompletionStatusHandler"
+ "flatMap:"
+ "futureErrorWithCommandBuffer:callbackQueue:"
+ "futureErrorWithSharedEvent:waitValue:listener:"
+ "futureWithCommandBuffer:callbackQueue:valueHandler:"
+ "gpustarttime"
+ "ifValue:otherwise:"
+ "initWithCallbackQueue:"
+ "instanceMask0"
+ "instanceMask1"
+ "instanceMask2"
+ "instanceMask3"
+ "luma"
+ "map:"
+ "outputImageRect alignment requirments not satisfied"
+ "personMask"
+ "refinedResult->numInliers >= ( 6 )"
+ "setValue:"
+ "sharedListener"
+ "signaledValue"
+ "simd_all( ! ( validOffset & ( PixelsPerThread - 1 ) ) )"
+ "skinMask"
+ "then:"
+ "toneMap"
+ "v24@?0@8Q16"
+ "v24@?0@8q16"
+ "v32@0:8@?16@?24"
+ "valueWaitingUpToTimeout:status:"
- "<<<< MetalIntercept >>>> %s: Deferred processing: exiting due to GPU failure"
- "CMIMetalRendderer"
- "GPU error during processing: CommandBuffer <%@> | Status <%@>"
- "continuation"
- "deferredmediad"

```

## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-664.60.7.0.0
-  __TEXT.__text: 0x28aeb8
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_methlist: 0x11ca0
-  __TEXT.__const: 0x102fb0
-  __TEXT.__cstring: 0x336fb
-  __TEXT.__gcc_except_tab: 0x19cc
-  __TEXT.__oslogstring: 0x357e5
+664.62.12.0.0
+  __TEXT.__text: 0x28ad6c
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x11cd0
+  __TEXT.__const: 0x102fa0
+  __TEXT.__cstring: 0x33805
+  __TEXT.__gcc_except_tab: 0x13f8
+  __TEXT.__oslogstring: 0x35a20
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4e28
-  __TEXT.__objc_classname: 0x3208
-  __TEXT.__objc_methname: 0x3427e
-  __TEXT.__objc_methtype: 0x172ca
-  __TEXT.__objc_stubs: 0x16480
+  __TEXT.__unwind_info: 0x4e10
+  __TEXT.__objc_classname: 0x3220
+  __TEXT.__objc_methname: 0x342de
+  __TEXT.__objc_methtype: 0x1732d
+  __TEXT.__objc_stubs: 0x164a0
   __DATA_CONST.__got: 0xbe0
-  __DATA_CONST.__const: 0x1358
-  __DATA_CONST.__objc_classlist: 0xda0
+  __DATA_CONST.__const: 0x1380
+  __DATA_CONST.__objc_classlist: 0xda8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6740
+  __DATA_CONST.__objc_selrefs: 0x6750
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa70
+  __DATA_CONST.__objc_superrefs: 0xa78
   __DATA_CONST.__objc_arraydata: 0xec0
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x13b20
-  __AUTH_CONST.__objc_const: 0x37578
+  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x13b80
+  __AUTH_CONST.__objc_const: 0x37670
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xb58
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_ivar: 0x3a60
+  __AUTH.__objc_data: 0x12c0
+  __DATA.__objc_ivar: 0x3a6c
   __DATA.__data: 0xba8
   __DATA.__common: 0x24
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x75d0
   __DATA_DIRTY.__bss: 0x140
   __DATA_DIRTY.__common: 0xf8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF245F43-12C1-35A5-9DC8-32D05BE34390
-  Functions: 13409
-  Symbols:   39513
-  CStrings:  19389
+  UUID: DA0DD10B-08A6-3C7C-8401-FDEEE1F45C34
+  Functions: 13439
+  Symbols:   39625
+  CStrings:  19413
 
Symbols:
+ -[CMITiledInferenceProcessorStage runProcessor:withTileCount:completion:]
+ -[CMITiledInferenceProcessorStage runProcessor:withTileCount:completion:].cold.1
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:]
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.1
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.10
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.11
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.12
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.13
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.14
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.15
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.2
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.3
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.4
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.5
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.6
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.7
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.8
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:].cold.9
+ -[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:completion:]
+ -[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:completion:]
+ -[NRFNetworkStatusTracker .cxx_destruct]
+ -[NRFNetworkStatusTracker errorHandler]
+ -[NRFNetworkStatusTracker errorHandler].cold.1
+ -[NRFNetworkStatusTracker initWithLabel:]
+ -[NRFNetworkStatusTracker verifyNetworkStatusIfSynchronous]
+ -[NRFNetworkStatusTracker verifyNetworkStatusIfSynchronous].cold.1
+ _NRFCheckStatusIsAsynchronous.checkStatusIsAsynchronous
+ _NRFCheckStatusIsAsynchronous.sOnceToken
+ _OBJC_CLASS_$_NRFNetworkStatusTracker
+ _OBJC_IVAR_$_NRFNetworkStatusTracker._label
+ _OBJC_IVAR_$_NRFNetworkStatusTracker._networkStatus
+ _OBJC_IVAR_$_NRFNetworkStatusTracker._networkStatusGroup
+ _OBJC_METACLASS_$_NRFNetworkStatusTracker
+ __OBJC_$_INSTANCE_METHODS_NRFNetworkStatusTracker
+ __OBJC_$_INSTANCE_VARIABLES_NRFNetworkStatusTracker
+ __OBJC_CLASS_RO_$_NRFNetworkStatusTracker
+ __OBJC_METACLASS_RO_$_NRFNetworkStatusTracker
+ ___35-[LearnedHRNRProcessor runPipeline]_block_invoke.201
+ ___37-[LearnedFusionProcessor runPipeline]_block_invoke.300
+ ___39-[NRFNetworkStatusTracker errorHandler]_block_invoke
+ ___39-[NRFNetworkStatusTracker errorHandler]_block_invoke.1
+ ___73-[CMITiledInferenceProcessorStage runProcessor:withTileCount:completion:]_block_invoke
+ ___99-[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:completion:]_block_invoke
+ ___NRFCheckStatusIsAsynchronous_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_52_e8_32s40bs_e8_v12?0i8ls32l8s40l8
+ _getprogname
+ _objc_msgSend$errorHandler
+ _objc_msgSend$initWithLabel:
+ _objc_msgSend$runDemosaicWithInputRawTexture:outputRgbTexture:completion:
+ _objc_msgSend$runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:completion:
+ _objc_msgSend$runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:completion:
+ _objc_msgSend$runProcessor:withTileCount:completion:
+ _objc_msgSend$verifyNetworkStatusIfSynchronous
+ _strcmp
- -[CMITiledInferenceProcessorStage runProcessor:withTileCount:].cold.1
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:]
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.1
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.10
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.11
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.12
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.13
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.14
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.15
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.2
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.3
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.4
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.5
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.6
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.7
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.8
- -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.9
- -[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:]
- -[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:]
- -[LearnedFusionProcessor runLearnedDemosaicNetworkStage]
- -[LearnedHRNRProcessor checkNetworkStatusWithLabel:statusGroup:status:]
- GCC_except_table46
- GCC_except_table51
- ___33-[LearnedNRProcessor runPipeline]_block_invoke
- ___35-[LearnedHRNRProcessor runPipeline]_block_invoke.188
- ___35-[LearnedHRNRProcessor runPipeline]_block_invoke.202
- ___35-[LearnedHRNRProcessor runPipeline]_block_invoke_2
- ___37-[LearnedFusionProcessor runPipeline]_block_invoke.292
- ___62-[CMITiledInferenceProcessorStage runProcessor:withTileCount:]_block_invoke
- ___block_descriptor_48_e8_32r40r_e8_v12?0i8lr32l8r40l8
- _objc_msgSend$checkNetworkStatusWithLabel:statusGroup:status:
- _objc_msgSend$runDemosaicWithInputRawTexture:outputRgbTexture:
- _objc_msgSend$runLearnedDemosaicNetworkStage
- _objc_msgSend$runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:
- _objc_msgSend$runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:
- _objc_msgSend$runProcessor:withTileCount:
CStrings:
+ "-[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:completion:]"
+ "-[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:completion:]"
+ "-[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:completion:]"
+ "-[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:completion:]_block_invoke"
+ "-[NRFNetworkStatusTracker errorHandler]_block_invoke"
+ "-[NRFNetworkStatusTracker verifyNetworkStatusIfSynchronous]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/Common/NRFCommon.m %s: Added Wait for < %@ > to get network status is = %.2f msecs"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/Common/NRFCommon.m %s: Network %@ failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/Common/NRFCommon.m %s: Network %@ finished with status = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Faile demosacing %@ with error = %d "
+ "@\"NSObject<OS_dispatch_group>\""
+ "@?16@0:8"
+ "NRFNetworkStatusTracker"
+ "_label"
+ "_networkStatus"
+ "_networkStatusGroup"
+ "deferredmediad"
+ "errorHandler"
+ "i40@0:8@1624@?32"
+ "i40@0:8@16@24@?32"
+ "i56@0:8@16@24@32@40@?48"
+ "initWithLabel:"
+ "lfNetwork"
+ "main_EVM"
+ "nrf.checkStatusIsAsynchronous"
+ "runDemosaicWithInputRawTexture:outputRgbTexture:completion:"
+ "runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:completion:"
+ "runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:completion:"
+ "runProcessor:withTileCount:completion:"
+ "verifyNetworkStatusIfSynchronous"
- "-[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:]"
- "-[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:]"
- "-[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:]"
- "-[LearnedFusionProcessor runLearnedDemosaicNetworkStage]"
- "checkNetworkStatusWithLabel:statusGroup:status:"
- "runDemosaicWithInputRawTexture:outputRgbTexture:"
- "runLearnedDemosaicNetworkStage"
- "runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:"
- "runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:"

```

## ISPKit

> `/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`

```diff

-20.104.4.0.0
-  __TEXT.__text: 0x2230c
-  __TEXT.__objc_methlist: 0x23fc
-  __TEXT.__const: 0x2b8
+20.105.6.0.0
+  __TEXT.__text: 0x22cc4
+  __TEXT.__objc_methlist: 0x2444
+  __TEXT.__const: 0x2d0
   __TEXT.__gcc_except_tab: 0x95c
-  __TEXT.__cstring: 0x1dfe
-  __TEXT.__oslogstring: 0x3085
+  __TEXT.__cstring: 0x1edf
+  __TEXT.__oslogstring: 0x3244
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__unwind_info: 0xbc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1458
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x1468
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x210
   __AUTH_CONST.__const: 0x68
-  __AUTH_CONST.__cfstring: 0x1c00
-  __AUTH_CONST.__objc_const: 0x7b08
+  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__objc_const: 0x7c68
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x688
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x69c
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x1040
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1039
-  Symbols:   2333
-  CStrings:  617
+  Functions: 1035
+  Symbols:   2352
+  CStrings:  625
 
Symbols:
+ -[CondFillZoomMapEncoder .cxx_destruct]
+ -[CondFillZoomMapEncoder computePipelineState]
+ -[CondFillZoomMapEncoder encodeToCommandBuffer:targetTexture:globalSumBackgroundMean:primaryValue:fallbackValue:flowMeanThreshold:personMaskSumThreshold:]
+ -[CondFillZoomMapEncoder initWithDevice:]
+ -[HybridWarper computeFlowStatsCPU:personMask:inputValidRect:personMaskValueThreshold:homography:outFlowBackgroundMean:outFlowMean:]
+ -[LLVUserDefaults tripodNetworkTuningEnable]
+ _LLVTuningKey_HybridWarper_ZoomMapFallbackToNonTripodFlowMeanThresholdLUT
+ _LLVTuningKey_NetworkOutputsModulation_DenoisedBlendingFactorLUT
+ _LLVTuningKey_NetworkOutputsModulation_DenoisedBlendingFactorOnTripodLUT
+ _LLVTuningKey_NetworkOutputsModulation_HistoryBlendingFactorLUT
+ _LLVTuningKey_NetworkOutputsModulation_HistoryBlendingFactorOnTripodLUT
+ _OBJC_CLASS_$_CondFillZoomMapEncoder
+ _OBJC_IVAR_$_CondFillZoomMapEncoder._computePipelineState
+ _OBJC_IVAR_$_CondFillZoomMapEncoder._device
+ _OBJC_IVAR_$_CondFillZoomMapEncoder._logger
+ _OBJC_IVAR_$_LLVProcessorIBP._condFillZoomMapEncoder
+ _OBJC_IVAR_$_LLVUserDefaults._tripodNetworkTuningEnable
+ _OBJC_METACLASS_$_CondFillZoomMapEncoder
+ __OBJC_$_INSTANCE_METHODS_CondFillZoomMapEncoder
+ __OBJC_$_INSTANCE_VARIABLES_CondFillZoomMapEncoder
+ __OBJC_$_PROP_LIST_CondFillZoomMapEncoder
+ __OBJC_CLASS_RO_$_CondFillZoomMapEncoder
+ __OBJC_METACLASS_RO_$_CondFillZoomMapEncoder
+ _objc_msgSend$computeFlowStatsCPU:personMask:inputValidRect:personMaskValueThreshold:homography:outFlowBackgroundMean:outFlowMean:
+ _objc_msgSend$encodeToCommandBuffer:targetTexture:globalSumBackgroundMean:primaryValue:fallbackValue:flowMeanThreshold:personMaskSumThreshold:
+ _objc_msgSend$tripodNetworkTuningEnable
- -[HybridWarper computeFlowBackgroundMeanCPU:personMask:inputValidRect:personMaskValueThreshold:homography:]
- _LLVTuningKey_NetworkOutputsModulation_DenoisedBlendingFactor
- _LLVTuningKey_NetworkOutputsModulation_HistoryBlendingFactor
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _objc_msgSend$computeFlowBackgroundMeanCPU:personMask:inputValidRect:personMaskValueThreshold:homography:
CStrings:
+ "B!"
+ "CPU: personMaskGlobalSum=%f, flowBackgroundMean=%f, flowMean=%f"
+ "CPU: personMaskSum=%f vs threshold=%f, flowMean=%f vs threshold=%f -> %s (dnr=%f, fusion=%f)"
+ "DEBUG: CPU flow stats: flowBackgroundMean=%f (bg count=%f), flowMean=%f (total count=%f), personMaskValueThreshold=%f"
+ "DenoisedBlendingFactorLUT"
+ "DenoisedBlendingFactorOnTripodLUT"
+ "Failed to create Metal function 'LLV::cond_fill_zoom_map'"
+ "Failed to create compute pipeline state for cond_fill_zoom_map: %@"
+ "Failed to initialize CondFillZoomMapEncoder"
+ "Frame %u: totalGain=%.4f (inputAGC=%u inputIspDGain=%u inputSensorDGain=%u)"
+ "Frame %u: zoomFactor=%.4f mode=%{public}s tripodDetected=%{BOOL}d tripodNetworkTuning=%{BOOL}d dnrZoom primary=%.4f fallback=%.4f fusionZoom primary=%.4f fallback=%.4f (dnr scale/offset primary=%.4f/%.4f fallback=%.4f/%.4f, fusion scale/offset primary=%.4f/%.4f fallback=%.4f/%.4f)"
+ "GPU: personMaskGlobalSum=%f, flowBackgroundMean=%f, flowMean=%f"
+ "HistoryBlendingFactorLUT"
+ "HistoryBlendingFactorOnTripodLUT"
+ "ISPKit.LLVTripodNetworkTuningEnable"
+ "LLV::cond_fill_zoom_map"
+ "ZoomMapFallbackToNonTripodFlowMeanThresholdLUT"
+ "clearHistory"
+ "cond_fill_zoom_map: nil argument"
+ "fallback"
+ "primary"
+ "regular"
+ "tripod"
- "  - Background pixel count: %f"
- "  - Flow background mean: %f"
- "  - Flow bytes per row: %lu"
- "  - Flow diff sum: %f"
- "  - Flow dimensions: %lux%lu"
- "  - personMaskValueThreshold: %f"
- "2!"
- "CPU: personMaskGlobalSum=%f, flowBackgroundMean=%f"
- "DEBUG: CPU flow background mean computation:"
- "DEBUG: Reading ANST mask texture data..."
- "DEBUG: Reading optical flow texture data..."
- "DEBUG: Successfully read ANST mask texture data"
- "DenoisedBlendingFactor"
- "GPU: personMaskGlobalSum=%f, flowBackgroundMean=%f"
- "HistoryBlendingFactor"
```

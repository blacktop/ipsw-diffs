## ISPKit

> `/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-20.55.3.0.0
-  __TEXT.__text: 0x200f8
-  __TEXT.__objc_methlist: 0x1fac
-  __TEXT.__const: 0x280
+20.57.3.0.0
+  __TEXT.__text: 0x2068c
+  __TEXT.__objc_methlist: 0x21ec
+  __TEXT.__const: 0x298
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__cstring: 0x1764
-  __TEXT.__oslogstring: 0x2f60
+  __TEXT.__cstring: 0x17b1
+  __TEXT.__oslogstring: 0x2fc3
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__unwind_info: 0x668
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a8
+  __DATA_CONST.__objc_selrefs: 0x1328
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x30
-  __AUTH_CONST.__cfstring: 0x16a0
-  __AUTH_CONST.__objc_const: 0x6fb8
+  __AUTH_CONST.__cfstring: 0x1740
+  __AUTH_CONST.__objc_const: 0x7438
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x5bc
+  __DATA.__objc_ivar: 0x61c
   __DATA.__data: 0x180
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x1040

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 942
-  Symbols:   2092
-  CStrings:  546
+  Functions: 993
+  Symbols:   2171
+  CStrings:  553
 
Symbols:
+ -[FrameOutCombinedEncoder encodeToCommandBuffer:inputDenoisedYUV:degammaLUT:gammaLUT:lscGainGrid:outputBand0Y:outputBand1R:outputBand1GB:outputBand1GBBytesPerRow:shaderModelInfo:lscCropParams:inputCropParams:ditherSeed:ditherStrength:artifactThreshold:uvMaskParams:]
+ -[LLVPostProcessorFrameParameters inputAWBCombBGain]
+ -[LLVPostProcessorFrameParameters inputAWBCombGGain]
+ -[LLVPostProcessorFrameParameters inputAWBCombRGain]
+ -[LLVPostProcessorFrameParameters inputAWBGrayWorldBGain]
+ -[LLVPostProcessorFrameParameters inputAWBGrayWorldGGain]
+ -[LLVPostProcessorFrameParameters inputAWBGrayWorldRGain]
+ -[LLVPostProcessorFrameParameters inputAWBLocked]
+ -[LLVPostProcessorFrameParameters inputAWBStable]
+ -[LLVPostProcessorFrameParameters setInputAWBCombBGain:]
+ -[LLVPostProcessorFrameParameters setInputAWBCombGGain:]
+ -[LLVPostProcessorFrameParameters setInputAWBCombRGain:]
+ -[LLVPostProcessorFrameParameters setInputAWBGrayWorldBGain:]
+ -[LLVPostProcessorFrameParameters setInputAWBGrayWorldGGain:]
+ -[LLVPostProcessorFrameParameters setInputAWBGrayWorldRGain:]
+ -[LLVPostProcessorFrameParameters setInputAWBLocked:]
+ -[LLVPostProcessorFrameParameters setInputAWBStable:]
+ -[LLVPreProcessorFrameParameters inputAWBCombBGain]
+ -[LLVPreProcessorFrameParameters inputAWBCombGGain]
+ -[LLVPreProcessorFrameParameters inputAWBCombRGain]
+ -[LLVPreProcessorFrameParameters inputAWBGrayWorldBGain]
+ -[LLVPreProcessorFrameParameters inputAWBGrayWorldGGain]
+ -[LLVPreProcessorFrameParameters inputAWBGrayWorldRGain]
+ -[LLVPreProcessorFrameParameters inputAWBLocked]
+ -[LLVPreProcessorFrameParameters inputAWBStable]
+ -[LLVPreProcessorFrameParameters setInputAWBCombBGain:]
+ -[LLVPreProcessorFrameParameters setInputAWBCombGGain:]
+ -[LLVPreProcessorFrameParameters setInputAWBCombRGain:]
+ -[LLVPreProcessorFrameParameters setInputAWBGrayWorldBGain:]
+ -[LLVPreProcessorFrameParameters setInputAWBGrayWorldGGain:]
+ -[LLVPreProcessorFrameParameters setInputAWBGrayWorldRGain:]
+ -[LLVPreProcessorFrameParameters setInputAWBLocked:]
+ -[LLVPreProcessorFrameParameters setInputAWBStable:]
+ -[LLVProcessorFrameParameters inputAWBCombBGain]
+ -[LLVProcessorFrameParameters inputAWBCombGGain]
+ -[LLVProcessorFrameParameters inputAWBCombRGain]
+ -[LLVProcessorFrameParameters inputAWBGrayWorldBGain]
+ -[LLVProcessorFrameParameters inputAWBGrayWorldGGain]
+ -[LLVProcessorFrameParameters inputAWBGrayWorldRGain]
+ -[LLVProcessorFrameParameters inputAWBLocked]
+ -[LLVProcessorFrameParameters inputAWBStable]
+ -[LLVProcessorFrameParameters setInputAWBCombBGain:]
+ -[LLVProcessorFrameParameters setInputAWBCombGGain:]
+ -[LLVProcessorFrameParameters setInputAWBCombRGain:]
+ -[LLVProcessorFrameParameters setInputAWBGrayWorldBGain:]
+ -[LLVProcessorFrameParameters setInputAWBGrayWorldGGain:]
+ -[LLVProcessorFrameParameters setInputAWBGrayWorldRGain:]
+ -[LLVProcessorFrameParameters setInputAWBLocked:]
+ -[LLVProcessorFrameParameters setInputAWBStable:]
+ _LLVTuningGroupName_FrameOutFilter
+ _LLVTuningKey_FrameOutFilter_BilateralThresholdLUT
+ _LLVTuningKey_FrameOutFilter_UVApplyRects
+ _LLVTuningKey_FrameOutFilter_UVBypassRects
+ _LLVTuningKey_FrameOutFilter_UVTransition
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBCombBGain
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBCombGGain
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBCombRGain
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBGrayWorldBGain
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBGrayWorldGGain
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBGrayWorldRGain
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBLocked
+ _OBJC_IVAR_$_LLVPostProcessorFrameParameters._inputAWBStable
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBCombBGain
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBCombGGain
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBCombRGain
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBGrayWorldBGain
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBGrayWorldGGain
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBGrayWorldRGain
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBLocked
+ _OBJC_IVAR_$_LLVPreProcessorFrameParameters._inputAWBStable
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBCombBGain
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBCombGGain
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBCombRGain
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBGrayWorldBGain
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBGrayWorldGGain
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBGrayWorldRGain
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBLocked
+ _OBJC_IVAR_$_LLVProcessorFrameParameters._inputAWBStable
+ __parseUVRects
+ _e5rt_precompiled_compute_op_create_options_set_anef_intermediate_buffer_size_hint
+ _objc_msgSend$encodeToCommandBuffer:inputDenoisedYUV:degammaLUT:gammaLUT:lscGainGrid:outputBand0Y:outputBand1R:outputBand1GB:outputBand1GBBytesPerRow:shaderModelInfo:lscCropParams:inputCropParams:ditherSeed:ditherStrength:artifactThreshold:uvMaskParams:
- -[FrameOutCombinedEncoder encodeToCommandBuffer:inputDenoisedYUV:degammaLUT:gammaLUT:lscGainGrid:outputBand0Y:outputBand1R:outputBand1GB:outputBand1GBBytesPerRow:shaderModelInfo:lscCropParams:inputCropParams:ditherSeed:ditherStrength:]
- _objc_msgSend$encodeToCommandBuffer:inputDenoisedYUV:degammaLUT:gammaLUT:lscGainGrid:outputBand0Y:outputBand1R:outputBand1GB:outputBand1GBBytesPerRow:shaderModelInfo:lscCropParams:inputCropParams:ditherSeed:ditherStrength:
CStrings:
+ "ArtifactThreshold = %f (totalGain = %f)"
+ "BilateralThresholdLUT"
+ "FrameOutFilter"
+ "Options set anef intermediate buffer size hint hint failed"
+ "UVApplyRects"
+ "UVBypassRects"
+ "UVTransition"
+ "\x92"
+ "\xa1"
- "R"
- "\x81"
```

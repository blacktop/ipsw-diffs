## STF

> `/System/Library/VideoProcessors/STF.bundle/STF`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x1012b0
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x1654
-  __TEXT.__const: 0x540
-  __TEXT.__cstring: 0x4084
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0xe30
+650.0.0.122.4
+  __TEXT.__text: 0x106fb0
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_methlist: 0x16b4
+  __TEXT.__const: 0x5c0
+  __TEXT.__oslogstring: 0x1b45
+  __TEXT.__cstring: 0x85e6
+  __TEXT.__gcc_except_tab: 0x24c
+  __TEXT.__unwind_info: 0xe50
   __TEXT.__eh_frame: 0xb38
   __TEXT.__objc_classname: 0x254
-  __TEXT.__objc_methname: 0x4809
-  __TEXT.__objc_methtype: 0x10a9
-  __TEXT.__objc_stubs: 0x25c0
-  __DATA_CONST.__got: 0x148
+  __TEXT.__objc_methname: 0x49c3
+  __TEXT.__objc_methtype: 0x10d4
+  __TEXT.__objc_stubs: 0x2700
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc60
+  __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x388
   __AUTH_CONST.__cfstring: 0x1100
-  __AUTH_CONST.__objc_const: 0x3ba0
+  __AUTH_CONST.__objc_const: 0x3c80
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x434
+  __DATA.__objc_ivar: 0x448
   __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2950F57B-B0CD-325C-BC4C-92442D421F38
-  Functions: 1980
-  Symbols:   4986
-  CStrings:  1784
+  UUID: 529A86DC-CD15-3E38-B23D-31B27C4AB885
+  Functions: 2009
+  Symbols:   5116
+  CStrings:  2307
 
Symbols:
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:]
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.1
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.2
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.3
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.4
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.5
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.6
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.7
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.8
+ -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:].cold.9
+ -[STFRingData bufferToGridHeightRatio]
+ -[STFRingData bufferToGridWidthRatio]
+ -[STFRingData gridOffsetX]
+ -[STFRingData gridOffsetY]
+ -[STFRingData setBufferToGridHeightRatio:]
+ -[STFRingData setBufferToGridWidthRatio:]
+ -[STFRingData setGridOffsetX:]
+ -[STFRingData setGridOffsetY:]
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:]
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.1
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.10
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.11
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.12
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.13
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.14
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.15
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.2
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.3
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.4
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.5
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.6
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.7
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.8
+ -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:].cold.9
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ _OBJC_IVAR_$_STFRingData._bufferToGridHeightRatio
+ _OBJC_IVAR_$_STFRingData._bufferToGridWidthRatio
+ _OBJC_IVAR_$_STFRingData._gridOffsetX
+ _OBJC_IVAR_$_STFRingData._gridOffsetY
+ _OBJC_IVAR_$_STFVideoProcessorV1._temporalThumbnailScale
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __ZL10ger_packedI6VectorIfLl4EE8ScaleOneEvllPKNT_6ScalarES6_lT0_PS4_l
+ __ZL15ger_packed_longI6VectorIfLl4EE8ScaleOneEvllPKNT_6ScalarES6_lT0_PS4_l
+ __ZL15ger_packed_longI6VectorIfLl4EE9ScaleZeroEvllPKNT_6ScalarES6_lT0_PS4_l
+ __ZL15ger_packed_longI6VectorIfLl4EEfEvllPKNT_6ScalarES5_lT0_PS3_l
+ __ZN3fem5utils9string_eqEPKcmS2_m
+ __ZN6lapack9reference6sgetf2ERKiS2_N3fem7arr_refIfLm2EEES2_NS4_IiLm1EEERi
+ __ZN6lapack9reference6sgetrfERKiS2_N3fem7arr_refIfLm2EEES2_NS4_IiLm1EEERi
+ __ZN6lapack9reference6slaswpERKiN3fem7arr_refIfLm2EEES2_S2_S2_NS3_8arr_crefIiLm1EEES2_
+ __ZN6lapack9reference7sgetrf2ERKiS2_N3fem7arr_refIfLm2EEES2_NS4_IiLm1EEERi
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _kFigCaptureStreamLTMThumbnailKey_Format
+ _kFigCaptureStreamMetadataOutputKey_LTMThumbnail
+ _kFigCaptureStreamMetadata_RawSensorHeight
+ _kFigCaptureStreamMetadata_RawSensorWidth
+ _kFigCaptureStreamMetadata_SensorRawValidBufferRect
+ _objc_msgSend$bufferToGridHeightRatio
+ _objc_msgSend$bufferToGridWidthRatio
+ _objc_msgSend$compressionLevel
+ _objc_msgSend$encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:
+ _objc_msgSend$getErrorMessage:
+ _objc_msgSend$gridOffsetX
+ _objc_msgSend$gridOffsetY
+ _objc_msgSend$prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:
+ _objc_msgSend$setBufferToGridHeightRatio:
+ _objc_msgSend$setBufferToGridWidthRatio:
+ _objc_msgSend$setGridOffsetX:
+ _objc_msgSend$setGridOffsetY:
- -[STFLtmFrameProcessorV1 getTightlyPackedISPLTCs:].cold.3
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:]
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.1
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.2
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.3
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.4
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.5
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.6
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.7
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.8
- -[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:].cold.9
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:]
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.1
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.10
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.11
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.12
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.13
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.14
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.15
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.2
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.3
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.4
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.5
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.6
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.7
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.8
- -[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:].cold.9
- -[STFVideoProcessorV1 bufferFrame:].cold.26
- _FigSignalErrorAt
- __ZN6lapack9reference7sgetf2_ERKiS2_N3fem7arr_refIfLm2EEES2_NS4_IiLm1EEERi
- __ZN6lapack9reference7sgetrf_ERKiS2_N3fem7arr_refIfLm2EEES2_NS4_IiLm1EEERi
- __ZN6lapack9reference7slaswp_ERKiN3fem7arr_refIfLm2EEES2_S2_S2_NS3_8arr_crefIiLm1EEES2_
- __ZN6lapack9reference8sgetrf2_ERKiS2_N3fem7arr_refIfLm2EEES2_NS4_IiLm1EEERi
- _exp
- _fig_log_get_emitter
- _kFigCaptureStreamPreLTMThumbnailKey_Format
- _objc_msgSend$encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:
- _objc_msgSend$prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:
- _strmm_noPack_LLNN
- _strmm_noPack_LLNU
- _strmm_noPack_LLTN
- _strmm_noPack_LLTU
- _strmm_noPack_LUNN
- _strmm_noPack_LUNU
- _strmm_noPack_LUTN
- _strmm_noPack_LUTU
- _strmm_noPack_RLNN
- _strmm_noPack_RLNU
- _strmm_noPack_RLTN
- _strmm_noPack_RLTU
- _strmm_noPack_RUNN
- _strmm_noPack_RUNU
- _strmm_noPack_RUTN
- _strmm_noPack_RUTU
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "(Fig)"
+ "+[MetaDataUtilities extractRGBThumbnailFrom:width:height:numberOfThumbnails:redChannelIndex:greenChannelIndex:blueChannelIndex:]"
+ "+[MetaDataUtilities extractRGBThumbnailFrom:width:height:numberOfThumbnails:redChannelIndex:greenChannelIndex:blueChannelIndex:validRect:]"
+ "+[MetaDataUtilities getRGBThumbnailFromLTMThumbnailData:]"
+ "+[MetaDataUtilities getRGBThumbnailFromLTMThumbnailPixelBuffer:]"
+ "+[STFLinearAlgebra prewarm:nWeights:nPoly:]"
+ "+[STFLtc populateLTCTextureData:LTCData:commandBuffer:]"
+ "-[FastBlur _createShaders]"
+ "-[FastBlur _encodeFastBlurHorzFir:inputTex:outputTex:]"
+ "-[FastBlur _encodeFastBlurVertFir:inputTex:outputTex:]"
+ "-[FastBlur allocateResources]"
+ "-[FastBlur prepareToProcess:]"
+ "-[FastBlur processWithCmdBuf:inputTex:outputTex:]"
+ "-[JointBilateralFilters _createShaders]"
+ "-[JointBilateralFilters _encodeSTFJointBilateralFilterPlane:guideTex:inputTex:outputTex:tmpTexArr:jbfToNormalScale:levelsCount:]"
+ "-[JointBilateralFilters _encodeScaleRef:inputTex:outputTex:pixelsMultiplier:]"
+ "-[JointBilateralFilters _encodeSpatialPass:guideTex:inputTex:tmpTexArr:outputTex:pstate:posIdx:level:levelsCount:set:]"
+ "-[JointBilateralFilters allocateResources]"
+ "-[JointBilateralFilters encodeSTFJointBilateralFilterWithFIRBlur:refTex:inputTexArr:outputTexArr:params:]"
+ "-[JointBilateralFilters initWithMetalContext:]"
+ "-[NormalizeWeights _createShaders]"
+ "-[NormalizeWeights allocateResources]"
+ "-[NormalizeWeights encodeNormaliseWeightPlanes:ioTexArr:nWeights:nIter:]"
+ "-[QuantileSplit _createShaders]"
+ "-[QuantileSplit allocateResources]"
+ "-[QuantileSplit encodeQuantileSplitLog:referenceTex:perturbedTex:inputParametersBuffer:outputTextureArray:numberOfPlanes:quantileSdevDiv:]"
+ "-[STFLinearAlgebra ADMM:lhs:rhs:result:maxSolution2Norm:]"
+ "-[STFLinearAlgebra _allocateMemory:commandBuffer:]"
+ "-[STFLinearAlgebra _checkSolution2Norm:LHS:RHS:maximum:]"
+ "-[STFLinsys _allocateSharedBuffers]"
+ "-[STFLinsys encodeLinsys:thumInTex:thumOutTex:wtsTexArr:ltcTex:coeffs:stfParams:converged:]"
+ "-[STFLinsys encodeLinsys:thumInTex:thumOutTex:wtsTexArr:ltcTex:coeffs:stfParams:converged:]_block_invoke"
+ "-[STFLinsys initWithMetalContext:]"
+ "-[STFLinsys setPipelineStates]"
+ "-[STFLtmFrameProcessorV1 allocate2DTextureWithLabel:pixelFormat:texWidth:texHeight:compressionLevel:]"
+ "-[STFLtmFrameProcessorV1 allocate3DTextureWithLabel:pixelFormat:texWidth:texHeight:texDepth:compressionLevel:]"
+ "-[STFLtmFrameProcessorV1 computeBinned8BitsMonochromeThumbnail:width:height:binnedThumbnail:]"
+ "-[STFLtmFrameProcessorV1 computeTCRMaskFromRGBThumbnail:width:height:mask:]"
+ "-[STFLtmFrameProcessorV1 createIdentityCorrectionTexture:pts:]"
+ "-[STFLtmFrameProcessorV1 getTightlyPackedISPLTCs:]"
+ "-[STFLtmFrameProcessorV1 initWithMetalContext:]"
+ "-[STFLtmFrameProcessorV1 prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:]"
+ "-[STFLtmFrameProcessorV1 prewarmShaders:withTuningParameters:]"
+ "-[STFLtmFrameProcessorV1 processingFrame:updatedLTCs:]"
+ "-[STFLtmFrameProcessorV1 processingFrameWithTCR:inputSbuf:HITHThumbnail:tcrMode:updatedLTCs:]"
+ "-[STFLtmFrameProcessorV1 releaseResources]"
+ "-[STFLtmFrameProcessorV1 temporalStabilization:stabilisedLtcs:stabilizationMode:]"
+ "-[STFMakeweightsLtmLog _createShaders]"
+ "-[STFMakeweightsLtmLog _encodeLog:inputTex:outputTex:]"
+ "-[STFMakeweightsLtmLog _encodeMakeWeightsLtmLogCmn:refTex:outputTexArr:params:]"
+ "-[STFMakeweightsLtmLog _encodeMeanLogRgb:inpTex:outTex:]"
+ "-[STFMakeweightsLtmLog _encodePerturbedImage:guideTex:perturbedTex:]"
+ "-[STFMakeweightsLtmLog _encodeRGBAToR:inputTex:outputTex:]"
+ "-[STFMakeweightsLtmLog _encodeRToRGBA:inputTex:outputTex:]"
+ "-[STFMakeweightsLtmLog allocateResources]"
+ "-[STFMakeweightsLtmLog blur2DWithCmdBuffer:inputTexture:outputTexture:blurSize:]"
+ "-[STFMakeweightsLtmLog encodeMakeweightsLtmLogSmooth:inputThumbnail:outputTexArr:np:]"
+ "-[STFMakeweightsLtmLog encodeMakeweightsLtmLogSmoothRGB:inpputRGBAThumbnail:outputTexArr:referenceImageGenerationType:np:]"
+ "-[STFMakeweightsLtmLog encodeRenormaliseMakeweights:weightPlaneArr:sumWeightPlane:numWeights:]"
+ "-[STFMakeweightsLtmLog initWithMetalContext:]"
+ "-[STFReintegration _encodeBlendLTCsWithCmdBuf:in0:in1:in2:outputTex:]"
+ "-[STFReintegration _encodeBlur2DWithCmdBuf:inputTexture:outputTexture:blurSize:]"
+ "-[STFReintegration _encodeBlurLTCsWithCmdBuf:inputTexture:outputTexture:blurSize:]"
+ "-[STFReintegration _encodeGenerateFusionWeightsWithCmdBuf:skymap:ltcFusionWeights:outLtcFusionWeightsLow:outLtcFusionWeightsMid:outLtcFusionWeightsHigh:]"
+ "-[STFReintegration _encodeGenerateMediumContrastMaskWithCmdBuf:inputLuma:outputMask:]"
+ "-[STFReintegration _encodeMixLTCsWithCmdBuf:in0:in1:weights:outputTex:]"
+ "-[STFReintegration _encodePreprocessLTCsWithCmdBuf:thumbnail:skymap:stfLTCs:originalISPLTCs:tcrLTCs:ltmRoi:outputLTCs:]"
+ "-[STFReintegration _encodeScaleValues:inputTex:outputTex:scale:]"
+ "-[STFReintegration _encodeSplitAndBlendLTCsWithCmdBuf:skymap:stfLTCs:originalISPLTCs:tcrLTCs:ltmRoi:weightsLow:weightsMid:weightsHigh:outLTCs:]"
+ "-[STFReintegration _encodeSubtractLTCsWithCmdBuf:inLTCs0:inLTCs1:outLTCs:]"
+ "-[STFReintegration _encodeUpsampleAndMergeLTCsWithCmdBuf:skymap:inLTCs0:inLTCs1:outLTCs:ltmRoi:]"
+ "-[STFReintegration encodeLTCLTMReintegrationSkyVideo1:lumaThumbnail:weights:numberOfWeights:coefficients:basisLTCs:originalISPLTCs:spatialGainCurveLUT:fusedSpatialGainCurveLUT:]"
+ "-[STFReintegration encodeLTCLTMReintegrationWithCmdBuf:inputLuma:inputChroma:lumaThumbnail:rgbThumbnail:weights:numberOfWeights:coefficients:basisLTCs:originalISPLTCs:tcrLTCs:foregroundLTCs:ltmRoi:skymask:personMask:gtcRatio:gtcFinal:highlightCompression:outputLumaGain:outputChroma:outputLTCs:outputPsnr:lumaHistogram:colorCorrection:spatialCCM:ccmRoi:linSysConverged:isLinear:exposureBiasFactor:scaleInput:chromaGainAdjPower:chromaBias:inputLumaPedestal:ltmHardGain:utmForegroundFactor:utmBackgroundFactor:hazeCorrection:]"
+ "-[STFReintegration initWithMetalContext:settings:]"
+ "-[STFRingBuffer add:]"
+ "-[STFRingBuffer getFramesDataWindow:]"
+ "-[STFRingBuffer initWithCapacity:historySize:]"
+ "-[STFRingBuffer releaseResources]"
+ "-[STFRingBuffer reset]"
+ "-[STFStillProcessorV1 _setupAllocator:label:externalMemoryResource:]"
+ "-[STFStillProcessorV1 extractSettings:]"
+ "-[STFStillProcessorV1 fillSettings]"
+ "-[STFStillProcessorV1 getCorrectionStrength]"
+ "-[STFStillProcessorV1 initializeStfBlocks]"
+ "-[STFStillProcessorV1 prepareToProcess:]"
+ "-[STFStillProcessorV1 prewarm]"
+ "-[STFStillProcessorV1 process]"
+ "-[STFStillProcessorV1 purgeResources]"
+ "-[STFStillProcessorV1 setup]"
+ "-[STFTemporalStabilization allocateTextures:thumbnailHeight:filterLength:]"
+ "-[STFTemporalStabilization compileShaders]"
+ "-[STFTemporalStabilization encodeIdentityCorrectionTexture:stabilisedLtcs:analyticsBuffer:pts:]"
+ "-[STFTemporalStabilization encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:]"
+ "-[STFTemporalStabilization initWithMetalContext:]"
+ "-[STFTemporalStabilization purgeResources]"
+ "-[STFThumbnailPreprocessor encodeApplyLTCWithCmdBuf:inpIspLumaTex:ltcTex:ltmRoi:outISPLTMTex:]"
+ "-[STFThumbnailPreprocessor encodeCalculateAndAddGlobalOffset:inputTexture:outputTexture:]"
+ "-[STFThumbnailPreprocessor encodeDownSampleRGBToISPLuma:inRgbTex:outISPLumaTex:outRGBTex:isLinear:]"
+ "-[STFThumbnailPreprocessor encodeDownsampleSkymaskWithCmdBuf:inputSkymask:outputSkymaskThumbnail:]"
+ "-[STFThumbnailPreprocessor encodeDownsampleToISPLumaWithCmdBuf:inpTexY:inpTexCbCr:colorCorrection:spatialCCMTex:ccmRoi:outISPLumaTex:outRGBTex:isLinear:exposureBiasFactor:scaleInput:chromaBias:inputLumaPedestal:ltmHardGain:highlightCompression:hazeCorrection:]"
+ "-[STFThumbnailPreprocessor encodeRgbToLuma:inpTexRGBA:outTexLuma:]"
+ "-[STFThumbnailPreprocessor encodeZeroTextureWithCmdBuf:texture:]"
+ "-[STFThumbnailPreprocessor initWithMetalContext:]"
+ "-[STFThumbnailPreprocessor initWithMetalContext:settings:]"
+ "-[STFVideoProcessorV1 bufferFrame:]"
+ "-[STFVideoProcessorV1 computeLTCsCorrection:forPTS:shouldShutdown:skipFrame:]"
+ "-[STFVideoProcessorV1 getAnalyticsData:]"
+ "-[STFVideoProcessorV1 initWithRingBufferSize:historySize:cmdQueue:]"
+ "-[STFVideoProcessorV1 prepareToProcessWithMetadata:]"
+ "-[STFVideoProcessorV1 prewarmWithTuningParameters:]"
+ "-[STFVideoProcessorV1 setTcrExtraMaskStrength:]"
+ "-[STFVideoProcessorV1 setTcrGlobalStrength:]"
+ "-[STFVideoProcessorV1 setTcrSkyMaskStrength:]"
+ "-[STFVideoProcessorV1 setTemporalWindowTimeDefault:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Encountered unsupported value (%d) for FigCaptureLTMLookUpTables.v1.lutsCurveEntryCount"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Encountered unsupported value (%d) for FigCaptureLTMLookUpTables.v2.lutsCurveEntryCount"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Support for FigCaptureLTMLookUpTables V%d struct not yet implemented"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Tried to get LTM curves pointer from CCM struct"
+ "< STF : MKW >"
+ "<<<< STF >>>>"
+ "<<<< STF >>>> %s: (valid rect present = %d) buffer size = %zu x %zu, validBufferRect = %f, %f, %f x %f"
+ "<<<< STF >>>> %s: Coudn't initialise STFLtmFrameProcessorV1"
+ "<<<< STF >>>> %s: Couldn't getFramesDataWindow not enough data in the ring buffer."
+ "<<<< STF >>>> %s: Couldn't initialize STFVideoProcessorV1"
+ "<<<< STF >>>> %s: Couldn't initialize StfRingBuffer. Capacity smaller then output window."
+ "<<<< STF >>>> %s: Couldn't initialize StfRingBuffer. Capacity too big."
+ "<<<< STF >>>> %s: Couldn't initialize StfRingBuffer. Memory full."
+ "<<<< STF >>>> %s: FigMetalAllocator size is: < %lu >"
+ "<<<< STF >>>> %s: HITH thumbnail doesn't contain blue channel"
+ "<<<< STF >>>> %s: HITH thumbnail doesn't contain green channel"
+ "<<<< STF >>>> %s: HITH thumbnail doesn't contain red channel"
+ "<<<< STF >>>> %s: Initializing FigMetalAllocator with compression level %d"
+ "<<<< STF >>>> %s: Invalid configuration: thumbnail was provided but TCR isn't configured to use it"
+ "<<<< STF >>>> %s: LTM CVIS analytics buffer pointer invalid."
+ "<<<< STF >>>> %s: LTM CVIS analytics data requested for wrong PTS value. Ensure command buffer is finished before calling this method."
+ "<<<< STF >>>> %s: LTMThumbnail has wrong size"
+ "<<<< STF >>>> %s: Missing LTMThumbnail"
+ "<<<< STF >>>> %s: Only ltmLUTs versions 4 and 5 are supported (got:%u)"
+ "<<<< STF >>>> %s: RGBThumbnailData is nil"
+ "<<<< STF >>>> %s: STF: Run STF"
+ "<<<< STF >>>> %s: STF: prepareToprocess for %d"
+ "<<<< STF >>>> %s: STF: prewarm"
+ "<<<< STF >>>> %s: STF: purgeResources"
+ "<<<< STF >>>> %s: STF: stfStrengthGrade = %d"
+ "<<<< STF >>>> %s: STFLtmFrameProcessorV1 reset"
+ "<<<< STF >>>> %s: STFLtmFrameProcessorV1: encoding an identity correction texture"
+ "<<<< STF >>>> %s: STFLtmFrameProcessorV1: temporalStabilization END"
+ "<<<< STF >>>> %s: STFLtmFrameProcessorV1: temporalStabilization START"
+ "<<<< STF >>>> %s: Sensor Switch Backwards with size:%d and currentIndex:%d after adjustment"
+ "<<<< STF >>>> %s: Sensor Switch Detected Backwards at:%d and currentIndex:%d size:%d"
+ "<<<< STF >>>> %s: Sensor Switch Detected Forwards at:%d and currentIndex:%d"
+ "<<<< STF >>>> %s: Sensor Switch Forwards with size:%d and currentIndex:%d after adjustment"
+ "<<<< STF >>>> %s: Undergoing shutdown. Swapping %d updatedLtcs and originalLtcs, with current ratio of ISP LTC's to TCR LTC's:%f"
+ "<<<< STF >>>> %s: Unsupported compression level requested in allocate2DTextureWithLabel."
+ "<<<< STF >>>> %s: Unsupported compression level requested in allocate3DTextureWithLabel."
+ "<<<< STF >>>> %s: Unsupported stabilization mode: %d"
+ "<<<< STF >>>> %s: Unsupported thumbnail size"
+ "<<<< STF >>>> %s: Using external memory resource %p of type %@ "
+ "<<<< STF >>>> %s: Using provided metal command queue %p"
+ "<<<< STF >>>> %s: array count:%d index:%d"
+ "<<<< STF >>>> %s: attachedMedia is nil"
+ "<<<< STF >>>> %s: buffering frame pts: %f"
+ "<<<< STF >>>> %s: combined grid offset = %f, %f,  combined buffer to LTM grid ratio = %f, %f"
+ "<<<< STF >>>> %s: computeLTCsCorrection:forPTS: %f"
+ "<<<< STF >>>> %s: computeLTCsCorrection:forPTS: %f END"
+ "<<<< STF >>>> %s: dealloc %lu items"
+ "<<<< STF >>>> %s: elapsed time:%lld ns"
+ "<<<< STF >>>> %s: fetching analytics data for LTM CVIS"
+ "<<<< STF >>>> %s: inputEIT:%f pEIT:%f"
+ "<<<< STF >>>> %s: inputLTMThumbnailPixelBuffer is nil"
+ "<<<< STF >>>> %s: inputLTMThumbnailSampleBuffer is nil"
+ "<<<< STF >>>> %s: inputPreLTMThumbnail format is incorrect (YlinRGBYavg, RGB, or RGBRGB is expected)"
+ "<<<< STF >>>> %s: inputPreLTMThumbnail format is not available"
+ "<<<< STF >>>> %s: inputPreLTMThumbnail valid buffer rect is not available"
+ "<<<< STF >>>> %s: ltm grid size = %d x %d,  grid offset buffer based = %f, %f,  buffer to grid ratio = %f, %f"
+ "<<<< STF >>>> %s: prewarmWithTuningParameters:"
+ "<<<< STF >>>> %s: processingFrame END"
+ "<<<< STF >>>> %s: processingFrame START"
+ "<<<< STF >>>> %s: processingFrameWithTCR END"
+ "<<<< STF >>>> %s: processingFrameWithTCR START"
+ "<<<< STF >>>> %s: rawSensorSize = %d x %d, sensorRawValidRect = %.0f, %.0f  %.0f x %.0f, grid origin = %d, %d, tile size = %d x %d, correction curves grid to LTM grid size ratio = %d, grid offset v5 = %f, %f, sensor to LTM grid ratio = %f, %f"
+ "<<<< STF >>>> %s: reading ring buffer 2 times"
+ "<<<< STF >>>> %s: sensorID:%X AGC:%.3f ispDGain:%.3f exposureTime:%.0fus hrGainDownRatio:%.3f"
+ "<<<< STF >>>> %s: stfRing reset"
+ "<<<< STF >>>> %s: stfRingBuffer add a data _inputIndex:%d _count:%d distanceOutToIn:%d"
+ "<<<< STF >>>> %s: stfRingBuffer initialized with capacity:%d _historySize:%d"
+ "<<<< STF >>>> %s: storage thermal flag wind down count:%d size:%d indexOfPresent:%d"
+ "<<<< STF >>>> %s: tcrExtraMaskStrength:%f"
+ "<<<< STF >>>> %s: tcrGlobalStrength:%f"
+ "<<<< STF >>>> %s: tcrSkyMaskStrength:%f"
+ "<<<< STF >>>> %s: temporalWindowTimeDefault:%f"
+ "<<<< STFLinearAlgebra >>>>"
+ "<<<< STFLinearAlgebra >>>> %s: %s"
+ "<<<< STFLinearAlgebra >>>> %s: STF: ADMM Succeeded on iteration %d"
+ "<<<< STFLinearAlgebra >>>> %s: STF: CPU linear system solution 2norm: %.3f (maximum allowed: %.3f)"
+ "<<<< STFLinearAlgebra >>>> %s: STF: CPU linear system solver END"
+ "<<<< STFLinearAlgebra >>>> %s: STF: CPU linear system solver START"
+ "<<<< STFLinearAlgebra >>>> %s: STF: CPU linear system solver failed to find a solution. Falling back to original ISP LTCs."
+ "<<<< STFLinearAlgebra >>>> %s: STF: STFLinSys allocateSharedBuffers"
+ "<<<< STFLinearAlgebra >>>> %s: STF: matrixStatusPtr->alphaSolver %.2f"
+ "<<<< STFLinearAlgebra >>>> %s: STF: matrixStatusPtr->extLambda %.2f"
+ "<<<< STFLinearAlgebra >>>> %s: STF: matrixStatusPtr->numWgts %d"
+ "<<<< STFLinearAlgebra >>>> %s: STF: matrixStatusPtr->regLambda %.2f"
+ "<<<< STFLinearAlgebra >>>> %s: STF: matrixStatusPtr->rhoSolver %.2f"
+ "<<<< STFLinearAlgebra >>>> %s: STF: matrixStatusPtr->tikLambda %.2f"
+ "<<<< STFTemporalStabilization >>>>"
+ "<<<< STFTemporalStabilization >>>> %s: STF: STFTemporalStabilisation allocateTextures "
+ "<<<< STFTemporalStabilization >>>> %s: STF: STFTemporalStabilisation encodeTemporalStabilisation"
+ "<<<< STFTemporalStabilization >>>> %s: STF: STFTemporalStabilisation filter type: %d"
+ "<<<< STFTemporalStabilization >>>> %s: STF: STFTemporalStabilisation initWithFigMetalContext "
+ "<<<< STFTemporalStabilization >>>> %s: STF: STFTemporalStabilisation purgeSharedBuffers"
+ "<<<< STFTemporalStabilization >>>> %s: STF: STFTemporalStabilisation setPipelineStates "
+ "Compressed textures not supported"
+ "Couldn't initialize STFVideoProcessorV1. The ringBufferSize must be positive."
+ "External memory resource too low"
+ "Failed to allocate FigMetalAllocatorDescriptor"
+ "FigCFDictionaryGetInt32IfPresent( inputPreLTMThumbnailMetadata, kFigCaptureStreamLTMThumbnailKey_Format, &inputPreLTMThumbnailFormat )"
+ "Height must be > 0"
+ "Height must be a multiple of 2"
+ "Height must be a multiple of 4"
+ "I/O/PRM sizes mismatch"
+ "Incompatible image vs binned image dimensions"
+ "Incompatible thumbnail and mask dimensions"
+ "LTM LUT requested for incorrect PTS."
+ "Metal Texture Cache allocation failed."
+ "NULL array"
+ "NULL samplebuffer"
+ "STF Params input does not conform with the STFStillLtmIBPParams protocol"
+ "STFVideoProcessorV1 couldn't prepare to process - LTCs grid cannot have size 0."
+ "STFVideoProcessorV1 couldn't prepare to process - LTCs in first frame metadata are nil."
+ "STFVideoProcessorV1 couldn't prepare to process - LTCs in first frame metadata are not valid."
+ "STFVideoProcessorV1 couldn't prepare to process - LTMLookUpTables missing from first frame metadata."
+ "STFVideoProcessorV1 couldn't prepare to process - first frame metadata missing."
+ "Tf,N,V_bufferToGridHeightRatio"
+ "Tf,N,V_bufferToGridWidthRatio"
+ "Tf,N,V_gridOffsetX"
+ "Tf,N,V_gridOffsetY"
+ "Thumbnail dimensions don't match"
+ "Unknown procType"
+ "Width must be > 0"
+ "Width must be a multiple of 2"
+ "Width must be a multiple of 4"
+ "_LTCLTMDotSkyPipelineState is NULL"
+ "_LTCLTMReintegAllPipelineState is NULL"
+ "_LTMLTCReintegVideoPipelineState is NULL"
+ "_addGlobalOffsetPipelineState is NULL"
+ "_analyticsBuffer is NULL"
+ "_applyGtcPipelineState is NULL"
+ "_applyGtcReferencePipelineState is NULL"
+ "_applyLTCPipelineState is NULL"
+ "_applyLtcPipelineState is NULL"
+ "_applyTikonovPipelineState is NULL"
+ "_applyTikonovRegularizationPipelineState is NULL"
+ "_blendLTCsPipelineState is NULL"
+ "_blur2DXPipelineState is NULL"
+ "_blur2DYPipelineState is NULL"
+ "_blur2dXPipelineState is NULL"
+ "_blur2dYPipelineState is NULL"
+ "_blurIntermediateTex is NULL"
+ "_blurLTCsPipelineState is NULL"
+ "_blurLTCsUshortPipelineState is NULL"
+ "_bufferToGridHeightRatio"
+ "_bufferToGridWidthRatio"
+ "_buildupRightHandSidePipelineState is NULL"
+ "_calcCorrectionAmountPipelineState is NULL"
+ "_calcNodesGainsPipelineState is NULL"
+ "_calculateGlobalOffsetPipelineState is NULL"
+ "_cnstBuffer allocation failed"
+ "_computeLogPipelineState is NULL"
+ "_computeMeanLogPipelineState is NULL"
+ "_computePerturbationPipelineState is NULL"
+ "_conditionLHSAddLagPipelineState is NULL"
+ "_conditionLHSEndPipelineState is NULL"
+ "_conditionLHSRightPipelineState is NULL"
+ "_correctionGainTexture is NULL"
+ "_correctionNodeTexture is NULL"
+ "_countGreaterThanValuePipelineState is NULL"
+ "_divideWeightsPipelineState is NULL"
+ "_downsampleRGBToISPLumaPipelineState is NULL"
+ "_downsampleSkymapPipelineState is NULL"
+ "_downsampleToISPLumaPipelineState is NULL"
+ "_downsizePipelineState is NULL"
+ "_fastBlur allocation failed"
+ "_fastBlurHorizFIRPipeState is NULL"
+ "_fastBlurVertFIRPipeState is NULL"
+ "_filterBuf is NULL"
+ "_gainAdjustedAccumulationPipelineState is NULL"
+ "_genFusWgtsPipelineState is NULL"
+ "_getLTM_ltmCurveAndCCMEntryCounts"
+ "_gridOffsetX"
+ "_gridOffsetY"
+ "_histLogPipelineState is NULL"
+ "_identityTexturePipelineState is NULL"
+ "_identityTextureUshortPipelineState is NULL"
+ "_inflexionPipelineState is NULL"
+ "_inputEITBuf is NULL"
+ "_inputEITPlaceholder allocation failed."
+ "_interpolate1DcoefsPipelineState is NULL"
+ "_invSumPipelineState is NULL"
+ "_ispLTC allocation failed."
+ "_lhsPipelineState is NULL"
+ "_ltcPreBlurTexture is NULL"
+ "_ltcTextureSmoothedRescaled is NULL"
+ "_ltcTextureUnsmoothedRescaled is NULL"
+ "_ltmVectorizable allocation failed."
+ "_mainMetalContext.metalContext is NULL"
+ "_mainMetalContext.metalContext.allocator is NULL"
+ "_matrixTCondBuf is NULL"
+ "_matrixTregBuf is NULL"
+ "_matrixfBuf is NULL"
+ "_metal is NULL"
+ "_mirrorGlobalMatrixPipelineState is NULL"
+ "_mirrorSubMatrixPipeLineState is NULL"
+ "_mixLTCsPipelineState is NULL"
+ "_mtlBuffer allocation failed"
+ "_mtlCPUPreparedBuffer allocation failed"
+ "_newLTC allocation failed."
+ "_normPlanesPipelineState is NULL"
+ "_obj(s) allocation failed"
+ "_offsetWeightsPipelineState is NULL"
+ "_pEITBuf is NULL"
+ "_pEITPlaceholder allocation failed."
+ "_paramsBuf is NULL"
+ "_permuteLtcsFwToSwPipelineState is NULL"
+ "_perturbedPipelineState is NULL"
+ "_polyExpandInputPipelineState is NULL"
+ "_polyExpandedInput is NULL"
+ "_privateMetalContext.metalContext is NULL"
+ "_privateMetalContext.metalContext.allocator is NULL"
+ "_psnrPipelineState is NULL"
+ "_ptsBuf is NULL"
+ "_rToRgbaPipelineState is NULL"
+ "_randBuffer allocation failed"
+ "_ratioBuf is NULL"
+ "_ratioGainBuf is NULL"
+ "_referenceThumbnailTexturePostGtcISPLuma is NULL"
+ "_referenceThumbnailTexturePostGtcYLuma is NULL"
+ "_referenceThumbnailTexturePostLtc is NULL"
+ "_regGlobal allocation failed."
+ "_regLocal allocation failed."
+ "_regWeight allocation failed."
+ "_rescaleLtcsPipelineState is NULL"
+ "_rgbToLumaPipelineState is NULL"
+ "_rgbaToRPipelineState is NULL"
+ "_rstBufferPipelineState is NULL"
+ "_rstSumPipelineState is NULL"
+ "_saveLtcsTo1DPipelineState is NULL"
+ "_scaleRefPipelineState is NULL"
+ "_scaleValuesPipelineState is NULL"
+ "_setBufferPipelineState is NULL"
+ "_sharedEventListener is NULL"
+ "_spatialPassAt41xPipelineStates.offsetLeft is NULL"
+ "_spatialPassAt41xPipelineStates.offsetRight is NULL"
+ "_spatialPassAt42xPipelineStates.offsetLeft is NULL"
+ "_spatialPassAt42xPipelineStates.offsetRight is NULL"
+ "_spatialPassAt44xPipelineStates.offsetDown is NULL"
+ "_spatialPassAt44xPipelineStates.offsetLeft is NULL"
+ "_spatialPassAt44xPipelineStates.offsetRight is NULL"
+ "_spatialPassAt44xPipelineStates.offsetUp is NULL"
+ "_splitWeightsLogPipelineState is NULL"
+ "_stdDevGatePipelineState is NULL"
+ "_stfLinSys is NULL"
+ "_stfMakeWeightsLtmLog is NULL"
+ "_stfStrengthMetric is NULL"
+ "_strengthCalcPipelineState is NULL"
+ "_subtractPipelineState is NULL"
+ "_sumAboveValPipelineState is NULL"
+ "_sumWeightsPipelineState is NULL"
+ "_targetThumbnailTexturePostGtc is NULL"
+ "_targetThumbnailTexturePostLtc is NULL"
+ "_tcrMask allocation failed."
+ "_tcrMaskDownscaled allocation failed."
+ "_tcrMaxLuma allocation failed."
+ "_temporalStabilization allocation failed."
+ "_temporalThumbnailScale"
+ "_texMinF32PipelineState is NULL"
+ "_texMinMaxF32PipelineState is NULL"
+ "_texSumPipelineState is NULL"
+ "_thumbProc allocation failed."
+ "_upsampleLTCsPipelineState is NULL"
+ "_varsBuffer allocation failed"
+ "_weightsAndKernelParams allocation failed"
+ "_zeroLtcTexturePipelineState is NULL"
+ "_zeroTexturePipelineState is NULL"
+ "analyticBufferDescriptor is NULL"
+ "basisltcTex is NULL"
+ "bd is NULL"
+ "blitEncoder is NULL"
+ "bufferToGridHeightRatio"
+ "bufferToGridWidthRatio"
+ "cmdBuf is NULL"
+ "cmdEnc is NULL"
+ "coeffs is NULL"
+ "compressionLevel"
+ "convergedPtr is NULL"
+ "currentTuningKey is NULL"
+ "dataBuffer is NULL"
+ "defaultGlobalMaskOffset is NULL"
+ "desc is NULL"
+ "dotProdMixTexture is NULL"
+ "dotProdTexture is NULL"
+ "encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:gridOffsetX:gridOffsetY:gridRatioX:gridRatioY:alternativeLayout:referenceFrame:filterLength:pts:"
+ "encoder is NULL"
+ "failed to allocate lumaGTCTexture"
+ "failed to allocate originalLTCTexture"
+ "failed to allocate rgbGTCTexture"
+ "failed to allocate rgbThumbnailTexture"
+ "failed to allocate updatedLTCs"
+ "filterBufPtr is NULL"
+ "filterLength <= sizeof(args->ltcIn) / sizeof(args->ltcIn[0]) is NULL"
+ "foregroundLTCsUpsampled is NULL"
+ "frameLtc->version == 4 || frameLtc->version == 5"
+ "getLTM_data"
+ "getLTM_leftPadding"
+ "getLTM_lutsBytesPerColumn"
+ "getLTM_lutsBytesPerRow"
+ "getLTM_topPadding"
+ "getLTM_validHeight"
+ "getLTM_validWidth"
+ "globalMaskOffsetThreshold is NULL"
+ "globalOffset is NULL"
+ "gridOffsetX"
+ "gridOffsetY"
+ "guidePixelMultipliedTex allocation failed"
+ "i148@0:8@16^@24^@32@40@48@56@64@72@80@88@96f104f108f112f116B120Q124Q132d140"
+ "i40@0:8Q16Q24I32I36"
+ "i72@0:8^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})16{_STFTCRPlist=fffffffi}2456@64"
+ "info == 0 is NULL"
+ "info >= 0 is NULL"
+ "inputEITP is NULL"
+ "inputLTMThumbnailPixelBuffer"
+ "inputLTMThumbnailSampleBuffer"
+ "inputThumbRGB is NULL"
+ "inputThumbtextureISPY is NULL"
+ "intermediateBlurTexture is NULL"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "lagrangianBuffer is NULL"
+ "lhsCondPtr is NULL"
+ "lhsPtr is NULL"
+ "linAlg is NULL"
+ "linSysConverged is NULL"
+ "ltcBytes->version == 4 || ltcBytes->version == 5"
+ "ltcFusionContReluGate1High is NULL"
+ "ltcFusionContReluGate1Low is NULL"
+ "ltcFusionContReluGate2High is NULL"
+ "ltcFusionContReluGate2Low is NULL"
+ "ltcFusionContReluOut1High is NULL"
+ "ltcFusionContReluOut1Low is NULL"
+ "ltcFusionContReluOut2High is NULL"
+ "ltcFusionContReluOut2Low is NULL"
+ "ltcFusionHighFreqWeight is NULL"
+ "ltcFusionLowFilterSize is NULL"
+ "ltcFusionLowFreqWeight is NULL"
+ "ltcFusionMaskOffset is NULL"
+ "ltcFusionMidFilterSize is NULL"
+ "ltcFusionMidFreqWeight is NULL"
+ "ltcFusionOtherOffset is NULL"
+ "ltcFusionWeightsHigh is NULL"
+ "ltcFusionWeightsLow is NULL"
+ "ltcFusionWeightsMid is NULL"
+ "ltcsForegroundTexture is NULL"
+ "ltcsRegularizedTexture is NULL"
+ "ltcsTexture is NULL"
+ "ltmLut->version == 4 || ltmLut->version == 5"
+ "matrixBuffer is NULL"
+ "metalContext.commandBuffer is NULL"
+ "midContrastMask is NULL"
+ "midContrastMaskDownsized is NULL"
+ "mp is NULL"
+ "newLtcsHigh is NULL"
+ "newLtcsLow is NULL"
+ "newLtcsLowBlur is NULL"
+ "newLtcsMid is NULL"
+ "newLtcsMidBlur is NULL"
+ "nil downscaled thumbnail"
+ "nil mask"
+ "nil thumbnail"
+ "numChannels"
+ "oldLtcsLow is NULL"
+ "oldLtcsPermuted is NULL"
+ "originalISPLtcsHigh is NULL"
+ "originalISPLtcsLowBlur is NULL"
+ "originalISPLtcsMid is NULL"
+ "originalISPLtcsMidBlur is NULL"
+ "originalISPLtcsUpsampled is NULL"
+ "pEITP is NULL"
+ "paramsBufP is NULL"
+ "perturbedTex is NULL"
+ "pivotBuffer is NULL"
+ "pivotsBuffer is NULL"
+ "prepareToProcessWithThumbnailWidth:thumbnailHeight:temporalThumbnailScale:filterLength:"
+ "processingFrame: frameLtc->version != 4 or 5"
+ "ptsBufPtr is NULL"
+ "ratioBufP is NULL"
+ "ratioGainBufP is NULL"
+ "refGenTp not supported"
+ "refTex allocation failed"
+ "refTex allocation from metal heap failed"
+ "regularizeLocalToneCurves: ltmLut->version != 4 or 5"
+ "resultPtr is NULL"
+ "rgbaTexArr allocation from metal heap failed"
+ "rhsBuffer is NULL"
+ "rhsPtr is NULL"
+ "rndTex is NULL"
+ "self is NULL"
+ "semanticBlurSize is NULL"
+ "serializedSettings is NULL"
+ "setBufferToGridHeightRatio:"
+ "setBufferToGridWidthRatio:"
+ "setGridOffsetX:"
+ "setGridOffsetY:"
+ "settingsSet is NULL"
+ "sgetrfWorkBuffer is NULL"
+ "sgetrfWorkSpaceLength > 0 is NULL"
+ "sharedEvent is NULL"
+ "skyMaskDownsized is NULL"
+ "skyMaskDownsizedOffset is NULL"
+ "skyMaskIntermediate is NULL"
+ "skyMaskTexUNorm is NULL"
+ "stfFunctionConstants is NULL"
+ "stfGainAdjustedAccumulationArgsBuf is NULL"
+ "stfLinsysDispatchQueue is NULL"
+ "stfParams.numWgts > 0 is NULL"
+ "stfReintegration is NULL"
+ "stfThumbnailPreprocessor is NULL"
+ "targetThumbtextureISPY is NULL"
+ "tcrFallbackWeight is NULL"
+ "td is NULL"
+ "texDesc is NULL"
+ "the ring buffer overflow"
+ "thumbProc is NULL"
+ "tmp is NULL"
+ "tmpTexArr[i] allocation failed"
+ "tuningForCaptureType is NULL"
+ "u"
+ "vectorBuffer is NULL"
+ "workSpaceBuffer is NULL"
+ "workSpaceLengthFloat > 0 is NULL"
+ "wtsTexArr[i] is NULL"
- "EXC"
- "FigCFDictionaryGetInt32IfPresent( inputPreLTMThumbnailMetadata, kFigCaptureStreamPreLTMThumbnailKey_Format, &inputPreLTMThumbnailFormat )"
- "GGHD3"
- "GGHRD"
- "HSEQR"
- "encodeTemporalStabilization:ltcTextures:ltcTexturesStf:stabilisedLtcs:gtcRatio:gtcFinal:thumbnailCurrent:thumbnailCurrentLinearRgb:analyticsBuffer:inputEIT:pEIT:alternativeLayout:referenceFrame:filterLength:pts:"
- "frameLtc->version == 4"
- "i132@0:8@16^@24^@32@40@48@56@64@72@80@88@96B104Q108Q116d124"
- "i36@0:8Q16Q24I32"
- "i72@0:8^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})16{_STFTCRPlist=fffffffi}2456@64"
- "inputPreLTMThumbnailFormat == kFigCaptureStreamPreLTMThumbnailFormat_YlinRGBYavg"
- "inputPreLTMThumbnailPixelBuffer"
- "inputPreLTMThumbnailSampleBuffer"
- "ltcBytes->version != 4"
- "ltcBytes->version == 4"
- "ltmLut->version == 4"
- "prepareToProcessWithThumbnailWidth:thumbnailHeight:filterLength:"
- "processingFrame: frameLtc->version != 4"
- "regularizeLocalToneCurves: ltmLut->version != 4"

```

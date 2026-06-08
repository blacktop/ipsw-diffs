## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

-1.55.0.0.0
-  __TEXT.__text: 0x172a0
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x32c
-  __TEXT.__const: 0x3028
-  __TEXT.__oslogstring: 0x3def
-  __TEXT.__cstring: 0x102a
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x8da
-  __TEXT.__objc_methtype: 0x24a9
-  __TEXT.__objc_stubs: 0x5e0
-  __DATA_CONST.__got: 0x50
+1.57.0.0.0
+  __TEXT.__text: 0x8f30
+  __TEXT.__objc_methlist: 0x2dc
+  __TEXT.__const: 0x63bc
+  __TEXT.__cstring: 0x448
+  __TEXT.__oslogstring: 0x2bd
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x650
-  __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x1cb50
-  __DATA.__common: 0x20
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0x570
+  __AUTH_CONST.__auth_got: 0x160
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0x1972c
+  __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8
-  __DATA_DIRTY.__common: 0x4
+  __DATA_DIRTY.__common: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0944C810-328B-3F86-8475-5CD8063C28C0
-  Functions: 152
-  Symbols:   875
-  CStrings:  510
+  UUID: 836FE846-A5B0-3E3F-8A31-3A6B274E8D98
+  Functions: 122
+  Symbols:   774
+  CStrings:  72
 
Symbols:
+ OBJC_IVAR_$_ASEProcessingT0._dc_state
+ _calcPiecewiseCurveSlope
+ _float_to_fixed_cmodel
+ _getScalingRatio
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_release_x20
+ _objc_retain
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _process_measurement
- -[ASEProcessingT0 DumpOutputHcus:]
- -[ASEProcessingT0 processPixelWithInput_V1:Measurement:Output:].cold.1
- -[ASEProcessingT0 processPixelWithInput_V2:Measurement:Output:].cold.1
- -[ASEProcessingT0 processPixelWithPixelControl_V1:Output:].cold.1
- -[ASEProcessingT0 processPixelWithPixelControl_V2:Output:].cold.1
- -[ASEProcessingT1 DumpArray:type:array:count:numberPerRow:]
- -[ASEProcessingT1 DumpFloatArray:array:count:numberPerRow:]
- -[ASEProcessingT1 DumpIntArray:array:count:numberPerRow:]
- -[ASEProcessingT1 DumpOutputHcus:]
- -[ASEProcessingT1 DumpPiecewiseLinearCurveV3:curve:]
- -[ASEProcessingT1 DumpUintArray:array:count:numberPerRow:]
- -[ASEProcessingT1 initWithConfig:aseProcessing:productType:].cold.1
- -[ASEProcessingT1 populateOutputHcus:].cold.1
- -[ASEProcessingT1 processFrameWithInput:Measurement:outputData:].cold.1
- -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:].cold.1
- -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:].cold.2
- -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:].cold.3
- OBJC_IVAR_$_ASEProcessingT0._FD_state
- OBJC_IVAR_$_ASEProcessingT0._FG_count
- OBJC_IVAR_$_ASEProcessingT0._NFG_count
- OBJC_IVAR_$_ASEProcessingT0._noiseMeterStepSize
- OBJC_IVAR_$_ASEProcessingT0._prev_H1_7
- OBJC_IVAR_$_ASEProcessingT0._prev_V1_7
- OBJC_IVAR_$_ASEProcessingT0._prev_ratio_2D_1D
- OBJC_IVAR_$_ASEProcessingT1._msrBaseAddr
- _CFPreferencesGetAppIntegerValue
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- ___assert_rtn
- ___snprintf_chk
- ___stack_chk_fail
- ___stack_chk_guard
- _calcSlope
- _calculate_control_setting_V3.cold.1
- _calculate_graphics_control_setting_V3
- _copyArray.cold.1
- _copyPieceWiseCurves.cold.1
- _createCacheNode.cold.1
- _createCacheNode.cold.2
- _createCacheNode.cold.3
- _createCacheNode.cold.4
- _disableSampleShift
- _float_to_twos_complement
- _getMSRBaseAddr
- _getMSRBaseAddr.cold.1
- _hideHcu
- _interpolateArray.cold.1
- _interpolatePieceWiseCurves.cold.1
- _maxFGLevel
- _minFGLevel
- _objc_msgSend$DumpArray:type:array:count:numberPerRow:
- _objc_msgSend$DumpFloatArray:array:count:numberPerRow:
- _objc_msgSend$DumpIntArray:array:count:numberPerRow:
- _objc_msgSend$DumpOutputHcus:
- _objc_msgSend$DumpPiecewiseLinearCurveV3:curve:
- _objc_msgSend$DumpUintArray:array:count:numberPerRow:
- _objc_msgSend$bytes
- _objc_msgSend$shouldEnhanceWidth:height:destinationWidth:destinationHeight:
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
- _overrideASEScalingFactor
- _overrideChipID
- _overrideEnhancement
- _overrideFGLevel
- _overrideInputTransferFunction
- _overrideInputType
- _snprintf
CStrings:
+ " [1.57.0] \n"
+ " [1.57.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
+ " [1.57.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
+ " [1.57.0]  %30s: %-12d\n"
+ " [1.57.0] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.57.0] %s : config=%p"
+ " [1.57.0] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
+ " [1.57.0] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
+ " [1.57.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
+ " [1.57.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
+ " [1.57.0] %s: Frame #%llu:\n"
+ " [1.57.0] ++ %s: ASEApiVer=%d\n"
- " "
- "    %s: blendConfigV3Hcu:"
- "    %s: ebeConfigV3Hcu:"
- "    %s: ebeConfigV3Hcu: lowPass :"
- "    %s: ebeConfigV3Hcu: weightLut :"
- "    %s: peakingConfigV3Hcu:"
- "    %s: peakingConfigV3Hcu: filt11 :"
- "    %s: peakingConfigV3Hcu: filt13 :"
- "    %s: peakingConfigV3Hcu: filt3 :"
- "    %s: peakingConfigV3Hcu: filt5 :"
- "    %s: peakingConfigV3Hcu: filt7 :"
- "    %s: peakingConfigV3Hcu: filt9 :"
- "    %s: scalingCoeffV3Hcu: coeff :"
- " [1.55.0] \n"
- " [1.55.0]     %s : ERROR: Not supported, _productType = %d\n"
- " [1.55.0]     %s : INFO: override input type: %d -> %d!\n"
- " [1.55.0]     %s : INFO: override transfer function: %d -> %d!\n"
- " [1.55.0]     %s : Warning: Unexpected format \"%c%c%c%c\", will output sRGB Gamma\n"
- " [1.55.0]     %s : Warning: Unexpected format transfer function %d!\n"
- " [1.55.0]     %s : Warning: Unspecified transfer function, deriving from surface format \"%c%c%c%c\"!\n"
- " [1.55.0]     %s : aseControlUnit->hcuCount %d, aseControlUnit->hcuSize %d, \n"
- " [1.55.0]     %s : aseProcessingType=%d [%s], width=%d, height=%d, strength=%f\n"
- " [1.55.0]     %s : aseProcessingType=%d [%s], width=%d, height=%d, strength=%f, destinationWidth=%d, destinationHeight=%d, inputType=%s\n"
- " [1.55.0]     %s: %09llx:  %08x %08x %08x %08x\n"
- " [1.55.0]     %s: %09llx:  %08x %08x %08x %s\n"
- " [1.55.0]     %s: %09llx:  %08x %08x %s %s\n"
- " [1.55.0]     %s: %09llx:  %08x %s %s %s\n"
- " [1.55.0]     %s: %09llx:  %s %08x %08x %08x\n"
- " [1.55.0]     %s: %09llx:  %s %08x %s %s\n"
- " [1.55.0]     %s: %09llx:  %s %s %s %08x\n"
- " [1.55.0]     %s: -----------------------------------------------\n"
- " [1.55.0]     %s: ASELumaBlendConfig: lumaSlope : { { %d, %d }, { %d, %d }, { %d, %d }, { %d, %d } }\n"
- " [1.55.0]     %s: ASELumaBlendConfig: lumaThresh : { { %d, %d }, { %d, %d }, { %d, %d }, { %d, %d } }\n"
- " [1.55.0]     %s: ASELumaBlendConfig: lumaVal : { { %d, %d }, { %d, %d }, { %d, %d }, { %d, %d } }\n"
- " [1.55.0]     %s: ERROR: Unsupported HCU!  hcuType = 0x%x ('%c%c%c%c')\n"
- " [1.55.0]     %s: _enabledHcus = 0x%x, hideHcu = 0x%x (%d)\n"
- " [1.55.0]     %s: angleDetectV3Hcu: signChangeThreshold = %u, hfeqThresh2 = %u\n"
- " [1.55.0]     %s: blendConfigV3Hcu: BlendLogicSkinToneProtection: toneThresh = %u, toneEdgeThresh = %u, toneMaxThresh = %d, toneFactor = %d\n"
- " [1.55.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveEbeFactor]:\n"
- " [1.55.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveLuma]:\n"
- " [1.55.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveW_EBE]:\n"
- " [1.55.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveW_Peaking]:\n"
- " [1.55.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveEbeV3]:\n"
- " [1.55.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1NegV3]:\n"
- " [1.55.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1PosV3]:\n"
- " [1.55.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf2V3]:\n"
- " [1.55.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf3V3]:\n"
- " [1.55.0]     %s: ebeConfigV3Hcu: ebeParams: { sdaPenalty1 = %d, sdaPenalty2 = %d, dFfactor = %d }\n"
- " [1.55.0]     %s: entryHeader[%d]: hcuSize = %d, hcuType = 0x%x ('%c%c%c%c')\n"
- " [1.55.0]     %s: hcuHeader: hcuCount = %d, hcuSize = %d\n"
- " [1.55.0]     %s: noiseMeterV3Hcu: NoiseMeter: NoiseMeterConfig: sizeX = %u, sizeY = %u\n"
- " [1.55.0]     %s: noiseMeterV3Hcu: NoiseMeter: NoiseMeterGainControl: lut0Gain = %u, lut1Gain = %u, lut2Gain = %u\n"
- " [1.55.0]     %s: peakingConfigV3Hcu: coreGainCurve:\n"
- " [1.55.0]     %s: peakingConfigV3Hcu: gainForce = %d\n"
- " [1.55.0]     %s: peakingConfigV3Hcu: lowAdaptGainCurve:\n"
- " [1.55.0]     %s: peakingConfigV3Hcu: mediumAdaptGainCurve:\n"
- " [1.55.0]     %s: peakingConfigV3Hcu: peakingGain: adaptive = %u, gain5_3 = %u, gain7_5 = %u, gain11_9 = %u, gain13_11 = %u,\n"
- " [1.55.0]     %s: scalingConfigV3Hcu: DDAInitX = %u, DDAInitY = %u, DDAStepX = 0x%x, DDAStepY = 0x%x, DDAInvStepX = 0x%x, DDAInvStepY = 0x%x\n"
- " [1.55.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
- " [1.55.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
- " [1.55.0]  %30s: %-12d\n"
- " [1.55.0]  %30s: %-12f\n"
- " [1.55.0]  08062025 artificial ramp  no enhancement\n"
- " [1.55.0]  applying the fix to all HH02012023\n"
- " [1.55.0] %s\n\n"
- " [1.55.0] %s #%d: { %f, %f, %f }\n"
- " [1.55.0] %s : Unknown device! deviceNameRef: %p, %@, chipID = 0x%llx, productType=%u\n"
- " [1.55.0] %s : Use %s polyphase scaling filters: enhancement_strength = %f, scaler = %f\n"
- " [1.55.0] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
- " [1.55.0] %s : config=%p"
- " [1.55.0] %s : disableSampleShift = %d\n"
- " [1.55.0] %s : enhancement: %f -> %f\n"
- " [1.55.0] %s : initX = %f, initY = %f, DDAInitX = 0x%x, DDAInitY = 0x%x, DDAStepX = 0x%x, DDAStepY = 0x%x, DDAInvStepX = 0x%x, DDAInvStepY = 0x%x\n"
- " [1.55.0] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
- " [1.55.0] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p\n"
- " [1.55.0] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
- " [1.55.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
- " [1.55.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
- " [1.55.0] %s : xScaler = %f, yScaler = %f\n"
- " [1.55.0] %s: Enable graphics settings! isHDR = %s, transferFunction = %s\n"
- " [1.55.0] %s: Failed to query kMGQDeviceName\n"
- " [1.55.0] %s: Frame #%llu:\n"
- " [1.55.0] %s: chipID: 0x%llx -> 0x%x\n"
- " [1.55.0] %s: productType=%d, deviceName = %@, chipID = 0x%llx\n"
- " [1.55.0] ++  %s : ERROR: Async API Not supported!\n"
- " [1.55.0] ++  %s : aseControlUnit=%p\n"
- " [1.55.0] ++  %s : aseControlUnit=%p, strength=%f\n"
- " [1.55.0] ++  %s : input=%p, aseMeasurementOutput=%p, aseControlUnit=%p\n"
- " [1.55.0] ++  %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p\n"
- " [1.55.0] ++  %s : input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
- " [1.55.0] ++  %s : pixelControl=%p\n"
- " [1.55.0] ++ %s : config=%p\n"
- " [1.55.0] ++ %s: ASEApiVer=%d\n"
- " [1.55.0] --  %s \n"
- " [1.55.0] --  %s : _destinationWidth=%d, _destinationHeight=%d, inputType=%s, inputTransferFunction=%s\n"
- " [1.55.0] --  %s : frame=%ld, retVal=%ld\n"
- " [1.55.0] --  %s: HCU Cache disabled!\n"
- " [1.55.0] --  %s: HCU Cache enabled!\n"
- " [1.55.0] -- %s : frame=%ld, retVal=%ld\n"
- " [1.55.0] -- %s : instance=%p\n"
- " [1.55.0] -- %s : retVal=%ld\n"
- " [1.55.0] 06092025: Frame %d:  Ratio_HA_LA_H_2 = %d, Ratio_HA_LA_V_2 = %d, Ratio_HA_LA_HV22  = %d, No_Bad_coded_FilmGrain_score = %d \n"
- " [1.55.0] 06122025 Frame %d:  Curr_GFX_level = %d \n"
- " [1.55.0] 06162025 Frame %d:  Curr_GFX_level = %d,  local_step_size = %d, Curr_badly_coded_FG_level =%d\n"
- " [1.55.0] 07302025: Frame %d:  local_step_size = %d\n"
- " [1.55.0] 07302025: after Band1 adjustment:  No_Bad_coded_FilmGrain_score = %d \n"
- " [1.55.0] 08042025 Frame %d:  Curr_comb_FG = %d, Curr_GFX_level = %d \n"
- " [1.55.0] 08182025: inside else  from if (isPhone), Curr_comb_FG = %d\n"
- " [1.55.0] 08182025: inside populateEbeConfig (variable ratio)\n"
- " [1.55.0] 08272025: inside if (isPhone), Curr_comb_FG = %d\n"
- " [1.55.0] 08282025: Curr_FG_count =%d,  local_FG_count = %d\n"
- " [1.55.0] 08282025: final local_FG_count = %d\n"
- " [1.55.0] 08282025: scene change detected\n"
- " [1.55.0] Apply iPad control setting V2\n"
- " [1.55.0] Apply iPad control setting V3\n"
- " [1.55.0] Apply iPhone control setting V1\n"
- " [1.55.0] Apply iPhone control setting V2\n"
- " [1.55.0] Apply iPhone control setting V3\n"
- " [1.55.0] Assertion: \"!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 1711\n"
- " [1.55.0] Assertion: \"(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 1720\n"
- " [1.55.0] Assertion: \"((void*)0) == config\" failed in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 301 goto EXIT\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingCache.m\" at line 44\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 1047\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 793\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 831\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 960\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 1725\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 1789\n"
- " [1.55.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 277\n"
- " [1.55.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 535 goto EXIT\n"
- " [1.55.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT0.m\" at line 590 goto EXIT\n"
- " [1.55.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 1903 goto EXIT\n"
- " [1.55.0] Assertion: \"count <= 16\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 142\n"
- " [1.55.0] Assertion: \"input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 199\n"
- " [1.55.0] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 207\n"
- " [1.55.0] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 261\n"
- " [1.55.0] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 1922\n"
- " [1.55.0] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingT1.m\" at line 207\n"
- " [1.55.0] Assertion: \"isT1OrNewer(productType)\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 692\n"
- " [1.55.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValueBlend)\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingCache.m\" at line 40\n"
- " [1.55.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValueEbe)\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingCache.m\" at line 36\n"
- " [1.55.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValuePeaking)\" warned in \"/Library/Caches/com.apple.xbs/B46D8D72-BBEA-4B0A-BA34-DC3FDDBCC7E9/TemporaryDirectory.iXRGCv/Sources/ASEFramework/ASEProcessingCache.m\" at line 32\n"
- " [1.55.0] ERROR: Not supported, _asePlatform = %d\n"
- " [1.55.0] Film grain level 0\n"
- " [1.55.0] Film grain level 1\n"
- " [1.55.0] Film grain level 1 LargeRatio\n"
- " [1.55.0] Film grain level 2\n"
- " [1.55.0] Film grain level 2 LargeRatio\n"
- " [1.55.0] Film grain level 3\n"
- " [1.55.0] Film grain level 3 LargeRatio\n"
- " [1.55.0] Film grain level 4\n"
- " [1.55.0] Film grain level 5\n"
- " [1.55.0] Film grain level 6\n"
- " [1.55.0] Film grain level 7\n"
- " [1.55.0] Film grain level 8\n"
- " [1.55.0] Film grain level heavy\n"
- " [1.55.0] Film grain level heavy LargeRatio\n"
- " [1.55.0] Film grain level light\n"
- " [1.55.0] Film grain level light LargeRatio\n"
- " [1.55.0] Frame %d:  Curr_FG_level = %d, Curr_badly_coded_FG_level = %d, No_Bad_coded_FilmGrain_score = %d; inputIsHDR = %d, inputTransferFunction = %d\n"
- " [1.55.0] Frame %d:  Curr_comb_FG = %d\n"
- " [1.55.0] Frame %d:  Curr_comb_FG = %d -> %d\n"
- " [1.55.0] Frame %d: TemporalControl: Curr_comb_FG = %d -> %d, prev_comb_FG = %d (%d:%d),  max_change_per_frame = (%d: %dx%d)\n"
- " [1.55.0] Frame %ld aseMeasurementOutput:\n"
- " [1.55.0] HH08202025 DZ : %f  \n"
- " [1.55.0] applying the zoneplate fix to all HH02012023\n"
- " [1.55.0] aseControlUnit->asePixelControl.dsEnable=%d, enhancementConfig.{ebeEnable=%d, peakingEnable=%d, chromaEnhanceEnable=%d}\n"
- " [1.55.0] aseControlUnit->hcuCount %d, aseControlUnit->hcuSize %d, \n"
- " [1.55.0] aseControlUnit->noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
- " [1.55.0] aseFrameProcessingControl->control.size (V1) is %lu, ASELumaBlendConfig is %lu\n"
- " [1.55.0] blkCtrH[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] blkCtrV[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] blkDiffH[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] blkDiffV[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutH1[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutH2[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutHV0[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutHV0[9 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutHV1[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutHV1[7 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutHV2[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutHV2[0 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutV1[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] histOutV2[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
- " [1.55.0] maxAbsH0 = %010d\n"
- " [1.55.0] maxAbsH1 = %010d\n"
- " [1.55.0] maxAbsH2 = %010d\n"
- " [1.55.0] maxAbsHV0 = %010d\n"
- " [1.55.0] maxAbsHV1 = %010d\n"
- " [1.55.0] maxAbsHV2 = %010d\n"
- " [1.55.0] maxAbsV0 = %010d\n"
- " [1.55.0] maxAbsV1 = %010d\n"
- " [1.55.0] maxAbsV2 = %010d\n"
- " [1.55.0] noDS == 1, set mediumAdaptGain = 0, adjust Hfactor\n"
- " [1.55.0] noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
- " [1.55.0] pixelControl->blendLogicCurve.point0.slope=%f\n"
- " [1.55.0] pixelControl->blendLogicCurve.point0.x_position=%f\n"
- " [1.55.0] pixelControl->blendLogicCurve.point0.y_position=%f\n"
- " [1.55.0] pixelControl->noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
- " [1.55.0] pixelControl[%p]=%s\n"
- " [1.55.0] scene_change_detected = %d, ratio_2D_1D is :%d vs %d; H1 is : %d vs %d,  V1 is: %d vs %d;\n"
- " [1.55.0] sumAbsHV0 = %010d\n"
- " [1.55.0] sumAbsHV1 = %010d\n"
- " [1.55.0] sumAbsHV2 = %010d\n"
- " [1.55.0] totalValid = %010d\n"
- " [1.55.0] totalValidActivity = %010d\n"
- " [1.55.0] totalValidValue = %010d\n"
- " [1.55.0] variance = %010d\n"
- " }"
- "!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
- "%s %s"
- "%s%d"
- "%s%f"
- "%s%u"
- "(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
- ","
- ", "
- "-[ASEProcessingT0 DumpOutputHcus:]"
- "-[ASEProcessingT0 dealloc]"
- "-[ASEProcessingT0 digitalZoomSelectControl_V2:]"
- "-[ASEProcessingT0 processPixelWithInput:Measurement:controlUnit:]"
- "-[ASEProcessingT0 processPixelWithInput_V1:Measurement:Output:]"
- "-[ASEProcessingT0 processPixelWithInput_V2:Measurement:Output:]"
- "-[ASEProcessingT0 processPixelWithMeasurement_V1:Measurement:pixelControl:]"
- "-[ASEProcessingT0 processPixelWithMeasurement_V2:Measurement:Output:]"
- "-[ASEProcessingT0 processPixelWithPixelControl_V1:Output:]"
- "-[ASEProcessingT0 processPixelWithPixelControl_V2:Output:]"
- "-[ASEProcessingT1 DumpOutputHcus:]"
- "-[ASEProcessingT1 dealloc]"
- "-[ASEProcessingT1 initWithConfig:aseProcessing:productType:]"
- "-[ASEProcessingT1 populateOutputHcus:]"
- "-[ASEProcessingT1 processFrameWithInput:Measurement:callback:]"
- "-[ASEProcessingT1 processPixelWithInput:Measurement:controlUnitV3:]"
- "-[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:]"
- "-[ASEProcessingT1 processPixelWithMeasurement_V3:Measurement:Output:]"
- "-[ASEProcessingT1 processPixelWithPixelControl_V3:Output:]"
- ".cxx_destruct"
- "0"
- "@\"ASEProcessingT0\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@16@0:8"
- "@24@0:8^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
- "@24@0:8r^{?=iIII}16"
- "@36@0:8r^{?=iIII}16@24I32"
- "ASECalculateControlSettingV3.m"
- "ASEProcessing"
- "ASEProcessingCache.m"
- "ASEProcessingT0"
- "ASEProcessingT0.m"
- "ASEProcessingT1"
- "ASEProcessingT1.m"
- "ASEProductType getCurrentProductType(void)"
- "B"
- "B16@0:8"
- "B32@0:8I16I20I24I28"
- "B36@0:8I16I20I24I28f32"
- "Default"
- "DumpArray:type:array:count:numberPerRow:"
- "DumpFloatArray:array:count:numberPerRow:"
- "DumpIntArray:array:count:numberPerRow:"
- "DumpOutputHcus:"
- "DumpPiecewiseLinearCurveV3:curve:"
- "DumpUintArray:array:count:numberPerRow:"
- "FG_dyn_setting"
- "I"
- "I16@0:8"
- "InitialSettingVideo"
- "InitialSettingVideo_V2"
- "Mix_dyn_setting"
- "NEW"
- "Q"
- "SettingVideo_NFG"
- "SettingVideo_NFG LargeRatio"
- "SettingVideo_NFG_LargeRatio_V2"
- "SettingVideo_NFG_V2"
- "TB,N,V_inputType"
- "TI,N,V_destinationHeight"
- "TI,N,V_destinationWidth"
- "Tf,N,V_enhancementStrength"
- "XXXXXXXX"
- "^{?={?=I^{_ASEHcuCacheNodeCommon}^{_ASEHcuCacheNodeCommon}{?=QQQ}}{?=I^{_ASEHcuCacheNodeCommon}^{_ASEHcuCacheNodeCommon}{?=QQQ}}{?=I^{_ASEHcuCacheNodeCommon}^{_ASEHcuCacheNodeCommon}{?=QQQ}}}"
- "^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}"
- "^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}"
- "_Bool getInputType(_Bool)"
- "_FD_state"
- "_FG_count"
- "_NFG_count"
- "_ase"
- "_aseControlUnit"
- "_aseControlUnitV3"
- "_aseControlUnitV3Cache"
- "_asePlatform"
- "_aseProcessingType"
- "_aseProcessingVersion"
- "_completionQueue"
- "_destinationHeight"
- "_destinationWidth"
- "_enabledHcus"
- "_enhancementStrength"
- "_inputHeight"
- "_inputType"
- "_inputWidth"
- "_msrBaseAddr"
- "_noiseMeterStepSize"
- "_numberOfProcessedFrames"
- "_numberOfRequestedFrames"
- "_numberOfScheduledFrames"
- "_prev_H1_7"
- "_prev_V1_7"
- "_prev_ratio_2D_1D"
- "_prev_temporal_context"
- "_productType"
- "_scheduleQueue"
- "_scheduleSemaphone"
- "appendBytes:length:"
- "bytes"
- "calculate_control_setting_V3"
- "com.apple.aseprocessing"
- "configControlHeader_V1:"
- "configControlHeader_V2:"
- "configControlHeader_V3:"
- "copyArray"
- "copyPieceWiseCurves"
- "count <= 16"
- "createCacheNode"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "dealloc"
- "destinationHeight"
- "destinationWidth"
- "digitalZoomSelectControl_V1:"
- "digitalZoomSelectControl_V2:"
- "disableSampleShift"
- "enhancementStrength"
- "exceptionWithName:reason:userInfo:"
- "f"
- "f16@0:8"
- "getCurrentProductType"
- "getDestinationHeight"
- "getDestinationWidth"
- "getEnhancementStrength"
- "getMSRBaseAddr"
- "hideHcu"
- "i"
- "iPhone_SettingVideo_NFG_LargeRatio_V2"
- "iPhone_SettingVideo_NFG_V2"
- "init"
- "initWithConfig:"
- "initWithConfig:aseProcessing:productType:"
- "input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16"
- "input && input->type == WDT_TYPE_INTERPOLATED"
- "input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16"
- "inputTransferFunction"
- "inputType"
- "intValue"
- "interpolateArray"
- "interpolatePieceWiseCurves"
- "isT1OrNewer(_productType)"
- "isT1OrNewer(productType)"
- "maxFGLevel"
- "minFGLevel"
- "objectForKeyedSubscript:"
- "overrideChipID"
- "overrideEnhancement"
- "overrideFGLevel"
- "peakingConfig_FG"
- "peakingConfig_InitialSettingVideo_V3"
- "populateOutputHcus:"
- "populateScalingConfig"
- "printAseMeasurementOutput:"
- "processFrameWithInput:Measurement:Output:"
- "processFrameWithInput:Measurement:callback:"
- "processFrameWithInput:Measurement:outputData:"
- "processFrameWithInput:Output:"
- "processFrameWithInput:callback:"
- "processFrameWithInput:outputData:"
- "processPixelWithInput:Measurement:controlUnit:"
- "processPixelWithInput:Measurement:controlUnitV3:"
- "processPixelWithInput_V1:Measurement:Output:"
- "processPixelWithInput_V2:Measurement:Output:"
- "processPixelWithInput_V3:Measurement:Output:"
- "processPixelWithMeasurement_V1:Measurement:pixelControl:"
- "processPixelWithMeasurement_V2:Measurement:Output:"
- "processPixelWithMeasurement_V3:Measurement:Output:"
- "processPixelWithPixelControl_V1:Output:"
- "processPixelWithPixelControl_V2:Output:"
- "processPixelWithPixelControl_V3:Output:"
- "q32@0:8^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16@?24"
- "q32@0:8^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16^@24"
- "q32@0:8^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16^{?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}24"
- "q40@0:8^{__IOSurface=}16^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24@?32"
- "q40@0:8^{__IOSurface=}16^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^@32"
- "q40@0:8^{__IOSurface=}16^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^{?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}32"
- "setDestinationHeight:"
- "setDestinationWidth:"
- "setEnhancementStrength:"
- "setInputType:"
- "shouldApplyGraphicSettings"
- "shouldEnhanceWidth:height:destinationWidth:destinationHeight:"
- "shouldEnhanceWidth:height:destinationWidth:destinationHeight:fps:"
- "size == sizeof(ASEHcuCacheNodeValueBlend)"
- "size == sizeof(ASEHcuCacheNodeValueEbe)"
- "size == sizeof(ASEHcuCacheNodeValuePeaking)"
- "uint32_t getTransferFunction(IOSurfaceRef _Nonnull)"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v24@0:8@16"
- "v24@0:8^{aseConfigurationUnitsV1_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}16"
- "v24@0:8^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}16"
- "v24@0:8^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
- "v24@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}16"
- "v24@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16"
- "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV1_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}24"
- "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}24"
- "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}24"
- "v32@0:8r*16^{?=[32{?=fff}]}24"
- "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}24^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}32"
- "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^{aseConfigurationUnitsV1_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}32"
- "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}32"
- "v40@0:8r*16r^I24I32I36"
- "v40@0:8r*16r^f24I32I36"
- "v40@0:8r*16r^i24I32I36"
- "v44@0:8r*16i24^v28I36I40"
- "void populateScalingCoeff(scalingCoeffV3Hcu *, float, float, float, int, uint32_t *)"
- "void populateScalingConfig(scalingConfigV3Hcu *, float, float, uint32_t *)"
- "{"
- "{?=\"FG_value\"i\"FG_level_count\"[5i]}"

```

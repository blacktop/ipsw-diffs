## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

 1.50.3.0.0
-  __TEXT.__text: 0x8578
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x2dc
-  __TEXT.__const: 0x1be2c
-  __TEXT.__cstring: 0x380
-  __TEXT.__oslogstring: 0x27d
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__text: 0x153c4
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__const: 0x1be9c
+  __TEXT.__oslogstring: 0x3643
+  __TEXT.__cstring: 0xf81
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x7ea
-  __TEXT.__objc_methtype: 0x23fe
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_methname: 0x8c3
+  __TEXT.__objc_methtype: 0x2485
+  __TEXT.__objc_stubs: 0x5e0
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x1b8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x630
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1c818

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F086CC19-9F90-36A4-8D40-338496CB27F4
-  Functions: 116
-  Symbols:   824
-  CStrings:  184
+  UUID: 13870BF4-42F8-3919-B844-A67102FA8F26
+  Functions: 144
+  Symbols:   903
+  CStrings:  481
 
Symbols:
+ -[ASEProcessingT0 DumpOutputHcus:]
+ -[ASEProcessingT0 processPixelWithInput_V1:Measurement:Output:].cold.1
+ -[ASEProcessingT0 processPixelWithInput_V2:Measurement:Output:].cold.1
+ -[ASEProcessingT0 processPixelWithPixelControl_V1:Output:].cold.1
+ -[ASEProcessingT0 processPixelWithPixelControl_V2:Output:].cold.1
+ -[ASEProcessingT1 DumpArray:type:array:count:numberPerRow:]
+ -[ASEProcessingT1 DumpFloatArray:array:count:numberPerRow:]
+ -[ASEProcessingT1 DumpIntArray:array:count:numberPerRow:]
+ -[ASEProcessingT1 DumpOutputHcus:]
+ -[ASEProcessingT1 DumpPiecewiseLinearCurveV3:curve:]
+ -[ASEProcessingT1 DumpUintArray:array:count:numberPerRow:]
+ -[ASEProcessingT1 initWithConfig:aseProcessing:productType:].cold.1
+ -[ASEProcessingT1 populateOutputHcus:].cold.1
+ -[ASEProcessingT1 processFrameWithInput:Measurement:outputData:].cold.1
+ -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:].cold.1
+ -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:].cold.2
+ -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:].cold.3
+ _CFPreferencesGetAppIntegerValue
+ _OUTLINED_FUNCTION_0
+ ___assert_rtn
+ ___snprintf_chk
+ _calculate_control_setting_V3.cold.1
+ _copyArray.cold.1
+ _copyPieceWiseCurves.cold.1
+ _createCacheNode.cold.1
+ _createCacheNode.cold.2
+ _createCacheNode.cold.3
+ _createCacheNode.cold.4
+ _getMSRBaseAddr.cold.1
+ _interpolateArray.cold.1
+ _interpolatePieceWiseCurves.cold.1
+ _objc_msgSend$DumpArray:type:array:count:numberPerRow:
+ _objc_msgSend$DumpFloatArray:array:count:numberPerRow:
+ _objc_msgSend$DumpIntArray:array:count:numberPerRow:
+ _objc_msgSend$DumpOutputHcus:
+ _objc_msgSend$DumpPiecewiseLinearCurveV3:curve:
+ _objc_msgSend$DumpUintArray:array:count:numberPerRow:
+ _objc_msgSend$bytes
+ _objc_msgSend$shouldEnhanceWidth:height:destinationWidth:destinationHeight:
+ _objc_release_x21
+ _objc_release_x23
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _snprintf
- _objc_release
CStrings:
+ " "
+ "    %s: blendConfigV3Hcu:"
+ "    %s: ebeConfigV3Hcu:"
+ "    %s: ebeConfigV3Hcu: lowPass :"
+ "    %s: ebeConfigV3Hcu: weightLut :"
+ "    %s: peakingConfigV3Hcu:"
+ "    %s: peakingConfigV3Hcu: filt11 :"
+ "    %s: peakingConfigV3Hcu: filt13 :"
+ "    %s: peakingConfigV3Hcu: filt3 :"
+ "    %s: peakingConfigV3Hcu: filt5 :"
+ "    %s: peakingConfigV3Hcu: filt7 :"
+ "    %s: peakingConfigV3Hcu: filt9 :"
+ "    %s: scalingCoeffV3Hcu: coeff :"
+ " [1.50.3]     %s : ERROR: Not supported, _productType = %d\n"
+ " [1.50.3]     %s : INFO: override input type: %d -> %d!\n"
+ " [1.50.3]     %s : INFO: override transfer function: %d -> %d!\n"
+ " [1.50.3]     %s : Warning: Unexpected format \"%c%c%c%c\", will output sRGB Gamma\n"
+ " [1.50.3]     %s : Warning: Unexpected format transfer function %d!\n"
+ " [1.50.3]     %s : Warning: Unspecified transfer function, deriving from surface format \"%c%c%c%c\"!\n"
+ " [1.50.3]     %s : aseControlUnit->hcuCount %d, aseControlUnit->hcuSize %d, \n"
+ " [1.50.3]     %s : aseProcessingType=%d [%s], width=%d, height=%d, strength=%f\n"
+ " [1.50.3]     %s : aseProcessingType=%d [%s], width=%d, height=%d, strength=%f, destinationWidth=%d, destinationHeight=%d, inputType=%s\n"
+ " [1.50.3]     %s: %09llx:  %08x %08x %08x %08x\n"
+ " [1.50.3]     %s: %09llx:  %08x %08x %08x %s\n"
+ " [1.50.3]     %s: %09llx:  %08x %08x %s %s\n"
+ " [1.50.3]     %s: %09llx:  %08x %s %s %s\n"
+ " [1.50.3]     %s: %09llx:  %s %08x %08x %08x\n"
+ " [1.50.3]     %s: %09llx:  %s %08x %s %s\n"
+ " [1.50.3]     %s: %09llx:  %s %s %s %08x\n"
+ " [1.50.3]     %s: -----------------------------------------------\n"
+ " [1.50.3]     %s: ASELumaBlendConfig: lumaSlope : { { %d, %d }, { %d, %d }, { %d, %d }, { %d, %d } }\n"
+ " [1.50.3]     %s: ASELumaBlendConfig: lumaThresh : { { %d, %d }, { %d, %d }, { %d, %d }, { %d, %d } }\n"
+ " [1.50.3]     %s: ASELumaBlendConfig: lumaVal : { { %d, %d }, { %d, %d }, { %d, %d }, { %d, %d } }\n"
+ " [1.50.3]     %s: ERROR: Unsupported HCU!  hcuType = 0x%x ('%c%c%c%c')\n"
+ " [1.50.3]     %s: _enabledHcus = 0x%x, hideHcu = 0x%x (%d)\n"
+ " [1.50.3]     %s: angleDetectV3Hcu: signChangeThreshold = %u, hfeqThresh2 = %u\n"
+ " [1.50.3]     %s: blendConfigV3Hcu: BlendLogicSkinToneProtection: toneThresh = %u, toneEdgeThresh = %u, toneMaxThresh = %d, toneFactor = %d\n"
+ " [1.50.3]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveEbeFactor]:\n"
+ " [1.50.3]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveLuma]:\n"
+ " [1.50.3]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveW_EBE]:\n"
+ " [1.50.3]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveW_Peaking]:\n"
+ " [1.50.3]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveEbeV3]:\n"
+ " [1.50.3]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1NegV3]:\n"
+ " [1.50.3]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1PosV3]:\n"
+ " [1.50.3]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf2V3]:\n"
+ " [1.50.3]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf3V3]:\n"
+ " [1.50.3]     %s: ebeConfigV3Hcu: ebeParams: { sdaPenalty1 = %d, sdaPenalty2 = %d, dFfactor = %d }\n"
+ " [1.50.3]     %s: entryHeader[%d]: hcuSize = %d, hcuType = 0x%x ('%c%c%c%c')\n"
+ " [1.50.3]     %s: hcuHeader: hcuCount = %d, hcuSize = %d\n"
+ " [1.50.3]     %s: noiseMeterV3Hcu: NoiseMeter: NoiseMeterConfig: sizeX = %u, sizeY = %u\n"
+ " [1.50.3]     %s: noiseMeterV3Hcu: NoiseMeter: NoiseMeterGainControl: lut0Gain = %u, lut1Gain = %u, lut2Gain = %u\n"
+ " [1.50.3]     %s: peakingConfigV3Hcu: coreGainCurve:\n"
+ " [1.50.3]     %s: peakingConfigV3Hcu: gainForce = %d\n"
+ " [1.50.3]     %s: peakingConfigV3Hcu: lowAdaptGainCurve:\n"
+ " [1.50.3]     %s: peakingConfigV3Hcu: mediumAdaptGainCurve:\n"
+ " [1.50.3]     %s: peakingConfigV3Hcu: peakingGain: adaptive = %u, gain5_3 = %u, gain7_5 = %u, gain11_9 = %u, gain13_11 = %u,\n"
+ " [1.50.3]     %s: scalingConfigV3Hcu: DDAInitX = %u, DDAInitY = %u, DDAStepX = 0x%x, DDAStepY = 0x%x, DDAInvStepX = 0x%x, DDAInvStepY = 0x%x\n"
+ " [1.50.3]  08062025 artificial ramp  no enhancement\n"
+ " [1.50.3]  applying the fix to all HH02012023\n"
+ " [1.50.3] %s\n\n"
+ " [1.50.3] %s #%d: { %f, %f, %f }\n"
+ " [1.50.3] %s : Unknown device! deviceNameRef: %p, %@, chipID = 0x%llx, productType=%u\n"
+ " [1.50.3] %s : Use %s polyphase scaling filters: enhancement_strength = %f, scaler = %f\n"
+ " [1.50.3] %s : disableSampleShift = %d\n"
+ " [1.50.3] %s : enhancement: %f -> %f\n"
+ " [1.50.3] %s : initX = %f, initY = %f, DDAInitX = 0x%x, DDAInitY = 0x%x, DDAStepX = 0x%x, DDAStepY = 0x%x, DDAInvStepX = 0x%x, DDAInvStepY = 0x%x\n"
+ " [1.50.3] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p\n"
+ " [1.50.3] %s : xScaler = %f, yScaler = %f\n"
+ " [1.50.3] %s: Enable graphics settings! isHDR = %s, transferFunction = %s\n"
+ " [1.50.3] %s: Failed to query kMGQDeviceName\n"
+ " [1.50.3] %s: productType=%d, deviceName = %@, chipID = 0x%llx\n"
+ " [1.50.3] ++  %s : ERROR: Async API Not supported!\n"
+ " [1.50.3] ++  %s : aseControlUnit=%p\n"
+ " [1.50.3] ++  %s : aseControlUnit=%p, strength=%f\n"
+ " [1.50.3] ++  %s : input=%p, aseMeasurementOutput=%p, aseControlUnit=%p\n"
+ " [1.50.3] ++  %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p\n"
+ " [1.50.3] ++  %s : input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.50.3] ++  %s : pixelControl=%p\n"
+ " [1.50.3] ++ %s : config=%p\n"
+ " [1.50.3] --  %s \n"
+ " [1.50.3] --  %s : _destinationWidth=%d, _destinationHeight=%d, inputType=%s, inputTransferFunction=%s\n"
+ " [1.50.3] --  %s : frame=%ld, retVal=%ld\n"
+ " [1.50.3] --  %s: HCU Cache disabled!\n"
+ " [1.50.3] --  %s: HCU Cache enabled!\n"
+ " [1.50.3] -- %s : frame=%ld, retVal=%ld\n"
+ " [1.50.3] -- %s : instance=%p\n"
+ " [1.50.3] -- %s : retVal=%ld\n"
+ " [1.50.3] 06092025: Frame %d:  Ratio_HA_LA_H_2 = %d, Ratio_HA_LA_V_2 = %d, Ratio_HA_LA_HV22  = %d, No_Bad_coded_FilmGrain_score = %d \n"
+ " [1.50.3] 06122025 Frame %d:  Curr_GFX_level = %d \n"
+ " [1.50.3] 06162025 Frame %d:  Curr_GFX_level = %d,  local_step_size = %d, Curr_badly_coded_FG_level =%d\n"
+ " [1.50.3] 07302025: Frame %d:  local_step_size = %d\n"
+ " [1.50.3] 07302025: after Band1 adjustment:  No_Bad_coded_FilmGrain_score = %d \n"
+ " [1.50.3] 08042025 Frame %d:  Curr_GFX_level = %d \n"
+ " [1.50.3] 08182025: inside else  from if (isPhone), Curr_comb_FG = %d\n"
+ " [1.50.3] 08272025: inside if (isPhone), Curr_comb_FG = %d\n"
+ " [1.50.3] 08282025: Curr_FG_count =%d,  local_FG_count = %d\n"
+ " [1.50.3] 08282025: final local_FG_count = %d\n"
+ " [1.50.3] 08282025: scene change detected\n"
+ " [1.50.3] Apply iPad control setting V2\n"
+ " [1.50.3] Apply iPad control setting V3\n"
+ " [1.50.3] Apply iPhone control setting V1\n"
+ " [1.50.3] Apply iPhone control setting V2\n"
+ " [1.50.3] Apply iPhone control setting V3\n"
+ " [1.50.3] Assertion: \"!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1580\n"
+ " [1.50.3] Assertion: \"(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1589\n"
+ " [1.50.3] Assertion: \"((void*)0) == config\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 301 goto EXIT\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 44\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 1044\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 790\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 828\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 957\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 146\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1594\n"
+ " [1.50.3] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1654\n"
+ " [1.50.3] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 531 goto EXIT\n"
+ " [1.50.3] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 586 goto EXIT\n"
+ " [1.50.3] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1769 goto EXIT\n"
+ " [1.50.3] Assertion: \"count <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 142\n"
+ " [1.50.3] Assertion: \"input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 199\n"
+ " [1.50.3] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 207\n"
+ " [1.50.3] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 261\n"
+ " [1.50.3] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 100\n"
+ " [1.50.3] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1788\n"
+ " [1.50.3] Assertion: \"isT1OrNewer(productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 575\n"
+ " [1.50.3] Assertion: \"size == sizeof(ASEHcuCacheNodeValueBlend)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 40\n"
+ " [1.50.3] Assertion: \"size == sizeof(ASEHcuCacheNodeValueEbe)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 36\n"
+ " [1.50.3] Assertion: \"size == sizeof(ASEHcuCacheNodeValuePeaking)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 32\n"
+ " [1.50.3] ERROR: Not supported, _asePlatform = %d\n"
+ " [1.50.3] Film grain level 0\n"
+ " [1.50.3] Film grain level 1\n"
+ " [1.50.3] Film grain level 1 LargeRatio\n"
+ " [1.50.3] Film grain level 2\n"
+ " [1.50.3] Film grain level 2 LargeRatio\n"
+ " [1.50.3] Film grain level 3\n"
+ " [1.50.3] Film grain level 3 LargeRatio\n"
+ " [1.50.3] Film grain level 4\n"
+ " [1.50.3] Film grain level 5\n"
+ " [1.50.3] Film grain level 6\n"
+ " [1.50.3] Film grain level 7\n"
+ " [1.50.3] Film grain level 8\n"
+ " [1.50.3] Film grain level heavy\n"
+ " [1.50.3] Film grain level heavy LargeRatio\n"
+ " [1.50.3] Film grain level light\n"
+ " [1.50.3] Film grain level light LargeRatio\n"
+ " [1.50.3] Frame %d:  Curr_FG_level = %d, Curr_badly_coded_FG_level = %d, No_Bad_coded_FilmGrain_score = %d; inputIsHDR = %d, inputTransferFunction = %d\n"
+ " [1.50.3] Frame %ld aseMeasurementOutput:\n"
+ " [1.50.3] applying the zoneplate fix to all HH02012023\n"
+ " [1.50.3] aseControlUnit->asePixelControl.dsEnable=%d, enhancementConfig.{ebeEnable=%d, peakingEnable=%d, chromaEnhanceEnable=%d}\n"
+ " [1.50.3] aseControlUnit->hcuCount %d, aseControlUnit->hcuSize %d, \n"
+ " [1.50.3] aseControlUnit->noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
+ " [1.50.3] aseFrameProcessingControl->control.size (V1) is %lu, ASELumaBlendConfig is %lu\n"
+ " [1.50.3] blkCtrH[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] blkCtrV[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] blkDiffH[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] blkDiffV[ 0 -  5] = %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutH1[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutH2[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutHV0[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutHV0[9 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutHV1[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutHV1[7 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutHV2[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutHV2[0 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutV1[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] histOutV2[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.50.3] maxAbsH0 = %010d\n"
+ " [1.50.3] maxAbsH1 = %010d\n"
+ " [1.50.3] maxAbsH2 = %010d\n"
+ " [1.50.3] maxAbsHV0 = %010d\n"
+ " [1.50.3] maxAbsHV1 = %010d\n"
+ " [1.50.3] maxAbsHV2 = %010d\n"
+ " [1.50.3] maxAbsV0 = %010d\n"
+ " [1.50.3] maxAbsV1 = %010d\n"
+ " [1.50.3] maxAbsV2 = %010d\n"
+ " [1.50.3] noDS == 1, set mediumAdaptGain = 0, adjust Hfactor\n"
+ " [1.50.3] noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
+ " [1.50.3] pixelControl->blendLogicCurve.point0.slope=%f\n"
+ " [1.50.3] pixelControl->blendLogicCurve.point0.x_position=%f\n"
+ " [1.50.3] pixelControl->blendLogicCurve.point0.y_position=%f\n"
+ " [1.50.3] pixelControl->noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
+ " [1.50.3] pixelControl[%p]=%s\n"
+ " [1.50.3] scene_change_detected = %d, ratio_2D_1D is :%d vs %d; H1 is : %d vs %d,  V1 is: %d vs %d;\n"
+ " [1.50.3] sumAbsHV0 = %010d\n"
+ " [1.50.3] sumAbsHV1 = %010d\n"
+ " [1.50.3] sumAbsHV2 = %010d\n"
+ " [1.50.3] totalValid = %010d\n"
+ " [1.50.3] totalValidActivity = %010d\n"
+ " [1.50.3] totalValidValue = %010d\n"
+ " [1.50.3] variance = %010d\n"
+ " }"
+ "!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
+ "%s %s"
+ "%s%d"
+ "%s%f"
+ "%s%u"
+ "(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
+ ","
+ ", "
+ "-[ASEProcessingT0 DumpOutputHcus:]"
+ "-[ASEProcessingT0 dealloc]"
+ "-[ASEProcessingT0 digitalZoomSelectControl_V2:]"
+ "-[ASEProcessingT0 processPixelWithInput:Measurement:controlUnit:]"
+ "-[ASEProcessingT0 processPixelWithInput_V1:Measurement:Output:]"
+ "-[ASEProcessingT0 processPixelWithInput_V2:Measurement:Output:]"
+ "-[ASEProcessingT0 processPixelWithMeasurement_V1:Measurement:pixelControl:]"
+ "-[ASEProcessingT0 processPixelWithMeasurement_V2:Measurement:Output:]"
+ "-[ASEProcessingT0 processPixelWithPixelControl_V1:Output:]"
+ "-[ASEProcessingT0 processPixelWithPixelControl_V2:Output:]"
+ "-[ASEProcessingT1 DumpOutputHcus:]"
+ "-[ASEProcessingT1 dealloc]"
+ "-[ASEProcessingT1 initWithConfig:aseProcessing:productType:]"
+ "-[ASEProcessingT1 populateOutputHcus:]"
+ "-[ASEProcessingT1 processFrameWithInput:Measurement:callback:]"
+ "-[ASEProcessingT1 processPixelWithInput:Measurement:controlUnitV3:]"
+ "-[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:]"
+ "-[ASEProcessingT1 processPixelWithMeasurement_V3:Measurement:Output:]"
+ "-[ASEProcessingT1 processPixelWithPixelControl_V3:Output:]"
+ "0"
+ "ASECalculateControlSettingV3.m"
+ "ASEProcessingCache.m"
+ "ASEProcessingT0.m"
+ "ASEProcessingT1.m"
+ "ASEproductType getCurrentProductType(void)"
+ "Default"
+ "DumpArray:type:array:count:numberPerRow:"
+ "DumpFloatArray:array:count:numberPerRow:"
+ "DumpIntArray:array:count:numberPerRow:"
+ "DumpOutputHcus:"
+ "DumpPiecewiseLinearCurveV3:curve:"
+ "DumpUintArray:array:count:numberPerRow:"
+ "FG_dyn_setting"
+ "InitialSettingVideo"
+ "InitialSettingVideo_V2"
+ "Mix_dyn_setting"
+ "NEW"
+ "SettingVideo_NFG"
+ "SettingVideo_NFG LargeRatio"
+ "SettingVideo_NFG_LargeRatio_V2"
+ "SettingVideo_NFG_V2"
+ "XXXXXXXX"
+ "_Bool getInputType(_Bool)"
+ "bytes"
+ "calculate_control_setting_V3"
+ "com.apple.aseprocessing"
+ "copyArray"
+ "copyPieceWiseCurves"
+ "count <= 16"
+ "createCacheNode"
+ "disableHcuCache"
+ "disableSampleShift"
+ "dumpOutputHcu"
+ "getCurrentProductType"
+ "getMSRBaseAddr"
+ "hideHcu"
+ "iPhone_SettingVideo_NFG_LargeRatio_V2"
+ "iPhone_SettingVideo_NFG_V2"
+ "input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16"
+ "input && input->type == WDT_TYPE_INTERPOLATED"
+ "input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16"
+ "inputTransferFunction"
+ "interpolateArray"
+ "interpolatePieceWiseCurves"
+ "isT1OrNewer(_productType)"
+ "isT1OrNewer(productType)"
+ "logLevel"
+ "overrideEnhancement"
+ "overrideFGLevel"
+ "peakingConfig_FG"
+ "peakingConfig_InitialSettingVideo_V3"
+ "populateScalingConfig"
+ "readDefaultsWriteEnabled"
+ "shouldApplyGraphicSettings"
+ "size == sizeof(ASEHcuCacheNodeValueBlend)"
+ "size == sizeof(ASEHcuCacheNodeValueEbe)"
+ "size == sizeof(ASEHcuCacheNodeValuePeaking)"
+ "uint32_t getTransferFunction(IOSurfaceRef _Nonnull)"
+ "v24@0:8@16"
+ "v32@0:8r*16^{?=[32{?=fff}]}24"
+ "v40@0:8r*16r^I24I32I36"
+ "v40@0:8r*16r^f24I32I36"
+ "v40@0:8r*16r^i24I32I36"
+ "v44@0:8r*16i24^v28I36I40"
+ "void populateScalingCoeff(scalingCoeffV3Hcu *, float, float, float, int, uint32_t *)"
+ "void populateScalingConfig(scalingConfigV3Hcu *, float, float, uint32_t *)"
+ "{"

```

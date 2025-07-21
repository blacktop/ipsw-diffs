## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

 1.41.0.0.0
-  __TEXT.__text: 0x6fe0
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x288
-  __TEXT.__const: 0x366f4
-  __TEXT.__oslogstring: 0x25c
-  __TEXT.__cstring: 0x340
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__text: 0x12aec
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x2ac
+  __TEXT.__const: 0x3673c
+  __TEXT.__oslogstring: 0x2c16
+  __TEXT.__cstring: 0xdfc
+  __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x6d4
-  __TEXT.__objc_methtype: 0x19f3
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_methname: 0x723
+  __TEXT.__objc_methtype: 0x1a2f
+  __TEXT.__objc_stubs: 0x540
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x148
-  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x600
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x1a4a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F75EABE0-ECD4-315B-9190-48A5858F639C
-  Functions: 98
-  Symbols:   810
-  CStrings:  166
+  UUID: 7B4F4ED2-F728-3506-9D17-C19A9EF3FE52
+  Functions: 122
+  Symbols:   879
+  CStrings:  403
 
Symbols:
+ -[ASEProcessingT0 processPixelWithInput_V1:Output:].cold.1
+ -[ASEProcessingT0 processPixelWithInput_V2:Output:].cold.1
+ -[ASEProcessingT0 processPixelWithPixelControl_V1:].cold.1
+ -[ASEProcessingT0 processPixelWithPixelControl_V2:].cold.1
+ -[ASEProcessingT1 DumpArray:array:count:]
+ -[ASEProcessingT1 DumpOutputHcus:]
+ -[ASEProcessingT1 DumpPiecewiseLinearCurveV3:curve:]
+ -[ASEProcessingT1 initWithConfig:aseProcessing:productType:].cold.1
+ -[ASEProcessingT1 populateOutputHcus:].cold.1
+ -[ASEProcessingT1 processFrameWithInput:outputData:].cold.1
+ -[ASEProcessingT1 processPixelWithInput_V3:Output:].cold.1
+ -[ASEProcessingT1 processPixelWithInput_V3:Output:].cold.2
+ -[ASEProcessingT1 processPixelWithInput_V3:Output:].cold.3
+ _CFPreferencesGetAppIntegerValue
+ _OUTLINED_FUNCTION_0
+ ___assert_rtn
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
+ _objc_msgSend$DumpArray:array:count:
+ _objc_msgSend$DumpOutputHcus:
+ _objc_msgSend$DumpPiecewiseLinearCurveV3:curve:
+ _objc_msgSend$bytes
+ _objc_msgSend$shouldEnhanceWidth:height:destinationWidth:destinationHeight:
+ _objc_release_x22
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _snprintf
CStrings:
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
+ " [1.41.0]     %s : ERROR: Not supported, _productType = %d\n"
+ " [1.41.0]     %s : aseControlUnit->hcuCount %d, aseControlUnit->hcuSize %d, \n"
+ " [1.41.0]     %s : aseProcessingType=%d [%s], width=%d, height=%d, strength=%f\n"
+ " [1.41.0]     %s : aseProcessingType=%d [%s], width=%d, height=%d, strength=%f, destinationWidth=%d, destinationHeight=%d\n"
+ " [1.41.0]     %s: %09llx:  %08x %08x %08x %08x\n"
+ " [1.41.0]     %s: %09llx:  %08x %08x %08x %s\n"
+ " [1.41.0]     %s: %09llx:  %08x %08x %s %s\n"
+ " [1.41.0]     %s: %09llx:  %08x %s %s %s\n"
+ " [1.41.0]     %s: %09llx:  %s %08x %08x %08x\n"
+ " [1.41.0]     %s: %09llx:  %s %08x %s %s\n"
+ " [1.41.0]     %s: %09llx:  %s %s %s %08x\n"
+ " [1.41.0]     %s: -----------------------------------------------\n"
+ " [1.41.0]     %s: ERROR: Unsupported HCU!  hcuType = 0x%x ('%c%c%c%c')\n"
+ " [1.41.0]     %s: _enabledHcus = 0x%x, hideHcu = 0x%x (%d)\n"
+ " [1.41.0]     %s: angleDetectV3Hcu: signChangeThreshold = %u, hfeqThresh2 = %u\n"
+ " [1.41.0]     %s: blendConfigV3Hcu: BlendLogicSkinToneProtection: toneThresh = %u, toneEdgeThresh = %u, toneMaxThresh = %d, toneFactor = %d\n"
+ " [1.41.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveEbeFactor]:\n"
+ " [1.41.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveLuma]:\n"
+ " [1.41.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveW_EBE]:\n"
+ " [1.41.0]     %s: blendConfigV3Hcu: blendCurve[kASEBlendCurveW_Peaking]:\n"
+ " [1.41.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveEbeV3]:\n"
+ " [1.41.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1NegV3]:\n"
+ " [1.41.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1PosV3]:\n"
+ " [1.41.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf2V3]:\n"
+ " [1.41.0]     %s: ebeConfigV3Hcu: EBECurve[kASEEBECurveHf3V3]:\n"
+ " [1.41.0]     %s: ebeConfigV3Hcu: ebeParams: { sdaPenalty1 = %d, sdaPenalty2 = %d, dFfactor = %d }\n"
+ " [1.41.0]     %s: entryHeader[%d]: hcuSize = %d, hcuType = 0x%x ('%c%c%c%c')\n"
+ " [1.41.0]     %s: hcuHeader: hcuCount = %d, hcuSize = %d\n"
+ " [1.41.0]     %s: noiseMeterV3Hcu: NoiseMeter: NoiseMeterConfig: sizeX = %u, sizeY = %u\n"
+ " [1.41.0]     %s: noiseMeterV3Hcu: NoiseMeter: NoiseMeterGainControl: lut0Gain = %u, lut1Gain = %u, lut2Gain = %u\n"
+ " [1.41.0]     %s: peakingConfigV3Hcu: coreGainCurve:\n"
+ " [1.41.0]     %s: peakingConfigV3Hcu: gainForce = %d\n"
+ " [1.41.0]     %s: peakingConfigV3Hcu: lowAdaptGainCurve:\n"
+ " [1.41.0]     %s: peakingConfigV3Hcu: mediumAdaptGainCurve:\n"
+ " [1.41.0]     %s: peakingConfigV3Hcu: peakingGain: adaptive = %u, gain5_3 = %u, gain7_5 = %u, gain11_9 = %u, gain13_11 = %u,\n"
+ " [1.41.0]     %s: scalingConfigV3Hcu: DDAInitX = %u, DDAInitY = %u, DDAStepX = 0x%x, DDAStepY = 0x%x, DDAInvStepX = 0x%x, DDAInvStepY = 0x%x\n"
+ " [1.41.0]  applying the fix to all HH02012023\n"
+ " [1.41.0] %s\n"
+ " [1.41.0] %s #%d: { %f, %f, %f }\n"
+ " [1.41.0] %s : Unknown device! deviceNameRef: %p, %@, chipID = 0x%llx, productType=%u\n"
+ " [1.41.0] %s : aseMeasurementOutput=%p, aseFrameProcessingControl=%p\n"
+ " [1.41.0] %s : xScaler = %f, yScaler = %f\n"
+ " [1.41.0] %s: Failed to query kMGQDeviceName\n"
+ " [1.41.0] %s: T1 Simulation enabled!\n"
+ " [1.41.0] %s: productType=%d, deviceName = %@, chipID = 0x%llx\n"
+ " [1.41.0] ++  %s : ERROR: Async API Not supported!\n"
+ " [1.41.0] ++  %s : aseControlUnit=%p\n"
+ " [1.41.0] ++  %s : aseControlUnit=%p, strength=%f\n"
+ " [1.41.0] ++  %s : aseMeasurementOutput=%p, aseControlUnit=%p\n"
+ " [1.41.0] ++  %s : aseMeasurementOutput=%p, aseFrameProcessingControl=%p\n"
+ " [1.41.0] ++  %s : aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.41.0] ++  %s : aseMeasurementOutput=%p, pixelControl=%p\n"
+ " [1.41.0] ++  %s : pixelControl=%p\n"
+ " [1.41.0] ++ %s : config=%p\n"
+ " [1.41.0] --  %s \n"
+ " [1.41.0] --  %s : _destinationWidth =%d, _destinationHeight=%d\n"
+ " [1.41.0] --  %s : frame=%ld, retVal=%ld\n"
+ " [1.41.0] --  %s: HCU Cache disabled!\n"
+ " [1.41.0] --  %s: HCU Cache enabled!\n"
+ " [1.41.0] -- %s : frame=%ld, retVal=%ld\n"
+ " [1.41.0] -- %s : instance=%p\n"
+ " [1.41.0] -- %s : retVal=%ld\n"
+ " [1.41.0] Apply iPad control setting V2\n"
+ " [1.41.0] Apply iPad control setting V3\n"
+ " [1.41.0] Apply iPhone control setting V1\n"
+ " [1.41.0] Apply iPhone control setting V2\n"
+ " [1.41.0] Apply iPhone control setting V3\n"
+ " [1.41.0] Assertion: \"!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1414\n"
+ " [1.41.0] Assertion: \"(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1422\n"
+ " [1.41.0] Assertion: \"((void*)0) == config\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 64 goto EXIT\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 44\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 432\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 466\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 578\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 642\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 133\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1427\n"
+ " [1.41.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1482\n"
+ " [1.41.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 196 goto EXIT\n"
+ " [1.41.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 248 goto EXIT\n"
+ " [1.41.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1588 goto EXIT\n"
+ " [1.41.0] Assertion: \"count <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 128\n"
+ " [1.41.0] Assertion: \"input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 185\n"
+ " [1.41.0] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 193\n"
+ " [1.41.0] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 247\n"
+ " [1.41.0] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1603\n"
+ " [1.41.0] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 90\n"
+ " [1.41.0] Assertion: \"isT1OrNewer(productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 508\n"
+ " [1.41.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValueBlend)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 40\n"
+ " [1.41.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValueEbe)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 36\n"
+ " [1.41.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValuePeaking)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 32\n"
+ " [1.41.0] ERROR: Not supported, _asePlatform = %d\n"
+ " [1.41.0] Film grain level 1\n"
+ " [1.41.0] Film grain level 1 LargeRatio\n"
+ " [1.41.0] Film grain level 2\n"
+ " [1.41.0] Film grain level 2 LargeRatio\n"
+ " [1.41.0] Film grain level 3\n"
+ " [1.41.0] Film grain level 3 LargeRatio\n"
+ " [1.41.0] Film grain level heavy\n"
+ " [1.41.0] Film grain level heavy LargeRatio\n"
+ " [1.41.0] Film grain level light\n"
+ " [1.41.0] Film grain level light LargeRatio\n"
+ " [1.41.0] Frame %d:  Curr_FG_level = %d, Curr_badly_coded_FG_level = %d, No_Bad_coded_FilmGrain_score  = %d \n"
+ " [1.41.0] Frame %ld aseMeasurementOutput:\n"
+ " [1.41.0] applying the zoneplate fix to all HH02012023\n"
+ " [1.41.0] aseControlUnit->hcuCount %d, aseControlUnit->hcuSize %d, \n"
+ " [1.41.0] aseFrameProcessingControl->control.size (V1) is %lu\n"
+ " [1.41.0] histOutH1[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutH2[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutHV0[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutHV0[9 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutHV1[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutHV1[7 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutHV2[0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutHV2[0 - 15] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutV1[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] histOutV2[ 0 -  7] = %010d, %010d, %010d, %010d, %010d, %010d, %010d, %010d\n"
+ " [1.41.0] maxAbsH0 = %010d\n"
+ " [1.41.0] maxAbsH1 = %010d\n"
+ " [1.41.0] maxAbsH2 = %010d\n"
+ " [1.41.0] maxAbsHV0 = %010d\n"
+ " [1.41.0] maxAbsHV1 = %010d\n"
+ " [1.41.0] maxAbsHV2 = %010d\n"
+ " [1.41.0] maxAbsV0 = %010d\n"
+ " [1.41.0] maxAbsV1 = %010d\n"
+ " [1.41.0] maxAbsV2 = %010d\n"
+ " [1.41.0] noDS == 1, set mediumAdaptGain = 0, adjust Hfactor\n"
+ " [1.41.0] noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
+ " [1.41.0] pixelControl->asePixelControl.dsEnable=%d, enhancementConfig.{ebeEnable=%d, peakingEnable=%d, chromaEnhanceEnable=%d}\n"
+ " [1.41.0] pixelControl->blendLogicCurve.point0.slope=%f\n"
+ " [1.41.0] pixelControl->blendLogicCurve.point0.x_position=%f\n"
+ " [1.41.0] pixelControl->blendLogicCurve.point0.y_position=%f\n"
+ " [1.41.0] pixelControl->noiseMeter = config.{ sizeX=%d, sizeY=%d }, gainControl.{ lut0Gain= %d, lut1Gain= %d, lut2Gain= %d }\n"
+ " [1.41.0] pixelControl[%p]=%s\n"
+ " [1.41.0] scene_change_detected = %d, ratio_2D_1D is :%d vs %d; H1 is : %d vs %d,  V1 is: %d vs %d;\n"
+ " [1.41.0] sumAbsHV0 = %010d\n"
+ " [1.41.0] sumAbsHV1 = %010d\n"
+ " [1.41.0] sumAbsHV2 = %010d\n"
+ " [1.41.0] totalValid = %010d\n"
+ " [1.41.0] totalValidActivity = %010d\n"
+ " [1.41.0] totalValidValue = %010d\n"
+ "!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
+ "%s { %d"
+ "(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
+ ", %d"
+ ", %d }"
+ "-[ASEProcessingT0 dealloc]"
+ "-[ASEProcessingT0 digitalZoomSelectControl_V2:]"
+ "-[ASEProcessingT0 processPixelWithInput:Output:]"
+ "-[ASEProcessingT0 processPixelWithInput:controlUnit:]"
+ "-[ASEProcessingT0 processPixelWithInput_V1:Output:]"
+ "-[ASEProcessingT0 processPixelWithInput_V2:Output:]"
+ "-[ASEProcessingT0 processPixelWithMeasurement_V1:pixelControl:]"
+ "-[ASEProcessingT0 processPixelWithMeasurement_V2:Output:]"
+ "-[ASEProcessingT0 processPixelWithPixelControl_V1:]"
+ "-[ASEProcessingT0 processPixelWithPixelControl_V2:]"
+ "-[ASEProcessingT1 DumpOutputHcus:]"
+ "-[ASEProcessingT1 dealloc]"
+ "-[ASEProcessingT1 initWithConfig:aseProcessing:productType:]"
+ "-[ASEProcessingT1 populateOutputHcus:]"
+ "-[ASEProcessingT1 processFrameWithInput:callback:]"
+ "-[ASEProcessingT1 processPixelWithInput:controlUnitV3:]"
+ "-[ASEProcessingT1 processPixelWithInput_V3:Output:]"
+ "-[ASEProcessingT1 processPixelWithMeasurement_V3:Output:]"
+ "-[ASEProcessingT1 processPixelWithPixelControl_V3:]"
+ "0"
+ "ASECalculateControlSettingV3.m"
+ "ASEProcessingCache.m"
+ "ASEProcessingT0.m"
+ "ASEProcessingT1.m"
+ "ASEproductType getCurrentProductType(void)"
+ "DumpArray:array:count:"
+ "DumpOutputHcus:"
+ "DumpPiecewiseLinearCurveV3:curve:"
+ "FG_dyn_setting"
+ "InitialSettingVideo"
+ "InitialSettingVideo_V2"
+ "Mix_dyn_setting"
+ "SettingVideo_NFG"
+ "SettingVideo_NFG LargeRatio"
+ "SettingVideo_NFG_LargeRatio_V2"
+ "SettingVideo_NFG_V2"
+ "XXXXXXXX"
+ "bytes"
+ "calculate_control_setting_V3"
+ "com.apple.aseprocessing"
+ "copyArray"
+ "copyPieceWiseCurves"
+ "count <= 16"
+ "createCacheNode"
+ "disableHcuCache"
+ "dumpOutputHcu"
+ "enableT1Sim"
+ "getCurrentProductType"
+ "getMSRBaseAddr"
+ "hideHcu"
+ "iPhone_SettingVideo_NFG_LargeRatio_V2"
+ "iPhone_SettingVideo_NFG_V2"
+ "input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16"
+ "input && input->type == WDT_TYPE_INTERPOLATED"
+ "input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16"
+ "interpolateArray"
+ "interpolatePieceWiseCurves"
+ "isT1OrNewer(_productType)"
+ "isT1OrNewer(productType)"
+ "logLevel"
+ "peakingConfig_FG"
+ "peakingConfig_InitialSettingVideo_V3"
+ "peakingConfig_Mix"
+ "peakingConfig_Video_NFG_LargeRatio_V3"
+ "peakingConfig_Video_NFG_V3"
+ "peakingConfig_iPhone_Video_NFG_LargeRatio_V3"
+ "peakingConfig_iPhone_Video_NFG_V3"
+ "size == sizeof(ASEHcuCacheNodeValueBlend)"
+ "size == sizeof(ASEHcuCacheNodeValueEbe)"
+ "size == sizeof(ASEHcuCacheNodeValuePeaking)"
+ "v24@0:8@16"
+ "v32@0:8r*16^{?=[32{?=fff}]}24"
+ "v36@0:8r*16^I24I32"
+ "void populateScalingConfig(scalingConfigV3Hcu *, float, float, uint32_t *)"

```

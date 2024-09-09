## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

 1.37.0.0.0
-  __TEXT.__text: 0x6fd4
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x288
-  __TEXT.__const: 0x366f4
-  __TEXT.__oslogstring: 0x25c
-  __TEXT.__cstring: 0x333
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__text: 0x12c6c
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x2ac
+  __TEXT.__const: 0x3673c
+  __TEXT.__oslogstring: 0x2b90
+  __TEXT.__cstring: 0xde0
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x6c7
-  __TEXT.__objc_methtype: 0x19f3
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_methname: 0x716
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
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x5e0
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x1a4a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 99
-  Symbols:   692
-  CStrings:  154
+  Functions: 123
+  Symbols:   728
+  CStrings:  383
 
Symbols:
+ _snprintf
+ _objc_retain_x22
+ _objc_retain_x26
+ _objc_retain_x27
+ _CFPreferencesGetAppIntegerValue
+ _objc_retain_x23
+ _objc_retain_x25
+ ___assert_rtn
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_release_x22
+ _objc_retain_x20
CStrings:
+ " [1.37.0] ++  %!s(MISSING) : aseMeasurementOutput=%!p(MISSING), pixelControl=%!p(MISSING)\n"
+ " [1.37.0] -- %!s(MISSING) : retVal=%!l(MISSING)d\n"
+ " [1.37.0] Film grain level 3 LargeRatio\n"
+ " [1.37.0] maxAbsH0 = %!d(MISSING)\n"
+ "interpolateArray"
+ "    %!s(MISSING): peakingConfigV3Hcu: filt5 :"
+ " [1.37.0]     %!s(MISSING): blendConfigV3Hcu: blendCurve[kASEBlendCurveW_EBE]:\n"
+ " [1.37.0]     %!s(MISSING): entryHeader[%!d(MISSING)]: hcuSize = %!d(MISSING), hcuType = 0x%!x(MISSING) ('%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)')\n"
+ "%!s(MISSING) { %!d(MISSING)"
+ "-[ASEProcessingT1 populateOutputHcus:]"
+ "createCacheNode"
+ " [1.37.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValuePeaking)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 32\n"
+ "ASEproductType getCurrentProductType(void)"
+ " [1.37.0] %!s(MISSING)\n"
+ "-[ASEProcessingT1 processPixelWithPixelControl_V3:]"
+ "calculate_control_setting_V3"
+ " [1.37.0] Assertion: \"(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1403\n"
+ " [1.37.0] histOutH1[ 0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "SettingVideo_NFG"
+ "com.apple.aseprocessing"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!x(MISSING) %!s(MISSING) %!s(MISSING) %!s(MISSING)\n"
+ " [1.37.0] Film grain level 1\n"
+ " [1.37.0] sumAbsHV2 = %!d(MISSING)\n"
+ "-[ASEProcessingT0 processPixelWithInput_V2:Output:]"
+ " [1.37.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValueEbe)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 36\n"
+ " [1.37.0] Frame %!d(MISSING):  Curr_FG_level = %!d(MISSING), Curr_badly_coded_FG_level = %!d(MISSING), No_Bad_coded_FilmGrain_score  = %!d(MISSING) \n"
+ " [1.37.0] aseFrameProcessingControl->control.size (V1) is %!l(MISSING)u\n"
+ " [1.37.0] histOutHV1[7 - 15] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "v36@0:8r*16^I24I32"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!s(MISSING) %!s(MISSING) %!s(MISSING) %!x(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): noiseMeterV3Hcu: NoiseMeter: NoiseMeterConfig: sizeX = %!u(MISSING), sizeY = %!u(MISSING)\n"
+ " [1.37.0] Apply iPhone control setting V3\n"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1463\n"
+ " [1.37.0] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 193\n"
+ " [1.37.0] maxAbsH1 = %!d(MISSING)\n"
+ ", %!d(MISSING)"
+ "    %!s(MISSING): peakingConfigV3Hcu:"
+ " [1.37.0] ++  %!s(MISSING) : ERROR: Async API Not supported!\n"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 466\n"
+ " [1.37.0] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1584\n"
+ " [1.37.0] Assertion: \"isT1OrNewer(_productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 88\n"
+ "DumpOutputHcus:"
+ "    %!s(MISSING): blendConfigV3Hcu:"
+ " [1.37.0] %!s(MISSING) : Unknown device! deviceNameRef: %!p(MISSING), %!@(MISSING), chipID = 0x%!l(MISSING)lx\n"
+ " [1.37.0] Assertion: \"((void *)0) == config\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 64 goto EXIT\n"
+ " [1.37.0] Film grain level light LargeRatio\n"
+ "-[ASEProcessingT1 processPixelWithMeasurement_V3:Output:]"
+ "hideHcu"
+ "peakingConfig_Video_NFG_V3"
+ " [1.37.0] %!s(MISSING) : xScaler = %!f(MISSING), yScaler = %!f(MISSING)\n"
+ " [1.37.0] maxAbsH2 = %!d(MISSING)\n"
+ " [1.37.0] totalValidActivity = %!d(MISSING)\n"
+ "copyPieceWiseCurves"
+ " [1.37.0]     %!s(MISSING): ebeConfigV3Hcu: ebeParams: { sdaPenalty1 = %!d(MISSING), sdaPenalty2 = %!d(MISSING), dFfactor = %!d(MISSING) }\n"
+ " [1.37.0] Assertion: \"size == sizeof(ASEHcuCacheNodeValueBlend)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 40\n"
+ "peakingConfig_Mix"
+ " [1.37.0]     %!s(MISSING): ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1PosV3]:\n"
+ " [1.37.0] histOutV2[ 0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "    %!s(MISSING): peakingConfigV3Hcu: filt11 :"
+ "    %!s(MISSING): peakingConfigV3Hcu: filt9 :"
+ " [1.37.0] Apply iPhone control setting V2\n"
+ "input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!x(MISSING) %!x(MISSING) %!x(MISSING) %!s(MISSING)\n"
+ " [1.37.0] noDS == 1, set mediumAdaptGain = 0, adjust Hfactor\n"
+ "v24@0:8@16"
+ " [1.37.0]     %!s(MISSING): blendConfigV3Hcu: BlendLogicSkinToneProtection: toneThresh = %!u(MISSING), toneEdgeThresh = %!u(MISSING), toneMaxThresh = %!d(MISSING), toneFactor = %!d(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): blendConfigV3Hcu: blendCurve[kASEBlendCurveLuma]:\n"
+ " [1.37.0] Assertion: \"!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1395\n"
+ "-[ASEProcessingT0 processPixelWithMeasurement_V2:Output:]"
+ "InitialSettingVideo"
+ " [1.37.0] Film grain level 2\n"
+ " [1.37.0] %!s(MISSING): Failed to query kMGQDeviceName\n"
+ " [1.37.0] Apply iPad control setting V3\n"
+ " [1.37.0] Assertion: \"input && input->type == WDT_TYPE_CONSTANT && input->pointCount <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 185\n"
+ " [1.37.0] sumAbsHV1 = %!d(MISSING)\n"
+ "peakingConfig_FG"
+ "peakingConfig_iPhone_Video_NFG_V3"
+ "    %!s(MISSING): peakingConfigV3Hcu: filt3 :"
+ " [1.37.0]     %!s(MISSING): -----------------------------------------------\n"
+ " [1.37.0]     %!s(MISSING): peakingConfigV3Hcu: mediumAdaptGainCurve:\n"
+ "-[ASEProcessingT1 dealloc]"
+ "v32@0:8r*16^{?=[32{?=fff}]}24"
+ " [1.37.0]     %!s(MISSING): blendConfigV3Hcu: blendCurve[kASEBlendCurveEbeFactor]:\n"
+ " [1.37.0] ++  %!s(MISSING) : aseControlUnit=%!p(MISSING)\n"
+ " [1.37.0] Apply iPhone control setting V1\n"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1408\n"
+ " [1.37.0] Film grain level 1 LargeRatio\n"
+ "!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
+ "iPhone_SettingVideo_NFG_V2"
+ " [1.37.0] histOutHV0[0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ " [1.37.0] pixelControl->asePixelControl.dsEnable=%!d(MISSING), enhancementConfig.{ebeEnable=%!d(MISSING), peakingEnable=%!d(MISSING), chromaEnhanceEnable=%!d(MISSING)}\n"
+ "-[ASEProcessingT0 processPixelWithMeasurement_V1:pixelControl:]"
+ "-[ASEProcessingT1 processPixelWithInput_V3:Output:]"
+ "SettingVideo_NFG_V2"
+ "logLevel"
+ " [1.37.0] --  %!s(MISSING) : _destinationWidth =%!d(MISSING), _destinationHeight=%!d(MISSING)\n"
+ " [1.37.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT1.m\" at line 1569 goto EXIT\n"
+ "    %!s(MISSING): peakingConfigV3Hcu: filt13 :"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!x(MISSING) %!x(MISSING) %!s(MISSING) %!s(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): blendConfigV3Hcu: blendCurve[kASEBlendCurveW_Peaking]:\n"
+ " [1.37.0]     %!s(MISSING): peakingConfigV3Hcu: coreGainCurve:\n"
+ " [1.37.0] --  %!s(MISSING) : frame=%!l(MISSING)d, retVal=%!l(MISSING)d\n"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 642\n"
+ " [1.37.0] --  %!s(MISSING): HCU Cache disabled!\n"
+ "copyArray"
+ "-[ASEProcessingT1 processPixelWithInput:controlUnitV3:]"
+ "SettingVideo_NFG LargeRatio"
+ " [1.37.0]     %!s(MISSING) : aseProcessingType=%!d(MISSING) [%!s(MISSING)], width=%!d(MISSING), height=%!d(MISSING), strength=%!f(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): ebeConfigV3Hcu: EBECurve[kASEEBECurveEbeV3]:\n"
+ " [1.37.0] Assertion: \"input && input->type == WDT_TYPE_INTERPOLATED\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 247\n"
+ " [1.37.0] totalValid = %!d(MISSING)\n"
+ "0"
+ "dumpOutputHcu"
+ " [1.37.0]     %!s(MISSING): ERROR: Unsupported HCU!  hcuType = 0x%!x(MISSING) ('%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)')\n"
+ " [1.37.0]  applying the fix to all HH02012023\n"
+ " [1.37.0] %!s(MISSING): T1 Simulation enabled!\n"
+ " [1.37.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 196 goto EXIT\n"
+ " [1.37.0] Frame %!l(MISSING)d aseMeasurementOutput:\n"
+ " [1.37.0] scene_change_detected = %!d(MISSING), ratio_2D_1D is :%!d(MISSING) vs %!d(MISSING); H1 is : %!d(MISSING) vs %!d(MISSING),  V1 is: %!d(MISSING) vs %!d(MISSING);\n"
+ "(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))"
+ "void populateScalingConfig(scalingConfigV3Hcu *, float, float, uint32_t *)"
+ "    %!s(MISSING): ebeConfigV3Hcu:"
+ " [1.37.0] ++  %!s(MISSING) : aseMeasurementOutput=%!p(MISSING), completionCallback=%!p(MISSING)\n"
+ " [1.37.0] ++  %!s(MISSING) : pixelControl=%!p(MISSING)\n"
+ " [1.37.0] Film grain level 3\n"
+ "-[ASEProcessingT1 initWithConfig:aseProcessing:productType:]"
+ "-[ASEProcessingT1 processFrameWithInput:callback:]"
+ "disableHcuCache"
+ "enableT1Sim"
+ "getCurrentProductType"
+ "    %!s(MISSING): ebeConfigV3Hcu: lowPass :"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingCache.m\" at line 44\n"
+ "DumpPiecewiseLinearCurveV3:curve:"
+ "-[ASEProcessingT0 processPixelWithInput:Output:]"
+ " [1.37.0]     %!s(MISSING): ebeConfigV3Hcu: EBECurve[kASEEBECurveHf2V3]:\n"
+ " [1.37.0]     %!s(MISSING): peakingConfigV3Hcu: gainForce = %!d(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): peakingConfigV3Hcu: lowAdaptGainCurve:\n"
+ "-[ASEProcessingT1 DumpOutputHcus:]"
+ " [1.37.0]     %!s(MISSING) : ERROR: Not supported, _productType = %!d(MISSING)\n"
+ " [1.37.0] %!s(MISSING): productType=%!d(MISSING), deviceName = %!@(MISSING), chipID = 0x%!l(MISSING)lx\n"
+ " [1.37.0]     %!s(MISSING) : aseProcessingType=%!d(MISSING) [%!s(MISSING)], width=%!d(MISSING), height=%!d(MISSING), strength=%!f(MISSING), destinationWidth=%!d(MISSING), destinationHeight=%!d(MISSING)\n"
+ " [1.37.0] ++ %!s(MISSING) : config=%!p(MISSING)\n"
+ " [1.37.0] Film grain level light\n"
+ " [1.37.0] histOutHV2[0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ " [1.37.0] maxAbsV2 = %!d(MISSING)\n"
+ "-[ASEProcessingT0 processPixelWithPixelControl_V1:]"
+ " [1.37.0]     %!s(MISSING): ebeConfigV3Hcu: EBECurve[kASEEBECurveHf1NegV3]:\n"
+ " [1.37.0] Assertion: \"isT1OrNewer(productType)\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 508\n"
+ " [1.37.0] aseControlUnit->hcuCount %!d(MISSING), aseControlUnit->hcuSize %!d(MISSING), \n"
+ " [1.37.0] maxAbsHV2 = %!d(MISSING)\n"
+ " [1.37.0] pixelControl->noiseMeter = config.{ sizeX=%!d(MISSING), sizeY=%!d(MISSING) }, gainControl.{ lut0Gain= %!d(MISSING), lut1Gain= %!d(MISSING), lut2Gain= %!d(MISSING) }\n"
+ ", %!d(MISSING) }"
+ "ASECalculateControlSettingV3.m"
+ " [1.37.0] Assertion: \"count <= 16\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASECalculateControlSettingV3.m\" at line 128\n"
+ " [1.37.0] maxAbsHV1 = %!d(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): hcuHeader: hcuCount = %!d(MISSING), hcuSize = %!d(MISSING)\n"
+ " [1.37.0] ++  %!s(MISSING) : aseMeasurementOutput=%!p(MISSING), aseControlUnit=%!p(MISSING)\n"
+ " [1.37.0] maxAbsHV0 = %!d(MISSING)\n"
+ " [1.37.0] totalValidValue = %!d(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): noiseMeterV3Hcu: NoiseMeter: NoiseMeterGainControl: lut0Gain = %!u(MISSING), lut1Gain = %!u(MISSING), lut2Gain = %!u(MISSING)\n"
+ "-[ASEProcessingT0 processPixelWithPixelControl_V2:]"
+ " [1.37.0]     %!s(MISSING): ebeConfigV3Hcu: EBECurve[kASEEBECurveHf3V3]:\n"
+ " [1.37.0] applying the zoneplate fix to all HH02012023\n"
+ " [1.37.0] histOutH2[ 0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ " [1.37.0] maxAbsV0 = %!d(MISSING)\n"
+ "count <= 16"
+ "FG_dyn_setting"
+ " [1.37.0] pixelControl->blendLogicCurve.point0.x_position=%!f(MISSING)\n"
+ "InitialSettingVideo_V2"
+ "    %!s(MISSING): ebeConfigV3Hcu: weightLut :"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!s(MISSING) %!x(MISSING) %!x(MISSING) %!x(MISSING)\n"
+ " [1.37.0] histOutHV2[0 - 15] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "bytes"
+ " [1.37.0] ++  %!s(MISSING) : aseControlUnit=%!p(MISSING), strength=%!f(MISSING)\n"
+ " [1.37.0] Film grain level heavy\n"
+ "    %!s(MISSING): peakingConfigV3Hcu: filt7 :"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 432\n"
+ " [1.37.0] histOutHV0[9 - 15] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "isT1OrNewer(_productType)"
+ " [1.37.0]     %!s(MISSING): scalingConfigV3Hcu: DDAInitX = %!u(MISSING), DDAInitY = %!u(MISSING), DDAStepX = 0x%!x(MISSING), DDAStepY = 0x%!x(MISSING), DDAInvStepX = 0x%!x(MISSING), DDAInvStepY = 0x%!x(MISSING)\n"
+ " [1.37.0] pixelControl->blendLogicCurve.point0.slope=%!f(MISSING)\n"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!x(MISSING) %!x(MISSING) %!x(MISSING) %!x(MISSING)\n"
+ " [1.37.0] pixelControl[%!p(MISSING)]=%!s(MISSING)\n"
+ "Mix_dyn_setting"
+ "XXXXXXXX"
+ " [1.37.0] Assertion: \"0\" warned in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 578\n"
+ " [1.37.0] -- %!s(MISSING) : instance=%!p(MISSING)\n"
+ "size == sizeof(ASEHcuCacheNodeValueBlend)"
+ " [1.37.0] ++  %!s(MISSING) : aseMeasurementOutput=%!p(MISSING), aseFrameProcessingControl=%!p(MISSING)\n"
+ " [1.37.0] ERROR: Not supported, _asePlatform = %!d(MISSING)\n"
+ " [1.37.0] histOutHV1[0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "ASEProcessingCache.m"
+ " [1.37.0]     %!s(MISSING): peakingConfigV3Hcu: peakingGain: adaptive = %!u(MISSING), gain5_3 = %!u(MISSING), gain7_5 = %!u(MISSING), gain11_9 = %!u(MISSING), gain13_11 = %!u(MISSING),\n"
+ " [1.37.0] --  %!s(MISSING): HCU Cache enabled!\n"
+ " [1.37.0] maxAbsV1 = %!d(MISSING)\n"
+ "-[ASEProcessingT0 processPixelWithInput:controlUnit:]"
+ "ASEProcessingT1.m"
+ "SettingVideo_NFG_LargeRatio_V2"
+ " [1.37.0]     %!s(MISSING): %!l(MISSING)lx:  %!s(MISSING) %!x(MISSING) %!s(MISSING) %!s(MISSING)\n"
+ " [1.37.0] --  %!s(MISSING) \n"
+ " [1.37.0] Apply iPad control setting V2\n"
+ "-[ASEProcessingT0 dealloc]"
+ "size == sizeof(ASEHcuCacheNodeValuePeaking)"
+ " [1.37.0] %!s(MISSING) #%!d(MISSING): { %!f(MISSING), %!f(MISSING), %!f(MISSING) }\n"
+ " [1.37.0] histOutV1[ 0 -  7] = %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING), %!d(MISSING)\n"
+ "-[ASEProcessingT0 digitalZoomSelectControl_V2:]"
+ "DumpArray:array:count:"
+ "peakingConfig_Video_NFG_LargeRatio_V3"
+ " [1.37.0] %!s(MISSING) : aseMeasurementOutput=%!p(MISSING), aseFrameProcessingControl=%!p(MISSING)\n"
+ " [1.37.0] -- %!s(MISSING) : frame=%!l(MISSING)d, retVal=%!l(MISSING)d\n"
+ " [1.37.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/Library/Caches/com.apple.xbs/Sources/ASEFramework/ASEProcessingT0.m\" at line 248 goto EXIT\n"
+ " [1.37.0] Film grain level heavy LargeRatio\n"
+ "peakingConfig_InitialSettingVideo_V3"
+ "peakingConfig_iPhone_Video_NFG_LargeRatio_V3"
+ " [1.37.0]     %!s(MISSING) : aseControlUnit->hcuCount %!d(MISSING), aseControlUnit->hcuSize %!d(MISSING), \n"
+ " [1.37.0]     %!s(MISSING): _enabledHcus = 0x%!x(MISSING), hideHcu = 0x%!x(MISSING) (%!d(MISSING))\n"
+ "size == sizeof(ASEHcuCacheNodeValueEbe)"
+ " [1.37.0]     %!s(MISSING): angleDetectV3Hcu: signChangeThreshold = %!u(MISSING), hfeqThresh2 = %!u(MISSING)\n"
+ "-[ASEProcessingT0 processPixelWithInput_V1:Output:]"
+ "ASEProcessingT0.m"
+ " [1.37.0] Film grain level 2 LargeRatio\n"
+ " [1.37.0] noiseMeter = config.{ sizeX=%!d(MISSING), sizeY=%!d(MISSING) }, gainControl.{ lut0Gain= %!d(MISSING), lut1Gain= %!d(MISSING), lut2Gain= %!d(MISSING) }\n"
+ " [1.37.0] pixelControl->blendLogicCurve.point0.y_position=%!f(MISSING)\n"
+ "interpolatePieceWiseCurves"
+ "isT1OrNewer(productType)"
+ " [1.37.0] sumAbsHV0 = %!d(MISSING)\n"
+ "iPhone_SettingVideo_NFG_LargeRatio_V2"
+ "input && input->type == WDT_TYPE_INTERPOLATED"
+ "input && input->type == WDT_TYPE_INTERPOLATED && input->pointCount <= 16"

```

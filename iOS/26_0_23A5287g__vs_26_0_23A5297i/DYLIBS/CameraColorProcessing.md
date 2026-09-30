## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-659.0.0.0.4
-  __TEXT.__text: 0x83028
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0x1d6c
-  __TEXT.__const: 0x694c
-  __TEXT.__gcc_except_tab: 0x4854
-  __TEXT.__cstring: 0x7d96
+661.0.0.0.3
+  __TEXT.__text: 0x86e6c
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_methlist: 0x1dbc
+  __TEXT.__const: 0x6bdc
+  __TEXT.__gcc_except_tab: 0x4ebc
+  __TEXT.__cstring: 0x80a9
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__oslogstring: 0xaf11
-  __TEXT.__unwind_info: 0xb70
+  __TEXT.__oslogstring: 0xb0e5
+  __TEXT.__unwind_info: 0xba0
   __TEXT.__eh_frame: 0x90
-  __TEXT.__objc_classname: 0x43d
-  __TEXT.__objc_methname: 0x491a
-  __TEXT.__objc_methtype: 0xc248
-  __TEXT.__objc_stubs: 0x2bc0
+  __TEXT.__objc_classname: 0x454
+  __TEXT.__objc_methname: 0x4bad
+  __TEXT.__objc_methtype: 0xc8d2
+  __TEXT.__objc_stubs: 0x2c80
   __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc8
+  __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x3e0
-  __AUTH_CONST.__const: 0x430
-  __AUTH_CONST.__cfstring: 0x2840
-  __AUTH_CONST.__objc_const: 0x4948
-  __AUTH_CONST.__objc_intobj: 0x3f0
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__const: 0x3f8
+  __AUTH_CONST.__cfstring: 0x28a0
+  __AUTH_CONST.__objc_const: 0x49d8
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2d0
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x450
-  __DATA.__data: 0xfe8
+  __DATA.__data: 0x1070
   __DATA.__common: 0x420
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0x178
-  __DATA_DIRTY.__bss: 0x748
+  __DATA_DIRTY.__data: 0x15c
+  __DATA_DIRTY.__bss: 0x740
   __DATA_DIRTY.__common: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 160D37DE-7AF3-350E-8438-49BB6233DAEB
-  Functions: 995
-  Symbols:   3534
-  CStrings:  3029
+  UUID: C58CD333-8ED3-3340-8DCE-6928317F8B3A
+  Functions: 1005
+  Symbols:   3555
+  CStrings:  3060
 
Symbols:
+ +[AWBAlgorithm awbSensorCalibrationsLoad:idealColorCalibrations:to:]
+ +[AWBAlgorithm calculateNonComboGainsFromComboGains:awbAlgorithm:gains:]
+ +[AWBAlgorithm calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:]
+ +[AWBAlgorithm calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:]
+ +[AWBAlgorithm encodeSetFileIDForModuleConfig:setFileID:]
+ +[AWBAlgorithm getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:platformID:]
+ +[AWBAlgorithm populateSlaveConfigWithModuleConfigIfColorMatchingModelExistsInPrimaryAWBConfig:secondaryAWBConfig:secondaryIdealColorCals:secondaryAbsoluteColorCals:secondarySetFileID:secondarySensorConfig:]
+ +[AWBProcessor calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:]
+ +[AWBProcessor calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:]
+ +[FWPlatformIDUtilities getFWPlatformID]
+ +[FWPlatformIDUtilities getFWPlatformID].cold.1
+ -[AWBAlgorithm initWithMetalContext:platformID:]
+ -[AWBProcessor internalSetupWithFWPlatformID:]
+ -[AWBProcessor internalSetupWithFWPlatformID:].cold.1
+ -[AWBProcessor internalSetupWithFWPlatformID:].cold.2
+ -[AWBProcessor internalSetupWithFWPlatformID:].cold.3
+ -[AWBProcessor internalSetupWithFWPlatformID:].cold.4
+ -[AWBProcessor internalSetupWithFWPlatformID:].cold.5
+ -[AWBProcessor internalSetupWithFWPlatformID:].cold.6
+ GCC_except_table32
+ GCC_except_table33
+ _OBJC_CLASS_$_FWPlatformIDUtilities
+ _OBJC_METACLASS_$_FWPlatformIDUtilities
+ __OBJC_CLASS_RO_$_FWPlatformIDUtilities
+ __OBJC_METACLASS_RO_$_FWPlatformIDUtilities
+ __ZN10CAWBAFEH1420ProcessMatchSlaveAWBEPjhP21SensorConfigAWBParamsP20sSlaveCameraAWBParamP22sCIspMetaDataSharedAWBb
+ __ZN10CAWBAFEH1443SetSlaveCameraListColorMatchingLatticeModelEjPK66sCIspCmdAppleChAWBSlaveCameraListColorMatchingLatticeModelSetEntry
+ __ZN10CAWBAFEH1443calculateSlaveCameraWBGainfromMatchingModelEPKjPfjPK35_sSlaveCameraListColorMatchingModelji
+ __ZN10CAWBAFEH14C1EPKcP7CObjecti
+ __ZN10CAWBAFEH14C2EPKcP7CObjecti
+ __ZN30CAWBAFEPhotometerAssistPenroseC1Ebi
+ __ZN30CAWBAFEPhotometerAssistPenroseC2Ebi
+ __ZN7CAWBAFE20GetCCTFromColorRatioEf
+ __ZN7CAWBAFE20SetFileVersionUpdateEhjj
+ __ZN7CAWBAFE30calBilinearInterpolationWeightEtffP19bilinearWeightIndex
+ __ZN7CAWBAFEC2EPKcP7CObjecti
+ ___getFigCaptureGetModelSpecificNameSymbolLoc_block_invoke
+ ___getFigCaptureGetModelSpecificNameSymbolLoc_block_invoke.cold.1
+ _getFigCaptureGetModelSpecificNameSymbolLoc.ptr
+ _objc_msgSend$awbSensorCalibrationsLoad:idealColorCalibrations:to:
+ _objc_msgSend$calculateNonComboGainsFromComboGains:awbAlgorithm:gains:
+ _objc_msgSend$calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:
+ _objc_msgSend$calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:
+ _objc_msgSend$cmi_simdFloat4ValueForKey:defaultValue:found:
+ _objc_msgSend$getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:platformID:
+ _objc_msgSend$initWithMetalContext:platformID:
+ _objc_msgSend$internalSetupWithFWPlatformID:
+ _objc_msgSend$populateSlaveConfigWithModuleConfigIfColorMatchingModelExistsInPrimaryAWBConfig:secondaryAWBConfig:secondaryIdealColorCals:secondaryAbsoluteColorCals:secondarySetFileID:secondarySensorConfig:
- +[AWBAlgorithm calculateSTRBKeyFromWideCamera:moduleConfig:]
- +[AWBProcessor calculateSTRBKeyFromWideCamera:moduleConfig:]
- -[AWBAlgorithm encodeSetFileIDForModuleConfig:setFileID:]
- -[AWBAlgorithm initFWPlatformID]
- -[AWBAlgorithm initWithMetalContext:]
- -[AWBProcessor setup].cold.1
- -[AWBProcessor setup].cold.2
- -[AWBProcessor setup].cold.3
- -[AWBProcessor setup].cold.4
- -[AWBProcessor setup].cold.5
- -[AWBProcessor setup].cold.6
- GCC_except_table45
- __ZGVZN12CEnvironment8InstanceEvE8instance
- __ZL21audit_stringCMCapture
- __ZN10CAWBAFEH1420ProcessMatchSlaveAWBEPjhP21SensorConfigAWBParamsP20sSlaveCameraAWBParamP22sCIspMetaDataSharedAWB
- __ZN10CAWBAFEH14C1EPKcP7CObject
- __ZN10CAWBAFEH14C2EPKcP7CObject
- __ZN12CEnvironment8InstanceEv
- __ZN12CEnvironmentC1Ev
- __ZN12CEnvironmentD0Ev
- __ZN12CEnvironmentD1Ev
- __ZN30CAWBAFEPhotometerAssistPenroseC1Eb
- __ZN30CAWBAFEPhotometerAssistPenroseC2Ev
- __ZN7CAWBAFEC2EPKcP7CObject
- __ZN7CObjectC2Ev
- __ZTI12CEnvironment
- __ZTS12CEnvironment
- __ZTV12CEnvironment
- __ZZL20CMCaptureLibraryCorePPcE16frameworkLibrary.0
- __ZZL42getFigCaptureGetModelSpecificNameSymbolLocvE3ptr.0
- __ZZN12CEnvironment8InstanceEvE8instance
- ____ZL20CMCaptureLibraryCorePPc_block_invoke
- ____ZL42getFigCaptureGetModelSpecificNameSymbolLocv_block_invoke
- ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
- ___cxa_guard_abort
- ___cxa_guard_acquire
- ___cxa_guard_release
- _objc_msgSend$calculateSTRBKeyFromWideCamera:moduleConfig:
- _objc_msgSend$firstObject
- _objc_msgSend$initFWPlatformID
CStrings:
+ "+[AWBAlgorithm awbSensorCalibrationsLoad:idealColorCalibrations:to:]"
+ "+[AWBAlgorithm calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:]"
+ "+[AWBAlgorithm calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:]"
+ "+[AWBAlgorithm encodeSetFileIDForModuleConfig:setFileID:]"
+ "+[AWBAlgorithm getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:platformID:]"
+ "+[AWBAlgorithm populateSlaveConfigWithModuleConfigIfColorMatchingModelExistsInPrimaryAWBConfig:secondaryAWBConfig:secondaryIdealColorCals:secondaryAbsoluteColorCals:secondarySetFileID:secondarySensorConfig:]"
+ "+[FWPlatformIDUtilities getFWPlatformID]"
+ "-[AWBAlgorithm initWithMetalContext:platformID:]"
+ "-[AWBProcessor internalSetupWithFWPlatformID:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CameraColorProcessing/CameraColorProcessing/Sources/AWBAlgorithm/FWPlatformIDUtilities.m %s: Unsupported device: %@ (this may be overridden with defaults write com.apple.coremedia softisp.awb.modelname <model>)"
+ "<<<< AWBAlgorithm >>>> %s: No ColorMatchingLatticeModel entries found in ModuleConfig"
+ "<<<< AWBAlgorithm >>>> %s: Value for [%@][%@] not found in %@, using default value"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: M2S %hhu %u"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: M2S Lattice LogAWBGain %f %f %f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: M2S Linear %f %f %f"
+ "@28@0:8@16i24"
+ "ColorMatchingLatticeModel"
+ "FWPlatformIDUtilities"
+ "FWPlatformIDUtilities.m"
+ "Failed to initialize CAWBAFE object"
+ "Failed to initialize secondary sensor configuration object"
+ "NSString *soft_FigCaptureGetModelSpecificName(void)"
+ "Secondary sensor set file ID not valid."
+ "Secondary set file ID not found in color matching models"
+ "awbAlgorithmSWide->InitialReset()"
+ "awbAlgorithmWide->InitialReset()"
+ "awbSensorCalibrationsLoad:idealColorCalibrations:to:"
+ "calculateNonComboGainsFromComboGains:awbAlgorithm:gains:"
+ "calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:"
+ "calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:"
+ "calculateSlaveCameraWBGainfromMatchingModel"
+ "cmi_simdFloat4ValueForKey:defaultValue:found:"
+ "darkSceneLuxThreshold"
+ "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:platformID:"
+ "i20@0:8i16"
+ "i40@0:8^{?=i(?={?=ffff}{?=ff}{?=ff})}16@24@32"
+ "i40@0:8r^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]ff}BBf}16r^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}32"
+ "i48@0:8r^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]ff}BBf}32^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}40"
+ "i56@0:8^{?=i(?={?=ffff}{?=ff}{?=ff})}16@24@32@40@48"
+ "i60@0:8@16@24@32@40I48^{SensorConfigAWBParams={sCSensorCalIdeal=SSSS}{sCSensorCalAbs=SSSS}{sCSensorCalBias=SSSS}{sCSensorCalGain=SSSS}II{sCameraColorConfig=[9s][9s][2s][2I]S[6[9s]][8[3S]][30[2s]]}}52"
+ "i68@0:8@16@24@32@40@48@56i64"
+ "initWithMetalContext:platformID:"
+ "internalSetupWithFWPlatformID:"
+ "latticeModelLUTGridSize"
+ "populateSlaveConfigWithModuleConfigIfColorMatchingModelExistsInPrimaryAWBConfig:secondaryAWBConfig:secondaryIdealColorCals:secondaryAbsoluteColorCals:secondarySetFileID:secondarySensorConfig:"
+ "secondarySetFileIDFoundInColorMatchingModels > 0"
+ "setFileIDSWide != 0"
+ "setFileIDWide != 0"
+ "v40@0:8[3I]16^{CAWBAFEH14=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSfffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}CBI[4{_sSlaveCameraListColorMatchingModel=Ii{?=iii}{?=iii}{?=C[2[81f]]}}][32f]}24[3I]32"
+ "wbGainMatchingModel"
+ "{sLtmComputeInput_SOFTISP=\"ltmComputeInput\"{sLtmComputeInput=\"rotationMagnitude\"f\"rotationMagnitudeDeltaIIR\"f\"rotationMagnitudeDeltaFiltered\"f\"thumbHistBlendingWeight\"f\"localHist\"[12288f]\"averageLocalHist\"[256f]\"globalHist\"[1024f]\"globalHist2\"[64f]\"tMaxArray\"[48f]\"nLumArray\"[48f]\"thumbnailHist\"[256f]\"thumbnailHistEV0\"[256f]\"thumbnailLumaHist\"[256f]\"faceWeightForTone\"[48f]\"fmapHFF\"[192f]\"faceWeightForHistBlend\"[48f]\"faceFraction\"f\"sceneLux\"f\"bin0Ratio\"f\"pixelCountRatio\"f\"exposureRatio\"f\"exposureBias\"f\"preBiasExposureRatio\"f\"faceExposureRatio\"f\"darkExposureRatio\"f\"luminanceRatio\"f\"flareScale\"f\"rGainRatio\"f\"bGainRatio\"f\"gamutSizeIndex\"S\"ccm\"[9f]\"ccmWeights\"[192f]\"ccmMixFactor\"f\"eit\"f\"darkEit\"f\"ltcGridScaleLogLumaThumb\"[192f]\"blendingMaskInputTh\"[768f]\"CBBrightMap\"[192f]\"CBLowlightDampWeight\"f\"faceBiasScaler\"f}\"LTMHazeCorrectionOff\"B\"useBt709\"B\"totalGain\"f}"
+ "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"bSoftGainOnly\"B\"gammaCurve\"i\"faceLTMVer\"C\"CBVer\"C\"updateMixLUT\"B}\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"darkSceneLuxThreshold\"\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"channel\"C\"enableHiResLocalHistogram\"B}"
+ "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"gammaCurve\"i\"updateMixLUT\"B\"levelSmoothNumPasses\"i\"levelSmoothCenterWeight\"f}\"channel\"C\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"darkSceneLuxThreshold\"\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B}"
+ "{sRefDriverInputs_SOFTISP=\"HROn\"B\"hrGainDownRatio\"S\"exposureTime\"I\"gainAnal\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigi\"I\"hardIspDGain\"f\"softIspDGain\"f\"expBias\"S\"realizedExpBias\"S\"hdrRatio\"S\"ev0Ratio\"S\"overflowDGain\"I\"faceExpRatioFiltered\"f\"panoExpRatio\"S\"bLTMSingleFrameMode\"B\"ltmProcMode\"C\"bracketingMode\"C\"bracketingExpRatio\"I\"gainDigiSensor\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"luxLevel\"f\"useSpatialCCM\"B\"channel\"C\"flashStatus\"B\"isHLGMode\"B\"LTMGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"localHistGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"flashMixPercentage\"[512S]\"flashProjMixWeighting\"f\"tileStatsRegion\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"ccm\"{sAWBColorCorrectionMatrix_local=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"isLEDMainFlashforAWB\"B\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsSkinOnly\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"fdAWBChistMixFactor\"I\"awbColorspace\"C\"faceInfo\"{sFaceInfo_SOFTISP=\"rectArray\"[10{sCIspFDRect=\"x\"i\"y\"i\"width\"I\"height\"I}]\"primaryFaceIndex\"I\"numFaces\"I}\"forceDisableFaceBoost\"B\"gammaCurve\"i\"useHighlightCompression\"B\"useAdaptiveHighlightCompression\"B\"highlightCompressionGain\"f\"isSIFRFrame\"B\"LTMHazeCorrectionOff\"B\"useBt709\"B\"useHazeCorrection\"B\"hazeCorrection\"\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"darkSceneLuxThreshold\"\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"faceBiasScaler\"f\"faceLTMVer\"C\"CBVer\"C}"
- "+[AWBAlgorithm calculateSTRBKeyFromWideCamera:moduleConfig:]"
- "+[AWBAlgorithm getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:]"
- "-[AWBAlgorithm encodeSetFileIDForModuleConfig:setFileID:]"
- "-[AWBAlgorithm initFWPlatformID]"
- "-[AWBAlgorithm initWithMetalContext:]"
- "-[AWBProcessor setup]"
- "<<<< AWBAlgorithm >>>> %s: Unsupported device: %@ (this may be overridden with defaults write com.apple.coremedia softisp.awb.modelname <model>)"
- "Failed to get ColorMatchingModelDictEntry"
- "Failed to get bgGainColorMatchingModel"
- "Failed to get rgGainColorMatchingModel"
- "NSString *soft_FigCaptureGetModelSpecificName()"
- "SlaveCamID"
- "bgGainColorMatchingModel"
- "calculateSTRBKeyFromWideCamera:moduleConfig:"
- "colorMatchingModelDictEntry"
- "firstObject"
- "i32@0:8^{?=i(?={?=ffff}{?=ff}{?=ff})}16@24"
- "i40@0:8r^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]ff}BB}16r^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}32"
- "i48@0:8r^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]ff}BB}32^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}40"
- "initFWPlatformID"
- "rgGainColorMatchingModel"
- "void *CMCaptureLibrary()"
- "{sLtmComputeInput_SOFTISP=\"ltmComputeInput\"{sLtmComputeInput=\"rotationMagnitude\"f\"rotationMagnitudeDeltaIIR\"f\"rotationMagnitudeDeltaFiltered\"f\"thumbHistBlendingWeight\"f\"localHist\"[12288f]\"averageLocalHist\"[256f]\"globalHist\"[1024f]\"globalHist2\"[64f]\"tMaxArray\"[48f]\"nLumArray\"[48f]\"thumbnailHist\"[256f]\"thumbnailHistEV0\"[256f]\"thumbnailLumaHist\"[256f]\"faceWeightForTone\"[48f]\"fmapHFF\"[192f]\"faceWeightForHistBlend\"[48f]\"faceFraction\"f\"sceneLux\"f\"bin0Ratio\"f\"pixelCountRatio\"f\"exposureRatio\"f\"exposureBias\"f\"preBiasExposureRatio\"f\"faceExposureRatio\"f\"darkExposureRatio\"f\"luminanceRatio\"f\"flareScale\"f\"rGainRatio\"f\"bGainRatio\"f\"gamutSizeIndex\"S\"ccm\"[9f]\"ccmWeights\"[192f]\"ccmMixFactor\"f\"eit\"f\"darkEit\"f\"ltcGridScaleLogLumaThumb\"[192f]\"blendingMaskInputTh\"[768f]\"CBBrightMap\"[192f]\"CBLowlightDampWeight\"f\"faceBiasScaler\"f}\"LTMHazeCorrectionOff\"B\"useBt709\"B}"
- "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"bSoftGainOnly\"B\"gammaCurve\"i\"faceLTMVer\"C\"CBVer\"C\"updateMixLUT\"B}\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"channel\"C\"enableHiResLocalHistogram\"B}"
- "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"gammaCurve\"i\"updateMixLUT\"B\"levelSmoothNumPasses\"i\"levelSmoothCenterWeight\"f}\"channel\"C\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B}"
- "{sRefDriverInputs_SOFTISP=\"HROn\"B\"hrGainDownRatio\"S\"exposureTime\"I\"gainAnal\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigi\"I\"hardIspDGain\"f\"softIspDGain\"f\"expBias\"S\"realizedExpBias\"S\"hdrRatio\"S\"ev0Ratio\"S\"overflowDGain\"I\"faceExpRatioFiltered\"f\"panoExpRatio\"S\"bLTMSingleFrameMode\"B\"ltmProcMode\"C\"bracketingMode\"C\"bracketingExpRatio\"I\"gainDigiSensor\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"luxLevel\"f\"useSpatialCCM\"B\"channel\"C\"flashStatus\"B\"isHLGMode\"B\"LTMGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"localHistGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"flashMixPercentage\"[512S]\"flashProjMixWeighting\"f\"tileStatsRegion\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"ccm\"{sAWBColorCorrectionMatrix_local=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"isLEDMainFlashforAWB\"B\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsSkinOnly\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"fdAWBChistMixFactor\"I\"awbColorspace\"C\"faceInfo\"{sFaceInfo_SOFTISP=\"rectArray\"[10{sCIspFDRect=\"x\"i\"y\"i\"width\"I\"height\"I}]\"primaryFaceIndex\"I\"numFaces\"I}\"forceDisableFaceBoost\"B\"gammaCurve\"i\"useHighlightCompression\"B\"useAdaptiveHighlightCompression\"B\"highlightCompressionGain\"f\"isSIFRFrame\"B\"LTMHazeCorrectionOff\"B\"useBt709\"B\"useHazeCorrection\"B\"hazeCorrection\"\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"faceBiasScaler\"f\"faceLTMVer\"C\"CBVer\"C}"

```

## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-492.60.4.0.1
-  __TEXT.__text: 0x9d4f0
-  __TEXT.__auth_stubs: 0x13e0
+492.60.5.0.1
+  __TEXT.__text: 0xa0b58
+  __TEXT.__auth_stubs: 0x1410
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x230
-  __TEXT.__objc_methlist: 0x98e4
-  __TEXT.__const: 0x21260
-  __TEXT.__cstring: 0x6f41
-  __TEXT.__oslogstring: 0x4908
-  __TEXT.__gcc_except_tab: 0x1844
+  __TEXT.__objc_methlist: 0x9dbc
+  __TEXT.__const: 0x21320
+  __TEXT.__cstring: 0x7127
+  __TEXT.__oslogstring: 0x4a6e
+  __TEXT.__gcc_except_tab: 0x1a78
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2138
-  __TEXT.__objc_classname: 0x1390
-  __TEXT.__objc_methname: 0x1ae79
-  __TEXT.__objc_methtype: 0x57e2
-  __TEXT.__objc_stubs: 0xfc60
-  __DATA_CONST.__got: 0x928
-  __DATA_CONST.__const: 0x970
-  __DATA_CONST.__objc_classlist: 0x578
+  __TEXT.__unwind_info: 0x21d0
+  __TEXT.__objc_classname: 0x144c
+  __TEXT.__objc_methname: 0x1beee
+  __TEXT.__objc_methtype: 0x59e8
+  __TEXT.__objc_stubs: 0x103a0
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__const: 0x998
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5088
+  __DATA_CONST.__objc_selrefs: 0x5320
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x768
   __DATA_CONST.__vfx_script_tbl: 0x50
   __DATA_CONST.__vfx_script_tbx: 0x48
-  __AUTH_CONST.__auth_got: 0xa90
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0x1cbc0
+  __AUTH_CONST.__auth_got: 0xaa8
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__objc_const: 0x1dbc8
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x1e50
+  __AUTH.__objc_data: 0x2080
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x177c
+  __DATA.__objc_ivar: 0x18b4
   __DATA.__data: 0x818
-  __DATA.__bss: 0xe5c
+  __DATA.__bss: 0xe6c
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A34218A-4DBD-39EE-A16F-8348C9FDC3AD
-  Functions: 4060
-  Symbols:   15091
-  CStrings:  7628
+  UUID: FC58F2CA-BA45-3294-9038-1D697EBCF049
+  Functions: 4181
+  Symbols:   15531
+  CStrings:  7873
 
Symbols:
+ +[PTEffectColorTemperatureEstimation RGBFromNormalizedColorTemperature:]
+ -[PTEffectDebugLayer initWithMetalContext:effectRelighting:ringLightEstimation:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:]
+ -[PTEffectDescriptor ringLightConfig]
+ -[PTEffectFaceLuxEstimation .cxx_destruct]
+ -[PTEffectFaceLuxEstimation computeFaceLux:frameIndex:]
+ -[PTEffectFaceLuxEstimation computeFaceLux:frameIndex:].cold.1
+ -[PTEffectFaceLuxEstimation computeFaceLux:frameIndex:].cold.2
+ -[PTEffectFaceLuxEstimation computeFaceLux:frameIndex:].cold.3
+ -[PTEffectFaceLuxEstimation faceLuxLevel:inColorBuffer:frameIndex:]
+ -[PTEffectFaceLuxEstimation faceLuxLevel:inColorBuffer:frameIndex:].cold.1
+ -[PTEffectFaceLuxEstimation faceLuxLevel:inColorBuffer:frameIndex:].cold.2
+ -[PTEffectFaceLuxEstimation faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:]
+ -[PTEffectFaceLuxEstimation faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:].cold.1
+ -[PTEffectFaceLuxEstimation faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:].cold.2
+ -[PTEffectFaceLuxEstimation faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:].cold.3
+ -[PTEffectFaceLuxEstimation initWithMetalContext:humanDetections:effectDescriptor:]
+ -[PTEffectFaceLuxEstimation initWithMetalContext:humanDetections:effectDescriptor:].cold.1
+ -[PTEffectFaceLuxEstimation initWithMetalContext:humanDetections:effectDescriptor:].cold.2
+ -[PTEffectFaceLuxEstimation initWithMetalContext:humanDetections:effectDescriptor:].cold.3
+ -[PTEffectFaceLuxEstimation largestFaceRect]
+ -[PTEffectFaceLuxEstimation lumaFromAEStats:]
+ -[PTEffectFaceLuxEstimation lumaFromAEStats:].cold.1
+ -[PTEffectFaceLuxEstimation rgbFromAEStats:]
+ -[PTEffectFaceLuxEstimation rgbFromAEStats:].cold.1
+ -[PTEffectRenderRequest inRingLightInput]
+ -[PTEffectRenderRequest outRingLightControl]
+ -[PTEffectRenderRequest outRingLightOutput]
+ -[PTEffectRenderRequest ringLightInput]
+ -[PTEffectRenderRequest ringLightOutput]
+ -[PTEffectRenderRequest setInRingLightInput:]
+ -[PTEffectRenderRequest setOutRingLightOutput:]
+ -[PTEffectRenderRequest setRingLightInput:]
+ -[PTEffectRenderRequest setRingLightOutput:]
+ -[PTEffectRenderer isRenderRequiredForRequest:].cold.1
+ -[PTEffectRingLightConfig .cxx_destruct]
+ -[PTEffectRingLightConfig EMAFactorPerFrame]
+ -[PTEffectRingLightConfig deadZoneFactorPerFrame]
+ -[PTEffectRingLightConfig deviceMaxScreenNits]
+ -[PTEffectRingLightConfig deviceScreenSizeInches]
+ -[PTEffectRingLightConfig diagonalScreenSizeInches]
+ -[PTEffectRingLightConfig effectDisableAtLux]
+ -[PTEffectRingLightConfig effectEnableAtLux]
+ -[PTEffectRingLightConfig effectMaxAtLux]
+ -[PTEffectRingLightConfig effectMinAtLux]
+ -[PTEffectRingLightConfig init]
+ -[PTEffectRingLightConfig isEqual:]
+ -[PTEffectRingLightConfig maxNitsMaxEffectStrength]
+ -[PTEffectRingLightConfig maxNitsMinEffectStrength]
+ -[PTEffectRingLightConfig minNitsMaxEffectStrength]
+ -[PTEffectRingLightConfig minNitsMinEffectStrength]
+ -[PTEffectRingLightConfig ringLightAdaptiveSettings]
+ -[PTEffectRingLightConfig setDeadZoneFactorPerFrame:]
+ -[PTEffectRingLightConfig setDeviceMaxScreenNits:]
+ -[PTEffectRingLightConfig setDeviceScreenSizeInches:]
+ -[PTEffectRingLightConfig setDiagonalScreenSizeInches:]
+ -[PTEffectRingLightConfig setEMAFactorPerFrame:]
+ -[PTEffectRingLightConfig setEffectDisableAtLux:]
+ -[PTEffectRingLightConfig setEffectEnableAtLux:]
+ -[PTEffectRingLightConfig setEffectMaxAtLux:]
+ -[PTEffectRingLightConfig setEffectMinAtLux:]
+ -[PTEffectRingLightConfig setMaxNitsMaxEffectStrength:]
+ -[PTEffectRingLightConfig setMaxNitsMinEffectStrength:]
+ -[PTEffectRingLightConfig setMinNitsMaxEffectStrength:]
+ -[PTEffectRingLightConfig setMinNitsMinEffectStrength:]
+ -[PTEffectRingLightConfig setRingLightAdaptiveSettings:]
+ -[PTEffectRingLightEstimation .cxx_destruct]
+ -[PTEffectRingLightEstimation computeNormalizedEffectStrength]
+ -[PTEffectRingLightEstimation detectAdaptiveBehavior:]
+ -[PTEffectRingLightEstimation estimateScreenNits:]
+ -[PTEffectRingLightEstimation faceLuxLevelFiltered]
+ -[PTEffectRingLightEstimation faceLuxLevel]
+ -[PTEffectRingLightEstimation initWithMetalContext:humanDetections:effectDescriptor:]
+ -[PTEffectRingLightEstimation initWithMetalContext:humanDetections:effectDescriptor:].cold.1
+ -[PTEffectRingLightEstimation mapEffectStrengthToRingLightWidth:]
+ -[PTEffectRingLightEstimation mapEffectStrengthToScreenNits:]
+ -[PTEffectRingLightEstimation reset]
+ -[PTEffectRingLightEstimation updateDefaults:]
+ -[PTEffectRingLightEstimation updateDefaults:].cold.1
+ -[PTEffectRingLightEstimation updateFaceLuxLevelFiltered:frameIndex:]
+ -[PTEffectRingLightEstimation updateNitsBasedOnEffectStrength]
+ -[PTEffectRingLightInput .cxx_destruct]
+ -[PTEffectRingLightInput ambientColorEstimationMode]
+ -[PTEffectRingLightInput currentRingLightWidth]
+ -[PTEffectRingLightInput currentScreenNits]
+ -[PTEffectRingLightInput enabled]
+ -[PTEffectRingLightInput init]
+ -[PTEffectRingLightInput ringLightEffectStrength]
+ -[PTEffectRingLightInput ringLightMetadataFile]
+ -[PTEffectRingLightInput ringLightUserColorTemperatureNormalized]
+ -[PTEffectRingLightInput screenNitsEstimationMode]
+ -[PTEffectRingLightInput setAmbientColorEstimationMode:]
+ -[PTEffectRingLightInput setCurrentRingLightWidth:]
+ -[PTEffectRingLightInput setCurrentScreenNits:]
+ -[PTEffectRingLightInput setEnabled:]
+ -[PTEffectRingLightInput setRingLightEffectStrength:]
+ -[PTEffectRingLightInput setRingLightMetadataFile:]
+ -[PTEffectRingLightInput setRingLightUserColorTemperatureNormalized:]
+ -[PTEffectRingLightInput setScreenNitsEstimationMode:]
+ -[PTEffectRingLightInput setUserScreenBrightnessChangeFrom:]
+ -[PTEffectRingLightInput setUserScreenBrightnessChangeTo:]
+ -[PTEffectRingLightInput userScreenBrightnessChangeFrom]
+ -[PTEffectRingLightInput userScreenBrightnessChangeTo]
+ -[PTEffectRingLightOutput .cxx_destruct]
+ -[PTEffectRingLightOutput recommendedColorTemperatureNormalized]
+ -[PTEffectRingLightOutput ringLightAdaptiveSettings]
+ -[PTEffectRingLightOutput ringLightWidth]
+ -[PTEffectRingLightOutput screenNitsFloor]
+ -[PTEffectRingLightOutput setRecommendedColorTemperatureNormalized:]
+ -[PTEffectRingLightOutput setRingLightAdaptiveSettings:]
+ -[PTEffectRingLightOutput setRingLightWidth:]
+ -[PTEffectRingLightOutput setScreenNitsFloor:]
+ -[PTMedianFilter dealloc]
+ -[PTMedianFilter filter:]
+ -[PTMedianFilter initWithFilterWidth:]
+ -[PTMedianFilter reset]
+ GCC_except_table104
+ GCC_except_table31
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table91
+ _CFAutorelease
+ _CGColorCreateGenericRGB
+ _OBJC_CLASS_$_PTEffectColorTemperatureEstimation
+ _OBJC_CLASS_$_PTEffectFaceLuxEstimation
+ _OBJC_CLASS_$_PTEffectRingLightConfig
+ _OBJC_CLASS_$_PTEffectRingLightEstimation
+ _OBJC_CLASS_$_PTEffectRingLightInput
+ _OBJC_CLASS_$_PTEffectRingLightOutput
+ _OBJC_CLASS_$_PTMedianFilter
+ _OBJC_IVAR_$_PTEffectDebugLayer._ringLightEstimation
+ _OBJC_IVAR_$_PTEffectDebugLayer._ringLightEstimationLuxGraph
+ _OBJC_IVAR_$_PTEffectDebugLayer._ringLightEstimationScreenNitsGraph
+ _OBJC_IVAR_$_PTEffectDescriptor._ringLightConfig
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._MSRResize
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._aeThumbnailLuma
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._aeThumbnailRGB
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._chroma
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._faceLuxBuffer
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._faceLuxEstimation
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._faceLuxEstimationFromAEStats
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._humanDetections
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._lastFrameIndexWithFaceRect
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._lowResYUV
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._luma
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._lumaFromAEStats
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._metalContext
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._personSemanticsNetwork
+ _OBJC_IVAR_$_PTEffectFaceLuxEstimation._rgbFromAEStats
+ _OBJC_IVAR_$_PTEffectRenderRequest._ringLightInput
+ _OBJC_IVAR_$_PTEffectRenderRequest._ringLightOutput
+ _OBJC_IVAR_$_PTEffectRenderer._ringLightEstimation
+ _OBJC_IVAR_$_PTEffectRingLightConfig._EMAFactorPerFrame
+ _OBJC_IVAR_$_PTEffectRingLightConfig._deadZoneFactorPerFrame
+ _OBJC_IVAR_$_PTEffectRingLightConfig._deviceMaxScreenNits
+ _OBJC_IVAR_$_PTEffectRingLightConfig._deviceScreenSizeInches
+ _OBJC_IVAR_$_PTEffectRingLightConfig._effectDisableAtLux
+ _OBJC_IVAR_$_PTEffectRingLightConfig._effectEnableAtLux
+ _OBJC_IVAR_$_PTEffectRingLightConfig._effectMaxAtLux
+ _OBJC_IVAR_$_PTEffectRingLightConfig._effectMinAtLux
+ _OBJC_IVAR_$_PTEffectRingLightConfig._maxNitsMaxEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightConfig._maxNitsMinEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightConfig._minNitsMaxEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightConfig._minNitsMinEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightConfig._ringLightAdaptiveSettings
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._EMAFactorPerFrame
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._currentRingLightWidth
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._currentScreenNits
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._deadZoneFactorPerFrame
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectDisableAtLux
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectEnableAtLux
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectEnabled
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectMaxAtLux
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectMinAtLux
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectStrength
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._effectStrengthData
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._faceLuxEstimation
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._faceLuxLevel
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._faceLuxLevelFiltered
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._frameIndex
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._globalLuxLevelFilter
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._lastFrameTimeSecondsScreenNitsEstimation
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._maxNits
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._maxNitsMaxEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._maxNitsMinEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._minNits
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._minNitsMaxEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._minNitsMinEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._ringlightConfig
+ _OBJC_IVAR_$_PTEffectRingLightEstimation._screenNitsDeadzone
+ _OBJC_IVAR_$_PTEffectRingLightInput._ambientColorEstimationMode
+ _OBJC_IVAR_$_PTEffectRingLightInput._currentRingLightWidth
+ _OBJC_IVAR_$_PTEffectRingLightInput._currentScreenNits
+ _OBJC_IVAR_$_PTEffectRingLightInput._enabled
+ _OBJC_IVAR_$_PTEffectRingLightInput._ringLightEffectStrength
+ _OBJC_IVAR_$_PTEffectRingLightInput._ringLightMetadataFile
+ _OBJC_IVAR_$_PTEffectRingLightInput._ringLightUserColorTemperatureNormalized
+ _OBJC_IVAR_$_PTEffectRingLightInput._screenNitsEstimationMode
+ _OBJC_IVAR_$_PTEffectRingLightInput._userScreenBrightnessChangeFrom
+ _OBJC_IVAR_$_PTEffectRingLightInput._userScreenBrightnessChangeTo
+ _OBJC_IVAR_$_PTEffectRingLightOutput._recommendedColorTemperatureNormalized
+ _OBJC_IVAR_$_PTEffectRingLightOutput._ringLightAdaptiveSettings
+ _OBJC_IVAR_$_PTEffectRingLightOutput._ringLightWidth
+ _OBJC_IVAR_$_PTEffectRingLightOutput._screenNitsFloor
+ _OBJC_IVAR_$_PTMedianFilter._data
+ _OBJC_IVAR_$_PTMedianFilter._dataSorted
+ _OBJC_IVAR_$_PTMedianFilter._frameIndex
+ _OBJC_IVAR_$_PTMedianFilter._width
+ _OBJC_METACLASS_$_PTEffectColorTemperatureEstimation
+ _OBJC_METACLASS_$_PTEffectFaceLuxEstimation
+ _OBJC_METACLASS_$_PTEffectRingLightConfig
+ _OBJC_METACLASS_$_PTEffectRingLightEstimation
+ _OBJC_METACLASS_$_PTEffectRingLightInput
+ _OBJC_METACLASS_$_PTEffectRingLightOutput
+ _OBJC_METACLASS_$_PTMedianFilter
+ _PTAEStatsContainsPoint
+ _PTAEStatsLargestFaceRectIndex
+ _PTAEStatsParseFaceRects
+ _PTAEStatsParseFaceRects.cold.1
+ _PTAEStatsThumbnailToLuma
+ _PTAEStatsThumbnailToRGB
+ __OBJC_$_CLASS_METHODS_PTEffectColorTemperatureEstimation
+ __OBJC_$_INSTANCE_METHODS_PTEffectFaceLuxEstimation
+ __OBJC_$_INSTANCE_METHODS_PTEffectRingLightConfig
+ __OBJC_$_INSTANCE_METHODS_PTEffectRingLightEstimation
+ __OBJC_$_INSTANCE_METHODS_PTEffectRingLightInput
+ __OBJC_$_INSTANCE_METHODS_PTEffectRingLightOutput
+ __OBJC_$_INSTANCE_METHODS_PTMedianFilter
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectFaceLuxEstimation
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectRingLightConfig
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectRingLightEstimation
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectRingLightInput
+ __OBJC_$_INSTANCE_VARIABLES_PTEffectRingLightOutput
+ __OBJC_$_INSTANCE_VARIABLES_PTMedianFilter
+ __OBJC_$_PROP_LIST_PTEffectRingLightConfig
+ __OBJC_$_PROP_LIST_PTEffectRingLightInput
+ __OBJC_$_PROP_LIST_PTEffectRingLightOutput
+ __OBJC_CLASS_RO_$_PTEffectColorTemperatureEstimation
+ __OBJC_CLASS_RO_$_PTEffectFaceLuxEstimation
+ __OBJC_CLASS_RO_$_PTEffectRingLightConfig
+ __OBJC_CLASS_RO_$_PTEffectRingLightEstimation
+ __OBJC_CLASS_RO_$_PTEffectRingLightInput
+ __OBJC_CLASS_RO_$_PTEffectRingLightOutput
+ __OBJC_CLASS_RO_$_PTMedianFilter
+ __OBJC_METACLASS_RO_$_PTEffectColorTemperatureEstimation
+ __OBJC_METACLASS_RO_$_PTEffectFaceLuxEstimation
+ __OBJC_METACLASS_RO_$_PTEffectRingLightConfig
+ __OBJC_METACLASS_RO_$_PTEffectRingLightEstimation
+ __OBJC_METACLASS_RO_$_PTEffectRingLightInput
+ __OBJC_METACLASS_RO_$_PTEffectRingLightOutput
+ __OBJC_METACLASS_RO_$_PTMedianFilter
+ ___46-[PTEffectRingLightEstimation updateDefaults:]_block_invoke
+ ___79-[PTEffectFaceLuxEstimation faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:]_block_invoke
+ ___79-[PTEffectFaceLuxEstimation faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:]_block_invoke.cold.1
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.224
+ ___block_literal_global.242
+ _awbRGBNeutral
+ _awbRGBNeutral.cold.1
+ _compareFloats
+ _faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:.onceToken
+ _objc_msgSend$EMAFactorPerFrame
+ _objc_msgSend$applyDeadZoneOnValue:deadZoneFactor:valueRange:newValue:edgeEMACoefficient:
+ _objc_msgSend$applyStepFunctionOnValue:min:max:levels:
+ _objc_msgSend$bindInputPixelBuffer:
+ _objc_msgSend$computeFaceLux:frameIndex:
+ _objc_msgSend$computeNormalizedEffectStrength
+ _objc_msgSend$currentRingLightWidth
+ _objc_msgSend$deadZoneFactorPerFrame
+ _objc_msgSend$detectAdaptiveBehavior:
+ _objc_msgSend$deviceMaxScreenNits
+ _objc_msgSend$deviceScreenSizeInches
+ _objc_msgSend$effectDisableAtLux
+ _objc_msgSend$effectEnableAtLux
+ _objc_msgSend$effectMaxAtLux
+ _objc_msgSend$effectMinAtLux
+ _objc_msgSend$estimateScreenNits:
+ _objc_msgSend$faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:
+ _objc_msgSend$filter:
+ _objc_msgSend$initWithFilterWidth:
+ _objc_msgSend$initWithMetalContext:effectRelighting:ringLightEstimation:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:
+ _objc_msgSend$initWithMetalContext:humanDetections:effectDescriptor:
+ _objc_msgSend$largestFaceRect
+ _objc_msgSend$lumaFromAEStats:
+ _objc_msgSend$mapEffectStrengthToRingLightWidth:
+ _objc_msgSend$mapEffectStrengthToScreenNits:
+ _objc_msgSend$maxNitsMaxEffectStrength
+ _objc_msgSend$maxNitsMinEffectStrength
+ _objc_msgSend$metadataDictionary
+ _objc_msgSend$minNitsMaxEffectStrength
+ _objc_msgSend$minNitsMinEffectStrength
+ _objc_msgSend$pixelBufferToLumaChroma:pixelBuffer:outLuma:outChroma:read:write:
+ _objc_msgSend$ringLightAdaptiveSettings
+ _objc_msgSend$ringLightConfig
+ _objc_msgSend$ringLightInput
+ _objc_msgSend$ringLightOutput
+ _objc_msgSend$screenNitsEstimationMode
+ _objc_msgSend$setDeadZoneFactorPerFrame:
+ _objc_msgSend$setDeviceMaxScreenNits:
+ _objc_msgSend$setDeviceScreenSizeInches:
+ _objc_msgSend$setEMAFactorPerFrame:
+ _objc_msgSend$setEffectDisableAtLux:
+ _objc_msgSend$setEffectEnableAtLux:
+ _objc_msgSend$setEffectMaxAtLux:
+ _objc_msgSend$setEffectMinAtLux:
+ _objc_msgSend$setMaxNitsMaxEffectStrength:
+ _objc_msgSend$setMaxNitsMinEffectStrength:
+ _objc_msgSend$setMinNitsMaxEffectStrength:
+ _objc_msgSend$setMinNitsMinEffectStrength:
+ _objc_msgSend$setRingLightAdaptiveSettings:
+ _objc_msgSend$setRingLightInput:
+ _objc_msgSend$setRingLightOutput:
+ _objc_msgSend$setRingLightWidth:
+ _objc_msgSend$setScreenNitsFloor:
+ _objc_msgSend$shortValue
+ _objc_msgSend$updateDefaults:
+ _objc_msgSend$updateFaceLuxLevelFiltered:frameIndex:
+ _objc_msgSend$updateNitsBasedOnEffectStrength
+ _objc_msgSend$userScreenBrightnessChangeFrom
+ _objc_msgSend$userScreenBrightnessChangeTo
+ _qsort
+ _updateDefaults:.onceToken
- -[PTEffectDebugLayer initWithMetalContext:effectRelighting:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:]
- GCC_except_table35
- GCC_except_table38
- GCC_except_table41
- GCC_except_table45
- GCC_except_table47
- GCC_except_table48
- GCC_except_table50
- GCC_except_table52
- GCC_except_table53
- GCC_except_table56
- GCC_except_table58
- GCC_except_table59
- GCC_except_table72
- ___block_literal_global.138
- ___block_literal_global.156
- _objc_msgSend$initWithMetalContext:effectRelighting:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:
CStrings:
+ "@\"PTEffectFaceLuxEstimation\""
+ "@\"PTEffectRingLightConfig\""
+ "@\"PTEffectRingLightEstimation\""
+ "@\"PTEffectRingLightInput\""
+ "@\"PTEffectRingLightOutput\""
+ "@\"PTMedianFilter\""
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120"
+ "AEStatistics"
+ "AWBBGain"
+ "AWBComboBGain"
+ "AWBComboGGain"
+ "AWBComboRGain"
+ "AWBGGain"
+ "AWBRGain"
+ "Adjust effectStrength to %.1f"
+ "Cannot parse %@"
+ "Couldn't find white balance in the metadata"
+ "EMAFactorPerFrame"
+ "Error unexpected AE thumbnail %@"
+ "Error unexpected AE thumbnail missing %i"
+ "FaceRects"
+ "H16ISPAEMetadataFaceBlockX0"
+ "H16ISPAEMetadataFaceBlockX1"
+ "H16ISPAEMetadataFaceBlockY0"
+ "H16ISPAEMetadataFaceBlockY1"
+ "H16ISPAEMetadataFaceWeight"
+ "PTEffectColorTemperatureEstimation"
+ "PTEffectFaceLuxEstimation"
+ "PTEffectFaceLuxEstimation computeFaceLux"
+ "PTEffectRingLightConfig"
+ "PTEffectRingLightEstimation"
+ "PTEffectRingLightInput"
+ "PTEffectRingLightOutput"
+ "PTMedianFilter"
+ "QBA"
+ "RGBFromNormalizedColorTemperature:"
+ "Screen size factor %f for screen size %f x %f"
+ "T,V_deviceScreenSizeInches"
+ "T@\"NSData\",&,N,V_ringLightAdaptiveSettings"
+ "T@\"NSString\",&,N,V_ringLightMetadataFile"
+ "T@\"PTEffectRingLightConfig\",R,V_ringLightConfig"
+ "T@\"PTEffectRingLightInput\",&,N"
+ "T@\"PTEffectRingLightInput\",&,V_ringLightInput"
+ "T@\"PTEffectRingLightOutput\",&,N"
+ "T@\"PTEffectRingLightOutput\",&,V_ringLightOutput"
+ "T@\"PTEffectRingLightOutput\",R"
+ "Tf,V_EMAFactorPerFrame"
+ "Tf,V_currentRingLightWidth"
+ "Tf,V_currentScreenNits"
+ "Tf,V_deadZoneFactorPerFrame"
+ "Tf,V_deviceMaxScreenNits"
+ "Tf,V_effectDisableAtLux"
+ "Tf,V_effectEnableAtLux"
+ "Tf,V_effectMaxAtLux"
+ "Tf,V_effectMinAtLux"
+ "Tf,V_maxNitsMaxEffectStrength"
+ "Tf,V_maxNitsMinEffectStrength"
+ "Tf,V_minNitsMaxEffectStrength"
+ "Tf,V_minNitsMinEffectStrength"
+ "Tf,V_recommendedColorTemperatureNormalized"
+ "Tf,V_ringLightEffectStrength"
+ "Tf,V_ringLightUserColorTemperatureNormalized"
+ "Tf,V_ringLightWidth"
+ "Tf,V_screenNitsFloor"
+ "Tf,V_userScreenBrightnessChangeFrom"
+ "Tf,V_userScreenBrightnessChangeTo"
+ "Thumbnail"
+ "ThumbnailHeight"
+ "ThumbnailWidth"
+ "Ti,V_ambientColorEstimationMode"
+ "Ti,V_screenNitsEstimationMode"
+ "[1024 ]"
+ "[256 ]"
+ "^{CGColor=}20@0:8f16"
+ "_EMAFactorPerFrame"
+ "_MSRResize"
+ "_aeThumbnailLuma"
+ "_aeThumbnailRGB"
+ "_ambientColorEstimationMode"
+ "_chroma"
+ "_currentRingLightWidth"
+ "_currentScreenNits"
+ "_dataSorted"
+ "_deadZoneFactorPerFrame"
+ "_deviceMaxScreenNits"
+ "_deviceScreenSizeInches"
+ "_effectDisableAtLux"
+ "_effectEnableAtLux"
+ "_effectEnabled"
+ "_effectMaxAtLux"
+ "_effectMinAtLux"
+ "_effectMinAtLux %f must be greater than effectMaxAtLux %f"
+ "_effectStrength"
+ "_effectStrengthData"
+ "_faceLuxBuffer"
+ "_faceLuxBuffer[i]"
+ "_faceLuxEstimation"
+ "_faceLuxEstimationFromAEStats"
+ "_faceLuxLevel"
+ "_faceLuxLevelFiltered"
+ "_globalLuxLevelFilter"
+ "_lastFrameIndexWithFaceRect"
+ "_lastFrameTimeSecondsScreenNitsEstimation"
+ "_lowResYUV"
+ "_luma"
+ "_luma.width / 2 == _faceLuxEstimation.threadExecutionWidth"
+ "_lumaFromAEStats"
+ "_maxNits"
+ "_maxNitsMaxEffectStrength"
+ "_maxNitsMinEffectStrength"
+ "_minNits"
+ "_minNitsMaxEffectStrength"
+ "_minNitsMinEffectStrength"
+ "_recommendedColorTemperatureNormalized"
+ "_rgbFromAEStats"
+ "_ringLightAdaptiveSettings"
+ "_ringLightConfig"
+ "_ringLightEffectStrength"
+ "_ringLightEstimation"
+ "_ringLightEstimationLuxGraph"
+ "_ringLightEstimationScreenNitsGraph"
+ "_ringLightInput"
+ "_ringLightMetadataFile"
+ "_ringLightOutput"
+ "_ringLightUserColorTemperatureNormalized"
+ "_ringLightWidth"
+ "_ringlightConfig"
+ "_ringlightConfig %@"
+ "_screenNitsDeadzone"
+ "_screenNitsEstimationMode"
+ "_screenNitsFloor"
+ "_userScreenBrightnessChangeFrom"
+ "_userScreenBrightnessChangeTo"
+ "ambientColorEstimationMode"
+ "computeFaceLux:frameIndex:"
+ "computeNormalizedEffectStrength"
+ "currentRingLightWidth"
+ "currentScreenNits"
+ "deadZoneFactorPerFrame"
+ "detectAdaptiveBehavior:"
+ "deviceMaxScreenNits"
+ "deviceScreenSizeInches"
+ "diagonalScreenSizeInches"
+ "effectDisableAtLux"
+ "effectEnableAtLux"
+ "effectMaxAtLux"
+ "effectMinAtLux"
+ "estimateScreenNits:"
+ "f24@0:8f16i20"
+ "f32@0:8f16^{__CVBuffer=}20i28"
+ "face rect metadata not found"
+ "faceLuxEstimation"
+ "faceLuxEstimationFromAEStats"
+ "faceLuxLevel"
+ "faceLuxLevel:inColorBuffer:frameIndex:"
+ "faceLuxLevelFiltered"
+ "faceLuxLevelFromAEStats:globalLuxLevel:frameIndex:"
+ "filter:"
+ "inRingLightInput"
+ "initWithFilterWidth:"
+ "initWithMetalContext:effectRelighting:ringLightEstimation:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:"
+ "initWithMetalContext:humanDetections:effectDescriptor:"
+ "largestFaceRect"
+ "lumaFromAEStats:"
+ "mapEffectStrengthToRingLightWidth:"
+ "mapEffectStrengthToScreenNits:"
+ "maxNitsMaxEffectStrength"
+ "maxNitsMinEffectStrength"
+ "minNitsMaxEffectStrength"
+ "minNitsMinEffectStrength"
+ "outFaceRects array must be %i but was %i"
+ "outRingLightControl"
+ "outRingLightOutput"
+ "recommendedColorTemperatureNormalized"
+ "rgbFromAEStats:"
+ "ringLightAdaptiveSettings"
+ "ringLightConfig"
+ "ringLightEffectStrength"
+ "ringLightInput"
+ "ringLightMetadataFile"
+ "ringLightOutput"
+ "ringLightUserColorTemperatureNormalized"
+ "ringLightWidth"
+ "screenNitsEstimationMode"
+ "screenNitsFloor"
+ "setAmbientColorEstimationMode:"
+ "setCurrentRingLightWidth:"
+ "setCurrentScreenNits:"
+ "setDeadZoneFactorPerFrame:"
+ "setDeviceMaxScreenNits:"
+ "setDeviceScreenSizeInches:"
+ "setDiagonalScreenSizeInches:"
+ "setEMAFactorPerFrame:"
+ "setEffectDisableAtLux:"
+ "setEffectEnableAtLux:"
+ "setEffectMaxAtLux:"
+ "setEffectMinAtLux:"
+ "setInRingLightInput:"
+ "setMaxNitsMaxEffectStrength:"
+ "setMaxNitsMinEffectStrength:"
+ "setMinNitsMaxEffectStrength:"
+ "setMinNitsMinEffectStrength:"
+ "setOutRingLightOutput:"
+ "setRecommendedColorTemperatureNormalized:"
+ "setRingLightAdaptiveSettings:"
+ "setRingLightEffectStrength:"
+ "setRingLightInput:"
+ "setRingLightMetadataFile:"
+ "setRingLightOutput:"
+ "setRingLightUserColorTemperatureNormalized:"
+ "setRingLightWidth:"
+ "setScreenNitsEstimationMode:"
+ "setScreenNitsFloor:"
+ "setUserScreenBrightnessChangeFrom:"
+ "setUserScreenBrightnessChangeTo:"
+ "shortValue"
+ "updateDefaults:"
+ "updateFaceLuxLevelFiltered:frameIndex:"
+ "updateNitsBasedOnEffectStrength"
+ "userScreenBrightnessChangeFrom"
+ "userScreenBrightnessChangeTo"
+ "v24@0:8f16i20"
+ "{PTEffectFaceLuxEstimationOutput=\"faceLuxValue\"f\"lumaToLuxFactor\"f\"skinAreaToFullFrameFactor\"f\"skinLumaFullRes\"f\"lumaSumAll\"f\"skinLumaSumAll\"f\"skinSumAll\"f}"
+ "{PTEffectFaceLuxEstimationOutput=fffffff}16@0:8"
+ "{PTEffectFaceLuxEstimationOutput=fffffff}32@0:8@16f24i28"
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "initWithMetalContext:effectRelighting:effectDescritor:renderState:util:colorConversion:msrColorPyramid:vfxRenderEffect:depthConverter:disparityFixedFocus:faceDisparityArray:focusDisparityRaw:focusDisparityModifiers:"

```

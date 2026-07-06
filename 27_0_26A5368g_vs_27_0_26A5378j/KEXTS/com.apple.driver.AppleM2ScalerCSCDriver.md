## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-  __TEXT.__const: 0xc3050
-  __TEXT.__cstring: 0x241d6
-  __TEXT_EXEC.__text: 0x13e3d8
+  __TEXT.__const: 0xc3020
+  __TEXT.__cstring: 0x254d4
+  __TEXT_EXEC.__text: 0x145ea0
   __TEXT_EXEC.__auth_stubs: 0xba0
   __DATA.__data: 0x22388
-  __DATA.__common: 0x2738
-  __DATA.__bss: 0x215c
-  __DATA_CONST.__mod_init_func: 0x6a0
-  __DATA_CONST.__mod_term_func: 0x670
-  __DATA_CONST.__const: 0x3d830
-  __DATA_CONST.__kalloc_type: 0x4e80
+  __DATA.__common: 0x2760
+  __DATA.__bss: 0x2184
+  __DATA_CONST.__mod_init_func: 0x6a8
+  __DATA_CONST.__mod_term_func: 0x678
+  __DATA_CONST.__const: 0x3de88
+  __DATA_CONST.__kalloc_type: 0x4ec0
   __DATA_CONST.__kalloc_var: 0x1310
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10052
-  Symbols:   14330
-  CStrings:  3545
+  Functions: 10214
+  Symbols:   14505
+  CStrings:  3649
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _GLOBAL__sub_I_M2ScalerScalingASEControlMSR29.cpp
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _ZN27IosaFirmwareControlMSR29Rtk17fdrGetReadPointerEj
+ _ZN27IosaFirmwareControlMSR30Rtk20dashboardPairWrite64Ejy
+ _ZN30M2ScalerScalingASEControlMSR2926configureEBEE_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ _ZN30M2ScalerScalingASEControlMSR2930configureSharpLUT_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ _ZN30M2ScalerScalingASEControlMSR2935configureInterpolation_gatedContextEP18M2ScalerCSCRequest18COLOR_FORMAT_CLASSbP16pipeUnitExchange
+ _ZNK16IosaPowerManager27logPowerStateTrackerEntriesEv
+ __Z19floatToFixedRoundedfjj
+ __Z20doubleToFixedRoundeddjj
+ __Z22getCustomFilterBinNamej
+ __Z23getDefaultFilterBinNamej
+ __ZL34M2ScalerScalingASEControlMSR29_ktv
+ __ZN22AppleM2ScalerCSCDriver17parseHalEdtConfigEP9IOServicej
+ __ZN22AppleM2ScalerCSCDriver34checkPowerAckWatchdog_gatedContextEv
+ __ZN24AppleM2ScalerCSCHalMSR2316getPsdPowerDieIdEv
+ __ZN24AppleM2ScalerCSCHalMSR3016getPsdPowerDieIdEv
+ __ZN24IosaFirmwareControlMSR2317fdrGetReadPointerEj
+ __ZN24IosaFirmwareControlMSR2319sdrWriteReadPointerEy
+ __ZN25M2ScalerScalingASEControl30configureSharpLUT_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN27IosaFirmwareControlMSR29Rtk17fdrGetReadPointerEj
+ __ZN27IosaFirmwareControlMSR29Rtk19dashboardIrqMaskSetEjj
+ __ZN27IosaFirmwareControlMSR29Rtk19dashboardPairRead64Ej
+ __ZN27IosaFirmwareControlMSR29Rtk19sdrWriteReadPointerEy
+ __ZN27IosaFirmwareControlMSR29Rtk20dashboardPairWrite64Ejy
+ __ZN27IosaFirmwareControlMSR30Rtk19dashboardIrqMaskSetEjj
+ __ZN27IosaFirmwareControlMSR30Rtk19dashboardPairRead64Ej
+ __ZN27IosaFirmwareControlMSR30Rtk20dashboardPairWrite64Ejy
+ __ZN29BlockDescriptorRegStreamMSR2322deallocateNeighborDataERN24BlockDescriptorRegStream12NeighborDataE
+ __ZN30M2ScalerScalingASEControlMSR2910gMetaClassE
+ __ZN30M2ScalerScalingASEControlMSR2910superClassE
+ __ZN30M2ScalerScalingASEControlMSR2917configureTunablesEP18M2ScalerCSCRequest
+ __ZN30M2ScalerScalingASEControlMSR2926configureEBEE_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2927configureBlend_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2928configureAsecti_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2929configurePeaking_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2930commitEnhancement_gatedContextEP18M2ScalerCSCRequestbP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2930configureSharpLUT_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2931configureToneStats_gatedContextEP18M2ScalerCSCRequestP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2933configureAngleDetect_gatedContextEP18M2ScalerCSCRequestb
+ __ZN30M2ScalerScalingASEControlMSR2935configureInterpolation_gatedContextEP18M2ScalerCSCRequest18COLOR_FORMAT_CLASSbP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR2937configureNoiseEstimation_gatedContextEP18M2ScalerCSCRequestbP16pipeUnitExchange
+ __ZN30M2ScalerScalingASEControlMSR299MetaClassC1Ev
+ __ZN30M2ScalerScalingASEControlMSR299MetaClassC2Ev
+ __ZN30M2ScalerScalingASEControlMSR299MetaClassD0Ev
+ __ZN30M2ScalerScalingASEControlMSR299MetaClassD1Ev
+ __ZN30M2ScalerScalingASEControlMSR299metaClassE
+ __ZN30M2ScalerScalingASEControlMSR29C1EPK11OSMetaClass
+ __ZN30M2ScalerScalingASEControlMSR29C1Ev
+ __ZN30M2ScalerScalingASEControlMSR29C2EPK11OSMetaClass
+ __ZN30M2ScalerScalingASEControlMSR29C2Ev
+ __ZN30M2ScalerScalingASEControlMSR29D0Ev
+ __ZN30M2ScalerScalingASEControlMSR29D1Ev
+ __ZN30M2ScalerScalingASEControlMSR29D2Ev
+ __ZN30M2ScalerScalingASEControlMSR29dlEPvm
+ __ZN30M2ScalerScalingASEControlMSR29nwEm
+ __ZNK16IosaPowerManager27logPowerStateTrackerEntriesEv
+ __ZNK30M2ScalerScalingASEControlMSR2912getMetaClassEv
+ __ZNK30M2ScalerScalingASEControlMSR299MetaClass5allocEv
+ __ZTV30M2ScalerScalingASEControlMSR29
+ __ZTVN30M2ScalerScalingASEControlMSR299MetaClassE
+ __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_3135
+ __ZZN12ActiveWindow18obtainActiveWindowEjjjjE21kalloc_type_view_2308
+ __ZZN15ActiveWindowSet7releaseEvE21kalloc_type_view_2298
+ __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEjE22kalloc_type_view_11042
+ __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10972
+ __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10978
+ __ZZN19AppleM2ScalerCSCHal32updateShadowMapperCacheTTL_gatedEjyE22kalloc_type_view_11026
+ __ZZN19AppleM2ScalerCSCHal4freeEvE21kalloc_type_view_9609
+ __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6284
+ __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6263
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1726
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1733
+ __ZZN24BlockDescriptorRegStream20invalidateFrameStateEP18M2ScalerCSCRequestE20kalloc_type_view_322
+ __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_623
+ __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_684
+ __ZZN26IOSurfaceAcceleratorClient40asynchronousUserClientCompletionCallbackEPvS0_E20kalloc_type_view_591
+ _get_single_dimen_tilearray
- _ZN27IosaFirmwareControlMSR29Rtk18sdrGetWritePointerEv
- __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_3006
- __ZZN12ActiveWindow18obtainActiveWindowEjjjjE21kalloc_type_view_2147
- __ZZN15ActiveWindowSet7releaseEvE21kalloc_type_view_2137
- __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEjE22kalloc_type_view_11034
- __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10964
- __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10970
- __ZZN19AppleM2ScalerCSCHal32updateShadowMapperCacheTTL_gatedEjyE22kalloc_type_view_11018
- __ZZN19AppleM2ScalerCSCHal4freeEvE21kalloc_type_view_9601
- __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6155
- __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6134
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1600
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1607
- __ZZN24BlockDescriptorRegStream20invalidateFrameStateEP18M2ScalerCSCRequestE20kalloc_type_view_318
- __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_624
- __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_683
- __ZZN26IOSurfaceAcceleratorClient40asynchronousUserClientCompletionCallbackEPvS0_E20kalloc_type_view_594
- _get_single_dimen_tile
CStrings:
+ "    ... (remaining %d entries omitted, enable TRACE to see all)\n"
+ "    biCoeff[%d]: c0=%d, c1=%d, c2=%d, c3=%d\n"
+ "    biNegSlope[%d]: slope0=%d, slope1=%d\n"
+ "    biNegThresh[%d]: thresh0=%d, thresh1=%d\n"
+ "    biNegVal[%d]: value0=%d, value1=%d\n"
+ "    biPosSlope[%d]: slope0=%d, slope1=%d\n"
+ "    biPosThresh[%d]: thresh0=%d, thresh1=%d\n"
+ "    biPosVal[%d]: value0=%d, value1=%d\n"
+ "    deltaSlope[%d]: slope0=%d, slope1=%d\n"
+ "    deltaThresh[%d]: thresh0=%d, thresh1=%d\n"
+ "    deltaVal[%d]: v0=%d, v1=%d, v2=%d, v3=%d\n"
+ "    dwCoeff[%d]: c0=%d, c1=%d, c2=%d, c3=%d\n"
+ "    mixSlope[%d]: s0=%d, s1=%d\n"
+ "    mixThresh[%d]: t0=%d, t1=%d, t2=%d, t3=%d\n"
+ "    mixVal[%d]: v0=%d, v1=%d\n"
+ "    sharpLut[%d]: value0=%d, value1=%d\n"
+ "  Bilateral Coefficients [%d entries × 4]:\n"
+ "  Bilateral Negative Curves:\n"
+ "  Bilateral Positive Curves:\n"
+ "  Delta Slopes:\n"
+ "  Delta Thresholds:\n"
+ "  Delta Values:\n"
+ "  Directional Weighting Coefficients [%d entries × 4]:\n"
+ "  Found ASE Angle Detect V3\n"
+ "  Found ASE Blend Config V3\n"
+ "  Found ASE EBE Config V3\n"
+ "  Found ASE EBE Config V4\n"
+ "  Found ASE Noise Meter V3\n"
+ "  Found ASE Peaking Config V3\n"
+ "  Found ASE Scaling Coeff Config V3\n"
+ "  Found ASE Sharp LUT Config V4\n"
+ "  MATCH FOUND: type=%s, size=%u, expectedSize=%zu\n"
+ "  Mix Curves:\n"
+ "  Optional HCU type %s not found (OK)\n"
+ "  Parse loop: offset=%zu, remaining=%u, entryType=%s, entrySize=%u\n"
+ "  Processing V4-specific HCUs...\n"
+ "  controlParams: shootCtlEn=%d, sharpLUTEn=%d, lessBit=%d, deltaEBEEn=%d\n"
+ "  ebeParams2: phiMin=%d, diffPenalty=%d\n"
+ "  sharpLut[%d × 2] (showing first 10, use TRACE for all):\n"
+ "  shootControlParams1: overBase=%d, underBase=%d, overSlope=%d, underSlope=%d\n"
+ "  shootControlParams2: overMinVal=%d, underMinVal=%d, overShift=%d, underShift=%d\n"
+ " (0.%03ux downscale)"
+ " (identity)"
+ " (upscale)"
+ " 0x%08x"
+ " deallocateNeighborChannel nd=%p\n"
+ "\"[%s] \" \"setPowerState sleep ack watchdog: MSR%u scaler %u sleepStateSPS=%u powerRefCount=%u partitionPower=%u compQueueEmpty=%u running=%u cmdQueueDepth=%u recoveryInProgress=%u resetReason=%u fwLoaded=%u pendingMask=0x%x ticks=%u\\n\" @%s:%d"
+ "\"[%s] \" sd.frame_info.priority @%s:%d"
+ "\"[IOSA] Unexpected frame pri from FW ( %u )\\n\""
+ "%s\n"
+ "%s %s, src to dst ratio index=%d%s:\n"
+ "%s : %s tap %d and tap %d are not close in value as expected\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR28.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR29.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR30.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR29Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR30Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR29.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaTunableControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/K2KTests.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR29.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23CurvatureLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MailBox.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MailBoxMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/Request.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
+ "0.25x"
+ "0.375x"
+ "0.5x"
+ "0.625x"
+ "0.75x"
+ "0.875x"
+ "12000000200000002111121122222112222211222221122222112222211222221122222112222211222221111222111122211112221111222111122211112221111222111122222112000000"
+ "12111112122212121222211122111222022121111111111111000000200000002000000020000000212211111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221121122212"
+ "12111122221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222002000000022222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222212222211211221121222221121122112112222222222222222222222222222222122222222222222222222222222221222222222211222222222222222222222222222222222221212121212121212111121111111111111122111211121212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111122222222222222222222222122122112122112122112122112122112122112122112122110000020000000221111111100000020000000"
+ "12122121221212212122121221212212122121221212212122121221212212122120000020000000122112221200000020000000211112112222211222221122222112222211222221122222112222211222221122222111122211112221111222111122211112221111222111122211112222211200000020000000"
+ "=== ASE EBE V4 Config Injected ===\n"
+ "=== ASE Sharp LUT V4 Config Injected ===\n"
+ "=== End EBE V4 Config ===\n"
+ "=== End Sharp LUT V4 Config ===\n"
+ "ASE API Legacy: elem=%u, size=%u, min=%zu (ASEConfigUnits), max=%zu\n"
+ "ASE API V3: elem=%u, size=%u, min=%zu (hdr+entry+scaling), max=%zu\n"
+ "ASE API V4: elem=%u, size=%u, min=%zu (hdr), max=%zu\n"
+ "ASE API capability: V3=%d, V4=%d, commElement=%d\n"
+ "Comm elem=%u (non-ASE): size=%u, min=%zu, max=%zu\n"
+ "Custom Chroma Filter [%s]:\n"
+ "Custom Filter [%s]:\n"
+ "HCU API %s validation FAILED: elem=%u, size=%u not in [%zu, %zu]\n"
+ "HCU API %s validation PASSED: elem=%u, size=%u in [%zu, %zu]\n"
+ "HCU API bad entry header: headerEnd=%p bufferEnd=%p size=%u min=%zu type=%s\n"
+ "HCU API bad header format: count=%u, totalSize=%u, bufLen=%zu\n"
+ "HCU API entry %s invalid: size=%u expected=%zu bufEnd=%p entryEnd=%p\n"
+ "HCU API size accounting error: entrySize=%u > remaining=%u, type=%s\n"
+ "Histogram bin count (%d) exceeds maximum (%d)"
+ "Identity"
+ "Initialize MSR29 Dashboard interrupt sources index %u..\n"
+ "Initialize MSR29 Mailbox interrupt sources index %u..\n"
+ "LEGACY"
+ "M2ScalerScalingASEControlMSR29"
+ "M2ScalerScalingASEControlMSR29.cpp"
+ "MSR23BackwardsCompatibleFilter::checkCoefficientsValid...0x%x\n"
+ "MSR23BackwardsCompatibleFilter::updateWithCoefficients srcToDstRatioIndex %d (%s) %p\n"
+ "NC slot %u not yet released req %d; forcing release\n"
+ "T(%02d)"
+ "Upscale"
+ "Upscale/Identity"
+ "V1/V2"
+ "V3"
+ "V4"
+ "WA: fake the dashboard interrupt!\n"
+ "[%05X %08X] %03u {%08X %08X} tile %s: f=%08X: tile=[%u,%u]%s%s%s (tdr=%u)"
+ "[%s][%s]getIndexFromSrcToDstRatio filterIndex: %d (%s)\n"
+ "[%s][Chroma] bin mismatch; %s custom filter has ratio match, using %s coefficients\n"
+ "[%s][Chroma] bin mismatch; falling back to default filter bin %d (%s)\n"
+ "[%s][Luma] bin mismatch; %s custom filter has ratio match, using %s coefficients\n"
+ "[%s][Luma] bin mismatch; falling back to default filter bin %d (%s)\n"
+ "[FilterComp] pCoefficients %p Returning 0x%x for t:%d p:%d\n"
+ "[IOSA] Discarding stale SD frame_id %u (all requests flushed, firmware reset pending)\n"
+ "[IOSA][Boot ] Scaler[%d]:[%s]: %d (%#x) (%s)\n"
+ "dashboardIrqMaskSet"
+ "dashboardIrqMaskSet pair %d offset 0x%x mask 0x%x\n"
+ "dashboardPairWrite64"
+ "dashboardPairWrite64 dash_index = %u, base_pair = %u, pair = %u, offset = 0x%x\n"
+ "dst format %d pixels align(%d %d)\n"
+ "fdrGetReadPointer"
+ "fdrResetPointers prio = %d, val 0x%llx\n"
+ "findApiParams FAILED: type=%s, error=0x%x\n"
+ "findApiParams SUCCESS: type=%s found at %p\n"
+ "findApiParams: type=%s, expectedSize=%zu, bufAddr=%p, bufLen=%zu, required=%d\n"
+ "get_single_dimen_tilearray H failed (%u)\n"
+ "get_single_dimen_tilearray V failed (%u)\n"
+ "logEBEConfigV4"
+ "logPowerStateTrackerEntries"
+ "logSharpLUTConfigV4"
+ "pair = %u, mStartAddr = 0x%x\n"
+ "powerStateTracker[%u]: req=%p transformId=%d reason=%u count=%u\n"
+ "ratio %s%d.%s%u\n"
+ "releaseTileArraySlot (private) slot %u dva 0x%llx\n"
+ "releaseTileArraySlot slot %u dva 0x%llx\n"
+ "releaseTileArraySlots"
+ "releaseTileArraySlots: slot %u decrementing default NC refCount\n"
+ "releaseTileArraySlots: slot %u freeing stale NC buffer %p\n"
+ "site.M2ScalerScalingASEControlMSR29"
- " deallocateNeighborChannel %p\n"
- "\"[IOSA] Unexpected frame pri from FW ( %u )\\n\" @%s:%d"
- "%s %s, src to dst ratio index=%d:\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR28.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR29.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR30.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR29Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR29.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaTunableControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/K2KTests.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MSR23CurvatureLUT.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MailBox.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MailBoxMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/Request.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SUOqn5/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
- "0x%08x "
- "1200000020000000211112112222211112211112211112211112211112211112211112211112222112000000"
- "12111112122212121222111221112220221211111111111110000000200000002000000020000000212211111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221121122212"
- "12111122221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222002000000022222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222212222211211221121222221121122112112222222222222222222222222222222122222222222222222222222222221222222222211222222222222222222222222222222222221212121212121212111121111111111112211121112121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111112222222222222222222222212212211212211212211212211212211212211212211212211000000020000000221111111100000020000000"
- "1212212122121221212212122121221212212122121221212212122121221212212000002000000012211222120000002000000021111211222221111221111221111221111221111221111221111221111222211200000020000000"
- "HCU API bad entry header format\n"
- "HCU API bad header format\n"
- "HCU API entry %s is invalid\n"
- "HCU API list size inconsistency: HeaderHcuSize=%u, hcuTotal=%u\n"
- "Initialize MSR29 Dashboard interrupt sources ..\n"
- "Initialize MSR29 Mailbox interrupt sources ..\n"
- "T(%02d) "
- "[%05X %08X] %03u {%08X %08X} tile %s: f=%08X: tile=[%u,%u]%s (tdr=%u)"
- "[%s][%s]getIndexFromSrcToDstRatio filterIndex: %d \n"
- "[FilterComp]Returning 0x%x for t:%d p:%d\n"
- "fdrResetPointers prio = %d, offset = 0x%x val 0x%llx\n"
- "get_single_dimen_tile H[%u] failed (%u)\n"
- "get_single_dimen_tile V[%u] failed (%u)\n"
- "mStartAddr = 0x%x\n"
- "prio = %d, base_pair = %d, fdr_pair = %d, (fdr_pair * 2) = %d, offset = 0x%x \n"
- "sdrGetWritePointer"
- "sdrGetWritePointer %lld\n"
- "src format %d pixels align(%d %d)\n"
- "tap %d and tap %d are not close in value as expected\n"

```

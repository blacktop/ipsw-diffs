## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-154.19.0.0.0
-  __TEXT.__const: 0x69cf0
-  __TEXT.__cstring: 0x1cb78
-  __TEXT_EXEC.__text: 0x106888
+154.22.0.0.0
+  __TEXT.__const: 0x69fe0
+  __TEXT.__cstring: 0x1ce7e
+  __TEXT_EXEC.__text: 0x10834c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1ff08
   __DATA.__common: 0x2330

   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x650
   __DATA_CONST.__mod_term_func: 0x5a8
-  __DATA_CONST.__const: 0x35b58
+  __DATA_CONST.__const: 0x35e10
   __DATA_CONST.__kalloc_type: 0x4700
   __DATA_CONST.__kalloc_var: 0xb90
-  UUID: 3CB6F1CC-0F2F-3F09-B944-57E541CFFD0A
-  Functions: 8294
-  Symbols:   12251
-  CStrings:  2909
+  UUID: 663679A7-45AF-3FD4-BDCE-004925313FE4
+  Functions: 8390
+  Symbols:   12347
+  CStrings:  2919
 
Symbols:
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _ZN21IosaPowerManagerMSR2334trackPowerStateReason_gatedContextE17powerManagerStateP18M2ScalerCSCRequest27PowerManagerStateReasonCode.cold.1
+ _ZN21IosaPowerManagerMSR2334trackPowerStateReason_gatedContextE17powerManagerStateP18M2ScalerCSCRequest27PowerManagerStateReasonCode.cold.2
+ _ZN22AppleM2ScalerCSCDriver15decStatLoadSizeEjy.cold.1
+ _ZN22AppleM2ScalerCSCDriver38dequeueAndExecuteRequests_gatedContextEv.cold.2
+ _ZN24AppleM2ScalerCSCHalMSR2320interruptOccurredMSREP22IOInterruptEventSourcei.cold.2
+ _ZN24AppleM2ScalerCSCHalMSR2320interruptOccurredMSREP22IOInterruptEventSourcei.cold.3
+ _ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy.cold.1
+ _ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy.cold.2
+ _ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy.cold.3
+ _ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy.cold.4
+ _ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy.cold.5
+ _ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy.cold.6
+ _ZN24BlockDescriptorRegStream23clearBlockDescriptorSetERNS_18BlockDescriptorSetE.cold.1
+ __ZL20ditherKernelMatrices
+ __ZN16IosaColorManager31configurePrecisionScalingFactorEP18M2ScalerCSCRequest
+ __ZN16IosaPowerManager34trackPowerStateReason_gatedContextE17powerManagerStateP18M2ScalerCSCRequest27PowerManagerStateReasonCode
+ __ZN16IosaPowerManager35setPartitionPowerState_gatedContextE21powerManagerPartition17powerManagerStatebP18M2ScalerCSCRequest27PowerManagerStateReasonCode
+ __ZN16IosaPowerManager38checkPowerStateForRequest_gatedContextEP18M2ScalerCSCRequest
+ __ZN19AppleM2ScalerCSCHal20trackDartError_gatedEjy
+ __ZN19AppleM2ScalerCSCHal22setDeferredResetReasonE14reset_reason_t
+ __ZN19FrameDescriptorRing5remapEv
+ __ZN19FrameDescriptorRing5unmapEv
+ __ZN19IosaFirmwareControl18getPendingFdrCountEv
+ __ZN20IosaColorManagerMSR831configurePrecisionScalingFactorEP18M2ScalerCSCRequest
+ __ZN21IosaColorManagerMSR2031configurePrecisionScalingFactorEP18M2ScalerCSCRequest
+ __ZN21IosaColorManagerMSR2331configurePrecisionScalingFactorEP18M2ScalerCSCRequest
+ __ZN21IosaPowerManagerMSR2334trackPowerStateReason_gatedContextE17powerManagerStateP18M2ScalerCSCRequest27PowerManagerStateReasonCode
+ __ZN21IosaPowerManagerMSR2338checkPowerStateForRequest_gatedContextEP18M2ScalerCSCRequest
+ __ZN22AppleM2ScalerCSCDriver14trackDartErrorEjjy
+ __ZN22AppleM2ScalerCSCDriver15decStatLoadSizeEjy
+ __ZN22AppleM2ScalerCSCDriver15incStatLoadSizeEjy
+ __ZN22AppleM2ScalerCSCHalMSR22setDeferredResetReasonE14reset_reason_t
+ __ZN24AppleM2ScalerCSCHalMSR2320trackDartError_gatedEjy
+ __ZN24AppleM2ScalerCSCHalMSR2328canResetMsrIfWithDartGangingEv
+ __ZN24IosaFirmwareControlMSR2318getPendingFdrCountEv
+ __ZN24IosaFirmwareControlMSR2318remapFrameDescRingEv
+ __ZN24IosaFirmwareControlMSR2318unmapFrameDescRingEv
+ __ZNK19AppleM2ScalerCSCHal22getDeferredResetReasonEv
+ __ZNK22AppleM2ScalerCSCHalMSR22getDeferredResetReasonEv
+ __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_2825
+ __ZZL22notify_signal_callbackP8OSObjectP20IOSurfaceSharedEventyyE21kalloc_type_view_2711
+ __ZZN12ActiveWindow18obtainActiveWindowEjjjjE21kalloc_type_view_2150
+ __ZZN15ActiveWindowSet7releaseEvE21kalloc_type_view_2141
+ __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEvE22kalloc_type_view_10498
+ __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE22kalloc_type_view_10437
+ __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE22kalloc_type_view_10459
+ __ZZN19AppleM2ScalerCSCHal40removeSurfaceFromShadowMapperCache_gatedEP9IOSurfaceE22kalloc_type_view_10483
+ __ZZN22AppleM2ScalerCSCDriver12notify_eventEP20IOSurfaceSharedEventyyE21kalloc_type_view_2674
+ __ZZN22AppleM2ScalerCSCDriver14trackDartErrorEjjyEN3$_08__invokeEP8OSObjectPvS3_S3_S3_
+ __ZZN22AppleM2ScalerCSCDriver16transformGeneralEP18M2ScalerCSCRequestEN3$_08__invokeEP8OSObjectPvS5_S5_S5_
+ __ZZN22AppleM2ScalerCSCDriver21isSharedEventWaitDoneEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3984
+ __ZZN22AppleM2ScalerCSCDriver24executeSharedEventSignalEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_4038
+ __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_5844
+ __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_5823
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1546
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1553
+ __ZZN24BlockDescriptorRegStream20invalidateFrameStateEP18M2ScalerCSCRequestE20kalloc_type_view_233
+ __ZZN24BlockDescriptorRegStream23clearBlockDescriptorSetERNS_18BlockDescriptorSetEE20kalloc_type_view_192
+ __ZZNK24BlockDescriptorRegStream24allocateBlockDescriptorsERNS_18BlockDescriptorSetEmE20kalloc_type_view_119
- _ZN24AppleM2ScalerCSCHalMSR2314onBufferMappedE16ScalerMapperTypeym.cold.1
- _ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy.cold.1
- _ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy.cold.2
- _ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy.cold.3
- _ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy.cold.4
- _ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy.cold.5
- _ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy.cold.6
- __ZN16IosaPowerManager35setPartitionPowerState_gatedContextE21powerManagerPartition17powerManagerStatebP18M2ScalerCSCRequest
- __ZN19IosaFirmwareControl16nonEmptyFdrCountEv
- __ZN24AppleM2ScalerCSCHalMSR2314trackDartErrorEjy
- __ZN24IosaFirmwareControlMSR2316nonEmptyFdrCountEv
- __ZN24IosaFirmwareControlMSR2319deInitFrameDescRingEv
- __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_2795
- __ZZL22notify_signal_callbackP8OSObjectP20IOSurfaceSharedEventyyE21kalloc_type_view_2681
- __ZZN12ActiveWindow18obtainActiveWindowEjjjjE21kalloc_type_view_2140
- __ZZN15ActiveWindowSet7releaseEvE21kalloc_type_view_2131
- __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEvE22kalloc_type_view_10464
- __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE22kalloc_type_view_10403
- __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE22kalloc_type_view_10425
- __ZZN19AppleM2ScalerCSCHal40removeSurfaceFromShadowMapperCache_gatedEP9IOSurfaceE22kalloc_type_view_10449
- __ZZN22AppleM2ScalerCSCDriver12notify_eventEP20IOSurfaceSharedEventyyE21kalloc_type_view_2644
- __ZZN22AppleM2ScalerCSCDriver21isSharedEventWaitDoneEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3912
- __ZZN22AppleM2ScalerCSCDriver24executeSharedEventSignalEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3966
- __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_5753
- __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_5732
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1545
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1552
- __ZZN24BlockDescriptorRegStream20invalidateFrameStateEP18M2ScalerCSCRequestE20kalloc_type_view_213
- __ZZN24BlockDescriptorRegStream23clearBlockDescriptorSetERNS_18BlockDescriptorSetEE20kalloc_type_view_189
- __ZZNK24BlockDescriptorRegStream24allocateBlockDescriptorsERNS_18BlockDescriptorSetEmE20kalloc_type_view_116
CStrings:
+ "\"[%s] \" \"Request %d hold power ref (%d)!\\n\" @%s:%d"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTunableControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/K2KTests.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23CurvatureLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBox.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Request.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugDGTHT3A6kBLdZmpXbjf6cIsyBS4n1e1Wk/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
+ "1211111222222222212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122"
+ "121111122222222221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221122222"
+ "121111222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220020000000222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222122122122122112222222222222222222222222222222122222222222222222222222222221222222222211222222222222222222222222222222222221212121212121212111121111111111112211121112121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222221221221121221121221121221121221121221121221121221100020000000221111111100000020000000"
+ "1222222222212111111112111111111111111111122122112211111211122222222"
+ "122222222221211111111211111111111111111112212211221111121112222222221111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222000002000000022200000"
+ "Defer reset (MSR Dart Ganging) %d: %d, %d\n"
+ "MSR Reset - Remap frame desc ring failed.\n"
+ "No available slots to track power state change to %d for request %p with reason %d\n"
+ "Power down with count already zero for request %p with reason %d\n"
+ "Power state change to %d for request %p (transform ID: %d) with reason %d, count: %d\n"
+ "Promote to default NC buffer! %zu, %zu -> %zu,%zu\n"
+ "Request %d hold power ref (%d)!\n"
+ "Unbalanced power down for request %p with reason %d\n"
+ "Unserviced Dashboard FDR Enqueue %d\n"
+ "clearBlockDescriptorSet"
+ "decStatLoadSize"
+ "decStatLoadSize: stat size %llu < load size %llu\n"
+ "dequeueAndExecuteRequests_gatedContext"
+ "req %d has pre-failed :%x.\n"
+ "trackDartError_gated"
+ "trackPowerStateReason_gatedContext"
- "\"[%s] \" \"Request hold power ref %d > %d!\\n\" @%s:%d"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTunableControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/K2KTests.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23CurvatureLUT.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBox.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Request.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugBbki4rI-06s_Li88RHb0WBsdlgVsWS9oY/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
- "1211111222222222"
- "121111122222222221122222"
- "1211112222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222200200000002222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222221221221221221122222222222222222222222222222221222222222222222222222222222212222222222112222222222222222222222222222222222212121212121212121111211111111111221112111212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222122121121211212112121121211212112121121211000020000000221111111100000020000000"
- "122222222221211111111211111111111111111112212211221111121112222222"
- "1222222222212111111112111111111111111111122122112211111211122222222211111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222000002000000022200000"
- "MSR Reset - Init frame desc ring failed.\n"
- "Request hold power ref %d > %d!\n"
- "Too many buffers allocated!\n"
- "Unserviced Dashboard FDR Enqueue\n"
- "onBufferMapped"
- "trackDartError"

```

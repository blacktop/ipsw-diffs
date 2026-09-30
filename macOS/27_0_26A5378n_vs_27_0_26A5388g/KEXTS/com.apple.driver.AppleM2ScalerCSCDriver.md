## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-200.56.1.0.0
+200.57.0.0.0
   __TEXT.__const: 0xc3020
-  __TEXT.__cstring: 0x254d4
-  __TEXT_EXEC.__text: 0x145ea0
+  __TEXT.__cstring: 0x25520
+  __TEXT_EXEC.__text: 0x146028
   __TEXT_EXEC.__auth_stubs: 0xba0
   __DATA.__data: 0x22388
   __DATA.__common: 0x2760

   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10214
+  Functions: 10215
   Symbols:   10288
-  CStrings:  3649
+  CStrings:  3650
 
Symbols:
+ __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6292
+ __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6271
- __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6284
- __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6263
Functions:
~ __ZN24AppleM2ScalerCSCHalMSR2318wakeSequence_gatedEv : 876 -> 884
~ __ZN24AppleM2ScalerCSCHalMSR2325restoreTunablesDuringWakeEv : 440 -> 400
~ __ZN24AppleM2ScalerCSCHalMSR2329activateMSRState_gatedContextE17powerManagerState : 696 -> 1000
~ __ZN24AppleM2ScalerCSCHalMSR2327handleFirmwareTimeout_gatedEP18M2ScalerCSCRequest : 616 -> 668
~ _OUTLINED_FUNCTION_20 : 16 -> 20
~ _OUTLINED_FUNCTION_21 : 20 -> 16
~ _OUTLINED_FUNCTION_22 : 12 -> 20
~ _OUTLINED_FUNCTION_23 : 20 -> 12
~ _OUTLINED_FUNCTION_24 : 12 -> 20
~ _OUTLINED_FUNCTION_25 : 24 -> 12
~ _OUTLINED_FUNCTION_26 : 16 -> 24
~ __ZN27IosaFirmwareControlMSR23Rtk25mainLogFlush_gatedContextEb : 6972 -> 6952
~ __ZN22AppleM2ScalerCSCDriver40activateAndExecuteTransform_gatedContextEP18M2ScalerCSCRequestj : 1264 -> 1332
~ __ZN16IosaPowerManager35setPartitionPowerState_gatedContextE21powerManagerPartition17powerManagerStatebP18M2ScalerCSCRequest27PowerManagerStateReasonCode : 1068 -> 1008
~ _ZN24AppleM2ScalerCSCHalMSR2327handleFirmwareTimeout_gatedEP18M2ScalerCSCRequest.cold.1 : 80 -> 76
~ _ZN24AppleM2ScalerCSCHalMSR2327handleFirmwareTimeout_gatedEP18M2ScalerCSCRequest.cold.2 : 72 -> 64
~ _ZN24AppleM2ScalerCSCHalMSR2327handleFirmwareTimeout_gatedEP18M2ScalerCSCRequest.cold.3 : 80 -> 72
+ _ZN24AppleM2ScalerCSCHalMSR2327handleFirmwareTimeout_gatedEP18M2ScalerCSCRequest.cold.4
~ _ZN24AppleM2ScalerCSCHalMSR2337tryExecuteGangedFrameDescriptor_gatedEP18M2ScalerCSCRequest.cold.1 : 76 -> 84
~ _ZN24AppleM2ScalerCSCHalMSR2317canEnqueueRequestEPK18M2ScalerCSCRequest.cold.2 : 68 -> 76
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR28.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR29.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR30.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR29Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR30Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR29.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR27.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaTunableControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/K2KTests.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR29.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MSR23CurvatureLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MailBox.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MailBoxMSR26.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/Request.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P9HXzD/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
+ "12222222222212111111112111111111111111111122122112221122211111121112222222221111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220002000000022222000"
+ "Scaler [%d]: Flushing in-flight requests after %d stalls during power-down\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR28.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR29.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR30.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR29Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR30Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR29.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR27.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaTunableControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/K2KTests.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR29.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23CurvatureLUT.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MailBox.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MailBoxMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/Request.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5mR4ha/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
- "12222222222212111111112111111111111111111122122112221122211111121112222222221111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220002000000022200000"
```

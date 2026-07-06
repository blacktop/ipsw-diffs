## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-  __TEXT.__text: 0x8d880
-  __TEXT.__objc_methlist: 0x36cc
+  __TEXT.__text: 0x8dd24
+  __TEXT.__objc_methlist: 0x372c
   __TEXT.__const: 0x1cb0
-  __TEXT.__gcc_except_tab: 0xde0
+  __TEXT.__gcc_except_tab: 0xdec
   __TEXT.__oslogstring: 0x6b0c
-  __TEXT.__cstring: 0x38f1
+  __TEXT.__cstring: 0x3901
   __TEXT.__constg_swiftt: 0x7fc
-  __TEXT.__swift5_typeref: 0xcaa
+  __TEXT.__swift5_typeref: 0xd14
   __TEXT.__swift5_reflstr: 0x851
   __TEXT.__swift5_fieldmd: 0x718
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_proto: 0x11c
   __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x17f8
+  __TEXT.__unwind_info: 0x17d8
   __TEXT.__eh_frame: 0xe90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x1020
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x238
+  __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2df8
+  __DATA_CONST.__objc_selrefs: 0x2e18
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xc8
-  __DATA_CONST.__got: 0xd30
+  __DATA_CONST.__got: 0xd38
   __AUTH_CONST.__const: 0x1260
-  __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0x68d0
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0x6928
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x11b8
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x4b4
-  __DATA.__data: 0x1758
+  __DATA.__objc_ivar: 0x4b8
+  __DATA.__data: 0x1738
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1160
+  __DATA.__bss: 0x10e0
   __DATA_DIRTY.__objc_data: 0x11c0
-  __DATA_DIRTY.__data: 0xc48
-  __DATA_DIRTY.__bss: 0x1180
+  __DATA_DIRTY.__data: 0xc90
+  __DATA_DIRTY.__bss: 0x1200
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/HealthKitOrchestrationAdditions.framework/HealthKitOrchestrationAdditions
   - /System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles
   - /System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration
+  - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2352
-  Symbols:   5954
-  CStrings:  1114
+  Functions: 2347
+  Symbols:   5970
+  CStrings:  1115
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[HDMCAnalysisManager registerObserver:queue:userInitiated:needsCycles:]
+ -[HDMCDailyMetric hasBleedingPostMenopauseSamples]
+ -[HDMCDailyMetric logBleedingPostMenopauseEnabled]
+ -[HDMCDailyMetric setBleedingPostMenopauseSamples:]
+ -[HDMCDailyMetric setLogBleedingPostMenopauseEnabled:]
+ -[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:]
+ -[HDMCProfileExtension getMenopauseModelProvider]
+ GCC_except_table72
+ GCC_except_table82
+ _HKMCDisplayTypeIdentifierBleedingAfterMenopauseFlow
+ _HKMCPrivateMetadataKeyConfirmedDeviationUserDeclinedMenopauseStageAtConfirmation
+ _OBJC_IVAR_$_HDMCAnalysisManager._cyclesNeedingObservers
+ _OBJC_IVAR_$_HDMCDailyMetric._bleedingPostMenopauseSamples
+ _OBJC_IVAR_$_HDMCDailyMetric._logBleedingPostMenopauseEnabled
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKMCMenopauseModelProvidingInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKMCMenopauseModelProvidingInterface
+ __OBJC_$_PROTOCOL_REFS_HKMCMenopauseModelProvidingInterface
+ __OBJC_LABEL_PROTOCOL_$_HKMCMenopauseModelProvidingInterface
+ __OBJC_PROTOCOL_$_HKMCMenopauseModelProvidingInterface
+ ___251-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:]_block_invoke
+ ___251-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:]_block_invoke_2
+ ___72-[HDMCAnalysisManager registerObserver:queue:userInitiated:needsCycles:]_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_166_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r_e28_v24?0"HKMCDaySummary"8^B16lr80l8s32l8r88l8s40l8s48l8r96l8r104l8r112l8r120l8s56l8s64l8r128l8s72l8
+ ___block_descriptor_49_e8_32s_e34_16?0"HKMCUnconfirmedDeviation"8ls32l8
+ ___swift_closure_destructor.14Tm
+ _objc_msgSend$hasBleedingPostMenopauseSamples
+ _objc_msgSend$logBleedingPostMenopauseEnabled
+ _objc_msgSend$needsCycles
+ _objc_msgSend$registerObserver:queue:userInitiated:needsCycles:
+ _objc_msgSend$remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:
+ _objc_msgSend$setBleedingPostMenopauseSamples:
+ _objc_msgSend$setLogBleedingPostMenopauseEnabled:
+ _symbolic _____ySaySo15HKDeletedObjectCGSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySo39HDCodableMenstrualCyclesExperienceModelCG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 27HealthMenstrualCyclesDaemon20HDMCAnalysisExecutorC7PlannerC5State33_57580856FC49E16A24C9DF95B8FF534CLLV
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 27HealthMenstrualCyclesDaemon20HDMCPregnancyManagerC5State33_865A72A9437EC0D5F8ABCC85373490A0LLV
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 27HealthMenstrualCyclesDaemon25HDMCMenopauseStateManagerC0H0031_495C53339DF1A80222D5AF25A29592M0LLV
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 27HealthMenstrualCyclesDaemon32HDMCAnalysisOrchestrationManagerC5State33_91BAC5C98FA3A8C6CB34E60FFD2D1508LLV
- -[HDMCDailyMetric hasBleedingAfterMenopauseSamples]
- -[HDMCDailyMetric logBleedingAfterMenopauseEnabled]
- -[HDMCDailyMetric setBleedingAfterMenopauseSamples:]
- -[HDMCDailyMetric setLogBleedingAfterMenopauseEnabled:]
- GCC_except_table71
- GCC_except_table81
- _OBJC_IVAR_$_HDMCDailyMetric._bleedingAfterMenopauseSamples
- _OBJC_IVAR_$_HDMCDailyMetric._logBleedingAfterMenopauseEnabled
- ___216-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:completion:]_block_invoke
- ___216-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:completion:]_block_invoke_2
- ___60-[HDMCAnalysisManager registerObserver:queue:userInitiated:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_163_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r_e28_v24?0"HKMCDaySummary"8^B16ls32l8r80l8s40l8r88l8s48l8s56l8r96l8r104l8r112l8r120l8s64l8r128l8s72l8
- ___block_descriptor_48_e8_32s_e34_16?0"HKMCUnconfirmedDeviation"8ls32l8
- ___swift_closure_destructor.16Tm
- _get_type_metadata 15Synchronization5MutexVy27HealthMenstrualCyclesDaemon20HDMCAnalysisExecutorC7PlannerC5State33_57580856FC49E16A24C9DF95B8FF534CLLVG noncopyable
- _get_type_metadata 15Synchronization5MutexVy27HealthMenstrualCyclesDaemon20HDMCPregnancyManagerC5State33_865A72A9437EC0D5F8ABCC85373490A0LLVG noncopyable
- _get_type_metadata 15Synchronization5MutexVy27HealthMenstrualCyclesDaemon25HDMCMenopauseStateManagerC0H0031_495C53339DF1A80222D5AF25A29592M0LLVG noncopyable
- _get_type_metadata 15Synchronization5MutexVy27HealthMenstrualCyclesDaemon32HDMCAnalysisOrchestrationManagerC5State33_91BAC5C98FA3A8C6CB34E60FFD2D1508LLVG noncopyable
- _get_type_metadata 15Synchronization5MutexVySaySo15HKDeletedObjectCGSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVySo39HDCodableMenstrualCyclesExperienceModelCG noncopyable
- _objc_msgSend$hasBleedingAfterMenopauseSamples
- _objc_msgSend$logBleedingAfterMenopauseEnabled
- _objc_msgSend$setBleedingAfterMenopauseSamples:
- _objc_msgSend$setLogBleedingAfterMenopauseEnabled:
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "HKMCAnalysisManagerCyclesNeedingObservers"
+ "hasBleedingPostMenopauseSamples"
+ "settings_logBleedingPostMenopauseEnabled"
- "com.apple.Health"
- "hasBleedingAfterMenopauseSamples"
- "logBleedingAfterMenopauseEnabled"

```

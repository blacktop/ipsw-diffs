## HealthMenstrualCycles

> `/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles`

```diff

-  __TEXT.__text: 0x2dc58
-  __TEXT.__objc_methlist: 0x3794
+  __TEXT.__text: 0x2debc
+  __TEXT.__objc_methlist: 0x37d4
   __TEXT.__const: 0x59e
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__cstring: 0x3f56
-  __TEXT.__oslogstring: 0x2566
+  __TEXT.__cstring: 0x3fe6
+  __TEXT.__oslogstring: 0x2580
   __TEXT.__ustring: 0x166
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x6e

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf98
+  __DATA_CONST.__const: 0xfa8
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2130
+  __DATA_CONST.__objc_selrefs: 0x2150
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__got: 0x5d0
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x3380
-  __AUTH_CONST.__objc_const: 0x6858
+  __AUTH_CONST.__cfstring: 0x33e0
+  __AUTH_CONST.__objc_const: 0x68c0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x390
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x480
+  __DATA.__objc_ivar: 0x488
   __DATA.__data: 0xb80
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x9b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1333
-  Symbols:   4702
-  CStrings:  1012
+  Functions: 1337
+  Symbols:   4718
+  CStrings:  1018
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[HKMCAnalysisQuery initWithForceAnalysis:userInitiated:needsInitialResult:needsCycles:updateHandler:]
+ -[HKMCAnalysisQuery needsCycles]
+ -[HKMCAnalysisQueryConfiguration needsCycles]
+ -[HKMCAnalysisQueryConfiguration setNeedsCycles:]
+ -[HKMenstrualCyclesStore confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:]
+ _HKMCAddMenopauseStageOnboardingEligibilityDateKey
+ _HKMCPrivateMetadataKeyConfirmedDeviationUserDeclinedMenopauseStageAtConfirmation
+ _OBJC_IVAR_$_HKMCAnalysisQuery._needsCycles
+ _OBJC_IVAR_$_HKMCAnalysisQueryConfiguration._needsCycles
+ ___250-[HKMenstrualCyclesStore confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:]_block_invoke
+ ___250-[HKMenstrualCyclesStore confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80bs_e50_v16?0"<HDMenstrualCyclesPluginServerInterface>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _objc_msgSend$confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:
+ _objc_msgSend$initWithForceAnalysis:userInitiated:needsInitialResult:needsCycles:updateHandler:
+ _objc_msgSend$needsCycles
+ _objc_msgSend$remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:overrideUserDeclinedMenopauseStage:completion:
+ _objc_msgSend$setNeedsCycles:
- -[HKMenstrualCyclesStore confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:completion:]
- ___215-[HKMenstrualCyclesStore confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:completion:]_block_invoke
- ___215-[HKMenstrualCyclesStore confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:completion:]_block_invoke_2
- ___block_descriptor_96_e8_32s40s48s56s64s72bs_e50_v16?0"<HDMenstrualCyclesPluginServerInterface>"8ls32l8s40l8s48l8s56l8s64l8s72l8
- _objc_msgSend$confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:overridePerimenopauseContextState:completion:
CStrings:
+ "HKMCAddMenopauseStageOnboardingEligibilityDate"
+ "NeedsCycles"
+ "[%{public}@:%{public}@] Configured with forced analysis: %{public}@, user initiated: %{public}@, needs initial result: %{public}@, needs cycles: %{public}@"
+ "_HKPrivateMetadataKeyHKMCConfirmedDeviationUserDeclinedMenopauseStageAtConfirmation"
- "[%{public}@:%{public}@] Configured with forced analysis: %{public}@, user initiated: %{public}@, needs initial result: %{public}@"

```

## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-  __TEXT.__text: 0x2476c
-  __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0x768
+  __TEXT.__text: 0x256a4
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_stubs: 0x1b20
+  __TEXT.__objc_methlist: 0x778
   __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x8ff0
-  __TEXT.__objc_methname: 0x1c02
-  __TEXT.__oslogstring: 0x26df
+  __TEXT.__cstring: 0x9529
+  __TEXT.__objc_methname: 0x1c2a
+  __TEXT.__oslogstring: 0x2745
   __TEXT.__objc_classname: 0x128
   __TEXT.__objc_methtype: 0x52c
-  __TEXT.__gcc_except_tab: 0x720
-  __TEXT.__unwind_info: 0x598
-  __DATA_CONST.__const: 0x750
+  __TEXT.__gcc_except_tab: 0x748
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__cfstring: 0x1a80
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x6f0
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__auth_got: 0x6f8
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__auth_ptr: 0x98
   __DATA.__objc_const: 0x938
-  __DATA.__objc_selrefs: 0x830
+  __DATA.__objc_selrefs: 0x838
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x19a0

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/Versions/A/CoreRepairCore
   - /System/Library/PrivateFrameworks/HID.framework/Versions/A/HID
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/Versions/A/IntelligencePlatform
-  - /System/Library/PrivateFrameworks/NearField.framework/Versions/A/NearField
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/Versions/A/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/Versions/A/ProactiveInputPredictions

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 341
-  Symbols:   307
-  CStrings:  2423
+  Functions: 343
+  Symbols:   308
+  CStrings:  2482
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _PLSysdiagnoseCopyLogs
CStrings:
+ "AlignedFastReadDisturbs"
+ "AlignedRegularReadDisturbs"
+ "Background powerlog SPI not found"
+ "Background powerlogs did not succeed"
+ "Background powerlogs timed out"
+ "_backgroundPowerTaskForDir:withTimeout:"
+ "bandCyclesHisto"
+ "bandCyclesHistoStart"
+ "cbdrRefreshGradesHP"
+ "cbdrRefreshGradesMP"
+ "cbdrStatusHP"
+ "cbdrStatusMP"
+ "fairPurgeCompleteCount"
+ "fairPurgeStartCount"
+ "fairPurgeValidityDeltaSectors"
+ "fairPurgeValidityIncreasedCount"
+ "gcSlowInlineT0ReadLatencyHisto"
+ "gcSlowInlineT0Reads"
+ "gcSlowIsT0ReadLatencyHisto"
+ "gcSlowIsT0Reads"
+ "gcSlowT0ReadLatencyHisto"
+ "gcSlowT0Reads"
+ "hotBandsClass"
+ "idleStackAvgValidityAtSlowGC"
+ "idleStackCurrentUrgency"
+ "idleStackFullnessAtSlowGC"
+ "idleStackHighWritesDailyHisto"
+ "idleStackPhaseDurationAlignFast"
+ "idleStackPhaseDurationAlignRegular"
+ "idleStackPhaseDurationCbdr"
+ "idleStackPhaseDurationPurgeable"
+ "idleStackPhaseDurationSquareGC1"
+ "idleStackPhaseDurationSquareGC2"
+ "idleStackPhaseDurationSquareGC3"
+ "idleStackPhaseDurationWearlevel"
+ "idleStackSectorsToHigh"
+ "idleStackSectorsToSlowGC"
+ "idleStackSlowGCDailyHisto"
+ "idleStackSlowGCSrcRankHisto"
+ "idleStackTimeToSlowGC"
+ "idleStackValidityCurveAtIdleStackStart"
+ "istkHostWritesToHighUrgency"
+ "istkHostWritesToMedUrgency"
+ "istkHoursSinceAlignFast"
+ "istkHoursSinceAlignRegular"
+ "istkHoursSinceSquare"
+ "istkHoursSinceWearLevel"
+ "istkLastAlignFastHr"
+ "istkLastAlignRegularHr"
+ "istkLastFullDoneHostWrites"
+ "istkLastSquareHr"
+ "istkLastWearLevelHr"
+ "istkSecsSinceLastSidebarGen"
+ "istkValidLbasDeltaToHighUrgency"
+ "istkValidLbasDeltaToMedUrgency"
+ "massScanLastDebugInfo"
+ "massScanStatus"
+ "numIdleStackDays"
+ "progTempDeltaHisto"
+ "purgeableBandCyclesHisto"
+ "purgeableBandCyclesHistoStart"
+ "purgeableVcurve"
+ "purgeableVcurveAtIdleStackSquareUpEnd"
+ "purgeableVcurveAtSlowGC"
+ "qosEventHighLatency"
+ "qosEventSmallReadLatency"
+ "sidebarLastValidWallTime"
+ "slowGcMustReasons"
+ "totalReadAmpAtBoot"
+ "unalignedPageReads"
+ "vcurveAtSlowGC"
- "cbdrAborts"
- "cbdrInvalidGrade"
- "cbdrNeedToRefresh"
- "cbdrNoNeedToRefresh"
- "cbdrNotEnoughReads"
- "cbdrRefreshGrades"
- "idleStackNandWritesPerRoundHigh"
- "idleStackNandWritesPerRoundLow"
- "idleStackNandWritesPerRoundMed"
- "idleStackNandWritesRoundHighIdx"
- "idleStackNandWritesRoundLowIdx"
- "idleStackNandWritesRoundMedIdx"

```

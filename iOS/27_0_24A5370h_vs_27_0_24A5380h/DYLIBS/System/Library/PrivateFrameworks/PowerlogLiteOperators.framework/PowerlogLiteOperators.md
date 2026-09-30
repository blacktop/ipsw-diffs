## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-  __TEXT.__text: 0x4cb598
-  __TEXT.__objc_methlist: 0x2e2b4
+  __TEXT.__text: 0x4cea50
+  __TEXT.__objc_methlist: 0x2e334
   __TEXT.__const: 0x2cb0
   __TEXT.__swift5_typeref: 0x710
   __TEXT.__constg_swiftt: 0x544

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x5dd2a
+  __TEXT.__cstring: 0x5e5c6
   __TEXT.__swift5_capture: 0x73c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
-  __TEXT.__swift_as_cont: 0xbc
-  __TEXT.__oslogstring: 0x154ca
+  __TEXT.__swift_as_cont: 0xd0
+  __TEXT.__oslogstring: 0x155b9
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x2cdc
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x81d8
-  __TEXT.__eh_frame: 0x1688
+  __TEXT.__unwind_info: 0x8210
+  __TEXT.__eh_frame: 0x16d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x93f8
+  __DATA_CONST.__const: 0x9400
   __DATA_CONST.__objc_classlist: 0xa10
   __DATA_CONST.__objc_nlclslist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14588
+  __DATA_CONST.__objc_selrefs: 0x145e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xaf0
-  __DATA_CONST.__objc_arraydata: 0x16620
-  __DATA_CONST.__got: 0x1ae0
-  __AUTH_CONST.__const: 0x29f8
-  __AUTH_CONST.__cfstring: 0x74840
-  __AUTH_CONST.__objc_const: 0x36e68
+  __DATA_CONST.__objc_arraydata: 0x16670
+  __DATA_CONST.__got: 0x1ae8
+  __AUTH_CONST.__const: 0x2a18
+  __AUTH_CONST.__cfstring: 0x74e00
+  __AUTH_CONST.__objc_const: 0x36f28
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x6e40
   __AUTH_CONST.__objc_arrayobj: 0x2fa0
-  __AUTH_CONST.__objc_dictobj: 0x5078
+  __AUTH_CONST.__objc_dictobj: 0x50a0
   __AUTH_CONST.__objc_doubleobj: 0x1310
   __AUTH_CONST.__auth_got: 0x1950
-  __AUTH.__objc_data: 0x2c10
+  __AUTH.__objc_data: 0x28f0
   __AUTH.__data: 0x668
   __DATA.__objc_ivar: 0x1ea0
-  __DATA.__data: 0x1128
+  __DATA.__data: 0x10f8
   __DATA.__common: 0x1f8
   __DATA.__bss: 0x26f0
-  __DATA_DIRTY.__objc_ivar: 0x12f4
-  __DATA_DIRTY.__objc_data: 0x3b48
-  __DATA_DIRTY.__data: 0x6f8
-  __DATA_DIRTY.__bss: 0x4438
+  __DATA_DIRTY.__objc_ivar: 0x1304
+  __DATA_DIRTY.__objc_data: 0x3e68
+  __DATA_DIRTY.__data: 0x728
+  __DATA_DIRTY.__bss: 0x4440
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19329
-  Symbols:   52062
-  CStrings:  34179
+  Functions: 19348
+  Symbols:   52106
+  CStrings:  34328
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[PLBatteryAgent entryEventBackwardDefinitionPowerDistribution]
+ +[PLDisplayAgent hasAppleARMBacklightPublisher]
+ -[PLAudioAgent activeMediaPlaybackAssertions]
+ -[PLAudioAgent handleMediaPlaybackAssertionEntry:]
+ -[PLAudioAgent mediaPlaybackAssertionListener]
+ -[PLAudioAgent setActiveMediaPlaybackAssertions:]
+ -[PLAudioAgent setMediaPlaybackAssertionListener:]
+ -[PLBatteryAgent lastPowerDistribution]
+ -[PLBatteryAgent logInputPowerDistribution:]
+ -[PLBatteryAgent logInputPowerDistributionToCA:]
+ -[PLBatteryAgent setLastPowerDistribution:]
+ -[PLXPCAgent clientDroppedEventsXPCListener]
+ -[PLXPCAgent logEventBackwardClientDroppedEvents:]
+ -[PLXPCAgent setClientDroppedEventsXPCListener:]
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table154
+ GCC_except_table157
+ GCC_except_table174
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table247
+ GCC_except_table257
+ GCC_except_table259
+ GCC_except_table268
+ GCC_except_table275
+ GCC_except_table282
+ GCC_except_table321
+ GCC_except_table324
+ GCC_except_table328
+ GCC_except_table433
+ ___40-[PLAudioAgent initOperatorDependancies]_block_invoke_2
+ ___47+[PLDisplayAgent hasAppleARMBacklightPublisher]_block_invoke
+ ___48-[PLBatteryAgent logInputPowerDistributionToCA:]_block_invoke
+ ___block_descriptor_120_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ _kPLBatteryAgentEventBackwardNamePowerDistribution
+ _objc_msgSend$activeMediaPlaybackAssertions
+ _objc_msgSend$entryEventBackwardDefinitionPowerDistribution
+ _objc_msgSend$getDeviceStateValueWithCompletion:
+ _objc_msgSend$handleMediaPlaybackAssertionEntry:
+ _objc_msgSend$hasAppleARMBacklightPublisher
+ _objc_msgSend$initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:
+ _objc_msgSend$lastPowerDistribution
+ _objc_msgSend$logEventBackwardClientDroppedEvents:
+ _objc_msgSend$logInputPowerDistribution:
+ _objc_msgSend$logInputPowerDistributionToCA:
+ _objc_msgSend$setClientDroppedEventsXPCListener:
+ _objc_msgSend$setLastPowerDistribution:
- -[PLDebugService fireSignificantBatteryChangeNotification]
- -[PLDebugService testArchive]
- GCC_except_table109
- GCC_except_table133
- GCC_except_table137
- GCC_except_table156
- GCC_except_table185
- GCC_except_table190
- GCC_except_table244
- GCC_except_table253
- GCC_except_table258
- GCC_except_table266
- GCC_except_table272
- GCC_except_table278
- GCC_except_table320
- GCC_except_table323
- GCC_except_table327
- GCC_except_table431
- ___block_descriptor_108_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
- _objc_msgSend$fireSignificantBatteryChangeNotification
- _objc_msgSend$getDeviceStateWithCompletion:
- _objc_msgSend$runActivityWithLastCompletedDate:
- _objc_msgSend$testArchive
CStrings:
+ "ANE0"
+ "ANE1"
+ "AlignedFastReadDisturbs"
+ "AlignedRegularReadDisturbs"
+ "ChargerAccumEfficiencyCount"
+ "ChargerAccumulatedEfficiency"
+ "ChargerCount"
+ "ChargerEfficiency"
+ "ChargerHwIlimBackoffReason"
+ "ChargerIBUS"
+ "ChargerPower"
+ "ChargerVBUS"
+ "ClientDroppedEvents"
+ "ClientDroppedEvents payload: %@"
+ "ECPU_CORE0_NRG"
+ "ECPU_CORE0_SRM_NRG"
+ "ECPU_CORE1_NRG"
+ "ECPU_CORE1_SRM_NRG"
+ "ECPU_CORE2_NRG"
+ "ECPU_CORE2_SRM_NRG"
+ "ECPU_CORE3_NRG"
+ "ECPU_CORE3_SRM_NRG"
+ "ECPU_CPM_NRG"
+ "ECPU_CPM_SRM_NRG"
+ "ECPU_NRG"
+ "IPDChargingAllowed"
+ "IPDInputCurrent"
+ "IPDInputPower"
+ "IPDInputVoltage"
+ "IPDRatioOverride"
+ "IPDWattageOverride"
+ "InstantBootAdapterReady"
+ "InstantBootCount"
+ "InstantBootFailure"
+ "InstantBootGGReady"
+ "OPDDualChargerState"
+ "PCPU0_CORE0_NRG"
+ "PCPU0_CORE0_SRM_NRG"
+ "PCPU0_CORE1_NRG"
+ "PCPU0_CORE1_SRM_NRG"
+ "PCPU0_CPM_NRG"
+ "PCPU0_CPM_SRM_NRG"
+ "PCPU_NRG"
+ "PLPowerAssertionAgent_EventForward_Assertion"
+ "PowerDistribution"
+ "Pushing InputPowerDistribution to CA: %@"
+ "SystemCapability100ms_Battery0"
+ "SystemCapability100ms_Battery1"
+ "SystemCapability1sec_Battery0"
+ "SystemCapability1sec_Battery1"
+ "SystemCapabilityInsta_Battery0"
+ "SystemCapabilityInsta_Battery1"
+ "XPCMetrics::ClientDroppedEvents"
+ "[OnDeviceACAMSBC] Skipping offset %@: payload entry is %{public}@, expected NSDictionary"
+ "[OnDeviceACAMSBC] Skipping offset %@: timeSinceLastSBC is %{public}@, expected NSNumber/NSString"
+ "bandCyclesHisto"
+ "bandCyclesHistoStart"
+ "cbdrRefreshGradesHP"
+ "cbdrRefreshGradesMP"
+ "cbdrStatusHP"
+ "cbdrStatusMP"
+ "com.apple.power.battery.InputPowerDistribution"
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
- "-[PLDebugService testArchive]"
- "HERE: Line: %d"
- "Manually firing SBC"
- "PLDebugService::testArchive"
- "cbdrAborts"
- "cbdrInvalidGrade"
- "cbdrNeedToRefresh"
- "cbdrNoNeedToRefresh"
- "cbdrNotEnoughReads"
- "cbdrRefreshGrades"
- "com.apple.powerlogd.archive"
- "com.apple.powerlogd.fireSBC"
- "idleStackNandWritesPerRoundHigh"
- "idleStackNandWritesPerRoundLow"
- "idleStackNandWritesPerRoundMed"
- "idleStackNandWritesRoundHighIdx"
- "idleStackNandWritesRoundLowIdx"
- "idleStackNandWritesRoundMedIdx"

```

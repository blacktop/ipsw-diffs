## NANDInfo_osx

> `/System/Library/PrivateFrameworks/NANDInfo_osx.framework/Versions/A/NANDInfo_osx`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-847.0.0.0.0
-  __TEXT.__text: 0x23238
+849.0.5.0.0
+  __TEXT.__text: 0x23f00
   __TEXT.__objc_methlist: 0x344
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0xf76c
+  __TEXT.__cstring: 0x103b7
   __TEXT.__oslogstring: 0x12eb
   __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x10298
+  __DATA_CONST.__objc_arraydata: 0x11260
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x130
-  __AUTH_CONST.__cfstring: 0x13f00
+  __AUTH_CONST.__cfstring: 0x14f00
   __AUTH_CONST.__objc_const: 0x6b8
-  __AUTH_CONST.__objc_intobj: 0x12b58
-  __AUTH_CONST.__objc_arrayobj: 0xbee0
+  __AUTH_CONST.__objc_intobj: 0x13c80
+  __AUTH_CONST.__objc_arrayobj: 0xcab0
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__auth_got: 0x380
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x16c0
   __DATA.__objc_ivar: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 309
-  Symbols:   592
-  CStrings:  2976
+  Symbols:   594
+  CStrings:  3105
 
Symbols:
+ _os_variant_is_basesystem
+ _statfs
Functions:
~ _buildFTLStatsArrayDictionary : 25876 -> 28492
~ _buildMSPStatsArrayDictionary : 7056 -> 7440
~ _createAndLogSMagFTLFieldsToCoreAnalyticsForEvent : 1760 -> 1768
~ _GetSystemInfo : 692 -> 956
CStrings:
+ "/System/Volumes/macOS"
+ "AlignedFastReadDisturbs"
+ "AlignedRegularReadDisturbs"
+ "bandCyclesHisto"
+ "bandCyclesHistoStart"
+ "blockMassScanOnRaidConversion"
+ "cbdrStatusHP"
+ "cbdrStatusMP"
+ "com.apple.massStorage.NANDInfo.SM.FTLStatArray_6"
+ "controller_vs_nand_temp_diff_"
+ "dspExceptionParameter170"
+ "dspExceptionParameter171"
+ "ess_segments_"
+ "fairPurgeCompleteCount"
+ "fairPurgeStartCount"
+ "fairPurgeValidityDeltaSectors"
+ "fairPurgeValidityIncreasedCount"
+ "gcDestPurgeable"
+ "gcFastActiveReasons"
+ "gcRoundTime"
+ "gcSlowActiveReasons"
+ "gcSlowInlineT0ReadLatencyHisto"
+ "gcSlowIsT0ReadLatencyHisto"
+ "gcSlowT0ReadLatencyHisto"
+ "hostBandsSinceSquare"
+ "hotBandsClass"
+ "idleStackAvgValidityAtSlowGC"
+ "idleStackBadListLBAs"
+ "idleStackCurrentUrgency"
+ "idleStackFlavorLimited"
+ "idleStackFlowVCurveCDPEnd"
+ "idleStackFlowVCurveCDPStart"
+ "idleStackFullnessAtSlowGC"
+ "idleStackHighWritesDailyHisto"
+ "idleStackNandWritesUrgencyHigh"
+ "idleStackNandWritesUrgencyHighLtd"
+ "idleStackNandWritesUrgencyLow"
+ "idleStackNandWritesUrgencyMed"
+ "idleStackNandWritesUrgencyMedLtd"
+ "idleStackPhaseDurationAlignFast"
+ "idleStackPhaseDurationAlignRegular"
+ "idleStackPhaseDurationCbdr"
+ "idleStackPhaseDurationPurgeable"
+ "idleStackPhaseDurationSquareGC1"
+ "idleStackPhaseDurationSquareGC2"
+ "idleStackPhaseDurationSquareGC3"
+ "idleStackPhaseDurationWearlevel"
+ "idleStackPingResetPhase"
+ "idleStackSectorsToHigh"
+ "idleStackSectorsToSlowGC"
+ "idleStackSlowGCDailyHisto"
+ "idleStackSlowGCSrcRankHisto"
+ "idleStackTimeToSlowGC"
+ "idleStackValidityCurveAtIdleStackStart"
+ "idleStackWearlevelBandErasesDelta"
+ "initialReadStage14_"
+ "isExternalBoot"
+ "istkAvailSpaceSectors"
+ "istkDutyCycleSelfDeferred"
+ "istkHighSnapshotDeferred"
+ "istkHostWritesToHighUrgency"
+ "istkHostWritesToMedUrgency"
+ "istkHoursSinceAlignFast"
+ "istkHoursSinceAlignRegular"
+ "istkHoursSinceSquare"
+ "istkHoursSinceWearLevel"
+ "istkLastAlignFastHr"
+ "istkLastAlignRegularHr"
+ "istkLastCompletedPrio"
+ "istkLastDoneCalTimeHr"
+ "istkLastDoneHr"
+ "istkLastDoneHrAnyFlvr"
+ "istkLastFullDoneHostWrites"
+ "istkLastLowDoneHr"
+ "istkLastSquareHr"
+ "istkLastWearLevelHr"
+ "istkLowNoSUIExpired"
+ "istkOvpSectors"
+ "istkSavedFakeUrg"
+ "istkSecsSinceLastSidebarGen"
+ "istkValidLbasDeltaToHighUrgency"
+ "istkValidLbasDeltaToMedUrgency"
+ "istkWLUrgencyNoDestBand"
+ "lastISHighPingHr"
+ "lastISLowNoSUIPingHr"
+ "lastISLowPingHr"
+ "lastISMedPingHr"
+ "lastISPollingHr"
+ "lastISQueriedTask"
+ "massRefreshThrottleDisable"
+ "massRefreshThrottleEvict"
+ "massRefreshThrottleMassScan"
+ "massScanDeferStart"
+ "massScanDeferStop"
+ "massScanLastDebugInfo"
+ "massScanRequestWhileET"
+ "massScanStatus"
+ "massStorage_NANDInfo_SM_FTLStatArrays_6"
+ "migrationAutoPingCount"
+ "migrationAutoPingMB"
+ "migrationAutoPingStarts"
+ "nandWritesInSLCOnlyMode"
+ "numIdleStackDays"
+ "page_eviction_duration_"
+ "page_fault_load_duration_"
+ "page_swap_distance_"
+ "parallel_slip_hist_"
+ "pgHappyBandReleaseusingDeltaPmx"
+ "progTempDeltaHisto"
+ "purgeableBandCyclesHisto"
+ "purgeableBandCyclesHistoStart"
+ "purgeableVcurve"
+ "purgeableVcurveAtIdleStackSquareUpEnd"
+ "purgeableVcurveAtSlowGC"
+ "qosEventHighLatency"
+ "qosEventSmallReadLatency"
+ "shutdownGCTimeoutQLC"
+ "shutdownGCTimeoutTLC"
+ "shutdownSpbxEvictQLC"
+ "shutdownSpbxEvictTLC"
+ "slowGcMustReasons"
+ "vcurveAtSlowGC"
+ "vref_search_ofw_opt_vref_hist_"
+ "vref_search_pts_wr_vref"
+ "vref_search_pts_wr_win_size_at_opt"
+ "vref_search_rd_retries"
+ "vref_search_wr_retries"
+ "vref_search_wr_win_size_at_opt_hist_"
+ "vref_search_wr_win_size_at_vgh_hist_"
```

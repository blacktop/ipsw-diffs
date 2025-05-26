## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3100.20.2.1.6
-  __TEXT.__text: 0x9121d4
-  __TEXT.__auth_stubs: 0xb100
+3110.8.2.0.0
+  __TEXT.__text: 0x913334
+  __TEXT.__auth_stubs: 0xb120
   __TEXT.__objc_methlist: 0x193c
-  __TEXT.__cstring: 0x56083
-  __TEXT.__oslogstring: 0x3a180
+  __TEXT.__cstring: 0x5611f
+  __TEXT.__oslogstring: 0x3a385
   __TEXT.__const: 0x40890
-  __TEXT.__gcc_except_tab: 0xac0
+  __TEXT.__gcc_except_tab: 0xac8
   __TEXT.__dlopen_cstrs: 0x166
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0xf900

   __TEXT.__objc_methtype: 0x236b
   __TEXT.__objc_stubs: 0x5240
   __DATA_CONST.__got: 0x3068
-  __DATA_CONST.__const: 0x17cf8
+  __DATA_CONST.__const: 0x17d18
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_classrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x45a40
+  __AUTH_CONST.__cfstring: 0x45a80
   __AUTH_CONST.__objc_const: 0x12d8
   __AUTH_CONST.__const: 0x34208
   __AUTH_CONST.__auth_ptr: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5898
+  __AUTH_CONST.__auth_got: 0x58a8
   __AUTH.__data: 0x1218
   __AUTH.__objc_data: 0xd70
   __DATA.__objc_ivar: 0x2a8
-  __DATA.__data: 0x1f308
+  __DATA.__data: 0x1f318
   __DATA.__common: 0x16dd
   __DATA.__bss: 0x5588
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20943
-  Symbols:   56663
-  CStrings:  17632
+  Functions: 20948
+  Symbols:   56679
+  CStrings:  17646
 
Symbols:
+ GCC_except_table117
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table141
+ GCC_except_table34
+ GCC_except_table74
+ GCC_except_table75
+ _CFMakeCollectable
+ _FigStreamPlaylistIsCryptKeyEntryFreed
+ _FigUserCrashWithMessage
+ ___block_literal_global.113
+ ___block_literal_global.171
+ ___block_literal_global.182
+ ___block_literal_global.188
+ ___fpic_EnsureNextEventWillBuffer_block_invoke.99
+ ___fpic_HTTPReadCallback_block_invoke.88
+ ___fpic_NotifyServiceCurrentEvent_block_invoke.115
+ ___fpic_customURLReadCallback_block_invoke.91
+ _fpic_DequeueItemsFromInterstitialPlayer
+ _fra_issuePowerlogEvent
+ _kFigNetworkCostMonitorProperty_DisableHighSpeedHighPowerBuffering
+ _kFigReportingEventKey_PeriodicBandwidthPrediction_DetectFlatCompleteUtilizationThrottle_PredictedBandwidth
+ _kFigReportingEventKey_PeriodicBandwidthPrediction_DetectFlatCompleteUtilizationThrottle_PredictionError
+ _kFigTrialFactor_DisableHSHPBuffering
+ _segPumpGetStartupAlternateFromCache
+ _segPumpLogMessageAndCrashIfCryptKeyEntryMemoryIsFreed
+ _segPumpMediaConnectionIncludesMedia
+ _segPumpReplaceMediaFileWithDiscontinuity
- GCC_except_table116
- GCC_except_table124
- GCC_except_table127
- GCC_except_table140
- GCC_except_table32
- GCC_except_table82
- GCC_except_table83
- ___block_literal_global.114
- ___block_literal_global.168
- ___block_literal_global.176
- ___block_literal_global.185
- ___fpic_EnsureNextEventWillBuffer_block_invoke.100
- ___fpic_HTTPReadCallback_block_invoke.92
- ___fpic_NotifyServiceCurrentEvent_block_invoke.116
- ___fpic_customURLReadCallback_block_invoke.95
- _playerfig_reportPowerLogEvents
- _segPumpStreamActiveMediaConnectionIncludesMedia
CStrings:
+ "102612696: %s %s %s %s %s %@"
+ "<<<< Boss >>>> %s: (%p) Last preroll is not compatible: snippet rate changed. audioPipelineRate/timebaseRate changed from %1.2f/%1.2f to %1.2f/%1.2f."
+ "<<<< Boss >>>> %s: (%p) Last preroll is not compatible: snippetization changed from %s playback to %s playback"
+ "<SEGPUMP> %s: %{public}s: no alternates with valid codecs available"
+ "<SEGPUMP> %s: %{public}s: no non-iframe or alternates with valid codecs available"
+ "<SEGPUMP> %s: WARNING: Removing crypt key used by an active media file being fetched"
+ "<dw-orch> %s: %p %{public}@: WARNING: SelectedMediaArray is empty"
+ "<dw-orch> %s: %p %{public}@: selected media array was NULL; resolving media selection using automatic media selection. SelectedMediaArrays length is %d"
+ "DFCUT_P"
+ "DFCUT_PE"
+ "FNCM_DisableHighSpeedHighPowerBuffering"
+ "Live"
+ "N"
+ "disableHSHPBuffering"
+ "non-snippetized"
+ "preload_system_cpc"
+ "segPumpGetFirstMatchingAlternateEntry"
+ "segPumpSetupCommonCryptKeyData"
+ "snippetized"
- "%s must be greater than 0"
- "<<<< Boss >>>> %s: (%p) last preroll is not compatible: snippetization changed"
- "<dw-orch> %s: %p %{public}@: selected media array was NULL; resolving media selection using automatic media selection"
- "illegal variable use"
- "unterminated quoted string"

```

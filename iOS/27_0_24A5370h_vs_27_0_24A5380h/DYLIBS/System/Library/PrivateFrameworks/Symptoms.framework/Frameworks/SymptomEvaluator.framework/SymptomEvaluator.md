## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-  __TEXT.__text: 0x29d04c
-  __TEXT.__objc_methlist: 0x18ae0
-  __TEXT.__cstring: 0x272c4
-  __TEXT.__const: 0x1258
-  __TEXT.__oslogstring: 0x47375
-  __TEXT.__gcc_except_tab: 0x527c
+  __TEXT.__text: 0x29f910
+  __TEXT.__objc_methlist: 0x18c20
+  __TEXT.__cstring: 0x27620
+  __TEXT.__const: 0x1268
+  __TEXT.__oslogstring: 0x47b65
+  __TEXT.__gcc_except_tab: 0x52b8
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x38d
   __TEXT.__swift5_capture: 0x518

   __TEXT.network_clp: 0x4bb0
   __TEXT.baseband_clp: 0xed50
   __TEXT.bb_MAV_clp: 0x89e0
-  __TEXT.bb_INT_clp: 0x6a10
+  __TEXT.bb_INT_clp: 0x6d20
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x79d8
+  __TEXT.__unwind_info: 0x7a60
   __TEXT.__eh_frame: 0x7d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6f00
-  __DATA_CONST.__objc_classlist: 0x8a8
+  __DATA_CONST.__const: 0x6f98
+  __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd420
+  __DATA_CONST.__objc_selrefs: 0xd4a8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x5d0
+  __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x960
-  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__got: 0x10c0
   __AUTH_CONST.__const: 0x3210
-  __AUTH_CONST.__cfstring: 0x1f0a0
-  __AUTH_CONST.__objc_const: 0x411c8
+  __AUTH_CONST.__cfstring: 0x1f280
+  __AUTH_CONST.__objc_const: 0x41918
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0xa00
-  __AUTH_CONST.__objc_intobj: 0xa08
-  __AUTH_CONST.__objc_doubleobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x9f0
+  __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__auth_got: 0x1790
-  __AUTH.__objc_data: 0x13f8
+  __AUTH.__objc_data: 0x1448
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x3128
-  __DATA.__data: 0x1f28
+  __DATA.__objc_ivar: 0x3184
+  __DATA.__data: 0x1f30
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1030
   __DATA.__common: 0xa8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12178
-  Symbols:   39238
-  CStrings:  16132
+  Functions: 12215
+  Symbols:   39382
+  CStrings:  16203
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.evaluator_cfg : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[TrackedFlow wifiNonLocalInboundUsageGrandTallyAfterAdding:]
+ -[CellFallbackHandler _flushPendingSustainedDnsOut]
+ -[CellFallbackHandler _onDnsOutChangedTo:]
+ -[NetworkStateRelay setSustainedDnsOut:]
+ -[NetworkStateRelay sustainedDnsOut]
+ -[NoBackhaulHandler _captureRxRecoveryBaseline]
+ -[NoBackhaulHandler _configureBBHParamsFromPrefs:]
+ -[NoBackhaulHandler _currentBBHTunables]
+ -[NoBackhaulHandler _descriptionBBHTunables]
+ -[NoBackhaulHandler _evalBBHTunables]
+ -[NoBackhaulHandler _evaluateRxRecoveryForIteration:]
+ -[NoBackhaulHandler _initBBHTunables]
+ -[NoBackhaulHandler _recoverFromBrokenWithEgressTrigger:]
+ -[NoBackhaulHandler _setBBHConfiguration:]
+ -[NoBackhaulHandler _setTrialExperimentHandlerForTesting:]
+ -[NoBackhaulHandler trialExperimentHandler]
+ -[NoBackhaulTrialExperimentHandler .cxx_destruct]
+ -[NoBackhaulTrialExperimentHandler initWithQueue:]
+ -[NoBackhaulTrialExperimentHandler setTreatmentID:]
+ -[NoBackhaulTrialExperimentHandler setTrialTunablesBBH:]
+ -[NoBackhaulTrialExperimentHandler subscribeToTrialUpdates]
+ -[NoBackhaulTrialExperimentHandler treatmentID]
+ -[NoBackhaulTrialExperimentHandler trialExperimentWithProjectIDHasBegun:namespaceName:factorName:treatmentID:trialConfiguration:]
+ -[NoBackhaulTrialExperimentHandler trialExperimentWithProjectIDHasEnded:namespaceName:factorName:]
+ -[NoBackhaulTrialExperimentHandler trialTunablesBBH]
+ -[NoBackhaulTrialExperimentHandler unsubscribeFromTrialUpdates]
+ GCC_except_table127
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table290
+ GCC_except_table314
+ GCC_except_table356
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table371
+ GCC_except_table421
+ GCC_except_table51
+ GCC_except_table85
+ GCC_except_table91
+ _OBJC_CLASS_$_NoBackhaulTrialExperimentHandler
+ _OBJC_IVAR_$_CellFallbackHandler.sustainedDnsOutDelaySecs
+ _OBJC_IVAR_$_CellFallbackHandler.sustainedDnsOutTimer
+ _OBJC_IVAR_$_NetworkStateRelay._sustainedDnsOut
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhBrokenProgressTimeoutSecs
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhDefaultRouteProgressInPackets
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhExcessiveStayInPositiveSecs
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhFastTrackMinFallbacks
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhFastTrackProbeTimeoutSecs
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhPenaltyBoxMaxMultiplier
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhProbeTimeoutSecs
+ _OBJC_IVAR_$_NoBackhaulHandler._bbhWifiFrictionLookbackSecs
+ _OBJC_IVAR_$_NoBackhaulHandler._fastTrackEnabled
+ _OBJC_IVAR_$_NoBackhaulHandler._frictionScoreEnabled
+ _OBJC_IVAR_$_NoBackhaulHandler._hasBBHTunablesSetLocally
+ _OBJC_IVAR_$_NoBackhaulHandler._rxRecoveryEnabled
+ _OBJC_IVAR_$_NoBackhaulHandler._rxRecoveryThresholdBytes
+ _OBJC_IVAR_$_NoBackhaulHandler._rxRecoveryWindowsCount
+ _OBJC_IVAR_$_NoBackhaulHandler._rxRecoveryWindowsMetCount
+ _OBJC_IVAR_$_NoBackhaulHandler._trialExperimentHandler
+ _OBJC_IVAR_$_NoBackhaulHandler._wifiNonLocalInboundAtBaseline
+ _OBJC_IVAR_$_NoBackhaulTrialExperimentHandler._treatmentID
+ _OBJC_IVAR_$_NoBackhaulTrialExperimentHandler._trialManager
+ _OBJC_IVAR_$_NoBackhaulTrialExperimentHandler._trialTunablesBBH
+ _OBJC_METACLASS_$_NoBackhaulTrialExperimentHandler
+ __OBJC_$_INSTANCE_METHODS_NoBackhaulTrialExperimentHandler
+ __OBJC_$_INSTANCE_VARIABLES_NoBackhaulTrialExperimentHandler
+ __OBJC_$_PROP_LIST_NoBackhaulTrialExperimentHandler
+ __OBJC_CLASS_PROTOCOLS_$_NoBackhaulTrialExperimentHandler
+ __OBJC_CLASS_RO_$_NoBackhaulTrialExperimentHandler
+ __OBJC_METACLASS_RO_$_NoBackhaulTrialExperimentHandler
+ ___36-[NetworkStateRelay sustainedDnsOut]_block_invoke
+ ___40-[NetworkStateRelay setSustainedDnsOut:]_block_invoke
+ ___42-[CellFallbackHandler _onDnsOutChangedTo:]_block_invoke
+ ___57-[NoBackhaulHandler _recoverFromBrokenWithEgressTrigger:]_block_invoke
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ _kBBHBrokenProgressTimeoutSecs
+ _kBBHDefaultRouteProgressInPackets
+ _kBBHExcessiveStayInPositiveSecs
+ _kBBHFastTrackMinFallbacks
+ _kBBHFastTrackProbeTimeoutSecs
+ _kBBHParamsName
+ _kBBHPenaltyBoxMaxMultiplier
+ _kBBHProbeTimeoutSecs
+ _kBBHTcpFrictionScoreEarly
+ _kBBHWifiFrictionLookbackSecs
+ _kNetDiagOptDiagsUseGMI
+ _kSustainedDnsOutDelaySecsRNF
+ _objc_msgSend$_captureRxRecoveryBaseline
+ _objc_msgSend$_configureBBHParamsFromPrefs:
+ _objc_msgSend$_descriptionBBHTunables
+ _objc_msgSend$_evalBBHTunables
+ _objc_msgSend$_evaluateRxRecoveryForIteration:
+ _objc_msgSend$_flushPendingSustainedDnsOut
+ _objc_msgSend$_initBBHTunables
+ _objc_msgSend$_onDnsOutChangedTo:
+ _objc_msgSend$_recoverFromBrokenWithEgressTrigger:
+ _objc_msgSend$_setBBHConfiguration:
+ _objc_msgSend$setSustainedDnsOut:
+ _objc_msgSend$setTrialTunablesBBH:
+ _objc_msgSend$sustainedDnsOut
+ _objc_msgSend$trialTunablesBBH
+ _objc_msgSend$wifiNonLocalInboundUsageGrandTallyAfterAdding:
+ _wifiNonLocalInboundUsageGrandTally
- GCC_except_table116
- GCC_except_table123
- GCC_except_table129
- GCC_except_table144
- GCC_except_table199
- GCC_except_table260
- GCC_except_table262
- GCC_except_table286
- GCC_except_table289
- GCC_except_table294
- GCC_except_table304
- GCC_except_table353
- GCC_except_table354
- GCC_except_table389
- GCC_except_table96
- ___44-[NoBackhaulHandler resumedDefRouteProgress]_block_invoke
CStrings:
+ "%s (active%s/primary%s/constrained%s/expensive%s/rssifull%s/rssithresh%s/txthresh%s/arp%s/dns%s/sust-dns%s/i-dns%s/i-stuck%s/rssiexempt:%d/rnfPoll:%d/rnfFrict%s/rnfDStall%s/rnfFback%s/apsd%s/1ppservconnfric%s/tcphints:%ld/lqm:%ld/assess:%ld/advisory:%d/pwrDL:%ld/pwrUL:%ld/ic:%ld%s/txRate:%.1f/rxRate:%.1f/wfrict:%lu/wfft%s/bbh:%d)"
+ "(active == NO) OR (primary == NO) OR ( (sustainedDnsOut == NO) AND ((linkAssessment <= 4) OR (((rnfPolledScore >= 50) OR (rnfFellback == NO)) AND (apsdFailure == NO))) AND (linkAssessment > 4) AND ((rxSignalThresholded == NO) OR ((rnfPolledScore >= 50) AND (rnfDataStalled == NO))) AND ((rxSignalExemptions & 4) != 4) AND ((rxSignalExemptions & 8) != 8) AND ((rxSignalExemptions & 16) != 16) )"
+ "(active == YES) AND (primary == YES) AND ( (sustainedDnsOut == YES) OR ((linkAssessment > 4) AND (((rnfPolledScore < 50) AND (rnfFellback == YES)) OR (apsdFailure == YES))) OR (linkAssessment <= 4) OR ((rxSignalThresholded == YES) AND ((rnfPolledScore < 50) OR (rnfDataStalled == YES))) OR ((rxSignalExemptions & 4) == 4) OR ((rxSignalExemptions & 8) == 8) OR ((rxSignalExemptions & 16) == 16) )"
+ "BBH: Trial configuration: %@"
+ "BBH: trialExperimentWithProjectIDHasBegun TrialTunablesBBH: %@"
+ "BBH: trialExperimentWithProjectIDHasBegun for %d/%@/%@/%@"
+ "BBH: trialExperimentWithProjectIDHasEnded for %d/%@/%@"
+ "CFSM sustainedDnsOut: armed (%.1fs)"
+ "CFSM sustainedDnsOut: cancelled (recovered before %.1fs)"
+ "CFSM sustainedDnsOut: cleared"
+ "CFSM sustainedDnsOut: cleared (admin disable)"
+ "CFSM sustainedDnsOut: fired (sustained for %.1fs)"
+ "GeoIP: Computed geohash for latitude: %{private}f, longitude: %{private}f, hashLength: %zu, geohash: %{private}@"
+ "GeoIP: Computing geohash for latitude: %{private}f, longitude: %{private}f, hashLength: %zu"
+ "Recovering from Broken on sustained Wi-Fi inbound bytes (threshold %llu)"
+ "TrialTunablesBBH"
+ "Wi-Fi non-local inbound bytes, was: %llu, is: %llu (delta %llu, threshold %llu, window %lu/%lu)"
+ "bbhBrokenProgressTimeoutSecs"
+ "bbhDefaultRouteProgressInPackets"
+ "bbhExcessiveStayInPositiveSecs"
+ "bbhFastTrackMinFallbacks"
+ "bbhFastTrackMinFallbacks %u is too small, clamping to 1"
+ "bbhFastTrackProbeTimeoutSecs"
+ "bbhPenaltyBoxMaxMultiplier"
+ "bbhPenaltyBoxMaxMultiplier %u is too small (would disable backoff), clamping to 2"
+ "bbhProbeTimeoutSecs"
+ "bbhTcpFrictionScoreEarly"
+ "bbhWifiFrictionLookbackSecs"
+ "bbh_params"
+ "config %s %@"
+ "config bbh_params, %@"
+ "config removal of %s, restoring defaults"
+ "default tunables, %@"
+ "diagsusegmi"
+ "dsTshold: %d, dsTimeSecs: %d, dsRefreshSecs: %d, probesFailureFactor: %.2f, packetsFrictionFactor %.2f, progressTimeSecs: %d, historyProgressTimeSecs: %d, maxPreferResidencyMsecs: %llu, rnfToCellRatio: %.2f, fallbackHeavyRatio: %.2f, usePolledScore: %d, rnfPolledScoreWindowSize: %lu, useOpportunistic: %d, usePrefer: %d, fallbackClosedLoop: %d, sustainedDnsOutDelaySecs: %.1f"
+ "invalid bbhFastTrackProbeTimeoutSecs %.2f, restoring default %.2f"
+ "invalid bbhProbeTimeoutSecs %.2f, restoring default %.2f"
+ "invalid bbhWifiFrictionLookbackSecs %.2f (would disable friction tracking), restoring default %.2f"
+ "invalid value '%lld' for no_backhaul_rx_recovery_threshold_bytes, keeping %llu"
+ "invalid value '%lld' for no_backhaul_rx_recovery_windows, keeping %lu"
+ "no_backhaul_fast_track_enabled"
+ "no_backhaul_rx_recovery_enabled"
+ "no_backhaul_rx_recovery_threshold_bytes"
+ "no_backhaul_rx_recovery_windows"
+ "no_backhaul_wifi_friction_score_enabled"
+ "probeTimeoutSecs: %.2f, fastTrackProbeTimeoutSecs: %.2f, penaltyBoxMaxMultiplier: %u, defaultRouteProgressInPackets: %u, brokenProgressTimeoutSecs: %u, excessiveStayInPositiveSecs: %u, wifiFrictionLookbackSecs: %.2f, fastTrackMinFallbacks: %u"
+ "re-setting no_backhaul_fast_track_enabled to default: %d"
+ "re-setting no_backhaul_rx_recovery_enabled to default: %d"
+ "re-setting no_backhaul_rx_recovery_threshold_bytes to default: %d"
+ "re-setting no_backhaul_rx_recovery_windows to default: %d"
+ "re-setting no_backhaul_wifi_friction_score_enabled to default: %d"
+ "set to a new value for no_backhaul_fast_track_enabled (was/is): %d/%d"
+ "set to a new value for no_backhaul_rx_recovery_enabled (was/is): %d/%d"
+ "set to a new value for no_backhaul_rx_recovery_threshold_bytes (was/is): %llu/%lld"
+ "set to a new value for no_backhaul_rx_recovery_windows (was/is): %lu/%lld"
+ "set to a new value for no_backhaul_wifi_friction_score_enabled (was/is): %d/%d"
+ "stayed in Positive for %llu seconds (> %u seconds)."
+ "sustainedDnsOut"
+ "sustainedDnsOutDelaySecs"
+ "trial-augmented tunables, treatmentID: %@, %@"
+ "trialTunablesBBH"
+ "trialTunablesBBH changed, re-evaluating tunables"
+ "wifiInboundProgress"
- "%s (active%s/primary%s/constrained%s/expensive%s/rssifull%s/rssithresh%s/txthresh%s/arp%s/dns%s/i-dns%s/i-stuck%s/rssiexempt:%d/rnfPoll:%d/rnfFrict%s/rnfDStall%s/rnfFback%s/apsd%s/1ppservconnfric%s/tcphints:%ld/lqm:%ld/assess:%ld/advisory:%d/pwrDL:%ld/pwrUL:%ld/ic:%ld%s/txRate:%.1f/rxRate:%.1f/wfrict:%lu/wfft%s/bbh:%d)"
- "(active == NO) OR (primary == NO) OR ( (dnsOut == NO) AND ((linkAssessment <= 4) OR (((rnfPolledScore >= 50) OR (rnfFellback == NO)) AND (apsdFailure == NO))) AND (linkAssessment > 4) AND ((rxSignalThresholded == NO) OR ((rnfPolledScore >= 50) AND (rnfDataStalled == NO))) AND ((rxSignalExemptions & 4) != 4) AND ((rxSignalExemptions & 8) != 8) AND ((rxSignalExemptions & 16) != 16) )"
- "(active == YES) AND (primary == YES) AND ( (dnsOut == YES) OR ((linkAssessment > 4) AND (((rnfPolledScore < 50) AND (rnfFellback == YES)) OR (apsdFailure == YES))) OR (linkAssessment <= 4) OR ((rxSignalThresholded == YES) AND ((rnfPolledScore < 50) OR (rnfDataStalled == YES))) OR ((rxSignalExemptions & 4) == 4) OR ((rxSignalExemptions & 8) == 8) OR ((rxSignalExemptions & 16) == 16) )"
- "GeoIP: Computed geohash for latitude: %f, longitude: %f, hashLength: %zu, geohash: %@"
- "GeoIP: Computing geohash for latitude: %f, longitude: %f, hashLength: %zu"
- "dsTshold: %d, dsTimeSecs: %d, dsRefreshSecs: %d, probesFailureFactor: %.2f, packetsFrictionFactor %.2f, progressTimeSecs: %d, historyProgressTimeSecs: %d, maxPreferResidencyMsecs: %llu, rnfToCellRatio: %.2f, fallbackHeavyRatio: %.2f, usePolledScore: %d, rnfPolledScoreWindowSize: %lu, useOpportunistic: %d, usePrefer: %d, fallbackClosedLoop: %d"
- "stayed in Positive for %llu seconds (> %d seconds)."

```

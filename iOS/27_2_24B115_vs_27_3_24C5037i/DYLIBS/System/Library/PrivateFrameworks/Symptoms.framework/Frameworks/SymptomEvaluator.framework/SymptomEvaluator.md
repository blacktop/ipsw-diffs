## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2394.40.17.0.0
-  __TEXT.__text: 0x29d0a8
-  __TEXT.__objc_methlist: 0x18ee0
-  __TEXT.__cstring: 0x27c30
-  __TEXT.__const: 0x12f8
-  __TEXT.__oslogstring: 0x480a5
-  __TEXT.__gcc_except_tab: 0x5378
+2394.60.9.0.0
+  __TEXT.__text: 0x29f258
+  __TEXT.__objc_methlist: 0x19050
+  __TEXT.__cstring: 0x27db0
+  __TEXT.__const: 0x1308
+  __TEXT.__oslogstring: 0x484c5
+  __TEXT.__gcc_except_tab: 0x541c
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x38d
   __TEXT.__swift5_capture: 0x518

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x78
-  __TEXT.evaluator_cfg: 0x6649
+  __TEXT.evaluator_cfg: 0x664b
   __TEXT.default_clp: 0x2fe0
   __TEXT.symptoms_clp: 0x6010
   __TEXT.network_clp: 0x4bb0

   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6d20
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x93b8
+  __TEXT.__unwind_info: 0x9450
   __TEXT.__eh_frame: 0x7d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x70e8
-  __DATA_CONST.__objc_classlist: 0x8c0
+  __DATA_CONST.__const: 0x7148
+  __DATA_CONST.__objc_classlist: 0x8c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd750
+  __DATA_CONST.__objc_selrefs: 0xd7e0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x5e8
+  __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x980
-  __DATA_CONST.__got: 0x10e8
+  __DATA_CONST.__got: 0x10f0
   __AUTH_CONST.__const: 0x3250
-  __AUTH_CONST.__cfstring: 0x1fbc0
-  __AUTH_CONST.__objc_const: 0x42298
+  __AUTH_CONST.__cfstring: 0x1fd80
+  __AUTH_CONST.__objc_const: 0x42828
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xa00
-  __AUTH_CONST.__objc_intobj: 0x9f0
+  __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__auth_got: 0x17d0
-  __AUTH.__objc_data: 0xf98
+  __AUTH.__objc_data: 0xfe8
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x31f4
-  __DATA.__data: 0x1f20
+  __DATA.__objc_ivar: 0x3218
+  __DATA.__data: 0x1f30
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x4808

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12302
-  Symbols:   20122
-  CStrings:  12273
+  Functions: 12351
+  Symbols:   20200
+  CStrings:  12305
 
Symbols:
+ +[NetworkAnalyticsEngine _armSustainedTimer:forValue:delaySecs:label:readUnderlying:setSustained:readSustained:]
+ +[NetworkAnalyticsEngine _clearSharedInstanceForTesting]
+ +[NetworkAnalyticsEngine _onDnsOutChangedTo:forRelay:]
+ +[NetworkAnalyticsEngine _onInternetDnsOutChangedTo:forRelay:]
+ +[NetworkAnalyticsEngine _sustainedDnsOutDelaySecsForTesting]
+ +[NetworkAnalyticsEngine _testDriveDnsOutForRelay:on:]
+ +[NetworkAnalyticsEngine _testDriveInternetDnsOutForRelay:on:]
+ +[NetworkAnalyticsEngine _testResetNetworkTunablesState]
+ +[NetworkAnalyticsEngine _testSetSustainedDnsOutDelaySecs:]
+ -[CanUseAppsCache removeEntryFor:state:]
+ -[CellFallbackHandler _evaluateExploreEvict]
+ -[CellFallbackHandler _handleBundleAddedNotification:]
+ -[CellFallbackHandler _setExploreEvictDeltaBytesForTesting:]
+ -[CellFallbackHandler _setExploreEvictHoldMsecsForTesting:]
+ -[CellFallbackHandler _setExploreEvictTimeMsecsForTesting:]
+ -[CellFallbackHandler descriptionTunablesExtended]
+ -[ConfigurationParams initWithUnderlyingDictionary:logHandle:]
+ -[NetworkAnalyticsEngine _configureNetworkParamsFromPrefs:]
+ -[NetworkAnalyticsEngine _evalNetworkTunables:treatmentID:]
+ -[NetworkAnalyticsEngine _setTrialExperimentHandlerForTesting:]
+ -[NetworkAnalyticsEngine initTestInstanceWithQueue:]
+ -[NetworkAnalyticsEngine trialExperimentHandler]
+ -[NetworkStateRelay setSustainedInternetDnsOut:]
+ -[NetworkStateRelay sustainedInternetDnsOut]
+ -[NetworkTrialExperimentHandler .cxx_destruct]
+ -[NetworkTrialExperimentHandler initWithQueue:]
+ -[NetworkTrialExperimentHandler setTreatmentID:]
+ -[NetworkTrialExperimentHandler setTrialTunablesGeneralParams:]
+ -[NetworkTrialExperimentHandler subscribeToTrialUpdates]
+ -[NetworkTrialExperimentHandler treatmentID]
+ -[NetworkTrialExperimentHandler trialExperimentWithProjectIDHasBegun:namespaceName:factorName:treatmentID:trialConfiguration:]
+ -[NetworkTrialExperimentHandler trialExperimentWithProjectIDHasEnded:namespaceName:factorName:]
+ -[NetworkTrialExperimentHandler trialTunablesGeneralParams]
+ -[NetworkTrialExperimentHandler unsubscribeFromTrialUpdates]
+ GCC_except_table100
+ GCC_except_table152
+ GCC_except_table212
+ GCC_except_table223
+ GCC_except_table262
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table292
+ GCC_except_table294
+ GCC_except_table318
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table325
+ GCC_except_table333
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table375
+ GCC_except_table380
+ GCC_except_table419
+ GCC_except_table429
+ GCC_except_table436
+ GCC_except_table447
+ GCC_except_table87
+ _OBJC_CLASS_$_NetworkTrialExperimentHandler
+ _OBJC_IVAR_$_CellFallbackHandler.bundleAddedObserver
+ _OBJC_IVAR_$_CellFallbackHandler.exploreEvictDeltaBytes
+ _OBJC_IVAR_$_CellFallbackHandler.exploreEvictHoldMsecs
+ _OBJC_IVAR_$_CellFallbackHandler.exploreEvictTimeMsecs
+ _OBJC_IVAR_$_CellFallbackHandler.exploreEvictUsageMarker
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._registeredWithCTShim
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._trialExperimentHandler
+ _OBJC_IVAR_$_NetworkStateRelay._sustainedInternetDnsOut
+ _OBJC_IVAR_$_NetworkTrialExperimentHandler._treatmentID
+ _OBJC_IVAR_$_NetworkTrialExperimentHandler._trialManager
+ _OBJC_IVAR_$_NetworkTrialExperimentHandler._trialTunablesGeneralParams
+ _OBJC_METACLASS_$_NetworkTrialExperimentHandler
+ __OBJC_$_INSTANCE_METHODS_NetworkTrialExperimentHandler
+ __OBJC_$_INSTANCE_VARIABLES_NetworkTrialExperimentHandler
+ __OBJC_$_PROP_LIST_NetworkTrialExperimentHandler
+ __OBJC_CLASS_PROTOCOLS_$_NetworkTrialExperimentHandler
+ __OBJC_CLASS_RO_$_NetworkTrialExperimentHandler
+ __OBJC_METACLASS_RO_$_NetworkTrialExperimentHandler
+ ___112+[NetworkAnalyticsEngine _armSustainedTimer:forValue:delaySecs:label:readUnderlying:setSustained:readSustained:]_block_invoke
+ ___27-[CellFallbackHandler init]_block_invoke_4
+ ___27-[CellFallbackHandler init]_block_invoke_5
+ ___44-[CellFallbackHandler _evaluateExploreEvict]_block_invoke
+ ___44-[NetworkStateRelay sustainedInternetDnsOut]_block_invoke
+ ___48-[NetworkStateRelay setSustainedInternetDnsOut:]_block_invoke
+ ___54+[NetworkAnalyticsEngine _onDnsOutChangedTo:forRelay:]_block_invoke
+ ___54+[NetworkAnalyticsEngine _onDnsOutChangedTo:forRelay:]_block_invoke_2
+ ___54+[NetworkAnalyticsEngine _onDnsOutChangedTo:forRelay:]_block_invoke_3
+ ___62+[NetworkAnalyticsEngine _onInternetDnsOutChangedTo:forRelay:]_block_invoke
+ ___62+[NetworkAnalyticsEngine _onInternetDnsOutChangedTo:forRelay:]_block_invoke_2
+ ___62+[NetworkAnalyticsEngine _onInternetDnsOutChangedTo:forRelay:]_block_invoke_3
+ ___88-[CellFallbackHandler initTestInstanceWithCellRelay:wifiRelay:motionRelay:outrankRelay:]_block_invoke_3
+ ___88-[CellFallbackHandler initTestInstanceWithCellRelay:wifiRelay:motionRelay:outrankRelay:]_block_invoke_4
+ ___block_descriptor_72_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ _hasSustainedDnsTunableSetLocally
+ _kExploreEvictDeltaBytesRNF
+ _kExploreEvictHoldMsecsRNF
+ _kExploreEvictTimeMsecsRNF
+ _kNetworkParamsName
+ _kNotificationBundleAdded
+ _kNotificationBundleIDAdded
+ _kSustainedDnsOutDelaySecs
+ _sustainedDnsOutDelaySecs
+ _sustainedDnsOutTimer
+ _sustainedInternetDnsOutTimer
- -[CellFallbackHandler _flushPendingSustainedDnsOut]
- -[CellFallbackHandler _onDnsOutChangedTo:]
- GCC_except_table121
- GCC_except_table143
- GCC_except_table217
- GCC_except_table259
- GCC_except_table260
- GCC_except_table264
- GCC_except_table265
- GCC_except_table266
- GCC_except_table272
- GCC_except_table290
- GCC_except_table293
- GCC_except_table296
- GCC_except_table298
- GCC_except_table300
- GCC_except_table301
- GCC_except_table303
- GCC_except_table308
- GCC_except_table357
- GCC_except_table358
- GCC_except_table359
- GCC_except_table393
- GCC_except_table414
- GCC_except_table54
- GCC_except_table81
- _OBJC_IVAR_$_CellFallbackHandler.sustainedDnsOutDelaySecs
- _OBJC_IVAR_$_CellFallbackHandler.sustainedDnsOutTimer
- ___42-[CellFallbackHandler _onDnsOutChangedTo:]_block_invoke
- _kSustainedDnsOutDelaySecsRNF
CStrings:
+ "\t\t\tCFSM evict action for: explore - RNF cell usage moved %llu bytes over window, withdrawing advice (was %ld) for %llu ms"
+ "\t\t\tCFSM evict no-op for: explore - RNF cell usage moved %llu bytes, advice %ld"
+ "%s (active%s/primary%s/constrained%s/expensive%s/rssifull%s/rssithresh%s/txthresh%s/arp%s/dns%s/sust-dns%s/i-dns%s/sust-i-dns%s/i-stuck%s/rssiexempt:%d/rnfPoll:%d/rnfFrict%s/rnfDStall%s/rnfFback%s/apsd%s/1ppservconnfric%s/tcphints:%ld/lqm:%ld/assess:%ld/advisory:%d/pwrDL:%ld/pwrUL:%ld/ic:%ld%s/txRate:%.1f/rxRate:%.1f/wfrict:%lu/wfft%s/bbh:%d)"
+ "(active == NO) OR (primary == NO) OR (rxSignalFullBars == NO) OR ((apsdFailure == NO) AND (sustainedDnsOut == NO) AND (tcpProgressHintsScore <= 10) AND (wifiFrictionScore <= 10) AND (wifiFrictionFastTrack == NO))"
+ "(active == NO) OR (primary == NO) OR (rxSignalFullBars == NO) OR ((sustainedDnsOut == NO) AND (tcpProgressHintsScore <= 10) AND (wifiFrictionScore <= 10))"
+ "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((apsdFailure == YES) OR (sustainedDnsOut == YES) OR (tcpProgressHintsScore > 10) OR (wifiFrictionScore > 10) OR (wifiFrictionFastTrack == YES))"
+ "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((apsdFailure == YES) OR (sustainedInternetDnsOut == YES) OR (tcpProgressHintsScore > 50) OR (wifiFrictionScore > 50) OR (wifiFrictionFastTrack == YES))"
+ "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((sustainedDnsOut == YES) OR (tcpProgressHintsScore > 10) OR (wifiFrictionScore > 10))"
+ "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((sustainedInternetDnsOut == YES) OR (tcpProgressHintsScore > 50) OR (wifiFrictionScore > 50))"
+ "BundleIDAdded"
+ "CFSM cache: removed (appName/state): %@/%ld"
+ "CFSM cache: wants non-nil args (appName): %p"
+ "CFSM extra-tunables from %s: %@"
+ "CFSM: bundle added to FAE DB, evicting stale policy cache entry for %{private}@"
+ "CFSM: bundle-added notification with no/invalid bundle name, userInfo: %{private}@"
+ "CFSM: config rnf_params extra, %@"
+ "CFSM: default tunables extra, %@"
+ "CFSM: trial-augmented tunables extra, %@"
+ "TrialTunablesGeneralParams"
+ "com.apple.symptomsd.MotionStateRelay"
+ "config %s restored to defaults, sustainedDnsOutDelaySecs: %.1f"
+ "config %s, sustainedDnsOutDelaySecs: %.1f"
+ "default tunables, sustainedDnsOutDelaySecs: %.1f"
+ "dsTshold: %d, dsTimeSecs: %d, dsRefreshSecs: %d, probesFailureFactor: %.2f, packetsFrictionFactor %.2f, progressTimeSecs: %d, historyProgressTimeSecs: %d, maxPreferResidencyMsecs: %llu, rnfToCellRatio: %.2f, fallbackHeavyRatio: %.2f, usePolledScore: %d, rnfPolledScoreWindowSize: %lu, useOpportunistic: %d, usePrefer: %d, fallbackClosedLoop: %d, fallbackClosedLoopCount: %u, fallbackClosedLoopMsecs: %llu"
+ "exploreEvictDeltaBytes"
+ "exploreEvictDeltaBytes: %llu, "
+ "exploreEvictHoldMsecs"
+ "exploreEvictHoldMsecs: %llu, "
+ "exploreEvictTimeMsecs"
+ "exploreEvictTimeMsecs: %llu, "
+ "extra-tunables (%s)"
+ "kNotificationBundleAdded"
+ "network_params"
+ "network_params: Trial configuration: %@"
+ "network_params: trialExperimentWithProjectIDHasBegun TrialTunablesGeneralParams: %@"
+ "network_params: trialExperimentWithProjectIDHasBegun for %d/%@/%@/%@"
+ "network_params: trialExperimentWithProjectIDHasEnded for %d/%@/%@"
+ "relay %s: armed (%.1fs)"
+ "relay %s: cancelled (recovered before %.1fs)"
+ "relay %s: cleared"
+ "relay %s: fired (sustained for %.1fs)"
+ "sustainedInternetDnsOut"
+ "trial-augmented tunables, treatmentID: %@, sustainedDnsOutDelaySecs: %.1f"
+ "trialTunablesGeneralParams"
+ "trialTunablesGeneralParams changed, re-evaluating tunables"
- "%s (active%s/primary%s/constrained%s/expensive%s/rssifull%s/rssithresh%s/txthresh%s/arp%s/dns%s/sust-dns%s/i-dns%s/i-stuck%s/rssiexempt:%d/rnfPoll:%d/rnfFrict%s/rnfDStall%s/rnfFback%s/apsd%s/1ppservconnfric%s/tcphints:%ld/lqm:%ld/assess:%ld/advisory:%d/pwrDL:%ld/pwrUL:%ld/ic:%ld%s/txRate:%.1f/rxRate:%.1f/wfrict:%lu/wfft%s/bbh:%d)"
- "(active == NO) OR (primary == NO) OR (rxSignalFullBars == NO) OR ((apsdFailure == NO) AND (dnsOut == NO) AND (tcpProgressHintsScore <= 10) AND (wifiFrictionScore <= 10) AND (wifiFrictionFastTrack == NO))"
- "(active == NO) OR (primary == NO) OR (rxSignalFullBars == NO) OR ((dnsOut == NO) AND (tcpProgressHintsScore <= 10) AND (wifiFrictionScore <= 10))"
- "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((apsdFailure == YES) OR (dnsOut == YES) OR (tcpProgressHintsScore > 10) OR (wifiFrictionScore > 10) OR (wifiFrictionFastTrack == YES))"
- "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((apsdFailure == YES) OR (internetDnsOut == YES) OR (tcpProgressHintsScore > 50) OR (wifiFrictionScore > 50) OR (wifiFrictionFastTrack == YES))"
- "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((dnsOut == YES) OR (tcpProgressHintsScore > 10) OR (wifiFrictionScore > 10))"
- "(active == YES) AND (primary == YES) AND (rxSignalFullBars == YES) AND ((internetDnsOut == YES) OR (tcpProgressHintsScore > 50) OR (wifiFrictionScore > 50))"
- "CFSM sustainedDnsOut: armed (%.1fs)"
- "CFSM sustainedDnsOut: cancelled (recovered before %.1fs)"
- "CFSM sustainedDnsOut: cleared"
- "CFSM sustainedDnsOut: cleared (admin disable)"
- "CFSM sustainedDnsOut: fired (sustained for %.1fs)"
- "dsTshold: %d, dsTimeSecs: %d, dsRefreshSecs: %d, probesFailureFactor: %.2f, packetsFrictionFactor %.2f, progressTimeSecs: %d, historyProgressTimeSecs: %d, maxPreferResidencyMsecs: %llu, rnfToCellRatio: %.2f, fallbackHeavyRatio: %.2f, usePolledScore: %d, rnfPolledScoreWindowSize: %lu, useOpportunistic: %d, usePrefer: %d, fallbackClosedLoop: %d, fallbackClosedLoopCount: %u, fallbackClosedLoopMsecs: %llu, sustainedDnsOutDelaySecs: %.1f"
```

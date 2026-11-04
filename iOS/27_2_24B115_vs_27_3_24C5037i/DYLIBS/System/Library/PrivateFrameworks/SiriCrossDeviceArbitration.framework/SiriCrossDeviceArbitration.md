## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3605.25.1.0.0
-  __TEXT.__text: 0x3c354
-  __TEXT.__objc_methlist: 0x3d94
+3610.8.1.0.0
+  __TEXT.__text: 0x3df00
+  __TEXT.__objc_methlist: 0x3f14
   __TEXT.__const: 0x2e8
   __TEXT.__dlopen_cstrs: 0x15c
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x5f
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x72eb
+  __TEXT.__cstring: 0x7686
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_reflstr: 0x18
   __TEXT.__swift5_fieldmd: 0x28

   __TEXT.__swift_as_cont: 0x4
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__gcc_except_tab: 0x48c
-  __TEXT.__oslogstring: 0x77f8
-  __TEXT.__unwind_info: 0x1608
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__oslogstring: 0x7e48
+  __TEXT.__unwind_info: 0x1698
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1518
-  __DATA_CONST.__objc_classlist: 0x1c8
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__const: 0x15f8
+  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2448
+  __DATA_CONST.__objc_selrefs: 0x2518
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__got: 0x3c0
   __AUTH_CONST.__const: 0x578
-  __AUTH_CONST.__cfstring: 0x3940
-  __AUTH_CONST.__objc_const: 0x6bb0
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x6e80
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x578
-  __DATA.__objc_ivar: 0x630
-  __DATA.__data: 0x30
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x65c
+  __DATA.__data: 0x90
   __DATA_DIRTY.__objc_data: 0x11d0
   __DATA_DIRTY.__data: 0x748
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1598
-  Symbols:   2992
-  CStrings:  1309
+  Functions: 1634
+  Symbols:   3063
+  CStrings:  1347
 
Symbols:
+ +[SCDADeviceRoutingPriority canLocalStandByForWinnerInCandidates:]
+ +[SCDAFeatureFlags isDeviceSelectionShadowModeEnabled]
+ +[SCDAFeatureFlags setDeviceSelectionShadowModeEnabledOverride:]
+ +[SCDAUtilities setSiriDeviceRoutingModeOverride:]
+ -[SCDACoordinator(ElectionLedger) _expireProvisionalOutcomeInLedger]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _announceStandbyBeginUnlessLedgerAnnounces]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _announceStandbyEndIfOwnedWithReason:]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _endPendingStandby]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _ledgerAnnouncesStandby]
+ -[SCDAElectionLedger _resolveEntry:withOutcome:didWin:observed:source:standbyEndReason:]
+ -[SCDAElectionLedger standbyAnnouncer]
+ -[SCDAInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withConfidence:withBoost:withCdaId:currentRequestId:withTimestamp:]
+ -[SCDAMonitor _enterPendingIfBeginIsInFlight]
+ -[SCDAMonitor _init]
+ -[SCDAMonitor _postedBeginGeneration]
+ -[SCDAMonitor _readsPublishedElectionData]
+ -[SCDAMonitor _replayEarlyReleases:]
+ -[SCDAMonitor initForTestingWithHoldCoordinator:]
+ -[SCDANotifyObserver postedStateOnQueue]
+ -[SCDARecord generateAirPodsConfidence]
+ -[SCDAStandbyAnnouncer .cxx_destruct]
+ -[SCDAStandbyAnnouncer _enqueueLocked:]
+ -[SCDAStandbyAnnouncer _isCurrentGeneration:]
+ -[SCDAStandbyAnnouncer _releaseOrphanedQueueLocked]
+ -[SCDAStandbyAnnouncer init]
+ -[SCDAStandbyAnnouncer isListening]
+ -[SCDAStandbyAnnouncer notifyStandbyDidBeginForElection:]
+ -[SCDAStandbyAnnouncer notifyStandbyDidEndForElection:reason:]
+ -[SCDAStandbyAnnouncer openStandbyIdentity]
+ -[SCDAStandbyAnnouncer removeListener:]
+ -[SCDAStandbyAnnouncer setListener:deliverOn:]
+ -[SCDAStandbyObserver _initWithAnnouncer:]
+ -[SCDAStandbyObserver deliveryQueueForTesting]
+ -[SCDAStandbyObserver initForTestingWithAnnouncer:]
+ -[SCDAStandbyObserver scdaStandbyDidBeginForElection:]
+ -[SCDAStandbyObserver scdaStandbyDidEndForElection:reason:]
+ GCC_except_table1033
+ GCC_except_table1106
+ GCC_except_table1158
+ GCC_except_table1161
+ GCC_except_table1165
+ GCC_except_table1170
+ GCC_except_table1197
+ GCC_except_table1241
+ GCC_except_table1261
+ GCC_except_table1282
+ GCC_except_table1346
+ GCC_except_table1347
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1465
+ GCC_except_table1498
+ GCC_except_table1500
+ GCC_except_table1581
+ GCC_except_table1582
+ GCC_except_table1588
+ GCC_except_table245
+ GCC_except_table251
+ GCC_except_table514
+ GCC_except_table750
+ GCC_except_table759
+ GCC_except_table918
+ GCC_except_table950
+ GCC_except_table954
+ GCC_except_table959
+ GCC_except_table962
+ GCC_except_table985
+ _OBJC_CLASS_$_SCDAStandbyAnnouncer
+ _OBJC_IVAR_$_SCDACoordinator._coordinatorStandbyIdentity
+ _OBJC_IVAR_$_SCDAElectionLedger._standbyAnnouncer
+ _OBJC_IVAR_$_SCDAMonitor._earlyReleasesBySender
+ _OBJC_IVAR_$_SCDAMonitor._lastBeginGeneration
+ _OBJC_IVAR_$_SCDAStandbyAnnouncer._deliveryQueue
+ _OBJC_IVAR_$_SCDAStandbyAnnouncer._generation
+ _OBJC_IVAR_$_SCDAStandbyAnnouncer._listener
+ _OBJC_IVAR_$_SCDAStandbyAnnouncer._lock
+ _OBJC_IVAR_$_SCDAStandbyAnnouncer._openIdentity
+ _OBJC_IVAR_$_SCDAStandbyObserver._announcer
+ _OBJC_IVAR_$_SCDAStandbyObserver._deliveryQueue
+ _OBJC_METACLASS_$_SCDAStandbyAnnouncer
+ _SCDAStandbyEndReasonDescription
+ __OBJC_$_INSTANCE_METHODS_SCDAStandbyAnnouncer
+ __OBJC_$_INSTANCE_VARIABLES_SCDAStandbyAnnouncer
+ __OBJC_$_PROP_LIST_SCDAElectionLedger
+ __OBJC_$_PROP_LIST_SCDAStandbyAnnouncer
+ __OBJC_$_PROP_LIST_SCDAStandbyObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCDAStandbyAnnouncerListening
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDAStandbyAnnouncerListening
+ __OBJC_$_PROTOCOL_REFS_SCDAStandbyAnnouncerListening
+ __OBJC_CLASS_PROTOCOLS_$_SCDAStandbyObserver
+ __OBJC_CLASS_RO_$_SCDAStandbyAnnouncer
+ __OBJC_LABEL_PROTOCOL_$_SCDAStandbyAnnouncerListening
+ __OBJC_METACLASS_RO_$_SCDAStandbyAnnouncer
+ __OBJC_PROTOCOL_$_SCDAStandbyAnnouncerListening
+ ___239-[SCDAInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withConfidence:withBoost:withCdaId:currentRequestId:withTimestamp:]_block_invoke
+ ___36-[SCDAMonitor _replayEarlyReleases:]_block_invoke
+ ___39-[SCDAMonitor _registerForMyriadEvents]_block_invoke
+ ___39-[SCDAStandbyAnnouncer _enqueueLocked:]_block_invoke
+ ___46-[SCDAStandbyAnnouncer setListener:deliverOn:]_block_invoke
+ ___57-[SCDAStandbyAnnouncer notifyStandbyDidBeginForElection:]_block_invoke
+ ___61-[SCDAMonitor releaseRoutingTargetHoldAsWon:fromSenderIdsId:]_block_invoke
+ ___62-[SCDAStandbyAnnouncer notifyStandbyDidEndForElection:reason:]_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_40_e8_32s_e41_v16?0"<SCDAStandbyAnnouncerListening>"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e41_v16?0"<SCDAStandbyAnnouncerListening>"8ls32l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_73_e8_32r40r48r56r64r_e27_v32?0"SCDARecord"8Q16^B24lr32l8r40l8r48l8r56l8r64l8
+ __deviceSelectionShadowModeEnabledOverride
+ __siriDeviceRoutingModeOverride
- +[SCDAStandbyObserver announceStandbyDidBegin]
- +[SCDAStandbyObserver announceStandbyDidEndAsWon:]
- -[SCDACoordinator(SiriDeviceRoutingStandby) _endPendingStandbyAnnouncingWon:]
- -[SCDAInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:]
- -[SCDAMonitor _setElectionDataForTesting:]
- -[SCDAMonitor initForTesting]
- -[SCDAStandbyObserver _initSharedObserver]
- GCC_except_table1007
- GCC_except_table1080
- GCC_except_table1132
- GCC_except_table1135
- GCC_except_table1139
- GCC_except_table1144
- GCC_except_table1171
- GCC_except_table1215
- GCC_except_table1235
- GCC_except_table1256
- GCC_except_table1320
- GCC_except_table1321
- GCC_except_table1419
- GCC_except_table1422
- GCC_except_table1434
- GCC_except_table1467
- GCC_except_table1469
- GCC_except_table1545
- GCC_except_table1546
- GCC_except_table1552
- GCC_except_table244
- GCC_except_table250
- GCC_except_table513
- GCC_except_table749
- GCC_except_table758
- GCC_except_table914
- GCC_except_table943
- GCC_except_table947
- GCC_except_table951
- ___224-[SCDAInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:]_block_invoke
- ___42-[SCDAMonitor _setElectionDataForTesting:]_block_invoke
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_65_e8_32r40r48r56r_e27_v32?0"SCDARecord"8Q16^B24lr32l8r40l8r48l8r56l8
CStrings:
+ "%s Election begin generation %llu posted but not yet delivered (last %llu); treating the decision as pending instead of %@"
+ "%s Myriad Delay Monitor Begin (%@, generation %llu)"
+ "%s Myriad Delay Monitor Begin (%@, generation %llu) already pending"
+ "%s Releasing command immediately for Myriad decision: %@ (reason = %@, begin generation %llu)."
+ "%s cdaId: %@, state: %@, withDecision: %@, withPreviousDecision: %@, timeSincePreviousDecision: %llu, withWinningDevice: %@ (score: %d), withThisDevice: %@ (score: %d), withParticipants: %@, withRawScore:%u, withConfidence:%{public}@, withBoost:%@, withTrumpReason:%@"
+ "%s election ledger: answered identity=%llu didWin=%d inferred=1 source=dealloc reason=%{public}@"
+ "%s election ledger: deallocated with %lu waiter(s) on identity %llu; answering didWin=%d. Invalidate first. %{public}@"
+ "%s election ledger: deallocated with identity %llu still provisional; announcing standby end"
+ "%s election ledger: expiring the standby hold for identity %{public}@ on teardown"
+ "%s siriDeviceRouting standby for election generation %llu announced by the coordinator as identity %{public}@; the ledger does not record it"
+ "%s siriDeviceRouting standby for election generation %llu keeps the begin announced as identity %{public}@"
+ "%s siriDeviceRouting: %s arrived while the Myriad decision is pending — keeping it until the hold engages."
+ "%s siriDeviceRouting: discarding %lu signal(s) kept while pending — no hold engaged."
+ "%s siriDeviceRouting: none of the %lu signal(s) kept while pending came from the winner."
+ "%s siriDeviceRouting: not standing by; the winner forced a local decision without completing an election"
+ "%s siriDeviceRouting: released the hold with the %s that arrived before it engaged."
+ "%s standby announcer: a second listener registered; the earlier one stops receiving announcements"
+ "%s standby announcer: begin identity=%llu listening=%d"
+ "%s standby announcer: end identity=%llu reason=%{public}@ listening=%d"
+ "%s standby announcer: registration with no delivery queue, dropping"
+ "%s standby announcer: registration with no listener, dropping"
+ "%s standby announcer: replaying open standby begin identity=%llu to a listener registering mid-hold"
+ "+[SCDADeviceRoutingPriority canLocalStandByForWinnerInCandidates:]"
+ "-[SCDACoordinator(ElectionLedger) _expireProvisionalOutcomeInLedger]"
+ "-[SCDACoordinator(SiriDeviceRoutingStandby) _announceStandbyBeginUnlessLedgerAnnounces]"
+ "-[SCDAElectionLedger _resolveEntry:withOutcome:didWin:observed:source:standbyEndReason:]"
+ "-[SCDAInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withConfidence:withBoost:withCdaId:currentRequestId:withTimestamp:]_block_invoke"
+ "-[SCDAMonitor _enterPendingIfBeginIsInFlight]"
+ "-[SCDAMonitor _replayEarlyReleases:]"
+ "-[SCDAMonitor _replayEarlyReleases:]_block_invoke"
+ "-[SCDAMonitor releaseRoutingTargetHoldAsWon:fromSenderIdsId:]_block_invoke"
+ "-[SCDAStandbyAnnouncer notifyStandbyDidBeginForElection:]"
+ "-[SCDAStandbyAnnouncer notifyStandbyDidEndForElection:reason:]"
+ "-[SCDAStandbyAnnouncer setListener:deliverOn:]"
+ "Continue"
+ "Dismiss"
+ "Dismissed"
+ "Expired"
+ "Promoted"
+ "com.apple.siri.crossdevicearbitration.standbyobserver.delivery"
+ "device_selection_shadow"
+ "standby begin announced with no identity"
+ "standby end announced with no identity"
+ "v16@?0@\"<SCDAStandbyAnnouncerListening>\"8"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
- "%s Myriad Delay Monitor Begin (%@)"
- "%s Releasing command immediately for Myriad decision: %@ (reason = %@)."
- "%s cdaId: %@, state: %@, withDecision: %@, withPreviousDecision: %@, timeSincePreviousDecision: %llu, withWinningDevice: %@ (score: %d), withThisDevice: %@ (score: %d), withParticipants: %@, withRawScore:%u, withBoost:%@, withTrumpReason:%@"
- "%s election ledger: answered identity=%llu didWin=1 inferred=1 source=dealloc reason=%{public}@"
- "%s election ledger: deallocated with %lu waiter(s) on identity %llu; answering win. Invalidate first. %{public}@"
- "-[SCDAElectionLedger _resolveEntry:withOutcome:didWin:observed:source:]"
- "-[SCDAInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:]_block_invoke"
```

## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration`

```diff

-3600.49.15.0.0
-  __TEXT.__text: 0x30760
-  __TEXT.__objc_methlist: 0x310c
-  __TEXT.__const: 0x1b0
-  __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__oslogstring: 0x557e
-  __TEXT.__cstring: 0x5da9
-  __TEXT.__unwind_info: 0x10c0
+3605.22.1.0.0
+  __TEXT.__text: 0x3e750
+  __TEXT.__objc_methlist: 0x3d94
+  __TEXT.__const: 0x2f0
+  __TEXT.__dlopen_cstrs: 0x106
+  __TEXT.__constg_swiftt: 0x54
+  __TEXT.__swift5_typeref: 0x5f
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__cstring: 0x7306
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__swift5_reflstr: 0x18
+  __TEXT.__swift5_fieldmd: 0x28
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0x4
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__gcc_except_tab: 0x450
+  __TEXT.__oslogstring: 0x7819
+  __TEXT.__unwind_info: 0x15b0
+  __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x668
-  __DATA_CONST.__objc_classlist: 0x148
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__const: 0x938
+  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e10
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_selrefs: 0x2440
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x2e8
-  __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0x5338
+  __DATA_CONST.__got: 0x3b0
+  __AUTH_CONST.__const: 0x1358
+  __AUTH_CONST.__cfstring: 0x3940
+  __AUTH_CONST.__objc_const: 0x6bb0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x350
-  __DATA.__objc_ivar: 0x4fc
-  __DATA.__data: 0x5d0
+  __AUTH_CONST.__auth_got: 0x470
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x630
+  __DATA.__data: 0x778
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x10

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/Versions/A/SiriCrossDeviceArbitrationFeedback

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1270
-  Symbols:   3067
-  CStrings:  1048
+  Functions: 1632
+  Symbols:   3898
+  CStrings:  1305
 
Symbols:
+ +[SCDACoordinator(ElectionLedger) mintElectionIdentity]
+ +[SCDADeviceRoutingPriority bestSiriDeviceRoutingTargetInCandidates:winnerDeviceClass:domain:]
+ +[SCDADeviceRoutingPriority canDeviceClass:holdForWinnerClass:]
+ +[SCDADeviceRoutingPriority eligibleStandbyIdsInCandidates:winnerDeviceClass:]
+ +[SCDADeviceRoutingPriority isLocalEligibleRoutingTargetInCandidates:]
+ +[SCDADeviceRoutingPriority isWinnerDecidedLocallyWithoutElectionInCandidates:]
+ +[SCDADeviceRoutingPriority standbyCapablePeersInCandidates:]
+ +[SCDAElectionCandidate candidatesFromReplies:]
+ +[SCDAElectionCandidate candidatesFromReplies:nameResolver:]
+ +[SCDAElectionCandidate candidatesFromResults:]
+ +[SCDAElectionCandidate deviceClassesInCandidates:]
+ +[SCDAElectionCandidate supportsSecureCoding]
+ +[SCDAElectionCandidate winnerIdsIdentifierInCandidates:]
+ +[SCDAElectionDataPublisher clearPublishedElectionData]
+ +[SCDAElectionIdentity identityWithRawValue:]
+ +[SCDAElectionIdentity supportsSecureCoding]
+ +[SCDAElectionLedger sharedLedger]
+ +[SCDAElectionLedgerPublisher initialize]
+ +[SCDAElectionLedgerPublisher startWithEndpointForTesting:]
+ +[SCDAElectionLedgerPublisher start]
+ +[SCDAElectionLedgerReceiver _startWithLedger:listener:requiresPeerEntitlement:]
+ +[SCDAElectionLedgerReceiver initialize]
+ +[SCDAElectionLedgerReceiver startAnonymousReceiverWithLedgerForTesting:]
+ +[SCDAElectionLedgerReceiver startWithLedger:]
+ +[SCDAElectionOutcome supportsSecureCoding]
+ +[SCDAFeatureFlags isDeviceSelectionEnabled]
+ +[SCDAFeatureFlags isElectionLedgerEnabled]
+ +[SCDAFeatureFlags isMonitorDataSiriDeviceRoutingEnabled]
+ +[SCDAFeatureFlags isWatchBoostRebalanceEnabled]
+ +[SCDAFeatureFlags setDeviceSelectionEnabledOverride:]
+ +[SCDAFeatureFlags setElectionLedgerEnabledOverride:]
+ +[SCDAFeatureFlags setMonitorDataSiriDeviceRoutingEnabledOverride:]
+ +[SCDAFeatureFlags setWatchBoostRebalanceEnabledOverride:]
+ +[SCDAMonitor deviceClassesFromElectionData:]
+ +[SCDAStandbyObserver announceStandbyDidBegin]
+ +[SCDAStandbyObserver announceStandbyDidEndAsWon:]
+ +[SCDAStandbyObserver sharedObserver]
+ +[SCDAUtilities setIsATVOverride:]
+ +[SCDAUtilities setIsCommunalOverride:]
+ +[SCDAUtilities shouldAdvertiseEmergencyContinuation]
+ +[SCDAUtilities siriDeviceRoutingMode]
+ -[SCDACoordinator _initiateEmergencyCall]
+ -[SCDACoordinator _maybeEngageRoutingTargetStandby]
+ -[SCDACoordinator init]
+ -[SCDACoordinator(ElectionLedger) _ledgerPublisher]
+ -[SCDACoordinator(ElectionLedger) _publishElectionOutcomeWithDidWin:provisional:]
+ -[SCDACoordinator(ElectionLedger) _publishProvisionalResolutionWithLost:]
+ -[SCDACoordinator(ElectionLedger) _resolveCurrentElectionIdentityAsLostWithReason:]
+ -[SCDACoordinator(ElectionLedger) _tagElectionWithIdentity:origin:]
+ -[SCDACoordinator(ElectionLedger) _useElectionLedgerPublisher:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) currentElectionIdentity]
+ -[SCDACoordinator(ElectionLedger) electionLedger]
+ -[SCDACoordinator(ElectionLedger) setElectionLedger:]
+ -[SCDACoordinator(ElectionLedger) startAdvertisingFromAlertFiringVoiceTriggerWithContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startAdvertisingFromDirectTriggerWithContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startAdvertisingFromInTaskVoiceTriggerWithContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startAdvertisingFromVoiceTriggerAdjusted:withContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startAdvertisingFromVoiceTriggerWithContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startWatchAdvertisingFromDirectTriggerWithContext:electionIdentity:]
+ -[SCDACoordinator(ElectionLedger) startWatchAdvertisingFromVoiceTriggerWithContext:electionIdentity:]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _clearPendingStandby]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _endPendingStandbyAnnouncingWon:]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _engageRoutingTargetStandbyForGeneration:]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) _resolvePendingStandbyAsWon:]
+ -[SCDACoordinator(SiriDeviceRoutingStandby) handleRoutingTargetReleaseWithLost:]
+ -[SCDADevice idsDeviceID]
+ -[SCDADevice setIdsDeviceID:]
+ -[SCDADeviceNameInfo .cxx_destruct]
+ -[SCDADeviceNameInfo description]
+ -[SCDADeviceNameInfo deviceName]
+ -[SCDADeviceNameInfo initWithRoomName:deviceName:]
+ -[SCDADeviceNameInfo roomName]
+ -[SCDAElectionCandidate .cxx_destruct]
+ -[SCDAElectionCandidate copyWithZone:]
+ -[SCDAElectionCandidate deviceClass]
+ -[SCDAElectionCandidate deviceGroup]
+ -[SCDAElectionCandidate deviceName]
+ -[SCDAElectionCandidate encodeWithCoder:]
+ -[SCDAElectionCandidate goodnessScore]
+ -[SCDAElectionCandidate hash]
+ -[SCDAElectionCandidate idsIdentifier]
+ -[SCDAElectionCandidate initWithCoder:]
+ -[SCDAElectionCandidate initWithDictionary:]
+ -[SCDAElectionCandidate initWithIdsIdentifier:goodnessScore:deviceClass:productType:isWinner:isLocalDevice:deviceGroup:userConfidence:pHash:deviceName:]
+ -[SCDAElectionCandidate initWithIdsIdentifier:goodnessScore:deviceClass:productType:isWinner:isLocalDevice:deviceGroup:userConfidence:pHash:deviceName:electionId:]
+ -[SCDAElectionCandidate initWithIdsIdentifier:goodnessScore:deviceClass:productType:isWinner:isLocalDevice:deviceGroup:userConfidence:pHash:deviceName:roomName:]
+ -[SCDAElectionCandidate isEqual:]
+ -[SCDAElectionCandidate isLocalDevice]
+ -[SCDAElectionCandidate isWinner]
+ -[SCDAElectionCandidate pHash]
+ -[SCDAElectionCandidate productType]
+ -[SCDAElectionCandidate roomName]
+ -[SCDAElectionCandidate toDictionary]
+ -[SCDAElectionCandidate userConfidence]
+ -[SCDAElectionDataPublisher publishElectionDataFromReplies:generation:]
+ -[SCDAElectionIdentity copyWithZone:]
+ -[SCDAElectionIdentity description]
+ -[SCDAElectionIdentity encodeWithCoder:]
+ -[SCDAElectionIdentity hash]
+ -[SCDAElectionIdentity initWithCoder:]
+ -[SCDAElectionIdentity initWithRawValue:]
+ -[SCDAElectionIdentity init]
+ -[SCDAElectionIdentity isEqual:]
+ -[SCDAElectionIdentity rawValue]
+ -[SCDAElectionLedger .cxx_destruct]
+ -[SCDAElectionLedger _armTimeoutTimer]
+ -[SCDAElectionLedger _deliverDecision:on:identity:didWin:outcome:source:reason:detail:registeredAt:]
+ -[SCDAElectionLedger _entryForIdentity:]
+ -[SCDAElectionLedger _evaluateTimeouts]
+ -[SCDAElectionLedger _evictEntry:]
+ -[SCDAElectionLedger _parkWaiter:forIdentity:existingEntry:]
+ -[SCDAElectionLedger _parkWaiterForIdentity:entry:reason:detail:deliverOn:completion:]
+ -[SCDAElectionLedger _pruneActivationKinds]
+ -[SCDAElectionLedger _pruneHistory]
+ -[SCDAElectionLedger _registerActivationKind:forIdentity:]
+ -[SCDAElectionLedger _resolveEntry:withOutcome:didWin:observed:]
+ -[SCDAElectionLedger _resolveEntry:withOutcome:didWin:observed:source:]
+ -[SCDAElectionLedger _resolveProvisionalEntry:withResult:]
+ -[SCDAElectionLedger _stateSnapshot]
+ -[SCDAElectionLedger dealloc]
+ -[SCDAElectionLedger debugDescription]
+ -[SCDAElectionLedger decisionForElection:reason:detail:deliverOn:completion:]
+ -[SCDAElectionLedger entryCount]
+ -[SCDAElectionLedger evaluateTimeouts]
+ -[SCDAElectionLedger initWithClock:decisionTimeout:promotionWindow:]
+ -[SCDAElectionLedger invalidate]
+ -[SCDAElectionLedger outstandingWaiterCount]
+ -[SCDAElectionLedger recordOutcome:]
+ -[SCDAElectionLedger recordProvisionalOutcome:]
+ -[SCDAElectionLedger registeredActivationKindCount]
+ -[SCDAElectionLedger resolveProvisionalOutcomeForElectionId:result:]
+ -[SCDAElectionLedger setActivationKind:forElection:]
+ -[SCDAElectionLedgerEntry .cxx_destruct]
+ -[SCDAElectionLedgerEntry deadlineContinuousNanos]
+ -[SCDAElectionLedgerEntry identity]
+ -[SCDAElectionLedgerEntry initWithIdentity:]
+ -[SCDAElectionLedgerEntry outcome]
+ -[SCDAElectionLedgerEntry resolvedAtContinuousNanos]
+ -[SCDAElectionLedgerEntry setDeadlineContinuousNanos:]
+ -[SCDAElectionLedgerEntry setIdentity:]
+ -[SCDAElectionLedgerEntry setOutcome:]
+ -[SCDAElectionLedgerEntry setResolvedAtContinuousNanos:]
+ -[SCDAElectionLedgerEntry setState:]
+ -[SCDAElectionLedgerEntry setWaiters:]
+ -[SCDAElectionLedgerEntry state]
+ -[SCDAElectionLedgerEntry waiters]
+ -[SCDAElectionLedgerPublisher .cxx_destruct]
+ -[SCDAElectionLedgerPublisher _configureConnection:]
+ -[SCDAElectionLedgerPublisher _initWithConnection:requiresPeerVerification:]
+ -[SCDAElectionLedgerPublisher _receiver]
+ -[SCDAElectionLedgerPublisher _verifyPeer:]
+ -[SCDAElectionLedgerPublisher flushPendingPublishes]
+ -[SCDAElectionLedgerPublisher invalidate]
+ -[SCDAElectionLedgerPublisher publishOutcome:provisional:]
+ -[SCDAElectionLedgerPublisher publishProvisionalResolutionForElectionId:result:]
+ -[SCDAElectionLedgerPublisher reconnectToEndpointForTesting:]
+ -[SCDAElectionLedgerPublisher replayRetainedOutcomesWithReply:]
+ -[SCDAElectionLedgerReceiver .cxx_destruct]
+ -[SCDAElectionLedgerReceiver _initWithLedger:listener:requiresPeerEntitlement:]
+ -[SCDAElectionLedgerReceiver _isTornDownSynchronized]
+ -[SCDAElectionLedgerReceiver _requestReplayOverConnection:]
+ -[SCDAElectionLedgerReceiver connectedPublisherCount]
+ -[SCDAElectionLedgerReceiver deliverOutcome:provisional:]
+ -[SCDAElectionLedgerReceiver endpoint]
+ -[SCDAElectionLedgerReceiver invalidate]
+ -[SCDAElectionLedgerReceiver listener:shouldAcceptNewConnection:]
+ -[SCDAElectionLedgerReceiver resolveProvisionalOutcomeForElectionId:holdResult:]
+ -[SCDAElectionLedgerReceiver waitForDeliveredOutcomes]
+ -[SCDAElectionLedgerWaiter .cxx_destruct]
+ -[SCDAElectionLedgerWaiter decisionBlock]
+ -[SCDAElectionLedgerWaiter deliveryQueue]
+ -[SCDAElectionLedgerWaiter detail]
+ -[SCDAElectionLedgerWaiter reason]
+ -[SCDAElectionLedgerWaiter registeredAtContinuousNanos]
+ -[SCDAElectionLedgerWaiter setDecisionBlock:]
+ -[SCDAElectionLedgerWaiter setDeliveryQueue:]
+ -[SCDAElectionLedgerWaiter setDetail:]
+ -[SCDAElectionLedgerWaiter setReason:]
+ -[SCDAElectionLedgerWaiter setRegisteredAtContinuousNanos:]
+ -[SCDAElectionOutcome .cxx_destruct]
+ -[SCDAElectionOutcome candidates]
+ -[SCDAElectionOutcome copyWithZone:]
+ -[SCDAElectionOutcome description]
+ -[SCDAElectionOutcome didWin]
+ -[SCDAElectionOutcome electionId]
+ -[SCDAElectionOutcome encodeWithCoder:]
+ -[SCDAElectionOutcome hash]
+ -[SCDAElectionOutcome identity]
+ -[SCDAElectionOutcome initWithCoder:]
+ -[SCDAElectionOutcome initWithIdentity:electionId:didWin:candidates:resolvedAtContinuousNanos:]
+ -[SCDAElectionOutcome isEqual:]
+ -[SCDAElectionOutcome participatingDeviceClasses]
+ -[SCDAElectionOutcome resolvedAtContinuousNanos]
+ -[SCDAGoodnessScoreEvaluator signedAdjustedBoostForGoodnessScoreContext:]
+ -[SCDAHoldController .cxx_destruct]
+ -[SCDAHoldController _releaseOnQueue:]
+ -[SCDAHoldController _releaseOnQueue:suppressNotification:]
+ -[SCDAHoldController _startWatchdogOnQueue]
+ -[SCDAHoldController currentGeneration]
+ -[SCDAHoldController dealloc]
+ -[SCDAHoldController evaluateAndHoldIfNeededWithEligibility:generation:expectedSenderIdsId:onRelease:]
+ -[SCDAHoldController expectedSenderIdsId]
+ -[SCDAHoldController holdWatchdogTimeout]
+ -[SCDAHoldController init]
+ -[SCDAHoldController isHolding]
+ -[SCDAHoldController onRelease]
+ -[SCDAHoldController queue]
+ -[SCDAHoldController releaseHoldLocallyWithResult:]
+ -[SCDAHoldController releaseHoldWithResult:fromSenderIdsId:]
+ -[SCDAHoldController setCurrentGeneration:]
+ -[SCDAHoldController setExpectedSenderIdsId:]
+ -[SCDAHoldController setHoldWatchdogTimeout:]
+ -[SCDAHoldController setOnRelease:]
+ -[SCDAHoldController setQueue:]
+ -[SCDAHoldController setWatchdog:]
+ -[SCDAHoldController watchdog]
+ -[SCDAMonitor _engageRoutingTargetHoldIfEligible]
+ -[SCDAMonitor _runSyncOnMonitorQueue:]
+ -[SCDAMonitor _setElectionDataForTesting:]
+ -[SCDAMonitor deviceClassesInMostRecentElection]
+ -[SCDAMonitor deviceNameResolver]
+ -[SCDAMonitor initForTesting]
+ -[SCDAMonitor releaseRoutingTargetHoldAsWon:fromSenderIdsId:]
+ -[SCDAMonitor setDeviceNameResolver:]
+ -[SCDARecord idsDeviceID]
+ -[SCDARecord setIdsDeviceID:]
+ -[SCDARecord(InternalDebug) debugDeviceDescription]
+ -[SCDARoutingTargetReleaseObserver .cxx_destruct]
+ -[SCDARoutingTargetReleaseObserver callbackQueue]
+ -[SCDARoutingTargetReleaseObserver dealloc]
+ -[SCDARoutingTargetReleaseObserver delegate]
+ -[SCDARoutingTargetReleaseObserver initWithDelegate:]
+ -[SCDARoutingTargetReleaseObserver observing]
+ -[SCDARoutingTargetReleaseObserver setCallbackQueue:]
+ -[SCDARoutingTargetReleaseObserver setObserving:]
+ -[SCDARoutingTargetReleaseObserver startObserving]
+ -[SCDARoutingTargetReleaseObserver stopObserving]
+ -[SCDAStandbyHoldCoordinator .cxx_destruct]
+ -[SCDAStandbyHoldCoordinator cancelAnyHold]
+ -[SCDAStandbyHoldCoordinator engageHoldIfEligibleInCandidates:generation:onRelease:]
+ -[SCDAStandbyHoldCoordinator init]
+ -[SCDAStandbyHoldCoordinator isHolding]
+ -[SCDAStandbyHoldCoordinator releaseHoldAsWon:fromSenderIdsId:]
+ -[SCDAStandbyObserver .cxx_destruct]
+ -[SCDAStandbyObserver _initSharedObserver]
+ -[SCDAStandbyObserver _listener]
+ -[SCDAStandbyObserver removeListener:]
+ -[SCDAStandbyObserver setListener:]
+ GCC_except_table1040
+ GCC_except_table1113
+ GCC_except_table1167
+ GCC_except_table1171
+ GCC_except_table1180
+ GCC_except_table1207
+ GCC_except_table1251
+ GCC_except_table1271
+ GCC_except_table1292
+ GCC_except_table1358
+ GCC_except_table1359
+ GCC_except_table1457
+ GCC_except_table1460
+ GCC_except_table1473
+ GCC_except_table1506
+ GCC_except_table1508
+ GCC_except_table254
+ GCC_except_table264
+ GCC_except_table537
+ GCC_except_table69
+ GCC_except_table773
+ GCC_except_table786
+ GCC_except_table945
+ GCC_except_table976
+ GCC_except_table980
+ GCC_except_table984
+ IDSLibraryCore.frameworkLibrary
+ OBJC_IVAR_$_SCDACoordinator._currentElectionIdentity
+ OBJC_IVAR_$_SCDACoordinator._electionDataPublisher
+ OBJC_IVAR_$_SCDACoordinator._electionLedgerOverride
+ OBJC_IVAR_$_SCDACoordinator._electionLedgerPublisher
+ OBJC_IVAR_$_SCDACoordinator._isElectionIdentityHeldForStandby
+ OBJC_IVAR_$_SCDACoordinator._pendingLedgerElectionId
+ OBJC_IVAR_$_SCDACoordinator._pendingStandbyGeneration
+ OBJC_IVAR_$_SCDACoordinator._pendingStandbyTimer
+ OBJC_IVAR_$_SCDACoordinator._routingTargetReleaseObserver
+ OBJC_IVAR_$_SCDADevice._idsDeviceID
+ OBJC_IVAR_$_SCDADeviceNameInfo._deviceName
+ OBJC_IVAR_$_SCDADeviceNameInfo._roomName
+ OBJC_IVAR_$_SCDAElectionCandidate._deviceClass
+ OBJC_IVAR_$_SCDAElectionCandidate._deviceGroup
+ OBJC_IVAR_$_SCDAElectionCandidate._deviceName
+ OBJC_IVAR_$_SCDAElectionCandidate._goodnessScore
+ OBJC_IVAR_$_SCDAElectionCandidate._idsIdentifier
+ OBJC_IVAR_$_SCDAElectionCandidate._isLocalDevice
+ OBJC_IVAR_$_SCDAElectionCandidate._isWinner
+ OBJC_IVAR_$_SCDAElectionCandidate._pHash
+ OBJC_IVAR_$_SCDAElectionCandidate._productType
+ OBJC_IVAR_$_SCDAElectionCandidate._roomName
+ OBJC_IVAR_$_SCDAElectionCandidate._userConfidence
+ OBJC_IVAR_$_SCDAElectionIdentity._rawValue
+ OBJC_IVAR_$_SCDAElectionLedger._activationKindOrder
+ OBJC_IVAR_$_SCDAElectionLedger._activationKinds
+ OBJC_IVAR_$_SCDAElectionLedger._clock
+ OBJC_IVAR_$_SCDAElectionLedger._decisionTimeout
+ OBJC_IVAR_$_SCDAElectionLedger._entries
+ OBJC_IVAR_$_SCDAElectionLedger._evictedIdentities
+ OBJC_IVAR_$_SCDAElectionLedger._isInvalidated
+ OBJC_IVAR_$_SCDAElectionLedger._promotionWindow
+ OBJC_IVAR_$_SCDAElectionLedger._provisionalIdentity
+ OBJC_IVAR_$_SCDAElectionLedger._stateQueue
+ OBJC_IVAR_$_SCDAElectionLedger._timer
+ OBJC_IVAR_$_SCDAElectionLedgerEntry._deadlineContinuousNanos
+ OBJC_IVAR_$_SCDAElectionLedgerEntry._identity
+ OBJC_IVAR_$_SCDAElectionLedgerEntry._outcome
+ OBJC_IVAR_$_SCDAElectionLedgerEntry._resolvedAtContinuousNanos
+ OBJC_IVAR_$_SCDAElectionLedgerEntry._state
+ OBJC_IVAR_$_SCDAElectionLedgerEntry._waiters
+ OBJC_IVAR_$_SCDAElectionLedgerPublisher._connection
+ OBJC_IVAR_$_SCDAElectionLedgerPublisher._replayHistory
+ OBJC_IVAR_$_SCDAElectionLedgerPublisher._requiresPeerVerification
+ OBJC_IVAR_$_SCDAElectionLedgerPublisher._stateQueue
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._connections
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._deliveryQueue
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._isTornDown
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._ledger
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._listener
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._requiresPeerEntitlement
+ OBJC_IVAR_$_SCDAElectionLedgerReceiver._stateQueue
+ OBJC_IVAR_$_SCDAElectionLedgerWaiter._decisionBlock
+ OBJC_IVAR_$_SCDAElectionLedgerWaiter._deliveryQueue
+ OBJC_IVAR_$_SCDAElectionLedgerWaiter._detail
+ OBJC_IVAR_$_SCDAElectionLedgerWaiter._reason
+ OBJC_IVAR_$_SCDAElectionLedgerWaiter._registeredAtContinuousNanos
+ OBJC_IVAR_$_SCDAElectionOutcome._candidates
+ OBJC_IVAR_$_SCDAElectionOutcome._didWin
+ OBJC_IVAR_$_SCDAElectionOutcome._electionId
+ OBJC_IVAR_$_SCDAElectionOutcome._identity
+ OBJC_IVAR_$_SCDAElectionOutcome._resolvedAtContinuousNanos
+ OBJC_IVAR_$_SCDAHoldController._currentGeneration
+ OBJC_IVAR_$_SCDAHoldController._expectedSenderIdsId
+ OBJC_IVAR_$_SCDAHoldController._holdWatchdogTimeout
+ OBJC_IVAR_$_SCDAHoldController._onRelease
+ OBJC_IVAR_$_SCDAHoldController._queue
+ OBJC_IVAR_$_SCDAHoldController._watchdog
+ OBJC_IVAR_$_SCDAMonitor._deviceNameResolver
+ OBJC_IVAR_$_SCDAMonitor._holdCoordinator
+ OBJC_IVAR_$_SCDAMonitor._mostRecentElectionData
+ OBJC_IVAR_$_SCDARecord._idsDeviceID
+ OBJC_IVAR_$_SCDARoutingTargetReleaseObserver._callbackQueue
+ OBJC_IVAR_$_SCDARoutingTargetReleaseObserver._delegate
+ OBJC_IVAR_$_SCDARoutingTargetReleaseObserver._observing
+ OBJC_IVAR_$_SCDAStandbyHoldCoordinator._holdController
+ OBJC_IVAR_$_SCDAStandbyObserver._listener
+ SCDAElectionLedgerContinuousNanos.onceToken
+ SCDAElectionLedgerContinuousNanos.timebase
+ SCDALiveReceivers.liveReceivers
+ SCDALiveReceivers.onceToken
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFNotificationCenterRemoveEveryObserver
+ _CFRelease
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_SCDADeviceNameInfo
+ _OBJC_CLASS_$_SCDADeviceRoutingPriority
+ _OBJC_CLASS_$_SCDAElectionCandidate
+ _OBJC_CLASS_$_SCDAElectionDataPublisher
+ _OBJC_CLASS_$_SCDAElectionIdentity
+ _OBJC_CLASS_$_SCDAElectionLedger
+ _OBJC_CLASS_$_SCDAElectionLedgerEntry
+ _OBJC_CLASS_$_SCDAElectionLedgerPublisher
+ _OBJC_CLASS_$_SCDAElectionLedgerReceiver
+ _OBJC_CLASS_$_SCDAElectionLedgerWaiter
+ _OBJC_CLASS_$_SCDAElectionOutcome
+ _OBJC_CLASS_$_SCDAFeatureFlags
+ _OBJC_CLASS_$_SCDAHoldController
+ _OBJC_CLASS_$_SCDARoutingTargetReleaseObserver
+ _OBJC_CLASS_$_SCDAStandbyHoldCoordinator
+ _OBJC_CLASS_$_SCDAStandbyObserver
+ _OBJC_METACLASS_$_SCDADeviceNameInfo
+ _OBJC_METACLASS_$_SCDADeviceRoutingPriority
+ _OBJC_METACLASS_$_SCDAElectionCandidate
+ _OBJC_METACLASS_$_SCDAElectionDataPublisher
+ _OBJC_METACLASS_$_SCDAElectionIdentity
+ _OBJC_METACLASS_$_SCDAElectionLedger
+ _OBJC_METACLASS_$_SCDAElectionLedgerEntry
+ _OBJC_METACLASS_$_SCDAElectionLedgerPublisher
+ _OBJC_METACLASS_$_SCDAElectionLedgerReceiver
+ _OBJC_METACLASS_$_SCDAElectionLedgerWaiter
+ _OBJC_METACLASS_$_SCDAElectionOutcome
+ _OBJC_METACLASS_$_SCDAFeatureFlags
+ _OBJC_METACLASS_$_SCDAHoldController
+ _OBJC_METACLASS_$_SCDARoutingTargetReleaseObserver
+ _OBJC_METACLASS_$_SCDAStandbyHoldCoordinator
+ _OBJC_METACLASS_$_SCDAStandbyObserver
+ _OUTLINED_FUNCTION_0
+ _SCDACanHandleEmergencyFlow
+ _SCDACanHostCarPlaySession
+ _SCDADecodeBoundedInt
+ _SCDADeviceClassDisplayName
+ _SCDADeviceRoutingDomainIdentifier
+ _SCDAElectionActivationKindArbitrates
+ _SCDAElectionActivationKindConflict
+ _SCDAElectionActivationKindDescription
+ _SCDAElectionActivationKindMissing
+ _SCDAElectionActivationKindSetConflictHandlerForTesting
+ _SCDAElectionDataKeyGeneration
+ _SCDAElectionDataKeyResults
+ _SCDAElectionEntryKeyDeviceClass
+ _SCDAElectionEntryKeyDeviceGroup
+ _SCDAElectionEntryKeyDeviceName
+ _SCDAElectionEntryKeyGoodness
+ _SCDAElectionEntryKeyIdsIdentifier
+ _SCDAElectionEntryKeyIsLocalDevice
+ _SCDAElectionEntryKeyIsWinner
+ _SCDAElectionEntryKeyPHash
+ _SCDAElectionEntryKeyProductType
+ _SCDAElectionEntryKeyRoomName
+ _SCDAElectionEntryKeyUserConfidence
+ _SCDAElectionIdentityMissing
+ _SCDAElectionIdentityReplaced
+ _SCDAElectionIdentitySetMissingHandlerForTesting
+ _SCDAElectionIdentitySetReplacedHandlerForTesting
+ _SCDAElectionLedgerAllowEntitlement
+ _SCDAElectionLedgerContinuousNanos
+ _SCDAElectionLedgerDefaultDecisionTimeout
+ _SCDAElectionLedgerDefaultPromotionWindow
+ _SCDAElectionLedgerHistoryMaxAge
+ _SCDAElectionLedgerHistoryMaxCount
+ _SCDAElectionLedgerMachServiceName
+ _SCDAElectionLedgerPeerHasEntitlement
+ _SCDAElectionLedgerPublisherReplayHistoryMaxCount
+ _SCDAElectionLedgerTransportAllowedClasses
+ _SCDAElectionOriginDescription
+ _SCDAElectionWaitReasonDescription
+ _SCDAFeatureFlagSetOverride
+ _SCDAFeatureFlagValue
+ _SCDAHoldResultDescription
+ _SCDALiveReceivers
+ _SCDALivenessOutcome
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ __49-[SCDAMonitor _engageRoutingTargetHoldIfEligible]_block_invoke
+ __52-[SCDAElectionLedgerPublisher _configureConnection:]_block_invoke
+ __59-[SCDAElectionLedgerReceiver _requestReplayOverConnection:]_block_invoke
+ __65-[SCDAElectionLedgerReceiver listener:shouldAcceptNewConnection:]_block_invoke
+ __Block_copy
+ __Block_release
+ __OBJC_$_CLASS_METHODS_SCDACoordinator(ElectionLedger|SiriDeviceRoutingStandby)
+ __OBJC_$_CLASS_METHODS_SCDADeviceRoutingPriority
+ __OBJC_$_CLASS_METHODS_SCDAElectionCandidate
+ __OBJC_$_CLASS_METHODS_SCDAElectionDataPublisher
+ __OBJC_$_CLASS_METHODS_SCDAElectionIdentity
+ __OBJC_$_CLASS_METHODS_SCDAElectionLedger
+ __OBJC_$_CLASS_METHODS_SCDAElectionLedgerPublisher
+ __OBJC_$_CLASS_METHODS_SCDAElectionLedgerReceiver
+ __OBJC_$_CLASS_METHODS_SCDAElectionOutcome
+ __OBJC_$_CLASS_METHODS_SCDAFeatureFlags
+ __OBJC_$_CLASS_METHODS_SCDAStandbyObserver
+ __OBJC_$_CLASS_PROP_LIST_SCDAElectionCandidate
+ __OBJC_$_CLASS_PROP_LIST_SCDAElectionIdentity
+ __OBJC_$_CLASS_PROP_LIST_SCDAElectionOutcome
+ __OBJC_$_INSTANCE_METHODS_SCDACoordinator(ElectionLedger|SiriDeviceRoutingStandby)
+ __OBJC_$_INSTANCE_METHODS_SCDADeviceNameInfo
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionCandidate
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionDataPublisher
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionIdentity
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionLedger
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionLedgerEntry
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionLedgerPublisher
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionLedgerReceiver
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionLedgerWaiter
+ __OBJC_$_INSTANCE_METHODS_SCDAElectionOutcome
+ __OBJC_$_INSTANCE_METHODS_SCDAHoldController
+ __OBJC_$_INSTANCE_METHODS_SCDARoutingTargetReleaseObserver
+ __OBJC_$_INSTANCE_METHODS_SCDAStandbyHoldCoordinator
+ __OBJC_$_INSTANCE_METHODS_SCDAStandbyObserver
+ __OBJC_$_INSTANCE_VARIABLES_SCDADeviceNameInfo
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionCandidate
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionIdentity
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionLedger
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionLedgerEntry
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionLedgerPublisher
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionLedgerReceiver
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionLedgerWaiter
+ __OBJC_$_INSTANCE_VARIABLES_SCDAElectionOutcome
+ __OBJC_$_INSTANCE_VARIABLES_SCDAHoldController
+ __OBJC_$_INSTANCE_VARIABLES_SCDARoutingTargetReleaseObserver
+ __OBJC_$_INSTANCE_VARIABLES_SCDAStandbyHoldCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SCDAStandbyObserver
+ __OBJC_$_PROP_LIST_SCDADeviceNameInfo
+ __OBJC_$_PROP_LIST_SCDAElectionCandidate
+ __OBJC_$_PROP_LIST_SCDAElectionIdentity
+ __OBJC_$_PROP_LIST_SCDAElectionLedgerEntry
+ __OBJC_$_PROP_LIST_SCDAElectionLedgerPublisher
+ __OBJC_$_PROP_LIST_SCDAElectionLedgerReceiver
+ __OBJC_$_PROP_LIST_SCDAElectionLedgerWaiter
+ __OBJC_$_PROP_LIST_SCDAElectionOutcome
+ __OBJC_$_PROP_LIST_SCDAHoldController
+ __OBJC_$_PROP_LIST_SCDARoutingTargetReleaseObserver
+ __OBJC_$_PROP_LIST_SCDAStandbyHoldCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCDAElectionLedgerPublisherProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCDAElectionLedgerReceiverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCDARoutingTargetReleaseHandling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDAElectionLedgerPublisherProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDAElectionLedgerReceiverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDARoutingTargetReleaseHandling
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_SCDAElectionLedgerPublisherProtocol
+ __OBJC_$_PROTOCOL_REFS_SCDAElectionLedgerReceiverProtocol
+ __OBJC_$_PROTOCOL_REFS_SCDARoutingTargetReleaseHandling
+ __OBJC_CLASS_PROTOCOLS_$_SCDACoordinator(ElectionLedger|SiriDeviceRoutingStandby)
+ __OBJC_CLASS_PROTOCOLS_$_SCDAElectionCandidate
+ __OBJC_CLASS_PROTOCOLS_$_SCDAElectionIdentity
+ __OBJC_CLASS_PROTOCOLS_$_SCDAElectionLedgerPublisher
+ __OBJC_CLASS_PROTOCOLS_$_SCDAElectionLedgerReceiver
+ __OBJC_CLASS_PROTOCOLS_$_SCDAElectionOutcome
+ __OBJC_CLASS_RO_$_SCDADeviceNameInfo
+ __OBJC_CLASS_RO_$_SCDADeviceRoutingPriority
+ __OBJC_CLASS_RO_$_SCDAElectionCandidate
+ __OBJC_CLASS_RO_$_SCDAElectionDataPublisher
+ __OBJC_CLASS_RO_$_SCDAElectionIdentity
+ __OBJC_CLASS_RO_$_SCDAElectionLedger
+ __OBJC_CLASS_RO_$_SCDAElectionLedgerEntry
+ __OBJC_CLASS_RO_$_SCDAElectionLedgerPublisher
+ __OBJC_CLASS_RO_$_SCDAElectionLedgerReceiver
+ __OBJC_CLASS_RO_$_SCDAElectionLedgerWaiter
+ __OBJC_CLASS_RO_$_SCDAElectionOutcome
+ __OBJC_CLASS_RO_$_SCDAFeatureFlags
+ __OBJC_CLASS_RO_$_SCDAHoldController
+ __OBJC_CLASS_RO_$_SCDARoutingTargetReleaseObserver
+ __OBJC_CLASS_RO_$_SCDAStandbyHoldCoordinator
+ __OBJC_CLASS_RO_$_SCDAStandbyObserver
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SCDAElectionLedgerPublisherProtocol
+ __OBJC_LABEL_PROTOCOL_$_SCDAElectionLedgerReceiverProtocol
+ __OBJC_LABEL_PROTOCOL_$_SCDARoutingTargetReleaseHandling
+ __OBJC_METACLASS_RO_$_SCDADeviceNameInfo
+ __OBJC_METACLASS_RO_$_SCDADeviceRoutingPriority
+ __OBJC_METACLASS_RO_$_SCDAElectionCandidate
+ __OBJC_METACLASS_RO_$_SCDAElectionDataPublisher
+ __OBJC_METACLASS_RO_$_SCDAElectionIdentity
+ __OBJC_METACLASS_RO_$_SCDAElectionLedger
+ __OBJC_METACLASS_RO_$_SCDAElectionLedgerEntry
+ __OBJC_METACLASS_RO_$_SCDAElectionLedgerPublisher
+ __OBJC_METACLASS_RO_$_SCDAElectionLedgerReceiver
+ __OBJC_METACLASS_RO_$_SCDAElectionLedgerWaiter
+ __OBJC_METACLASS_RO_$_SCDAElectionOutcome
+ __OBJC_METACLASS_RO_$_SCDAFeatureFlags
+ __OBJC_METACLASS_RO_$_SCDAHoldController
+ __OBJC_METACLASS_RO_$_SCDARoutingTargetReleaseObserver
+ __OBJC_METACLASS_RO_$_SCDAStandbyHoldCoordinator
+ __OBJC_METACLASS_RO_$_SCDAStandbyObserver
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_$_SCDAElectionLedgerPublisherProtocol
+ __OBJC_PROTOCOL_$_SCDAElectionLedgerReceiverProtocol
+ __OBJC_PROTOCOL_$_SCDARoutingTargetReleaseHandling
+ __OBJC_PROTOCOL_REFERENCE_$_SCDAElectionLedgerPublisherProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SCDAElectionLedgerReceiverProtocol
+ __SCDABestIdsIdMatching
+ __SCDABestRoutingTargetIdsId
+ __SCDAReleaseLostCallback
+ __SCDAReleaseWonCallback
+ ___100-[SCDAElectionLedger _deliverDecision:on:identity:didWin:outcome:source:reason:detail:registeredAt:]_block_invoke
+ ___102-[SCDAHoldController evaluateAndHoldIfNeededWithEligibility:generation:expectedSenderIdsId:onRelease:]_block_invoke
+ ___29-[SCDAElectionLedger dealloc]_block_invoke
+ ___31-[SCDAHoldController isHolding]_block_invoke
+ ___32-[SCDAElectionLedger entryCount]_block_invoke
+ ___32-[SCDAElectionLedger invalidate]_block_invoke
+ ___34+[SCDAElectionLedger sharedLedger]_block_invoke
+ ___35-[SCDAElectionLedger _pruneHistory]_block_invoke
+ ___36-[SCDAElectionLedger recordOutcome:]_block_invoke
+ ___37+[SCDAStandbyObserver sharedObserver]_block_invoke
+ ___38-[SCDAElectionLedger debugDescription]_block_invoke
+ ___38-[SCDAElectionLedger evaluateTimeouts]_block_invoke
+ ___40-[SCDAElectionLedgerPublisher _receiver]_block_invoke
+ ___40-[SCDAElectionLedgerReceiver invalidate]_block_invoke
+ ___41-[SCDAElectionLedgerPublisher invalidate]_block_invoke
+ ___42-[SCDAMonitor _setElectionDataForTesting:]_block_invoke
+ ___43-[SCDAHoldController _startWatchdogOnQueue]_block_invoke
+ ___44-[SCDAElectionLedger outstandingWaiterCount]_block_invoke
+ ___47-[SCDAElectionLedger recordProvisionalOutcome:]_block_invoke
+ ___48-[SCDAMonitor deviceClassesInMostRecentElection]_block_invoke
+ ___49-[SCDAMonitor _engageRoutingTargetHoldIfEligible]_block_invoke
+ ___51-[SCDAElectionLedger registeredActivationKindCount]_block_invoke
+ ___51-[SCDAHoldController releaseHoldLocallyWithResult:]_block_invoke
+ ___52-[SCDAElectionLedger setActivationKind:forElection:]_block_invoke
+ ___52-[SCDAElectionLedgerPublisher _configureConnection:]_block_invoke
+ ___52-[SCDAElectionLedgerPublisher flushPendingPublishes]_block_invoke
+ ___53-[SCDAElectionLedgerReceiver _isTornDownSynchronized]_block_invoke
+ ___53-[SCDAElectionLedgerReceiver connectedPublisherCount]_block_invoke
+ ___54-[SCDAElectionLedgerReceiver waitForDeliveredOutcomes]_block_invoke
+ ___57-[SCDAElectionLedgerReceiver deliverOutcome:provisional:]_block_invoke
+ ___58-[SCDAElectionLedgerPublisher publishOutcome:provisional:]_block_invoke
+ ___59-[SCDAElectionLedgerReceiver _requestReplayOverConnection:]_block_invoke
+ ___59-[SCDAElectionLedgerReceiver _requestReplayOverConnection:]_block_invoke_2
+ ___60-[SCDAHoldController releaseHoldWithResult:fromSenderIdsId:]_block_invoke
+ ___61-[SCDAElectionLedgerPublisher reconnectToEndpointForTesting:]_block_invoke
+ ___63-[SCDAElectionLedgerPublisher replayRetainedOutcomesWithReply:]_block_invoke
+ ___65-[SCDAElectionLedgerReceiver listener:shouldAcceptNewConnection:]_block_invoke
+ ___65-[SCDAElectionLedgerReceiver listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___68-[SCDAElectionLedger initWithClock:decisionTimeout:promotionWindow:]_block_invoke
+ ___68-[SCDAElectionLedger initWithClock:decisionTimeout:promotionWindow:]_block_invoke_2
+ ___68-[SCDAElectionLedger resolveProvisionalOutcomeForElectionId:result:]_block_invoke
+ ___77-[SCDAElectionLedger decisionForElection:reason:detail:deliverOn:completion:]_block_invoke
+ ___80-[SCDACoordinator(SiriDeviceRoutingStandby) handleRoutingTargetReleaseWithLost:]_block_invoke
+ ___80-[SCDAElectionLedgerPublisher publishProvisionalResolutionForElectionId:result:]_block_invoke
+ ___80-[SCDAElectionLedgerReceiver resolveProvisionalOutcomeForElectionId:holdResult:]_block_invoke
+ ___84-[SCDAStandbyHoldCoordinator engageHoldIfEligibleInCandidates:generation:onRelease:]_block_invoke
+ ___86-[SCDACoordinator(SiriDeviceRoutingStandby) _engageRoutingTargetStandbyForGeneration:]_block_invoke
+ ___IDSLibraryCore_block_invoke
+ ___SCDAElectionLedgerContinuousNanos_block_invoke
+ ___SCDALiveReceivers_block_invoke
+ ____SCDABestRoutingTargetIdsId_block_invoke
+ ____SCDAEmergencyCapableIdsId_block_invoke
+ ____SCDAReleaseLostCallback_block_invoke
+ ____SCDAReleaseWonCallback_block_invoke
+ ___block_descriptor_32_e31_B16?0"SCDAElectionCandidate"8l
+ ___block_descriptor_32_e5_Q8?0l
+ ___block_descriptor_32_e61_q24?0"SCDAElectionLedgerEntry"8"SCDAElectionLedgerEntry"16l
+ ___block_descriptor_33_e31_B16?0"SCDAElectionCandidate"8l
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8l
+ ___block_descriptor_41_e8_32w_e5_v8?0l
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___block_descriptor_48_e8_32w_e8_v16?0q8l
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_49_e8_32s40s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_56_e8_32s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48bs56r_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b56r
+ ___copy_helper_block_e8_32s40s48s56b
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32s40s48s56r
+ ___destroy_helper_block_e8_32w40w
+ ___getIDSCopyLocalDeviceUniqueIDSymbolLoc_block_invoke
+ ___getWPHeySiriNeedsIdentitySymbolLoc_block_invoke
+ ___getWPHeySiriRPIdentitySymbolLoc_block_invoke
+ ___kCFBooleanTrue
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy16_8
+ __activationKindConflictHandler
+ __deviceSelectionEnabledOverride
+ __electionLedgerEnabledOverride
+ __isATVOverride
+ __isCommunalOverride
+ __liveReceiversLock
+ __missingIdentityHandler
+ __monitorDataSiriDeviceRoutingEnabledOverride
+ __os_log_fault_impl
+ __overrideLock
+ __replacedIdentityHandler
+ __swiftImmortalRefCount
+ _associated conformance So23SCDADeviceRoutingDomainVs12CaseIterable26SiriCrossDeviceArbitration8AllCasessACP_Sl
+ _audit_stringIDS
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _getWPHeySiriNeedsIdentity
+ _kSCDAHoldQueueKey
+ _kSCDAMonitorQueueKey
+ _mach_continuous_time
+ _objc_msgSend$_armTimeoutTimer
+ _objc_msgSend$_clearPendingStandby
+ _objc_msgSend$_configureConnection:
+ _objc_msgSend$_deliverDecision:on:identity:didWin:outcome:source:reason:detail:registeredAt:
+ _objc_msgSend$_endPendingStandbyAnnouncingWon:
+ _objc_msgSend$_engageRoutingTargetHoldIfEligible
+ _objc_msgSend$_engageRoutingTargetStandbyForGeneration:
+ _objc_msgSend$_entryForIdentity:
+ _objc_msgSend$_evaluateTimeouts
+ _objc_msgSend$_evictEntry:
+ _objc_msgSend$_initSharedObserver
+ _objc_msgSend$_initWithConnection:requiresPeerVerification:
+ _objc_msgSend$_initWithLedger:listener:requiresPeerEntitlement:
+ _objc_msgSend$_initiateEmergencyCall
+ _objc_msgSend$_isTornDownSynchronized
+ _objc_msgSend$_ledgerPublisher
+ _objc_msgSend$_listener
+ _objc_msgSend$_maybeEngageRoutingTargetStandby
+ _objc_msgSend$_parkWaiter:forIdentity:existingEntry:
+ _objc_msgSend$_parkWaiterForIdentity:entry:reason:detail:deliverOn:completion:
+ _objc_msgSend$_pruneActivationKinds
+ _objc_msgSend$_pruneHistory
+ _objc_msgSend$_publishElectionOutcomeWithDidWin:provisional:
+ _objc_msgSend$_publishProvisionalResolutionWithLost:
+ _objc_msgSend$_receiver
+ _objc_msgSend$_registerActivationKind:forIdentity:
+ _objc_msgSend$_releaseOnQueue:
+ _objc_msgSend$_releaseOnQueue:suppressNotification:
+ _objc_msgSend$_requestReplayOverConnection:
+ _objc_msgSend$_resolveCurrentElectionIdentityAsLostWithReason:
+ _objc_msgSend$_resolveEntry:withOutcome:didWin:observed:
+ _objc_msgSend$_resolveEntry:withOutcome:didWin:observed:source:
+ _objc_msgSend$_resolvePendingStandbyAsWon:
+ _objc_msgSend$_resolveProvisionalEntry:withResult:
+ _objc_msgSend$_runSyncOnMonitorQueue:
+ _objc_msgSend$_startWatchdogOnQueue
+ _objc_msgSend$_startWithLedger:listener:requiresPeerEntitlement:
+ _objc_msgSend$_stateSnapshot
+ _objc_msgSend$_tagElectionWithIdentity:origin:
+ _objc_msgSend$_verifyPeer:
+ _objc_msgSend$announceStandbyDidBegin
+ _objc_msgSend$announceStandbyDidEndAsWon:
+ _objc_msgSend$anonymousListener
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$auditToken
+ _objc_msgSend$callbackQueue
+ _objc_msgSend$cancelAnyHold
+ _objc_msgSend$candidates
+ _objc_msgSend$candidatesFromReplies:
+ _objc_msgSend$candidatesFromReplies:nameResolver:
+ _objc_msgSend$candidatesFromResults:
+ _objc_msgSend$clearPublishedElectionData
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$deadlineContinuousNanos
+ _objc_msgSend$debugDeviceDescription
+ _objc_msgSend$decisionBlock
+ _objc_msgSend$decisionForElection:reason:detail:deliverOn:completion:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$delegate
+ _objc_msgSend$deliverOutcome:provisional:
+ _objc_msgSend$deliveryQueue
+ _objc_msgSend$detail
+ _objc_msgSend$deviceClassesFromElectionData:
+ _objc_msgSend$deviceClassesInCandidates:
+ _objc_msgSend$deviceNameResolver
+ _objc_msgSend$dictionary
+ _objc_msgSend$didWin
+ _objc_msgSend$electionId
+ _objc_msgSend$electionLedger
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$endpoint
+ _objc_msgSend$engageHoldIfEligibleInCandidates:generation:onRelease:
+ _objc_msgSend$evaluateAndHoldIfNeededWithEligibility:generation:expectedSenderIdsId:onRelease:
+ _objc_msgSend$handleRoutingTargetReleaseWithLost:
+ _objc_msgSend$holdWatchdogTimeout
+ _objc_msgSend$identity
+ _objc_msgSend$identityWithRawValue:
+ _objc_msgSend$idsDeviceID
+ _objc_msgSend$idsIdentifier
+ _objc_msgSend$init
+ _objc_msgSend$initWithClock:decisionTimeout:promotionWindow:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithIdentity:
+ _objc_msgSend$initWithIdentity:electionId:didWin:candidates:resolvedAtContinuousNanos:
+ _objc_msgSend$initWithIdsIdentifier:goodnessScore:deviceClass:productType:isWinner:isLocalDevice:deviceGroup:userConfidence:pHash:deviceName:
+ _objc_msgSend$initWithIdsIdentifier:goodnessScore:deviceClass:productType:isWinner:isLocalDevice:deviceGroup:userConfidence:pHash:deviceName:roomName:
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithRawValue:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isDeviceSelectionEnabled
+ _objc_msgSend$isElectionLedgerEnabled
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isHolding
+ _objc_msgSend$isLocalDevice
+ _objc_msgSend$isLocalEligibleRoutingTargetInCandidates:
+ _objc_msgSend$isMonitorDataSiriDeviceRoutingEnabled
+ _objc_msgSend$isWinner
+ _objc_msgSend$isWinnerDecidedLocallyWithoutElectionInCandidates:
+ _objc_msgSend$myriadMonitorTimeOutInterval
+ _objc_msgSend$namesForIdsDeviceUniqueIdentifier:
+ _objc_msgSend$onRelease
+ _objc_msgSend$orderedSet
+ _objc_msgSend$outcome
+ _objc_msgSend$publishElectionDataFromReplies:generation:
+ _objc_msgSend$publishOutcome:provisional:
+ _objc_msgSend$publishProvisionalResolutionForElectionId:result:
+ _objc_msgSend$rawValue
+ _objc_msgSend$recordOutcome:
+ _objc_msgSend$recordProvisionalOutcome:
+ _objc_msgSend$registeredAtContinuousNanos
+ _objc_msgSend$releaseHoldAsWon:fromSenderIdsId:
+ _objc_msgSend$releaseHoldLocallyWithResult:
+ _objc_msgSend$releaseHoldWithResult:fromSenderIdsId:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$replayRetainedOutcomesWithReply:
+ _objc_msgSend$resolveProvisionalOutcomeForElectionId:holdResult:
+ _objc_msgSend$resolveProvisionalOutcomeForElectionId:result:
+ _objc_msgSend$resolvedAtContinuousNanos
+ _objc_msgSend$resume
+ _objc_msgSend$roomName
+ _objc_msgSend$scdaStandbyDidBegin
+ _objc_msgSend$scdaStandbyDidEndAsWon:
+ _objc_msgSend$set
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDeadlineContinuousNanos:
+ _objc_msgSend$setDecisionBlock:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDeliveryQueue:
+ _objc_msgSend$setDetail:
+ _objc_msgSend$setExpectedSenderIdsId:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setIdsDeviceID:
+ _objc_msgSend$setOnRelease:
+ _objc_msgSend$setOutcome:
+ _objc_msgSend$setRegisteredAtContinuousNanos:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setResolvedAtContinuousNanos:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$sharedLedger
+ _objc_msgSend$sharedMonitor
+ _objc_msgSend$sharedObserver
+ _objc_msgSend$shortValue
+ _objc_msgSend$shouldAdvertiseEmergencyContinuation
+ _objc_msgSend$signedAdjustedBoostForGoodnessScoreContext:
+ _objc_msgSend$siriDeviceRoutingMode
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$startObserving
+ _objc_msgSend$stopObserving
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$toDictionary
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$waiters
+ _objc_msgSend$winnerIdsIdentifierInCandidates:
+ _objc_opt_self
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_release
+ _swift_retain
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _symbolic $ss12CaseIterableP
+ _symbolic Say_____G So23SCDADeviceRoutingDomainV
+ _symbolic Sb
+ _symbolic ScCy__________G 26SiriCrossDeviceArbitration22MyriadElectionDecisionV s5NeverO
+ _symbolic So19SCDAElectionOutcomeC
+ _symbolic _____ 26SiriCrossDeviceArbitration22MyriadElectionDecisionV
+ _symbolic _____ So23SCDADeviceRoutingDomainV
+ _type_layout_string 26SiriCrossDeviceArbitration22MyriadElectionDecisionV
+ getIDSCopyLocalDeviceUniqueIDSymbolLoc.ptr
+ getWPHeySiriNeedsIdentitySymbolLoc.ptr
+ getWPHeySiriRPIdentitySymbolLoc.ptr
+ init.lastMinted
+ sharedLedger.onceToken
+ sharedLedger.sharedLedger
+ sharedObserver.onceToken
+ sharedObserver.sharedObserver
- +[SCDAUtilities isWatchBoostRebalanceEnabled]
- +[SCDAUtilities setWatchBoostRebalanceEnabledOverride:]
- -[SCDACoordinator _writeElectionDataToDefaults]
- -[SCDACoordinator injectAdvertisementForTesting:forDevice:]
- -[SCDACoordinator myriadSession:]
- -[SCDACoordinator resetMyriadCoordinator:]
- -[SCDACoordinator startAdvertisingEmergencySignal]
- -[SCDACoordinator startListeningToEmergencySignal]
- -[SCDACoordinator stateAsString:]
- -[SCDACoordinator updateRepliesWith:id:data:]
- -[SCDARecord(InternalDebug) deviceName]
- GCC_except_table1022
- GCC_except_table1042
- GCC_except_table1063
- GCC_except_table1131
- GCC_except_table1159
- GCC_except_table1162
- GCC_except_table251
- GCC_except_table261
- GCC_except_table529
- GCC_except_table68
- GCC_except_table758
- GCC_except_table804
- GCC_except_table875
- GCC_except_table890
- GCC_except_table940
- GCC_except_table944
- GCC_except_table951
- GCC_except_table978
- __OBJC_$_CLASS_METHODS_SCDACoordinator
- __OBJC_$_INSTANCE_METHODS_SCDACoordinator
- __OBJC_$_PROP_LIST_SCDACoordinator
- __OBJC_CLASS_PROTOCOLS_$_SCDACoordinator
- ___42-[SCDACoordinator resetMyriadCoordinator:]_block_invoke
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0l
- _getWPHeySiriKeyManufacturerData
- _objc_msgSend$_writeElectionDataToDefaults
- _objc_msgSend$heySiri:foundDevice:withInfo:
- _objc_msgSend$myriadCoordinator:didAddAdvertisement:toSession:
- _objc_msgSend$myriadCoordinator:didEnterState:fromState:
- _objc_msgSend$myriadCoordinator:didReceiveAdvertisement:
- _objc_msgSend$myriadCoordinator:willStartAdvertisingUsingData:
- _objc_msgSend$myriadCoordinator:willStartAdvertisingWithSlowDownInterval:
- _objc_msgSend$myriadCoordinatorBTLEDidEndAdvertising:
- _objc_msgSend$myriadCoordinatorBTLEDidEndScanning:
- _objc_msgSend$myriadCoordinatorBTLEDidStartAdvertising:
- _objc_msgSend$myriadCoordinatorBTLEDidStartScanning:
- _objc_msgSend$myriadCoordinatorIsAdvertisingEmergency:
- _objc_msgSend$myriadCoordinatorOverallTimerCancelled:
- _objc_msgSend$stateAsString:
CStrings:
+ "\n    waiting: %@ for %llums"
+ "\n  identity=%llu state=%@"
+ " deadlineIn=%lldms"
+ " didWin=%d candidates=%lu"
+ " entries=%lu invalidated=%d"
+ " waiters=%lu"
+ "\""
+ "#"
+ "%@ activation started with no electionIdentity"
+ "%@ query on unregistered identity %llu"
+ "%@ query with no identity"
+ "%@%@:%@"
+ "%s #scda BTLE foundDevice callback entered at: %lld from: %@"
+ "%s #scda BTLE processing advert in state: %@ from: %@ BTLE address= %@ record= %@ advData= %@ queueHop= %lld ms"
+ "%s #scda adjustedScoreOverride was set: %d"
+ "%s #scda adjustment took goodness below zero (%d %+d); flooring to 0"
+ "%s BTLE notify myriad loss, identity %{public}@"
+ "%s BTLE notify myriad won, identity %{public}@"
+ "%s Clear suppressed — routing target hold is active for %lu completion(s); hold will resolve them"
+ "%s Myriad decision had %d block(s) waiting (signal = %zd, forceLost = %{BOOL}d)"
+ "%s Myriad monitor safety timer fired but a routing target hold is active — ignoring; hold owns the wait"
+ "%s Parking command on the standby routing target hold queue (reason = %@, depth will be %lu)."
+ "%s Queueing command waiting for Myriad decision: %@ (reason = %@, depth will be %lu)."
+ "%s Releasing after %f seconds for Myriad decision (reason = %@) and dequeue signal %zd."
+ "%s Releasing command immediately for Myriad decision: %@ (reason = %@)."
+ "%s a second SCDAStandbyObserver listener registered; the earlier one stops receiving standby announcements"
+ "%s candidatesFromResults couldn't read results, returning without parsing"
+ "%s decisionForElection called without a completion or delivery queue, reason %{public}@"
+ "%s dequeueBlocksWaitingForMyriadDecision suppressed — routing target hold is active; %lu completion(s) will release when hold resolves"
+ "%s deviceClassesInMostRecentElection received no election data"
+ "%s election activation kind conflict: %{public}@. One request has one activation kind. The first registration stands, because a waiter may already have been answered against it."
+ "%s election activation kind not registered: %{public}@. The answer is unaffected; a non-arbitrating activation pays one decision timeout of latency and reports source=timeout."
+ "%s election candidate: refusing a decoded %{public}@ of %d, outside 0...%d"
+ "%s election identity %llu replaced by %llu while still outstanding: %{public}@. The displaced request has no outcome to match, so its waiters time out into a win they did not earn."
+ "%s election identity missing where one is required: %{public}@. Treating it as a loss: the outcome cannot be matched to its request, and answering a win would let a device act on an election it may have lost."
+ "%s election identity: refusing to wrap a zero raw value; the caller has lost its identity"
+ "%s election ledger transport: %{public}@ is not declared on macOS, not checking in"
+ "%s election ledger transport: Device Selection owns %{public}@, not checking in"
+ "%s election ledger transport: accepted a publisher connection"
+ "%s election ledger transport: connection interrupted; replay will repopulate on reconnect"
+ "%s election ledger transport: connection invalidated; outcomes can no longer be published"
+ "%s election ledger transport: electionLedger off, not checking in"
+ "%s election ledger transport: entitlement lookup for %{public}@ failed"
+ "%s election ledger transport: no audit token for peer, rejecting"
+ "%s election ledger transport: publish failed: %{public}@"
+ "%s election ledger transport: publisher connected to %{public}@ (peer verification %d)"
+ "%s election ledger transport: publishing identity %{public}@ didWin=%d provisional=%d"
+ "%s election ledger transport: publishing provisional resolution %ld for electionId %{public}@"
+ "%s election ledger transport: receiver listening (entitlement required %d)"
+ "%s election ledger transport: recording %lu replayed outcome(s)"
+ "%s election ledger transport: refusing a connection accepted during teardown"
+ "%s election ledger transport: rejecting connection without %{public}@"
+ "%s election ledger transport: replay peer lacks %{public}@, refusing"
+ "%s election ledger transport: replay request failed: %{public}@"
+ "%s election ledger transport: replaying %lu outcome(s)"
+ "%s election ledger: %{public}@ activation supersedes outstanding identity %{public}@"
+ "%s election ledger: answered identity=%llu didWin=1 inferred=1 source=dealloc reason=%{public}@"
+ "%s election ledger: answered identity=%llu electionId=%{public}@ didWin=%d inferred=%d source=%{public}@ waited=%llums candidates=%lu reason=%{public}@ detail=%{private}@"
+ "%s election ledger: deallocated with %lu waiter(s) on identity %llu; answering win. Invalidate first. %{public}@"
+ "%s election ledger: decision timeout configured to %f"
+ "%s election ledger: election resolved didWin=%d with no identity; not published"
+ "%s election ledger: identity %llu activated by %{public}@ (arbitrates=%d)"
+ "%s election ledger: identity %llu already resolved, ignoring duplicate outcome"
+ "%s election ledger: identity %llu already resolved, ignoring provisional outcome"
+ "%s election ledger: identity %llu preempts the hold on identity %llu"
+ "%s election ledger: identity %llu promoted to a win"
+ "%s election ledger: identity %llu promotion window expired"
+ "%s election ledger: identity %llu provisional (electionId %{public}@), %lu waiter(s) parked for up to %.1fs"
+ "%s election ledger: identity %llu registered %{public}@ after %lu waiter(s) parked; answering no-election"
+ "%s election ledger: identity %llu registered %{public}@ in state %{public}@; nothing to release"
+ "%s election ledger: identity %llu resolved as a loss (hold result %ld)"
+ "%s election ledger: identity %llu timed out with no decision, answering the liveness default"
+ "%s election ledger: identity %{public}@ left outstanding (%{public}@); a standby hold owns it"
+ "%s election ledger: identity %{public}@ resolved as lost (%{public}@); its election reached no decision"
+ "%s election ledger: ignoring a configured decision timeout of %f; keeping %f"
+ "%s election ledger: invalidating with identity %llu outstanding"
+ "%s election ledger: invalidating with identity %llu provisional; resolving as the observed loss"
+ "%s election ledger: no provisional outcome to resolve for electionId %{public}@"
+ "%s election ledger: parked %{public}@ on identity %llu (%lu waiter(s)) detail=%{private}@"
+ "%s election ledger: provisional outcome with no identity cannot be resolved, dropping"
+ "%s election ledger: publishing identity %{public}@ didWin=%d provisional=%d candidates=%lu"
+ "%s election ledger: publishing provisional resolution for identity %{public}@ lost=%d"
+ "%s election ledger: recording identity %llu didWin=%d electionId=%{public}@ candidates=%lu"
+ "%s election ledger: resolved identity %llu didWin=%d observed=%d source=%{public}@ waiters=%lu"
+ "%s election ledger: resolving provisional identity %llu (electionId %{public}@) from signal naming %{public}@"
+ "%s election ledger: tagging this %{public}@ election with identity %{public}@"
+ "%s election ledger: unkeyed outcome (electionId %{public}@, didWin %d) matches no waiter"
+ "%s routing target standby resolved Lost for election generation %llu; running deferred abort delegate"
+ "%s routing target standby resolved Won for election generation %llu; UI will be retained for the promoted session"
+ "%s routing target standby safety timer fired for election generation %llu; running deferred abort"
+ "%s siriDeviceRouting standby engaged for election generation %llu; suppressing abort delegate"
+ "%s siriDeviceRouting standby not engaged — no election generation has been published."
+ "%s siriDeviceRouting: %s release ignored — no hold is active."
+ "%s siriDeviceRouting: %s release rejected for election generation %llu — sender is not this election's winner (senderIdsId=%s)."
+ "%s siriDeviceRouting: already holding for election generation %llu — re-engaging, keeping the original release callback."
+ "%s siriDeviceRouting: election generation %llu candidates — %@"
+ "%s siriDeviceRouting: hold watchdog fired after %.1fs — neither Continue nor Dismiss arrived."
+ "%s siriDeviceRouting: holding for election generation %llu — watchdog %.1fs, releaseCallback=%{BOOL}d, expectedSender=hasIdsId."
+ "%s siriDeviceRouting: local %@ with winner %@ — %@ routing target (TV→accessory policy)"
+ "%s siriDeviceRouting: local %s release ignored — no hold is active."
+ "%s siriDeviceRouting: no identifier for routing domain %u — not a declared domain"
+ "%s siriDeviceRouting: not engaging standby — generation 0 identifies no election."
+ "%s siriDeviceRouting: not holding for election generation %llu — no winner IDS identity to which to attribute a Continue or Dismiss."
+ "%s siriDeviceRouting: not holding for election generation %llu — this device is not an eligible routing target."
+ "%s siriDeviceRouting: not holding — generation 0 identifies no election."
+ "%s siriDeviceRouting: preempting the hold for election generation %llu — generation %llu arrived."
+ "%s siriDeviceRouting: releasing the hold for election generation %llu — result=%s, notify=%{BOOL}d, callback=%{BOOL}d."
+ "%s siriDeviceRouting: revoking routing eligibility for election generation %llu — no election candidates."
+ "%s siriDeviceRouting: revoking routing eligibility for election generation %llu — the winner forced a local decision without completing an election."
+ "%s siriDeviceRouting: revoking routing eligibility for election generation %llu — this device is not an eligible routing target for the winner."
+ "%s siriDeviceRouting: standby engaged for election generation %llu"
+ "%s siriDeviceRouting: standby routing target hold released → flushing %lu queued completion(s) result=%s didWin=%d (generation=%llu)"
+ "%s stopMonitoring while holding — cancelling routing target hold so completions drain"
+ "(winner)"
+ "+[SCDAElectionCandidate candidatesFromResults:]"
+ "+[SCDAElectionIdentity identityWithRawValue:]"
+ "+[SCDAElectionLedgerReceiver _startWithLedger:listener:requiresPeerEntitlement:]"
+ "+[SCDAElectionLedgerReceiver startWithLedger:]"
+ ", "
+ ",ids=%@"
+ "-[SCDACoordinator _maybeEngageRoutingTargetStandby]"
+ "-[SCDACoordinator(ElectionLedger) _publishElectionOutcomeWithDidWin:provisional:]"
+ "-[SCDACoordinator(ElectionLedger) _publishProvisionalResolutionWithLost:]"
+ "-[SCDACoordinator(ElectionLedger) _resolveCurrentElectionIdentityAsLostWithReason:]"
+ "-[SCDACoordinator(ElectionLedger) _tagElectionWithIdentity:origin:]"
+ "-[SCDACoordinator(SiriDeviceRoutingStandby) _engageRoutingTargetStandbyForGeneration:]_block_invoke"
+ "-[SCDACoordinator(SiriDeviceRoutingStandby) _resolvePendingStandbyAsWon:]"
+ "-[SCDAElectionDataPublisher publishElectionDataFromReplies:generation:]"
+ "-[SCDAElectionLedger _deliverDecision:on:identity:didWin:outcome:source:reason:detail:registeredAt:]"
+ "-[SCDAElectionLedger _evaluateTimeouts]"
+ "-[SCDAElectionLedger _parkWaiter:forIdentity:existingEntry:]"
+ "-[SCDAElectionLedger _registerActivationKind:forIdentity:]"
+ "-[SCDAElectionLedger _resolveEntry:withOutcome:didWin:observed:source:]"
+ "-[SCDAElectionLedger _resolveProvisionalEntry:withResult:]"
+ "-[SCDAElectionLedger dealloc]"
+ "-[SCDAElectionLedger decisionForElection:reason:detail:deliverOn:completion:]"
+ "-[SCDAElectionLedger invalidate]_block_invoke"
+ "-[SCDAElectionLedger recordOutcome:]"
+ "-[SCDAElectionLedger recordOutcome:]_block_invoke"
+ "-[SCDAElectionLedger recordProvisionalOutcome:]_block_invoke"
+ "-[SCDAElectionLedger resolveProvisionalOutcomeForElectionId:result:]_block_invoke"
+ "-[SCDAElectionLedgerPublisher _configureConnection:]_block_invoke"
+ "-[SCDAElectionLedgerPublisher _initWithConnection:requiresPeerVerification:]"
+ "-[SCDAElectionLedgerPublisher _receiver]_block_invoke"
+ "-[SCDAElectionLedgerPublisher _verifyPeer:]"
+ "-[SCDAElectionLedgerPublisher publishOutcome:provisional:]_block_invoke"
+ "-[SCDAElectionLedgerPublisher publishProvisionalResolutionForElectionId:result:]_block_invoke"
+ "-[SCDAElectionLedgerPublisher replayRetainedOutcomesWithReply:]_block_invoke"
+ "-[SCDAElectionLedgerReceiver _requestReplayOverConnection:]_block_invoke"
+ "-[SCDAElectionLedgerReceiver _requestReplayOverConnection:]_block_invoke_2"
+ "-[SCDAElectionLedgerReceiver listener:shouldAcceptNewConnection:]"
+ "-[SCDAGoodnessScoreEvaluator signedAdjustedBoostForGoodnessScoreContext:]"
+ "-[SCDAHoldController _releaseOnQueue:suppressNotification:]"
+ "-[SCDAHoldController _startWatchdogOnQueue]_block_invoke"
+ "-[SCDAHoldController evaluateAndHoldIfNeededWithEligibility:generation:expectedSenderIdsId:onRelease:]_block_invoke"
+ "-[SCDAHoldController releaseHoldLocallyWithResult:]_block_invoke"
+ "-[SCDAHoldController releaseHoldWithResult:fromSenderIdsId:]_block_invoke"
+ "-[SCDAMonitor _engageRoutingTargetHoldIfEligible]_block_invoke"
+ "-[SCDAMonitor deviceClassesInMostRecentElection]"
+ "-[SCDAMonitor stopMonitoring]_block_invoke"
+ "-[SCDAStandbyHoldCoordinator engageHoldIfEligibleInCandidates:generation:onRelease:]"
+ "-[SCDAStandbyObserver setListener:]"
+ "/System/Library/PrivateFrameworks/IDS.framework/Contents/MacOS/IDS"
+ "<%@ %llu>"
+ "<%@ %p"
+ "<%@ %p identity=%@ electionId=%@ didWin=%d candidates=%lu>"
+ "<SCDADeviceNameInfo: room=%@ name=%@>"
+ ">"
+ "Apple Vision Pro"
+ "Apple Watch"
+ "AudioDonation"
+ "B16@?0@\"SCDAElectionCandidate\"8"
+ "BackChannelPrompt"
+ "CommandDispatch"
+ "ContinuousVoiceTrigger"
+ "Direct"
+ "ElectionParticipation"
+ "ErrorDialog"
+ "IDSCopyLocalDeviceUniqueID"
+ "LocalTurn"
+ "Mac"
+ "MultiUserState"
+ "NO-IDS-ID"
+ "Other"
+ "Q8@?0"
+ "RaiseToSpeak"
+ "RecordingStopAlert"
+ "SCDADecodeBoundedInt"
+ "SCDADeviceRoutingDomainIdentifier"
+ "SCDAElectionActivationKindConflict"
+ "SCDAElectionActivationKindMissing"
+ "SCDAElectionIdentityMissing"
+ "SCDAElectionIdentityReplaced"
+ "SCDAElectionLedgerDecisionTimeout"
+ "SCDAElectionLedgerPeerHasEntitlement"
+ "Siri"
+ "SpeechRequest"
+ "TimedOut"
+ "TwoShotFeedback"
+ "TwoShotPrompt"
+ "Unknown(%ld)"
+ "UtteranceGrading"
+ "WPHeySiriNeedsIdentity"
+ "WPHeySiriRPIdentity"
+ "[SiriDeviceRouting] Generation mismatch: expected %llu, got %llu. Discarding stale data."
+ "[SiriDeviceRouting] No election data found in defaults."
+ "[SiriDeviceRouting] Read election data: %lu results, generation: %llu"
+ "[SiriDeviceRouting] Wrote election data: %lu results, generation: %llu"
+ "_SCDAIsLocalEligibleRoutingTarget"
+ "absent"
+ "activation kind %@ registered with no identity"
+ "adjusted voice trigger"
+ "alarm"
+ "alert firing voice trigger"
+ "an untagged election resolved while an identity was held for standby"
+ "ask"
+ "candidates"
+ "cc=%d epId=%@ MyriadRecord: hash=%#06X,good=%03d,conf=%d,dc=%@,pt=%d,tb=%d,isMe=%@,g=%d%@"
+ "com.apple.scda.routingTargetReleaseObserver"
+ "com.apple.siri.crossdevicearbitration.electionledger"
+ "com.apple.siri.crossdevicearbitration.electionledger.receiver"
+ "com.apple.siri.crossdevicearbitration.electionledger.receiver.delivery"
+ "com.apple.siri.deviceselection"
+ "com.apple.siri.deviceselection.allow"
+ "com.apple.siri.myriad.runner_up.release.lost"
+ "com.apple.siri.myriad.runner_up.release.won"
+ "com.apple.siri.scda.electionledger.publisher"
+ "com.apple.siri.scda.siriDeviceRouting-hold"
+ "dealloc"
+ "decision(for:reason:detail:)"
+ "device"
+ "device_selection"
+ "didWin"
+ "direct trigger"
+ "electionId"
+ "electionLedger"
+ "eligible"
+ "emergencyFallback"
+ "evicted"
+ "goodness score voice trigger"
+ "hasIdsId"
+ "history"
+ "identity"
+ "identity %llu registered %@, then %@"
+ "identity-missing"
+ "in-task voice trigger"
+ "intercom"
+ "monitorDataSiriDeviceRouting"
+ "no-election"
+ "not"
+ "observed"
+ "pending"
+ "present"
+ "provisional"
+ "q24@?0@\"SCDAElectionLedgerEntry\"8@\"SCDAElectionLedgerEntry\"16"
+ "rawValue"
+ "resolved"
+ "resolvedAt"
+ "roomName"
+ "set"
+ "siriDeviceRouting"
+ "siriDeviceRoutingRemoteExecution"
+ "softlink:r:path:/System/Library/PrivateFrameworks/IDS.framework/IDS"
+ "state machine returned to no activity"
+ "superseded by a %@ activation"
+ "teardown"
+ "timeout"
+ "timer"
+ "unknown"
+ "v16@?0@\"NSArray\"8"
+ "voice trigger"
+ "watch direct trigger"
+ "watch voice trigger"
- "%s #scda BTLE processing advert in state: %@ from: %@ BTLE address= %@ record= %@ advData= %@"
- "%s #scda adjustedScoreOverride was set: %du"
- "%s BTLE notify myriad loss"
- "%s BTLE notify myriad won"
- "%s Dequeueing command for Myriad decision: %@ (reason = %@)."
- "%s Dequeuing after %f seconds for Myriad decision (reason = %@) and dequeue signal %zd."
- "%s Myriad decision had %d block(s) waiting"
- "%s Queueing command waiting for Myriad decision: %@ (reason = %@)."
- "-[SCDAGoodnessScoreEvaluator getMyriadAdjustedBoostForGoodnessScoreContext:]"
- "[MultiStage] Generation mismatch: expected %llu, got %llu. Discarding stale data."
- "[MultiStage] No election data found in defaults."
- "[MultiStage] Read election data: %lu results, generation: %llu"
- "[MultiStage] Wrote election data: %lu results, generation: %llu"
- "cc=%d epId=%@ MyriadRecord: hash=%#06X,good=%03d,conf=%d,dc=%@,pt=%d,tb=%d,isMe=%@,g=%d"
- "monitorDataHandoff"
- "\x91"
```

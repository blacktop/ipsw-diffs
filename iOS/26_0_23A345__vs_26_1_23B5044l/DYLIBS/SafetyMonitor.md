## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-1062.0.1.0.1
-  __TEXT.__text: 0x73084
+1067.0.2.0.0
+  __TEXT.__text: 0x73cac
   __TEXT.__auth_stubs: 0x1270
   __TEXT.__objc_methlist: 0x4d64
   __TEXT.__const: 0x1380

   __TEXT.__objc_methtype: 0x2166
   __TEXT.__objc_stubs: 0x58e0
   __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1480
+  __DATA_CONST.__const: 0x1478
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9A438798-3262-31AA-85E2-829697D8B96D
+  UUID: CEBFF489-0082-34A7-AC1F-09670B8E11D8
   Functions: 2185
-  Symbols:   5696
+  Symbols:   5694
   CStrings:  4009
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_SafetyMonitor
Functions:
~ -[SMAppDeletionManager isMessagesAppInstalled] : 288 -> 308
~ -[SMSessionMonitorState setCurrentRegionState:] : 252 -> 272
~ -[SMSessionMonitorState setTriggerPending:] : 220 -> 240
~ -[SMSessionMonitorState setTriggerConfirmed:] : 220 -> 240
~ ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke : 492 -> 512
~ ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke.21 : 452 -> 472
~ ___57-[SMEligibilityChecker checkReceiverEligibility:handler:]_block_invoke.22 : 1028 -> 1068
~ -[SMEligibilityChecker checkConversationEligibility:handler:] : 1164 -> 1184
~ ___61-[SMEligibilityChecker checkConversationEligibility:handler:]_block_invoke : 356 -> 392
~ ___61-[SMEligibilityChecker checkConversationEligibility:handler:]_block_invoke.32 : 540 -> 560
~ ___101-[SMEligibilityChecker resolveEndpointsForDestinations:service:requiredCapabilities:completionBlock:]_block_invoke : 564 -> 584
~ -[SMEligibilityChecker checkRecipientAccountIsUnique:] : 384 -> 404
~ _log_analytics_submission : 500 -> 520
~ ___76-[SMCloudKitFunction requestSafetyCacheRecordFromZone:withToken:completion:]_block_invoke : 532 -> 552
~ ___76-[SMCloudKitFunction requestSafetyCacheRecordFromZone:withToken:completion:]_block_invoke.17 : 1608 -> 1636
~ +[SMMobileSMSPreferencesUtilities migrateIfNeeded] : 660 -> 680
~ +[SMMobileSMSPreferencesUtilities _copyMobileSMSPreferencesValueForKey:] : 276 -> 296
~ +[SMMobileSMSPreferencesUtilities _copyDuetExpertPreferencesValueForKey:] : 276 -> 296
~ +[SMMobileSMSPreferencesUtilities _setMobileSMSPreferencesValue:forKey:] : 292 -> 312
~ +[SMMobileSMSPreferencesUtilities isLockScreenSuggestionsAllowed] : 424 -> 444
~ +[SMMobileSMSPreferencesUtilities showCheckInRemindersTip] : 996 -> 1136
~ -[SMHeartbeatTimer _startHeartbeatForSessionID:handler:] : 528 -> 548
~ ___56-[SMHeartbeatTimer _startHeartbeatForSessionID:handler:]_block_invoke : 228 -> 248
~ -[SMHeartbeatTimer _stopHeartbeatWithHandler:] : 260 -> 280
~ -[SMSessionStartMessage initWithDictionary:] : 3948 -> 3988
~ -[SMSessionStartMessage initWithURL:] : 5588 -> 5636
~ -[SMSessionStartMessage initWithCoder:] : 3548 -> 3628
~ +[SMMessage createMessageFromDict:] : 3076 -> 3732
~ +[SMMessage createMessageFromURL:] : 1576 -> 1836
~ -[SMTriggerDestinationState setTimeToUpdateStatus:] : 276 -> 296
~ -[SMTriggerDestinationState setLastLockDate:] : 276 -> 296
~ -[SMTriggerDestinationState setLastUnlockDate:] : 276 -> 296
~ -[SMTriggerDestinationState setCurrentStatus:] : 308 -> 328
~ -[SMTriggerDestinationState setCurrentStatusDate:] : 272 -> 292
~ -[SMTriggerDestinationState setRoundTripReminderDate:] : 276 -> 296
~ -[SMTriggerDestinationState setUpperBoundEta:] : 260 -> 280
~ -[SMTriggerDestinationState setPredominantModeOfTransport:] : 252 -> 272
~ -[SMTriggerDestinationState setMapsExpectedTravelTime:] : 220 -> 240
~ -[SMTriggerDestinationState setRemainingDistance:] : 220 -> 240
~ -[SMCache logCacheForSessionID:role:deviceType:transaction:hashString:] : 2088 -> 2308
~ +[SMCache logNoCacheDataForSessionID:role:deviceType:transaction:] : 272 -> 292
~ ___43-[SMCache shiftLocation:queue:withHandler:]_block_invoke_2 : 112 -> 132
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.61 : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.62 : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.63 : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.64 : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.65 : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.66 : 252 -> 272
~ ___41-[SMCache shiftLocationsOnQueue:handler:]_block_invoke.67 : 464 -> 484
~ -[SMKeyReleaseMessage initWithDictionary:] : 3604 -> 3616
~ -[SMKeyReleaseMessage initWithURL:] : 5252 -> 5264
~ -[SMKeyReleaseMessage initWithCoder:] : 3400 -> 3396
~ -[SMAppDeletionManager _addObserver:] : 404 -> 424
~ -[SMAppDeletionManager _removeObserver:] : 296 -> 316
~ -[SMSafetyMonitorManager initWithRestorationIdentifier:] : 700 -> 724
~ -[SMSafetyMonitorManager _createConnection] : 5172 -> 5192
~ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2 : 216 -> 236
~ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.331 : 196 -> 216
~ -[SMSafetyMonitorManager handleDaemonStart] : 280 -> 300
~ ___43-[SMSafetyMonitorManager handleDaemonStart]_block_invoke : 288 -> 308
~ -[SMSafetyMonitorManager _proxyForServicingSelector:asynchronous:withErrorHandler:] : 412 -> 432
~ ___95-[SMSafetyMonitorManager launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:]_block_invoke : 372 -> 392
~ ___95-[SMSafetyMonitorManager launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:]_block_invoke_3 : 240 -> 260
~ ___54-[SMSafetyMonitorManager _startHeartbeatForSessionID:]_block_invoke : 224 -> 244
~ ___40-[SMSafetyMonitorManager _stopHeartbeat]_block_invoke : 200 -> 220
~ -[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:] : 756 -> 776
~ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke : 356 -> 376
~ -[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:] : 464 -> 484
~ -[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:] : 536 -> 556
~ -[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:] : 776 -> 796
~ -[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:] : 768 -> 788
~ -[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:] : 776 -> 796
~ -[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:] : 768 -> 788
~ -[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:] : 756 -> 776
~ -[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:] : 804 -> 824
~ -[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:] : 756 -> 776
~ -[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:] : 440 -> 460
~ -[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:] : 440 -> 460
~ -[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:] : 440 -> 460
~ -[SMSafetyMonitorManager kickedFromIMessageGroupWith:] : 440 -> 460
~ -[SMSafetyMonitorManager startMonitoringInitiatorSafetyCacheWithHandler:] : 532 -> 552
~ -[SMSafetyMonitorManager onInitiatorSafetyCacheChangeForSessionID:phoneCache:watchCache:cacheExpiryDate:cacheReleaseDate:] : 448 -> 468
~ -[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:] : 776 -> 796
~ -[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:] : 776 -> 796
~ -[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:] : 1080 -> 1100
~ -[SMSafetyMonitorManager requestTimeFromTimed] : 512 -> 532
~ -[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:] : 296 -> 316
~ -[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection] : 224 -> 244
~ -[SMSafetyMonitorManager submitInitializationAnalyticsEventWithError:conversation:duration:] : 536 -> 556

```

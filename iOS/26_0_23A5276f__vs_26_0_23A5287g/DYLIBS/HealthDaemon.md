## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6087.1.2.1.0
-  __TEXT.__text: 0x77a6ac
-  __TEXT.__auth_stubs: 0x4770
-  __TEXT.__objc_methlist: 0x42a74
-  __TEXT.__const: 0x1d394
+6093.0.0.0.0
+  __TEXT.__text: 0x77c28c
+  __TEXT.__auth_stubs: 0x47b0
+  __TEXT.__objc_methlist: 0x42b0c
+  __TEXT.__const: 0x1d3a4
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x78a3e
+  __TEXT.__cstring: 0x78a15
   __TEXT.__constg_swiftt: 0x1064
   __TEXT.__swift5_typeref: 0xc01
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_capture: 0x4c4
-  __TEXT.__oslogstring: 0x41395
+  __TEXT.__swift5_capture: 0x4e4
+  __TEXT.__oslogstring: 0x4180f
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__gcc_except_tab: 0x37f58
+  __TEXT.__gcc_except_tab: 0x38138
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1c610
-  __TEXT.__eh_frame: 0x22c0
-  __TEXT.__objc_classname: 0xc42a
-  __TEXT.__objc_methname: 0x8dbbb
-  __TEXT.__objc_methtype: 0x168d4
-  __TEXT.__objc_stubs: 0x4fde0
-  __DATA_CONST.__got: 0x5560
-  __DATA_CONST.__const: 0x1d0e8
+  __TEXT.__unwind_info: 0x1c680
+  __TEXT.__eh_frame: 0x2310
+  __TEXT.__objc_classname: 0xc41e
+  __TEXT.__objc_methname: 0x8de3e
+  __TEXT.__objc_methtype: 0x1692c
+  __TEXT.__objc_stubs: 0x4ff20
+  __DATA_CONST.__got: 0x5580
+  __DATA_CONST.__const: 0x1d138
   __DATA_CONST.__objc_classlist: 0x28d8
   __DATA_CONST.__objc_catlist: 0x4b8
   __DATA_CONST.__objc_protolist: 0x9a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19bf8
+  __DATA_CONST.__objc_selrefs: 0x19c40
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d40
   __DATA_CONST.__objc_arraydata: 0x8430
-  __AUTH_CONST.__auth_got: 0x23d0
-  __AUTH_CONST.__const: 0xf2c8
-  __AUTH_CONST.__cfstring: 0x3ca40
-  __AUTH_CONST.__objc_const: 0x7c258
+  __AUTH_CONST.__auth_got: 0x23f0
+  __AUTH_CONST.__const: 0xf378
+  __AUTH_CONST.__cfstring: 0x3cac0
+  __AUTH_CONST.__objc_const: 0x7c3c8
   __AUTH_CONST.__objc_arrayobj: 0x1e48
-  __AUTH_CONST.__objc_intobj: 0x3e70
+  __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xc658
   __AUTH.__data: 0x4b8
-  __DATA.__objc_ivar: 0x4314
+  __DATA.__objc_ivar: 0x4338
   __DATA.__data: 0x8078
   __DATA.__common: 0x64
   __DATA.__bss: 0x858
-  __DATA_DIRTY.__objc_ivar: 0xe68
+  __DATA_DIRTY.__objc_ivar: 0xe6c
   __DATA_DIRTY.__objc_data: 0xdba0
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__bss: 0x3b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A958AEFD-4479-3B8D-9EB7-50ED28A6C8A4
-  Functions: 34094
-  Symbols:   103050
-  CStrings:  43802
+  UUID: 3A77BE0F-713D-3B54-890A-9CA49C72B1E9
+  Functions: 34118
+  Symbols:   103124
+  CStrings:  43841
 
Symbols:
+ +[HDAuthorizationBackupSyncEntity startSyncAnchorForEntity]
+ -[HDCloudSyncManager(Analytics) _gatherAttachmentAnalyticsForZoneID:repository:error:]
+ -[HDDaemon runtimeDebugInfo]
+ -[HDDatabase _protectedDataQueue_handleSpringboardLockoutNotification]
+ -[HDDatabase unitTest_triggerSpringboardLockout]
+ -[HDHRCoordinatorDataCollector unitTest_unregisterWithAggregators]
+ -[HDHealthRecordsAccountExistenceNotifier isCurrentCountryCodeSupportingCHR]
+ -[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]
+ -[HDProfile _newHealthRecordsAccountExistenceNotifier]
+ -[HDProfile _observerClassStringFor:late:]
+ -[HDProfile dealloc]
+ -[HDSleepDaySummaryBuilder initWithProfile:dayIndexRange:weekday:options:eighteenthBirthdayDayIndex:gregorianCalendar:sourceOrderProvider:]
+ -[HDSleepDaySummaryBuilder initWithProfile:morningIndex:weekday:options:eighteenthBirthdayDayIndex:gregorianCalendar:sourceOrderProvider:]
+ -[HDWorkoutBuilderServer _clearTailSpinTimer]
+ -[HDWorkoutManager _handleBiometricLockout]
+ -[HDWorkoutManager database:protectedDataDidBecomeAvailable:]
+ -[HDWorkoutManager database:protectedDataDidBecomeAvailable:dueToLockout:]
+ GCC_except_table144
+ _HDTailSpinCategorySlowWorkoutEnd
+ _HDTailSpinCategorySlowWorkoutStart
+ _HDTailSpinTeamIdentifierHealthKit
+ _HKLogDaemonInitialization
+ _HKSleepDurationGoalAdultRecommendation
+ _HKSleepDurationGoalChildRecommendation
+ _OBJC_CLASS_$_HDTailSpin
+ _OBJC_IVAR_$_HDDatabase._protectedDataLock_protectedDataState
+ _OBJC_IVAR_$_HDDatabase._springboardLockoutToken
+ _OBJC_IVAR_$_HDProfile._profileReadyObserversTimer
+ _OBJC_IVAR_$_HDProfile._profileTrackingLock
+ _OBJC_IVAR_$_HDProfile._profileTrackingLock_profileReadyObserversOutstanding
+ _OBJC_IVAR_$_HDSleepDaySummaryBuilder._eighteenthBirthdayDayIndex
+ _OBJC_IVAR_$_HDSleepDaySummaryEnumerator._eighteenthBirthdayDayIndex
+ _OBJC_IVAR_$_HDWorkoutSessionServer._currentStateLock
+ _OBJC_IVAR_$_HDWorkoutSessionServer._currentStateLock_currentState
+ _OBJC_IVAR_$_HDWorkoutSessionServer._tailSpinTimer
+ __OBJC_$_CLASS_METHODS_HDQuantityDatum
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDDatabaseProtectedDataObserver
+ ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.470
+ ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.473
+ ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.445
+ ___122-[HDAuthorizationManager handleHealthConceptAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.468
+ ___127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.498
+ ___133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.418
+ ___134-[HDAuthorizationManager _authorizationRequestStatusForClientBundleIdentifier:writeTypes:readTypes:updateAuthorizationStatuses:error:]_block_invoke.401
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.368
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.371
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke_2
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke_2.370
+ ___43-[HDWorkoutBuilderServer _didUpdateEvents:]_block_invoke.614
+ ___43-[HDWorkoutManager _handleBiometricLockout]_block_invoke
+ ___45-[HDWorkoutBuilderServer _didUpdateMetadata:]_block_invoke.604
+ ___46-[HDWorkoutSessionServer didBeginNewActivity:]_block_invoke.623
+ ___47-[HDWorkoutBuilderServer _didUpdateStatistics:]_block_invoke.653
+ ___47-[HDWorkoutSessionServer _queue_generateError:]_block_invoke.709
+ ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.706
+ ___48-[HDDatabase unitTest_triggerSpringboardLockout]_block_invoke
+ ___48-[HDWorkoutSessionServer didEndCurrentActivity:]_block_invoke.629
+ ___48-[HDWorkoutSessionServer syncSessionEvent:date:]_block_invoke.673
+ ___49-[HDWorkoutSessionServer remoteSessionDidRecover]_block_invoke.674
+ ___55-[HDWorkoutBuilderServer remote_addSamples:completion:]_block_invoke.574
+ ___55-[HDWorkoutBuilderServer remote_recoverWithCompletion:]_block_invoke.603
+ ___55-[HDWorkoutSessionServer _queue_startInvalidationTimer]_block_invoke.720
+ ___56-[HDWorkoutBuilderServer remote_addMetadata:completion:]_block_invoke.578
+ ___57-[HDWorkoutSessionServer endCurrentActivityOnDate:error:]_block_invoke.644
+ ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke.657
+ ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke_2.658
+ ___59-[HDWorkoutBuilderServer remote_removeMetadata:completion:]_block_invoke.583
+ ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.576
+ ___61-[HDWorkoutBuilderServer remote_addWorkoutEvents:completion:]_block_invoke.576
+ ___61-[HDWorkoutSessionServer _queue_generateConfigurationUpdate:]_block_invoke.710
+ ___63-[HDWorkoutBuilderServer remote_addWorkoutActivity:completion:]_block_invoke.592
+ ___64-[HDNanoSyncManager _queue_receiveTinkerOptInRequest:syncStore:]_block_invoke.821
+ ___64-[HDNanoSyncManager _scheduleResetReceivedNanoSyncAnchorsForHFD]_block_invoke.929
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.545
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.550
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.551
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.560
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.561
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.541
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.546
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.552
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.549
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.553
+ ___65-[HDDatabase _protectedDataQueue_beginObservingContentProtection]_block_invoke
+ ___66-[HDAggregateDataCollector _beginUpdatesHandlerWithSuccess:error:]_block_invoke
+ ___66-[HDHRCoordinatorDataCollector unitTest_unregisterWithAggregators]_block_invoke
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.912
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.914
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke_2.916
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.848
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.866
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.871
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.873
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.875
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.877
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.879
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.881
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.876
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.878
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.880
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.882
+ ___68-[HDNanoSyncManager _queue_recieveStartWorkoutAppRequest:syncStore:]_block_invoke.796
+ ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke.390
+ ___70-[HDDatabase _protectedDataQueue_handleSpringboardLockoutNotification]_block_invoke
+ ___71-[HDWorkoutSessionServer stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.662
+ ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.409
+ ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.410
+ ___73-[HDSkiingWorkoutEventCollector _startUpdatesFromRecordHandlerWithError:]_block_invoke
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.303
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.307
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.310
+ ___74-[HDWorkoutSessionServer _scheduleTailSpinTimeoutForCategory:description:]_block_invoke
+ ___74-[HDWorkoutSessionServer _scheduleTailSpinTimeoutForCategory:description:]_block_invoke_2
+ ___75-[HDWorkoutBuilderServer remote_updateActivityWithUUID:endDate:completion:]_block_invoke.600
+ ___76-[HDNanoSyncManager _queue_receiveTinkerEndToEndCloudSyncRequest:syncStore:]_block_invoke.895
+ ___76-[HDWorkoutSessionServer didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.669
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.433
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.438
+ ___78-[HDNanoSyncManager _queue_recieveCompanionUserNotificationRequest:syncStore:]_block_invoke.807
+ ___79-[HDPostInstallUpdateManager _triggerMigrationForProfile:protected:completion:]_block_invoke.318
+ ___79-[HDWorkoutBuilderServer remote_updateActivityWithUUID:addMetadata:completion:]_block_invoke.602
+ ___80-[HDWorkoutSessionServer beginNewActivityWithConfiguration:date:metadata:error:]_block_invoke.643
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.542
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.544
+ ___82-[HDDatabase _old_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.547
+ ___82-[HDWorkoutSessionServer enableAutomaticDetectionForActivityConfigurations:error:]_block_invoke.646
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.596
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.607
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.608
+ ___86-[HDCloudSyncManager(Analytics) _gatherAttachmentAnalyticsForZoneID:repository:error:]_block_invoke
+ ___86-[HDCloudSyncManager(Analytics) _gatherAttachmentAnalyticsForZoneID:repository:error:]_block_invoke_2
+ ___86-[HDCloudSyncManager(Analytics) _gatherAttachmentAnalyticsForZoneID:repository:error:]_block_invoke_3
+ ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.571
+ ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.572
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.299
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.302
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke_2.304
+ ___94-[HDWorkoutManager generatePauseOrResumeRequestAllowingBackgroundRuntime:metadata:completion:]_block_invoke.371
+ ___96-[HDWorkoutBuilderServer _scheduleTailSpinTimeoutIfNeededForCategory:description:workoutEvents:]_block_invoke
+ ___96-[HDWorkoutBuilderServer _scheduleTailSpinTimeoutIfNeededForCategory:description:workoutEvents:]_block_invoke_2
+ ___block_descriptor_178_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r136r144r152r160r_e47_B104?0q8q16[16C]24d32d40q48q56d64d72d80q88^96lr112l8r120l8s32l8s40l8s48l8s56l8r128l8s64l8s72l8s80l8s88l8r136l8r144l8s96l8r152l8s104l8r160l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"<HDProfileReadyObserver>"8Q16^B24ls32l8
+ ___block_descriptor_40_ea8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s_e34_v16?0"<HDProfileReadyObserver>"8ls32l8u40l8
+ ___block_descriptor_56_e8_32s40r48r_e44_B32?0"HDCloudSyncAttachmentRecord"8q16^24lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e53_B32?0"HDCloudSyncAttachmentReferenceRecord"8q16^24lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e42_v16?0"<HDPostInstallUpdateTaskHandler>"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0lu64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.474
+ ___block_literal_global.548
+ ___block_literal_global.549
+ ___block_literal_global.556
+ ___block_literal_global.562
+ ___block_literal_global.563
+ ___block_literal_global.598
+ ___block_literal_global.600
+ ___block_literal_global.606
+ ___block_literal_global.610
+ ___block_literal_global.612
+ ___block_literal_global.614
+ ___block_literal_global.616
+ ___block_literal_global.618
+ ___block_literal_global.620
+ ___block_literal_global.622
+ ___block_literal_global.628
+ ___block_literal_global.633
+ ___block_literal_global.635
+ ___block_literal_global.647
+ ___block_literal_global.653
+ ___block_literal_global.676
+ ___block_literal_global.677
+ ___block_literal_global.679
+ ___block_literal_global.702
+ ___block_literal_global.707
+ ___block_literal_global.710
+ ___block_literal_global.715
+ ___block_literal_global.723
+ ___block_literal_global.725
+ ___block_literal_global.740
+ ___block_literal_global.771
+ ___block_literal_global.805
+ ___block_literal_global.931
+ ___block_literal_global.935
+ _objc_msgSend$_gatherAttachmentAnalyticsForZoneID:repository:error:
+ _objc_msgSend$_handleBiometricLockout
+ _objc_msgSend$_newHealthRecordsAccountExistenceNotifier
+ _objc_msgSend$_postInstallUpdateHandlerDidFire:completion:
+ _objc_msgSend$_setLogStatus:
+ _objc_msgSend$database:protectedDataDidBecomeAvailable:dueToLockout:
+ _objc_msgSend$daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:
+ _objc_msgSend$generateTailSpinForTeam:category:description:logger:
+ _objc_msgSend$hk_dayIndexByAddingYears:gregorianCalendar:
+ _objc_msgSend$initWithName:queue:completion:
+ _objc_msgSend$initWithProfile:dayIndexRange:weekday:options:eighteenthBirthdayDayIndex:gregorianCalendar:sourceOrderProvider:
+ _objc_msgSend$initWithProfile:morningIndex:weekday:options:eighteenthBirthdayDayIndex:gregorianCalendar:sourceOrderProvider:
+ _objc_msgSend$isCurrentCountryCodeSupportingCHR
+ _objc_msgSend$logStatus
+ _objc_msgSend$runtimeDebugInfo
+ _objc_msgSend$startSyncAnchorForEntity
- +[HDQuantityDatum(HealthKitTests) hdt_quantityDatumForType:startTime:endTime:value:]
- -[HDDataAggregatorConfiguration setHasBackgroundObserver:]
- -[HDDataAggregatorConfiguration setHasForegroundObserver:]
- -[HDSleepDaySummaryBuilder initWithProfile:dayIndexRange:weekday:options:gregorianCalendar:sourceOrderProvider:]
- -[HDSleepDaySummaryBuilder initWithProfile:morningIndex:weekday:options:gregorianCalendar:sourceOrderProvider:]
- -[HDWorkoutManager _handleSpringboardLockoutNotification]
- GCC_except_table195
- _.str.381
- _OBJC_IVAR_$_HDDatabase._protectedDataState
- __HDCreateSurveySnapshotsTable
- __OBJC_$_CLASS_METHODS_HDQuantityDatum(HealthKitTests)
- ___100-[HDCloudSyncManager(Analytics) _reportDailyAttachmentsAnalyticsForProfile:zoneID:repository:error:]_block_invoke
- ___100-[HDCloudSyncManager(Analytics) _reportDailyAttachmentsAnalyticsForProfile:zoneID:repository:error:]_block_invoke_2
- ___100-[HDCloudSyncManager(Analytics) _reportDailyAttachmentsAnalyticsForProfile:zoneID:repository:error:]_block_invoke_3
- ___100-[HDCloudSyncManager(Analytics) _reportDailyAttachmentsAnalyticsForProfile:zoneID:repository:error:]_block_invoke_4
- ___100-[HDCloudSyncManager(Analytics) _reportDailyAttachmentsAnalyticsForProfile:zoneID:repository:error:]_block_invoke_5
- ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.468
- ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.471
- ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.447
- ___122-[HDAuthorizationManager handleHealthConceptAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.470
- ___127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.495
- ___133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.415
- ___134-[HDAuthorizationManager _authorizationRequestStatusForClientBundleIdentifier:writeTypes:readTypes:updateAuthorizationStatuses:error:]_block_invoke.403
- ___36-[HDWorkoutManager initWithProfile:]_block_invoke
- ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.355
- ___43-[HDWorkoutBuilderServer _didUpdateEvents:]_block_invoke.607
- ___45-[HDWorkoutBuilderServer _didUpdateMetadata:]_block_invoke.597
- ___46-[HDWorkoutSessionServer didBeginNewActivity:]_block_invoke.620
- ___47-[HDAggregateDataCollector _queue_beginUpdates]_block_invoke.433
- ___47-[HDWorkoutBuilderServer _didUpdateStatistics:]_block_invoke.646
- ___47-[HDWorkoutSessionServer _queue_generateError:]_block_invoke.706
- ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.700
- ___48-[HDWorkoutSessionServer didEndCurrentActivity:]_block_invoke.626
- ___48-[HDWorkoutSessionServer syncSessionEvent:date:]_block_invoke.670
- ___49-[HDWorkoutSessionServer remoteSessionDidRecover]_block_invoke.671
- ___55-[HDWorkoutBuilderServer remote_addSamples:completion:]_block_invoke.567
- ___55-[HDWorkoutBuilderServer remote_recoverWithCompletion:]_block_invoke.596
- ___55-[HDWorkoutSessionServer _queue_startInvalidationTimer]_block_invoke.717
- ___56-[HDWorkoutBuilderServer remote_addMetadata:completion:]_block_invoke.571
- ___57-[HDWorkoutManager _handleSpringboardLockoutNotification]_block_invoke
- ___57-[HDWorkoutSessionServer endCurrentActivityOnDate:error:]_block_invoke.641
- ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke.650
- ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke_2.651
- ___59-[HDWorkoutBuilderServer remote_removeMetadata:completion:]_block_invoke.576
- ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.573
- ___61-[HDWorkoutBuilderServer remote_addWorkoutEvents:completion:]_block_invoke.569
- ___61-[HDWorkoutSessionServer _queue_generateConfigurationUpdate:]_block_invoke.707
- ___63-[HDWorkoutBuilderServer remote_addWorkoutActivity:completion:]_block_invoke.585
- ___64-[HDNanoSyncManager _queue_receiveTinkerOptInRequest:syncStore:]_block_invoke.818
- ___64-[HDNanoSyncManager _scheduleResetReceivedNanoSyncAnchorsForHFD]_block_invoke.926
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.539
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.547
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.548
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.557
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.558
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.538
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.543
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.549
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.546
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.550
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.908
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.909
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke_2.913
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.845
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.860
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.862
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.870
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.872
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.874
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.876
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.878
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.873
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.875
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.877
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.879
- ___68-[HDNanoSyncManager _queue_recieveStartWorkoutAppRequest:syncStore:]_block_invoke.793
- ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke.392
- ___69-[HDSkiingWorkoutEventCollector _queue_startCollectionWithSessionId:]_block_invoke_2
- ___71-[HDWorkoutSessionServer stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.659
- ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.418
- ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.419
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.304
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.309
- ___75-[HDWorkoutBuilderServer remote_updateActivityWithUUID:endDate:completion:]_block_invoke.593
- ___76-[HDNanoSyncManager _queue_receiveTinkerEndToEndCloudSyncRequest:syncStore:]_block_invoke.892
- ___76-[HDWorkoutSessionServer didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.666
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.434
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.440
- ___78-[HDNanoSyncManager _queue_recieveCompanionUserNotificationRequest:syncStore:]_block_invoke.804
- ___79-[HDPostInstallUpdateManager _triggerMigrationForProfile:protected:completion:]_block_invoke.317
- ___79-[HDWorkoutBuilderServer remote_updateActivityWithUUID:addMetadata:completion:]_block_invoke.595
- ___80-[HDWorkoutSessionServer beginNewActivityWithConfiguration:date:metadata:error:]_block_invoke.640
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.537
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.538
- ___82-[HDDatabase _old_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.544
- ___82-[HDWorkoutSessionServer enableAutomaticDetectionForActivityConfigurations:error:]_block_invoke.643
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.593
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.601
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.605
- ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.564
- ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.565
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.298
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.301
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke_2.303
- ___94-[HDWorkoutManager generatePauseOrResumeRequestAllowingBackgroundRuntime:metadata:completion:]_block_invoke.373
- ___block_descriptor_186_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r136r144r152r160r168r_e47_B104?0q8q16[16C]24d32d40q48q56d64d72d80q88^96lr112l8s32l8r120l8r128l8s40l8s48l8s56l8r136l8s64l8s72l8s80l8s88l8r144l8r152l8s96l8r160l8s104l8r168l8
- ___block_descriptor_40_e8_32s_e46_B16?0"HDCloudSyncAttachmentReferenceRecord"8ls32l8
- ___block_descriptor_48_e8_32s40s_e42_v16?0"<HDPostInstallUpdateTaskHandler>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSError"16ls32l8w40l8
- ___block_descriptor_56_e8_32s40r48r_e53_B32?0"HDCloudSyncAttachmentReferenceRecord"8q16^24lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40r48r56r_e44_B32?0"HDCloudSyncAttachmentRecord"8q16^24lr40l8r48l8s32l8r56l8
- ___block_literal_global.337
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.436
- ___block_literal_global.529
- ___block_literal_global.545
- ___block_literal_global.546
- ___block_literal_global.553
- ___block_literal_global.559
- ___block_literal_global.560
- ___block_literal_global.595
- ___block_literal_global.603
- ___block_literal_global.607
- ___block_literal_global.609
- ___block_literal_global.611
- ___block_literal_global.613
- ___block_literal_global.615
- ___block_literal_global.617
- ___block_literal_global.619
- ___block_literal_global.630
- ___block_literal_global.632
- ___block_literal_global.650
- ___block_literal_global.670
- ___block_literal_global.673
- ___block_literal_global.700
- ___block_literal_global.703
- ___block_literal_global.709
- ___block_literal_global.720
- ___block_literal_global.722
- ___block_literal_global.802
- ___block_literal_global.928
- ___block_literal_global.932
- _objc_msgSend$_handleSpringboardLockoutNotification
- _objc_msgSend$_setStatus:
- _objc_msgSend$daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:
- _objc_msgSend$hk_testableCurrentLocale
- _objc_msgSend$initWithProfile:dayIndexRange:weekday:options:gregorianCalendar:sourceOrderProvider:
- _objc_msgSend$initWithProfile:morningIndex:weekday:options:gregorianCalendar:sourceOrderProvider:
CStrings:
+ " "
+ "%{public}@ lookup state: error checking for gateway backed accounts, skipping to issuer backed accounts lookup. Error: %{public}@"
+ "%{public}@ lookup state: returning \"accounts exist\" since there are gateway backed accounts"
+ "%{public}@ lookup state: returning \"no accounts\" since there are no issuer backed accounts"
+ "%{public}@ lookup state: returning \"unknown\" since there is no CHR profile extension"
+ "%{public}@ lookup state: returning \"unknown\" since there was an error checking issuer backed accounts: %{public}@"
+ "%{public}@ lookup state: returning unit test override value"
+ "%{public}@ lookup state: there are issuer backed accounts, locale is supported: %{public}@"
+ "%{public}@: Ignoring attempted update for background activity. Session has not yet started"
+ "%{public}@: Persisted, consuming %ld datums with last datum: %@ in %0.1f seconds"
+ "%{public}@: Received biolockout notification; flushing protected data"
+ "%{public}@: remote_insertDatums:device:... called."
+ "<%@:%p> Adding unitTest_didReadyProfile for profile"
+ "<%@:%p> Calling unitTest_didReadyProfile for profile"
+ "<%@:%p> End notification of profile ready observers in %0.1f seconds for %@"
+ "<%@:%p> Notified all post profile ready blocks"
+ "<%@:%p> Notified late profile ready observer %@"
+ "<%@:%p> Notified profile ready observer %@"
+ "<%@:%p> Notifying %lu post profile ready blocks"
+ "<%@:%p> Notifying all profile ready observers is slow. Still pending: %@"
+ "<%@:%p> Notifying profile ready observer %@"
+ "<%@:%p> Start notification of %lu profile ready observers for %@"
+ "<%@:%p> unitTest_didReadyProfile for profile returned"
+ "<%p>%@%@"
+ "@72@0:8@16q24Q32Q40@48@56@64"
+ "@80@0:8@16{?=qq}24Q40Q48@56@64@72"
+ "B40@0:8^B16@\"NSLocale\"24^@32"
+ "B40@0:8^B16@24^@32"
+ "HDProfileObservers"
+ "Ignoring invalid protection state transition (%{public}@ -> %{public}@)"
+ "Notifying %lu Daemon Ready Observers"
+ "Slow preparing"
+ "Slow workout end"
+ "TB,R,N,V_hasForegroundObserver"
+ "_currentStateLock"
+ "_currentStateLock_currentState"
+ "_eighteenthBirthdayDayIndex"
+ "_gatherAttachmentAnalyticsForZoneID:repository:error:"
+ "_handleBiometricLockout"
+ "_newHealthRecordsAccountExistenceNotifier"
+ "_notifyProfileReadyObservers called twice!"
+ "_postInstallUpdateHandlerDidFire:completion:"
+ "_profileReadyObserversTimer"
+ "_profileTrackingLock"
+ "_profileTrackingLock_profileReadyObserversOutstanding"
+ "_protectedDataLock_protectedDataState"
+ "_setLogStatus:"
+ "_tailSpinTimer"
+ "database:protectedDataDidBecomeAvailable:dueToLockout:"
+ "daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:"
+ "deviceConfigurationSupportsHealthRecords:givenLocale:error:"
+ "generateTailSpinForTeam:category:description:logger:"
+ "healthd"
+ "hk_dayIndexByAddingYears:gregorianCalendar:"
+ "initWithName:queue:completion:"
+ "initWithProfile:dayIndexRange:weekday:options:eighteenthBirthdayDayIndex:gregorianCalendar:sourceOrderProvider:"
+ "initWithProfile:morningIndex:weekday:options:eighteenthBirthdayDayIndex:gregorianCalendar:sourceOrderProvider:"
+ "isCurrentCountryCodeSupportingCHR"
+ "logStatus"
+ "runtimeDebugInfo"
+ "startSyncAnchorForEntity"
+ "unitTest_triggerSpringboardLockout"
+ "v32@0:8@\"<HDHealthDatabase>\"16B24B28"
+ "v32@0:8@16B24B28"
+ "v32@?0@\"<HDProfileReadyObserver>\"8Q16^B24"
+ "\xf0q"
- "%{public}@: Persisted, consuming %ld datums with last datum: %@."
- "%{public}@: Received springboard lockout notification. Ending all workout sessions"
- "@48@0:8@16d24d32d40"
- "@64@0:8@16q24Q32Q40@48@56"
- "@72@0:8@16{?=qq}24Q40Q48@56@64"
- "Adding unitTest_didReadyProfile for profile %@"
- "B16@?0@\"HDCloudSyncAttachmentReferenceRecord\"8"
- "Calling unitTest_didReadyProfile for profile %@"
- "Difference in Provenance row ID"
- "Difference in Provenance row ID detected in the same call to %s"
- "Difference in Provenance row ID detected in the same call to %s: current %@ != first %@"
- "HealthKitTests"
- "Notified observer (%@) profile ready for profile %@"
- "Notify (%lu) Daemon Ready Observers"
- "Notify (%lu) profile ready blocks for profile %@"
- "Notify (%lu) profile ready observers for profile %@"
- "Notifying observer (%@) profile ready for profile %@"
- "TB,N,V_hasBackgroundObserver"
- "TB,N,V_hasForegroundObserver"
- "[Data Provenance] Workout Condenser Problem Detected"
- "_handleSpringboardLockoutNotification"
- "_protectedDataState"
- "_setStatus:"
- "cound=%lu"
- "daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:"
- "hdt_quantityDatumForType:startTime:endTime:value:"
- "hk_testableCurrentLocale"
- "initWithProfile:dayIndexRange:weekday:options:gregorianCalendar:sourceOrderProvider:"
- "initWithProfile:morningIndex:weekday:options:gregorianCalendar:sourceOrderProvider:"
- "setHasBackgroundObserver:"
- "setHasForegroundObserver:"
- "\xf0A"

```

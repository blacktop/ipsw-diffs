## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/Versions/A/HealthDaemon`

```diff

-5124.0.0.0.0
-  __TEXT.__text: 0x7d5004
+5116.0.0.0.0
+  __TEXT.__text: 0x7d59d0
   __TEXT.__auth_stubs: 0x3240
-  __TEXT.__objc_methlist: 0x3c6a0
+  __TEXT.__objc_methlist: 0x3c710
   __TEXT.__const: 0x1c31c
-  __TEXT.__oslogstring: 0x3c707
+  __TEXT.__oslogstring: 0x3c749
   __TEXT.__swift5_typeref: 0x323
   __TEXT.__swift5_fieldmd: 0x1f4
   __TEXT.__constg_swiftt: 0x4d4
-  __TEXT.__cstring: 0x754c8
+  __TEXT.__cstring: 0x75518
   __TEXT.__swift5_reflstr: 0x1a0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_capture: 0xa0
-  __TEXT.__gcc_except_tab: 0x376b0
+  __TEXT.__gcc_except_tab: 0x37828
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1be38
+  __TEXT.__unwind_info: 0x1bed8
   __TEXT.__eh_frame: 0x3c0
-  __TEXT.__objc_classname: 0xc540
-  __TEXT.__objc_methname: 0x89d97
-  __TEXT.__objc_methtype: 0x1716e
-  __TEXT.__objc_stubs: 0x4d7a0
-  __DATA_CONST.__got: 0x4e18
-  __DATA_CONST.__const: 0xbad8
-  __DATA_CONST.__objc_classlist: 0x2860
+  __TEXT.__objc_classname: 0xc559
+  __TEXT.__objc_methname: 0x8a0b8
+  __TEXT.__objc_methtype: 0x1712e
+  __TEXT.__objc_stubs: 0x4d900
+  __DATA_CONST.__got: 0x4df8
+  __DATA_CONST.__const: 0xbab8
+  __DATA_CONST.__objc_classlist: 0x2868
   __DATA_CONST.__objc_catlist: 0x468
   __DATA_CONST.__objc_protolist: 0x990
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18bc0
+  __DATA_CONST.__objc_selrefs: 0x18ca0
   __DATA_CONST.__objc_protorefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x1d70
+  __DATA_CONST.__objc_superrefs: 0x1d78
   __DATA_CONST.__objc_arraydata: 0x8708
   __AUTH_CONST.__auth_got: 0x1938
   __AUTH_CONST.__auth_ptr: 0xa0
-  __AUTH_CONST.__const: 0x20aa8
-  __AUTH_CONST.__cfstring: 0x3ba40
-  __AUTH_CONST.__objc_const: 0x82a50
+  __AUTH_CONST.__const: 0x20a68
+  __AUTH_CONST.__cfstring: 0x3bb60
+  __AUTH_CONST.__objc_const: 0x82c70
   __AUTH_CONST.__objc_arrayobj: 0x1ec0
   __AUTH_CONST.__objc_intobj: 0x4380
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x198b8
+  __AUTH.__objc_data: 0x19a00
   __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x5008
+  __DATA.__objc_ivar: 0x503c
   __DATA.__data: 0x7580
   __DATA.__bss: 0x640
   __DATA.__common: 0x24

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 33235
-  Symbols:   69164
-  CStrings:  8985
+  Functions: 33263
+  Symbols:   69229
+  CStrings:  8994
 
Symbols:
+ -[HDAnalyticsSubmissionCoordinator(Workout) workout_reportWorkoutEventWithHeartBeatFailures:workoutDuration:isFirstParty:wasBuilderAbandoned:]
+ -[HDConceptIndexManager unitTest_triggerConceptIndexing]
+ -[HDFitnessMachineStateTimer .cxx_destruct]
+ -[HDFitnessMachineStateTimer begin]
+ -[HDFitnessMachineStateTimer cancel]
+ -[HDFitnessMachineStateTimer dealloc]
+ -[HDFitnessMachineStateTimer initWithName:duration:queue:handler:]
+ -[HDFitnessMachineStateTimers .cxx_destruct]
+ -[HDFitnessMachineStateTimers beginDisconnectTimeout]
+ -[HDFitnessMachineStateTimers beginFieldDetectTimeout]
+ -[HDFitnessMachineStateTimers beginMachineIdentityVerificationTimeout]
+ -[HDFitnessMachineStateTimers beginMfaTimeout]
+ -[HDFitnessMachineStateTimers beginPauseTimeout]
+ -[HDFitnessMachineStateTimers beginRetryConnectionTimeout]
+ -[HDFitnessMachineStateTimers beginTagReadTimeout]
+ -[HDFitnessMachineStateTimers beginUserAcceptanceTimeout]
+ -[HDFitnessMachineStateTimers beginWaitForMachineStartTimeout]
+ -[HDFitnessMachineStateTimers cancelAllTimers]
+ -[HDFitnessMachineStateTimers cancelDisconnectTimeout]
+ -[HDFitnessMachineStateTimers cancelFieldDetectTimeout]
+ -[HDFitnessMachineStateTimers cancelMachineIdentityVerificationTimeout]
+ -[HDFitnessMachineStateTimers cancelMfaTimeout]
+ -[HDFitnessMachineStateTimers cancelPauseTimeout]
+ -[HDFitnessMachineStateTimers cancelRetryConnectionTimeout]
+ -[HDFitnessMachineStateTimers cancelTagReadTimeout]
+ -[HDFitnessMachineStateTimers cancelUserAcceptanceTimeout]
+ -[HDFitnessMachineStateTimers cancelWaitForMachineStartTimeout]
+ -[HDFitnessMachineStateTimers dealloc]
+ -[HDFitnessMachineStateTimers delegate]
+ -[HDFitnessMachineStateTimers initWithQueue:delegate:]
+ -[HDFitnessMachineStateTimers isDisconnectTimerValid]
+ -[HDFitnessMachineStateTimers isFieldDetectTimerValid]
+ -[HDFitnessMachineStateTimers isMachineIdentityVerificationTimerValid]
+ -[HDFitnessMachineStateTimers isMfaTimerValid]
+ -[HDFitnessMachineStateTimers isPauseTimerValid]
+ -[HDFitnessMachineStateTimers isRetryConnectionTimerValid]
+ -[HDFitnessMachineStateTimers isTagReadTimerValid]
+ -[HDFitnessMachineStateTimers isUserAcceptanceTimerValid]
+ -[HDFitnessMachineStateTimers isWaitForMachineStartTimerValid]
+ -[HDFitnessMachineStateTimers setDelegate:]
+ -[HDFitnessMachineStateTimers setDisconnectTimer:]
+ -[HDFitnessMachineStateTimers setFieldDetectTimer:]
+ -[HDFitnessMachineStateTimers setMachineIdentityVerificationTimer:]
+ -[HDFitnessMachineStateTimers setMfaTimer:]
+ -[HDFitnessMachineStateTimers setPauseTimer:]
+ -[HDFitnessMachineStateTimers setRetryConnectionTimer:]
+ -[HDFitnessMachineStateTimers setTagReadTimer:]
+ -[HDFitnessMachineStateTimers setUserAcceptanceTimer:]
+ -[HDFitnessMachineStateTimers setWaitForMachineStartTimer:]
+ -[HDMirroredWorkoutAnalyticsCollector submitHeartBeatFailuresWithCoordinator:numOfHeartbeatFailures:workoutDuration:isFirstParty:wasBuilderAbandoned:]
+ OBJC_IVAR_$_HDFeatureAvailabilityHealthDataRequirementEvaluationManager._lock_observedRequirements
+ OBJC_IVAR_$_HDFitnessMachineStateTimer._duration
+ OBJC_IVAR_$_HDFitnessMachineStateTimer._handler
+ OBJC_IVAR_$_HDFitnessMachineStateTimer._name
+ OBJC_IVAR_$_HDFitnessMachineStateTimer._queue
+ OBJC_IVAR_$_HDFitnessMachineStateTimer._timer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._delegate
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._disconnectTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._fieldDetectTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._machineIdentityVerificationTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._mfaTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._pauseTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._queue
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._retryConnectionTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._tagReadTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._userAcceptanceTimer
+ OBJC_IVAR_$_HDFitnessMachineStateTimers._waitForMachineStartTimer
+ _OBJC_CLASS_$_HDFitnessMachineStateTimer
+ _OBJC_CLASS_$_HDFitnessMachineStateTimers
+ _OBJC_METACLASS_$_HDFitnessMachineStateTimer
+ _OBJC_METACLASS_$_HDFitnessMachineStateTimers
+ __100-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForAttachmentRecordTypeInZone:error:]_block_invoke.296
+ __100-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForAttachmentRecordTypeInZone:error:]_block_invoke.300
+ __101-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForTransactionRecordTypeInZone:error:]_block_invoke.286
+ __118-[HDClientDataCollectionTaskServer _queue_insertDatums:device:metadata:options:batchUUID:registrationUUID:completion:]_block_invoke.304
+ __41-[HDProfile _notifyProfileReadyObservers]_block_invoke.321
+ __48+[HDServiceEntity allServicesWithProfile:error:]_block_invoke.326
+ __62+[HDServiceEntity insertOrUpdateService:healthDatabase:error:]_block_invoke.312
+ __62+[HDServiceEntity insertOrUpdateService:healthDatabase:error:]_block_invoke.316
+ __78-[HDDatabaseCoalescedWritePool _queue_performPendingWriteOperationsWithError:]_block_invoke.267
+ __OBJC_$_INSTANCE_METHODS_HDFitnessMachineStateTimer
+ __OBJC_$_INSTANCE_METHODS_HDFitnessMachineStateTimers
+ __OBJC_$_INSTANCE_VARIABLES_HDFitnessMachineStateTimer
+ __OBJC_$_INSTANCE_VARIABLES_HDFitnessMachineStateTimers
+ __OBJC_$_PROP_LIST_HDFitnessMachineStateTimers
+ __OBJC_CLASS_RO_$_HDFitnessMachineStateTimer
+ __OBJC_CLASS_RO_$_HDFitnessMachineStateTimers
+ __OBJC_METACLASS_RO_$_HDFitnessMachineStateTimer
+ __OBJC_METACLASS_RO_$_HDFitnessMachineStateTimers
+ ___142-[HDAnalyticsSubmissionCoordinator(Workout) workout_reportWorkoutEventWithHeartBeatFailures:workoutDuration:isFirstParty:wasBuilderAbandoned:]_block_invoke
+ ___35-[HDFitnessMachineStateTimer begin]_block_invoke
+ ___46-[HDFitnessMachineStateTimers beginMfaTimeout]_block_invoke
+ ___48-[HDFitnessMachineStateTimers beginPauseTimeout]_block_invoke
+ ___50-[HDFitnessMachineStateTimers beginTagReadTimeout]_block_invoke
+ ___53-[HDFitnessMachineStateTimers beginDisconnectTimeout]_block_invoke
+ ___54-[HDFitnessMachineStateTimers beginFieldDetectTimeout]_block_invoke
+ ___57-[HDFitnessMachineStateTimers beginUserAcceptanceTimeout]_block_invoke
+ ___58-[HDFitnessMachineStateTimers beginRetryConnectionTimeout]_block_invoke
+ ___62-[HDFitnessMachineStateTimers beginWaitForMachineStartTimeout]_block_invoke
+ ___70-[HDFitnessMachineStateTimers beginMachineIdentityVerificationTimeout]_block_invoke
+ ___block_descriptor_51_e26_"NSMutableDictionary"8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e20_B24?0"NSUUID"8^16l
+ __block_literal_global.322
+ __block_literal_global.419
+ _kHKConnectedGymPreferencesDomain
+ _kHKConnectedGymPreferencesSpartanMFATimeoutOverride
+ _objc_msgSend$cancelAllTimers
+ _objc_msgSend$cancelDisconnectTimeout
+ _objc_msgSend$cancelFieldDetectTimeout
+ _objc_msgSend$cancelMachineIdentityVerificationTimeout
+ _objc_msgSend$cancelMfaTimeout
+ _objc_msgSend$cancelPauseTimeout
+ _objc_msgSend$cancelRetryConnectionTimeout
+ _objc_msgSend$cancelTagReadTimeout
+ _objc_msgSend$cancelUserAcceptanceTimeout
+ _objc_msgSend$cancelWaitForMachineStartTimeout
+ _objc_msgSend$setCountry:
+ _objc_msgSend$stateTimersDisconnectTimeout:
+ _objc_msgSend$stateTimersFieldDetectTimeout:
+ _objc_msgSend$stateTimersMachineIdentityVerificationTimeout:
+ _objc_msgSend$stateTimersMfaTimeout:
+ _objc_msgSend$stateTimersPauseTimeout:
+ _objc_msgSend$stateTimersRetryConnectionTimeout:
+ _objc_msgSend$stateTimersTagReadTimeout:
+ _objc_msgSend$stateTimersUserAcceptanceTimeout:
+ _objc_msgSend$stateTimersWaitForMachineStartTimeout:
+ _objc_msgSend$submitHeartBeatFailuresWithCoordinator:numOfHeartbeatFailures:workoutDuration:isFirstParty:wasBuilderAbandoned:
+ _objc_msgSend$workout_reportWorkoutEventWithHeartBeatFailures:workoutDuration:isFirstParty:wasBuilderAbandoned:
- +[HDAuthorizationEntity authorizationRequestsForBundleIdentifier:types:profile:error:]
- +[HDFeatureAvailabilityHealthDataRequirementStoreServer requiredEntitlements]
- +[HDObjectTypeAnchorQueryServer queryClass]
- +[HDOntologyConceptManager predicateForConceptsWithoutAttributeType:attributeValue:]
- -[HDAnalyticsSubmissionCoordinator(Workout) workout_reportWorkoutEventWithHeartBeatFailures:workoutDuration:isFirstParty:]
- -[HDMirroredWorkoutAnalyticsCollector submitHeartBeatFailuresWithCoordinator:numOfHeartbeatFailures:workoutDuration:isFirstParty:]
- -[HDObjectTypeAnchorQueryServer .cxx_destruct]
- -[HDObjectTypeAnchorQueryServer _queue_fetchAndDeliver]
- -[HDObjectTypeAnchorQueryServer _queue_scheduleUpdate]
- -[HDObjectTypeAnchorQueryServer _queue_start]
- -[HDObjectTypeAnchorQueryServer _shouldListenForUpdates]
- -[HDObjectTypeAnchorQueryServer _shouldObserveAllSampleTypes]
- -[HDObjectTypeAnchorQueryServer database:protectedDataDidBecomeAvailable:]
- -[HDObjectTypeAnchorQueryServer didAddSamplesOfTypes:anchor:]
- -[HDObjectTypeAnchorQueryServer initWithUUID:configuration:client:delegate:]
- -[HDObjectTypeAnchorQueryServer samplesJournaled:type:]
- -[HDObjectTypeAnchorQueryServer samplesOfTypesWereRemoved:anchor:]
- -[HDProfile requirementEvaluationDataSource]
- -[HDProfile(HKFeatureAvailabilityHealthDataSource) sharedRequirementEvaluationDataSource]
- OBJC_IVAR_$_HDFeatureAvailabilityHealthDataRequirementEvaluationManager._lock_observedRequirementsByObserver
- OBJC_IVAR_$_HDProfile._requirementEvaluationDataSource
- _HDSimpleGraphDatabaseNodeEntityPredicateWithoutAttribute
- _OBJC_CLASS_$_HDObjectTypeAnchorQueryServer
- _OBJC_CLASS_$__HKObjectTypeAnchor
- _OBJC_CLASS_$__HKObjectTypeAnchorQuery
- _OBJC_METACLASS_$_HDObjectTypeAnchorQueryServer
- __100-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForAttachmentRecordTypeInZone:error:]_block_invoke.301
- __101-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForTransactionRecordTypeInZone:error:]_block_invoke.290
- __118-[HDClientDataCollectionTaskServer _queue_insertDatums:device:metadata:options:batchUUID:registrationUUID:completion:]_block_invoke.306
- __41-[HDProfile _notifyProfileReadyObservers]_block_invoke.322
- __48+[HDServiceEntity allServicesWithProfile:error:]_block_invoke.323
- __62+[HDServiceEntity insertOrUpdateService:healthDatabase:error:]_block_invoke.306
- __62+[HDServiceEntity insertOrUpdateService:healthDatabase:error:]_block_invoke.313
- __78-[HDDatabaseCoalescedWritePool _queue_performPendingWriteOperationsWithError:]_block_invoke.272
- __HKPrivateMetadataKeyWorkoutActivityUUID
- __OBJC_$_CLASS_METHODS_HDObjectTypeAnchorQueryServer
- __OBJC_$_INSTANCE_METHODS_HDObjectTypeAnchorQueryServer
- __OBJC_$_INSTANCE_VARIABLES_HDObjectTypeAnchorQueryServer
- __OBJC_CLASS_RO_$_HDObjectTypeAnchorQueryServer
- __OBJC_METACLASS_RO_$_HDObjectTypeAnchorQueryServer
- ___100-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForAttachmentRecordTypeInZone:error:]_block_invoke_3
- ___110-[HDCloudSyncPipelineStageDescribe _cloudSyncRecordDescriptionsForDeviceContextRecords:deviceKeyValueRecords:]_block_invoke
- ___122-[HDAnalyticsSubmissionCoordinator(Workout) workout_reportWorkoutEventWithHeartBeatFailures:workoutDuration:isFirstParty:]_block_invoke
- ___54-[HDObjectTypeAnchorQueryServer _queue_scheduleUpdate]_block_invoke
- ___55-[HDObjectTypeAnchorQueryServer samplesJournaled:type:]_block_invoke
- ___56-[HDObjectTypeAnchorQueryServer _fetchAnchorsWithError:]_block_invoke
- ___56-[HDObjectTypeAnchorQueryServer _fetchAnchorsWithError:]_block_invoke_2
- ___56-[HDObjectTypeAnchorQueryServer _fetchAnchorsWithError:]_block_invoke_3
- ___61-[HDObjectTypeAnchorQueryServer didAddSamplesOfTypes:anchor:]_block_invoke
- ___66-[HDObjectTypeAnchorQueryServer samplesOfTypesWereRemoved:anchor:]_block_invoke
- ___68-[HDObjectTypeAnchorQueryServer _queue_protectedDataBecameAvailable]_block_invoke
- ___block_descriptor_32_e25_16?0"HKQuantityDatum"8l
- ___block_descriptor_50_e26_"NSMutableDictionary"8?0l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e20_B24?0"NSUUID"8^16l
- _objc_msgSend$_setCountry:
- _objc_msgSend$_updateConceptIndexWithReason:
- _objc_msgSend$activityGoalScheduleType
- _objc_msgSend$client_deliverAnchor:query:
- _objc_msgSend$dataSourceWithHealthDataSource:
- _objc_msgSend$initWithAnchors:databaseIdentifier:
- _objc_msgSend$pauseRingsScheduleType
- _objc_msgSend$requirementEvaluationDataSource
- _objc_msgSend$submitHeartBeatFailuresWithCoordinator:numOfHeartbeatFailures:workoutDuration:isFirstParty:
- _objc_msgSend$timeInBedTracking
- _objc_msgSend$workout_reportWorkoutEventWithHeartBeatFailures:workoutDuration:isFirstParty:
CStrings:
+ "+ Product Type Name: %!@(MISSING)\n+ Current OS Version: %!@(MISSING)\n+ Current OS Name: %!@(MISSING)\n+ Modification date: %!@(MISSING)\n+--------------------------------------------------"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBPlusTree.hpp"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBlockAccessFile.cpp"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDTransactionalFile.cpp"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDVirtualFilesystem.cpp"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDWriteAheadLog.cpp"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDEncoder.h"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDFilePage.h"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDRawBuffer.h"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDStaticArray.h"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDTransactionalCache.hpp"
+ "Disconnect"
+ "Field Detect"
+ "MFA"
+ "Machine Identity Verification"
+ "Pause"
+ "Retry Connection"
+ "Tag Read"
+ "Unit Testing"
+ "User Acceptance"
+ "Wait for Machine Start"
+ "wasBuilderAbandoned"
- "+ Product Type Name: %!@(MISSING)\n+ Current OS Version: %!@(MISSING)\n+ Current OS Name: %!@(MISSING)\n+ Sync identity: %!@(MISSING)\n+ Modification date: %!@(MISSING)\n+--------------------------------------------------"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBPlusTree.hpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBlockAccessFile.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDTransactionalFile.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDVirtualFilesystem.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDWriteAheadLog.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDEncoder.h"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDFilePage.h"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDRawBuffer.h"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDStaticArray.h"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDTransactionalCache.hpp"
- "PendingWriteOperation"
- "SELECT %!@(MISSING), MAX(%!@(MISSING)) FROM %!@(MISSING) GROUP BY %!@(MISSING);"

```

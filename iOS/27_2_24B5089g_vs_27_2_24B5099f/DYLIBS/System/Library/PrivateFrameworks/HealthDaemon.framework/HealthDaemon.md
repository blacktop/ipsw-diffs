## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0xcf47b0
-  __TEXT.__objc_methlist: 0x4a0d4
-  __TEXT.__const: 0x73ce0
+7027.1.54.2.3
+  __TEXT.__text: 0xcf84dc
+  __TEXT.__objc_methlist: 0x4a2d4
+  __TEXT.__const: 0x73d10
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x8eb4d
+  __TEXT.__cstring: 0x8ee60
   __TEXT.__swift5_typeref: 0x4fc3
   __TEXT.__swift5_capture: 0x25c0
   __TEXT.__constg_swiftt: 0x4a00
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x3608
-  __TEXT.__swift5_fieldmd: 0x3844
+  __TEXT.__swift5_reflstr: 0x3638
+  __TEXT.__swift5_fieldmd: 0x3850
   __TEXT.__swift5_assocty: 0xb80
   __TEXT.__swift5_proto: 0x67c
   __TEXT.__swift5_types: 0x408
-  __TEXT.__oslogstring: 0x4b3ac
+  __TEXT.__oslogstring: 0x4b364
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0xe8
   __TEXT.__swift_as_entry: 0x74
   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x90
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x7b348
-  __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x366b8
-  __TEXT.__eh_frame: 0x7910
+  __TEXT.__gcc_except_tab: 0x7b380
+  __TEXT.__ustring: 0xb6
+  __TEXT.__unwind_info: 0x36820
+  __TEXT.__eh_frame: 0x7980
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e288
-  __DATA_CONST.__objc_classlist: 0x2de0
+  __DATA_CONST.__const: 0x1e300
+  __DATA_CONST.__objc_classlist: 0x2df8
   __DATA_CONST.__objc_catlist: 0x538
-  __DATA_CONST.__objc_protolist: 0xb90
+  __DATA_CONST.__objc_protolist: 0xb98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x1c470
-  __DATA_CONST.__objc_protorefs: 0x320
-  __DATA_CONST.__objc_superrefs: 0x1f00
-  __DATA_CONST.__objc_arraydata: 0x8a10
-  __DATA_CONST.__got: 0x60c8
+  __DATA_CONST.__objc_selrefs: 0x1c530
+  __DATA_CONST.__objc_protorefs: 0x328
+  __DATA_CONST.__objc_superrefs: 0x1ef8
+  __DATA_CONST.__objc_arraydata: 0x8a18
+  __DATA_CONST.__got: 0x60f0
   __AUTH_CONST.__const: 0x2a390
-  __AUTH_CONST.__cfstring: 0x41fa0
-  __AUTH_CONST.__objc_const: 0x897c0
+  __AUTH_CONST.__cfstring: 0x42200
+  __AUTH_CONST.__objc_const: 0x89f00
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x3ed0
-  __AUTH_CONST.__objc_arrayobj: 0x21c0
+  __AUTH_CONST.__objc_arrayobj: 0x21d8
   __AUTH_CONST.__objc_doubleobj: 0x3c0
-  __AUTH_CONST.__auth_got: 0x3f20
-  __AUTH.__objc_data: 0x9cd8
-  __AUTH.__data: 0x1ee0
-  __DATA.__objc_ivar: 0x48a8
-  __DATA.__data: 0x9e78
+  __AUTH_CONST.__auth_got: 0x3f58
+  __AUTH.__objc_data: 0x9e28
+  __AUTH.__data: 0x1f60
+  __DATA.__objc_ivar: 0x491c
+  __DATA.__data: 0x9f58
   __DATA.__common: 0x2d0
   __DATA_DIRTY.__objc_ivar: 0xe80
-  __DATA_DIRTY.__objc_data: 0x14b60
-  __DATA_DIRTY.__data: 0x4570
+  __DATA_DIRTY.__objc_data: 0x14b68
+  __DATA_DIRTY.__data: 0x4520
   __DATA_DIRTY.__bss: 0x2878
   __DATA_DIRTY.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 52724
-  Symbols:   80421
-  CStrings:  14765
+  Functions: 52833
+  Symbols:   80488
+  CStrings:  14796
 
Symbols:
+ +[HDDataEntity hasStaticJoinClauses]
+ +[HDMedicalRecordEntity hasStaticJoinClauses]
+ -[HDDaemon _forceExitAfterFailureToQuiesce]
+ -[HDDaemon _requestCleanExitFromXPC]
+ -[HDDataOriginProvenance effectiveSystemBuild]
+ -[HDQueryManager scheduleDatabaseAccessForQueryServer:handler:]
+ -[HDQueryServer debugIdentifier]
+ -[HDQueryUsageDailyAnalytics _addClientWaitTimingFieldsToEvent:stats:databaseAccessStats:]
+ -[HDQueryUsageDailyAnalytics _eventDictionaryForStats:databaseAccessStats:databaseSizeMB:dataCacheSizeMB:databaseShape:isIHAEnabled:]
+ -[HDQueryUsageDatabaseAccessStatistics backgroundAccessCount]
+ -[HDQueryUsageDatabaseAccessStatistics backgroundConnectionDelaySampleCount]
+ -[HDQueryUsageDatabaseAccessStatistics foregroundAccessCount]
+ -[HDQueryUsageDatabaseAccessStatistics foregroundConnectionDelaySampleCount]
+ -[HDQueryUsageDatabaseAccessStatistics maxBackgroundConnectionDelay]
+ -[HDQueryUsageDatabaseAccessStatistics maxBackgroundManagerDelay]
+ -[HDQueryUsageDatabaseAccessStatistics maxForegroundConnectionDelay]
+ -[HDQueryUsageDatabaseAccessStatistics maxForegroundManagerDelay]
+ -[HDQueryUsageDatabaseAccessStatistics recordAccessWithManagerDelay:connectionDelay:foreground:]
+ -[HDQueryUsageDatabaseAccessStatistics reset]
+ -[HDQueryUsageDatabaseAccessStatistics totalBackgroundConnectionDelay]
+ -[HDQueryUsageDatabaseAccessStatistics totalBackgroundManagerDelay]
+ -[HDQueryUsageDatabaseAccessStatistics totalForegroundConnectionDelay]
+ -[HDQueryUsageDatabaseAccessStatistics totalForegroundManagerDelay]
+ -[HDQueryUsageStatistics backgroundOneShotQueryCount]
+ -[HDQueryUsageStatistics foregroundOneShotQueryCount]
+ -[HDQueryUsageStatistics maxBackgroundOneShotQueryDuration]
+ -[HDQueryUsageStatistics maxForegroundOneShotQueryDuration]
+ -[HDQueryUsageStatistics recordOneShotQueryWithDuration:foreground:]
+ -[HDQueryUsageStatistics totalBackgroundOneShotQueryDuration]
+ -[HDQueryUsageStatistics totalForegroundOneShotQueryDuration]
+ -[HDQueryUsageTracker _lock_statisticsForQueryType:]
+ -[HDQueryUsageTracker drainStatisticsWithDatabaseAccessStatistics:]
+ -[HDQueryUsageTracker recordDatabaseAccessWithManagerDelay:connectionDelay:foreground:]
+ -[HDWorkoutSessionServer unitTest_rebuildSessionControllerFromServerConfiguration]
+ _HDQuerySanitizedDebugIdentifier
+ _HDQueryServerLifetimeSummary
+ _HDQueryServerRunSummary
+ _HKLogQueryCategory
+ _OBJC_CLASS_$_HDMutableNewMedicalRecordsTally
+ _OBJC_CLASS_$_HDNewMedicalRecordsCounts
+ _OBJC_CLASS_$_HDNewMedicalRecordsTally
+ _OBJC_CLASS_$_HDQueryUsageDatabaseAccessStatistics
+ _OBJC_IVAR_$_HDDaemon._forceExitTimerSource
+ _OBJC_IVAR_$_HDDaemon._hasRequestedCleanExit
+ _OBJC_IVAR_$_HDQueryServer._activationCount
+ _OBJC_IVAR_$_HDQueryServer._activationDelay
+ _OBJC_IVAR_$_HDQueryServer._databaseAccessDelay
+ _OBJC_IVAR_$_HDQueryServer._debugIdentifier
+ _OBJC_IVAR_$_HDQueryServer._lastExecutionDuration
+ _OBJC_IVAR_$_HDQueryServer._lastTransactionDuration
+ _OBJC_IVAR_$_HDQueryServer._pauseCount
+ _OBJC_IVAR_$_HDQueryServer._pauseStartTime
+ _OBJC_IVAR_$_HDQueryServer._pendingAccessesAtDequeue
+ _OBJC_IVAR_$_HDQueryServer._runningAccessesAtDequeue
+ _OBJC_IVAR_$_HDQueryServer._totalExecutionDuration
+ _OBJC_IVAR_$_HDQueryServer._totalPausedDuration
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._backgroundAccessCount
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._backgroundConnectionDelaySampleCount
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._foregroundAccessCount
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._foregroundConnectionDelaySampleCount
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._maxBackgroundConnectionDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._maxBackgroundManagerDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._maxForegroundConnectionDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._maxForegroundManagerDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._totalBackgroundConnectionDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._totalBackgroundManagerDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._totalForegroundConnectionDelay
+ _OBJC_IVAR_$_HDQueryUsageDatabaseAccessStatistics._totalForegroundManagerDelay
+ _OBJC_IVAR_$_HDQueryUsageStatistics._backgroundOneShotQueryCount
+ _OBJC_IVAR_$_HDQueryUsageStatistics._foregroundOneShotQueryCount
+ _OBJC_IVAR_$_HDQueryUsageStatistics._maxBackgroundOneShotQueryDuration
+ _OBJC_IVAR_$_HDQueryUsageStatistics._maxForegroundOneShotQueryDuration
+ _OBJC_IVAR_$_HDQueryUsageStatistics._totalBackgroundOneShotQueryDuration
+ _OBJC_IVAR_$_HDQueryUsageStatistics._totalForegroundOneShotQueryDuration
+ _OBJC_IVAR_$_HDQueryUsageTracker._databaseAccessStatistics
+ _OBJC_IVAR_$_HDWorkoutSessionServer._workoutConfigurationLock
+ _OBJC_IVAR_$__HDQueryDatabaseAccessBlock._handler
+ _OBJC_METACLASS_$_HDMutableNewMedicalRecordsTally
+ _OBJC_METACLASS_$_HDNewMedicalRecordsCounts
+ _OBJC_METACLASS_$_HDNewMedicalRecordsTally
+ _OBJC_METACLASS_$_HDQueryUsageDatabaseAccessStatistics
+ __CLASS_METHODS_HDMutableNewMedicalRecordsTally
+ __CLASS_METHODS_HDNewMedicalRecordsCounts
+ __CLASS_METHODS_HDNewMedicalRecordsTally
+ __CLASS_PROPERTIES_HDMutableNewMedicalRecordsTally
+ __CLASS_PROPERTIES_HDNewMedicalRecordsCounts
+ __CLASS_PROPERTIES_HDNewMedicalRecordsTally
+ __DATA_HDMutableNewMedicalRecordsTally
+ __DATA_HDNewMedicalRecordsCounts
+ __DATA_HDNewMedicalRecordsTally
+ __HDQueryUsageSetAverageAndMaximum
+ __HDReserveRecordSyncCachedRequestColumns
+ __HDResetReceivedNanoSyncAnchorsOnWatchForBodyMetrics
+ __INSTANCE_METHODS_HDMutableNewMedicalRecordsTally
+ __INSTANCE_METHODS_HDNewMedicalRecordsCounts
+ __INSTANCE_METHODS_HDNewMedicalRecordsTally
+ __IVARS_HDNewMedicalRecordsCounts
+ __IVARS_HDNewMedicalRecordsTally
+ __METACLASS_DATA_HDMutableNewMedicalRecordsTally
+ __METACLASS_DATA_HDNewMedicalRecordsCounts
+ __METACLASS_DATA_HDNewMedicalRecordsTally
+ __OBJC_$_INSTANCE_METHODS_HDQueryUsageDatabaseAccessStatistics
+ __OBJC_$_INSTANCE_VARIABLES_HDQueryUsageDatabaseAccessStatistics
+ __OBJC_$_PROP_LIST_HDQueryUsageDatabaseAccessStatistics
+ __OBJC_CLASS_RO_$_HDQueryUsageDatabaseAccessStatistics
+ __OBJC_METACLASS_RO_$_HDQueryUsageDatabaseAccessStatistics
+ __PROPERTIES_HDNewMedicalRecordsCounts
+ __PROPERTIES_HDNewMedicalRecordsTally
+ __PROTOCOLS_HDNewMedicalRecordsCounts
+ __PROTOCOLS_HDNewMedicalRecordsTally
+ ___67-[HDQueryUsageTracker drainStatisticsWithDatabaseAccessStatistics:]_block_invoke
+ ___75-[HDCloudSyncSeizeAbandonedStoresOperation _childTargetsForSyncIdentities:]_block_invoke
+ ___82-[HDWorkoutSessionServer unitTest_rebuildSessionControllerFromServerConfiguration]_block_invoke
+ ___88-[HDQueryServer _scheduleDatabaseAccessWithBlock:enqueueTime:pendingCount:runningCount:]_block_invoke
+ ___block_descriptor_56_e8_32bs40w_e11_v24?0Q8Q16lw40l8s32l8
+ ___block_descriptor_56_e8_32s_e9_B16?0^8ls32l8
+ ___block_descriptor_72_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_89_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- -[HDAnchoredObjectQueryServer _queue_didChangeStateFromPreviousState:state:]
- -[HDCodableHealthReportState .cxx_destruct]
- -[HDCodableHealthReportState copyTo:]
- -[HDCodableHealthReportState copyWithZone:]
- -[HDCodableHealthReportState description]
- -[HDCodableHealthReportState dictionaryRepresentation]
- -[HDCodableHealthReportState evaluationBuddyLastCompletedDate]
- -[HDCodableHealthReportState evaluationBuddyLastStartedDate]
- -[HDCodableHealthReportState hasEvaluationBuddyLastCompletedDate]
- -[HDCodableHealthReportState hasEvaluationBuddyLastStartedDate]
- -[HDCodableHealthReportState hasLastGeneratedReportId]
- -[HDCodableHealthReportState hasLastReportGenerationDate]
- -[HDCodableHealthReportState hash]
- -[HDCodableHealthReportState isEqual:]
- -[HDCodableHealthReportState lastGeneratedReportId]
- -[HDCodableHealthReportState lastReportGenerationDate]
- -[HDCodableHealthReportState mergeFrom:]
- -[HDCodableHealthReportState readFrom:]
- -[HDCodableHealthReportState setEvaluationBuddyLastCompletedDate:]
- -[HDCodableHealthReportState setEvaluationBuddyLastStartedDate:]
- -[HDCodableHealthReportState setHasEvaluationBuddyLastCompletedDate:]
- -[HDCodableHealthReportState setHasEvaluationBuddyLastStartedDate:]
- -[HDCodableHealthReportState setHasLastReportGenerationDate:]
- -[HDCodableHealthReportState setLastGeneratedReportId:]
- -[HDCodableHealthReportState setLastReportGenerationDate:]
- -[HDCodableHealthReportState writeTo:]
- -[HDQueryManager scheduleDatabaseAccessForQueryServer:block:]
- -[HDQueryUsageDailyAnalytics _eventDictionaryForStats:databaseSizeMB:dataCacheSizeMB:databaseShape:isIHAEnabled:]
- -[HDQueryUsageTracker drainStatistics]
- OBJC_IVAR_$_HDCodableHealthReportState._evaluationBuddyLastCompletedDate
- OBJC_IVAR_$_HDCodableHealthReportState._evaluationBuddyLastStartedDate
- OBJC_IVAR_$_HDCodableHealthReportState._has
- OBJC_IVAR_$_HDCodableHealthReportState._lastGeneratedReportId
- OBJC_IVAR_$_HDCodableHealthReportState._lastReportGenerationDate
- _HDCodableHealthReportStateReadFrom
- _OBJC_CLASS_$_HDCodableHealthReportState
- _OBJC_IVAR_$__HDQueryDatabaseAccessBlock._block
- _OBJC_METACLASS_$_HDCodableHealthReportState
- __OBJC_$_INSTANCE_METHODS_HDCodableHealthReportState
- __OBJC_$_INSTANCE_VARIABLES_HDCodableHealthReportState
- __OBJC_$_PROP_LIST_HDCodableHealthReportState
- __OBJC_CLASS_PROTOCOLS_$_HDCodableHealthReportState
- __OBJC_CLASS_RO_$_HDCodableHealthReportState
- __OBJC_METACLASS_RO_$_HDCodableHealthReportState
- ___29-[HDDaemon exitClean:reason:]_block_invoke_2
- ___38-[HDQueryUsageTracker drainStatistics]_block_invoke
- ___50-[HDQueryServer _scheduleDatabaseAccessWithBlock:]_block_invoke
- ___80-[HDCloudSyncSeizeAbandonedStoresOperation _childTargetBySyncIdentityForParent:]_block_invoke
- ___block_descriptor_73_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
- _exitClean:reason:.onceToken
- _exitClean:reason:.timerSource
CStrings:
+ " (%.3fs in database transactions)"
+ " window, which holds recent days only"
+ "%@\n%@\n%@\n%@"
+ "%@:%d"
+ "%lu activation%s, exec %.3fs total"
+ "%s wait %.3fs (sched %.3fs, queued %.3fs behind %lu/%lu), exec %.3fs"
+ "%{public}@ -> %{public}@"
+ "%{public}@ Concept not found in Ontology for \"bodySiteConceptIdentifiers\" on medical history record entity"
+ "%{public}@ Concept not found in Ontology for \"methodConceptIdentifiers\" on medical history record entity"
+ "%{public}@ Concept not found in Ontology for \"reasonConceptIdentifiers\" on medical history record entity"
+ "%{public}@: %{public}@ -> %{public}@ (+%.3fs)"
+ "%{public}@: %{public}s — %{public}@"
+ "%{public}@: finished %{public}@"
+ ", cache %ld/%ld hit/miss"
+ ", n=%lld"
+ ", paused %.3fs ×%lu"
+ "CountsByMedicalType"
+ "HealthDaemon.HDNewMedicalRecordsCounts"
+ "Posting zone change for %s: new: %s, previous: %s, last sample date: %s"
+ "UPDATE sync_anchors SET received=0, validated=0 WHERE schema = 'main' AND sync_anchors.type = 4 AND store IN (SELECT ROWID FROM sync_stores WHERE sync_stores.type=1);"
+ "[%s] Not advancing past generation %ld: a write failed this pass."
+ "[%{public}s:%{public}s] Enumerating live for padded request %{public}s (%{public}s)"
+ "[%{public}s] Merged state's size (%ld) above the limit (%ld), purge metadata and increment epoch, previous: %lld"
+ "after %.3fs — "
+ "avgClientBackgroundConnectionDelay"
+ "avgClientBackgroundManagerDelay"
+ "avgClientBackgroundOneShotQueryDuration"
+ "avgClientForegroundConnectionDelay"
+ "avgClientForegroundManagerDelay"
+ "avgClientForegroundOneShotQueryDuration"
+ "bg"
+ "by design: no profile covers this configuration"
+ "by design: reaches past the "
+ "by design: this configuration is not cacheable"
+ "countClientBackgroundAccess"
+ "countClientBackgroundOneShotQuery"
+ "countClientForegroundAccess"
+ "countClientForegroundOneShotQuery"
+ "did not run"
+ "fg"
+ "maxClientBackgroundConnectionDelay"
+ "maxClientBackgroundManagerDelay"
+ "maxClientBackgroundOneShotQueryDuration"
+ "maxClientForegroundConnectionDelay"
+ "maxClientForegroundManagerDelay"
+ "maxClientForegroundOneShotQueryDuration"
+ "no cache plan was built; see the error logged above"
+ "ran"
+ "v24@?0Q8Q16"
+ "\xf0q1a"
+ "\xf0\xf0\xf1"
- "%@\n%@\n%@"
- "%{public}@ Failed to apply concepts for \"bodySiteConceptIdentifiers\" to medical history record entity. Concept not found in Ontology"
- "%{public}@ Failed to apply concepts for \"methodConceptIdentifiers\" to medical history record entity. Concept not found in Ontology"
- "%{public}@ Failed to apply concepts for \"reasonConceptIdentifiers\" to medical history record entity. Concept not found in Ontology"
- "%{public}@: Ran in %.3fs"
- "%{public}@: Ran in %.3fs (%.3fs in database transactions)"
- "%{public}@: Total activation delay: %.3fs, database access delay: %.3fs"
- "%{public}@: changed state (%@) -> (%@)"
- "%{public}@: did deactivate"
- "Failed to apply concepts for 'bodySiteConceptIdentifiers' to medical history record entity. Concept not found in Ontology"
- "Failed to apply concepts for 'methodConceptIdentifiers' to medical history record entity. Concept not found in Ontology"
- "Failed to apply concepts for 'reasonConceptIdentifiers' to medical history record entity. Concept not found in Ontology"
- "Posting zone change for %s: current zone: %s, new duration: %s, previous duration: %s, last sample date: %s"
- "[%{public}s:%{public}s] Skipping caching for padded request %{public}s"
- "[%{public}s] Merged state's size (%ld above the limit (%ld, purge metadata and increment epoch, previous: %lld"
- "evaluationBuddyLastCompletedDate"
- "evaluationBuddyLastStartedDate"
- "lastGeneratedReportId"
- "lastReportGenerationDate"
- "\xb1!a"
```

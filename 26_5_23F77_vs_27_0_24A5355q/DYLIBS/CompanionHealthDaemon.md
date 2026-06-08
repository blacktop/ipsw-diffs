## CompanionHealthDaemon

> `/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon`

```diff

-2026.5.4.0.0
-  __TEXT.__text: 0x7508
-  __TEXT.__auth_stubs: 0x470
+2027.0.93.0.0
+  __TEXT.__text: 0x7590
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x27c
-  __TEXT.__cstring: 0x4ab
-  __TEXT.__oslogstring: 0xc42
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__objc_classname: 0x1ca
-  __TEXT.__objc_methname: 0x1ae2
-  __TEXT.__objc_methtype: 0x489
-  __TEXT.__objc_stubs: 0x1900
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x278
+  __TEXT.__cstring: 0x4d1
+  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__oslogstring: 0xcba
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b8
+  __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__objc_const: 0x1bb0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x360

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 294636C3-FC0B-399F-8AB8-FCDFF18D4191
-  Functions: 133
-  Symbols:   820
-  CStrings:  489
+  UUID: 5FF07DB0-4750-34C7-8D4A-074145E314D7
+  Functions: 144
+  Symbols:   859
+  CStrings:  145
 
Symbols:
+ GCC_except_table1
+ GCC_except_table3
+ _CHActivitySummaryAnalyticsHasCompletedWorkoutWithProfile
+ _CHActivitySummaryAnalyticsHasCompletedWorkoutWithProfile.cold.1
+ _CHActivitySummaryAnalyticsHasCompletedWorkoutWithProfile.cold.2
+ _CHActivitySummaryAnalyticsNumberOfRingsCompletedWithProfile
+ _CHActivitySummaryAnalyticsNumberOfRingsCompletedWithProfile.cold.1
+ _CHActivitySummaryAnalyticsNumberOfRingsCompletedWithProfile.cold.2
+ _CHActivitySummaryAnalyticsPayloadForProfileAndSummaryCacheIndex
+ _CHActivitySummaryAnalyticsPayloadForProfileAndSummaryCacheIndex.cold.1
+ _CHActivitySummaryAnalyticsPayloadForProfileAndSummaryCacheIndex.cold.2
+ _CHActivitySummaryForSummaryIndex
+ _FIActivitySummaryAnalyticsPayloadForActivitySummary
+ _FIActivitySummaryNumberOfRingsCompletedError
+ _FIActivitySummaryNumberOfRingsCompletedForActivitySummary
+ _HDActivityCacheEntityPredicateForCacheIndex
+ __HKActivityCacheDateComponentsFromCacheIndex
+ ___56-[CHTrendsNotificationManager sendNotificationIfAllowed]_block_invoke.383
+ ___67-[CHCompanionWorkoutCreditManager _queue_performWorkoutCreditFixup]_block_invoke.394
+ ___CHActivitySummaryAnalyticsHasCompletedWorkoutWithProfile_block_invoke
+ ___CHActivitySummaryForSummaryIndex_block_invoke
+ ___block_descriptor_40_e8_32r_e25_B32?0"HKObject"8q16^24lr32l8
+ ___block_descriptor_48_e8_32r_e31_v24?0"HKActivitySummary"8^B16lr32l8
+ __os_log_debug_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$entityEnumeratorWithProfile:
+ _objc_msgSend$enumerateWithError:handler:
+ _objc_msgSend$hk_dateByAddingDays:toDate:
+ _objc_msgSend$hk_isDatabaseAccessibilityError
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$predicateWithProperty:lessThanValue:
+ _objc_msgSend$setLimitCount:
+ _objc_msgSend$setPredicate:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
- _FIActivitySummaryAnalyticsHasCompletedWorkoutWithProfile
- _FIActivitySummaryAnalyticsPayloadForProfileAndSummaryCacheIndex
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___56-[CHTrendsNotificationManager sendNotificationIfAllowed]_block_invoke.362
- ___67-[CHCompanionWorkoutCreditManager _queue_performWorkoutCreditFixup]_block_invoke.373
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "B32@?0@\"HKObject\"8q16^@24"
+ "Error fetching activity summary: %{public}@"
+ "Error fetching workouts: %{public}@"
+ "No activity summary found for yesterday"
- "#16@0:8"
- ".cxx_destruct"
- "@\"ASDSystemAppRequest\""
- "@\"HDDatabaseAvailabilityCondition\""
- "@\"HDKeyValueDomain\""
- "@\"HDProfile\""
- "@\"HDRepeatingBackgroundTask\""
- "@\"NSCalendar\""
- "@\"NSDate\""
- "@\"NSDateInterval\""
- "@\"NSHashTable\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"UNUserNotificationCenter\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16q24"
- "@32@0:8^@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B64@0:8@16@24@32@40@48@56"
- "CHActivityApplicationInstallationManager"
- "CHCoachingDiagnosticManager"
- "CHCompanionHealthProfileExtending"
- "CHCompanionWidgetSchedulingManager"
- "CHCompanionWorkoutCreditManager"
- "CHCompanionWorkoutCreditManagerInterval"
- "CHFitnessAppBadgeManager"
- "CHTrendsNotificationManager"
- "HDAssociationObserver"
- "HDDataObserver"
- "HDDatabaseProtectedDataObserver"
- "HDDiagnosticObject"
- "HDNanoSyncManagerObserver"
- "HDProfileReadyObserver"
- "HDUserCharacteristicsProfileObserver"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"HDKeyValueDomain\",&,N,V_keyValueDomain"
- "T@\"HDProfile\",W,N,V_profile"
- "T@\"NSDateInterval\",R,N,V_dateInterval"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UNUserNotificationCenter\",&,N,V_userNotificationCenter"
- "TQ,R"
- "Tq,R,N,V_activityMoveMode"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activityMoveMode"
- "_activitySummaryIndex"
- "_anchor"
- "_applicationsInstalled:"
- "_applicationsUninstalled:"
- "_badgeCount"
- "_cachedLastSubmittedDate"
- "_calendar"
- "_cleanupInstallRequest"
- "_currentWheelchairUse"
- "_databaseAvailableCondition"
- "_dateInterval"
- "_donateRelevance"
- "_hasPairedWatches"
- "_installationRequestInProgress"
- "_keyValueDomain"
- "_lastRingCompletionSubmittedIndex"
- "_lastRunDate"
- "_launchFitnessApp"
- "_loadBadgeCount"
- "_profile"
- "_providers"
- "_queue"
- "_queue_cleanupInstallRequest"
- "_queue_fastForwardAnchor"
- "_queue_generateAndSaveSamplesForIntervals:withExerciseMinuteTable:standHourTable:standMinuteTable:moveMinuteTable:error:"
- "_queue_lastRingCompletionSubmittedIndex"
- "_queue_lastSubmittedDate"
- "_queue_performRingCompletionDiagnostics"
- "_queue_performWorkoutCreditFixup"
- "_queue_processWorkouts"
- "_queue_requestActivityAppInstallIfNecessaryWithPairedDeviceSnapshot:"
- "_queue_samplesForType:fromStartTime:toEndTime:"
- "_queue_setLastRingCompletionSubmittedIndex:"
- "_queue_setLastSubmittedDate:"
- "_queue_setWorkoutAnchor:"
- "_queue_startInstalling"
- "_queue_userLocalProtectedDomain"
- "_queue_workoutAnchor"
- "_queue_workoutsSinceAnchor:error:"
- "_reloadWidgetTimelines"
- "_repeatingBackgroundTask"
- "_requestActivityAppInstallIfNecessaryWithPairedDeviceSnapshot:"
- "_serialQueue"
- "_setAndNotifyStickersAvailable:"
- "_standalonePhoneFitnessModeChangeToken"
- "_startObservingEffort"
- "_startObservingStandalonePhoneFitnessMode"
- "_startObservingUserCharacteristics"
- "_startObservingWorkouts"
- "_stopObservingEffort"
- "_stopObservingStandalonePhoneFitnessMode"
- "_stopObservingUserCharacteristics"
- "_stopObservingWorkouts"
- "_storeBadgeCount:"
- "_systemAppRequest"
- "_userNotificationCenter"
- "_wheelchairUse"
- "activityMoveMode"
- "addAccessibilityAssertion:"
- "addNotificationRequest:withCompletionHandler:"
- "addObject:"
- "addObserver:"
- "addObserver:forDataType:"
- "addObserver:selector:name:object:"
- "addProfileObserver:"
- "addProtectedDataObserver:"
- "allDeviceInfos"
- "appendFormat:"
- "applicationIsInstalled:"
- "arrayWithObjects:count:"
- "associatedObjectsDeletedForParentTypeMap:"
- "associationManager"
- "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
- "autorelease"
- "autoupdatingCurrentCalendar"
- "badgeCount"
- "boolForKey:"
- "boolValue"
- "briskMinuteDataType"
- "bundleForClass:"
- "calendarWithIdentifier:"
- "categorySampleWithType:value:startDate:endDate:"
- "categoryTypeForIdentifier:"
- "characteristicTypeForIdentifier:"
- "class"
- "compare:"
- "components:fromDate:"
- "components:fromDate:toDate:options:"
- "compoundPredicateWithPredicate:otherPredicate:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "dataManager"
- "dataProvenanceManager"
- "database"
- "database:protectedDataDidBecomeAvailable:"
- "database:protectedDataDidBecomeAvailable:dueToLockout:"
- "date"
- "dateByAddingTimeInterval:"
- "dateByAddingUnit:value:toDate:options:"
- "dateForKey:domain:category:profile:entity:error:"
- "dateInterval"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultLocalDataProvenance"
- "defaultStore"
- "defaultWorkspace"
- "description"
- "diagnosticDescription"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didAddSamplesOfTypes:anchor:"
- "endDate"
- "enumerateActivitySummariesWithPredicate:error:handler:"
- "enumerateObjectsUsingBlock:"
- "firstObject"
- "getActivePairedDevice"
- "getRequest"
- "hash"
- "hk_gregorianCalendar"
- "hk_gregorianCalendarWithUTCTimeZone"
- "hour"
- "i"
- "init"
- "initWithBundleID:"
- "initWithBundleIdentifier:"
- "initWithCategory:domainName:profile:"
- "initWithDatabase:loggingCategory:"
- "initWithDateInterval:activityMoveMode:"
- "initWithExtensionBundleIdentifier:kind:"
- "initWithIdentifier:"
- "initWithName:loggingCategory:scheduler:handler:condition:"
- "initWithProfile:"
- "initWithStartDate:endDate:"
- "initWithString:"
- "insertDataObjects:withProvenance:creationDate:error:"
- "integerForKey:"
- "integerValue"
- "invalidate"
- "isConditionMet"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProtectedDataAvailable"
- "isProxy"
- "isStandalonePhoneFitnessMode"
- "keyValueDomain"
- "localizedStringForKey:value:table:"
- "longLongValue"
- "minuteUnit"
- "nanoSyncManager"
- "nanoSyncManager:pairedDevicesChanged:"
- "notificationDelayNumberOfMinutes"
- "notificationDidSendSuccessfully"
- "now"
- "numberForKey:domain:category:profile:entity:error:"
- "numberForKey:error:"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openApplication:withOptions:completion:"
- "optionsWithDictionary:"
- "pairedDevicesSnapshot"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWhenDataProtectedByFirstUnlockIsAvailable:"
- "performWithTransactionContext:error:block:"
- "performWorkoutCreditFixup"
- "performWriteTransactionWithHealthDatabase:error:block:"
- "predicateMatchingAllPredicates:"
- "predicateMatchingAnyPredicates:"
- "predicateWithProperty:greaterThanOrEqualToValue:"
- "predicateWithProperty:lessThanOrEqualToValue:"
- "profile"
- "profileDidBecomeReady:"
- "profileExtensionsConformingToProtocol:"
- "protectedDataBecameAvailable"
- "q"
- "q16@0:8"
- "quantitySampleWithType:quantity:startDate:endDate:"
- "quantityTypeForIdentifier:"
- "quantityWithUnit:doubleValue:"
- "registerFitnessAppBadgeCountProvider:"
- "registerProfileReadyObserver:queue:"
- "registerProvider:"
- "release"
- "reloadTimelineWithReason:"
- "removeObject:"
- "removeObserver:"
- "removeObserver:forDataType:"
- "removeProfileObserver:"
- "removeProtectedDataObserver:"
- "requestBadgeUpdate"
- "requestFitnessAppBadgeCountUpdate"
- "requestWithIdentifier:content:trigger:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "samplesAdded:anchor:"
- "samplesJournaled:type:"
- "samplesMapWereRemoved:anchor:"
- "samplesOfTypesWereRemoved:anchor:"
- "samplesWithType:profile:encodingOptions:predicate:limit:anchor:error:"
- "second"
- "self"
- "sendNotificationIfAllowed"
- "sendNotificationWithCompletion:"
- "serviceWithDefaultShellEndpoint"
- "setBody:"
- "setBool:forKey:"
- "setDate:forKey:domain:category:profile:error:"
- "setDay:"
- "setInterval:"
- "setKeyValueDomain:"
- "setLimit:"
- "setMonth:"
- "setNumber:forKey:domain:category:profile:error:"
- "setNumber:forKey:error:"
- "setObject:forKey:"
- "setOrderByDateAscending:"
- "setPriority:"
- "setProfile:"
- "setRelevanceProviders:"
- "setRelevantShortcuts:completionHandler:"
- "setRequiresExternalPower:"
- "setRequiresProtectionClass:"
- "setShouldIncludePrivateProperties:"
- "setShouldIncludeStatistics:"
- "setSubtitle:"
- "setTitle:"
- "setUserNotificationCenter:"
- "setWidgetKind:"
- "setYear:"
- "sharedBehavior"
- "sharedDiagnosticManager"
- "sharedInstance"
- "standardUserDefaults"
- "startDate"
- "startOfDayForDate:"
- "startWithErrorHandler:"
- "stopObservingWorkouts"
- "submitRequest:error:"
- "superclass"
- "synchronize"
- "takeAccessibilityAssertionWithOwnerIdentifier:timeout:error:"
- "timeIntervalSinceReferenceDate"
- "triggerWithDateMatchingComponents:repeats:"
- "type"
- "unregisterFitnessAppBadgeCountProvider:"
- "unregisterProvider:"
- "userCharacteristicForType:error:"
- "userCharacteristicsManager"
- "userCharacteristicsManager:didUpdateUserProfile:"
- "userInfo"
- "userNotificationCenter"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<CHFitnessAppBadgeCountProvider>\"16"
- "v24@0:8@\"HDProfile\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v28@0:8@\"<HDHealthDatabase>\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"<HDHealthDatabase>\"16B24B28"
- "v32@0:8@\"HDNanoSyncManager\"16@\"HKNanoSyncPairedDevicesSnapshot\"24"
- "v32@0:8@\"HDUserCharacteristicsManager\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSArray\"16@\"HKSampleType\"24"
- "v32@0:8@\"NSArray\"16@\"NSNumber\"24"
- "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "v32@0:8@\"NSSet\"16@\"NSNumber\"24"
- "v32@0:8@16@24"
- "v32@0:8@16B24B28"
- "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
- "v64@0:8@16@24Q32Q40@48@56"
- "weakObjectsHashTable"
- "workoutEvents"
- "workoutType"
- "zone"

```

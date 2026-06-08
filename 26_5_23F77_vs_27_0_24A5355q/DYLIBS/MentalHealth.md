## MentalHealth

> `/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0xf9dc
-  __TEXT.__auth_stubs: 0x810
+7027.0.52.2.6
+  __TEXT.__text: 0xed00
   __TEXT.__objc_methlist: 0xff4
   __TEXT.__const: 0x92c
-  __TEXT.__cstring: 0xab6
+  __TEXT.__cstring: 0xac6
   __TEXT.__oslogstring: 0x5d3
-  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__gcc_except_tab: 0x68
   __TEXT.__swift5_typeref: 0x114
   __TEXT.__swift5_reflstr: 0x1a0
   __TEXT.__swift5_assocty: 0xd8

   __TEXT.__swift5_types: 0x34
   __TEXT.__unwind_info: 0x5e0
   __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0x378
-  __TEXT.__objc_methname: 0x1e38
-  __TEXT.__objc_methtype: 0x547
-  __TEXT.__objc_stubs: 0x1320
-  __DATA_CONST.__got: 0x248
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x408
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x248
   __AUTH_CONST.__const: 0x3a8
   __AUTH_CONST.__cfstring: 0x900
   __AUTH_CONST.__objc_const: 0x1da0
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x480
   __AUTH.__data: 0x230
   __DATA.__objc_ivar: 0xf4
-  __DATA.__data: 0x700
+  __DATA.__data: 0x6f8
   __DATA.__bss: 0xe90
   __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AEB625DB-4B62-3B85-8F38-DE37F8BC0EA3
-  Functions: 529
-  Symbols:   1348
-  CStrings:  611
+  UUID: CACC9EAF-1547-373C-BD9F-21B8EA7553A9
+  Functions: 525
+  Symbols:   1355
+  CStrings:  183
 
Symbols:
+ ___118-[HKMHValenceDistributionSummaryQuery client_deliverValenceDistributionSummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.362
+ ___53-[HKMHPromptedAssessmentsManager unregisterObserver:]_block_invoke.373
+ ___66-[HKMHValenceSummaryQuery client_deliverValenceSummary:queryUUID:]_block_invoke.361
+ ___75-[HKMHPromptedAssessmentsManager registerObserver:queue:activationHandler:]_block_invoke.370
+ ___78-[HKMHMostPrevalentDomainsQuery client_deliverMostPrevalentDomains:queryUUID:]_block_invoke.361
+ ___86-[HKMHDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.361
+ ___block_literal_global.363
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x24
+ _swift_retain_x20
+ _swift_retain_x28
- _OUTLINED_FUNCTION_6
- ___118-[HKMHValenceDistributionSummaryQuery client_deliverValenceDistributionSummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.341
- ___53-[HKMHPromptedAssessmentsManager unregisterObserver:]_block_invoke.352
- ___66-[HKMHValenceSummaryQuery client_deliverValenceSummary:queryUUID:]_block_invoke.340
- ___75-[HKMHPromptedAssessmentsManager registerObserver:queue:activationHandler:]_block_invoke.349
- ___78-[HKMHMostPrevalentDomainsQuery client_deliverMostPrevalentDomains:queryUUID:]_block_invoke.340
- ___86-[HKMHDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.340
- ___block_literal_global.342
- _objc_retain_x25
- _swift_retain
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"HKMHDomainSummary\""
- "@\"HKObserverSet\""
- "@\"HKStateOfMind\""
- "@\"HKTaskServerProxyProvider\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8^@16"
- "@\"NSCalendar\""
- "@\"NSDate\""
- "@\"NSDateComponents\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@\"NSXPCInterface\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8{?=qq}16"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24q32"
- "@40@0:8q16@24@32"
- "@40@0:8{?=qq}16@32"
- "@48@0:8@16@24{?=qq}32"
- "@48@0:8d16d24q32q40"
- "@56@0:8q16q24q32{?=qq}40"
- "@56@0:8{?=qq}16@32@40@?48"
- "@60@0:8{?=qq}16@32B40q44@?52"
- "@76@0:8{?=qq}16@32@40Q48B56q60@?68"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "HKMHCountBasedQueryConfiguration"
- "HKMHDaySummary"
- "HKMHDaySummaryQuery"
- "HKMHDaySummaryQueryClientInterface"
- "HKMHDaySummaryQueryConfiguration"
- "HKMHDomainSummary"
- "HKMHMostPrevalentDomains"
- "HKMHMostPrevalentDomainsQuery"
- "HKMHMostPrevalentDomainsQueryClientInterface"
- "HKMHNotification"
- "HKMHPromptedAssessment"
- "HKMHPromptedAssessmentsManagerClient"
- "HKMHPromptedAssessmentsManagerServer"
- "HKMHPromptedAssessmentsProviding"
- "HKMHReminder"
- "HKMHSettingsManager"
- "HKMHValenceDistributionData"
- "HKMHValenceDistributionSummary"
- "HKMHValenceDistributionSummaryQuery"
- "HKMHValenceDistributionSummaryQueryClientInterface"
- "HKMHValenceDistributionSummaryQueryConfiguration"
- "HKMHValenceSummary"
- "HKMHValenceSummaryQuery"
- "HKMHValenceSummaryQueryClientInterface"
- "HKMentalHealth"
- "HKQueryClientInterface"
- "HKRedactedDescription"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"HKMHDomainSummary\",R,N,V_mostPleasantDomains"
- "T@\"HKMHDomainSummary\",R,N,V_mostUnpleasantDomains"
- "T@\"HKStateOfMind\",C,N,V_dailyStateOfMind"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",R,C,N,V_momentaryStatesOfMind"
- "T@\"NSArray\",R,N,V_domains"
- "T@\"NSArray\",R,N,V_valenceDistributions"
- "T@\"NSCalendar\",&,N,V_gregorianCalendar"
- "T@\"NSCalendar\",R,N,V_gregorianCalendar"
- "T@\"NSDate\",R,C,N,V_eligibilityStartDate"
- "T@\"NSDateComponents\",R,C,N,V_dateComponents"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_category"
- "T@\"NSUserDefaults\",R,N"
- "T@\"NSUserDefaults\",R,N,V_userDefaults"
- "TB,N"
- "TB,N,V_ascending"
- "TB,R"
- "TB,R,N,V_ascending"
- "TB,R,N,V_isEnabled"
- "TQ,N,V_options"
- "TQ,R"
- "TQ,R,N,V_options"
- "Td,R,N,V_maximumValence"
- "Td,R,N,V_minimumValence"
- "Tq,N,V_countNeutral"
- "Tq,N,V_countPleasant"
- "Tq,N,V_countUnpleasant"
- "Tq,N,V_limit"
- "Tq,R,N"
- "Tq,R,N,V_count"
- "Tq,R,N,V_countDaily"
- "Tq,R,N,V_countMomentary"
- "Tq,R,N,V_dayIndex"
- "Tq,R,N,V_limit"
- "Tq,R,N,V_reason"
- "Tq,R,N,V_reflectiveInterval"
- "Tq,R,N,V_sampleCount"
- "Tq,R,N,V_totalSampleCount"
- "T{?=qq},N,V_dayIndexRange"
- "T{?=qq},R,N,V_dayIndexRange"
- "URLWithString:"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_HKXPCExportable"
- "_addValence:"
- "_allSettingsToObserve"
- "_ascending"
- "_category"
- "_contentForCategoryIdentifier:"
- "_count"
- "_countDaily"
- "_countMomentary"
- "_countNeutral"
- "_countPleasant"
- "_countUnpleasant"
- "_dailyStateOfMind"
- "_dateComponents"
- "_dayIndex"
- "_dayIndexRange"
- "_domains"
- "_eligibilityStartDate"
- "_gregorianCalendar"
- "_handleAutomaticProxyReconnection"
- "_initWithObjectType:predicate:"
- "_isEnabled"
- "_limit"
- "_maximumValence"
- "_minimumValence"
- "_momentaryStatesOfMind"
- "_mostPleasantDomains"
- "_mostUnpleasantDomains"
- "_notificationRequestIdentifierForCategoryIdentifier:date:"
- "_notificationSettingsDidUpdate"
- "_notifyObserversForPromptedAssessmentUpdate"
- "_observers"
- "_options"
- "_proxyProvider"
- "_reason"
- "_reflectiveInterval"
- "_resultsHandler"
- "_sampleCount"
- "_setTestDefaults:"
- "_startObservingDefaults"
- "_startObservingWithActivationHandler:"
- "_stopObservingAllDefaults"
- "_stringForEventDate:"
- "_summariesPendingDelivery"
- "_synchronouslyStartObservingWithError:"
- "_totalSampleCount"
- "_userDefaults"
- "_valenceDistributions"
- "addObjectsFromArray:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:queue:"
- "addValenceDistribution:"
- "allNotificationCategories"
- "allocWithZone:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "ascending"
- "assessmentsNotificationCategories"
- "autorelease"
- "boolForKey:"
- "bundleForClass:"
- "category"
- "class"
- "clientInterfaceProtocol"
- "clientQueue"
- "clientQueueActionHandlerWithCompletion:"
- "client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:"
- "client_deliverError:forQuery:"
- "client_deliverMostPrevalentDomains:queryUUID:"
- "client_deliverValenceDistributionSummaries:clearPending:isFinalBatch:queryUUID:"
- "client_deliverValenceSummary:queryUUID:"
- "client_promptedAssessmentsManagerDidUpdatePromptedAssessments"
- "configurationClass"
- "configureClientInterface:"
- "conformsToProtocol:"
- "connectionConfigured"
- "connectionInterrupted"
- "connectionInvalidated"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countDaily"
- "countMomentary"
- "countNeutral"
- "countPleasant"
- "countUnpleasant"
- "currentHandler"
- "customReminderSchedule"
- "d"
- "d16@0:8"
- "dailyStateOfMind"
- "dataForKey:"
- "dateComponents"
- "dayIndex"
- "dayIndexRange"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultSound"
- "description"
- "domains"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endOfDayNotificationsEnabled"
- "exportedInterface"
- "fetchProxyWithHandler:errorHandler:"
- "firstObject"
- "getSynchronousProxyWithHandler:errorHandler:"
- "gregorianCalendar"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasAnyAssessmentNotificationsEnabled"
- "hasAnyMentalHealthNotificationsEnabled"
- "hasAnyStateOfMindReminderEnabled"
- "hasEverEnabledAStateOfMindReminderNotification"
- "hash"
- "hk_dateOnDayIndex:atHour:calendar:"
- "hk_error:description:"
- "hk_firstObjectPassingTest:"
- "hk_redactedDescription"
- "hk_setArrayOfClass:forSelector:argumentIndex:ofReply:"
- "hk_sumUsingEvaluationBlock:"
- "hk_typesForArrayOf:"
- "hkmh_mentalHealthDefaults"
- "hkmh_mentalHealthSyncedDefaultsDomainWithHealthStore:"
- "hkmh_requestForCategoryIdentifier:date:"
- "init"
- "initWithCategory:"
- "initWithCategory:domainName:healthStore:"
- "initWithCoder:"
- "initWithCountPleasant:countNeutral:countUnpleasant:dayIndexRange:"
- "initWithDateComponents:isEnabled:"
- "initWithDayIndex:momentaryStatesOfMind:dailyStateOfMind:"
- "initWithDayIndexRange:"
- "initWithDayIndexRange:gregorianCalendar:ascending:limit:resultsHandler:"
- "initWithDayIndexRange:gregorianCalendar:predicate:options:ascending:limit:resultsHandler:"
- "initWithDayIndexRange:gregorianCalendar:predicate:resultsHandler:"
- "initWithDayIndexRange:valenceDistributions:"
- "initWithDomains:count:totalSampleCount:"
- "initWithEligibilityStartDate:reason:"
- "initWithHealthStore:"
- "initWithHealthStore:taskIdentifier:exportedObject:taskUUID:"
- "initWithMinimumValence:maximumValence:sampleCount:reflectiveInterval:"
- "initWithMostUnpleasantDomains:mostPleasantDomains:dayIndexRange:"
- "initWithName:loggingCategory:"
- "initWithSuiteName:"
- "initWithUserDefaults:"
- "interfaceWithProtocol:"
- "isAppleInternalInstall"
- "isEnabled"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToDate:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "limit"
- "localeWithLocaleIdentifier:"
- "localizedStringForKey:value:table:"
- "localizedUserNotificationStringForKey:arguments:"
- "maximumValence"
- "middayNotificationsEnabled"
- "minimumValence"
- "momentaryStatesOfMind"
- "mostPleasantDomains"
- "mostUnpleasantDomains"
- "mutableCopy"
- "notificationCategoryForString:"
- "notifyObservers:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "onboardToPregnancyRecommendedSettings"
- "options"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "periodicPromptedAssessmentNotificationTimeOfDay"
- "periodicPromptedAssessmentNotificationsEnabled"
- "promptedAssessmentsProvidingDidUpdatePromptedAssessments:"
- "promptedAssessmentsWithError:"
- "q16@0:8"
- "queue"
- "queue_deliverError:"
- "queue_dispatchToClientForUUID:shouldDeactivate:block:"
- "queue_populateConfiguration:"
- "queue_queryDidDeactivate:"
- "queue_validate"
- "raise:format:"
- "reflectiveInterval"
- "registerObserver:queue:"
- "registerObserver:queue:activationHandler:"
- "registerObserver:queue:runIfFirstObserver:"
- "release"
- "remoteInterface"
- "remote_getPromptedAssessmentsWithCompletion:"
- "remote_startObservingChangesWithCompletion:"
- "remote_stopObservingChanges"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "requestWithIdentifier:content:trigger:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sampleCount"
- "self"
- "setAscending:"
- "setAutomaticProxyReconnectionHandler:"
- "setBody:"
- "setBool:forKey:"
- "setCategoryIdentifier:"
- "setCountNeutral:"
- "setCountPleasant:"
- "setCountUnpleasant:"
- "setCustomReminderSchedule:"
- "setDailyStateOfMind:"
- "setDateFormat:"
- "setDayIndexRange:"
- "setEndOfDayNotificationsEnabled:"
- "setGregorianCalendar:"
- "setHour:"
- "setLimit:"
- "setLocale:"
- "setMiddayNotificationsEnabled:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setPeriodicPromptedAssessmentNotificationTimeOfDay:"
- "setPeriodicPromptedAssessmentNotificationsEnabled:"
- "setReminders:"
- "setShouldRetryOnInterruption:"
- "setSound:"
- "setTaskConfiguration:"
- "setTimeZone:"
- "setTitle:"
- "setUserInfo:"
- "setWithArray:"
- "setWithObject:"
- "settingsManagerDidUpdateNotificationSettings:"
- "sharedBehavior"
- "stateOfMindNotificationCategories"
- "stateOfMindType"
- "stringByAppendingFormat:"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "taskIdentifier"
- "timeIntervalSinceReferenceDate"
- "timeZoneForSecondsFromGMT:"
- "totalCount"
- "totalSampleCount"
- "unarchivedArrayOfObjectsOfClass:fromData:error:"
- "unarchivedObjectOfClass:fromData:error:"
- "unregisterObserver:"
- "unregisterObserver:runIfLastObserver:"
- "userDefaults"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<HKMHPromptedAssessmentsProvidingObserver>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"<HKMHPromptedAssessmentsProvidingObserver>\"16@\"NSObject<OS_dispatch_queue>\"24"
- "v32@0:8@\"HKMHMostPrevalentDomains\"16@\"NSUUID\"24"
- "v32@0:8@\"HKMHValenceSummary\"16@\"NSUUID\"24"
- "v32@0:8@\"NSError\"16@\"NSUUID\"24"
- "v32@0:8@16@24"
- "v32@0:8{?=qq}16"
- "v40@0:8@\"NSArray\"16B24B28@\"NSUUID\"32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16B24B28@32"
- "v48@0:8@16@24@32^v40"
- "valenceDistributions"
- "zone"
- "{?=\"start\"q\"duration\"q}"
- "{?=qq}16@0:8"

```

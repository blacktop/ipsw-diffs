## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-202.0.2.0.0
-  __TEXT.__text: 0x6680c
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_stubs: 0xa9a0
-  __TEXT.__objc_methlist: 0x694c
-  __TEXT.__objc_classname: 0x827
-  __TEXT.__objc_methtype: 0xf8b
-  __TEXT.__cstring: 0xb2de
-  __TEXT.__objc_methname: 0x114d9
+202.0.5.0.0
+  __TEXT.__text: 0x67ed8
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_stubs: 0xab00
+  __TEXT.__objc_methlist: 0x6a14
+  __TEXT.__objc_classname: 0x825
+  __TEXT.__objc_methtype: 0xfa1
+  __TEXT.__cstring: 0xb56b
+  __TEXT.__objc_methname: 0x117f7
   __TEXT.__const: 0x470
-  __TEXT.__gcc_except_tab: 0xbc0
-  __TEXT.__oslogstring: 0x6a6c
+  __TEXT.__gcc_except_tab: 0xbd0
+  __TEXT.__oslogstring: 0x6b39
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1128
-  __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0x518
+  __TEXT.__unwind_info: 0x1158
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x528
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2d70
-  __DATA_CONST.__cfstring: 0xe4c0
+  __DATA_CONST.__const: 0x2e58
+  __DATA_CONST.__cfstring: 0xe960
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x220
-  __DATA_CONST.__objc_intobj: 0xa68
-  __DATA_CONST.__objc_arraydata: 0x828
-  __DATA_CONST.__objc_arrayobj: 0x8a0
+  __DATA_CONST.__objc_intobj: 0xc00
+  __DATA_CONST.__objc_arraydata: 0x8b0
+  __DATA_CONST.__objc_arrayobj: 0xa38
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xbb60
-  __DATA.__objc_selrefs: 0x3628
-  __DATA.__objc_ivar: 0x8fc
+  __DATA.__objc_const: 0xbc50
+  __DATA.__objc_selrefs: 0x36b0
+  __DATA.__objc_ivar: 0x910
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0
   __DATA.__bss: 0x40

   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/Moments.framework/Moments
+  - /System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence
   - /System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/Trial.framework/Trial

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2443
-  Symbols:   18550
-  CStrings:  5435
+  Functions: 2463
+  Symbols:   18709
+  CStrings:  5502
 
Symbols:
+ _objc_msgSend$fetchGenerativeModelsAvailabilityWithReply:
+ -[MOContextAnalyticsManager setAssertionError:]
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.133.cold.1
+ _kMOTimeContextEmbeddingWeekOfYear
+ -[MOContextAnalyticsManager sendAssertionAnalyticsEvent]
+ __block_literal_global.141
+ _kMOContextDBAssertionErrorType
+ -[MOContextManager promptManager]
+ ___block_descriptor_32_e8_v12?0B8l
+ _objc_msgSend$sendAssertionAnalyticsEvent
+ _kMOContextTimeSinceAssertionTaskRegistration
+ GCC_except_table31
+ -[MOContextManager initWithClientID:].cold.1
+ -[MOContextAnalyticsManager getAnalyticsPlistFileURLWithFileName:].cold.1
+ _kMOContextLastDBAssertionStatus
+ _kMOContextLastAssertionTaskRegistration
+ _kMOContextTimeSinceLastDBAssertionFailure
+ -[PersonalizedSensingService dealloc]
+ ___55-[MOContextManager requestBackgroundProcessAccessForDB]_block_invoke
+ __block_literal_global.1482
+ _kCFAbsoluteTimeIntervalSince1970
+ -[MOContextAnalyticsManager initWithAssertionErrorState:dbAvailability:]
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.136
+ +[MOEventBundle getSuperTypeEnum:]
+ -[MOClusterMetadata initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:]
+ __block_literal_global.132
+ _objc_msgSend$assertionError
+ _kMOContextLastDBAssertionSuccessTime
+ _kMOContextDBAvailable
+ _objc_msgSend$acquireBackgroundProcessingPermissionsForMomentsWithHander:
+ GCC_except_table16
+ _kMOContextLastDBAssertionFailureTime
+ OBJC_IVAR_$_MOContextAnalyticsManager._isContextDBAvailable
+ ___56-[MOContextAnalyticsManager sendAssertionAnalyticsEvent]_block_invoke
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1366
+ -[MOContextAnalyticsManager getAnalyticsPlistFileURLWithFileName:]
+ _OBJC_CLASS_$_MOMomentsIntelligenceServiceManager
+ -[MOBundleContentExtractor initWithConfigurationManager:promptManager:]
+ OBJC_IVAR_$_MOContextAnalyticsManager._assertionError
+ _sysctl
+ __63-[MOContextManager _generateContextWithOption:request:handler:]_block_invoke.109
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.130
+ _objc_msgSend$generativeModelsAvailabilityStatus
+ -[MOContextAnalyticsManager bootTimestamp]
+ -[MOContextAnalyticsManager assertionError]
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ _kMOContextLastAssertionTaskRun
+ _objc_msgSend$clearMemoryAndExitCleanly
+ _kMOContextDBAssertionStatus
+ -[MOContextAnalyticsManager storeBinTime:withKey:toDict:]
+ -[MOContextAnalyticsManager isContextDBAvailable]
+ -[MOContextAnalyticsManager setIsContextDBAvailable:]
+ _kMOBundleClusterMetadatasubSuggestionIDsBeforePruning
+ OBJC_IVAR_$_MOClusterMetadata._subSuggestionIDsBeforePruning
+ -[MOClusterMetadata weekOfYearHistogram]
+ __block_literal_global.138
+ _objc_msgSend$initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:
+ OBJC_IVAR_$_MOContextManager._promptManager
+ _objc_msgSend$bootTimestamp
+ -[MOContextAnalyticsManager storeBinTime:withKey:toDict:].cold.1
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.136.cold.1
+ _kMOContextTimeSinceAssertionTaskRun
+ OBJC_IVAR_$_MOClusterMetadata._weekOfYearHistogram
+ -[MOContextAnalyticsManager storeBinTime:withKey:toDict:].cold.2
+ ___52+[MOPlatformInfo generativeModelsAvailabilityStatus]_block_invoke
+ +[MOPlatformInfo generativeModelsAvailabilityStatus]
+ __block_literal_global.135
+ _objc_msgSend$initWithAssertionErrorState:dbAvailability:
+ __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.123.cold.1
+ __block_literal_global.129
+ -[MOClusterMetadata setWeekOfYearHistogram:]
+ _stat
+ -[MOClusterMetadata subSuggestionIDsBeforePruning]
+ __55-[MOContextManager requestBackgroundProcessAccessForDB]_block_invoke.cold.1
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.130.cold.1
+ _kMOBundleClusterMetadataWeekOfYearHistogram
+ _objc_msgSend$initWithConfigurationManager:promptManager:
+ _objc_msgSend$getAnalyticsPlistFileURLWithFileName:
+ _objc_msgSend$storeBinTime:withKey:toDict:
+ -[MOClusterMetadata setSubSuggestionIDsBeforePruning:]
+ _objc_msgSend$promptManager
+ __52+[MOPlatformInfo generativeModelsAvailabilityStatus]_block_invoke.cold.1
+ __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.123
+ _kMOContextTimeSinceLastDBAssertionSuccess
+ _kMOContextTimeSinceLastBoot
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.133
- -[MOContextAnalyticsManager generateFetchAnalyticsPayload].cold.1
- __63-[MOContextManager _generateContextWithOption:request:handler:]_block_invoke.18
- __block_literal_global.38
- -[MOContextAnalyticsManager getAnalyticsPlistFileURL]
- -[MOContextAnalyticsManager generateFetchAnalyticsPayload].cold.2
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.45.cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.45
- -[MOContextAnalyticsManager generateFetchAnalyticsPayload].cold.3
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.42
- -[MOBundleContentExtractor initWithConfigurationManager:].cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.42.cold.1
- __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.32
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.39
- GCC_except_table30
- _objc_msgSend$initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:
- -[MOClusterMetadata initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:]
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1234
- __block_literal_global.47
- __block_literal_global.1350
- _objc_msgSend$getAnalyticsPlistFileURL
- __block_literal_global.41
- __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.32.cold.1
- -[MOContextAnalyticsManager generateFetchAnalyticsPayload].cold.4
- __block_literal_global.44
- -[MOBundleContentExtractor initWithConfigurationManager:]
- -[MOContextAnalyticsManager getAnalyticsPlistFileURL].cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.39.cold.1
CStrings:
+ "PSService,dealloc"
+ "lastTaskRegistration"
+ "setSubSuggestionIDsBeforePruning:"
+ "Carousel"
+ "lastAssertionStatus"
+ "TB,N,V_isContextDBAvailable"
+ "Could not get GMS Availability"
+ "_weekOfYearHistogram"
+ "last db assertion status: %!@(MISSING)"
+ "personalizedSensingAssertionAnalytics.plist"
+ "_subSuggestionIDsBeforePruning"
+ "Nightclub"
+ "subSuggestionIDsBeforePruning"
+ "acquireBackgroundProcessing, file ID, %!l(MISSING)lu"
+ "setAssertionError:"
+ "Ski Mountaineering"
+ "Farm"
+ "Log Cabin"
+ "getSuperTypeEnum:"
+ "bootTimestamp"
+ "TQ,N,V_assertionError"
+ "Shore"
+ "assertionStatus"
+ "Vineyard"
+ "lastTaskRun"
+ "_assertionError"
+ "timeSinceAssertionTaskRun"
+ "setWeekOfYearHistogram:"
+ "timeSinceLastAssertionFailure"
+ "Kayaking"
+ "setIsContextDBAvailable:"
+ "fetchGenerativeModelsAvailabilityWithReply:"
+ "Sailing"
+ "Time difference for key %!@(MISSING) (sec): %!f(MISSING)"
+ "storeBinTime:withKey:toDict:"
+ "initWithAssertionErrorState:dbAvailability:"
+ "getAnalyticsPlistFileURLWithFileName:"
+ "lastDBAssertionFailureTime"
+ "national monument"
+ "acquireBackgroundProcessingPermissionsForMomentsWithHander:"
+ "T@\"NSArray\",&,N,V_subSuggestionIDsBeforePruning"
+ "isContextDBAvailable"
+ "\x1f\x04"
+ "isGMSAvailable,%!d(MISSING)"
+ "com.apple.Moments.MOContextDBAssertion"
+ "Cruise Ship"
+ "Mountain"
+ "assertionError"
+ "Mountain Bike"
+ "initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:"
+ "initWithConfigurationManager:promptManager:"
+ "Failed to update background processing assertion for bundle DB"
+ "timeSinceDeviceBoot"
+ "weekOfYear"
+ "lastDBAssertionSuccessTime"
+ "@172@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148@156@164"
+ "Context DB assertion analytics payload sent: %!@(MISSING)"
+ "Forest"
+ "_isContextDBAvailable"
+ "sendAssertionAnalyticsEvent"
+ "assertionErrorType"
+ "Ferris Wheel"
+ "Parasailing"
+ "timeSinceAssertionTaskRegistration"
+ "v20@?0B8@\"NSError\"12"
+ "baseball"
+ "Mountain Biking"
+ "timeSinceLastAssertionSuccess"
+ "basketball"
+ "T@\"NSDictionary\",&,N,V_weekOfYearHistogram"
+ "Time difference for key %!@(MISSING) is after the current time."
+ "@28@0:8Q16B24"
+ "Succeed to update background processing assertion for bundle DB"
+ "generativeModelsAvailabilityStatus"
+ "weekOfYearHistogram"
- "Time since last successful invocation (sec): %!f(MISSING)"
- "Time of previous successful trigger is after the current time."
- "@156@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148"
- "\x1f\x02"
- "Time since last invocation (sec): %!f(MISSING)"
- "Time of previous trigger is after the current time."
- "MemoryCreation"
- "\n"
- "getAnalyticsPlistFileURL"
- "initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:timeContextFromPhotoTraitsHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:subBundleGoodnessScores:"
- "Photos"

```

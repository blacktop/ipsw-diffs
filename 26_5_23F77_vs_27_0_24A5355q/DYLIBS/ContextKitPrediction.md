## ContextKitPrediction

> `/System/Library/PrivateFrameworks/ContextKitPrediction.framework/ContextKitPrediction`

```diff

-302.0.0.0.0
-  __TEXT.__text: 0x97dc
-  __TEXT.__auth_stubs: 0x460
+305.0.0.0.0
+  __TEXT.__text: 0x9334
   __TEXT.__objc_methlist: 0x48c
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x2e4
-  __TEXT.__cstring: 0x8b1
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__cstring: 0x8bc
   __TEXT.__oslogstring: 0x5fc
   __TEXT.__dlopen_cstrs: 0x1e1
   __TEXT.__unwind_info: 0x328
-  __TEXT.__objc_classname: 0x98
-  __TEXT.__objc_methname: 0x16ee
-  __TEXT.__objc_methtype: 0x370
-  __TEXT.__objc_stubs: 0x13e0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x620
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x608
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x120
   __DATA.__bss: 0x58

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90B468A5-6BCD-39E1-A34F-AF53AA53D7C3
-  Functions: 172
-  Symbols:   747
-  CStrings:  459
+  UUID: FC81AA80-D2D9-316E-A246-69CE720FE830
+  Functions: 170
+  Symbols:   741
+  CStrings:  184
 
Symbols:
+ ___117-[CKContextRecentsCache insertUserActivityData:preferredTitle:bundleId:topics:hasAssociatedImageRepresentation:uuid:]_block_invoke.25
+ ___45-[CKContextRecentsCache allRecentsWithReply:]_block_invoke.29
+ ___45-[CKContextRecentsCache allRecentsWithReply:]_block_invoke.29.cold.1
+ ___45-[CKContextRecentsCache allRecentsWithReply:]_block_invoke.31
+ ___52-[CKContextRecentsCache _registerComputedModeStream]_block_invoke.61
+ ___63-[CKContextRecentsCache retrieveRecentsForPredictionWithReply:]_block_invoke.42
+ ___63-[CKContextRecentsCache retrieveRecentsForPredictionWithReply:]_block_invoke.45
+ ___73-[CKContextRecentsPredictionManager _updateBlendingLayerWithSuggestions:]_block_invoke.45
+ ___75-[CKContextRecentsCache retrieveRecentsBetweenStartDate:endDate:withReply:]_block_invoke.36
+ ___block_literal_global.44
+ ___block_literal_global.60
+ ___block_literal_global.65
+ ___block_literal_global.67
+ ___block_literal_global.74
+ ___block_literal_global.77
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retain_x26
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___117-[CKContextRecentsCache insertUserActivityData:preferredTitle:bundleId:topics:hasAssociatedImageRepresentation:uuid:]_block_invoke.26
- ___45-[CKContextRecentsCache allRecentsWithReply:]_block_invoke.30
- ___45-[CKContextRecentsCache allRecentsWithReply:]_block_invoke.30.cold.1
- ___45-[CKContextRecentsCache allRecentsWithReply:]_block_invoke.32
- ___52-[CKContextRecentsCache _registerComputedModeStream]_block_invoke.62
- ___63-[CKContextRecentsCache retrieveRecentsForPredictionWithReply:]_block_invoke.43
- ___63-[CKContextRecentsCache retrieveRecentsForPredictionWithReply:]_block_invoke.46
- ___73-[CKContextRecentsPredictionManager _updateBlendingLayerWithSuggestions:]_block_invoke.51
- ___75-[CKContextRecentsCache retrieveRecentsBetweenStartDate:endDate:withReply:]_block_invoke.37
- ___block_literal_global.45
- ___block_literal_global.61
- ___block_literal_global.66
- ___block_literal_global.68
- ___block_literal_global.75
- ___block_literal_global.78
- _objc_autorelease
- _objc_release_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<CKContextRecentsCacheDelegate>\""
- "@\"<CKContextRecentsPredictionManagerDelegate>\""
- "@\"ATXProactiveSuggestionClientModel\""
- "@\"BMUserActivityMetadataEvent\""
- "@\"BMUserActivityMetadataStream\""
- "@\"BMUserFocusComputedModeStream\""
- "@\"BPSSink\""
- "@\"CKContextRecentsCache\""
- "@\"DNDModeConfigurationService\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "CKContextRecentsCache"
- "CKContextRecentsCacheDelegate"
- "CKContextRecentsPredictionManager"
- "CKContextUserFacingUniversalRecent"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<CKContextRecentsCacheDelegate>\",W,N,V_delegate"
- "T@\"<CKContextRecentsPredictionManagerDelegate>\",W,N,V_delegate"
- "T@\"BMUserActivityMetadataEvent\",&,N,V_event"
- "T@\"CKContextRecentsCache\",R,N,V_recentsCache"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_associatedTopicIdsForRecent:"
- "_associatedTopicTitlesForRecent:"
- "_biomeQueue"
- "_clearSuggestions"
- "_clientModel"
- "_computedFocusModeQueue"
- "_computedModeSink"
- "_computedModeStream"
- "_configuration"
- "_constellationResult:intersectsWithRecent:"
- "_createClientModelIfNecessary"
- "_createDoNotDisturbServiceIfNecessary"
- "_createUserActivityDataWithOptions:completionHandler:"
- "_deferredMaintenanceTaskBlock"
- "_deferredMaintenanceTransaction"
- "_delegate"
- "_dndService"
- "_event"
- "_groupActivitiesByAppIntoSectionsWithRecents:limit:reply:"
- "_groupActivitiesByConstellationIntoSectionsWithRecents:limit:reply:"
- "_groupActivitiesByDateIntoSectionsWithRecents:limit:reply:"
- "_groupActivitiesByModeIntoSectionsWithRecents:limit:reply:"
- "_handleModeChangeToModeWithUUIDString:forCache:"
- "_initWithUserActivityData:"
- "_latestActivity"
- "_localizedStringForKey:"
- "_maximumNumberOfItemsToRetrieve"
- "_modeDidChangeToModeWithModeUUIDString:"
- "_modeForModeIdentifier:withConfigurations:"
- "_modeUUIDStringForComputedModeEvent:"
- "_oftenUsedStringForMode:"
- "_performMaintenanceTasks"
- "_performMaintenanceTasksForRecents:"
- "_pruneRecentsFromUnusedAppsForRecents:"
- "_recent:matchesKeywords:"
- "_recentlyUsedStringForMode:"
- "_recentsCache"
- "_recentsEligibleForDonationMatchingMode:fromRecents:uuidsToCounts:"
- "_registerComputedModeStream"
- "_relativeDateStringForRecent:"
- "_retrieveModeConfigurations"
- "_scheduleDeferredMaintenanceTasks"
- "_stream"
- "_suggestionConfidenceForRecent:withCount:"
- "_suggestionDonationTransaction"
- "_suggestionReportingQueue"
- "_suggestionsClearingBlock"
- "_suggestionsContributionBlock"
- "_updateBlendingLayerWithSuggestions:"
- "_updateLatestFocusMode"
- "_userFacingReasonStringForRecentWithNumberOfInstances:mode:"
- "absoluteString"
- "absoluteTimestamp"
- "activityType"
- "addObject:"
- "allKeys"
- "allRecentsWithReply:"
- "allocWithZone:"
- "array"
- "arrayByAddingObject:"
- "arrayWithArray:"
- "arrayWithObject:"
- "associatedBundleId"
- "associatedURLString"
- "autorelease"
- "bufferWithSize:prefetch:whenFull:"
- "bundleRecordWithApplicationIdentifier:error:"
- "bundleWithPath:"
- "cancel"
- "class"
- "clientWithDefaultRequestType:"
- "compare:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "date"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "didInitiatePruningMaintenanceTaskForCache:existingRecentsUUIDs:"
- "didInitiatePruningMaintenanceTaskForManager:existingRecentsUUIDs:"
- "earlierDate:"
- "eligiblePredictionsMatchingMode:forRecents:uuidsToCounts:"
- "enumerateKeysAndObjectsUsingBlock:"
- "error"
- "event"
- "eventBody"
- "executeWithReply:"
- "expirationDate"
- "filterWithIsIncluded:"
- "firstObject"
- "hasPrefix:"
- "hash"
- "identifier"
- "indexOfObject:"
- "init"
- "initWithAbsoluteTimestamp:userActivityData:title:activityType:associatedBundleId:associatedURLString:modeIdentifier:topics:hasAssociatedImageRepresentation:uuid:"
- "initWithCacheConfiguration:"
- "initWithClientModelId:clientModelVersion:"
- "initWithClientModelId:requestDelegate:"
- "initWithClientModelSpecification:executableSpecification:uiSpecification:scoreSpecification:"
- "initWithExecutableObject:executableDescription:executableIdentifier:suggestionExecutableType:"
- "initWithIdentifier:targetQueue:"
- "initWithNSUserActivity:actionUUID:bundleId:contentAttributeSet:itemIdentifier:heuristic:heuristicMetadata:criteria:isFutureMedia:title:subtitle:"
- "initWithRawScore:suggestedConfidenceCategory:"
- "initWithRestrictedStreamIdentifier:"
- "initWithTitle:subtitle:predictionReason:preferredLayoutConfigs:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:"
- "initWithUUIDString:"
- "insertObject:atIndex:"
- "insertUserActivityData:preferredTitle:bundleId:topics:hasAssociatedImageRepresentation:uuid:"
- "intValue"
- "intersectsOrderedSet:"
- "isEligibleForPrediction"
- "isEligibleForPublicIndexing"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isStarting"
- "keysSortedByValueUsingComparator:"
- "layoutConfigurationsForLayoutOptions:"
- "length"
- "level2Topics"
- "localizedCaseInsensitiveContainsString:"
- "localizedStringForKey:value:table:"
- "mode"
- "modeConfigurationsReturningError:"
- "modeDidChangeToModeWithUUIDString:forCache:"
- "modeIdentifier"
- "name"
- "newRequest"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "orderedSetWithArray:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "processName"
- "pruneRecentsForBundleIdentifiers:"
- "pruneWithPredicateBlock:"
- "publisher"
- "publisherFromStartTime:"
- "q32@0:8@16Q24"
- "recentsCache"
- "referrerURL"
- "relatedItems"
- "release"
- "removeAllRecentsWithReply:"
- "removeLastObject"
- "removeObjectAtIndex:"
- "removeRecentWithUUID:"
- "removeRecentsMatchingRecent:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retrievePredictionsForMode:withReply:"
- "retrieveRecentMatchingUUID:withReply:"
- "retrieveRecentsBetweenStartDate:endDate:withReply:"
- "retrieveRecentsCatalogWithStyle:withReply:"
- "retrieveRecentsForPredictionWithReply:"
- "retrieveRecentsMatchingBundleIdentifier:withReply:"
- "retrieveRecentsMatchingMode:withReply:"
- "retrieveRecentsMatchingStrings:withReply:"
- "retrieveRecentsMatchingTopicIds:titles:withReply:"
- "reverseObjectEnumerator"
- "self"
- "semanticType"
- "sendEvent:"
- "serviceForClientIdentifier:"
- "setDateStyle:"
- "setDelegate:"
- "setDoesRelativeDateFormatting:"
- "setEvent:"
- "setIncludeHigherLevelTopics:"
- "setItemIds:"
- "setMaxConstellationTopics:"
- "setObject:forKeyedSubscript:"
- "setTimeStyle:"
- "setWithArray:"
- "sinkWithCompletion:receiveInput:"
- "sinkWithCompletion:shouldContinue:"
- "sortedArrayUsingSelector:"
- "source"
- "startContributingPredictions"
- "state"
- "stopContributingPredictions"
- "stringFromDate:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "subscribeOn:"
- "superclass"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "title"
- "topicId"
- "topicIdentifier"
- "topics"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateSuggestions:"
- "updateSuggestions:completionHandler:"
- "userActivityData"
- "uuid"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"CKContextRecentsCache\"16@\"NSArray\"24"
- "v32@0:8@\"NSString\"16@\"CKContextRecentsCache\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v60@0:8@16@24@32@40B48@52"
- "webpageURL"
- "zone"

```

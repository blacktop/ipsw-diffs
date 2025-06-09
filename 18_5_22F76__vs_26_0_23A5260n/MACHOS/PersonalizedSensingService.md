## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-206.0.7.0.0
-  __TEXT.__text: 0x6842c
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0xacc0
-  __TEXT.__objc_methlist: 0x6db0
-  __TEXT.__objc_classname: 0x848
-  __TEXT.__objc_methtype: 0xfe8
-  __TEXT.__cstring: 0xb152
-  __TEXT.__objc_methname: 0x11b55
-  __TEXT.__const: 0x498
-  __TEXT.__gcc_except_tab: 0xbe0
-  __TEXT.__oslogstring: 0x6d58
-  __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1190
-  __DATA_CONST.__auth_got: 0x480
+255.0.0.0.0
+  __TEXT.__text: 0x722bc
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0xb3e0
+  __TEXT.__objc_methlist: 0x71e4
+  __TEXT.__objc_classname: 0x83c
+  __TEXT.__objc_methtype: 0x1116
+  __TEXT.__cstring: 0xbe85
+  __TEXT.__objc_methname: 0x12cc6
+  __TEXT.__const: 0x500
+  __TEXT.__gcc_except_tab: 0xe84
+  __TEXT.__oslogstring: 0x743b
+  __TEXT.__ustring: 0x10c
+  __TEXT.__unwind_info: 0x12b8
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2f50
-  __DATA_CONST.__cfstring: 0xe940
-  __DATA_CONST.__objc_classlist: 0x2e8
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__const: 0x3238
+  __DATA_CONST.__cfstring: 0xf960
+  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x230
-  __DATA_CONST.__objc_intobj: 0xc00
-  __DATA_CONST.__objc_arraydata: 0x908
-  __DATA_CONST.__objc_arrayobj: 0xa50
+  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_intobj: 0xd98
+  __DATA_CONST.__objc_arraydata: 0x930
+  __DATA_CONST.__objc_arrayobj: 0xbd0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_floatobj: 0x1b0
+  __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xbd00
-  __DATA.__objc_selrefs: 0x37b0
-  __DATA.__objc_ivar: 0x938
-  __DATA.__objc_data: 0x1d10
-  __DATA.__data: 0x4c0
-  __DATA.__bss: 0x40
+  __DATA.__objc_const: 0xc168
+  __DATA.__objc_selrefs: 0x3ab0
+  __DATA.__objc_ivar: 0x99c
+  __DATA.__objc_data: 0x1d60
+  __DATA.__data: 0x4d8
+  __DATA.__bss: 0x50
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 460748D0-D5FC-3D7A-8ED2-DBF9EF4F30E0
-  Functions: 2497
-  Symbols:   19012
-  CStrings:  7392
+  UUID: 25060094-634D-370C-B90A-BD6C490CC3E8
+  Functions: 2627
+  Symbols:   19853
+  CStrings:  7822
 
Symbols:
+ +[MOContextPredicate contextPredicateForContextType:withMetadata:startDate:endDate:]
+ +[MOContextPredicate contextPredicateForContextType:withMetadata:startDate:endDate:aroundLocation:withDistanceThreshold:]
+ +[MOContextPredicate supportsSecureCoding]
+ +[MOContextPredicateBuilder createAndPredicate:]
+ +[MOContextPredicateBuilder createNotPredicate:]
+ +[MOContextPredicateBuilder createOrPredicate:]
+ +[MOContextPredicateBuilder createPredicateForValue:inCollection:]
+ +[MOContextPredicateBuilder createPredicateWithLeftExpression:rightExpression:operation:]
+ +[MOContextPredicateBuilder disassemblePredicate:]
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.1
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.2
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.3
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.4
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.5
+ +[MOContextPredicateBuilder extractFirstValueForKeyPath:fromPredicates:]
+ +[MOContextPredicateBuilder inspectExpression:]
+ +[MOContextPredicateBuilder inspectExpression:].cold.1
+ +[MOContextPredicateBuilder inspectExpression:].cold.2
+ +[MOContextPredicateBuilder inspectExpression:].cold.3
+ +[MOContextPredicateBuilder inspectExpression:].cold.4
+ +[MOContextPredicateBuilder inspectExpression:].cold.5
+ +[MOContextPredicateBuilder inspectExpression:].cold.6
+ +[MOContextPredicateBuilder inspectExpression:].cold.7
+ +[MOContextPredicateBuilder inspectExpression:].cold.8
+ +[MOContextPredicateBuilder inspectExpression:].cold.9
+ +[MOContextPredicateBuilder predicateOperatorFromType:]
+ +[MOContextPredicateBuilder stringForCompoundPredicateType:]
+ +[MOContextPredicateBuilder stringForOperatorType:]
+ +[MODefaultsManager isExtendedLogEnabled:forDetaultsManager:]
+ +[MODefaultsManager momentsDaemonDefaults]
+ +[MODefaultsManager momentsDaemonDefaults].cold.1
+ +[MOEventBundle convertNSNumberToContactType:]
+ +[MOEventBundle convertNSNumberToRoadType:]
+ +[MOEventBundle convertNSNumberToSensitiveLocationType:]
+ +[MOEventBundle convertNSNumberToUninterestingLocationType:]
+ +[MOEventInvite supportsSecureCoding]
+ +[MOInvitePerson supportsSecureCoding]
+ +[MOMetaDataCurationUtility getPersonFromBirthdayPhotoTrait:eventBundle:]
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:]
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:]
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:].cold.1
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:].cold.2
+ +[MOMetaDataCurationUtility selectBirthdayFromPhotoTraits:]
+ +[MOMetaDataCurationUtility selectHolidayFromPhotoTraits:]
+ +[MOTime timeStringSingularToPluralForm:]
+ -[MOBundleContent endDate]
+ -[MOBundleContent hasLocation]
+ -[MOBundleContent location]
+ -[MOBundleContent setEndDate:]
+ -[MOBundleContent setHasLocation:]
+ -[MOBundleContent setLocation:]
+ -[MOBundleContent setStartDate:]
+ -[MOBundleContent startDate]
+ -[MOBundleContentExtractor _filterExtractedBundles:contextPredicate:withHandler:]
+ -[MOBundleContentExtractor _filterExtractedBundles:contextPredicate:withHandler:].cold.1
+ -[MOBundleContentExtractor extractContentsFromBundlesWithBundlePredicate:contextPredicate:handler:]
+ -[MOClusterMetadata celebrationHistogram]
+ -[MOClusterMetadata holidayHistogram]
+ -[MOClusterMetadata initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:holidayHistogram:celebrationHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:stateOfMindValenceHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:phenotypePersonUUIDs:]
+ -[MOClusterMetadata phenotypePersonUUIDs]
+ -[MOClusterMetadata setCelebrationHistogram:]
+ -[MOClusterMetadata setHolidayHistogram:]
+ -[MOClusterMetadata setPhenotypePersonUUIDs:]
+ -[MOClusterMetadata setStateOfMindValenceHistogram:]
+ -[MOClusterMetadata stateOfMindValenceHistogram]
+ -[MOContext isWithinDistanceFromLocation:maxDistance:]
+ -[MOContextActivityMetaData initWithActivityType:]
+ -[MOContextFetchOptions batchSize]
+ -[MOContextFetchOptions setBatchSize:]
+ -[MOContextLocationMetaData deserializeCLLocationObject:]
+ -[MOContextLocationMetaData initWithPlace:city:location:]
+ -[MOContextLocationMetaData location]
+ -[MOContextLocationMetaData serializeCLLocationObject]
+ -[MOContextManager _activityStringFromEnum:]
+ -[MOContextManager _addMetaDataToContextForRetrieval:bundleContent:authorizedTypes:]
+ -[MOContextManager _addMetaDataToContextForRetrieval:bundleContent:authorizedTypes:].cold.1
+ -[MOContextManager _addMetaDataToContextForRetrieval:bundleContent:authorizedTypes:].cold.2
+ -[MOContextManager _addMetaDataToContextForRetrieval:bundleContent:authorizedTypes:].cold.3
+ -[MOContextManager _bundleTypeFromContextType:]
+ -[MOContextManager _createContextsWithBundleContents:]
+ -[MOContextManager _createContextsWithBundleContents:authorizedTypes:]
+ -[MOContextManager _fetchContextWithOption:predicates:authorizedTypes:handler:]
+ -[MOContextManager _replacePredicate:forKeyPath:withNewKeyPath:newValue:comparisonType:]
+ -[MOContextManager _retrieveContextWithOption:predicate:authorizedTypes:handler:]
+ -[MOContextManager filterResults:withCriteria:]
+ -[MOContextManager filterResults:withCriteria:].cold.1
+ -[MOContextManager retrieveContextWithOption:predicates:authorizedTypes:handler:]
+ -[MOContextManager updatePredicateType:]
+ -[MOContextPredicate .cxx_destruct]
+ -[MOContextPredicate copyWithZone:]
+ -[MOContextPredicate encodeWithCoder:]
+ -[MOContextPredicate fetchRequestPredicate]
+ -[MOContextPredicate filterCriteriaMap]
+ -[MOContextPredicate initWithCoder:]
+ -[MOContextPredicate initWithPredicate:filter:metadataTypes:]
+ -[MOContextPredicate metadataTypes]
+ -[MOContextPredicate setFetchRequestPredicate:]
+ -[MOContextPredicate setFilterCriteriaMap:]
+ -[MOContextPredicate setMetadataTypes:]
+ -[MOContextTimeMetaData endDate]
+ -[MOContextTimeMetaData initWithStartDate:endDate:timeReferenceString:]
+ -[MOContextTimeMetaData setEndDate:]
+ -[MOContextTimeMetaData setStartDate:]
+ -[MOContextTimeMetaData startDate]
+ -[MOEvent categoryMuid]
+ -[MOEvent inviteEvent]
+ -[MOEvent setCategoryMuid:]
+ -[MOEvent setInviteEvent:]
+ -[MOEventBundle initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:]
+ -[MOEventBundle initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:isSensitive:]
+ -[MOEventBundle initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:]
+ -[MOEventBundle isSensitive]
+ -[MOEventBundle setIsSensitive:]
+ -[MOEventBundle shortDescription]
+ -[MOEventBundleLabelTemplate checkConditionForMetaData:].cold.1
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.10
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.9
+ -[MOEventBundleRankingInput isBusinessContact]
+ -[MOEventBundleRankingInput isSensitiveLocation]
+ -[MOEventBundleRankingInput numBirthdayAssets]
+ -[MOEventBundleRankingInput numHolidayAssets]
+ -[MOEventBundleRankingInput numInviteEvents]
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setIsBusinessContact:]
+ -[MOEventBundleRankingInput setIsSensitiveLocation:]
+ -[MOEventBundleRankingInput setNumBirthdayAssets:]
+ -[MOEventBundleRankingInput setNumHolidayAssets:]
+ -[MOEventBundleRankingInput setNumInviteEvents:]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ -[MOEventBundleRankingInput setViewCount:]
+ -[MOEventBundleRankingInput viewCount]
+ -[MOEventFetchOptions categories]
+ -[MOEventFetchOptions initWithDateInterval:ascending:categories:limit:]
+ -[MOEventInvite .cxx_destruct]
+ -[MOEventInvite copyWithZone:]
+ -[MOEventInvite description]
+ -[MOEventInvite encodeWithCoder:]
+ -[MOEventInvite initWithCoder:]
+ -[MOEventInvite init]
+ -[MOEventInvite inviteEventAttendees]
+ -[MOEventInvite inviteEventIsAllDay]
+ -[MOEventInvite inviteEventLocation]
+ -[MOEventInvite inviteEventOrganizers]
+ -[MOEventInvite inviteEventPlaceName]
+ -[MOEventInvite inviteEventTitle]
+ -[MOEventInvite setInviteEventAttendees:]
+ -[MOEventInvite setInviteEventIsAllDay:]
+ -[MOEventInvite setInviteEventLocation:]
+ -[MOEventInvite setInviteEventOrganizers:]
+ -[MOEventInvite setInviteEventPlaceName:]
+ -[MOEventInvite setInviteEventTitle:]
+ -[MOEventRoutine categoryMuid]
+ -[MOEventRoutine setCategoryMuid:]
+ -[MOEventSignificantContact containsOrganizationContact]
+ -[MOEventSignificantContact setContainsOrganizationContact:]
+ -[MOInvitePerson .cxx_destruct]
+ -[MOInvitePerson copyWithZone:]
+ -[MOInvitePerson description]
+ -[MOInvitePerson displayName]
+ -[MOInvitePerson encodeWithCoder:]
+ -[MOInvitePerson initWithCoder:]
+ -[MOInvitePerson isMe]
+ -[MOInvitePerson rsvpStatus]
+ -[MOInvitePerson setDisplayName:]
+ -[MOInvitePerson setIsMe:]
+ -[MOInvitePerson setRsvpStatus:]
+ -[MOPhotoTrait associatedPersonLocalIdentifiers]
+ -[MOPhotoTrait holidayIdentifier]
+ -[MOPhotoTrait initWithIdentifier:name:labelType:holidayIdentifier:meaningIdentifier:relevantAssetUUIDs:associatedPersonLocalIdentifiers:]
+ -[MOPhotoTrait initWithIdentifier:name:labelType:holidayIdentifier:relevantAssetUUIDs:]
+ -[MOPhotoTrait labelType]
+ -[MOPhotoTrait meaningIdentifier]
+ -[MOPhotoTrait setAssociatedPersonLocalIdentifiers:]
+ -[MOPhotoTrait setHolidayIdentifier:]
+ -[MOPhotoTrait setLabelType:]
+ -[MOPhotoTrait setMeaningIdentifier:]
+ -[MOPlace categoryMuid]
+ -[MOPlace initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:]
+ -[MOPlace initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:]
+ -[MOPlace initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:]
+ -[MOPlace setCategoryMuid:]
+ -[MOResource initWithIdentifier:name:type:assets:data:value:priorityScore:photoCurationScore:photoFaceCount:photoAssetMediaType:photoAssetCloudIdentifier:]
+ -[MOResource initWithName:type:photoAssetCloudIdentifier:]
+ -[MOResource photoAssetCloudIdentifier]
+ -[MOResource setPhotoAssetCloudIdentifier:]
+ -[PersonalizedSensingService fetchContextWithOptions:predicates:authorizedTypes:withReply:]
+ -[PersonalizedSensingService fetchContextWithOptions:predicates:authorizedTypes:withReply:].cold.1
+ -[PersonalizedSensingService setEntitlementsForDataAccess:]
+ -[PersonalizedSensingServiceDelegate .cxx_destruct]
+ -[PersonalizedSensingServiceDelegate clientConnection:cacheContextRetrievalEntitlement:]
+ -[PersonalizedSensingServiceDelegate clientConnection:cachePersonalizedContextEntitlement:]
+ -[PersonalizedSensingServiceDelegate init]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOContextPredicate.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOContextPredicateBuilder.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOEventBundleRankingKeys.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOEventInvite.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOMetaDataCurationUtility.o
+ GCC_except_table109
+ GCC_except_table19
+ GCC_except_table32
+ GCC_except_table40
+ GCC_except_table55
+ GCC_except_table69
+ MOContextPredicate.m
+ MOContextPredicateBuilder.m
+ MOEventBundleRankingKeys.m
+ MOEventInvite.m
+ MOMetaDataCurationUtility.m
+ OBJC_IVAR_$_MOBundleContent._endDate
+ OBJC_IVAR_$_MOBundleContent._hasLocation
+ OBJC_IVAR_$_MOBundleContent._location
+ OBJC_IVAR_$_MOBundleContent._startDate
+ OBJC_IVAR_$_MOClusterMetadata._celebrationHistogram
+ OBJC_IVAR_$_MOClusterMetadata._holidayHistogram
+ OBJC_IVAR_$_MOClusterMetadata._phenotypePersonUUIDs
+ OBJC_IVAR_$_MOClusterMetadata._stateOfMindValenceHistogram
+ OBJC_IVAR_$_MOContextFetchOptions._batchSize
+ OBJC_IVAR_$_MOContextLocationMetaData._location
+ OBJC_IVAR_$_MOContextPredicate._fetchRequestPredicate
+ OBJC_IVAR_$_MOContextPredicate._filterCriteriaMap
+ OBJC_IVAR_$_MOContextPredicate._metadataTypes
+ OBJC_IVAR_$_MOContextTimeMetaData._endDate
+ OBJC_IVAR_$_MOContextTimeMetaData._startDate
+ OBJC_IVAR_$_MOEvent._inviteEvent
+ OBJC_IVAR_$_MOEventBundle._isSensitive
+ OBJC_IVAR_$_MOEventBundleRankingInput._isBusinessContact
+ OBJC_IVAR_$_MOEventBundleRankingInput._isSensitiveLocation
+ OBJC_IVAR_$_MOEventBundleRankingInput._numBirthdayAssets
+ OBJC_IVAR_$_MOEventBundleRankingInput._numHolidayAssets
+ OBJC_IVAR_$_MOEventBundleRankingInput._numInviteEvents
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._viewCount
+ OBJC_IVAR_$_MOEventFetchOptions._categories
+ OBJC_IVAR_$_MOEventInvite._inviteEventAttendees
+ OBJC_IVAR_$_MOEventInvite._inviteEventIsAllDay
+ OBJC_IVAR_$_MOEventInvite._inviteEventLocation
+ OBJC_IVAR_$_MOEventInvite._inviteEventOrganizers
+ OBJC_IVAR_$_MOEventInvite._inviteEventPlaceName
+ OBJC_IVAR_$_MOEventInvite._inviteEventTitle
+ OBJC_IVAR_$_MOEventRoutine._categoryMuid
+ OBJC_IVAR_$_MOEventSignificantContact._containsOrganizationContact
+ OBJC_IVAR_$_MOInvitePerson._displayName
+ OBJC_IVAR_$_MOInvitePerson._isMe
+ OBJC_IVAR_$_MOInvitePerson._rsvpStatus
+ OBJC_IVAR_$_MOPhotoTrait._associatedPersonLocalIdentifiers
+ OBJC_IVAR_$_MOPhotoTrait._holidayIdentifier
+ OBJC_IVAR_$_MOPhotoTrait._labelType
+ OBJC_IVAR_$_MOPhotoTrait._meaningIdentifier
+ OBJC_IVAR_$_MOPlace._categoryMuid
+ OBJC_IVAR_$_MOResource._photoAssetCloudIdentifier
+ OBJC_IVAR_$_PersonalizedSensingService.dataAccessEntitlements
+ OBJC_IVAR_$_PersonalizedSensingServiceDelegate.dataAccessEntitlements
+ _CLLocationCoordinate2DMake
+ _KIsInThematicSummaryKey
+ _MOContextFilterKeyLocation
+ _MOEventBundleSubTypeStringPersonalizedReflectionActivity
+ _MOEventBundleSubTypeStringPersonalizedReflectionContact
+ _MOEventBundleSubTypeStringPersonalizedReflectionOuting
+ _MOEventBundleSubTypeStringThematicSummaryCommonActivity
+ _MOEventBundleSubTypeStringThematicSummaryCommonPlace
+ _MOEventBundleSubTypeStringThematicSummaryHoliday
+ _MOEventBundleSubTypeStringThematicSummaryPhotoSubject
+ _MOEventBundleSubTypeStringThematicSummarySocial
+ _MOEventBundleSubTypeStringThematicSummaryStateOfMind
+ _MOEventBundleSuperTypeStringPersonalizedReflection
+ _MOEventBundleSuperTypeStringThematicSummary
+ _MOEventBundleTypeThematicSummary
+ _MOPhotoResourceICloudIdentifier
+ _OBJC_CLASS_$_MOContextPredicate
+ _OBJC_CLASS_$_MOContextPredicateBuilder
+ _OBJC_CLASS_$_MOEventInvite
+ _OBJC_CLASS_$_MOInvitePerson
+ _OBJC_CLASS_$_MOMetaDataCurationUtility
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSExpression
+ _OBJC_METACLASS_$_MOContextPredicate
+ _OBJC_METACLASS_$_MOContextPredicateBuilder
+ _OBJC_METACLASS_$_MOEventInvite
+ _OBJC_METACLASS_$_MOInvitePerson
+ _OBJC_METACLASS_$_MOMetaDataCurationUtility
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.763
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.765
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.765.cold.1
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1538
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.186
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.186.cold.1
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.189
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.189.cold.1
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.192
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.192.cold.1
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.514
+ __63-[MOContextManager _generateContextWithOption:request:handler:]_block_invoke.118
+ __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.179
+ __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.179.cold.1
+ __79-[MOContextManager _fetchContextWithOption:predicates:authorizedTypes:handler:]_block_invoke.125
+ __79-[MOContextManager _fetchContextWithOption:predicates:authorizedTypes:handler:]_block_invoke.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.691
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.691.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.695
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.695.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.699
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.702
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.717
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.718
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.749
+ __99-[MOBundleContentExtractor extractContentsFromBundlesWithBundlePredicate:contextPredicate:handler:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_MOContext
+ __OBJC_$_CLASS_METHODS_MOContextPredicate
+ __OBJC_$_CLASS_METHODS_MOContextPredicateBuilder
+ __OBJC_$_CLASS_METHODS_MODefaultsManager
+ __OBJC_$_CLASS_METHODS_MOEventInvite
+ __OBJC_$_CLASS_METHODS_MOInvitePerson
+ __OBJC_$_CLASS_METHODS_MOMetaDataCurationUtility
+ __OBJC_$_CLASS_PROP_LIST_MOContextPredicate
+ __OBJC_$_CLASS_PROP_LIST_MOEventInvite
+ __OBJC_$_CLASS_PROP_LIST_MOInvitePerson
+ __OBJC_$_INSTANCE_METHODS_MOContext(MOContextMO)
+ __OBJC_$_INSTANCE_METHODS_MOContextPredicate
+ __OBJC_$_INSTANCE_METHODS_MOEventInvite
+ __OBJC_$_INSTANCE_METHODS_MOInvitePerson
+ __OBJC_$_INSTANCE_VARIABLES_MOContextPredicate
+ __OBJC_$_INSTANCE_VARIABLES_MOEventInvite
+ __OBJC_$_INSTANCE_VARIABLES_MOInvitePerson
+ __OBJC_$_PROP_LIST_MOContextPredicate
+ __OBJC_$_PROP_LIST_MOEventInvite
+ __OBJC_$_PROP_LIST_MOInvitePerson
+ __OBJC_CLASS_PROTOCOLS_$_MOContextPredicate
+ __OBJC_CLASS_PROTOCOLS_$_MOEventInvite
+ __OBJC_CLASS_PROTOCOLS_$_MOInvitePerson
+ __OBJC_CLASS_RO_$_MOContextPredicate
+ __OBJC_CLASS_RO_$_MOContextPredicateBuilder
+ __OBJC_CLASS_RO_$_MOEventInvite
+ __OBJC_CLASS_RO_$_MOInvitePerson
+ __OBJC_CLASS_RO_$_MOMetaDataCurationUtility
+ __OBJC_METACLASS_RO_$_MOContextPredicate
+ __OBJC_METACLASS_RO_$_MOContextPredicateBuilder
+ __OBJC_METACLASS_RO_$_MOEventInvite
+ __OBJC_METACLASS_RO_$_MOInvitePerson
+ __OBJC_METACLASS_RO_$_MOMetaDataCurationUtility
+ ___42+[MODefaultsManager momentsDaemonDefaults]_block_invoke
+ ___79-[MOContextManager _fetchContextWithOption:predicates:authorizedTypes:handler:]_block_invoke
+ ___81-[MOBundleContentExtractor _filterExtractedBundles:contextPredicate:withHandler:]_block_invoke
+ ___81-[MOContextManager _retrieveContextWithOption:predicate:authorizedTypes:handler:]_block_invoke
+ ___81-[MOContextManager retrieveContextWithOption:predicates:authorizedTypes:handler:]_block_invoke
+ ___81-[MOContextManager retrieveContextWithOption:predicates:authorizedTypes:handler:]_block_invoke_2
+ ___90+[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:]_block_invoke
+ ___91-[PersonalizedSensingService fetchContextWithOptions:predicates:authorizedTypes:withReply:]_block_invoke
+ ___99-[MOBundleContentExtractor extractContentsFromBundlesWithBundlePredicate:contextPredicate:handler:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e36_v32?0"NSMutableDictionary"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e36_v32?0"NSMutableDictionary"8Q16^B24lr40l8r48l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e29_v24?0"NSArray"8"NSError"16lr64l8s32l8s40l8s48l8r72l8s56l8
+ ___predicateForRemovingDuplicates_block_invoke
+ __block_literal_global.1661
+ __block_literal_global.185
+ __block_literal_global.188
+ __block_literal_global.191
+ __block_literal_global.194
+ __block_literal_global.197
+ __dispatch_main_q
+ _kActionNameHostingAtHome
+ _kActionNamePhotosAtHome
+ _kActionNameTimeAtHome
+ _kActionNameVisit
+ _kDecayRateAfterViewedKey
+ _kIsEligibleForTransitBundleSummarization
+ _kIsSensitive
+ _kMOBundleCategoryMuid
+ _kMOBundleClusterMetadataCelebrationHistogram
+ _kMOBundleClusterMetadataHolidayHistogram
+ _kMOBundleClusterMetadataPhenotypePersonUUIDs
+ _kMOBundleClusterMetadataStateOfMindValenceHistogram
+ _kMOBundleClusterMetadataSubSuggestionIDsBeforePruning
+ _kMOEmbeddingDistanceWeightCelebration
+ _kMOEmbeddingDistanceWeightHoliday
+ _kMOEmbeddingDistanceWeightStateOfMindContext
+ _kMOEmbeddingDistanceWeightStateOfMindDomains
+ _kMOEmbeddingDistanceWeightStateOfMindLabels
+ _kMOEmbeddingDistanceWeightStateOfMindValence
+ _kMOEventBundleMetaDataForRankKeywordBusinessContact
+ _kMOEventBundleMetaDataForRankKeywordInterestingLocation
+ _kMOEventBundleMetaDataForRankKeywordSensitiveLocation
+ _kMOEventBundleMetaDataForRankKeywordUninterestingLocation
+ _kMOEventCategoryMuid
+ _kMOEventRoutineEventCategoryMuid
+ _kMOPersonRelationshipScoreThresholdForChild
+ _kMOPersonRelationshipScoreThresholdForCoworker
+ _kMOPersonRelationshipScoreThresholdForFamily
+ _kMOPersonRelationshipScoreThresholdForFriend
+ _kMOPersonRelationshipScoreThresholdForMyPet
+ _kMOPersonalizedSensingXPCEntitlementActivity
+ _kMOPersonalizedSensingXPCEntitlementDataAccess
+ _kMOPersonalizedSensingXPCEntitlementLocation
+ _kMOPersonalizedSensingXPCEntitlementTime
+ _kMOStateOfMindContextEmbeddingDomains
+ _kMOStateOfMindContextEmbeddingLabels
+ _kMOStateOfMindContextEmbeddingValenceValues
+ _kMOTimeContextEmbeddingCelebration
+ _kMOTimeContextEmbeddingHoliday
+ _kMaxNumOfBirthdayBundlesPerDay
+ _kMaxNumOfHolidayBundlesPerDay
+ _kNumBirthdayAssets
+ _kNumHolidayAssets
+ _kNumInviteEvents
+ _kSensitiveRecommendedThresholdKey
+ _kUseBirthdayLabel
+ _kUseHolidayLabel
+ _kWeightBirthdayInclusionKey
+ _kWeightForIsBusinessContact
+ _kWeightForSensitivePOI
+ _kWeightHolidayInclusionKey
+ _kWeightInviteEventInclusionKey
+ _objc_msgSend$_activityStringFromEnum:
+ _objc_msgSend$_addMetaDataToContextForRetrieval:bundleContent:authorizedTypes:
+ _objc_msgSend$_bundleTypeFromContextType:
+ _objc_msgSend$_createContextsWithBundleContents:authorizedTypes:
+ _objc_msgSend$_fetchContextWithOption:predicates:authorizedTypes:handler:
+ _objc_msgSend$_filterExtractedBundles:contextPredicate:withHandler:
+ _objc_msgSend$_replacePredicate:forKeyPath:withNewKeyPath:newValue:comparisonType:
+ _objc_msgSend$_retrieveContextWithOption:predicate:authorizedTypes:handler:
+ _objc_msgSend$allowEvaluation
+ _objc_msgSend$altitude
+ _objc_msgSend$arguments
+ _objc_msgSend$associatedPersonLocalIdentifiers
+ _objc_msgSend$categories
+ _objc_msgSend$categoryMuid
+ _objc_msgSend$clientConnection:cacheContextRetrievalEntitlement:
+ _objc_msgSend$clientConnection:cachePersonalizedContextEntitlement:
+ _objc_msgSend$collection
+ _objc_msgSend$comparisonPredicateModifier
+ _objc_msgSend$compoundPredicateType
+ _objc_msgSend$constantValue
+ _objc_msgSend$coordinate
+ _objc_msgSend$createAndPredicate:
+ _objc_msgSend$createPredicateWithLeftExpression:rightExpression:operation:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$deserializeCLLocationObject:
+ _objc_msgSend$disassemblePredicate:
+ _objc_msgSend$distanceFromLocation:
+ _objc_msgSend$expressionForConstantValue:
+ _objc_msgSend$expressionForKeyPath:
+ _objc_msgSend$expressionType
+ _objc_msgSend$extractContentsFromBundlesWithBundlePredicate:contextPredicate:handler:
+ _objc_msgSend$extractFirstValueForKeyPath:fromPredicates:
+ _objc_msgSend$fetchEventBundlesWithPredicate:handler:
+ _objc_msgSend$fetchRequestPredicate
+ _objc_msgSend$filterCriteriaMap
+ _objc_msgSend$filterResults:withCriteria:
+ _objc_msgSend$function
+ _objc_msgSend$getPersonFromBirthdayPhotoTrait:eventBundle:
+ _objc_msgSend$getTheBestPersonRelationtshipTagFor:useRelationshipInference:
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$hasLocation
+ _objc_msgSend$holidayIdentifier
+ _objc_msgSend$horizontalAccuracy
+ _objc_msgSend$initWithActivityType:
+ _objc_msgSend$initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:
+ _objc_msgSend$initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:
+ _objc_msgSend$initWithDateInterval:ascending:categories:limit:
+ _objc_msgSend$initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:holidayHistogram:celebrationHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:stateOfMindValenceHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:phenotypePersonUUIDs:
+ _objc_msgSend$initWithIdentifier:name:labelType:holidayIdentifier:meaningIdentifier:relevantAssetUUIDs:associatedPersonLocalIdentifiers:
+ _objc_msgSend$initWithIdentifier:name:type:assets:data:value:priorityScore:photoCurationScore:photoFaceCount:photoAssetMediaType:photoAssetCloudIdentifier:
+ _objc_msgSend$initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$initWithPlace:city:location:
+ _objc_msgSend$initWithPredicate:filter:metadataTypes:
+ _objc_msgSend$initWithStartDate:endDate:timeReferenceString:
+ _objc_msgSend$inspectExpression:
+ _objc_msgSend$isBusinessContact
+ _objc_msgSend$isMe
+ _objc_msgSend$isSensitive
+ _objc_msgSend$isSensitiveLocation
+ _objc_msgSend$isWithinDistanceFromLocation:maxDistance:
+ _objc_msgSend$keyPath
+ _objc_msgSend$labelType
+ _objc_msgSend$leftExpression
+ _objc_msgSend$meaningIdentifier
+ _objc_msgSend$metadataTypes
+ _objc_msgSend$notPredicateWithSubpredicate:
+ _objc_msgSend$numBirthdayAssets
+ _objc_msgSend$numHolidayAssets
+ _objc_msgSend$numInviteEvents
+ _objc_msgSend$pCountMaxNormalized
+ _objc_msgSend$pCountWeightedAverageNormalized
+ _objc_msgSend$pCountWeightedSumNormalized
+ _objc_msgSend$photoAssetCloudIdentifier
+ _objc_msgSend$predicateFormat
+ _objc_msgSend$predicateOperatorFromType:
+ _objc_msgSend$predicateOperatorType
+ _objc_msgSend$predicateWithLeftExpression:rightExpression:modifier:type:options:
+ _objc_msgSend$retrieveContextWithOption:predicates:authorizedTypes:handler:
+ _objc_msgSend$rightExpression
+ _objc_msgSend$rsvpStatus
+ _objc_msgSend$selectBirthdayFromPhotoTraits:
+ _objc_msgSend$selectHolidayFromPhotoTraits:
+ _objc_msgSend$serializeCLLocationObject
+ _objc_msgSend$set
+ _objc_msgSend$setCategoryMuid:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setEntitlementsForDataAccess:
+ _objc_msgSend$setHasLocation:
+ _objc_msgSend$setIsBusinessContact:
+ _objc_msgSend$setIsMe:
+ _objc_msgSend$setIsSensitiveLocation:
+ _objc_msgSend$setNumBirthdayAssets:
+ _objc_msgSend$setNumHolidayAssets:
+ _objc_msgSend$setNumInviteEvents:
+ _objc_msgSend$setPCountMaxNormalized:
+ _objc_msgSend$setPCountWeightedAverageNormalized:
+ _objc_msgSend$setPCountWeightedSumNormalized:
+ _objc_msgSend$setRsvpStatus:
+ _objc_msgSend$setViewCount:
+ _objc_msgSend$stringForCompoundPredicateType:
+ _objc_msgSend$stringForOperatorType:
+ _objc_msgSend$subpredicates
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updatePredicateType:
+ _objc_msgSend$variable
+ _objc_msgSend$verticalAccuracy
+ _objc_msgSend$viewCount
+ _predicateForRemovingDuplicates
+ momentsDaemonDefaults.onceToken
+ momentsDaemonDefaults.shared
- +[BMPersonalizedSensingMomentsContextDimension(PersonalizedSensing) toBiome:]
- +[BMPersonalizedSensingMomentsContextMomentsContext(PersonalizedSensing) toBiome:]
- +[BMPersonalizedSensingMomentsContextMomentsContextString(PersonalizedSensing) toBiome:]
- +[MOAssetProperty supportsSecureCoding]
- +[MOClusteringUtility getTheBestPersonRelationtshipTagFor:]
- +[MOClusteringUtility getTheBestPersonRelationtshipTagFor:].cold.1
- +[MOClusteringUtility getTheBestPersonRelationtshipTagFor:].cold.2
- +[MOContext(ContextHistoryManager) getMetadataBitmapWithContext:]
- +[MOEventExtendedAttributes lowerCaseArrayOfStrings:]
- +[MOEventExtendedAttributes supportsSecureCoding]
- +[MOPublicEvent supportsSecureCoding]
- -[MOAssetProperty .cxx_destruct]
- -[MOAssetProperty copyWithZone:]
- -[MOAssetProperty description]
- -[MOAssetProperty encodeWithCoder:]
- -[MOAssetProperty favorite]
- -[MOAssetProperty initWithCoder:]
- -[MOAssetProperty initWithLocalToPhotoLibraryIdentifier:location:mediaType:mediaSubtypes:favorite:]
- -[MOAssetProperty localToPhotoLibraryIdentifier]
- -[MOAssetProperty location]
- -[MOAssetProperty mediaSubtypes]
- -[MOAssetProperty mediaType]
- -[MOAssetProperty setFavorite:]
- -[MOAssetProperty setLocalToPhotoLibraryIdentifier:]
- -[MOAssetProperty setLocation:]
- -[MOAssetProperty setMediaSubtypes:]
- -[MOAssetProperty setMediaType:]
- -[MOContextHistoryWriter .cxx_destruct]
- -[MOContextHistoryWriter _saveContextResults:withFetchDetails:options:usingRange:]
- -[MOContextHistoryWriter stream_publisher]
- -[MOContextHistoryWriter stream_source]
- -[MOEventBundle initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:]
- -[MOEventBundle initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:]
- -[MOEventBundle initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:]
- -[MOEventBundleRanking _fillHeuristicsInfoForRanking:forBundle:].cold.3
- -[MOEventBundleRankingInput isSensitivePOI]
- -[MOEventBundleRankingInput peopleCountMaxNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setIsSensitivePOI:]
- -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
- -[MOEventExtendedAttributes .cxx_destruct]
- -[MOEventExtendedAttributes copyWithZone:]
- -[MOEventExtendedAttributes description]
- -[MOEventExtendedAttributes encodeWithCoder:]
- -[MOEventExtendedAttributes hash]
- -[MOEventExtendedAttributes initWithCoder:]
- -[MOEventExtendedAttributes initWithLocalIdentifier:]
- -[MOEventExtendedAttributes initWithLocalIdentifier:].cold.1
- -[MOEventExtendedAttributes initWithMoment:]
- -[MOEventExtendedAttributes isEqual:]
- -[MOEventExtendedAttributes momentPropertyOfAssets]
- -[MOEventExtendedAttributes photoMomentHolidays]
- -[MOEventExtendedAttributes photoMomentInferences]
- -[MOEventExtendedAttributes photoMomentLocalIdentifier]
- -[MOEventExtendedAttributes photoMomentPersons]
- -[MOEventExtendedAttributes photoMomentPublicEvents]
- -[MOEventExtendedAttributes setMomentPropertyOfAssets:]
- -[MOEventExtendedAttributes setPhotoMomentHolidays:]
- -[MOEventExtendedAttributes setPhotoMomentInferences:]
- -[MOEventExtendedAttributes setPhotoMomentLocalIdentifier:]
- -[MOEventExtendedAttributes setPhotoMomentPersons:]
- -[MOEventExtendedAttributes setPhotoMomentPublicEvents:]
- -[MOEventFetchOptions category]
- -[MOEventFetchOptions initWithDateInterval:ascending:category:limit:]
- -[MOPlace initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:]
- -[MOPlace initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:]
- -[MOPlace initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:]
- -[MOPublicEvent .cxx_destruct]
- -[MOPublicEvent copyWithZone:]
- -[MOPublicEvent description]
- -[MOPublicEvent encodeWithCoder:]
- -[MOPublicEvent initWithCoder:]
- -[MOPublicEvent initWithEventDictionary:]
- -[MOPublicEvent initWithEventDictionary:].cold.1
- -[MOPublicEvent initWithName:performers:venue:]
- -[MOPublicEvent name]
- -[MOPublicEvent performers]
- -[MOPublicEvent setName:]
- -[MOPublicEvent setPerformers:]
- -[MOPublicEvent setVenue:]
- -[MOPublicEvent venue]
- -[PersonalizedSensingServiceDelegate clientConnection:hasEntitlement:]
- -[PersonalizedSensingServiceDelegate listener:shouldAcceptNewConnection:].cold.1
- -[PersonalizedSensingServiceDelegate listener:shouldAcceptNewConnection:].cold.2
- /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOClusteringUtility.o
- /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOEventExtendedAtrributes.o
- GCC_except_table106
- GCC_except_table3
- GCC_except_table31
- GCC_except_table36
- GCC_except_table51
- MOClusteringUtility.m
- MOEventExtendedAtrributes.m
- OBJC_IVAR_$_MOAssetProperty._favorite
- OBJC_IVAR_$_MOAssetProperty._localToPhotoLibraryIdentifier
- OBJC_IVAR_$_MOAssetProperty._location
- OBJC_IVAR_$_MOAssetProperty._mediaSubtypes
- OBJC_IVAR_$_MOAssetProperty._mediaType
- OBJC_IVAR_$_MOContextHistoryWriter._stream_publisher
- OBJC_IVAR_$_MOContextHistoryWriter._stream_source
- OBJC_IVAR_$_MOEventBundleRankingInput._isSensitivePOI
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
- OBJC_IVAR_$_MOEventExtendedAttributes._momentPropertyOfAssets
- OBJC_IVAR_$_MOEventExtendedAttributes._photoMomentHolidays
- OBJC_IVAR_$_MOEventExtendedAttributes._photoMomentInferences
- OBJC_IVAR_$_MOEventExtendedAttributes._photoMomentLocalIdentifier
- OBJC_IVAR_$_MOEventExtendedAttributes._photoMomentPersons
- OBJC_IVAR_$_MOEventExtendedAttributes._photoMomentPublicEvents
- OBJC_IVAR_$_MOEventFetchOptions._category
- OBJC_IVAR_$_MOPublicEvent._name
- OBJC_IVAR_$_MOPublicEvent._performers
- OBJC_IVAR_$_MOPublicEvent._venue
- _BiomeLibrary
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContext
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContextContextFetchDetails
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContextDimension
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContextMomentsContext
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContextMomentsContextFetchOptions
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContextMomentsContextString
- _OBJC_CLASS_$_BMPersonalizedSensingMomentsContextPersonalizedContext
- _OBJC_CLASS_$_MOAssetProperty
- _OBJC_CLASS_$_MOClusteringUtility
- _OBJC_CLASS_$_MOPublicEvent
- _OBJC_METACLASS_$_MOAssetProperty
- _OBJC_METACLASS_$_MOClusteringUtility
- _OBJC_METACLASS_$_MOEventExtendedAttributes
- _OBJC_METACLASS_$_MOPublicEvent
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1161
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1163
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1163.cold.1
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1385
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.135
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.135.cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.138
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.138.cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.141
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.141.cold.1
- __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.943
- __63-[MOContextManager _generateContextWithOption:request:handler:]_block_invoke.115
- __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.128
- __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.128.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1119
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1124
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke_3.cold.1
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1149
- __OBJC_$_CATEGORY_BMPersonalizedSensingMomentsContextDimension_$_PersonalizedSensing
- __OBJC_$_CATEGORY_BMPersonalizedSensingMomentsContextMomentsContextString_$_PersonalizedSensing
- __OBJC_$_CATEGORY_BMPersonalizedSensingMomentsContextMomentsContext_$_PersonalizedSensing
- __OBJC_$_CATEGORY_CLASS_METHODS_BMPersonalizedSensingMomentsContextDimension_$_PersonalizedSensing
- __OBJC_$_CATEGORY_CLASS_METHODS_BMPersonalizedSensingMomentsContextMomentsContextString_$_PersonalizedSensing
- __OBJC_$_CATEGORY_CLASS_METHODS_BMPersonalizedSensingMomentsContextMomentsContext_$_PersonalizedSensing
- __OBJC_$_CLASS_METHODS_MOAssetProperty
- __OBJC_$_CLASS_METHODS_MOClusteringUtility
- __OBJC_$_CLASS_METHODS_MOContext(MOContextMO|ContextHistoryManager)
- __OBJC_$_CLASS_METHODS_MOEventExtendedAttributes
- __OBJC_$_CLASS_METHODS_MOPublicEvent
- __OBJC_$_CLASS_PROP_LIST_MOAssetProperty
- __OBJC_$_CLASS_PROP_LIST_MOEventExtendedAttributes
- __OBJC_$_CLASS_PROP_LIST_MOPublicEvent
- __OBJC_$_INSTANCE_METHODS_MOAssetProperty
- __OBJC_$_INSTANCE_METHODS_MOContext(MOContextMO|ContextHistoryManager)
- __OBJC_$_INSTANCE_METHODS_MOEventExtendedAttributes
- __OBJC_$_INSTANCE_METHODS_MOPublicEvent
- __OBJC_$_INSTANCE_VARIABLES_MOAssetProperty
- __OBJC_$_INSTANCE_VARIABLES_MOContextHistoryWriter
- __OBJC_$_INSTANCE_VARIABLES_MOEventExtendedAttributes
- __OBJC_$_INSTANCE_VARIABLES_MOPublicEvent
- __OBJC_$_PROP_LIST_MOAssetProperty
- __OBJC_$_PROP_LIST_MOContextHistoryWriter
- __OBJC_$_PROP_LIST_MOEventExtendedAttributes
- __OBJC_$_PROP_LIST_MOPublicEvent
- __OBJC_CLASS_PROTOCOLS_$_MOAssetProperty
- __OBJC_CLASS_PROTOCOLS_$_MOEventExtendedAttributes
- __OBJC_CLASS_PROTOCOLS_$_MOPublicEvent
- __OBJC_CLASS_RO_$_MOAssetProperty
- __OBJC_CLASS_RO_$_MOClusteringUtility
- __OBJC_CLASS_RO_$_MOEventExtendedAttributes
- __OBJC_CLASS_RO_$_MOPublicEvent
- __OBJC_METACLASS_RO_$_MOAssetProperty
- __OBJC_METACLASS_RO_$_MOClusteringUtility
- __OBJC_METACLASS_RO_$_MOEventExtendedAttributes
- __OBJC_METACLASS_RO_$_MOPublicEvent
- ___59+[MOClusteringUtility getTheBestPersonRelationtshipTagFor:]_block_invoke
- __block_literal_global.134
- __block_literal_global.137
- __block_literal_global.140
- __block_literal_global.143
- __block_literal_global.146
- __block_literal_global.1505
- __os_feature_enabled_impl
- _kMOBundleClusterMetadatasubSuggestionIDsBeforePruning
- _kMOEmbeddingDistanceWeightTimeContextFromPhotoTraits
- _kMOEmbeddingPersonRelationshipScoreThresholdForChild
- _kMOEmbeddingPersonRelationshipScoreThresholdForCoworker
- _kMOEmbeddingPersonRelationshipScoreThresholdForFamily
- _kMOEmbeddingPersonRelationshipScoreThresholdForFriend
- _kMOEmbeddingPersonRelationshipScoreThresholdForMyPet
- _kMOEmbeddingPhotoTraitRankedListForActivityTypes
- _kMOEmbeddingPhotoTraitRankedListForOtherSubjects
- _kMOEmbeddingPhotoTraitRankedListForPlaceTypes
- _kMOEmbeddingPhotoTraitRankedListForSocialEvents
- _kMOEmbeddingPhotoTraitRankedListForTimeContexts
- _kMOKeyEventUniversalDateInterval
- _kMOKeyEvents
- _kMOKeyHolidays
- _kMOKeyInferences
- _kMOKeyLocalIdentifier
- _kMOKeyName
- _kMOKeyPerformers
- _kMOKeyPersons
- _kMOKeyPublicEvents
- _kMOKeyVenue
- _kMOTimeContextEmbeddingTimeContextFromPhotoTraits
- _objc_msgSend$MomentsContext
- _objc_msgSend$PersonalizedSensing
- _objc_msgSend$_saveContextResults:withFetchDetails:options:usingRange:
- _objc_msgSend$alternateClientIdentifier
- _objc_msgSend$clientBundleIdentifier
- _objc_msgSend$clientConnection:hasEntitlement:
- _objc_msgSend$favorite
- _objc_msgSend$fetchId
- _objc_msgSend$generativeModelsAvailabilityStatus
- _objc_msgSend$initWithArray:copyItems:
- _objc_msgSend$initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:
- _objc_msgSend$initWithContextIdentifier:contextStrings:contextCreationTimestamp:associatedPatternType:metadataContentBitmap:
- _objc_msgSend$initWithDateInterval:ascending:category:limit:
- _objc_msgSend$initWithEventDictionary:
- _objc_msgSend$initWithFetchDetails:fetchOptions:contexts:
- _objc_msgSend$initWithFetchId:timestamp:clientBundleIdentifier:alternateClientIdentifier:totalContextReplyCount:batchContextReplyStartIndex:
- _objc_msgSend$initWithIdentifier:name:relevantAssetUUIDs:
- _objc_msgSend$initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:
- _objc_msgSend$initWithLocalIdentifier:
- _objc_msgSend$initWithLocalToPhotoLibraryIdentifier:location:mediaType:mediaSubtypes:favorite:
- _objc_msgSend$initWithName:performers:venue:
- _objc_msgSend$initWithName:queries:
- _objc_msgSend$initWithPersonDictionary:
- _objc_msgSend$initWithPersonalizedContext:
- _objc_msgSend$initWithTextString:stringIdentifier:dimensions:
- _objc_msgSend$invalidate
- _objc_msgSend$isSensitivePOI
- _objc_msgSend$localToPhotoLibraryIdentifier
- _objc_msgSend$lowerCaseArrayOfStrings:
- _objc_msgSend$mediaSubtypes
- _objc_msgSend$momentPropertyOfAssets
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$performers
- _objc_msgSend$photoMomentHolidays
- _objc_msgSend$photoMomentInferences
- _objc_msgSend$photoMomentLocalIdentifier
- _objc_msgSend$photoMomentPersons
- _objc_msgSend$photoMomentPublicEvents
- _objc_msgSend$publisher
- _objc_msgSend$sendEvent:
- _objc_msgSend$setIsSensitivePOI:
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
- _objc_msgSend$stream_source
- _objc_msgSend$toBiome:
- _objc_msgSend$totalContextReplyCount
- _objc_msgSend$unsignedIntegerValue
- _objc_msgSend$unsignedLongValue
- _objc_msgSend$venue
CStrings:
+ "!="
+ "#bundlecuration, filtered bundle. reason: coarse granularity summary.bundleID %@, interfaceType %lu, subType %lu, summarizationGranularity %lu, isSensitive %lu"
+ "(rankingCategory,visibilityCategory) were updated from (%lu,%lu) to (%lu,%lu) because it's part of thematic summary: bundleID %@, suggestionID %@, bundleSubType %lu"
+ "<"
+ "<="
+ "<MOEventBundle bundleIdentifier, %@, suggestionID, %@, sub Suggestion IDs, %@, startDate, %@, endDate, %@, creationDate, %@, firstCreationDate, %@, interfaceType, %lu, bundleSubType, %lu, bundleSuperType, %lu, filtered, %@, agg./suppressed, %@, sum. granularity, %lu, includedInSummaryOnly, %@, promptLanguage, %@, photoSource, %lu, action, %@, concurrentMediaAction, %@, place, %@, time, %@, sub bundle IDs, %@, labels, %@, rankingVisibilityCategoryForUI, %@, rankingBundleGoodnessScore, %@ >"
+ "<MOPhotoTrait localIdentifier, %@, name, %@, labelType, %@, holidayIdentifier, %@, meaningIdentifier, %@, relevantAssetUUIDs, %@, associatedPersonLocalIdentifiers, %@,>"
+ "<MOPlace identifier, %@, name, %@, confidence, %f, placeType, %lu, placeUserType, %lu, categoryMuid, %@, locationMode, %lu, distanceToHomeInMiles, %f, poiCategory, %@, familiarityIndexLOI, %f>"
+ "<MOResource identifier, %@, name, %@, type, %lu, assets, %@, photoAssetCloudIdentifier, %@, data.length, %lu, value, %f"
+ "=="
+ ">="
+ "@\"MOEventInvite\""
+ "@104@0:8@16@24Q32@40@48d56d64@72Q80Q88@96"
+ "@120@0:8@16@24Q32Q40@48Q56@64@72d80d88d96@104@112"
+ "@136@0:8@16@24@32Q40Q48@56Q64@72@80d88d96d104d112@120@128"
+ "@204@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148@156@164@172@180@188@196"
+ "@252@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232@240B248"
+ "@272@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232B240Q244Q252@260B268"
+ "@288@0:8@16@24@32@40@48@56@64@72B80Q84Q92@100Q108@116@124@132@140@148@156@164@172@180@188@196Q204@212B220Q224@232@240@248B256Q260Q268@276B284"
+ "@40@0:8@16@24Q32"
+ "@44@0:8@16B24@28@36"
+ "@48@0:8Q16@24@32@40"
+ "@56@0:8@16@24@32@40Q48"
+ "@64@0:8Q16@24@32@40@48d56"
+ "@96@0:8@16Q24Q32@40Q48@56@64d72d80d88"
+ "AND"
+ "Activity"
+ "ActivityMetaData activityType,%@"
+ "Aggregate Expression (Array of expressions)"
+ "B32@0:8@16d24"
+ "BEGINSWITH"
+ "BETWEEN"
+ "BusinessContact"
+ "CONTAINS"
+ "Christmas Day"
+ "Christmas Eve"
+ "Cinco De Mayo"
+ "Compound Predicate Type: %@"
+ "Constant Value: %@"
+ "Context cross platform persistency sync unavailable"
+ "Diwali"
+ "Dynamic model parameter is not set for bundleInterfaceType %lu. Setting it to zero"
+ "ENDSWITH"
+ "Earth Day"
+ "Elliptical"
+ "Evaluated Object (self reference)"
+ "F"
+ "Filter sorted bundles by recommended visibility, count: %@"
+ "Fridays"
+ "Function Arguments:"
+ "Function: %@"
+ "Hosting at Home"
+ "IN"
+ "Independence Day_US"
+ "InterestingLocation"
+ "Invite"
+ "Invite Event"
+ "Key Path: %@"
+ "L"
+ "LIKE"
+ "Labor Day"
+ "Left Expression: %@"
+ "Location"
+ "Lowering rank of suggestion: %@, from value: %@ to value: %@"
+ "M"
+ "MOContextPredicate"
+ "MOContextPredicateBuilder"
+ "MOEventInvite"
+ "MOInvitePerson"
+ "MOMetaDataCurationUtility"
+ "MOPhotoResourceICloudIdentifier"
+ "Memorial Day"
+ "Mondays"
+ "N"
+ "NOT"
+ "No arguments for function"
+ "No personalRelationship is available for person %{private}@"
+ "None of personalRelationships are confident enough to generate the best relationship tag for person %{private}@"
+ "OR"
+ "Operator Type: %@"
+ "PSService, authorizedTypes,%@"
+ "PSService, context retrieval entitlement check failed"
+ "PSService,context retrieval entitlementCheck,arrayEntriesCount,%d"
+ "PSService,entitlementCheck,dataAccessEntitlements,%@"
+ "PSService,entitlementCheck,entry,%@,hasEntitlementForNLData,%d,hasEntitlementForStructuredData,%d"
+ "PSService,fetchContextWithOptions"
+ "PSService,personalized context entitlementCheck,arrayEntriesCount,%d"
+ "PhotoAssetCloudIdentifier"
+ "Photos at Home"
+ "Q28@0:8@16B24"
+ "RankingDict count for birthday bundles %lu"
+ "RankingDict count for holiday bundles %lu"
+ "Right Expression: %@"
+ "Running"
+ "S"
+ "Saturdays"
+ "Sensitive bundle count in top 5: %@"
+ "Sensitive bundle found during ranking: %@"
+ "SensitiveLocation"
+ "Setting thematic summary visibility status to Recommended only: bundleID %@, suggestionID %@"
+ "Sort bundles by ranking score for sensitivity handling, count: %@"
+ "Spotlight"
+ "StrengthTraining"
+ "Suggestion was already viewed (viewCount=%lu). Use DecayRateAfterViewed (rate=%.3f)"
+ "Suggestion's not viewed yet. Use default decayRate (rate=%.3f)"
+ "Sundays"
+ "T@\"CLLocation\",&,N,V_inviteEventLocation"
+ "T@\"CLLocation\",R,N,V_location"
+ "T@\"MOEventInvite\",&,N,V_inviteEvent"
+ "T@\"NSArray\",&,N,V_inviteEventAttendees"
+ "T@\"NSArray\",&,N,V_inviteEventOrganizers"
+ "T@\"NSArray\",&,N,V_phenotypePersonUUIDs"
+ "T@\"NSArray\",C,N,V_associatedPersonLocalIdentifiers"
+ "T@\"NSArray\",R,N,V_categories"
+ "T@\"NSData\",&,V_fetchRequestPredicate"
+ "T@\"NSDictionary\",&,N,V_celebrationHistogram"
+ "T@\"NSDictionary\",&,N,V_holidayHistogram"
+ "T@\"NSDictionary\",&,N,V_stateOfMindValenceHistogram"
+ "T@\"NSDictionary\",&,V_filterCriteriaMap"
+ "T@\"NSNumber\",&,N,V_categoryMuid"
+ "T@\"NSSet\",&,V_metadataTypes"
+ "T@\"NSString\",&,N,V_displayName"
+ "T@\"NSString\",&,N,V_holidayIdentifier"
+ "T@\"NSString\",&,N,V_inviteEventPlaceName"
+ "T@\"NSString\",&,N,V_inviteEventTitle"
+ "T@\"NSString\",&,N,V_labelType"
+ "T@\"NSString\",&,N,V_meaningIdentifier"
+ "T@\"NSString\",&,N,V_rsvpStatus"
+ "T@\"NSString\",R,&,N,V_photoAssetCloudIdentifier"
+ "TB,N,V_containsOrganizationContact"
+ "TB,N,V_hasLocation"
+ "TB,N,V_inviteEventIsAllDay"
+ "TB,N,V_isBusinessContact"
+ "TB,N,V_isMe"
+ "TB,N,V_isSensitive"
+ "TB,N,V_isSensitiveLocation"
+ "TQ,N,V_batchSize"
+ "TQ,N,V_numBirthdayAssets"
+ "TQ,N,V_numHolidayAssets"
+ "TQ,N,V_numInviteEvents"
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "Tf,N,V_viewCount"
+ "Thanksgiving_CA"
+ "Thanksgiving_US"
+ "Thematic summary gotgot rejected due to engagement signal: bundleID %@, suggestionID %@, isBundleOrSubBundlesSelectedOrQuickAdded %d, isBundleOrSubBundleDeleted %d"
+ "Thursdays"
+ "Time"
+ "Time at Home"
+ "Tuesdays"
+ "UNKNOWN"
+ "UninterestingLocation"
+ "Unknown expression type"
+ "Unknown predicate type: %@"
+ "Updating ranking dict for birthday, num assests: %@"
+ "Updating ranking dict for holiday, num assests: %@"
+ "V"
+ "Variable: %@"
+ "Walking"
+ "Wednesdays"
+ "XPCFetchContextForPinning"
+ "Yoga"
+ "_activityStringFromEnum:"
+ "_addMetaDataToContextForRetrieval:bundleContent:authorizedTypes:"
+ "_associatedPersonLocalIdentifiers"
+ "_batchSize"
+ "_bundleTypeFromContextType:"
+ "_categories"
+ "_categoryMuid"
+ "_celebrationHistogram"
+ "_containsOrganizationContact"
+ "_createContextsWithBundleContents:"
+ "_createContextsWithBundleContents:authorizedTypes:"
+ "_fetchContextWithOption"
+ "_fetchContextWithOption:predicates:authorizedTypes:handler:"
+ "_fetchRequestPredicate"
+ "_filterCriteriaMap"
+ "_filterExtractedBundles:contextPredicate:withHandler:"
+ "_hasLocation"
+ "_holidayHistogram"
+ "_holidayIdentifier"
+ "_inviteEvent"
+ "_inviteEventAttendees"
+ "_inviteEventIsAllDay"
+ "_inviteEventLocation"
+ "_inviteEventOrganizers"
+ "_inviteEventPlaceName"
+ "_inviteEventTitle"
+ "_isBusinessContact"
+ "_isMe"
+ "_isSensitive"
+ "_isSensitiveLocation"
+ "_labelType"
+ "_meaningIdentifier"
+ "_metadataTypes"
+ "_numBirthdayAssets"
+ "_numHolidayAssets"
+ "_numInviteEvents"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "_phenotypePersonUUIDs"
+ "_photoAssetCloudIdentifier"
+ "_replacePredicate:forKeyPath:withNewKeyPath:newValue:comparisonType:"
+ "_retrieveContextWithOption:predicate:authorizedTypes:handler:"
+ "_rsvpStatus"
+ "_stateOfMindValenceHistogram"
+ "_viewCount"
+ "add activityMetaData metadata: %@"
+ "afternoons"
+ "allowEvaluation"
+ "altitude"
+ "arguments"
+ "ascending, %@,  startDate, %@, endDate, %@, categories, %@, limit, %@"
+ "associatedPersonLocalIdentifiers"
+ "batchSize"
+ "bundle content after extraction: %@"
+ "bundleCategoryMuid"
+ "categoryMuid"
+ "celebration"
+ "celebrationHistogram"
+ "clientConnection:cacheContextRetrievalEntitlement:"
+ "clientConnection:cachePersonalizedContextEntitlement:"
+ "collection"
+ "com.apple.personalized-sensing-service.data-access"
+ "comparisonPredicateModifier"
+ "compoundPredicateType"
+ "constantValue"
+ "containsOrganizationContact"
+ "contents count before filtering, %lu"
+ "contextLocation,(%f,%f),targetLocation,(%f,%f),distance,%f"
+ "contextPredicateForContextType:withMetadata:startDate:endDate:"
+ "contextPredicateForContextType:withMetadata:startDate:endDate:aroundLocation:withDistanceThreshold:"
+ "contextType"
+ "contextType from predicate %@"
+ "contextType,%@,bundletype,%@"
+ "convertNSNumberToContactType:"
+ "convertNSNumberToRoadType:"
+ "convertNSNumberToSensitiveLocationType:"
+ "convertNSNumberToUninterestingLocationType:"
+ "coordinate"
+ "createAndPredicate:"
+ "createNotPredicate:"
+ "createOrPredicate:"
+ "createPredicateForValue:inCollection:"
+ "createPredicateWithLeftExpression:rightExpression:operation:"
+ "criteriaMap"
+ "currentHandler"
+ "dataAccessEntitlements"
+ "decayRateAfterViewed"
+ "deserializeCLLocationObject:"
+ "deserializedContextPredicateData, %@"
+ "deserializedfetchRequestPredicate, %@"
+ "deserializing context predicate failed"
+ "disassemblePredicate:"
+ "displayName, %@"
+ "distanceFromLocation"
+ "distanceThreshold,%f"
+ "embeddingDistWeight_celebration"
+ "embeddingDistWeight_holiday"
+ "embeddingDistWeight_stateOfMindContext"
+ "embeddingDistWeight_stateOfMindDomains"
+ "embeddingDistWeight_stateOfMindLabels"
+ "embeddingDistWeight_stateOfMindValence"
+ "evenings"
+ "eventCategoryMuid"
+ "eventRoutineEventCategoryMuid"
+ "expressionForConstantValue:"
+ "expressionForKeyPath:"
+ "expressionType"
+ "extractContentsFromBundlesWithBundlePredicate:contextPredicate:handler:"
+ "extractFirstValueForKeyPath:fromPredicates:"
+ "fetchContextWithOptions:predicates:authorizedTypes:withReply:"
+ "fetchEventBundlesWithPredicate, fetchError, %@"
+ "fetchEventBundlesWithPredicate, fetched eventBundle count, %lu"
+ "fetchEventBundlesWithPredicate:handler:"
+ "fetchRequestPredicate"
+ "filterCriteriaMap"
+ "filterResults, after count %lu"
+ "filterResults, before count %lu"
+ "filterResults:withCriteria:"
+ "function"
+ "getPersonFromBirthdayPhotoTrait:eventBundle:"
+ "getTheBestPersonRelationtshipTagFor:useRelationshipInference:"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "hasLocation"
+ "holiday"
+ "holidayHistogram"
+ "holidayIdentifier"
+ "horizontalAccuracy"
+ "initWithActivityType:"
+ "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:"
+ "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:isSensitive:"
+ "initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:"
+ "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:"
+ "initWithDateInterval:ascending:categories:limit:"
+ "initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:holidayHistogram:celebrationHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:stateOfMindValenceHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:phenotypePersonUUIDs:"
+ "initWithIdentifier:name:labelType:holidayIdentifier:meaningIdentifier:relevantAssetUUIDs:associatedPersonLocalIdentifiers:"
+ "initWithIdentifier:name:labelType:holidayIdentifier:relevantAssetUUIDs:"
+ "initWithIdentifier:name:type:assets:data:value:priorityScore:photoCurationScore:photoFaceCount:photoAssetMediaType:photoAssetCloudIdentifier:"
+ "initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:"
+ "initWithInt:"
+ "initWithLatitude:longitude:"
+ "initWithName:type:photoAssetCloudIdentifier:"
+ "initWithPlace:city:location:"
+ "initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:"
+ "initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:"
+ "initWithPredicate:filter:metadataTypes:"
+ "initWithStartDate:endDate:timeReferenceString:"
+ "inspectExpression:"
+ "interactionScoredContact identifier, %@, interactionGroupName, %@, interactionContact count, %lu, interaction count, %lu, interactionMechanisms, %@, contain organization , %d"
+ "invite event title, %@"
+ "inviteEvent"
+ "inviteEventAttendees"
+ "inviteEventIsAllDay"
+ "inviteEventLocation"
+ "inviteEventOrganizers"
+ "inviteEventPlaceName"
+ "inviteEventTitle"
+ "invitePersonDisplayName"
+ "invitePersonIsMe"
+ "invitePersonRSVPStatus"
+ "isBusinessContact"
+ "isEligibleForTransitBundleSummarization"
+ "isExtendedLogEnabled:forDetaultsManager:"
+ "isInThematicSummary"
+ "isMe"
+ "isSensitive"
+ "isSensitive == NO"
+ "isSensitive == YES"
+ "isSensitiveLocation"
+ "isWithinDistanceFromLocation:maxDistance:"
+ "keyPath"
+ "labelType"
+ "leftExpression"
+ "location decoding failed, %@"
+ "maxDistance"
+ "maxNumOfBirthdayBundlesPerDay"
+ "maxNumOfHolidayBundlesPerDay"
+ "meaning"
+ "meaningIdentifier"
+ "metadataTypes"
+ "midnights"
+ "momentsDaemonDefaults"
+ "mornings"
+ "nights"
+ "no content is extracted for predicate with contextType"
+ "notPredicateWithSubpredicate:"
+ "numBirthdayAssets"
+ "numHolidayAssets"
+ "numInviteEvents"
+ "personalized_reflection"
+ "personalized_reflection_activity"
+ "personalized_reflection_contact"
+ "personalized_reflection_outing"
+ "phenotypePersonUUIDs"
+ "photoAssetCloudIdentifier"
+ "place, %@, city, %@, location %{sensitive}@"
+ "placeName, %@, confidence, %f, locationMode, %@, new place, %lu, isHighConfidence, %d, isInvalid, %d, isPreOnboardedVisit, %d, poiCategory, %@, categoryMuid, %@, placeSource, %lu, placeType, %@, mapItemPlaceType, %@, userType, %lu, predominantWeather %@,familiarityIndexLOI, %.2f, mapItem, %lu"
+ "predicateFormat"
+ "predicateOperatorFromType:"
+ "predicateOperatorType"
+ "predicateWithLeftExpression:rightExpression:modifier:type:options:"
+ "requestPredicate"
+ "retrieveContextWithOption:predicates:authorizedTypes:handler:"
+ "rightExpression"
+ "rsvpStatus"
+ "selectBirthdayFromPhotoTraits:"
+ "selectHolidayFromPhotoTraits:"
+ "sensitiveOnRecommendedThreshold"
+ "serializeCLLocationObject"
+ "set"
+ "setAssociatedPersonLocalIdentifiers:"
+ "setBatchSize:"
+ "setCategoryMuid:"
+ "setCelebrationHistogram:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setContainsOrganizationContact:"
+ "setEntitlementsForDataAccess:"
+ "setFetchRequestPredicate:"
+ "setFilterCriteriaMap:"
+ "setHasLocation:"
+ "setHolidayHistogram:"
+ "setHolidayIdentifier:"
+ "setInviteEvent:"
+ "setInviteEventAttendees:"
+ "setInviteEventIsAllDay:"
+ "setInviteEventLocation:"
+ "setInviteEventOrganizers:"
+ "setInviteEventPlaceName:"
+ "setInviteEventTitle:"
+ "setIsBusinessContact:"
+ "setIsMe:"
+ "setIsSensitive:"
+ "setIsSensitiveLocation:"
+ "setLabelType:"
+ "setMeaningIdentifier:"
+ "setMetadataTypes:"
+ "setNumBirthdayAssets:"
+ "setNumHolidayAssets:"
+ "setNumInviteEvents:"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
+ "setPhenotypePersonUUIDs:"
+ "setPhotoAssetCloudIdentifier:"
+ "setRsvpStatus:"
+ "setStateOfMindValenceHistogram:"
+ "setViewCount:"
+ "shortDescription"
+ "stateOfMindDomains"
+ "stateOfMindLabels"
+ "stateOfMindValence"
+ "stateOfMindValenceHistogram"
+ "stringForCompoundPredicateType:"
+ "stringForOperatorType:"
+ "subpredicates"
+ "targetLocation"
+ "thematic_summary"
+ "thematic_summary_common_activity"
+ "thematic_summary_common_place"
+ "thematic_summary_holiday"
+ "thematic_summary_photo_subject"
+ "thematic_summary_social"
+ "thematic_summary_state_of_mind"
+ "timeIntervalSince1970"
+ "timeStringSingularToPluralForm:"
+ "updatePredicateType"
+ "updatePredicateType:"
+ "updating contextType"
+ "useBirthdayLabel"
+ "useHolidayLabel"
+ "v48@0:8@\"MOContextFetchOptions\"16@\"NSArray\"24@\"NSSet\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "variable"
+ "verticalAccuracy"
+ "viewCount"
+ "weekdays"
+ "weekends"
+ "weightBirthdayInclusion"
+ "weightForIsBusinessContact"
+ "weightForSensitivePOI"
+ "weightHolidayInclusion"
+ "weightInviteEventInclusion"
- "#bundlecuration, filtered bundle. reason: coarse granularity summary.bundleID %@, interfaceType %lu, subType %lu, summarizationGranularity %lu"
- "%@, %@"
- "-[MOEventExtendedAttributes initWithLocalIdentifier:]"
- "<MOAssetProperty localToPhotoLibraryIdentifier: %@, location: %@, mediaType: %@, mediaSubtypes: %@, favorite: %@>"
- "<MOEventExtendedAttributes localIdentifier, %@, photoMomentInferences, %@, photoMomentHolidays, %@, photoMomentPublicEvents, %@, photoMomentPersons, %@, momentPropertyOfAssets, %@>"
- "<MOPhotoTrait localIdentifier, %@, name, %@, relevantAssetUUIDs, %@,>"
- "<MOPlace identifier, %@, name, %@, confidence, %f, placeType, %lu, placeUserType, %lu, preposition, %lu, locationMode, %lu, distanceToHomeInMiles, %f, poiCategory, %@, familiarityIndexLOI, %f>"
- "<MOPublicEvent name, %s, performers, %@, venue, %@, >"
- "<MOResource identifier, %@, name, %@, type, %lu, assets, %@, data.length, %lu, value, %f"
- "@\"BMBookmarkablePublisher\""
- "@\"BMSource\""
- "@112@0:8@16@24Q32Q40@48Q56@64d72d80d88@96@104"
- "@128@0:8@16@24@32Q40Q48@56Q64@72d80d88d96d104@112@120"
- "@248@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232@240"
- "@268@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232B240Q244Q252@260"
- "@284@0:8@16@24@32@40@48@56@64@72B80Q84Q92@100Q108@116@124@132@140@148@156@164@172@180@188@196Q204@212B220Q224@232@240@248B256Q260Q268@276"
- "@44@0:8@16B24Q28@36"
- "@52@0:8@16@24q32Q40B48"
- "@88@0:8@16Q24Q32@40Q48@56d64d72d80"
- "Bundle contains sensitive POI: bundleID %@, startDate %@, endDate %@, poiCategory %@"
- "ContextHistoryManager"
- "Dynamic model parameter is not set for bundleInterfaceType %lu (in %s:%d)"
- "Invalid parameter not satisfying: localIdentifier (in %s:%d)"
- "Invalid parameter not satisfying: name"
- "MOAssetProperty"
- "MOClusteringUtility"
- "MOEventExtendedAttributes"
- "MOPersonalizedSensingEnabled"
- "MOPublicEvent"
- "MOSyncPersonalizedSensing"
- "Moments"
- "MomentsContext"
- "No personalRelationship is available for person %@"
- "None of personalRelationships are confident enough to generate the best relationship tag for person %@"
- "PSService, client does not have correct entitlement"
- "PSService,entitlementCheck,arrayEntriesCount,%d"
- "PSService,entitlementCheck,entry,%@,returnValue,%d,hasEntitlementForNLData,%d,hasEntitlementForStructuredData,%d"
- "Personalized Sensing Sync Disabled"
- "PersonalizedSensing"
- "PersonalizedSensingService, client not allowed to establish connection,%@"
- "PhotoDepthEffect"
- "PhotoHDR"
- "PhotoLive"
- "PhotoPanorama"
- "PhotoScreenshot"
- "PlatformInfoOverrideIsSeedBuild"
- "Posted Sync count: %ld"
- "Saved biome events!!!"
- "SpatialOverCapture"
- "SubtypeNone"
- "SubtypeUnknown"
- "Suggestion (recommended only) was rejected since it contains sensitive POI: bundleID %@, suggestionID %@ startDate %@ endDate %@"
- "Suggestion was set to recent only since it contains sensitive POI: bundleID %@, suggestionID %@ startDate %@ endDate %@"
- "T@\"BMBookmarkablePublisher\",R,N,V_stream_publisher"
- "T@\"BMSource\",R,N,V_stream_source"
- "T@\"CLLocation\",&,N,V_location"
- "T@\"NSArray\",&,N,V_momentPropertyOfAssets"
- "T@\"NSArray\",&,N,V_performers"
- "T@\"NSArray\",&,N,V_photoMomentHolidays"
- "T@\"NSArray\",&,N,V_photoMomentInferences"
- "T@\"NSArray\",&,N,V_photoMomentPersons"
- "T@\"NSArray\",&,N,V_photoMomentPublicEvents"
- "T@\"NSString\",&,N,V_localToPhotoLibraryIdentifier"
- "T@\"NSString\",&,N,V_venue"
- "T@\"NSString\",C,N,V_photoMomentLocalIdentifier"
- "TB,N,V_favorite"
- "TB,N,V_isSensitivePOI"
- "TQ,N,V_mediaSubtypes"
- "Tf,N,V_peopleCountMaxNormalized"
- "Tf,N,V_peopleCountWeightedAverageNormalized"
- "Tf,N,V_peopleCountWeightedSumNormalized"
- "Tq,N,V_mediaType"
- "VideoCinematic"
- "VideoHighFrameRate"
- "VideoStreamed"
- "VideoTimelapse"
- "_favorite"
- "_isSensitivePOI"
- "_localToPhotoLibraryIdentifier"
- "_mediaSubtypes"
- "_momentPropertyOfAssets"
- "_peopleCountMaxNormalized"
- "_peopleCountWeightedAverageNormalized"
- "_peopleCountWeightedSumNormalized"
- "_performers"
- "_photoMomentHolidays"
- "_photoMomentInferences"
- "_photoMomentLocalIdentifier"
- "_photoMomentPersons"
- "_photoMomentPublicEvents"
- "_saveContextResults:withFetchDetails:options:usingRange:"
- "_stream_publisher"
- "_stream_source"
- "_venue"
- "alternateClientIdentifier"
- "amusementpark"
- "anniversary"
- "ascending, %@,  startDate, %@, endDate, %@, category, %lu, limit, %@"
- "audio"
- "beaching"
- "birthday"
- "clientBundleIdentifier"
- "clientConnection:hasEntitlement:"
- "climbing"
- "concert"
- "diving"
- "embeddingDistWeight_timeContextFromPhotoTrait"
- "eventUniversalDateInterval"
- "favorite"
- "festival"
- "fetchId"
- "getMetadataBitmapWithContext:"
- "holidays"
- "image"
- "inferences"
- "initWithArray:copyItems:"
- "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:"
- "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:"
- "initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:"
- "initWithContextIdentifier:contextStrings:contextCreationTimestamp:associatedPatternType:metadataContentBitmap:"
- "initWithDateInterval:ascending:category:limit:"
- "initWithEventDictionary:"
- "initWithFetchDetails:fetchOptions:contexts:"
- "initWithFetchId:timestamp:clientBundleIdentifier:alternateClientIdentifier:totalContextReplyCount:batchContextReplyStartIndex:"
- "initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:"
- "initWithLocalIdentifier:"
- "initWithLocalToPhotoLibraryIdentifier:location:mediaType:mediaSubtypes:favorite:"
- "initWithMoment:"
- "initWithName:performers:venue:"
- "initWithName:queries:"
- "initWithPersonalizedContext:"
- "initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:"
- "initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:"
- "initWithTextString:stringIdentifier:dimensions:"
- "interactionScoredContact identifier, %@, interactionGroupName, %@, interactionContact count, %lu, interaction count, %lu, interactionMechanisms, %@"
- "invalidate"
- "isGMSAvailable,%d"
- "isSensitivePOI"
- "localToPhotoLibraryIdentifier"
- "lowerCaseArrayOfStrings:"
- "mediaSubtypes"
- "momentPropertyOfAssets"
- "nightout"
- "numberWithUnsignedInt:"
- "peopleCountMaxNormalized"
- "peopleCountWeightedAverageNormalized"
- "peopleCountWeightedSumNormalized"
- "performers"
- "photoMomentHolidays"
- "photoMomentInferences"
- "photoMomentLocalIdentifier"
- "photoMomentPersons"
- "photoMomentPublicEvents"
- "place, %@, city, %@, visit time window %@"
- "placeName, %@, confidence, %f, locationMode, %@, new place, %lu, isHighConfidence, %d, isInvalid, %d, isPreOnboardedVisit, %d, poiCategory, %@, placeSource, %lu, placeType, %@, mapItemPlaceType, %@, userType, %lu, predominantWeather %@,familiarityIndexLOI, %.2f, mapItem, %lu"
- "publicEvents"
- "publisher"
- "sendEvent:"
- "setFavorite:"
- "setIsSensitivePOI:"
- "setLocalToPhotoLibraryIdentifier:"
- "setMediaSubtypes:"
- "setMomentPropertyOfAssets:"
- "setPeopleCountMaxNormalized:"
- "setPeopleCountWeightedAverageNormalized:"
- "setPeopleCountWeightedSumNormalized:"
- "setPerformers:"
- "setPhotoMomentHolidays:"
- "setPhotoMomentInferences:"
- "setPhotoMomentLocalIdentifier:"
- "setPhotoMomentPersons:"
- "setPhotoMomentPublicEvents:"
- "setVenue:"
- "sportevent"
- "stream_publisher"
- "stream_source"
- "timeContextFromPhotoTraits"
- "toBiome:"
- "totalContextReplyCount"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "v56@0:8@16@24@32{_NSRange=QQ}40"
- "venue"
- "video"
- "wedding"
- "wintersport"

```

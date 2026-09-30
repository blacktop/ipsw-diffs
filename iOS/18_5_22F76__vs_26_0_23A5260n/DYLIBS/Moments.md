## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-206.0.7.0.0
-  __TEXT.__text: 0x4e2e8
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x5cfc
-  __TEXT.__cstring: 0xa940
-  __TEXT.__const: 0x360
-  __TEXT.__oslogstring: 0x495d
-  __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__unwind_info: 0x1098
-  __TEXT.__objc_classname: 0x88d
-  __TEXT.__objc_methname: 0xd76b
-  __TEXT.__objc_methtype: 0x18ca
-  __TEXT.__objc_stubs: 0x7b00
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x24e0
-  __DATA_CONST.__objc_classlist: 0x280
+255.0.0.0.0
+  __TEXT.__text: 0x56a00
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x62f4
+  __TEXT.__cstring: 0xd1ed
+  __TEXT.__const: 0x3d0
+  __TEXT.__oslogstring: 0x4d05
+  __TEXT.__gcc_except_tab: 0x464
+  __TEXT.__unwind_info: 0x1210
+  __TEXT.__objc_classname: 0x8ff
+  __TEXT.__objc_methname: 0xeaaf
+  __TEXT.__objc_methtype: 0x18ce
+  __TEXT.__objc_stubs: 0x82e0
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x31a0
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cf0
+  __DATA_CONST.__objc_selrefs: 0x3018
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x248
-  __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xcce0
-  __AUTH_CONST.__objc_const: 0x9ae0
-  __AUTH_CONST.__objc_intobj: 0x4f8
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_arraydata: 0x378
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0xfe60
+  __AUTH_CONST.__objc_const: 0xa478
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1810
-  __DATA.__objc_ivar: 0x748
-  __DATA.__data: 0xb20
-  __DATA.__bss: 0xe8
+  __AUTH.__objc_data: 0x16d0
+  __DATA.__objc_ivar: 0x7a8
+  __DATA.__data: 0xb98
+  __DATA.__bss: 0xd8
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4E45083-D188-32F7-9267-258EF0E7FF97
-  Functions: 2143
-  Symbols:   7861
-  CStrings:  6275
+  UUID: 9E99BC5C-F963-3C2F-BBA4-4C845486B280
+  Functions: 2310
+  Symbols:   8712
+  CStrings:  7258
 
Symbols:
+ +[MODefaultsManager isExtendedLogEnabled:forDetaultsManager:]
+ +[MODefaultsManager momentsDaemonDefaults]
+ +[MODefaultsManager momentsDaemonDefaults].cold.1
+ +[MOEventBundle convertNSNumberToContactType:]
+ +[MOEventBundle convertNSNumberToRoadType:]
+ +[MOEventBundle convertNSNumberToSensitiveLocationType:]
+ +[MOEventBundle convertNSNumberToUninterestingLocationType:]
+ +[MOEventBundleMetaDataUtility activityPhotoTraitLabelMetadataForThematicSummary:AtHome:]
+ +[MOEventBundleMetaDataUtility buildThematicSummaryMetaDataForEventBundle:]
+ +[MOEventBundleMetaDataUtility combinedPlaceTypeLabelMetadataForThematicSummary:]
+ +[MOEventBundleMetaDataUtility placeTypePhotoTraitLabelMetadataForThematicSummary:]
+ +[MOEventBundleMetaDataUtility setActivityNameForThematicSummaryFromActionName:metaData:keyword:keywordType:]
+ +[MOEventBundleMetaDataUtility setMetaDataForBirthday:metaData:eventBundle:]
+ +[MOEventBundleMetaDataUtility setMetaDataForHoliday:metaData:eventBundle:]
+ +[MOEventBundleMetaDataUtility setMetaDataForInvite:metaData:]
+ +[MOEventInvite supportsSecureCoding]
+ +[MOInvitePerson supportsSecureCoding]
+ +[MOMetaDataCurationUtility getPersonFromBirthdayPhotoTrait:eventBundle:]
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:]
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:]
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:].cold.1
+ +[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:].cold.2
+ +[MOMetaDataCurationUtility selectBirthdayFromPhotoTraits:]
+ +[MOMetaDataCurationUtility selectHolidayFromPhotoTraits:]
+ +[MOPersistenceUtilities isAllowedKeyPathForEventBundle:]
+ +[MOPersistenceUtilities isValidPredicate:]
+ +[MOPersistenceUtilities isValidPredicate:].cold.1
+ +[MOPersistenceUtilities isValidPredicate:].cold.2
+ +[MOPersistenceUtilities validateComparisonPredicate:]
+ +[MOPersistenceUtilities validateCompoundPredicate:]
+ +[MOTime timeStringSingularToPluralForm:]
+ -[MOAnalyticsManager makeNewConnectionWithInterfaceFor:]
+ -[MOAppEngagementReporter makeNewConnectionWithInterfaceFor:]
+ -[MOClusterMetadata celebrationHistogram]
+ -[MOClusterMetadata holidayHistogram]
+ -[MOClusterMetadata initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:holidayHistogram:celebrationHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:stateOfMindValenceHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:phenotypePersonUUIDs:]
+ -[MOClusterMetadata phenotypePersonUUIDs]
+ -[MOClusterMetadata setCelebrationHistogram:]
+ -[MOClusterMetadata setHolidayHistogram:]
+ -[MOClusterMetadata setPhenotypePersonUUIDs:]
+ -[MOClusterMetadata setStateOfMindValenceHistogram:]
+ -[MOClusterMetadata stateOfMindValenceHistogram]
+ -[MOConfiguration makeNewConnectionWithInterfaceFor:]
+ -[MOConnection delegate]
+ -[MOConnection getConnectionName]
+ -[MOConnection setDelegate:]
+ -[MOConnectionManager .cxx_destruct]
+ -[MOConnectionManager _callProxy:usingBlock:onError:]
+ -[MOConnectionManager _callProxyProvider:usingBlock:onError:]
+ -[MOConnectionManager _getActiveConnection]
+ -[MOConnectionManager _getActiveConnection].cold.1
+ -[MOConnectionManager _getActiveConnection].cold.2
+ -[MOConnectionManager _getActiveConnection].cold.3
+ -[MOConnectionManager _getSingleCallHandler:]
+ -[MOConnectionManager _makeConnectionErrorWithReason:]
+ -[MOConnectionManager _postProxy:usingBlock:onError:]
+ -[MOConnectionManager _postProxyProvider:usingBlock:onError:]
+ -[MOConnectionManager callAsyncProxyUsingBlock:onError:]
+ -[MOConnectionManager callSyncProxyUsingBlock:onError:]
+ -[MOConnectionManager dealloc]
+ -[MOConnectionManager delegate]
+ -[MOConnectionManager getAsyncProxyProvider]
+ -[MOConnectionManager getConnectionName]
+ -[MOConnectionManager getSyncProxyProvider]
+ -[MOConnectionManager initWithName:usingDelegate:]
+ -[MOConnectionManager invalidate]
+ -[MOConnectionManager postAsyncProxyUsingBlock:onError:]
+ -[MOConnectionManager postSyncProxyUsingBlock:onError:]
+ -[MOConnectionManager setDelegate:]
+ -[MOConnectionManager withProxyProvider:proxyHandler:onError:]
+ -[MOConnectionManager withProxyProvider:proxyHandler:onError:].cold.1
+ -[MOContact initWithIdentifier:personId:displayName:isOrganization:]
+ -[MOContact isOrganization]
+ -[MOEngagementHistoryWriter _logEngagementEvent:withContext:]
+ -[MOEngagementHistoryWriter makeNewConnectionWithInterfaceFor:]
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
+ -[MOPromptManager _purgeEventsWithHandler:]
+ -[MOPromptManager fetchEligiblePOICategoriesWithHandler:]
+ -[MOPromptManager fetchEventBundlesWithPredicate:handler:]
+ -[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]
+ -[MOPromptManager generateAvailabilityPredictionsWithHandler:]
+ -[MOPromptManager makeNewConnectionWithInterfaceFor:]
+ -[MOPromptManager setUpNotificationTimerWithFireDate:]
+ -[MOResource initWithIdentifier:name:type:assets:data:value:priorityScore:photoCurationScore:photoFaceCount:photoAssetMediaType:photoAssetCloudIdentifier:]
+ -[MOResource initWithName:type:photoAssetCloudIdentifier:]
+ -[MOResource photoAssetCloudIdentifier]
+ -[MOResource setPhotoAssetCloudIdentifier:]
+ GCC_except_table101
+ GCC_except_table11
+ GCC_except_table2
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table5
+ GCC_except_table7
+ _GEOPOICategoryAmusementPark
+ _GEOPOICategoryAquarium
+ _GEOPOICategoryBakery
+ _GEOPOICategoryBaseball
+ _GEOPOICategoryBasketball
+ _GEOPOICategoryBeach
+ _GEOPOICategoryBeauty
+ _GEOPOICategoryBowling
+ _GEOPOICategoryBrewery
+ _GEOPOICategoryCafe
+ _GEOPOICategoryCampground
+ _GEOPOICategoryCastle
+ _GEOPOICategoryConventionCenter
+ _GEOPOICategoryFairground
+ _GEOPOICategoryFishing
+ _GEOPOICategoryFitnessCenter
+ _GEOPOICategoryFoodMarket
+ _GEOPOICategoryFortress
+ _GEOPOICategoryGoKart
+ _GEOPOICategoryGolf
+ _GEOPOICategoryHiking
+ _GEOPOICategoryHotel
+ _GEOPOICategoryKayaking
+ _GEOPOICategoryLandmark
+ _GEOPOICategoryLibrary
+ _GEOPOICategoryMarina
+ _GEOPOICategoryMiniGolf
+ _GEOPOICategoryMovieTheater
+ _GEOPOICategoryMuseum
+ _GEOPOICategoryMusicVenue
+ _GEOPOICategoryNationalMonument
+ _GEOPOICategoryNationalPark
+ _GEOPOICategoryNightlife
+ _GEOPOICategoryPark
+ _GEOPOICategoryPlanetarium
+ _GEOPOICategoryPlayground
+ _GEOPOICategoryRVPark
+ _GEOPOICategoryRestaurant
+ _GEOPOICategoryRockClimbing
+ _GEOPOICategorySchool
+ _GEOPOICategorySkatePark
+ _GEOPOICategorySkating
+ _GEOPOICategorySkiing
+ _GEOPOICategorySoccer
+ _GEOPOICategorySpa
+ _GEOPOICategoryStadium
+ _GEOPOICategoryStore
+ _GEOPOICategorySurfing
+ _GEOPOICategorySwimming
+ _GEOPOICategoryTennis
+ _GEOPOICategoryTheater
+ _GEOPOICategoryUniversity
+ _GEOPOICategoryVolleyball
+ _GEOPOICategoryWinery
+ _GEOPOICategoryZoo
+ _KIsBundleOrSubBundleDeleted
+ _KIsBundleOrSubBundlesSelectedOrQuickAdded
+ _KIsInThematicSummaryKey
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
+ _MOLogFacilityPatternEmbedding
+ _MOLogFacilityThematicSummarization
+ _MOPhotoResourceICloudIdentifier
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_MOConnectionManager
+ _OBJC_CLASS_$_MOEventInvite
+ _OBJC_CLASS_$_MOInvitePerson
+ _OBJC_CLASS_$_MOMetaDataCurationUtility
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_IVAR_$_MOAnalyticsManager.connectionManager
+ _OBJC_IVAR_$_MOAppEngagementReporter.connectionManager
+ _OBJC_IVAR_$_MOClusterMetadata._celebrationHistogram
+ _OBJC_IVAR_$_MOClusterMetadata._holidayHistogram
+ _OBJC_IVAR_$_MOClusterMetadata._phenotypePersonUUIDs
+ _OBJC_IVAR_$_MOClusterMetadata._stateOfMindValenceHistogram
+ _OBJC_IVAR_$_MOConfiguration.connectionManager
+ _OBJC_IVAR_$_MOConnection._delegate
+ _OBJC_IVAR_$_MOConnection._interruptActive
+ _OBJC_IVAR_$_MOConnectionManager._connectionName
+ _OBJC_IVAR_$_MOConnectionManager._delegate
+ _OBJC_IVAR_$_MOConnectionManager._mo_connection
+ _OBJC_IVAR_$_MOConnectionManager._xpc_connection
+ _OBJC_IVAR_$_MOContact._isOrganization
+ _OBJC_IVAR_$_MOEngagementHistoryWriter.connectionManager
+ _OBJC_IVAR_$_MOEvent._inviteEvent
+ _OBJC_IVAR_$_MOEventBundle._isSensitive
+ _OBJC_IVAR_$_MOEventFetchOptions._categories
+ _OBJC_IVAR_$_MOEventInvite._inviteEventAttendees
+ _OBJC_IVAR_$_MOEventInvite._inviteEventIsAllDay
+ _OBJC_IVAR_$_MOEventInvite._inviteEventLocation
+ _OBJC_IVAR_$_MOEventInvite._inviteEventOrganizers
+ _OBJC_IVAR_$_MOEventInvite._inviteEventPlaceName
+ _OBJC_IVAR_$_MOEventInvite._inviteEventTitle
+ _OBJC_IVAR_$_MOEventRoutine._categoryMuid
+ _OBJC_IVAR_$_MOEventSignificantContact._containsOrganizationContact
+ _OBJC_IVAR_$_MOInvitePerson._displayName
+ _OBJC_IVAR_$_MOInvitePerson._isMe
+ _OBJC_IVAR_$_MOInvitePerson._rsvpStatus
+ _OBJC_IVAR_$_MOPhotoTrait._associatedPersonLocalIdentifiers
+ _OBJC_IVAR_$_MOPhotoTrait._holidayIdentifier
+ _OBJC_IVAR_$_MOPhotoTrait._labelType
+ _OBJC_IVAR_$_MOPhotoTrait._meaningIdentifier
+ _OBJC_IVAR_$_MOPlace._categoryMuid
+ _OBJC_IVAR_$_MOPromptManager.connectionManager
+ _OBJC_IVAR_$_MOPromptManager.moEventBundleClass
+ _OBJC_IVAR_$_MOPromptManager.moEventClass
+ _OBJC_IVAR_$_MOPromptManager.moXpcContextClass
+ _OBJC_IVAR_$_MOResource._photoAssetCloudIdentifier
+ _OBJC_METACLASS_$_MOConnectionManager
+ _OBJC_METACLASS_$_MOEventInvite
+ _OBJC_METACLASS_$_MOInvitePerson
+ _OBJC_METACLASS_$_MOMetaDataCurationUtility
+ __OBJC_$_CLASS_METHODS_MOEventInvite
+ __OBJC_$_CLASS_METHODS_MOInvitePerson
+ __OBJC_$_CLASS_METHODS_MOMetaDataCurationUtility
+ __OBJC_$_CLASS_PROP_LIST_MOEventInvite
+ __OBJC_$_CLASS_PROP_LIST_MOInvitePerson
+ __OBJC_$_INSTANCE_METHODS_MOConnectionManager
+ __OBJC_$_INSTANCE_METHODS_MOEventInvite
+ __OBJC_$_INSTANCE_METHODS_MOInvitePerson
+ __OBJC_$_INSTANCE_VARIABLES_MOConnectionManager
+ __OBJC_$_INSTANCE_VARIABLES_MOEventInvite
+ __OBJC_$_INSTANCE_VARIABLES_MOInvitePerson
+ __OBJC_$_PROP_LIST_MOAnalyticsManager
+ __OBJC_$_PROP_LIST_MOAppEngagementReporter
+ __OBJC_$_PROP_LIST_MOConfiguration
+ __OBJC_$_PROP_LIST_MOConnection
+ __OBJC_$_PROP_LIST_MOConnectionManager
+ __OBJC_$_PROP_LIST_MOEngagementHistoryWriter
+ __OBJC_$_PROP_LIST_MOEventInvite
+ __OBJC_$_PROP_LIST_MOInvitePerson
+ __OBJC_$_PROP_LIST_MOPromptManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MOConnectionManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOConnectionManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_MOConnectionManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MOAnalyticsManager
+ __OBJC_CLASS_PROTOCOLS_$_MOAppEngagementReporter
+ __OBJC_CLASS_PROTOCOLS_$_MOConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_MOEngagementHistoryWriter
+ __OBJC_CLASS_PROTOCOLS_$_MOEventInvite
+ __OBJC_CLASS_PROTOCOLS_$_MOInvitePerson
+ __OBJC_CLASS_PROTOCOLS_$_MOPromptManager
+ __OBJC_CLASS_RO_$_MOConnectionManager
+ __OBJC_CLASS_RO_$_MOEventInvite
+ __OBJC_CLASS_RO_$_MOInvitePerson
+ __OBJC_CLASS_RO_$_MOMetaDataCurationUtility
+ __OBJC_LABEL_PROTOCOL_$_MOConnectionManagerDelegate
+ __OBJC_METACLASS_RO_$_MOConnectionManager
+ __OBJC_METACLASS_RO_$_MOEventInvite
+ __OBJC_METACLASS_RO_$_MOInvitePerson
+ __OBJC_METACLASS_RO_$_MOMetaDataCurationUtility
+ __OBJC_PROTOCOL_$_MOConnectionManagerDelegate
+ ___119-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:handler:]_block_invoke.223
+ ___143-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:respectLearnFromThisApp:handler:]_block_invoke.225
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.29
+ ___39-[MOPromptManager storeEvents:handler:]_block_invoke.208
+ ___39-[MOSuggestionSheetController activate]_block_invoke.173
+ ___39-[MOSuggestionSheetController activate]_block_invoke.177
+ ___42+[MODefaultsManager momentsDaemonDefaults]_block_invoke
+ ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.237
+ ___42-[MOPromptManager dumpDBStateWithHandler:]_block_invoke.258
+ ___42-[MOPromptManager purgeEventsWithHandler:]_block_invoke.240
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke.8
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.34
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.cold.1
+ ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke
+ ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke.236
+ ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke_2
+ ___43-[MOPromptManager bundleEventsWithHandler:]_block_invoke.239
+ ___43-[MOPromptManager runAnalyticsWithHandler:]_block_invoke.241
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.36
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.cold.1
+ ___44-[MOPromptManager collectEventsWithHandler:]_block_invoke.238
+ ___45-[MOConnectionManager _getSingleCallHandler:]_block_invoke
+ ___45-[MOConnectionManager _getSingleCallHandler:]_block_invoke_2
+ ___49-[MOConfiguration isAllowedToPromptResourceType:]_block_invoke.113
+ ___49-[MOConfiguration isAllowedToPromptResourceType:]_block_invoke.113.cold.1
+ ___49-[MOPromptManager analyzeTrendsInEvents:handler:]_block_invoke.242
+ ___50-[MOConfiguration isAllowedToPromptEventCategory:]_block_invoke.110
+ ___50-[MOConfiguration isAllowedToPromptEventCategory:]_block_invoke.110.cold.1
+ ___50-[MOPromptManager fetchEventsWithOptions:handler:]_block_invoke.210
+ ___50-[MOPromptManager printOnboardingStatusAnalytics:]_block_invoke.261
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke.20
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.21
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.cold.1
+ ___53-[MOConnectionManager _postProxy:usingBlock:onError:]_block_invoke
+ ___53-[MOConnectionManager _postProxy:usingBlock:onError:]_block_invoke_2
+ ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.254
+ ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.256
+ ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke_2
+ ___54-[MOPromptManager printSettingValue:withType:handler:]_block_invoke.260
+ ___54-[MOPromptManager scheduleDatabaseUpgradeWithHandler:]_block_invoke.206
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.269
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.269.cold.1
+ ___55-[MOEngagementHistoryWriter logUsageEvent:withContext:]_block_invoke
+ ___55-[MOEngagementHistoryWriter logUsageEvent:withContext:]_block_invoke.8
+ ___55-[MOEngagementHistoryWriter logUsageEvent:withContext:]_block_invoke.8.cold.1
+ ___55-[MOEngagementHistoryWriter logUsageEvent:withContext:]_block_invoke.cold.1
+ ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.219
+ ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.220
+ ___56-[MOPromptManager triggerFeedbackAssistantFlow:handler:]_block_invoke.266
+ ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke
+ ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke.272
+ ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke_2
+ ___57-[MOPromptManager printEvergreenBundlesWithSeed:handler:]_block_invoke.253
+ ___57-[MOPromptManager printEvergreenBundlesWithSeed:handler:]_block_invoke_2
+ ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke
+ ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke.218
+ ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke_2
+ ___60-[MOEventBundle(MOEventBundleSourceType) primarySourceTypes]_block_invoke
+ ___61-[MOConnectionManager _callProxyProvider:usingBlock:onError:]_block_invoke
+ ___61-[MOConnectionManager _postProxyProvider:usingBlock:onError:]_block_invoke
+ ___61-[MOConnectionManager _postProxyProvider:usingBlock:onError:]_block_invoke_2
+ ___61-[MOEngagementHistoryWriter _logEngagementEvent:withContext:]_block_invoke
+ ___61-[MOEngagementHistoryWriter _logEngagementEvent:withContext:]_block_invoke.5
+ ___61-[MOEngagementHistoryWriter _logEngagementEvent:withContext:]_block_invoke.5.cold.1
+ ___61-[MOEngagementHistoryWriter _logEngagementEvent:withContext:]_block_invoke.cold.1
+ ___61-[MOEngagementHistoryWriter logPerformanceEvent:withContext:]_block_invoke
+ ___61-[MOEngagementHistoryWriter logPerformanceEvent:withContext:]_block_invoke.7
+ ___61-[MOEngagementHistoryWriter logPerformanceEvent:withContext:]_block_invoke.7.cold.1
+ ___61-[MOEngagementHistoryWriter logPerformanceEvent:withContext:]_block_invoke.cold.1
+ ___61-[MOPromptManager uploadFeedbackWithDBStateToServer:handler:]_block_invoke.246
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27.cold.1
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.cold.1
+ ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke
+ ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke.267
+ ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke_2
+ ___62-[MOPromptManager refreshEventsWithRefreshVariant:andHandler:]_block_invoke.243
+ ___64-[MOPromptManager getSnapshotDictionaryForAnalyticsWithHandler:]_block_invoke.259
+ ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke
+ ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke.268
+ ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke_2
+ ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke.244
+ ___90+[MOMetaDataCurationUtility getTheBestPersonRelationtshipTagFor:useRelationshipInference:]_block_invoke
+ ___93-[MOAppEngagementReporter didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke
+ ___93-[MOAppEngagementReporter didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke_2
+ ___93-[MOAppEngagementReporter didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke_2.cold.1
+ ___block_descriptor_32_e15_B32?0816^B24l
+ ___block_descriptor_40_e8_32bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8
+ ___block_descriptor_40_e8_32s_e24_16?0?<v?"NSError">8ls32l8
+ ___block_descriptor_40_e8_32s_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40r_e38_v16?0"<MOPromptManagerXPCProtocol>"8lr40l8s32l8
+ ___block_descriptor_48_e8_32r_e47_v24?0"<MOConfigurationXPCProtocol>"8?<B?>16lr32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v24?08?<B?>16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e50_v24?0"<MOAnalyticsManagerXPCProtocol>"8?<B?>16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e24_v24?0"MOResource"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e42_v16?0"<MOEngagementHistoryXCPProtocol>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48w_e17_v16?0"NSError"8lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e17_v16?0"NSError"8ls40l8s32l8s48l8
+ ___block_descriptor_56_e8_32s40bs48bs_e29_v24?0"NSArray"8"NSError"16ls40l8s48l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e8_v16?08ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48bs56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e17_v16?0"NSError"8lw56l8s40l8s48l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e38_v16?0"<MOAppEngagementXPCProtocol>"8ls32l8s40l8s48l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e47_v24?0"<MOPromptManagerXPCProtocol>"8?<B?>16ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.227
+ ___block_literal_global.229
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.235
+ ___block_literal_global.271
+ ___block_literal_global.29
+ ___kCFBooleanFalse
+ _kActionNameHostingAtHome
+ _kActionNamePhotosAtHome
+ _kActionNameTimeAtHome
+ _kActionNameVisit
+ _kAllContactIdentifiersSetKey
+ _kAllPlaceNamesSetKey
+ _kBPRRegularizationWeightkey
+ _kBaseScoreKey
+ _kBundleEndDateKey
+ _kBundleGoodnessScoreIncrementPhotoMemoryKey
+ _kBundleGoodnessScoreKey
+ _kBundleIdentifierKey
+ _kBundleInterfaceTypeKey
+ _kBundleScoreConstantKey
+ _kBundleScoreScalingParameterKey
+ _kBundleStartDateKey
+ _kBundleSubTypeKey
+ _kBundleSuperTypeKey
+ _kBurstyInteractionCountThresholdKey
+ _kCallDurationThresholdKey
+ _kContactHoldOffThresholdKey
+ _kDaysToSuppressCoarseSummaryAfterOnboarding
+ _kDecayFactorKey
+ _kDecayRateAfterViewedKey
+ _kDecayRateKey
+ _kDistanceToHomeThresholdKey
+ _kDistinctnessScoreKey
+ _kDiversityCoefficientAlphaKey
+ _kDiversityCoefficientKey
+ _kElapsedDaysFromBundleEndDateKey
+ _kEngagementScoreKey
+ _kEngagementScoreWeightKey
+ _kFIDownRankThresholdKey
+ _kHeuristicsScoreKey
+ _kHighContactSignificanceScoreThreshold
+ _kIsCoarseGranularitySummaryKey
+ _kIsDuplicatedKey
+ _kIsEligibleForTimeContextSummarization
+ _kIsEligibleForTransitBundleSummarization
+ _kIsEligibleForTripSummarization
+ _kIsPseudoDupInRecentKey
+ _kIsPseudoDupInRecommendedKey
+ _kIsSensitive
+ _kIsWithinHoldOffPeriodKey
+ _kJournalEntryWasCreatedWithNoWritingKey
+ _kJournalWasWrittenkey
+ _kLongTimePeriodSinceEngagementScoreParamsUpdatedSec
+ _kLowerBoundOfEngagementScoreParams
+ _kMOActivityContextEmbeddingActivityTypeFromPhotoTraits
+ _kMOActivityContextEmbeddingGenericActivityTypeFromPhotoTraits
+ _kMOActivityContextEmbeddingSecondLevelActivityType
+ _kMOActivityContextEmbeddingTopLevelActivityType
+ _kMOBundleCategoryMuid
+ _kMOBundleClusterMetadataCelebrationHistogram
+ _kMOBundleClusterMetadataHolidayHistogram
+ _kMOBundleClusterMetadataPhenotypePersonUUIDs
+ _kMOBundleClusterMetadataStateOfMindValenceHistogram
+ _kMOBundleClusterMetadataSubSuggestionIDsBeforePruning
+ _kMOEmbeddingDistanceWeightActivityContext
+ _kMOEmbeddingDistanceWeightActivityTypeFromPhotoTraits
+ _kMOEmbeddingDistanceWeightCelebration
+ _kMOEmbeddingDistanceWeightCombinedPlaceType
+ _kMOEmbeddingDistanceWeightContactNames
+ _kMOEmbeddingDistanceWeightDayOfWeek
+ _kMOEmbeddingDistanceWeightExtraContext
+ _kMOEmbeddingDistanceWeightGeographicalProximity
+ _kMOEmbeddingDistanceWeightHoliday
+ _kMOEmbeddingDistanceWeightIsWeekend
+ _kMOEmbeddingDistanceWeightIsWithChild
+ _kMOEmbeddingDistanceWeightIsWithContact
+ _kMOEmbeddingDistanceWeightIsWithCoworker
+ _kMOEmbeddingDistanceWeightIsWithFamily
+ _kMOEmbeddingDistanceWeightIsWithFriend
+ _kMOEmbeddingDistanceWeightIsWithMyPet
+ _kMOEmbeddingDistanceWeightLocationContext
+ _kMOEmbeddingDistanceWeightNormalizedDuration
+ _kMOEmbeddingDistanceWeightOtherSubjectFromPhotoTraits
+ _kMOEmbeddingDistanceWeightPlaceName
+ _kMOEmbeddingDistanceWeightPlaceTypeFromPhotoTraits
+ _kMOEmbeddingDistanceWeightSecondLevelActivityType
+ _kMOEmbeddingDistanceWeightSocialContext
+ _kMOEmbeddingDistanceWeightSocialEventFromPhotoTraits
+ _kMOEmbeddingDistanceWeightStateOfMindContext
+ _kMOEmbeddingDistanceWeightStateOfMindDomains
+ _kMOEmbeddingDistanceWeightStateOfMindLabels
+ _kMOEmbeddingDistanceWeightStateOfMindValence
+ _kMOEmbeddingDistanceWeightTimeContext
+ _kMOEmbeddingDistanceWeightTimeOfDay
+ _kMOEmbeddingDistanceWeightTopLevelActivityType
+ _kMOEmbeddingSummaryBundleID
+ _kMOEmbeddingSummarySuggestionID
+ _kMOEventBundleMetaDataForRankKeywordBusinessContact
+ _kMOEventBundleMetaDataForRankKeywordInterestingLocation
+ _kMOEventBundleMetaDataForRankKeywordSensitiveLocation
+ _kMOEventBundleMetaDataForRankKeywordUninterestingLocation
+ _kMOEventCategoryMuid
+ _kMOEventRoutineEventCategoryMuid
+ _kMOExtraContextEmbeddingBundleGoodnessScore
+ _kMOExtraContextEmbeddingOtherSubjectFromPhotoTraits
+ _kMOExtraContextEmbeddingPhotoCount
+ _kMOLabelFormatterMetaKeywordAtHome
+ _kMOLabelFormatterMetaKeywordAtPark
+ _kMOLabelFormatterMetaKeywordAtRestaurant
+ _kMOLabelFormatterMetaKeywordAtStore
+ _kMOLabelFormatterMetaKeywordBirthdayPersonName
+ _kMOLabelFormatterMetaKeywordDiversityKey
+ _kMOLabelFormatterMetaKeywordEnclosingArea
+ _kMOLabelFormatterMetaKeywordEnclosingAreaCap
+ _kMOLabelFormatterMetaKeywordHolidayName
+ _kMOLabelFormatterMetaKeywordInviteTitle
+ _kMOLabelFormatterMetaKeywordIsRoutine
+ _kMOLabelFormatterMetaKeywordPhotoTraitSubject
+ _kMOLabelFormatterMetaKeywordPromptIndex
+ _kMOLabelFormatterMetaKeywordPromptType
+ _kMOLabelFormatterMetaKeywordSensitive
+ _kMOLabelFormatterMetaKeywordThematicSummarySubType
+ _kMOLabelFormatterMetaKeywordTimes
+ _kMOLabelFormatterMetaKeywordWithContact
+ _kMOLabelFormatterMetaKeywordWithFamily
+ _kMOLabelFormatterMetaKeywordWithFriends
+ _kMOLabelFormatterMetaKeywordWithPets
+ _kMOLocationContextEmbeddingCombinedPlaceType
+ _kMOLocationContextEmbeddingEnclosingAreaName
+ _kMOLocationContextEmbeddingFamiliarityIndexLOI
+ _kMOLocationContextEmbeddingPlaceLatitude
+ _kMOLocationContextEmbeddingPlaceLongitude
+ _kMOLocationContextEmbeddingPlaceName
+ _kMOLocationContextEmbeddingPlaceTypeFromPhotoTraits
+ _kMOPersonRelationshipScoreThresholdForChild
+ _kMOPersonRelationshipScoreThresholdForCoworker
+ _kMOPersonRelationshipScoreThresholdForFamily
+ _kMOPersonRelationshipScoreThresholdForFriend
+ _kMOPersonRelationshipScoreThresholdForMyPet
+ _kMOSocialContextEmbeddingIsWithChild
+ _kMOSocialContextEmbeddingIsWithContact
+ _kMOSocialContextEmbeddingIsWithCoworker
+ _kMOSocialContextEmbeddingIsWithFamily
+ _kMOSocialContextEmbeddingIsWithFriend
+ _kMOSocialContextEmbeddingIsWithMyPet
+ _kMOSocialContextEmbeddingPersons
+ _kMOSocialContextEmbeddingSocialEventFromPhotoTraits
+ _kMOStateOfMindContextEmbeddingDomains
+ _kMOStateOfMindContextEmbeddingLabels
+ _kMOStateOfMindContextEmbeddingValenceValues
+ _kMOThematicSummaryLabelAtHome
+ _kMOThematicSummaryLabelDaySummary
+ _kMOThematicSummaryLabelDining
+ _kMOThematicSummaryLabelDiningAtHome
+ _kMOThematicSummaryLabelDiningOut
+ _kMOThematicSummaryLabelDiversityKeywordHighlights
+ _kMOThematicSummaryLabelDiversityKeywordMoments
+ _kMOThematicSummaryLabelDiversityKeywordReflection
+ _kMOThematicSummaryLabelDiversityKeywordTimes
+ _kMOThematicSummaryLabelDiversityKeywordWokrouts
+ _kMOThematicSummaryLabelIsOuting
+ _kMOThematicSummaryLabelMultiplePlaces
+ _kMOThematicSummaryLabelMultipleWorkouts
+ _kMOThematicSummaryLabelNotHome
+ _kMOThematicSummaryLabelShopping
+ _kMOThematicSummaryLabelVisit
+ _kMOThematicSummaryLabelWithMoreThanTwoContacts
+ _kMOThematicSummaryLabelWorkout
+ _kMOTimeContextEmbeddingCelebration
+ _kMOTimeContextEmbeddingDayOfWeek
+ _kMOTimeContextEmbeddingDayOfWeekCos
+ _kMOTimeContextEmbeddingDayOfWeekSin
+ _kMOTimeContextEmbeddingHoliday
+ _kMOTimeContextEmbeddingIsWeekend
+ _kMOTimeContextEmbeddingMonthCos
+ _kMOTimeContextEmbeddingMonthSin
+ _kMOTimeContextEmbeddingNormalizedDuration
+ _kMOTimeContextEmbeddingTimeOfDayCos
+ _kMOTimeContextEmbeddingTimeOfDaySin
+ _kMOTimeContextEmbeddingTimeString
+ _kMOTimeContextEmbeddingTimeTag
+ _kMOTimeContextEmbeddingWeekOfMonthCos
+ _kMOTimeContextEmbeddingWeekOfMonthSin
+ _kMOTimeContextEmbeddingWeekOfYear
+ _kMOUnavailableContextKey
+ _kMOUnknownContextKey
+ _kMaxBundleGoodnessScorePhotoMemoryKey
+ _kMaxDaysInRecommendedTabForContact
+ _kMaxDaysInRecommendedTabForStateOfMind
+ _kMaxDaysInRecommendedTabForWorkoutRoutine
+ _kMaxNumOfBirthdayBundlesPerDay
+ _kMaxNumOfHolidayBundlesPerDay
+ _kMaxPeopleCountFromSocialContextKey
+ _kMaxViewCountForAdjustmentKey
+ _kMediaPlayTimeThresholdKey
+ _kMinDaysElapsedForAdjustmentKey
+ _kMinEngagementCount
+ _kMinInterfaceTypes
+ _kMinSensedBundleCountInRecommendedTab
+ _kMinTimeIntervalForUpdateSec
+ _kMinViewCountForAdjustmentKey
+ _kNumAnomalyEventsNormalizedKey
+ _kNumBirthdayAssets
+ _kNumHolidayAssets
+ _kNumInviteEvents
+ _kNumMediaAssetsResourcesNormalizedKey
+ _kNumPhotoAssetsResourcesNormalizedKey
+ _kNumUniqueResourceTypesNormalizedKey
+ _kNumWorkoutRouteMapAssetsKey
+ _kOrdinalRankInRecommendedTabKey
+ _kPairWiseFar
+ _kPairWiseFarther
+ _kPairWiseFarthest
+ _kQualityScoreKey
+ _kRankingCategoryKey
+ _kRankingDictionaryIndexKey
+ _kRankingParamKeyPrefix
+ _kRankingRichnessAuxiliaryPriorityScoreKey
+ _kRankingRichnessPrimaryPriorityScoreKey
+ _kRankingRichnessSecondaryPriorityScoreKey
+ _kRankingScoreKey
+ _kRejectShortVisit
+ _kRejectSignificantContactWithHighSignificanceScoreKey
+ _kRejectWorkVisitWithNoPhotoKey
+ _kRejectWorkVisitWithPhotosKey
+ _kRejectedByVisitHeuristicsFilter
+ _kRichnessScoreKey
+ _kRichnessScoreScalingParameterKey
+ _kSensitiveRecommendedThresholdKey
+ _kShareCountThresholdKey
+ _kShortVisitDurationThresholdInSecKey
+ _kStateOfMindDomainCountThresholdKey
+ _kStateOfMindLabelCountThresholdKey
+ _kStateOfMindLoggedIn3pAppKey
+ _kStateOfMindLoggedInJournalAppKey
+ _kSuggestionAcceptThreshold
+ _kSuggestionAcceptThresholdForContactSubtype
+ _kSuggestionAcceptThresholdForContactWeeklySummarySubtype
+ _kSuggestionAcceptThresholdForDailyMediaVariants
+ _kSuggestionAcceptThresholdForMotionActivityWalkingSubtype
+ _kSuggestionAcceptThresholdForTimeAtHomeSubTypeVariants
+ _kSuggestionAcceptThresholdForTripSubType
+ _kSuggestionAcceptThresholdForVisitSubTypeVariants
+ _kSuggestionAcceptThresholdForWeeklyMediaSummaryVariants
+ _kSuggestionAcceptThresholdForWorkoutSubtype
+ _kSuggestionAcceptThresholdForWorkoutWeeklySummarySubtype
+ _kSuggestionDeleted
+ _kSuggestionIdentifierKey
+ _kSuggestionQuickAdd
+ _kSuggestionRecommendThreshold
+ _kSuggestionRecommendThresholdForContactSubtype
+ _kSuggestionRecommendThresholdForContactWeeklySummarySubtype
+ _kSuggestionRecommendThresholdForDailyMediaVariants
+ _kSuggestionRecommendThresholdForMotionActivityWalkingSubtype
+ _kSuggestionRecommendThresholdForTimeAtHomeSubTypeVariants
+ _kSuggestionRecommendThresholdForTripSubType
+ _kSuggestionRecommendThresholdForVisitSubTypeVariants
+ _kSuggestionRecommendThresholdForWeeklyMediaSummaryVariants
+ _kSuggestionRecommendThresholdForWorkoutSubtype
+ _kSuggestionRecommendThresholdForWorkoutWeeklySummarySubtype
+ _kSuggestionSelected
+ _kSuggestionViewed
+ _kSuggestionWasDeletedKey
+ _kSuggestionWasViewedButNotEngagedKey
+ _kSummarizationThresholdForMotionActivityWalkingSubType
+ _kSummarizationThresholdForVisitSubTypeVariants
+ _kSummarizationThresholdForWorkoutSubType
+ _kSuppressCoarseSummarization
+ _kTimeAtHomeDurationThresholdKey
+ _kTripSummarizationThresholdForVisitSubType
+ _kTripSummarizationThresholdForWorkoutSubType
+ _kUpperBoundOfEngagementScoreParams
+ _kUseBirthdayLabel
+ _kUseHolidayLabel
+ _kViewCountBasedScoreAdjustmentKey
+ _kVisibilityCategoryForUIKey
+ _kWeeklySummaryMediaPlayTimeThresholdKey
+ _kWeeklySummaryWorkoutDurationThresholdKey
+ _kWeightBirthdayInclusionKey
+ _kWeightForBurstyInteractionCount
+ _kWeightForCallDuration
+ _kWeightForContactLocationWork
+ _kWeightForDistanceToHome
+ _kWeightForFamiliarityIndex
+ _kWeightForGroupConversation
+ _kWeightForInterestingPOI
+ _kWeightForIsBusinessContact
+ _kWeightForIsCoworkerContact
+ _kWeightForIsFamilyContact
+ _kWeightForItemFromMe
+ _kWeightForLabelQualityScoreKey
+ _kWeightForMediaPlayTime
+ _kWeightForMultipleInteractionTypes
+ _kWeightForNumAnamolyEventsNormalizedKey
+ _kWeightForNumCoworkersKey
+ _kWeightForNumFamilyNormalizedKey
+ _kWeightForNumFriendsKey
+ _kWeightForNumKidsKey
+ _kWeightForNumOtherPersonsKey
+ _kWeightForNumPetsKey
+ _kWeightForNumRoutineEventsNormalizedKey
+ _kWeightForNumStateOfMindEventsNormalizedKey
+ _kWeightForNumTrendEventsNormalizedKey
+ _kWeightForPeopleCountMaxNormalizedKey
+ _kWeightForPeopleCountWeightedAverageNormalizedKey
+ _kWeightForPeopleCountWeightedSumNormalizedKey
+ _kWeightForPeopleDensityMaxNormalizedKey
+ _kWeightForPeopleDensityWeightedAverageNormalizedKey
+ _kWeightForSensitivePOI
+ _kWeightForTimeAtHomeDuration
+ _kWeightForTimeCorrelationScoreKey
+ _kWeightForViewCountBasedPenaltyKey
+ _kWeightForWorkoutDurationNormalizedKey
+ _kWeightHolidayInclusionKey
+ _kWeightInviteEventInclusionKey
+ _kWeightShareCountFeature
+ _kWeightStateOfMindDomainCountNormalizedKey
+ _kWeightStateOfMindLabelCountNormalizedKey
+ _kWorkoutDurationThresholdKey
+ _kWorkoutTypesSetKey
+ _kallStateOfMindIdentifiersSetKey
+ _momentsDaemonDefaults.onceToken
+ _momentsDaemonDefaults.shared
+ _objc_msgSend$_callProxy:usingBlock:onError:
+ _objc_msgSend$_callProxyProvider:usingBlock:onError:
+ _objc_msgSend$_getActiveConnection
+ _objc_msgSend$_getSingleCallHandler:
+ _objc_msgSend$_logEngagementEvent:withContext:
+ _objc_msgSend$_makeConnectionErrorWithReason:
+ _objc_msgSend$_postProxy:usingBlock:onError:
+ _objc_msgSend$_postProxyProvider:usingBlock:onError:
+ _objc_msgSend$_purgeEventsWithHandler:
+ _objc_msgSend$activityPhotoTraitLabelMetadataForThematicSummary:AtHome:
+ _objc_msgSend$associatedPersonLocalIdentifiers
+ _objc_msgSend$buildThematicSummaryMetaDataForEventBundle:
+ _objc_msgSend$callAsyncProxyUsingBlock:onError:
+ _objc_msgSend$callSyncProxyUsingBlock:onError:
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$categories
+ _objc_msgSend$categoryMuid
+ _objc_msgSend$clusterMetadata
+ _objc_msgSend$combinedPlaceTypeLabelMetadataForThematicSummary:
+ _objc_msgSend$constantValue
+ _objc_msgSend$expressionType
+ _objc_msgSend$fetchEligiblePOICategoriesWithHandler:
+ _objc_msgSend$fetchEventBundlesWithPredicate:withContext:andHandler:
+ _objc_msgSend$floatValue
+ _objc_msgSend$generateAvailabilityPredictionsAndRegisterTimerWithHandler:
+ _objc_msgSend$generateAvailabilityPredictionsWithHandler:
+ _objc_msgSend$getAsyncProxyProvider
+ _objc_msgSend$getConnectionName
+ _objc_msgSend$getPersonFromBirthdayPhotoTrait:eventBundle:
+ _objc_msgSend$getSyncProxyProvider
+ _objc_msgSend$getTheBestPersonRelationtshipTagFor:useRelationshipInference:
+ _objc_msgSend$holidayIdentifier
+ _objc_msgSend$initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:
+ _objc_msgSend$initWithDateInterval:ascending:categories:limit:
+ _objc_msgSend$initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:holidayHistogram:celebrationHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:stateOfMindValenceHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:phenotypePersonUUIDs:
+ _objc_msgSend$initWithIdentifier:name:labelType:holidayIdentifier:meaningIdentifier:relevantAssetUUIDs:associatedPersonLocalIdentifiers:
+ _objc_msgSend$initWithIdentifier:name:type:assets:data:value:priorityScore:photoCurationScore:photoFaceCount:photoAssetMediaType:photoAssetCloudIdentifier:
+ _objc_msgSend$initWithIdentifier:personId:displayName:isOrganization:
+ _objc_msgSend$initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:
+ _objc_msgSend$initWithName:usingDelegate:
+ _objc_msgSend$isAllowedKeyPathForEventBundle:
+ _objc_msgSend$isMe
+ _objc_msgSend$isOrganization
+ _objc_msgSend$isSensitive
+ _objc_msgSend$isValidPredicate:
+ _objc_msgSend$keyPath
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$labelType
+ _objc_msgSend$leftExpression
+ _objc_msgSend$makeNewConnectionWithInterfaceFor:
+ _objc_msgSend$meaningIdentifier
+ _objc_msgSend$phenotype
+ _objc_msgSend$phenotypePersonUUIDs
+ _objc_msgSend$photoAssetCloudIdentifier
+ _objc_msgSend$placeTypePhotoTraitLabelMetadataForThematicSummary:
+ _objc_msgSend$postAsyncProxyUsingBlock:onError:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$rightExpression
+ _objc_msgSend$rsvpStatus
+ _objc_msgSend$selectBirthdayFromPhotoTraits:
+ _objc_msgSend$selectHolidayFromPhotoTraits:
+ _objc_msgSend$setActivityNameForThematicSummaryFromActionName:metaData:keyword:keywordType:
+ _objc_msgSend$setCategoryMuid:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setIsMe:
+ _objc_msgSend$setMetaDataForBirthday:metaData:eventBundle:
+ _objc_msgSend$setMetaDataForHoliday:metaData:eventBundle:
+ _objc_msgSend$setMetaDataForInvite:metaData:
+ _objc_msgSend$setRsvpStatus:
+ _objc_msgSend$setUpNotificationTimerWithFireDate:
+ _objc_msgSend$subpredicates
+ _objc_msgSend$timeStringSingularToPluralForm:
+ _objc_msgSend$validateComparisonPredicate:
+ _objc_msgSend$validateCompoundPredicate:
+ _objc_msgSend$weekOfYearHistogram
+ _objc_msgSend$withProxyProvider:proxyHandler:onError:
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[MOAnalyticsManager dealloc]
- -[MOAppEngagementReporter dealloc]
- -[MOConfiguration isAllowedToPromptEventCategory:].cold.1
- -[MOConfiguration isAllowedToPromptResourceType:].cold.1
- -[MOContact initWithIdentifier:personId:displayName:]
- -[MOEngagementHistoryWriter dealloc]
- -[MOEngagementHistoryWriter logAppEntryEngagementEvent:clientIdentifier:forBundles:startTime:endTime:totalCharacters:addedCharacters:otherContext:]
- -[MOEngagementHistoryWriter logClientEngagementEvent:clientIdentifier:otherContext:]
- -[MOEngagementHistoryWriter logEngagementEvent:withContext:]
- -[MOEngagementHistoryWriter logEngagementEvent:withContext:].cold.1
- -[MOEngagementHistoryWriter logPerformanceEvent:withContext:].cold.1
- -[MOEngagementHistoryWriter logUsageEvent:withContext:].cold.1
- -[MOEventBundle initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:]
- -[MOEventBundle initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:]
- -[MOEventBundle initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:]
- -[MOEventFetchOptions category]
- -[MOEventFetchOptions initWithDateInterval:ascending:category:limit:]
- -[MOPlace initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:]
- -[MOPlace initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:]
- -[MOPlace initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:]
- -[MOPromptManager dealloc]
- GCC_except_table13
- GCC_except_table31
- _OBJC_IVAR_$_MOAnalyticsManager.connection
- _OBJC_IVAR_$_MOAnalyticsManager.connectionProxy
- _OBJC_IVAR_$_MOAnalyticsManager.proxy
- _OBJC_IVAR_$_MOAppEngagementReporter.connection
- _OBJC_IVAR_$_MOAppEngagementReporter.proxy
- _OBJC_IVAR_$_MOConfiguration.connection
- _OBJC_IVAR_$_MOConfiguration.connectionProxy
- _OBJC_IVAR_$_MOConfiguration.syncProxy
- _OBJC_IVAR_$_MOConnection._proxy
- _OBJC_IVAR_$_MOEngagementHistoryWriter.connection
- _OBJC_IVAR_$_MOEngagementHistoryWriter.proxy
- _OBJC_IVAR_$_MOEventFetchOptions._category
- _OBJC_IVAR_$_MOPromptManager.connection
- _OBJC_IVAR_$_MOPromptManager.connectionProxy
- _OBJC_IVAR_$_MOPromptManager.proxy
- ___102-[MOPromptManager setupPeriodicTimeToWriteMomentsNotificationsUsingDateComponents:defaultURL:handler:]_block_invoke
- ___102-[MOPromptManager setupPeriodicTimeToWriteMomentsNotificationsUsingDateComponents:defaultURL:handler:]_block_invoke.225
- ___102-[MOPromptManager setupPeriodicTimeToWriteMomentsNotificationsUsingDateComponents:defaultURL:handler:]_block_invoke_2
- ___119-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:handler:]_block_invoke.234
- ___143-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:respectLearnFromThisApp:handler:]_block_invoke.236
- ___23-[MOConfiguration init]_block_invoke
- ___23-[MOConfiguration init]_block_invoke.119
- ___26-[MOAnalyticsManager init]_block_invoke
- ___26-[MOAnalyticsManager init]_block_invoke_2
- ___31-[MOAppEngagementReporter init]_block_invoke
- ___31-[MOAppEngagementReporter init]_block_invoke.11
- ___31-[MOAppEngagementReporter init]_block_invoke.11.cold.1
- ___31-[MOAppEngagementReporter init]_block_invoke.8
- ___33-[MOEngagementHistoryWriter init]_block_invoke
- ___33-[MOEngagementHistoryWriter init]_block_invoke_2
- ___33-[MOEngagementHistoryWriter init]_block_invoke_3
- ___33-[MOEngagementHistoryWriter init]_block_invoke_3.cold.1
- ___39-[MOPromptManager storeEvents:handler:]_block_invoke.218
- ___39-[MOSuggestionSheetController activate]_block_invoke.170
- ___39-[MOSuggestionSheetController activate]_block_invoke.174
- ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.247
- ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.249
- ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.250
- ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke_2.248
- ___42-[MOPromptManager dumpDBStateWithHandler:]_block_invoke.266
- ___42-[MOPromptManager purgeEventsWithHandler:]_block_invoke.253
- ___43-[MOPromptManager bundleEventsWithHandler:]_block_invoke.252
- ___43-[MOPromptManager runAnalyticsWithHandler:]_block_invoke.254
- ___44-[MOPromptManager collectEventsWithHandler:]_block_invoke.251
- ___49-[MOConfiguration isAllowedToPromptResourceType:]_block_invoke.132
- ___49-[MOConfiguration isAllowedToPromptResourceType:]_block_invoke.132.cold.1
- ___49-[MOPromptManager analyzeTrendsInEvents:handler:]_block_invoke.255
- ___50-[MOConfiguration isAllowedToPromptEventCategory:]_block_invoke.130
- ___50-[MOConfiguration isAllowedToPromptEventCategory:]_block_invoke.130.cold.1
- ___50-[MOPromptManager fetchEventsWithOptions:handler:]_block_invoke.220
- ___50-[MOPromptManager printOnboardingStatusAnalytics:]_block_invoke.269
- ___51-[MOPromptManager getMomentsNotificationsSchedule:]_block_invoke
- ___51-[MOPromptManager getMomentsNotificationsSchedule:]_block_invoke.230
- ___51-[MOPromptManager getMomentsNotificationsSchedule:]_block_invoke_2
- ___54-[MOPromptManager printSettingValue:withType:handler:]_block_invoke.268
- ___54-[MOPromptManager scheduleDatabaseUpgradeWithHandler:]_block_invoke.217
- ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.231
- ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke_2
- ___56-[MOPromptManager triggerFeedbackAssistantFlow:handler:]_block_invoke.272
- ___61-[MOPromptManager uploadFeedbackWithDBStateToServer:handler:]_block_invoke.262
- ___62-[MOPromptManager refreshEventsWithRefreshVariant:andHandler:]_block_invoke.256
- ___63-[MOPromptManager testMomentsNotificationsWithOptions:handler:]_block_invoke
- ___63-[MOPromptManager testMomentsNotificationsWithOptions:handler:]_block_invoke.271
- ___63-[MOPromptManager testMomentsNotificationsWithOptions:handler:]_block_invoke_2
- ___64-[MOPromptManager getSnapshotDictionaryForAnalyticsWithHandler:]_block_invoke.267
- ___66-[MOPromptManager getTimeToWriteNotificationsScheduleWithHandler:]_block_invoke
- ___66-[MOPromptManager getTimeToWriteNotificationsScheduleWithHandler:]_block_invoke.227
- ___66-[MOPromptManager getTimeToWriteNotificationsScheduleWithHandler:]_block_invoke_2
- ___73-[MOPromptManager setupMomentsNotificationsWithSchedule:options:handler:]_block_invoke
- ___73-[MOPromptManager setupMomentsNotificationsWithSchedule:options:handler:]_block_invoke.228
- ___73-[MOPromptManager setupMomentsNotificationsWithSchedule:options:handler:]_block_invoke_2
- ___84-[MOPromptManager _initForSoftLinkwithMOEventClass:moEventBundleClass:moXpcContext:]_block_invoke
- ___84-[MOPromptManager _initForSoftLinkwithMOEventClass:moEventBundleClass:moXpcContext:]_block_invoke.200
- ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke.257
- ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke_2.260
- ___block_descriptor_48_e8_32bs40bs_e46_v32?0"NSArray"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32bs40bs_e48_v32?0"NSDateComponents"8"NSURL"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e14_v16?0?<B?>8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e14_v16?0?<B?>8ls32l8s40l8
- ___block_descriptor_56_e8_32s40r_e14_v16?0?<B?>8ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48bs_e14_v16?0?<B?>8ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40bs_e14_v16?0?<B?>8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e14_v16?0?<B?>8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e14_v16?0?<B?>8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_74_e8_32s40s48s56s64bs_e14_v16?0?<B?>8ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_75_e8_32s40s48s56s64bs_e14_v16?0?<B?>8ls32l8s40l8s48l8s64l8s56l8
- ___block_literal_global.10
- ___block_literal_global.113
- ___block_literal_global.119
- ___block_literal_global.12
- ___block_literal_global.122
- ___block_literal_global.14
- ___block_literal_global.199
- ___block_literal_global.203
- ___block_literal_global.238
- ___block_literal_global.240
- ___block_literal_global.242
- ___block_literal_global.244
- ___block_literal_global.246
- ___block_literal_global.259
- ___block_literal_global.7
- _kMOBundleClusterMetadatasubSuggestionIDsBeforePruning
- _objc_msgSend$getMomentsNotificationsSchedule:
- _objc_msgSend$getTimeToWriteNotificationsApplicationScheduleWithContext:andHandler:
- _objc_msgSend$infoDictionary
- _objc_msgSend$initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:
- _objc_msgSend$initWithDateInterval:ascending:category:limit:
- _objc_msgSend$initWithIdentifier:name:relevantAssetUUIDs:
- _objc_msgSend$initWithIdentifier:personId:displayName:
- _objc_msgSend$initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:
- _objc_msgSend$resume
- _objc_msgSend$setupMomentsNotificationsWithSchedule:options:handler:
- _objc_msgSend$setupPeriodicTimeToWriteMomentsNotificationsForApplication:usingDateComponents:withActionURL:withContext:andHandler:
- _objc_msgSend$softRefreshEventsWithContext:andRefreshVariant:andHandler:
- _objc_msgSend$testMomentsNotificationsWithOptions:handler:
- _objc_msgSend$unsignedLongValue
CStrings:
+ "%@: proxy error, %@, %@, retrying..."
+ "%@: proxy error, %@, %@."
+ "%@:%@"
+ "-[MOConnectionManager _getActiveConnection]"
+ "-[MOConnectionManager withProxyProvider:proxyHandler:onError:]"
+ "1"
+ "<MOEventBundle bundleIdentifier, %@, suggestionID, %@, sub Suggestion IDs, %@, startDate, %@, endDate, %@, creationDate, %@, firstCreationDate, %@, interfaceType, %lu, bundleSubType, %lu, bundleSuperType, %lu, filtered, %@, agg./suppressed, %@, sum. granularity, %lu, includedInSummaryOnly, %@, promptLanguage, %@, photoSource, %lu, action, %@, concurrentMediaAction, %@, place, %@, time, %@, sub bundle IDs, %@, labels, %@, rankingVisibilityCategoryForUI, %@, rankingBundleGoodnessScore, %@ >"
+ "<MOPhotoTrait localIdentifier, %@, name, %@, labelType, %@, holidayIdentifier, %@, meaningIdentifier, %@, relevantAssetUUIDs, %@, associatedPersonLocalIdentifiers, %@,>"
+ "<MOPlace identifier, %@, name, %@, confidence, %f, placeType, %lu, placeUserType, %lu, categoryMuid, %@, locationMode, %lu, distanceToHomeInMiles, %f, poiCategory, %@, familiarityIndexLOI, %f>"
+ "<MOResource identifier, %@, name, %@, type, %lu, assets, %@, photoAssetCloudIdentifier, %@, data.length, %lu, value, %f"
+ "@\"<MOConnectionDelegate>\""
+ "@\"<MOConnectionManagerDelegate>\""
+ "@\"MOConnectionManager\""
+ "@\"MOEventInvite\""
+ "@\"NSXPCConnection\"24@0:8@\"MOConnectionManager\"16"
+ "@104@0:8@16@24Q32@40@48d56d64@72Q80Q88@96"
+ "@120@0:8@16@24Q32Q40@48Q56@64@72d80d88d96@104@112"
+ "@136@0:8@16@24@32Q40Q48@56Q64@72@80d88d96d104d112@120@128"
+ "@16@?0@?<v@?@\"NSError\">8"
+ "@204@0:8@16B24@28@36@44@52@60@68@76@84@92@100@108@116@124@132@140@148@156@164@172@180@188@196"
+ "@252@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232@240B248"
+ "@272@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232B240Q244Q252@260B268"
+ "@288@0:8@16@24@32@40@48@56@64@72B80Q84Q92@100Q108@116@124@132@140@148@156@164@172@180@188@196Q204@212B220Q224@232@240@248B256Q260Q268@276B284"
+ "@44@0:8@16@24@32B40"
+ "@44@0:8@16B24@28@36"
+ "@96@0:8@16Q24Q32@40Q48@56@64d72d80d88"
+ "@?24@0:8@?16"
+ "A"
+ "Activating connection '%@'"
+ "B32@?0@8@16^B24"
+ "BPRRegularizationWeight"
+ "Birthday"
+ "Built label metadata for thematic summary:cluster phenotype=%{private}@, metaData=%@"
+ "BusinessContact"
+ "Called async proxy provider"
+ "Called sync proxy provider"
+ "Can't activate connection '%@': nil delegate"
+ "Connection '%@' Invalidated"
+ "Error: %@, Usage event: %@, context: %{private}@"
+ "Error: %@, didAppEntryUpdateUsingSuggestions"
+ "Error: %@, engagement event: %@, context: %{private}@"
+ "Error: %@, performance event: %@, context: %{private}@"
+ "FIDownRankThreshold"
+ "Fridays"
+ "Halloween"
+ "InterestingLocation"
+ "Invalid '%@' connection .remoteObjectInterface (in %s:%d)"
+ "Invite"
+ "Invite Event"
+ "Jump Rope"
+ "MOConfiguration initiate client"
+ "MOConnection managed interrupted, retrying..."
+ "MOConnectionManager"
+ "MOConnectionManagerDelegate"
+ "MOEngagementHistoryWritter"
+ "MOEventInvite"
+ "MOInvitePerson"
+ "MOMetaDataCurationUtility"
+ "MOPhotoResourceICloudIdentifier"
+ "MOPromptManager initiate client"
+ "MOPromptManager: calling(%d) getDiagnosticReporterConfiguration:handler"
+ "Mind and Body"
+ "Mondays"
+ "No personalRelationship is available for person %{private}@"
+ "None of personalRelationships are confident enough to generate the best relationship tag for person %{private}@"
+ "Notification Scheduling SPIs are deprecated, schedule is now handled internally within moments"
+ "Notification Scheduling SPIs deprecated, schedule is now handled internally within moments"
+ "NumUniqueResourceTypesNormalizedKey"
+ "NumWorkoutRouteMapAssets"
+ "PATTERNEMBEDDING"
+ "Personalized Reflection"
+ "PhotoAssetCloudIdentifier"
+ "Photos at Home"
+ "Predicate is of unexpected type"
+ "Q28@0:8@16B24"
+ "RV parks"
+ "RankingRichnessAuxiliaryPriorityScoreKey"
+ "RankingRichnessPrimaryPriorityScoreKey"
+ "RankingRichnessSecondaryPriorityScoreKey"
+ "Saturdays"
+ "SensitiveLocation"
+ "Should use valid sync proxy block handler (in %s:%d)"
+ "Spotlight"
+ "Sundays"
+ "T@\"<MOConnectionDelegate>\",W,N,V_delegate"
+ "T@\"<MOConnectionManagerDelegate>\",W,N,V_delegate"
+ "T@\"CLLocation\",&,N,V_inviteEventLocation"
+ "T@\"MOEventInvite\",&,N,V_inviteEvent"
+ "T@\"NSArray\",&,N,V_inviteEventAttendees"
+ "T@\"NSArray\",&,N,V_inviteEventOrganizers"
+ "T@\"NSArray\",&,N,V_phenotypePersonUUIDs"
+ "T@\"NSArray\",C,N,V_associatedPersonLocalIdentifiers"
+ "T@\"NSDictionary\",&,N,V_celebrationHistogram"
+ "T@\"NSDictionary\",&,N,V_holidayHistogram"
+ "T@\"NSDictionary\",&,N,V_stateOfMindValenceHistogram"
+ "T@\"NSNumber\",&,N,V_categoryMuid"
+ "T@\"NSString\",&,N,V_displayName"
+ "T@\"NSString\",&,N,V_holidayIdentifier"
+ "T@\"NSString\",&,N,V_inviteEventPlaceName"
+ "T@\"NSString\",&,N,V_inviteEventTitle"
+ "T@\"NSString\",&,N,V_labelType"
+ "T@\"NSString\",&,N,V_meaningIdentifier"
+ "T@\"NSString\",&,N,V_rsvpStatus"
+ "T@\"NSString\",R,&,N,V_photoAssetCloudIdentifier"
+ "TB,N,V_containsOrganizationContact"
+ "TB,N,V_inviteEventIsAllDay"
+ "TB,N,V_isMe"
+ "TB,N,V_isSensitive"
+ "TB,R,N,V_isOrganization"
+ "THEMATICSUMMARIZATION"
+ "Tai Chi"
+ "Test notifications Moments command deprecated and moved to MomentsUI"
+ "Thursdays"
+ "Time at Home"
+ "Tuesdays"
+ "UninterestingLocation"
+ "Wednesdays"
+ "WeeklySummaryWorkoutDurationThreshold"
+ "_associatedPersonLocalIdentifiers"
+ "_callProxy:usingBlock:onError:"
+ "_callProxyProvider:usingBlock:onError:"
+ "_categoryMuid"
+ "_celebrationHistogram"
+ "_connectionName"
+ "_containsOrganizationContact"
+ "_getActiveConnection"
+ "_getSingleCallHandler:"
+ "_holidayHistogram"
+ "_holidayIdentifier"
+ "_interruptActive"
+ "_inviteEvent"
+ "_inviteEventAttendees"
+ "_inviteEventIsAllDay"
+ "_inviteEventLocation"
+ "_inviteEventOrganizers"
+ "_inviteEventPlaceName"
+ "_inviteEventTitle"
+ "_isMe"
+ "_isOrganization"
+ "_isSensitive"
+ "_labelType"
+ "_logEngagementEvent:withContext:"
+ "_makeConnectionErrorWithReason:"
+ "_meaningIdentifier"
+ "_mo_connection"
+ "_phenotypePersonUUIDs"
+ "_photoAssetCloudIdentifier"
+ "_postProxy:usingBlock:onError:"
+ "_postProxyProvider:usingBlock:onError:"
+ "_purgeEventsWithHandler:"
+ "_rsvpStatus"
+ "_stateOfMindValenceHistogram"
+ "_xpc_connection"
+ "activityPhotoTraitLabelMetadataForThematicSummary:AtHome:"
+ "activityTypeFromPhotoTraits"
+ "afternoons"
+ "allContactIdentifiersSet"
+ "allPlaceNamesSet"
+ "allStateOfMindIdentifiersSet"
+ "amusement park"
+ "amusement parks"
+ "amusementpark"
+ "aquariums"
+ "ascending, %@,  startDate, %@, endDate, %@, categories, %@, limit, %@"
+ "associatedPersonLocalIdentifiers"
+ "at_home"
+ "at_park"
+ "at_restaurant"
+ "at_store"
+ "bakeries"
+ "baseScore"
+ "baseball fields"
+ "basketball courts"
+ "beaches"
+ "beauty stores"
+ "birthday_person_name"
+ "bowling alleys"
+ "breweries"
+ "buildThematicSummaryMetaDataForEventBundle:"
+ "bundleCategoryMuid"
+ "bundleGoodnessScoreIncrementPhotoMemory"
+ "bundleScoreConstant"
+ "bundleScoreScalingParameter"
+ "burstyInteractionCountThreshold"
+ "cafes"
+ "callAsyncProxyUsingBlock:onError:"
+ "callDurationThreshold"
+ "callSyncProxyUsingBlock:onError:"
+ "calling fetchEligiblePOICategoriesWithHandler"
+ "calling fetchEligiblePOICategoriesWithHandler completed"
+ "calling fetchEventBundlesWithOptions (%d)"
+ "calling fetchEventBundlesWithOptions completed found %@ events"
+ "calling fetchEventBundlesWithPredicate"
+ "calling fetchEventBundlesWithPredicate completed found %@ bundles"
+ "calling generateAvailabilityPredictionsAndRegisterTimerWithHandler"
+ "calling generateAvailabilityPredictionsAndRegisterTimerWithHandler completed"
+ "calling generateAvailabilityPredictionsWithHandler"
+ "calling generateAvailabilityPredictionsWithHandler completed"
+ "calling setUpNotificationTimerWithFireDate"
+ "calling setUpNotificationTimerWithFireDate completed"
+ "calling setUpNotificationTimerWithFireDate hit error: %@"
+ "campgrounds"
+ "capitalizedString"
+ "castles"
+ "categoryMuid"
+ "celebration"
+ "celebrationHistogram"
+ "combinedPlaceType"
+ "combinedPlaceTypeLabelMetadataForThematicSummary:"
+ "completed: getDiagnosticReporterConfiguration:handler"
+ "connectionManager"
+ "constantValue"
+ "contactHoldOffThreshold"
+ "contactIdentifier IN %@"
+ "containsOrganizationContact"
+ "convention centers"
+ "convertNSNumberToContactType:"
+ "convertNSNumberToRoadType:"
+ "convertNSNumberToSensitiveLocationType:"
+ "convertNSNumberToUninterestingLocationType:"
+ "dayOfWeek"
+ "dayOfWeekCos"
+ "dayOfWeekSin"
+ "day_summary"
+ "daysToSuppressCoarseSummaryAfterOnboarding"
+ "decayFactor"
+ "decayRate"
+ "decayRateAfterViewed"
+ "displayName, %@"
+ "distanceToHomeThreshold"
+ "distinctnessScore"
+ "diversityCoefficient"
+ "diversityCoefficientAlpha"
+ "diversity_key"
+ "eating"
+ "elapsedDaysFromBundleEndDate"
+ "embeddingDistWeight_IsWithContact"
+ "embeddingDistWeight_SocialEventFromPhotoTraits "
+ "embeddingDistWeight_activityContext"
+ "embeddingDistWeight_activityTypeFromPhotoTraits"
+ "embeddingDistWeight_celebration"
+ "embeddingDistWeight_contactNames"
+ "embeddingDistWeight_dayOfWeek"
+ "embeddingDistWeight_extraContext"
+ "embeddingDistWeight_geoProximity"
+ "embeddingDistWeight_holiday"
+ "embeddingDistWeight_isWeekend"
+ "embeddingDistWeight_isWithChild"
+ "embeddingDistWeight_isWithCoworker"
+ "embeddingDistWeight_isWithFamily"
+ "embeddingDistWeight_isWithFriend"
+ "embeddingDistWeight_isWithMyPet"
+ "embeddingDistWeight_locationContext"
+ "embeddingDistWeight_normalizedDuration"
+ "embeddingDistWeight_otherSubjectFromPhotoTraits"
+ "embeddingDistWeight_placeName"
+ "embeddingDistWeight_placeType"
+ "embeddingDistWeight_placeTypeFromPhotoTraits"
+ "embeddingDistWeight_secondLevelActivityType"
+ "embeddingDistWeight_socialContext"
+ "embeddingDistWeight_stateOfMindContext"
+ "embeddingDistWeight_stateOfMindDomains"
+ "embeddingDistWeight_stateOfMindLabels"
+ "embeddingDistWeight_stateOfMindValence"
+ "embeddingDistWeight_timeContext"
+ "embeddingDistWeight_timeOfDay"
+ "embeddingDistWeight_topLevelActivityType"
+ "enclosingAreaName"
+ "enclosing_area"
+ "enclosing_area_cap"
+ "engagement event: %@, context: %{private}@"
+ "engagementScore"
+ "evenings"
+ "eventCategoryMuid"
+ "eventRoutineEventCategoryMuid"
+ "expressionType"
+ "fairgrounds"
+ "fetchEligiblePOICategoriesWithHandler:"
+ "fetchEventBundlesWithPredicate:handler:"
+ "fetchEventBundlesWithPredicate:withContext:andHandler:"
+ "fishing spots"
+ "fitness centers"
+ "floatValue"
+ "food markets"
+ "fortresses"
+ "generateAvailabilityPredictionsAndRegisterTimerWithHandler:"
+ "generateAvailabilityPredictionsWithHandler:"
+ "getAsyncProxyProvider"
+ "getConnectionName"
+ "getPersonFromBirthdayPhotoTrait:eventBundle:"
+ "getSyncProxyProvider"
+ "getTheBestPersonRelationtshipTagFor:"
+ "getTheBestPersonRelationtshipTagFor:useRelationshipInference:"
+ "go kart"
+ "golf courses"
+ "gym"
+ "heuristicsScore"
+ "highContactSignificanceScoreThreshold"
+ "highlights"
+ "hiking trails"
+ "holiday"
+ "holidayHistogram"
+ "holidayIdentifier"
+ "holiday_name"
+ "home"
+ "hotels"
+ "identifier, %@, personId, %@, name, %@, is organization, %d"
+ "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:"
+ "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:isSensitive:"
+ "initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:isSensitive:"
+ "initWithDateInterval:ascending:categories:limit:"
+ "initWithIdentifier:isFiltered:phenoType:topLevelActivityHistogram:secondLevelActivityHistogram:activityTypeFromPhotoTraitsHistogram:timeTagHistogram:dayOfWeekHistogram:weekOfYearHistogram:timeContextFromPhotoTraitsHistogram:holidayHistogram:celebrationHistogram:placeNameHistogram:combinedPlaceTypeHistogram:enclosingPlaceNameHistogram:placeTypeFromPhotoTraitsHistogram:contactNamesHistogram:personRelationshipHistogram:socialEventFromPhotoTraitsHistogram:otherSubjectFromPhotoTraitsHistogram:stateOfMindValenceHistogram:subBundleGoodnessScores:subSuggestionIDsBeforePruning:phenotypePersonUUIDs:"
+ "initWithIdentifier:name:labelType:holidayIdentifier:meaningIdentifier:relevantAssetUUIDs:associatedPersonLocalIdentifiers:"
+ "initWithIdentifier:name:labelType:holidayIdentifier:relevantAssetUUIDs:"
+ "initWithIdentifier:name:type:assets:data:value:priorityScore:photoCurationScore:photoFaceCount:photoAssetMediaType:photoAssetCloudIdentifier:"
+ "initWithIdentifier:personId:displayName:isOrganization:"
+ "initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:"
+ "initWithName:type:photoAssetCloudIdentifier:"
+ "initWithName:usingDelegate:"
+ "initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:"
+ "initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:categoryMuid:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:"
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
+ "invite_title"
+ "isAllowedKeyPathForEventBundle:"
+ "isBundleOrSubBundleDeleted"
+ "isBundleOrSubBundlesSelectedOrQuickAdded"
+ "isCoarseGranularitySummaryKey"
+ "isDuplicated"
+ "isEligibleForTimeContextSummarization"
+ "isEligibleForTransitBundleSummarization"
+ "isEligibleForTripSummarization"
+ "isExtendedLogEnabled:forDetaultsManager:"
+ "isInThematicSummary"
+ "isMe"
+ "isOrganization"
+ "isPseudoDupInRecentTab"
+ "isPseudoDupInRecommendedTab"
+ "isSensitive"
+ "isValidPredicate:"
+ "isWeekend"
+ "isWithinHoldOffPeriod"
+ "is_outing"
+ "is_routine"
+ "journalEntryWasCreatedWithNoWriting"
+ "journalWasWritten"
+ "jump rope"
+ "kRejectedByVisitHeuristicsFilter"
+ "kayaking"
+ "keyPath"
+ "keysOfEntriesPassingTest:"
+ "labelType"
+ "landmarks"
+ "leftExpression"
+ "libraries"
+ "longTimePeriodSinceEngagementScoreParamsUpdatedSec"
+ "lowerBoundOfEngagementScoreParams"
+ "makeNewConnectionWithInterfaceFor:"
+ "marinas"
+ "maxBundleGoodnessScorePhotoMemory"
+ "maxDaysInRecommendedTabForContact"
+ "maxDaysInRecommendedTabForStateOfMind"
+ "maxDaysInRecommendedTabForWorkoutRoutine"
+ "maxNumOfBirthdayBundlesPerDay"
+ "maxNumOfHolidayBundlesPerDay"
+ "maxPeopleCountFromSocialContext"
+ "maxViewCountForAdjustment"
+ "meaning"
+ "meaningIdentifier"
+ "mediaPlayTimeThreshold"
+ "midnights"
+ "minDaysElapsedForAdjustment"
+ "minEngagementCount"
+ "minInterfaceTypes"
+ "minSensedBundleCountInRecommendedTab"
+ "minTimeIntervalForUpdateSec"
+ "minViewCountForAdjustment"
+ "mind and body"
+ "mini golf"
+ "moEventBundleClass"
+ "moEventClass"
+ "moXpcContextClass"
+ "moments"
+ "momentsDaemonDefaults"
+ "monthCos"
+ "monthSin"
+ "mornings"
+ "movie theaters"
+ "multiple_places"
+ "multiple_workouts"
+ "museums"
+ "music venues"
+ "national monuments"
+ "national parks"
+ "nightlife"
+ "nights"
+ "nil predicate"
+ "nil proxy"
+ "nil proxy @1"
+ "nil proxy @2"
+ "normalizedDuration"
+ "not_home"
+ "numBirthdayAssets"
+ "numHolidayAssets"
+ "numInviteEvents"
+ "numMediaAssetsResourcesNormalized"
+ "numPhotoAssetsResourcesNormalized"
+ "ordinalRankInRecommendedTab"
+ "otherSubjectFromPhotoTraits"
+ "pairWiseFar"
+ "pairWiseFarther"
+ "pairWiseFarthest"
+ "parks"
+ "personalized_reflection"
+ "personalized_reflection_activity"
+ "personalized_reflection_contact"
+ "personalized_reflection_outing"
+ "phenotypePersonUUIDs"
+ "photoAssetCloudIdentifier"
+ "photoCount"
+ "photoTraitActivityType"
+ "photo_trait_subject"
+ "placeFamiliarityIndexLOI"
+ "placeLatitude"
+ "placeLongitude"
+ "placeName, %@, confidence, %f, locationMode, %@, new place, %lu, isHighConfidence, %d, isInvalid, %d, isPreOnboardedVisit, %d, poiCategory, %@, categoryMuid, %@, placeSource, %lu, placeType, %@, mapItemPlaceType, %@, userType, %lu, predominantWeather %@,familiarityIndexLOI, %.2f, mapItem, %lu"
+ "placeTypeFromPhotoTraits"
+ "placeTypePhotoTraitLabelMetadataForThematicSummary:"
+ "planetariums"
+ "playgrounds"
+ "postAsyncProxyUsingBlock:onError:"
+ "postSyncProxyUsingBlock:onError:"
+ "preparing fetchEventBundlesWithOptions"
+ "prompt_idx"
+ "prompt_type"
+ "qualityScore"
+ "rankingCategory"
+ "rankingDictionaryIndex"
+ "rankingParams"
+ "rankingScore"
+ "reflection"
+ "rejectShortVisit"
+ "rejectSignificantContactWithHighSignificanceScore"
+ "rejectWorkVisitWithNoPhoto"
+ "rejectWorkVisitWithPhotos"
+ "remoteObjectInterface"
+ "restaurants"
+ "richnessScore"
+ "richnessScoreScalingParameter"
+ "rightExpression"
+ "rock climbing"
+ "rsvpStatus"
+ "school"
+ "schools"
+ "secondLevelActivityType"
+ "selectBirthdayFromPhotoTraits:"
+ "selectHolidayFromPhotoTraits:"
+ "sensitive"
+ "sensitiveOnRecommendedThreshold"
+ "setActivityNameForThematicSummaryFromActionName:metaData:keyword:keywordType:"
+ "setAssociatedPersonLocalIdentifiers:"
+ "setCategoryMuid:"
+ "setCelebrationHistogram:"
+ "setContainsOrganizationContact:"
+ "setDisplayName:"
+ "setHolidayHistogram:"
+ "setHolidayIdentifier:"
+ "setInviteEvent:"
+ "setInviteEventAttendees:"
+ "setInviteEventIsAllDay:"
+ "setInviteEventLocation:"
+ "setInviteEventOrganizers:"
+ "setInviteEventPlaceName:"
+ "setInviteEventTitle:"
+ "setIsMe:"
+ "setIsSensitive:"
+ "setLabelType:"
+ "setMeaningIdentifier:"
+ "setMetaDataForBirthday:metaData:eventBundle:"
+ "setMetaDataForHoliday:metaData:eventBundle:"
+ "setMetaDataForInvite:metaData:"
+ "setPhenotypePersonUUIDs:"
+ "setPhotoAssetCloudIdentifier:"
+ "setRsvpStatus:"
+ "setStateOfMindValenceHistogram:"
+ "setUpNotificationTimerWithFireDate:"
+ "shareCountThreshold"
+ "shortDescription"
+ "shortVisitDurationThresholdInSec"
+ "skate parks"
+ "skating"
+ "ski resorts"
+ "soccer fields"
+ "socialEventFromPhotoTraits"
+ "spas"
+ "stadiums"
+ "stateOfMindDomainCountThreshold"
+ "stateOfMindDomains"
+ "stateOfMindLabelCountThreshold"
+ "stateOfMindLabels"
+ "stateOfMindLoggedIn3pApp"
+ "stateOfMindLoggedInJournalApp"
+ "stateOfMindValence"
+ "stateOfMindValenceHistogram"
+ "stores"
+ "subpredicates"
+ "suggestionAcceptThreshold"
+ "suggestionAcceptThresholdForContactSubType"
+ "suggestionAcceptThresholdForContactWeeklySummarySubType"
+ "suggestionAcceptThresholdForDailyMediaVariants"
+ "suggestionAcceptThresholdForMotionActivityWalkingSubtype"
+ "suggestionAcceptThresholdForTimeAtHomeSubTypeVariants"
+ "suggestionAcceptThresholdForTripSubType"
+ "suggestionAcceptThresholdForVisitSubTypeVariants"
+ "suggestionAcceptThresholdForWeeklyMediaSummaryVariants"
+ "suggestionAcceptThresholdForWorkoutSubtype"
+ "suggestionAcceptThresholdForWorkoutWeeklySummarySubType"
+ "suggestionDeleted"
+ "suggestionQuickAdd"
+ "suggestionRecommendThreshold"
+ "suggestionRecommendThresholdForContactSubType"
+ "suggestionRecommendThresholdForContactWeeklySummarySubType"
+ "suggestionRecommendThresholdForDailyMediaVariants"
+ "suggestionRecommendThresholdForMotionActivityWalkingSubtype"
+ "suggestionRecommendThresholdForTimeAtHomeSubTypeVariants"
+ "suggestionRecommendThresholdForTripSubType"
+ "suggestionRecommendThresholdForVisitSubTypeVariants"
+ "suggestionRecommendThresholdForWeeklyMediaSummaryVariants"
+ "suggestionRecommendThresholdForWorkoutSubtype"
+ "suggestionRecommendThresholdForWorkoutWeeklySummarySubType"
+ "suggestionSelected"
+ "suggestionViewed"
+ "suggestionWasDeleted"
+ "suggestionWasViewedButNotEngaged"
+ "summarizationThresholdForMotionActivityWalkingSubType"
+ "summarizationThresholdForVisitSubTypeVariants"
+ "summarizationThresholdForWorkoutSubType"
+ "suppressCoarseSummarization"
+ "surfing spots"
+ "swimming pools"
+ "tai chi"
+ "tennis courts"
+ "theaters"
+ "thematic_summary"
+ "thematic_summary_common_activity"
+ "thematic_summary_common_place"
+ "thematic_summary_holiday"
+ "thematic_summary_photo_subject"
+ "thematic_summary_social"
+ "thematic_summary_state_of_mind"
+ "thematic_summary_subtype"
+ "timeAtHomeDurationThreshold"
+ "timeOfDayCos"
+ "timeOfDaySin"
+ "timeStringSingularToPluralForm:"
+ "times"
+ "topLevelActivityType"
+ "tripSummarizationThresholdForVisitSubType"
+ "tripSummarizationThresholdForWorkoutSubType"
+ "type == %lu"
+ "unavailable"
+ "universities"
+ "upperBoundOfEngagementScoreParams"
+ "useBirthdayLabel"
+ "useHolidayLabel"
+ "v16@?0@\"<MOAppEngagementXPCProtocol>\"8"
+ "v16@?0@\"<MOEngagementHistoryXCPProtocol>\"8"
+ "v16@?0@\"<MOPromptManagerXPCProtocol>\"8"
+ "v16@?0@8"
+ "v24@0:8@\"NSDate\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"<MOAnalyticsManagerXPCProtocol>\"8@?<B@?>16"
+ "v24@?0@\"<MOConfigurationXPCProtocol>\"8@?<B@?>16"
+ "v24@?0@\"<MOPromptManagerXPCProtocol>\"8@?<B@?>16"
+ "v24@?0@8@?<B@?>16"
+ "v40@0:8@\"NSData\"16@\"MOXPCContext\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@16@?24@?32"
+ "v40@0:8@?16@?24@?32"
+ "validateComparisonPredicate:"
+ "validateCompoundPredicate:"
+ "viewCountBasedScoreAdjustment"
+ "visibilityCategoryForUI"
+ "volleyball courts"
+ "weekOfMonthCos"
+ "weekOfMonthSin"
+ "weekOfYear"
+ "weekends"
+ "weeklySummaryMediaPlayTimeThreshold"
+ "weightBirthdayInclusion"
+ "weightForBurstyInteractionCount"
+ "weightForCallDuration"
+ "weightForContactLocationWork"
+ "weightForDistanceFromHome"
+ "weightForFamiliarityIndex"
+ "weightForGroupConversation"
+ "weightForInterestingPOI"
+ "weightForIsBusinessContact"
+ "weightForIsCoworkerContact"
+ "weightForIsFamilyContact"
+ "weightForItemFromMe"
+ "weightForLabelQualityScore"
+ "weightForMediaPlayTime"
+ "weightForMultipleInteractionTypes"
+ "weightForNumAnamolyEventsNormalized"
+ "weightForNumCoworkersNormalized"
+ "weightForNumFamilyNormalized"
+ "weightForNumFidsNormalized"
+ "weightForNumFriendsNormalized"
+ "weightForNumOtherPersonsNormalized"
+ "weightForNumPetsNormalized"
+ "weightForNumRoutineEventsNormalized"
+ "weightForNumStateOfMindEventsNormalized"
+ "weightForNumTrendEventsNormalized"
+ "weightForPCountMax"
+ "weightForPCountWeightedAverage"
+ "weightForPCountWeightedSum"
+ "weightForPDensityMax"
+ "weightForPDensityWeightedAverage"
+ "weightForSensitivePOI"
+ "weightForTimeAtHomeDuration"
+ "weightForTimeCorrelationScore"
+ "weightForViewCountBasedPenalty"
+ "weightForWorkoutDurationNormalized"
+ "weightHolidayInclusion"
+ "weightInviteEventInclusion"
+ "weightShareCountFeature"
+ "weightStateOfMindDomainCountNormalized"
+ "weightStateOfMindLabelCountNormalized"
+ "wineries"
+ "withChild"
+ "withContact"
+ "withCoworker"
+ "withFamily"
+ "withFriend"
+ "withMyPet"
+ "withProxyProvider:proxyHandler:onError:"
+ "with_contact"
+ "with_family"
+ "with_friends"
+ "with_more_than_two_contacts"
+ "with_pets"
+ "work"
+ "workoutDurationThreshold"
+ "workoutTypesSet"
+ "workouts"
+ "zoos"
- "%@: %@ %@\n"
- "<MOPhotoTrait localIdentifier, %@, name, %@, relevantAssetUUIDs, %@,>"
- "<MOPlace identifier, %@, name, %@, confidence, %f, placeType, %lu, placeUserType, %lu, preposition, %lu, locationMode, %lu, distanceToHomeInMiles, %f, poiCategory, %@, familiarityIndexLOI, %f>"
- "<MOResource identifier, %@, name, %@, type, %lu, assets, %@, data.length, %lu, value, %f"
- "@\"<MOAnalyticsManagerXPCProtocol>\""
- "@\"<MOAppEngagementXPCProtocol>\""
- "@\"<MOConfigurationXPCProtocol>\""
- "@\"<MOEngagementHistoryXCPProtocol>\""
- "@\"<MOPromptManagerXPCProtocol>\""
- "@112@0:8@16@24Q32Q40@48Q56@64d72d80d88@96@104"
- "@128@0:8@16@24@32Q40Q48@56Q64@72d80d88d96d104@112@120"
- "@248@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232@240"
- "@268@0:8@16@24@32@40@48@56B64Q68Q76@84Q92@100@108@116@124@132@140@148@156@164@172@180Q188@196B204Q208@216@224@232B240Q244Q252@260"
- "@284@0:8@16@24@32@40@48@56@64@72B80Q84Q92@100Q108@116@124@132@140@148@156@164@172@180@188@196Q204@212B220Q224@232@240@248B256Q260Q268@276"
- "@44@0:8@16B24Q28@36"
- "@88@0:8@16Q24Q32@40Q48@56d64d72d80"
- "CFBundleIdentifier"
- "Engagement event: %@, context: %{private}@"
- "Engagement reporter xpc interrupted"
- "Engagement reporter xpc invalidated"
- "Error on remote object proxy"
- "Interrupted"
- "Invalid remote syncProxy"
- "Invalidated"
- "MOAction.m"
- "MOAppEngagementReporter.m"
- "MODefaultsManager.m"
- "MODictionaryEncoder.m"
- "MOEvent.m"
- "MOEventBundle.m"
- "MOEventBundleLabelCondition.m"
- "MOEventBundleLabelFormat.m"
- "MOEventBundleLabelLocalizer.m"
- "MOEventBundleLabelTemplate.m"
- "MOEventExtendedAtrributes.m"
- "MOInteraction.m"
- "MOMediaPlaySession.m"
- "MOPlace.m"
- "MOResource.m"
- "MOTime.m"
- "MOXPCContext.m"
- "_proxy"
- "ascending, %@,  startDate, %@, endDate, %@, category, %lu, limit, %@"
- "calling fetchEventBundlesWithOption"
- "calling fetchEventBundlesWithOption completed found %@ events"
- "calling getDiagnosticReporterConfiguration:handler"
- "calling getDiagnosticReporterConfiguration:handler completed"
- "calling getMomentsNotificationsSchedule:"
- "calling getMomentsNotificationsSchedule: completed"
- "calling getTimeToWriteNotificationsScheduleWithHandler:"
- "calling getTimeToWriteNotificationsScheduleWithHandler: completed"
- "calling setupMomentsNotificationsWithSchedule:"
- "calling setupMomentsNotificationsWithSchedule: completed"
- "calling setupPeriodicTimeToWriteMomentsNotificationsUsingDateComponents"
- "calling setupPeriodicTimeToWriteMomentsNotificationsUsingDateComponents completed"
- "calling testMomentsNotifications"
- "calling testMomentsNotifications completed"
- "connection"
- "connectionProxy"
- "getTimeToWriteNotificationsApplicationScheduleWithContext:andHandler:"
- "identifier, %@, personId, %@, name, %@"
- "infoDictionary"
- "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:"
- "initWithBundleIdentifier:bundleType:creationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:photoTraits:"
- "initWithBundleIdentifier:suggestionID:bundleType:creationDate:firstCreationDate:endDate:expirationDate:events:filtered:interfaceType:photoSource:promptLanguage:source:startDate:action:concurrentMediaAction:actions:persons:place:predominantWeather:resources:time:metaDataForRank:suggestionEngagements:suggestionEngagementViewCount:appEntryEngagements:isAggregatedAndSuppressed:summarizationGranularity:places:subBundleIDs:subSuggestionIDs:includedInSummaryBundleOnly:bundleSubType:bundleSuperType:photoTraits:"
- "initWithDateInterval:ascending:category:limit:"
- "initWithIdentifier:personId:displayName:"
- "initWithIdentifier:placeName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:priorityScore:startDate:endDate:"
- "initWithPlaceName:enclosingArea:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:startDate:endDate:"
- "initWithPlaceName:placeType:placeUserType:location:locationMode:poiCategory:distanceToHomeInMiles:placeNameConfidence:familiarityIndexLOI:"
- "initiate client"
- "interactionScoredContact identifier, %@, interactionGroupName, %@, interactionContact count, %lu, interaction count, %lu, interactionMechanisms, %@"
- "logAppEntryEngagementEvent:clientIdentifier:forBundles:startTime:endTime:totalCharacters:addedCharacters:otherContext:"
- "logClientEngagementEvent:clientIdentifier:otherContext:"
- "logEngagementEvent:withContext:"
- "placeName, %@, confidence, %f, locationMode, %@, new place, %lu, isHighConfidence, %d, isInvalid, %d, isPreOnboardedVisit, %d, poiCategory, %@, placeSource, %lu, placeType, %@, mapItemPlaceType, %@, userType, %lu, predominantWeather %@,familiarityIndexLOI, %.2f, mapItem, %lu"
- "proxy"
- "resume"
- "setupPeriodicTimeToWriteMomentsNotificationsForApplication:usingDateComponents:withActionURL:withContext:andHandler:"
- "syncProxy"
- "unsignedLongValue"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">16"
- "v32@0:8@\"MOXPCContext\"16@?<v@?@\"NSDateComponents\"@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@?0@\"NSArray\"8@\"NSDictionary\"16@\"NSError\"24"
- "v32@?0@\"NSDateComponents\"8@\"NSURL\"16@\"NSError\"24"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "v56@0:8@\"NSString\"16@\"NSDateComponents\"24@\"NSURL\"32@\"MOXPCContext\"40@?<v@?@\"NSError\">48"
- "v80@0:8@16@24@32@40@48@56@64@72"

```

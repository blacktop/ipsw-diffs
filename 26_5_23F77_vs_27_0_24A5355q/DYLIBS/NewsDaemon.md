## NewsDaemon

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon`

```diff

-5883.0.0.0.0
-  __TEXT.__text: 0x288f8
-  __TEXT.__auth_stubs: 0x1310
+5916.1.0.0.0
+  __TEXT.__text: 0x28084
   __TEXT.__objc_methlist: 0xf38
-  __TEXT.__const: 0x24b8
-  __TEXT.__cstring: 0x11c9
-  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__const: 0x24a8
+  __TEXT.__cstring: 0x11d9
+  __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__oslogstring: 0x979
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__swift5_typeref: 0xa9b
+  __TEXT.__swift5_typeref: 0xa93
   __TEXT.__swift5_fieldmd: 0x7e0
   __TEXT.__constg_swiftt: 0x794
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_proto: 0x1a4
   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_capture: 0x1ac
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0xd18
-  __TEXT.__eh_frame: 0xe18
-  __TEXT.__objc_classname: 0x4ce
-  __TEXT.__objc_methname: 0x22a7
-  __TEXT.__objc_methtype: 0xe26
-  __TEXT.__objc_stubs: 0x15c0
-  __DATA_CONST.__got: 0x460
+  __TEXT.__unwind_info: 0xd00
+  __TEXT.__eh_frame: 0xe78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x8f8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x998
+  __DATA_CONST.__got: 0x458
   __AUTH_CONST.__const: 0x15b0
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x20b8
+  __AUTH_CONST.__auth_got: 0xa50
   __AUTH.__objc_data: 0x358
-  __AUTH.__data: 0x3c8
+  __AUTH.__data: 0x338
   __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0xb88
-  __DATA.__bss: 0x32f0
-  __DATA.__common: 0x20
+  __DATA.__data: 0xaa8
+  __DATA.__bss: 0x2cf0
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x6b8
-  __DATA_DIRTY.__data: 0x418
-  __DATA_DIRTY.__bss: 0x28
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__data: 0x5b8
+  __DATA_DIRTY.__bss: 0x630
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 728ABED3-629F-383C-98EF-22A921797FA5
+  UUID: 0748BE78-95A7-3F65-BA70-8052CB76637F
   Functions: 1176
-  Symbols:   1546
-  CStrings:  753
+  Symbols:   1611
+  CStrings:  215
 
Symbols:
+ _NDPrepareToAccessNewsdDataContainer
+ ___64-[NDNewsServiceConnection fetchModuleDescriptorsWithCompletion:]_block_invoke.60
+ ___71-[NDNewsServiceConnection fetchLatestResultsWithParameters:completion:]_block_invoke.64
+ ___76-[NDNewsServiceConnection _unsafeEstablishConnectionIfNeededWithCompletion:]_block_invoke.76
+ ___77-[NDNewsServiceConnection markAnalyticsElements:asSeenAtDate:withCompletion:]_block_invoke.67
+ ___block_literal_global.70
+ ___block_literal_global.75
+ ___swift__destructor
+ ___swift__destructor.4
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.41
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.51
+ ___swift_closure_destructor.7
+ ___swift_closure_destructor.7Tm
+ ___swift_closure_destructor.9
+ __swift_implicitisolationactor_to_executor_cast
+ _block_copy_helper.13
+ _block_copy_helper.14
+ _block_copy_helper.18
+ _block_copy_helper.20
+ _block_copy_helper.43
+ _block_copy_helper.56
+ _block_copy_helper.59
+ _block_copy_helper.64
+ _block_copy_helper.9
+ _block_descriptor.11
+ _block_descriptor.15
+ _block_descriptor.16
+ _block_descriptor.20
+ _block_descriptor.22
+ _block_descriptor.45
+ _block_descriptor.58
+ _block_descriptor.61
+ _block_descriptor.66
+ _block_destroy_helper.10
+ _block_destroy_helper.14
+ _block_destroy_helper.15
+ _block_destroy_helper.19
+ _block_destroy_helper.21
+ _block_destroy_helper.44
+ _block_destroy_helper.57
+ _block_destroy_helper.60
+ _block_destroy_helper.65
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x27
+ _swift_retain_x28
- GCC_except_table48
- _OUTLINED_FUNCTION_5
- ___64-[NDNewsServiceConnection fetchModuleDescriptorsWithCompletion:]_block_invoke.61
- ___71-[NDNewsServiceConnection fetchLatestResultsWithParameters:completion:]_block_invoke.65
- ___76-[NDNewsServiceConnection _unsafeEstablishConnectionIfNeededWithCompletion:]_block_invoke.78
- ___77-[NDNewsServiceConnection markAnalyticsElements:asSeenAtDate:withCompletion:]_block_invoke.68
- ___block_literal_global.71
- ___block_literal_global.76
- _block_copy_helper.10
- _block_copy_helper.11
- _block_copy_helper.16
- _block_copy_helper.19
- _block_copy_helper.49
- _block_copy_helper.57
- _block_copy_helper.60
- _block_copy_helper.65
- _block_descriptor.12
- _block_descriptor.13
- _block_descriptor.18
- _block_descriptor.21
- _block_descriptor.51
- _block_descriptor.59
- _block_descriptor.62
- _block_descriptor.67
- _block_destroy_helper.11
- _block_destroy_helper.12
- _block_destroy_helper.17
- _block_destroy_helper.20
- _block_destroy_helper.50
- _block_destroy_helper.58
- _block_destroy_helper.61
- _block_destroy_helper.66
- _objc_retain_x28
- _objectdestroy.8Tm
- _swift_bridgeObjectRetain_n
- _symbolic _____Sg 10NewsDaemon34LiveActivityScheduleRequestOptionsV
CStrings:
- "#16@0:8"
- "$__lazy_storage_$_engagement"
- ".cxx_destruct"
- "@\"<NDNewsService>\""
- "@\"<NDNewsServiceClient>\""
- "@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLArticleContentExpiration\"16@0:8"
- "@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLCohortList\"16@0:8"
- "@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLConversionStats\"16@0:8"
- "@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLTagMetadata\"16@0:8"
- "@\"FCANFDocumentManifest\"24@0:8@\"NSData\"16"
- "@\"FCContentArchive\""
- "@\"FCContentManifest\""
- "@\"FCFeedPersonalizedItemScoreProfile\"16@0:8"
- "@\"FCFeedPersonalizedItems\"40@0:8@\"NSArray\"16q24q32"
- "@\"FCFeedPersonalizedItems\"48@0:8@\"NSArray\"16q24q32@\"NSString\"40"
- "@\"FCFeedPersonalizingEnvironment\"16@0:8"
- "@\"NDANFHelper\""
- "@\"NDANFHelperProxy\""
- "@\"NFUnfairLock\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"NSArray\"16"
- "@\"NSArray\"32@0:8@\"NSArray\"16@\"FCMapTable\"24"
- "@\"NSArray\"40@0:8@\"NSArray\"16d24Q32"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDictionary\"24@0:8@\"NSArray\"16"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^B24"
- "@32@0:8@16q24"
- "@32@0:8q16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16d24Q32"
- "@40@0:8@16q24q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16q24q32@40"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "FCANFHelper"
- "FCFeedPersonalizing"
- "FCFeedPersonalizingItem"
- "FCTagRanking"
- "I"
- "I16@0:8"
- "NDANFDecodingServiceType"
- "NDANFHelper"
- "NDANFHelperProxy"
- "NDANFHelperProxyWithFallback"
- "NDAdditions"
- "NDAssertion"
- "NDDownloadConsumer"
- "NDDownloadLimits"
- "NDDownloadRequest"
- "NDDownloadService"
- "NDFeedItemPool"
- "NDFeedItemPoolFetchOptions"
- "NDManagedFeedItemPoolOptions"
- "NDNewsDaemonContext"
- "NDNewsService"
- "NDNewsServiceClient"
- "NDNewsServiceConnection"
- "NDNewsServiceConnectionClientProxy"
- "NDProxyScoringServiceConnection"
- "NDProxyTodayFeedServiceConnection"
- "NDTodayFeed"
- "NDTodayFeedConfig"
- "NDTodayFeedConfigDecodingServiceType"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<NDNewsService>\",&,N,V_daemon"
- "T@\"<NDNewsServiceClient>\",W,N,V_client"
- "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLArticleContentExpiration\",?,R,N"
- "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLCohortList\",R,N"
- "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLConversionStats\",R,N"
- "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLTagMetadata\",R,N"
- "T@\"FCContentArchive\",R,N,V_contentArchive"
- "T@\"FCContentManifest\",R,N,V_contentManifest"
- "T@\"FCFeedPersonalizedItemScoreProfile\",&"
- "T@\"FCFeedPersonalizingEnvironment\",?,R,N"
- "T@\"NDANFHelper\",R,N,V_inProcessHelper"
- "T@\"NDANFHelperProxy\",R,N,V_proxyHelper"
- "T@\"NDDownloadLimits\",R,N"
- "T@\"NDProxyScoringServiceConnection\",N,R"
- "T@\"NDProxyTodayFeedServiceConnection\",N,R"
- "T@\"NFUnfairLock\",&,N,V_xpcConnectionLock"
- "T@\"NSArray\",?,R,C,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_topStoriesArticleIDs"
- "T@\"NSArray\",R,C,N,V_topStoriesPackageURLs"
- "T@\"NSData\",?,R,N"
- "T@\"NSData\",R,N,V_configData"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDate\",R,C,N,V_publishDate"
- "T@\"NSDate\",R,N,V_publishDate"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_accessQueue"
- "T@\"NSObject<OS_os_transaction>\",R,N,V_transaction"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_contentID"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@?,C,N,V_updateResultsHandler"
- "TB,?,R,N"
- "TB,?,R,N,GisBundlePaid"
- "TB,N,R"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisANF"
- "TB,R,N,GisHiddenFromAutoFavorites"
- "TB,R,N,GisPaid"
- "TI,R,N,V_powerAssertionID"
- "TQ,?,R,N"
- "TQ,R"
- "TQ,R,N"
- "Td,?,R,N"
- "Td,R,N"
- "Tq,?,R,N"
- "Tq,N,R"
- "Tq,N,V_xpcConnectionInterest"
- "Tq,R,N,V_contentType"
- "Tq,R,N,V_maxDownloadStorage"
- "Tq,R,N,V_minDeviceStorage"
- "Tq,R,N,V_options"
- "URL"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC10NewsDaemon21ProxyFeedPersonalizer"
- "_TtC10NewsDaemon22MergedFeedItemIterator"
- "_TtC10NewsDaemon27LiveActivityScheduleRequest"
- "_TtC10NewsDaemon27NDScoringServiceEnvironment"
- "_TtC10NewsDaemon28EngagementDataEnqueueHandler"
- "_TtC10NewsDaemonP33_57384A5BC146306734585127338E266D12BundleLoader"
- "_TtC10NewsDaemonP33_5BFDE7E676D38A77D7B513724A4B1F9E23DropboxFeedItemSequence"
- "_TtP10NewsDaemon20NDScoringServiceType_"
- "_TtP10NewsDaemon22NDTodayFeedServiceType_"
- "_TtP10NewsDaemon23LiveActivityServiceType_"
- "_accessQueue"
- "_client"
- "_configData"
- "_connection"
- "_connectionToXPCService"
- "_contentArchive"
- "_contentID"
- "_contentManifest"
- "_contentType"
- "_daemon"
- "_establishConnectionIfNeededWithCompletion:"
- "_inProcessHelper"
- "_maxDownloadStorage"
- "_minDeviceStorage"
- "_options"
- "_powerAssertionID"
- "_proxyHelper"
- "_publishDate"
- "_queue"
- "_resourceIDFromURL:"
- "_resourceIDsFromURLs:"
- "_topStoriesArticleIDs"
- "_topStoriesPackageURLs"
- "_transaction"
- "_unsafeEstablishConnectionIfNeededWithCompletion:"
- "_updateResultsHandler"
- "_xpcConnection"
- "_xpcConnectionInterest"
- "_xpcConnectionLock"
- "accessQueue"
- "accessToken"
- "activate"
- "addField:object:"
- "addFinishBlock:"
- "adoptFeedConfigData:"
- "allResourcesForImageIdentifier:"
- "anf"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "articleID"
- "autorelease"
- "bag"
- "bodyTextLength"
- "boolForKey:"
- "bundleIdentifier"
- "bundlePaid"
- "cancelScheduledLiveActivityWithId:backgroundTaskID:completionHandler:"
- "class"
- "close"
- "clusterID"
- "conditionalScore"
- "conformsToProtocol:"
- "connection"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "containsValueForKey:"
- "contentType"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "d16@0:8"
- "daemon"
- "data"
- "dealloc"
- "debugDescription"
- "decayedPublisherDiversificationPenalty"
- "decodeANFDocumentData:completion:"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeTodayFeedConfigData:completion:"
- "defaultLimits"
- "defaultManager"
- "defaultScoreProfile"
- "description"
- "descriptionString"
- "distantPast"
- "documentController"
- "downloadFinishedForRequest:error:"
- "downloadProgressedForRequest:contentArchive:"
- "downloadProgressedForRequest:progress:"
- "empty"
- "enabledSources"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enqueueData:"
- "enumerateTopicCohortsWithBlock:"
- "enumerateTopicConversionStatsWithBlock:"
- "exceptionWithName:reason:userInfo:"
- "expirationData"
- "fc_arrayByTransformingWithBlock:"
- "fc_millisecondTimeIntervalUntilNow"
- "fc_removeContentsOfDirectoryAtURL:"
- "fc_safelyAddObject:"
- "feedID"
- "feedPersonalizingEnvironment"
- "fetchAggregateMapForPersonalizingItem:completion:"
- "fetchCachedTodayFeedWithCompletionHandler:"
- "fetchFeedItemPoolWithOptions:completionHandler:"
- "fetchLatestResultsWithParameters:completion:"
- "fetchModuleDescriptorsWithCompletion:"
- "fetchPlaceholderResultsWithOperationInfo:syncCompletion:"
- "firstObject"
- "float16FullBodyEncoding"
- "float16TitleEncoding"
- "flushCacheLookupsWithCompletion:"
- "flushWithCompletionHandler:"
- "forYouGroupScoreProfile"
- "globalCohorts"
- "globalConversionStats"
- "globalUserFeedback"
- "halfLife"
- "halfLifeOverride"
- "hasAudioTrack"
- "hasGlobalUserFeedback"
- "hasPrefix:"
- "hasThumbnail"
- "hasVideo"
- "hash"
- "hiddenFromAutoFavorites"
- "host"
- "iAdCategories"
- "identifier"
- "imageResourceForIdentifier:"
- "inProcessHelper"
- "init"
- "initForReadingURL:error:"
- "initWithBag:"
- "initWithChannelID:sectionID:topicID:articleListID:flags:"
- "initWithClient:"
- "initWithCoder:"
- "initWithConfigData:publishDate:contentManifest:contentArchive:"
- "initWithConfiguration:bag:"
- "initWithContentID:options:"
- "initWithFormat:"
- "initWithIdentifier:shareURL:JSONData:resourceDataSource:host:error:"
- "initWithItem:"
- "initWithMachServiceName:options:"
- "initWithMinDeviceStorage:maxDownloadStorage:"
- "initWithName:"
- "initWithName:options:"
- "initWithNonImageResourceIDs:optimalImageResourceIDs:smallestImageResourceIDs:"
- "initWithObject:"
- "initWithPublishDate:topStoriesArticleIDs:topStoriesPackageURLs:"
- "initWithServiceName:"
- "initWithStream:"
- "initWithURL:"
- "inputStream"
- "interfaceWithProtocol:"
- "invalidate"
- "invalidateCachesWith:"
- "invalidateCachesWithConfig:"
- "isAIGenerated"
- "isANF"
- "isBundlePaid"
- "isCoread"
- "isEqual:"
- "isEqualToString:"
- "isEvergreen"
- "isFeatureCandidate"
- "isFeatured"
- "isHiddenFromAutoFavorites"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPaid"
- "isProxy"
- "isSportsHighlight"
- "issueID"
- "itemID"
- "language"
- "lastModifiedDate"
- "lastPathComponent"
- "length"
- "limitItemsByFlowRate:timeInterval:publisherCount:"
- "limitItemsByMinimumItemQuality:scoreProfiles:"
- "liveActivityID"
- "lock"
- "mainBundle"
- "manifestFromANFDocumentData:"
- "manifestFromANFDocumentData:reachedService:"
- "markAnalyticsElement:asReadAtDate:withCompletion:"
- "markAnalyticsElements:asSeenAtDate:withCompletion:"
- "maxAge"
- "messageStream"
- "moveItemAtURL:toURL:error:"
- "name"
- "newsdCachesURL"
- "newsdDocumentsURL"
- "newsdGroupContainerURL"
- "nextMessage"
- "numberWithInteger:"
- "numberWithLongLong:"
- "open"
- "orderedImageIdentifiers"
- "paid"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "ping"
- "popInterest"
- "powerAssertionID"
- "preferredCount"
- "preferredOrder"
- "prepareForUseWithCompletionHandler:"
- "prewarmWithTabiScores:configurationSet:"
- "proxyConnection"
- "proxyHelper"
- "publisherCohorts"
- "publisherConversionStats"
- "publisherID"
- "publisherTagMetadata"
- "pushInterest"
- "puzzleID"
- "q"
- "q16@0:8"
- "raise:format:"
- "rankTagIDsDescending:"
- "recipeID"
- "reduceVisibility"
- "reduceVisibilityForNonFollowers"
- "registerDownloadConsumer:"
- "registerForManagedFeedItemPoolWithOptions:completionHandler:"
- "release"
- "remoteObjectInterface"
- "remoteObjectProxyWithErrorHandler:"
- "requiredNonImageResourceURLs"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "returnedIDs"
- "scheduleLiveActivityWithRequest:completionHandler:"
- "scheme"
- "scoreItems:environment:configurationSet:completion:"
- "scoreItemsIn:environment:configurationSet:completion:"
- "scoreKeyPath"
- "scoreNotificationItems:environment:completion:"
- "scoreProfile"
- "scoreProfiles"
- "scoresForTagIDs:"
- "self"
- "serviceHasNewTodayResults"
- "setAccessQueue:"
- "setAgedPersonalizationScore:"
- "setClassOfNextMessage:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClient:"
- "setConnection:"
- "setDaemon:"
- "setDefaultScoreProfile:"
- "setDownloadLimits:"
- "setDownloadRequests:"
- "setEngagementPushTopic:"
- "setExportedInterface:"
- "setExportedObject:"
- "setForYouGroupScoreProfile:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setPersonalizationScore:"
- "setRawPersonalizationScore:"
- "setRemoteObjectInterface:"
- "setScoreProfile:"
- "setScoreProfiles:"
- "setSortedItems:"
- "setTabiScore:"
- "setUpdateResultsHandler:"
- "setUserNotificationExtensionId:"
- "setWithObject:"
- "setWithObjects:"
- "setXpcConnection:"
- "setXpcConnectionInterest:"
- "setXpcConnectionLock:"
- "sharedInstance"
- "sortItems:options:configurationSet:"
- "sortItems:options:configurationSet:feedTagID:"
- "sourceFeedID"
- "streams"
- "stringByAppendingString:"
- "stringFromByteCount:countStyle:"
- "stringWithFormat:"
- "substringFromIndex:"
- "superclass"
- "supportsSecureCoding"
- "surfacedByArticleListIDs"
- "surfacedByChannelID"
- "surfacedByFlags"
- "surfacedBySectionID"
- "surfacedByTopicID"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tabiScore"
- "thumbnailPerceptualHash"
- "topicIDs"
- "topics"
- "transaction"
- "underlyingType"
- "unlock"
- "unsignedLongLongValue"
- "updateResultsHandler"
- "v16@0:8"
- "v24@0:8@\"<NDDownloadConsumer>\"16"
- "v24@0:8@\"FCCacheInvalidationConfig\"16"
- "v24@0:8@\"FCFeedPersonalizedItemScoreProfile\"16"
- "v24@0:8@\"NDDownloadLimits\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NDTodayFeed\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\"B>16"
- "v24@0:8@?<v@?@\"NSString\"@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLCohortList\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLConversionStats\">16"
- "v24@0:8q16"
- "v24@?0@\"AMSEngagementEnqueueResult\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v32@0:8@\"<FCFeedPersonalizingItem>\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"<NTTodayResultOperationInfoProviding>\"16@?<v@?@\"NTTodayResults\">24"
- "v32@0:8@\"<NTTodayResultOperationInfoProviding>\"16@?<v@?@\"NTTodayResults\"@\"NSDictionary\"@\"NSObject<NTTodayResultOperationFetchInfoProviding>\"@\"NSError\"B>24"
- "v32@0:8@\"NDDownloadRequest\"16@\"FCContentArchive\"24"
- "v32@0:8@\"NDDownloadRequest\"16@\"NSError\"24"
- "v32@0:8@\"NDDownloadRequest\"16d24"
- "v32@0:8@\"NDFeedItemPoolFetchOptions\"16@?<v@?@\"NDFeedItemPool\"@\"NSError\">24"
- "v32@0:8@\"NDManagedFeedItemPoolOptions\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"FCANFDocumentManifest\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NDTodayFeedConfig\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16q24"
- "v32@0:8@\"_TtC10NewsDaemon27LiveActivityScheduleRequest\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v40@0:8@\"<NTHeadlineAnalyticsElementProviding>\"16@\"NSDate\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDate\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"_TtC10NewsDaemon27NDScoringServiceEnvironment\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSArray\"16@\"_TtC10NewsDaemon27NDScoringServiceEnvironment\"24q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"_TtC8NewsCore19FeedItemDatabaseRef\"16@\"_TtC10NewsDaemon27NDScoringServiceEnvironment\"24q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24q32@?40"
- "webConverted"
- "withTodayFeedService:"
- "xpcConnection"
- "xpcConnectionInterest"
- "xpcConnectionLock"
- "zone"

```

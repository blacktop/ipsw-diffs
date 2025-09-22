## newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

-5345.2.0.0.0
-  __TEXT.__text: 0xb108
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x720
-  __TEXT.__objc_methname: 0x264e
-  __TEXT.__objc_classname: 0x234
-  __TEXT.__objc_methtype: 0x789
+5407.3.0.0.0
+  __TEXT.__text: 0x11670
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0x2da0
+  __TEXT.__objc_methlist: 0xb30
   __TEXT.__const: 0x1a
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__oslogstring: 0xd95
-  __TEXT.__cstring: 0xdcf
-  __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__cfstring: 0x360
-  __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x60
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__cstring: 0x10dd
+  __TEXT.__objc_methname: 0x3dd6
+  __TEXT.__oslogstring: 0x1692
+  __TEXT.__objc_classname: 0x33b
+  __TEXT.__objc_methtype: 0x1000
+  __TEXT.__unwind_info: 0x4fc
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__cfstring: 0x480
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x1e8
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA.__objc_const: 0x1910
-  __DATA.__objc_selrefs: 0x8b0
-  __DATA.__objc_ivar: 0x8c
-  __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0x488
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA.__objc_const: 0x2ff0
+  __DATA.__objc_selrefs: 0xc90
+  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x788
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NewsToday.framework/NewsToday
   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
+  - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7B33439-19BE-3BEA-965F-192AE9037D77
-  Functions: 260
-  Symbols:   159
-  CStrings:  639
+  UUID: 21EF2FDC-E563-3134-B975-56BD49150F47
+  Functions: 430
+  Symbols:   180
+  CStrings:  1023
 
Symbols:
+ _FCDispatchQueueForQualityOfService
+ _FCErrorDomain
+ _NDTodayFeedConfigDecodingServiceXPCConnection
+ _NDTodayFeedServiceXPCInterface
+ _OBJC_CLASS_$_FCAssetsFetchOperation
+ _OBJC_CLASS_$_FCOfflineAudioFetchOperation
+ _OBJC_CLASS_$_FCOfflinePuzzleFetchOperation
+ _OBJC_CLASS_$_FCOperation
+ _OBJC_CLASS_$_FCThreadSafeMutableArray
+ _OBJC_CLASS_$_NDANFHelperProxyWithFallback
+ _OBJC_CLASS_$_NDAnalyticsTelemetryUploader
+ _OBJC_CLASS_$_NDAnalyticsUploadFrameworkAssembly
+ _OBJC_CLASS_$_NDDownloadLimits
+ _OBJC_CLASS_$_NDTodayFeed
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSURLCache
+ _OBJC_CLASS_$_TFContainer
+ _OBJC_METACLASS_$_FCOperation
+ ___NSDictionary0__struct
+ _objc_retain_x9
+ _objc_unsafeClaimAutoreleasedReturnValue
- _OBJC_CLASS_$_NDANFParsingService
- _OBJC_CLASS_$_NSUserDefaults
CStrings:
+ "\a"
+ "\x11"
+ "\x11\x12"
+ "\x1c"
+ "%llu"
+ "%p"
+ "+\x14"
+ "-[NDContentDownloadService initWithContentContext:ANFHelper:]"
+ "-[NDContentDownloadService registerDownloadConsumer:]_block_invoke"
+ "-[NDContentDownloadService setCurrentConnection:]"
+ "-[NDTodayFeedServiceListenerDelegate init]"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/NDTodayFeedServiceListenerDelegate.m"
+ "@\"<FCANFHelper>\""
+ "@\"<FCAVAssetFactoryType>\"16@0:8"
+ "@\"<FCAVAssetPrewarming>\"16@0:8"
+ "@\"<FCBackgroundTaskable>\"16@0:8"
+ "@\"<FCContentContextInternal>\"16@0:8"
+ "@\"<FCCoreConfiguration>\"16@0:8"
+ "@\"<FCCoreConfigurationManager>\"16@0:8"
+ "@\"<FCCoreConfigurationManager><FCNewsAppConfigurationManager>\"16@0:8"
+ "@\"<FCFeedDatabaseProtocol>\"16@0:8"
+ "@\"<FCJSONRecordSourceType>\"24@0:8@\"FCJSONRecordSourceSchema\"16"
+ "@\"<FCJSONRecordTreeSourceType>\"24@0:8@\"NSArray\"16"
+ "@\"<FCMagazinesConfigurationManager>\"16@0:8"
+ "@\"<FCNetworkReachabilityType>\"16@0:8"
+ "@\"<FCNewsAppConfiguration>\"16@0:8"
+ "@\"<FCNewsAppConfiguration><FCJSONEncodableObjectProviding>\"16@0:8"
+ "@\"<FCNewsAppConfigurationManager>\"16@0:8"
+ "@\"<FCPPTContext>\"16@0:8"
+ "@\"FCANFDocumentManifest\"24@0:8@\"NSData\"16"
+ "@\"FCArticleController\"16@0:8"
+ "@\"FCAssetManager\"16@0:8"
+ "@\"FCFlintResourceManager\"16@0:8"
+ "@\"FCHeldRecords\"24@0:8@\"NSArray\"16"
+ "@\"FCInterestToken\"24@0:8@\"FCContentManifest\"16"
+ "@\"FCPuzzleController\"16@0:8"
+ "@\"FCPuzzleTypeController\"16@0:8"
+ "@\"FCSportsEventController\"16@0:8"
+ "@\"FCTagController\"16@0:8"
+ "@\"FCThreadSafeMutableArray\""
+ "@\"NDDownloadConsumerProxy\""
+ "@\"NDDownloadLimits\""
+ "@\"NDTodayFeedConfig\""
+ "@\"NDTodayFeedManager\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "@\"NSOperationQueue\""
+ "@\"NSURL\""
+ "@\"NSURL\"16@0:8"
+ "@16@?0@\"<TFResolver>\"8"
+ "@16@?0@\"NSURL\"8"
+ "@?"
+ "@?16@0:8"
+ "@?<v@?@\"FCContentArchive\">16@0:8"
+ "@?<v@?@@\"NSError\">16@0:8"
+ "@?<v@?d>16@0:8"
+ "ANFHelper"
+ "B16@?0@\"NSString\"8"
+ "FCANFHelper"
+ "FCContentContext"
+ "FCCoreConfigurationManager"
+ "FCFeldsparIDProvider"
+ "FCNewsAppConfigurationManager"
+ "FCOfflineFetchOperationType"
+ "NDAssembly"
+ "NDOfflineTodayFeedOperation"
+ "NDTodayFeedManager"
+ "NDTodayFeedService"
+ "NDTodayFeedServiceListenerDelegate"
+ "T@\"<FCANFHelper>\",R,N,V_ANFHelper"
+ "T@\"<FCAVAssetFactoryType>\",R,N"
+ "T@\"<FCAVAssetPrewarming>\",R,N"
+ "T@\"<FCBackgroundTaskable>\",R,W,N"
+ "T@\"<FCContentContextInternal>\",R,N"
+ "T@\"<FCCoreConfiguration>\",R,N"
+ "T@\"<FCCoreConfigurationManager>\",R,N"
+ "T@\"<FCFeedDatabaseProtocol>\",R,N"
+ "T@\"<FCNetworkReachabilityType>\",R,N"
+ "T@\"<FCNewsAppConfiguration>\",?,R,N"
+ "T@\"<FCNewsAppConfiguration>\",R,N"
+ "T@\"<FCNewsAppConfiguration><FCJSONEncodableObjectProviding>\",?,R,N"
+ "T@\"<FCNewsAppConfigurationManager>\",R,N"
+ "T@\"<FCPPTContext>\",R,N"
+ "T@\"FCArticleController\",R,N"
+ "T@\"FCAssetManager\",R,N"
+ "T@\"FCFlintResourceManager\",R,N"
+ "T@\"FCPuzzleController\",R,N"
+ "T@\"FCPuzzleTypeController\",R,N"
+ "T@\"FCSportsEventController\",R,N"
+ "T@\"FCTagController\",R,N"
+ "T@\"FCThreadSafeMutableArray\",R,N,V_resultErrors"
+ "T@\"FCThreadSafeMutableArray\",R,N,V_resultInterestTokens"
+ "T@\"NDContentArchiveStore\",R,N,V_archiveStore"
+ "T@\"NDDownloadConsumerProxy\",&,N,V_currentConsumer"
+ "T@\"NDDownloadLimits\",&,N"
+ "T@\"NDDownloadLimits\",&,N,V_downloadLimits"
+ "T@\"NDTodayFeedConfig\",R,N,V_feedConfig"
+ "T@\"NDTodayFeedManager\",R,N,V_todayFeedManager"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSMutableArray\",R,N,V_interestTokens"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,VarchiveQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,VfetchCompletionQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,VprogressQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSOperationQueue\",R,N,V_operationQueue"
+ "T@\"NSOperationQueue\",R,N,V_serialQueue"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSString\",R,C,N,V_connectionDescription"
+ "T@\"NSString\",R,C,N,V_parentDirectory"
+ "T@\"NSString\",R,N,V_rootDirectory"
+ "T@\"NSURL\",R,C,N,V_contentHostDirectoryFileURL"
+ "T@\"NSURL\",R,N"
+ "T@?,C,N"
+ "T@?,C,N,VarchiveHandler"
+ "T@?,C,N,VfetchCompletionHandler"
+ "T@?,C,N,VprogressHandler"
+ "TB,N"
+ "TB,N,VcachedOnly"
+ "TFAssembly"
+ "Td,V_progress"
+ "TodayFeedService XPC connection interrupted, connection=%{public}@"
+ "TodayFeedService XPC connection invalidated, connection=%{public}@"
+ "TodayFeedService did enter operation queue (instance=%{public}@)"
+ "TodayFeedService failed to adopt feed config data"
+ "TodayFeedService failed to decode config data with XPC error: %{public}@"
+ "TodayFeedService failed to decode config data with error: %{public}@"
+ "TodayFeedService failed to download feed contents, error=%{public}@"
+ "TodayFeedService successfully decoded config data, publishDate=%{public}@, articles=%lu, packages=%lu, time=%llums"
+ "TodayFeedService successfully downloaded feed contents, id=%{public}@"
+ "TodayFeedService will accept new XPC connection, connection=%{public}@, serviceName=%{public}@"
+ "TodayFeedService will adopt feed config data, length=%lu"
+ "TodayFeedService will begin downloading feed contents, id=%{public}@"
+ "TodayFeedService will enter operation queue (instance=%{public}@)"
+ "TodayFeedService will ignore feed config because it's already downloaded, id=%{public}@"
+ "TodayFeedService will reject donated config due to low-data mode"
+ "TodayFeedService will reject donated config due to low-power mode"
+ "Tq,R,N"
+ "URLSessionQueue"
+ "XPC connection interrupted, connection=%{public}@"
+ "XPC connection invalidated, connection=%{public}@"
+ "_ANFHelper"
+ "_archiveStore"
+ "_audioOperationForRequest:"
+ "_blobPathForName:contentID:"
+ "_canAdoptFeedConfig"
+ "_configFromData:"
+ "_connectionDescription"
+ "_contentHostDirectoryFileURL"
+ "_contentIDForConfig:"
+ "_downloadLimits"
+ "_feedConfig"
+ "_filePathForKey:"
+ "_handleArchive:"
+ "_handleError:"
+ "_handleInterestToken:"
+ "_hasReachedStorageLimits"
+ "_interestTokens"
+ "_isContentIDComplete:"
+ "_latestTodayFeed"
+ "_mostRecentContentID"
+ "_operationQueue"
+ "_parentDirectory"
+ "_progress"
+ "_publishDateFromContentID:"
+ "_puzzleOperationForRequest:"
+ "_queue"
+ "_resultErrors"
+ "_resultInterestTokens"
+ "_rootDirectory"
+ "_serialQueue"
+ "_storageUsedByDownloads"
+ "_todayFeedForContentID:"
+ "_todayFeedManager"
+ "_updateProgress:"
+ "activate"
+ "addAppConfigObserver:"
+ "addBlob:name:contentID:"
+ "adoptFeedConfigData:"
+ "aggregateArchiveForContentID:"
+ "allCompleteContentIDs"
+ "allKeys"
+ "appConfiguration"
+ "appConfigurationManager"
+ "archiveHandler"
+ "archiveQueue"
+ "archiveStore"
+ "archiveWithChildArchives:"
+ "articleController"
+ "articleID"
+ "assetCacheDirectoryURL"
+ "assetHandleForURL:lifetimeHint:"
+ "assetManager"
+ "associateChildOperation:"
+ "avAssetFactory"
+ "avAssetPrewarmer"
+ "available device storage has reached minimum, available=%{public}@, minimum=%{public}@"
+ "backgroundTaskable"
+ "blobWithName:contentID:"
+ "bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:"
+ "bookmarkForBlobWithName:contentID:"
+ "cachedOnly"
+ "com.apple.news.NDTodayFeedManager"
+ "com.apple.newsd.download.todayFeedSerial"
+ "com.apple.newsd.today-feed"
+ "compare:options:"
+ "config"
+ "configuration"
+ "connectionDescription"
+ "consumer proxy did send message, connection=%{public}@"
+ "consumer proxy lost connection, will drop %lu messages, connection=%{public}@"
+ "consumer proxy will send message, connection=%{public}@"
+ "content archive store added blob for name=%{public}@, contentID=%{public}@, manifestPath=%{public}@"
+ "content archive store failed to add blob for name=%{public}@, contentID=%{public}@, error=%{public}@"
+ "content archive store failed to generate blob bookmark for name=%{public}@, contentID=%{public}@, error=%{public}@"
+ "contentEnvironment"
+ "contentEnvironmentToken"
+ "contentHostDirectoryFileURL"
+ "contentHostDirectoryURL"
+ "contentStoreFrontID"
+ "convertRecords:"
+ "decodeTodayFeedConfigData:completion:"
+ "defaultLimits"
+ "download storage has reached maximum, used=%{public}@, maximum=%{public}@"
+ "downloadLimits"
+ "empty"
+ "enableFlushingWithFlushingThreshold:exceptForFlusher:"
+ "errorWithDomain:code:userInfo:"
+ "failed to load last known limits from store with error: %{public}@"
+ "failed to save last known limits to store with error: %{public}@"
+ "fc_addAsyncOperationWithBlock:"
+ "fc_dateWithMillisecondTimeIntervalSince1970:"
+ "fc_fileSystemFreeSize"
+ "fc_millisecondTimeIntervalSince1970"
+ "fc_millisecondTimeIntervalUntilNow"
+ "fc_sizeOfItemAtURL:error:"
+ "fc_unsignedLongLongValue"
+ "feedConfig"
+ "feedDatabase"
+ "feldsparID"
+ "fetchAppConfigurationIfNeededWithCompletion:"
+ "fetchAppConfigurationIfNeededWithCompletionQueue:completion:"
+ "fetchAppWidgetConfigurationWithTodayLiteConfig:additionalFields:completion:"
+ "fetchCachedTodayFeedWithCompletion:"
+ "fetchCompletionHandler"
+ "fetchCompletionQueue"
+ "fetchConfigurationIfNeededWithCompletion:"
+ "fetchConfigurationIfNeededWithCompletionQueue:completion:"
+ "fetchedAppConfiguration"
+ "finishedPerformingOperationWithError:"
+ "flintResourceManager"
+ "flushMessagesWithCompletion:"
+ "flushWithCompletion:"
+ "found no last known limits in store"
+ "inScope:"
+ "initWithAppConfigurationManager:telemetryUploader:storeDirectoryFileURL:URLSessionQueue:"
+ "initWithAssetHandles:"
+ "initWithBundleAssemblies:assemblies:"
+ "initWithConfigData:publishDate:contentManifest:contentArchive:"
+ "initWithConfiguration:configurationManager:contentHostDirectory:networkBehaviorMonitor:networkReachability:desiredHeadlineFieldOptions:feedUsage:assetKeyManagerDelegate:appActivityMonitor:backgroundTaskable:pptContext:"
+ "initWithConfigurationManager:cachesDirectoryURL:networkReachability:"
+ "initWithContentContext:ANFHelper:"
+ "initWithContentHostDirectoryFileURL:"
+ "initWithContext:ANFHelper:"
+ "initWithContext:ANFHelper:articleID:"
+ "initWithContext:ANFHelper:issueID:"
+ "initWithContext:articleID:"
+ "initWithContext:puzzleID:"
+ "initWithFeedConfig:context:ANFHelper:"
+ "initWithMemoryCapacity:diskCapacity:diskPath:"
+ "initWithParentDirectory:"
+ "initWithParentDirectory:name:"
+ "interestTokens"
+ "internalContentContext"
+ "invalidate"
+ "isFinished"
+ "issueID"
+ "jsonEncodableAppConfiguration"
+ "last-known-limits"
+ "lastKnownLimits"
+ "length"
+ "loadInRegistry:"
+ "magazinesConfigurationManager"
+ "manifestFromANFDocumentData:"
+ "maxDownloadStorage"
+ "minDeviceStorage"
+ "networkReachability"
+ "networkReachabilityConnectivityDidChange:"
+ "news_core_ConfigurationManager"
+ "operationQueue"
+ "operationWillFinishWithError:"
+ "parentDirectory"
+ "performOperation"
+ "popInterest"
+ "possiblyUnfetchedAppConfiguration"
+ "pptContext"
+ "ppt_overrideFeedEndpoint:"
+ "ppt_prewarmFeedDatabase"
+ "privateContainer"
+ "progress"
+ "progressHandler"
+ "progressQueue"
+ "publicContainer"
+ "publishDate"
+ "pushInterest"
+ "puzzleController"
+ "puzzleID"
+ "puzzleTypeController"
+ "q16@0:8"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "qualityOfService"
+ "queue"
+ "readOnlyArray"
+ "recordSourceWithSchema:"
+ "recordTreeSourceWithRecordSources:"
+ "refreshAppConfigurationIfNeededWithCompletionQueue:refreshCompletion:"
+ "registerClass:factory:"
+ "registerProtocol:factory:"
+ "registerUserInfo:"
+ "registering a consumer without an XPC connection"
+ "removeAppConfigObserver:"
+ "removeObserver:"
+ "replacing XPC connection while a consumer is already active"
+ "replacing download limits with limits=%{public}@"
+ "resolveClass:"
+ "resolveProtocol:"
+ "resolver"
+ "resultErrors"
+ "resultInterestTokens"
+ "rootDirectory"
+ "save"
+ "segmentSetIDs"
+ "serialQueue"
+ "serviceName"
+ "setCachePolicy:"
+ "setDownloadLimits:"
+ "setInterestTokenHandler:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setLastKnownLimits:"
+ "setMaxConcurrentFetchCount:"
+ "setProgress:"
+ "setSharedURLCache:"
+ "setShouldFailOnMissingObjects:"
+ "setUnderlyingQueue:"
+ "sortedArrayUsingComparator:"
+ "sportsEventController"
+ "storageSize"
+ "stringFromByteCount:countStyle:"
+ "successfully loaded last known limits from store: %{public}@"
+ "successfully saved last known limits to store"
+ "supportedContentStoreFrontID"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "tabiModelsContentDirectory"
+ "tabiResourcesContentDirectory"
+ "tagController"
+ "today-feed"
+ "todayFeedManager"
+ "topStoriesArticleIDs"
+ "topStoriesPackageURLs"
+ "treatmentIDs"
+ "v16@?0@\"FCInterestToken\"8"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"<FCCoreConfigurationObserving>\"16"
+ "v24@0:8@\"<FCFeldsparIDProviderObserving>\"16"
+ "v24@0:8@\"<FCNetworkReachabilityType>\"16"
+ "v24@0:8@\"<FCNewsAppConfigurationObserving>\"16"
+ "v24@0:8@\"<TFContainerRegistry>\"16"
+ "v24@0:8@\"FCUserInfo\"16"
+ "v24@0:8@\"NDDownloadLimits\"16"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
+ "v24@0:8@?<v@?@\"<FCCoreConfiguration>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<FCNewsAppConfiguration>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"FCContentArchive\">16"
+ "v24@0:8@?<v@?@\"NDTodayFeed\"@\"NSError\">16"
+ "v24@0:8@?<v@?@@\"NSError\">16"
+ "v24@0:8@?<v@?d>16"
+ "v24@0:8q16"
+ "v24@?0@\"<TFResolver>\"8@\"NDAnalyticsEnvelopeManager\"16"
+ "v24@?0@\"NDTodayFeedConfig\"8@\"NSError\"16"
+ "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"<FCCoreConfiguration>\"@\"NSError\">24"
+ "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"<FCNewsAppConfiguration>\"@\"NSError\">24"
+ "v32@0:8Q16@\"<FCCacheFlushing>\"24"
+ "v32@0:8Q16@24"
+ "v36@0:8B16@\"NSDictionary\"20@?<v@?@\"<FCNewsAppConfiguration>\"@\"NSDictionary\"@\"NSData\"@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@16@24@32"
+ "will accept new XPC connection, connection=%{public}@, serviceName=%{public}@"
+ "will limit further downloads due to insufficient storage"
+ "withConfiguration:"
- "\x11\x11"
- "\x11\x18\x14"
- "-[NDContentDownloadService initWithContentContext:]"
- "@\"<FCFlintHelper>\""
- "T@\"<FCFlintHelper>\",R,N,V_flintHelper"
- "T@\"<NDDownloadConsumer>\",&,N,V_currentConsumer"
- "_flintHelper"
- "fc_subarrayWithMaxCount:"
- "flintHelper"
- "initWithAppConfigurationManager:storeDirectoryFileURL:URLSessionQueue:"
- "initWithConfiguration:configurationManager:contentHostDirectory:networkBehaviorMonitor:desiredHeadlineFieldOptions:feedUsage:assetKeyManagerDelegate:appActivityMonitor:backgroundTaskable:pptContext:"
- "initWithConfigurationManager:cachesDirectoryURL:"
- "initWithContext:"
- "initWithContext:flintHelper:articleID:"
- "initWithContext:flintHelper:issueID:"
- "setIsBackgroundDownloadOperation:"
- "standardUserDefaults"
- "v24@0:8@\"FCNetworkReachability\"16"
- "will limit further downloads from %lu to %lu while waiting for a consumer"

```

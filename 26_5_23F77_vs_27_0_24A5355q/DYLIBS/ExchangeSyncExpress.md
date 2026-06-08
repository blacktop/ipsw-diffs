## ExchangeSyncExpress

> `/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress`

```diff

-2074.80.2.0.0
-  __TEXT.__text: 0xd004
-  __TEXT.__auth_stubs: 0x530
+2075.0.0.0.0
+  __TEXT.__text: 0xc5d0
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__gcc_except_tab: 0x940
-  __TEXT.__cstring: 0x64f
+  __TEXT.__gcc_except_tab: 0x7fc
+  __TEXT.__cstring: 0x659
   __TEXT.__const: 0x60
   __TEXT.__oslogstring: 0x112c
-  __TEXT.__unwind_info: 0x3c8
-  __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methname: 0x185d
-  __TEXT.__objc_methtype: 0x2e7
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x4b0
+  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x570
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x4b0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x860
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 22717A70-B737-3C17-8741-D172701FE96B
+  UUID: 5F5E29F6-88F6-3586-8540-A322AA7B64E5
   Functions: 191
-  Symbols:   891
-  CStrings:  409
+  Symbols:   894
+  CStrings:  149
 
Symbols:
+ ___120-[ESDConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.155
+ ___120-[ESDConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.157
+ ___130-[ESDConnection requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:]_block_invoke.151
+ ___130-[ESDConnection requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:]_block_invoke.153
+ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.104
+ ___97-[ESDConnection respondToSharedCalendarInvite:forCalendarWithID:accountID:queue:completionBlock:]_block_invoke.143
+ ___98-[ESDConnection beginDownloadingAttachmentWithUUID:accountID:queue:progressBlock:completionBlock:]_block_invoke.139
+ ___99-[ESDConnection reportSharedCalendarInviteAsJunkForCalendarWithID:accountID:queue:completionBlock:]_block_invoke.144
+ ___block_literal_global.123
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
- ___120-[ESDConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.156
- ___120-[ESDConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.158
- ___130-[ESDConnection requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:]_block_invoke.152
- ___130-[ESDConnection requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:]_block_invoke.154
- ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.110
- ___97-[ESDConnection respondToSharedCalendarInvite:forCalendarWithID:accountID:queue:completionBlock:]_block_invoke.144
- ___98-[ESDConnection beginDownloadingAttachmentWithUUID:accountID:queue:progressBlock:completionBlock:]_block_invoke.140
- ___99-[ESDConnection reportSharedCalendarInviteAsJunkForCalendarWithID:accountID:queue:completionBlock:]_block_invoke.145
- ___block_literal_global.124
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8@?16@?24"
- "@48@0:8@16@24@32@?40"
- "@56@0:8@16@24@32@?40@?48"
- "@64@0:8@16@24@32Q40@?48@?56"
- "@72@0:8@16@24@32@40@48@?56@?64"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B32@0:8@16@24"
- "B32@0:8@16q24"
- "B36@0:8@16@24B32"
- "B36@0:8@16q24B32"
- "B40@0:8@16@24q32"
- "B40@0:8@16q24B32B36"
- "B44@0:8@16@24q32B40"
- "B48@0:8@16@24@32@40"
- "B56@0:8@16@24@32@40@48"
- "ESDAMContainerIDCacheKey"
- "ESDConnection"
- "ESDownloadContext"
- "ESECalendarAvailabilityContext"
- "ESECalendarDirectorySearchContext"
- "ESSharedCalendarContext"
- "NSCopying"
- "Q16@0:8"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",R,N,V_accountID"
- "T@\"NSString\",R,N,V_attachmentUUID"
- "T@\"NSString\",R,N,V_calendarID"
- "T@?,R,C,N,V_completionBlock"
- "T@?,R,C,N,V_progressBlock"
- "TB,N,V_registered"
- "TB,N,V_shouldSyncCalendar"
- "Tq,R,N,V_dataclass"
- "UTF8String"
- "_accountID"
- "_accountIdsWithAlreadyResetCerts"
- "_accountIdsWithAlreadyResetThrottleTimers"
- "_attachmentUUID"
- "_calendarAvailabilityRequestFinished:"
- "_calendarAvailabilityRequestReturnedResults:"
- "_calendarDirectorySearchFinished:"
- "_calendarDirectorySearchReturnedResults:"
- "_calendarID"
- "_cancelDownloadsWithIDs:error:"
- "_completionBlock"
- "_connExchange"
- "_connectionForExchange"
- "_createReplyToRequest:withProperties:"
- "_dataclass"
- "_dispatchMessage:"
- "_downloadFinished:"
- "_downloadProgress:"
- "_exchangeServerDiedWithReason:"
- "_folderChangeFinished:"
- "_foldersUpdated:"
- "_getStatusReportsFromClient:"
- "_hasConnectionForExchange"
- "_inFlightAttachmentDownloads"
- "_inFlightCalendarAvailabilityRequests"
- "_inFlightCalendarDirectorySearches"
- "_inFlightFolderChanges"
- "_inFlightOofSettingsRequests"
- "_inFlightSearchQueries"
- "_inFlightShareRequests"
- "_init"
- "_initializeConnectionWithXPCEndpoint:"
- "_initializeExchangeConnection"
- "_initializeXPCConnection:"
- "_initializeXPCConnectionForExchange:"
- "_logDataAccessStatus:"
- "_muckingWithConn"
- "_muckingWithInFlightCollections"
- "_nextStopMonitoringStatusToken"
- "_oofSettingsRequestsFinished:"
- "_performOofSettingsRequest:forAccountWithID:forUpdate:"
- "_policyKeyChanged:"
- "_progressBlock"
- "_queue"
- "_registerForAppResumedNotification"
- "_registered"
- "_requestDaemonChangeAgentMonitoringStatus:withToken:waitForReply:"
- "_resetCertWarningsForAccountId:andDataclasses:isUserRequested:"
- "_resetThrottleTimersForAccountId:"
- "_resultsBlock"
- "_sendSynchronousXPCMessageWithParameters:handlerBlock:"
- "_serverContactsSearchQueryFinished:"
- "_serverDiedWithReason:"
- "_shareResponseFinished:"
- "_shouldSyncCalendar"
- "_statusReportBlock"
- "_tearDownInFlightObjects"
- "_validateXPCReply:"
- "absoluteString"
- "activeSyncDeviceIdentifier"
- "addObject:"
- "addObserver:selector:name:object:"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "archivedDataWithRootObject:"
- "arrayWithObjects:count:"
- "asyncProcessMeetingRequests:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:forAccountWithId:"
- "beginDownloadingAttachmentWithUUID:accountID:queue:progressBlock:completionBlock:"
- "boolValue"
- "cancelCalendarAvailabilityRequestWithID:"
- "cancelCalendarDirectorySearchWithID:"
- "cancelDownloadingAttachmentWithDownloadID:error:"
- "cancelServerContactsSearch:"
- "compare:"
- "completionBlock"
- "consumer"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentPolicyKeyForAccountID:"
- "dataclass"
- "dealloc"
- "decodeObjectOfClasses:forKey:"
- "decodedErrorFromData:"
- "defaultCenter"
- "description"
- "dictionaryRepresentation"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "externalIdentificationForAccountID:resultsBlock:"
- "fillOutCurrentEASTimeZoneInfo"
- "finishedWithError:"
- "finishedWithError:exceededResultLimit:"
- "folderChange:finishedWithStatus:error:"
- "handleURL:"
- "hash"
- "init"
- "initForReadingFromData:error:"
- "initWithAccountID:andDataclass:"
- "initWithArray:"
- "initWithAttachmentUUID:accountID:queue:downloadProgressBlock:completionBlock:"
- "initWithCalendarID:accountID:queue:completionBlock:"
- "initWithCapacity:"
- "initWithDictionary:"
- "initWithObjectsAndKeys:"
- "initWithResultsBlock:completionBlock:"
- "intValue"
- "integerValue"
- "isEqual:"
- "isEqualToString:"
- "isOofSettingsSupportedForAccountWithID:completionBlock:"
- "length"
- "longLongValue"
- "makeObjectsPerformSelector:withObject:"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "oofRequestInfo:finishedWithResult:error:"
- "performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:"
- "performServerContactsSearch:forAccountWithID:"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "processFolderChange:forAccountWithID:"
- "processMeetingRequests:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:forAccountWithId:"
- "progressBlock"
- "q"
- "q16@0:8"
- "queue"
- "raise"
- "reallyRegisterForInterrogation"
- "registerForInterrogationWithBlock:"
- "registered"
- "removeAllObjects"
- "removeObjectForKey:"
- "removeObserver:"
- "reportFolderItemsSyncSuccess:forFolderWithID:withItemsCount:andAccountWithID:"
- "reportSharedCalendarInviteAsJunkForCalendarWithID:accountID:queue:completionBlock:"
- "requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:"
- "requestDaemonShutdown"
- "requestDaemonStartMonitoringAgentsSyncWithToken:"
- "requestDaemonStartMonitoringAgentsWithToken:"
- "requestDaemonStopMonitoringAgents"
- "requestDaemonStopMonitoringAgentsSync"
- "requestPolicyUpdateForAccountID:"
- "resetTimersAndWarnings"
- "respondToSharedCalendarInvite:forCalendarWithID:accountID:queue:completionBlock:"
- "resultsReturned:"
- "resumeWatchingFoldersWithKeys:forAccountID:"
- "retrieveOofSettingsRequest:forAccountWithID:"
- "searchID"
- "searchString"
- "sendFinishedToConsumerWithError:"
- "sendResultsToConsumer:"
- "setConsumer:"
- "setDisplayName:"
- "setFolderId:"
- "setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:forAccountID:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setRegistered:"
- "setRequestID:"
- "setSearchID:"
- "setShouldSyncCalendar:"
- "setState:"
- "setWithObjects:"
- "sharedConnection"
- "shouldSyncCalendar"
- "statusReports"
- "stopWatchingFoldersWithKeys:forAccountID:"
- "stringWithFormat:"
- "suspendWatchingFoldersWithKeys:forAccountID:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unsignedIntegerValue"
- "updateContentsOfAllFoldersForAccountID:andDataclass:"
- "updateContentsOfAllFoldersForAccountID:andDataclass:isUserRequested:"
- "updateContentsOfAllFoldersForAccountID:andDataclasses:isUserRequested:"
- "updateContentsOfFoldersWithKeys:forAccountID:andDataclass:"
- "updateContentsOfFoldersWithKeys:forAccountID:andDataclass:isUserRequested:"
- "updateContentsOfFoldersWithKeys:forAccountID:andDataclasses:isUserRequested:"
- "updateFolderListForAccountID:andDataclasses:"
- "updateFolderListForAccountID:andDataclasses:isUserRequested:"
- "updateFolderListForAccountID:andDataclasses:requireChangedFolders:isUserRequested:"
- "updateOofSettingsRequest:forAccountWithID:"
- "updateProgressDownloadedByteCount:totalByteCount:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8B16Q20B28"
- "v32@0:8q16q24"
- "v36@0:8@16q24B32"
- "v44@0:8B16@20Q28@36"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8q16@24@32@40@?48"
- "watchFoldersWithKeys:forAccountID:"
- "watchFoldersWithKeys:forAccountID:persistent:"

```

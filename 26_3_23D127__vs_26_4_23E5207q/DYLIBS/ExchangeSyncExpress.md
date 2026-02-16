## ExchangeSyncExpress

> `/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress`

```diff

-2074.60.1.0.0
-  __TEXT.__text: 0xcc04
-  __TEXT.__auth_stubs: 0x560
+2074.80.2.0.0
+  __TEXT.__text: 0xd004
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__gcc_except_tab: 0x96c
+  __TEXT.__gcc_except_tab: 0x940
   __TEXT.__cstring: 0x64f
   __TEXT.__const: 0x60
   __TEXT.__oslogstring: 0x112c
-  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0xa6
   __TEXT.__objc_methname: 0x185d
   __TEXT.__objc_methtype: 0x2e7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x570
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0CD86684-A5E0-3A8B-87D1-414AA84E1185
+  UUID: 7793921A-855B-3ABA-8A26-AD8E742E3C30
   Functions: 191
-  Symbols:   894
+  Symbols:   891
   CStrings:  409
 
Symbols:
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
Functions:
~ -[ESECalendarAvailabilityContext initWithResultsBlock:completionBlock:] : 156 -> 152
~ -[ESECalendarDirectorySearchContext initWithResultsBlock:completionBlock:] : 156 -> 152
~ -[ESDAMContainerIDCacheKey isEqual:] : 160 -> 164
~ -[ESDownloadContext initWithAttachmentUUID:accountID:queue:downloadProgressBlock:completionBlock:] : 284 -> 260
~ -[ESDownloadContext updateProgressDownloadedByteCount:totalByteCount:] : 372 -> 384
~ -[ESDownloadContext finishedWithError:] : 364 -> 372
~ -[ESSharedCalendarContext initWithCalendarID:accountID:queue:completionBlock:] : 240 -> 228
~ -[ESSharedCalendarContext finishedWithError:] : 484 -> 496
~ ___45-[ESSharedCalendarContext finishedWithError:]_block_invoke : 188 -> 196
~ -[ESDConnection _tearDownInFlightObjects] : 2680 -> 2716
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke : 180 -> 188
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.105 : 180 -> 188
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.106 : 180 -> 188
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.107 : 180 -> 188
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.108 : 180 -> 188
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.109 : 180 -> 188
~ ___41-[ESDConnection _tearDownInFlightObjects]_block_invoke.110 : 180 -> 188
~ -[ESDConnection _serverDiedWithReason:] : 304 -> 316
~ -[ESDConnection _exchangeServerDiedWithReason:] : 304 -> 316
~ -[ESDConnection _connectionForExchange] : 240 -> 236
~ ___39-[ESDConnection _connectionForExchange]_block_invoke : 84 -> 92
~ -[ESDConnection _initializeExchangeConnection] : 336 -> 344
~ -[ESDConnection _initializeConnectionWithXPCEndpoint:] : 152 -> 160
~ ___54-[ESDConnection _initializeConnectionWithXPCEndpoint:]_block_invoke : 288 -> 292
~ ___42-[ESDConnection _initializeXPCConnection:]_block_invoke : 152 -> 160
~ ___53-[ESDConnection _initializeXPCConnectionForExchange:]_block_invoke : 152 -> 160
~ -[ESDConnection _createReplyToRequest:withProperties:] : 192 -> 188
~ -[ESDConnection decodedErrorFromData:] : 536 -> 552
~ ___35-[ESDConnection _policyKeyChanged:]_block_invoke : 464 -> 488
~ ___33-[ESDConnection _foldersUpdated:]_block_invoke : 468 -> 492
~ ___38-[ESDConnection _logDataAccessStatus:]_block_invoke : 88 -> 92
~ -[ESDConnection _serverContactsSearchQueryFinished:] : 1332 -> 1364
~ ___52-[ESDConnection _serverContactsSearchQueryFinished:]_block_invoke : 260 -> 268
~ -[ESDConnection _folderChangeFinished:] : 836 -> 876
~ ___39-[ESDConnection _folderChangeFinished:]_block_invoke : 260 -> 268
~ ___45-[ESDConnection _getStatusReportsFromClient:]_block_invoke : 472 -> 484
~ -[ESDConnection _downloadProgress:] : 632 -> 660
~ ___35-[ESDConnection _downloadProgress:]_block_invoke : 80 -> 84
~ -[ESDConnection _downloadFinished:] : 604 -> 632
~ ___35-[ESDConnection _downloadFinished:]_block_invoke : 92 -> 96
~ -[ESDConnection _shareResponseFinished:] : 396 -> 408
~ ___40-[ESDConnection _shareResponseFinished:]_block_invoke : 92 -> 96
~ -[ESDConnection _oofSettingsRequestsFinished:] : 1388 -> 1456
~ ___46-[ESDConnection _oofSettingsRequestsFinished:]_block_invoke : 260 -> 268
~ +[ESDConnection sharedConnection] : 84 -> 92
~ -[ESDConnection watchFoldersWithKeys:forAccountID:persistent:] : 472 -> 484
~ -[ESDConnection resumeWatchingFoldersWithKeys:forAccountID:] : 532 -> 544
~ -[ESDConnection suspendWatchingFoldersWithKeys:forAccountID:] : 408 -> 416
~ -[ESDConnection stopWatchingFoldersWithKeys:forAccountID:] : 408 -> 416
~ -[ESDConnection _validateXPCReply:] : 392 -> 408
~ -[ESDConnection requestPolicyUpdateForAccountID:] : 252 -> 260
~ -[ESDConnection currentPolicyKeyForAccountID:] : 548 -> 552
~ ___46-[ESDConnection currentPolicyKeyForAccountID:]_block_invoke : 364 -> 380
~ -[ESDConnection _requestDaemonChangeAgentMonitoringStatus:withToken:waitForReply:] : 676 -> 704
~ -[ESDConnection updateFolderListForAccountID:andDataclasses:requireChangedFolders:isUserRequested:] : 556 -> 580
~ -[ESDConnection updateContentsOfFoldersWithKeys:forAccountID:andDataclasses:isUserRequested:] : 544 -> 560
~ -[ESDConnection updateContentsOfAllFoldersForAccountID:andDataclasses:isUserRequested:] : 492 -> 512
~ -[ESDConnection performServerContactsSearch:forAccountWithID:] : 780 -> 800
~ ___62-[ESDConnection performServerContactsSearch:forAccountWithID:]_block_invoke_2 : 220 -> 224
~ -[ESDConnection cancelServerContactsSearch:] : 612 -> 636
~ -[ESDConnection processMeetingRequests:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:forAccountWithId:] : 548 -> 544
~ -[ESDConnection asyncProcessMeetingRequests:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:forAccountWithId:] : 384 -> 380
~ -[ESDConnection setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:forAccountID:] : 500 -> 496
~ -[ESDConnection reportFolderItemsSyncSuccess:forFolderWithID:withItemsCount:andAccountWithID:] : 392 -> 404
~ -[ESDConnection handleURL:] : 296 -> 308
~ -[ESDConnection _sendSynchronousXPCMessageWithParameters:handlerBlock:] : 296 -> 292
~ -[ESDConnection beginDownloadingAttachmentWithUUID:accountID:queue:progressBlock:completionBlock:] : 740 -> 716
~ ___98-[ESDConnection beginDownloadingAttachmentWithUUID:accountID:queue:progressBlock:completionBlock:]_block_invoke : 392 -> 400
~ ___47-[ESDConnection _cancelDownloadsWithIDs:error:]_block_invoke : 92 -> 96
~ -[ESDConnection cancelDownloadingAttachmentWithDownloadID:error:] : 424 -> 436
~ -[ESDConnection respondToSharedCalendarInvite:forCalendarWithID:accountID:queue:completionBlock:] : 640 -> 628
~ ___97-[ESDConnection respondToSharedCalendarInvite:forCalendarWithID:accountID:queue:completionBlock:]_block_invoke : 368 -> 372
~ -[ESDConnection reportSharedCalendarInviteAsJunkForCalendarWithID:accountID:queue:completionBlock:] : 568 -> 552
~ ___99-[ESDConnection reportSharedCalendarInviteAsJunkForCalendarWithID:accountID:queue:completionBlock:]_block_invoke : 368 -> 372
~ -[ESDConnection processFolderChange:forAccountWithID:] : 600 -> 616
~ ___54-[ESDConnection processFolderChange:forAccountWithID:]_block_invoke : 260 -> 268
~ -[ESDConnection statusReports] : 544 -> 548
~ ___30-[ESDConnection statusReports]_block_invoke : 364 -> 380
~ -[ESDConnection reallyRegisterForInterrogation] : 312 -> 324
~ -[ESDConnection fillOutCurrentEASTimeZoneInfo] : 360 -> 368
~ -[ESDConnection activeSyncDeviceIdentifier] : 804 -> 820
~ ___43-[ESDConnection activeSyncDeviceIdentifier]_block_invoke : 152 -> 164
~ -[ESDConnection _performOofSettingsRequest:forAccountWithID:forUpdate:] : 764 -> 784
~ ___71-[ESDConnection _performOofSettingsRequest:forAccountWithID:forUpdate:]_block_invoke_2 : 256 -> 260
~ -[ESDConnection isOofSettingsSupportedForAccountWithID:completionBlock:] : 480 -> 492
~ ___72-[ESDConnection isOofSettingsSupportedForAccountWithID:completionBlock:]_block_invoke : 252 -> 264
~ -[ESDConnection requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:] : 1552 -> 1500
~ ___130-[ESDConnection requestCalendarAvailabilityWithAccountID:startDate:endDate:ignoredEventID:addresses:resultsBlock:completionBlock:]_block_invoke.152 : 412 -> 416
~ -[ESDConnection cancelCalendarAvailabilityRequestWithID:] : 564 -> 580
~ ___57-[ESDConnection cancelCalendarAvailabilityRequestWithID:]_block_invoke : 92 -> 96
~ -[ESDConnection _calendarAvailabilityRequestReturnedResults:] : 700 -> 716
~ ___61-[ESDConnection _calendarAvailabilityRequestReturnedResults:]_block_invoke : 80 -> 84
~ -[ESDConnection _calendarAvailabilityRequestFinished:] : 404 -> 416
~ ___54-[ESDConnection _calendarAvailabilityRequestFinished:]_block_invoke : 92 -> 96
~ -[ESDConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:] : 1420 -> 1452
~ ___120-[ESDConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.156 : 412 -> 416
~ -[ESDConnection cancelCalendarDirectorySearchWithID:] : 680 -> 696
~ ___53-[ESDConnection cancelCalendarDirectorySearchWithID:]_block_invoke : 92 -> 96
~ -[ESDConnection _calendarDirectorySearchReturnedResults:] : 840 -> 856
~ ___57-[ESDConnection _calendarDirectorySearchReturnedResults:]_block_invoke : 80 -> 84
~ ___57-[ESDConnection _calendarDirectorySearchReturnedResults:]_block_invoke_2 : 140 -> 136
~ -[ESDConnection _calendarDirectorySearchFinished:] : 472 -> 488
~ ___50-[ESDConnection _calendarDirectorySearchFinished:]_block_invoke : 92 -> 96
~ -[ESDConnection externalIdentificationForAccountID:resultsBlock:] : 936 -> 952
~ ___65-[ESDConnection externalIdentificationForAccountID:resultsBlock:]_block_invoke : 260 -> 284
~ -[ESDConnection init] : 92 -> 96
~ -[ESDConnection dealloc] : 104 -> 108
~ -[ESDConnection _resetCertWarningsForAccountId:andDataclasses:isUserRequested:] : 428 -> 436
~ -[ESDConnection _resetThrottleTimersForAccountId:] : 488 -> 500
~ -[ESDConnection resetTimersAndWarnings] : 192 -> 196
~ -[ESDConnection _registerForAppResumedNotification] : 108 -> 112
~ -[ESDConnection _dispatchMessage:] : 876 -> 892

```

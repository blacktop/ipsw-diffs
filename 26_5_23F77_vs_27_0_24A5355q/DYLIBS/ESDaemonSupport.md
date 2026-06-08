## ESDaemonSupport

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport`

```diff

-2074.80.2.0.0
-  __TEXT.__text: 0x232ac
-  __TEXT.__auth_stubs: 0xab0
+2075.0.0.0.0
+  __TEXT.__text: 0x20e50
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x339b
-  __TEXT.__cstring: 0x10c5
-  __TEXT.__gcc_except_tab: 0x5bc
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__objc_classname: 0x351
-  __TEXT.__objc_methname: 0x486b
-  __TEXT.__objc_methtype: 0x731
-  __TEXT.__objc_stubs: 0x3ca0
-  __DATA_CONST.__got: 0x750
+  __TEXT.__cstring: 0x10e8
+  __TEXT.__gcc_except_tab: 0x578
+  __TEXT.__unwind_info: 0x680
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0x750
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0xaa0
   __AUTH_CONST.__objc_const: 0x2a70
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x370

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F12C149C-8ABF-3A7B-AFF6-DD5228120226
+  UUID: 415E85D5-2EE2-32FB-8F26-9D05AA596333
   Functions: 580
-  Symbols:   2443
-  CStrings:  1283
+  Symbols:   2445
+  CStrings:  419
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
- GCC_except_table16
Functions:
~ -[ESDClientCalendarAvailabilityResponseDelegate initWithAccountID:client:startDate:endDate:ignoredEventID:addresses:] : 336 -> 348
~ -[ESDClientCalendarAvailabilityResponseDelegate finishWithError:] : 796 -> 728
~ ___65-[ESDClientCalendarAvailabilityResponseDelegate finishWithError:]_block_invoke : 300 -> 284
~ -[ESDClientCalendarAvailabilityResponseDelegate performRequest] : 468 -> 416
~ -[ESDClientCalendarAvailabilityResponseDelegate calendarAvailabilityRequestReturnedResults:] : 200 -> 204
~ ___92-[ESDClientCalendarAvailabilityResponseDelegate calendarAvailabilityRequestReturnedResults:]_block_invoke : 328 -> 308
~ -[ESDClientDelegate disable] : 136 -> 132
~ -[ESDClientDelegate userRequestsCancel] : 124 -> 120
~ -[ESDClientDelegate finishWithError:] : 120 -> 116
~ -[ESDClientDelegate delegateID] : 16 -> 20
~ -[ESDClientDelegate setDelegateID:] : 80 -> 20
~ -[ESDClientDelegate accountID] : 16 -> 20
~ -[ESDClientDelegate setAccountID:] : 80 -> 20
~ -[ESDClientDelegate finished] : 16 -> 20
~ -[ESDClientDelegate setFinished:] : 16 -> 20
~ -[ESDClientDelegate consumerCancelled] : 16 -> 20
~ -[ESDClientDelegate setConsumerCancelled:] : 16 -> 20
~ -[DAAgent trustHandler] : 84 -> 76
~ -[DAAgent stateString] : 84 -> 76
~ -[DAAgent _reachabilityChanged:] : 416 -> 348
~ -[DAAgent observeReachabilityWithBlock:] : 104 -> 100
~ -[DAAgent stopObservingReachability] : 92 -> 88
~ -[DAAgent requestAgentStopMonitoringWithCompletionBlock:] : 104 -> 100
~ -[DAAgent shutdown] : 108 -> 100
~ -[DAAgent setAccount:] : 64 -> 12
~ -[DAAgent(DARefreshManagerDelegateSupport) saveXpcActivity:] : 100 -> 96
~ -[DAAgent(CalendarSupport) preferredEventDaysToSync] : 68 -> 64
~ -[DAAgent(CalendarSupport) preferredToDoDaysToSync] : 68 -> 64
~ -[ESDClientCalendarDirectorySearchResponseDelegate initWithAccountID:client:terms:recordTypes:resultLimit:] : 200 -> 212
~ -[ESDClientCalendarDirectorySearchResponseDelegate finishWithError:] : 972 -> 884
~ -[ESDClientCalendarDirectorySearchResponseDelegate performRequest] : 456 -> 400
~ -[ESDClientCalendarDirectorySearchResponseDelegate calendarDirectorySearchReturnedResults:] : 356 -> 332
~ -[ESDClientCalendarDirectorySearchResponseDelegate calendarDirectorySearchFinishedWithError:exceededResultLimit:] : 16 -> 20
~ -[ESDClientCalendarDirectorySearchResponseDelegate _convertSearchQueryResults:] : 772 -> 728
~ -[ESDClientCalendarDirectorySearchResponseDelegate searchQuery:returnedResults:] : 92 -> 88
~ -[ESDClientCalendarDirectorySearchResponseDelegate searchQuery:finishedWithError:] : 20 -> 24
~ -[_DAChangeHistoryABLegacyClerk initWithAddressBook:] : 100 -> 104
~ -[_DAChangeHistoryABLegacyClerk dealloc] : 84 -> 88
~ -[_DAChangeHistoryABLegacyClerk addressBook] : 16 -> 20
~ +[ESWifiAssertionManager sharedWifiAssertionManager] : 84 -> 68
~ -[ESWifiAssertionManager retainWifiAssertion] : 184 -> 180
~ -[ESWifiAssertionManager releaseWifiAssertion] : 188 -> 184
~ -[ESDClientContactsSearchDelegate beginQuery] : 408 -> 336
~ -[ESDClientContactsSearchDelegate searchQuery:returnedResults:] : 100 -> 96
~ -[ESDClientContactsSearchDelegate disable] : 108 -> 104
~ -[ESDClientContactsSearchDelegate finishWithError:] : 980 -> 908
~ -[ESDClientContactsSearchDelegate query] : 16 -> 20
~ -[ESDClientContactsSearchDelegate setQuery:] : 80 -> 20
~ -[ESDClientContactsSearchDelegate queryResultData] : 16 -> 20
~ -[ESDClientContactsSearchDelegate setQueryResultData:] : 80 -> 20
~ -[ESDAccessManager _setupServerConnection] : 380 -> 364
~ ___42-[ESDAccessManager _setupServerConnection]_block_invoke : 1956 -> 1872
~ -[ESDAccessManager init] : 96 -> 92
~ -[ESDAccessManager _init] : 216 -> 212
~ +[ESDAccessManager sharedManager] : 84 -> 68
~ -[ESDAccessManager removeClient:] : 344 -> 280
~ -[ESDAccessManager addPersistentClientWithAccountID:clientID:watchedIDs:] : 696 -> 688
~ -[ESDAccessManager mainConnection] : 16 -> 20
~ -[ESDAccessManager setMainConnection:] : 80 -> 20
~ -[ESDAccessManager exchangeConnection] : 16 -> 20
~ -[ESDAccessManager setExchangeConnection:] : 80 -> 20
~ -[ESDAccessManager clients] : 16 -> 20
~ -[ESDAccessManager setClients:] : 80 -> 20
~ -[DADClientAccountTimers folderIdToLastFolderContentsRequestDate] : 92 -> 84
~ -[DADClientAccountTimers clientBehaviorForFolderIds:] : 424 -> 420
~ -[DADClientAccountTimers clientBehaviorForFolderList] : 156 -> 152
~ -[DADClientAccountTimers clientBehaviorForFolderContents] : 156 -> 152
~ -[DADClientAccountTimers allowFolderWipe] : 124 -> 120
~ -[DADClientAccountTimers setLastAllFolderContentsRequestDate:] : 64 -> 12
~ -[DADClientAccountTimers setLastFolderListRequestDate:] : 64 -> 12
~ -[DADClientAccountTimers setLastFolderWipeRequestDate:] : 64 -> 12
~ -[DADClientAccountTimers setFolderIdToLastFolderContentsRequestDate:] : 64 -> 12
~ _handleSignal : 876 -> 796
~ -[ESDMain _shutdownDaemon] : 396 -> 384
~ ___26-[ESDMain _shutdownDaemon]_block_invoke : 76 -> 72
~ ___26-[ESDMain _shutdownDaemon]_block_invoke.5 : 444 -> 432
~ -[ESDMain _forceShutdownTimerFired:] : 72 -> 76
~ -[ESDMain _forceShutdownDaemonOnLogoutInTimeInterval:] : 380 -> 328
~ -[ESDMain addToOperationsQueueDisabledCheckAndGoBlock:wrappedBlock:] : 184 -> 192
~ ___68-[ESDMain addToOperationsQueueDisabledCheckAndGoBlock:wrappedBlock:]_block_invoke : 188 -> 176
~ -[ESDMain willSwitchUser] : 832 -> 780
~ -[ESDMain didFinishAllXPCTransactions] : 192 -> 180
~ -[ESDMain addSignalHandler] : 296 -> 304
~ __languageMayHaveChanged : 176 -> 156
~ +[ESDMain sharedMain] : 84 -> 68
~ ___21+[ESDMain sharedMain]_block_invoke : 240 -> 232
~ _getStateString : 216 -> 192
~ -[ESDMain waitForSystemAvailability] : 336 -> 320
~ -[ESDMain setRunLoopStoppedRef:] : 16 -> 20
~ -[ESDMain _setRunLoopStopped:] : 20 -> 24
~ -[ESDMain disable] : 164 -> 156
~ -[ESDMain _configureAggdLogging] : 432 -> 436
~ ___32-[ESDMain _configureAggdLogging]_block_invoke : 708 -> 712
~ -[ESDMain init] : 488 -> 432
~ -[ESDMain dealloc] : 152 -> 160
~ -[ESDMain userSwitchTasks] : 16 -> 20
~ -[ESDMain setUserSwitchTasks:] : 80 -> 20
~ ___logState_block_invoke : 312 -> 260
~ ___ESDAddStateCaptureBlock_block_invoke : 564 -> 508
~ -[ESFolderSyncRequest description] : 228 -> 216
~ -[ESFolderSyncRequest setFolder:] : 64 -> 12
~ -[ESFolderSyncRequest setActions:] : 64 -> 12
~ -[ESFolderSyncRequest setSkippedActions:] : 64 -> 12
~ -[ESDClientSettingsDelegate initWithAccountID:requestDictionary:forUpdate:client:] : 296 -> 300
~ -[ESDClientSettingsDelegate dealloc] : 172 -> 168
~ -[ESDClientSettingsDelegate beginSettingsRequest] : 436 -> 364
~ -[ESDClientSettingsDelegate isOofSupported] : 652 -> 568
~ -[ESDClientSettingsDelegate settingsRequestFinishedWithResults:status:error:] : 272 -> 248
~ -[ESDClientSettingsDelegate finishWithError:] : 776 -> 724
~ -[ESDClientSettingsDelegate isUpdate] : 16 -> 20
~ -[ESDClientSettingsDelegate setIsUpdate:] : 16 -> 20
~ -[ESDClientSettingsDelegate requestParams] : 16 -> 20
~ -[ESDClientSettingsDelegate setRequestParams:] : 80 -> 20
~ -[ESDClientSettingsDelegate responseParams] : 16 -> 20
~ -[ESDClientSettingsDelegate setResponseParams:] : 80 -> 20
~ +[_DAChangeHistoryContactsClerk os_log] : 84 -> 68
~ -[_DAChangeHistoryContactsClerk unregisterClientWithIdentifier:forContainer:] : 208 -> 192
~ -[_DAChangeHistoryContactsClerk registerClientWithIdentifier:forContainer:] : 208 -> 192
~ -[_DAChangeHistoryContactsClerk contactStore] : 16 -> 20
~ -[ESDClient initWithConnection:clientID:] : 976 -> 900
~ ___41-[ESDClient initWithConnection:clientID:]_block_invoke : 404 -> 348
~ -[ESDClient initWithClientID:] : 688 -> 632
~ -[ESDClient reconnectWithConnection:] : 316 -> 296
~ ___37-[ESDClient reconnectWithConnection:]_block_invoke : 140 -> 132
~ -[ESDClient dealloc] : 384 -> 328
~ -[ESDClient _clientName] : 308 -> 292
~ -[ESDClient _removeBusyFolderIDs:forAccountWithID:] : 368 -> 372
~ -[ESDClient _removeWatchedFolderIDs:forAccountWithID:] : 368 -> 372
~ -[ESDClient disable] : 784 -> 752
~ ___20-[ESDClient disable]_block_invoke : 1368 -> 1320
~ -[ESDClient watchedFolderCount] : 376 -> 360
~ -[ESDClient persistentClientCleanup] : 812 -> 780
~ ___36-[ESDClient persistentClientCleanup]_block_invoke : 640 -> 624
~ -[ESDClient isMonitoringAccountID:folderID:] : 356 -> 352
~ -[ESDClient noteBlockedClientCallChange:] : 568 -> 548
~ -[ESDClient noteRefreshClientCallChange:] : 404 -> 392
~ +[ESDClient clientsToInterrogate] : 132 -> 124
~ -[ESDClient registerForInterrogation] : 164 -> 160
~ -[ESDClient unregisterForInterrogation] : 132 -> 128
~ -[ESDClient _createReplyToRequest:withProperties:] : 188 -> 192
~ -[ESDClient _beginMonitoringFolders:] : 1244 -> 1168
~ ___37-[ESDClient _beginMonitoringFolders:]_block_invoke : 1384 -> 1296
~ ___37-[ESDClient _beginMonitoringFolders:]_block_invoke_2 : 112 -> 108
~ -[ESDClient beginMonitoringPersistentFolders:forAccount:] : 660 -> 640
~ ___57-[ESDClient beginMonitoringPersistentFolders:forAccount:]_block_invoke : 516 -> 440
~ ___57-[ESDClient beginMonitoringPersistentFolders:forAccount:]_block_invoke_2 : 112 -> 108
~ -[ESDClient _stopMonitoringFolders:] : 992 -> 932
~ ___36-[ESDClient _stopMonitoringFolders:]_block_invoke : 716 -> 668
~ ___36-[ESDClient _stopMonitoringFolders:]_block_invoke_2 : 548 -> 540
~ -[ESDClient _resumeMonitoringFolders:] : 992 -> 932
~ ___38-[ESDClient _resumeMonitoringFolders:]_block_invoke : 460 -> 432
~ ___38-[ESDClient _resumeMonitoringFolders:]_block_invoke_2 : 112 -> 108
~ -[ESDClient _suspendMonitoringFolders:] : 992 -> 932
~ ___39-[ESDClient _suspendMonitoringFolders:]_block_invoke : 580 -> 536
~ ___39-[ESDClient _suspendMonitoringFolders:]_block_invoke_2 : 112 -> 108
~ -[ESDClient _stopMonitoringAgentsWithClientToken:] : 204 -> 188
~ -[ESDClient _startMonitoringAgentsWithClientToken:] : 352 -> 288
~ -[ESDClient _startMonitoringAgentsWithServerToken:] : 92 -> 88
~ -[ESDClient _clearAllStopMonitoringAgentsTokens] : 316 -> 308
~ -[ESDClient _startMonitoringAgents:] : 472 -> 424
~ ___36-[ESDClient _startMonitoringAgents:]_block_invoke : 604 -> 572
~ -[ESDClient _stopMonitoringAgents:] : 472 -> 424
~ ___35-[ESDClient _stopMonitoringAgents:]_block_invoke : 452 -> 428
~ -[ESDClient _getCurrentPolicyKey:] : 552 -> 504
~ ___34-[ESDClient _getCurrentPolicyKey:]_block_invoke : 340 -> 320
~ -[ESDClient _requestPolicyUpdate:] : 536 -> 484
~ ___34-[ESDClient _requestPolicyUpdate:]_block_invoke : 92 -> 88
~ -[ESDClient timersForAccountWithID:] : 184 -> 172
~ -[ESDClient _requestFolderContentsUpdateForFolders:accountId:dataclasses:isUserRequested:] : 1288 -> 1272
~ ___90-[ESDClient _requestFolderContentsUpdateForFolders:accountId:dataclasses:isUserRequested:]_block_invoke : 260 -> 208
~ ___90-[ESDClient _requestFolderContentsUpdateForFolders:accountId:dataclasses:isUserRequested:]_block_invoke.60 : 112 -> 108
~ -[ESDClient _requestFolderContentsUpdate:] : 540 -> 472
~ -[ESDClient _requestAllFolderContentsUpdateForAccountId:dataclasses:isUserRequested:] : 1096 -> 1024
~ ___85-[ESDClient _requestAllFolderContentsUpdateForAccountId:dataclasses:isUserRequested:]_block_invoke : 600 -> 520
~ ___85-[ESDClient _requestAllFolderContentsUpdateForAccountId:dataclasses:isUserRequested:]_block_invoke.62 : 108 -> 104
~ -[ESDClient _requestAllFolderContentsUpdate:] : 372 -> 312
~ -[ESDClient _requestFolderListUpdateForAccountId:dataclasses:requireChangedFolders:isUserRequested:] : 1180 -> 1104
~ ___100-[ESDClient _requestFolderListUpdateForAccountId:dataclasses:requireChangedFolders:isUserRequested:]_block_invoke : 380 -> 320
~ ___100-[ESDClient _requestFolderListUpdateForAccountId:dataclasses:requireChangedFolders:isUserRequested:]_block_invoke.64 : 112 -> 108
~ -[ESDClient _requestFolderListUpdate:] : 428 -> 364
~ -[ESDClient delegateWithIDIsGoingAway:] : 100 -> 96
~ -[ESDClient _openServerContactsSearch:] : 880 -> 852
~ -[ESDClient _cancelServerContactsSearch:] : 588 -> 532
~ -[ESDClient _processMeetingRequests:] : 1392 -> 1384
~ ___37-[ESDClient _processMeetingRequests:]_block_invoke : 256 -> 252
~ ___37-[ESDClient _processMeetingRequests:]_block_invoke_2 : 676 -> 644
~ ___37-[ESDClient _processMeetingRequests:]_block_invoke.74 : 468 -> 444
~ -[ESDClient _asyncProcessMeetingRequests:] : 932 -> 852
~ ___42-[ESDClient _asyncProcessMeetingRequests:]_block_invoke : 236 -> 232
~ -[ESDClient _resetCertWarnings:] : 696 -> 636
~ ___32-[ESDClient _resetCertWarnings:]_block_invoke : 260 -> 208
~ -[ESDClient _setFolderIdsThatExternalClientsCareAbout:] : 824 -> 780
~ ___55-[ESDClient _setFolderIdsThatExternalClientsCareAbout:]_block_invoke : 484 -> 464
~ ___55-[ESDClient _setFolderIdsThatExternalClientsCareAbout:]_block_invoke.77 : 104 -> 100
~ -[ESDClient _reportFolderItemsSyncResult:] : 688 -> 628
~ ___42-[ESDClient _reportFolderItemsSyncResult:]_block_invoke : 104 -> 100
~ -[ESDClient _handleURL:] : 536 -> 484
~ ___24-[ESDClient _handleURL:]_block_invoke : 92 -> 88
~ -[ESDClient _processFolderChange:] : 664 -> 632
~ ___34-[ESDClient _processFolderChange:]_block_invoke : 448 -> 444
~ ___34-[ESDClient _processFolderChange:]_block_invoke_2 : 908 -> 872
~ ___34-[ESDClient _processFolderChange:]_block_invoke.86 : 388 -> 368
~ -[ESDClient _getStatusReports:] : 484 -> 436
~ ___31-[ESDClient _getStatusReports:]_block_invoke : 200 -> 196
~ ___31-[ESDClient _getStatusReports:]_block_invoke_2 : 384 -> 364
~ -[ESDClient _resetThrottleTimers:] : 408 -> 332
~ -[ESDClient _beginDownloadingAttachmentEvent:eventDict:] : 988 -> 960
~ -[ESDClient _cancelDownloadingAttachmentEvent:eventDict:] : 952 -> 872
~ -[ESDClient _respondToSharedCalendarEvent:eventDict:] : 1056 -> 1020
~ -[ESDClient _reportSharedCalendarAsJunkEvent:eventDict:] : 968 -> 936
~ -[ESDClient _fillOutEASTimeZoneInfo:] : 540 -> 488
~ ___37-[ESDClient _fillOutEASTimeZoneInfo:]_block_invoke_2 : 320 -> 308
~ -[ESDClient _getActiveSyncDeviceIdentifier:] : 620 -> 588
~ -[ESDClient _openServerOofSettingsRequest:] : 932 -> 904
~ -[ESDClient _checkIsOofSettingsSupported:] : 412 -> 388
~ -[ESDClient _requestCalendarAvailability:eventDict:] : 1152 -> 1100
~ -[ESDClient _cancelCalendarAvailabilityRequest:eventDict:] : 580 -> 524
~ -[ESDClient _performCalendarDirectorySearch:eventDict:] : 1164 -> 1140
~ -[ESDClient _cancelCalendarDirectorySearch:eventDict:] : 580 -> 524
~ -[ESDClient _getAccountExternalIdentification:eventDict:] : 496 -> 464
~ -[ESDClient _asPolicyKeyChanged:] : 588 -> 548
~ -[ESDClient _requestClientStatusDump:] : 232 -> 220
~ -[ESDClient _foldersUpdated:] : 908 -> 836
~ -[ESDClient _agentsStopped:] : 68 -> 64
~ -[ESDClient applyClientStatusReportToAggregator:] : 400 -> 388
~ ___49-[ESDClient applyClientStatusReportToAggregator:]_block_invoke_2 : 176 -> 164
~ -[ESDClient _clientDiedWithReason:] : 296 -> 288
~ -[ESDClient _dispatchMessage:] : 6660 -> 6588
~ -[ESDClient persistent] : 16 -> 20
~ -[ESDClient clientBundleID] : 16 -> 20
~ -[ESDClient setClientBundleID:] : 80 -> 20
~ -[ESDClient clientUniqueID] : 16 -> 20
~ -[ESDClient setClientUniqueID:] : 80 -> 20
~ -[ESDClient conn] : 16 -> 20
~ -[ESDClient setConn:] : 80 -> 20
~ -[ESDClient watchedIDs] : 16 -> 20
~ -[ESDClient setWatchedIDs:] : 80 -> 20
~ -[ESDClient busyIDs] : 16 -> 20
~ -[ESDClient setBusyIDs:] : 80 -> 20
~ -[ESDClient updatedIDs] : 16 -> 20
~ -[ESDClient setUpdatedIDs:] : 80 -> 20
~ -[ESDClient numOutstandingBlockingClientCalls] : 16 -> 20
~ -[ESDClient setNumOutstandingBlockingClientCalls:] : 16 -> 20
~ -[ESDClient numOutstandingRefreshPriorityClientCalls] : 16 -> 20
~ -[ESDClient setNumOutstandingRefreshPriorityClientCalls:] : 16 -> 20
~ -[ESDClient accountTimers] : 16 -> 20
~ -[ESDClient setAccountTimers:] : 80 -> 20
~ -[ESDClient actionDelegatesById] : 16 -> 20
~ -[ESDClient setActionDelegatesById:] : 80 -> 20
~ -[ESDClient clientName] : 16 -> 20
~ -[ESDClient setClientName:] : 80 -> 20
~ -[ESDClient agentMonitoringTokens] : 16 -> 20
~ -[ESDClient setAgentMonitoringTokens:] : 80 -> 20
~ -[ESDClientAttachmentDownloadDelegate beginDownload] : 428 -> 360
~ -[ESDClientAttachmentDownloadDelegate downloadProgressDownloadedByteCount:totalByteCount:] : 496 -> 464
~ -[ESDClientAttachmentDownloadDelegate finishWithError:] : 936 -> 876
~ -[ESDClientAttachmentDownloadDelegate attachmentUUID] : 16 -> 20
~ -[ESDClientAttachmentDownloadDelegate setAttachmentUUID:] : 80 -> 20
~ -[ESDClientAttachmentDownloadDelegate downloadID] : 16 -> 20
~ -[ESDClientAttachmentDownloadDelegate setDownloadID:] : 80 -> 20
~ +[ESDAgentManager sharedManager] : 84 -> 68
~ -[ESDAgentManager init] : 516 -> 496
~ __devicePowerChanged : 308 -> 256
~ -[ESDAgentManager dealloc] : 220 -> 216
~ -[ESDAgentManager activeAgents] : 236 -> 240
~ ___31-[ESDAgentManager activeAgents]_block_invoke : 264 -> 216
~ -[ESDAgentManager accountsProviderWithDBHelper:] : 180 -> 164
~ -[ESDAgentManager changeHistoryClerkWithDBHelper:] : 180 -> 164
~ -[ESDAgentManager agentWithAccountID:] : 376 -> 372
~ -[ESDAgentManager accountWithAccountID:] : 404 -> 388
~ -[ESDAgentManager accountWithAccountID:andClassName:] : 456 -> 432
~ -[ESDAgentManager _configFileForAgent:] : 284 -> 256
~ -[ESDAgentManager _accountInfoPath] : 220 -> 200
~ -[ESDAgentManager _phoneVersion] : 132 -> 120
~ -[ESDAgentManager loadAgents] : 124 -> 120
~ -[ESDAgentManager loadExchangeAgents] : 3604 -> 3460
~ ___37-[ESDAgentManager loadExchangeAgents]_block_invoke : 240 -> 192
~ -[ESDAgentManager saveAndReleaseAgents] : 708 -> 684
~ ___39-[ESDAgentManager saveAndReleaseAgents]_block_invoke : 232 -> 184
~ -[ESDAgentManager _deviceWillSleep] : 468 -> 452
~ -[ESDAgentManager _deviceDidWake] : 260 -> 256
~ -[ESDAgentManager currentPolicyKeyForAccount:] : 428 -> 404
~ -[ESDAgentManager requestPolicyUpdateForAccount:] : 632 -> 600
~ -[ESDAgentManager startMonitoringAccountID:folderIDs:] : 656 -> 636
~ -[ESDAgentManager stopMonitoringAccountID:folderIDs:] : 536 -> 520
~ -[ESDAgentManager suspendMonitoringAccountID:folderIDs:] : 536 -> 520
~ -[ESDAgentManager resumeMonitoringAccountID:folderIDs:] : 536 -> 520
~ -[ESDAgentManager addPersistMonitoringAccountID:folderIDs:clientID:] : 720 -> 696
~ -[ESDAgentManager removePersistMonitoringAccountID:folderIDs:clientID:] : 600 -> 580
~ -[ESDAgentManager clearPersistMonitoringAccountID:clientID:] : 524 -> 508
~ -[ESDAgentManager _clearOrphanedStores] : 2444 -> 2364
~ -[ESDAgentManager _clearOrphanedStoresInCalendarDatabase:eventAccountIds:toDoAccountIds:] : 1232 -> 1188
~ -[ESDAgentManager _systemMayNowBeReady] : 872 -> 788
~ -[ESDAgentManager _resetMonitoringRequestsAndLoadAgents] : 172 -> 164
~ -[ESDAgentManager _calDaysToSyncDidChange] : 584 -> 580
~ -[ESDAgentManager _registerForCTDataUsageNotificaiton] : 400 -> 348
~ ___54-[ESDAgentManager _registerForCTDataUsageNotificaiton]_block_invoke : 128 -> 124
~ ___54-[ESDAgentManager _registerForCTDataUsageNotificaiton]_block_invoke_2 : 76 -> 72
~ -[ESDAgentManager _handleCellularDataUsageChangedNotification] : 732 -> 692
~ -[ESDAgentManager _loadAndStartExchangeMonitoringAgents] : 512 -> 504
~ ___56-[ESDAgentManager _loadAndStartExchangeMonitoringAgents]_block_invoke : 988 -> 972
~ __pcPreferencesDidChange : 124 -> 120
~ __calDaysToSyncDidChange : 156 -> 148
~ __calDatabaseDidChange : 84 -> 80
~ __abDataBaseDidChangeByOtherProcess : 84 -> 80
~ __noteContextDidChange : 84 -> 80
~ __systemReadyCheckFired : 244 -> 200
~ -[ESDAgentManager registerForBuddy] : 256 -> 248
~ -[ESDAgentManager _stopMonitoringAndSaveAgents] : 1404 -> 1368
~ ___47-[ESDAgentManager _stopMonitoringAndSaveAgents]_block_invoke : 312 -> 260
~ -[ESDAgentManager _addAccountAggdEntries] : 1128 -> 1100
~ -[ESDAgentManager enableMonitoringAgentsWithToken:] : 520 -> 452
~ -[ESDAgentManager disableMonitoringAgents] : 452 -> 388
~ -[ESDAgentManager updateFolderListForAccountID:andDataclasses:requireChangedFolders:isUserRequested:] : 408 -> 396
~ -[ESDAgentManager updateContentsOfFolders:forAccountID:andDataclasses:isUserRequested:] : 632 -> 612
~ -[ESDAgentManager updateContentsOfAllFoldersForAccountID:andDataclasses:isUserRequested:] : 624 -> 600
~ -[ESDAgentManager activeAccountBundleIDs] : 384 -> 372
~ -[ESDAgentManager hasEASAccountConfigured] : 568 -> 536
~ -[ESDAgentManager processMeetingRequestDatas:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:forAccountWithId:callback:] : 576 -> 568
~ -[ESDAgentManager resetCertWarningsForAccountWithId:andDataclasses:] : 428 -> 416
~ -[ESDAgentManager setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:forAccountID:] : 536 -> 532
~ -[ESDAgentManager reportFolderItemsSyncSuccess:forFolderWithID:withItemsCount:andAccountWithID:] : 432 -> 424
~ -[ESDAgentManager stateString] : 660 -> 620
~ -[ESDAgentManager processFolderChange:forAccountWithID:completionBlock:] : 408 -> 404
~ -[ESDAgentManager getStatusReportDictsWithCompletionBlock:] : 864 -> 816
~ -[ESDAgentManager hasActiveAccounts] : 564 -> 544
~ -[ESDAgentManager enableDaemon] : 272 -> 200
~ _launchdSemaphorePath : 76 -> 72
~ -[ESDAgentManager disableDaemon] : 292 -> 220
~ -[ESDAgentManager cleanupLaunchdSemaphore] : 224 -> 176
~ -[ESDAgentManager enableActiveSync] : 272 -> 200
~ _launchdActiveSyncPath : 76 -> 72
~ -[ESDAgentManager disableActiveSync] : 224 -> 176
~ -[ESDAgentManager setSubCalHandlers:] : 64 -> 12
~ ___68-[ESDClientShareResponseDelegate respondToShareRequestWithResponse:]_block_invoke : 24 -> 28
~ ___46-[ESDClientShareResponseDelegate reportAsJunk]_block_invoke : 24 -> 28
~ -[ESDClientShareResponseDelegate _doResponseWithBlock:] : 448 -> 376
~ -[ESDClientShareResponseDelegate finishWithError:] : 936 -> 868
~ -[ESDClientShareResponseDelegate calendarID] : 16 -> 20
~ -[ESDClientShareResponseDelegate setCalendarID:] : 80 -> 20
~ -[ESDClientShareResponseDelegate shareID] : 16 -> 20
~ -[ESDClientShareResponseDelegate setShareID:] : 80 -> 20
~ -[ESDStatusReportAggregator initWithStatusReports:numOutstandingReports:timeout:completionBlock:] : 552 -> 556
~ -[ESDStatusReportAggregator _coalesceAndReport] : 540 -> 524
~ -[ESDStatusReportAggregator noteAdditionalReportDicts:] : 396 -> 388
~ -[DAChangeHistoryClerk unregisterClientWithIdentifier:forContainer:] : 80 -> 76
~ -[DAChangeHistoryClerk registerClientWithIdentifier:forContainer:] : 80 -> 76
~ -[DAChangeHistoryClerk identifiersOfAllRegisterdClients] : 64 -> 60
~ -[ESDAccessManager _setupServerConnection].cold.1 : 156 -> 132
~ -[ESDClient reconnectWithConnection:].cold.1 : 148 -> 140
~ -[ESDClient _openServerContactsSearch:].cold.1 : 80 -> 76
~ -[ESDClient _openServerContactsSearch:].cold.2 : 80 -> 76
~ -[ESDClient _beginDownloadingAttachmentEvent:eventDict:].cold.1 : 80 -> 76
~ -[ESDClient _beginDownloadingAttachmentEvent:eventDict:].cold.2 : 80 -> 76
~ -[ESDClient _cancelDownloadingAttachmentEvent:eventDict:].cold.1 : 80 -> 76
~ -[ESDClient _respondToSharedCalendarEvent:eventDict:].cold.1 : 80 -> 76
~ -[ESDClient _respondToSharedCalendarEvent:eventDict:].cold.2 : 80 -> 76
~ -[ESDClient _respondToSharedCalendarEvent:eventDict:].cold.3 : 80 -> 76
~ -[ESDClient _reportSharedCalendarAsJunkEvent:eventDict:].cold.1 : 80 -> 76
~ -[ESDClient _reportSharedCalendarAsJunkEvent:eventDict:].cold.2 : 80 -> 76
~ -[ESDClient _openServerOofSettingsRequest:].cold.1 : 80 -> 76
~ -[ESDClient _checkIsOofSettingsSupported:].cold.1 : 104 -> 100
~ -[ESDClient _requestCalendarAvailability:eventDict:].cold.1 : 80 -> 76
~ -[ESDClient _requestCalendarAvailability:eventDict:].cold.2 : 80 -> 76
~ -[ESDClient _requestCalendarAvailability:eventDict:].cold.3 : 80 -> 76
~ -[ESDClient _performCalendarDirectorySearch:eventDict:].cold.1 : 80 -> 76
~ -[ESDAgentManager _clearOrphanedStores].cold.1 : 120 -> 116
~ -[ESDAgentManager removePendingAccountSetup].cold.1 : 128 -> 124
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"CNContactStore\""
- "@\"DAAccount\""
- "@\"DAFolder\""
- "@\"DAOofParams\""
- "@\"DASearchQuery\""
- "@\"ESDClient\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^v16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@44@0:8@16@24B32@36"
- "@44@0:8@16i24d28@?36"
- "@56@0:8@16@24@32@40Q48"
- "@64@0:8@16@24@32@40@48@56"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16q24"
- "B36@0:8@16q24B32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B40@0:8@16q24B32B36"
- "B40@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24@32"
- "B44@0:8@16@24q32B40"
- "B48@0:8@16@24@32@40"
- "CFNetworkLogging"
- "CalendarSupport"
- "DAAgent"
- "DAChangeHistoryClerk"
- "DADClientAccountTimers"
- "DAEventsAttachmentDownloadConsumer"
- "DAEventsCalendarAvailabilityResponseConsumer"
- "DAEventsCalendarDirectorySearchResponseConsumer"
- "DAEventsCalendarSharingResponseConsumer"
- "DAExtendedDescription"
- "DARefreshManagerDelegateSupport"
- "DASearchQueryConsumer"
- "DATransactionMonitorDelegate"
- "DaemonAdditions"
- "ESDAccessManager"
- "ESDAgentManager"
- "ESDClient"
- "ESDClientAttachmentDownloadDelegate"
- "ESDClientCalendarAvailabilityResponseDelegate"
- "ESDClientCalendarDirectorySearchResponseDelegate"
- "ESDClientContactsSearchDelegate"
- "ESDClientDelegate"
- "ESDClientSettingsDelegate"
- "ESDClientShareResponseDelegate"
- "ESDMain"
- "ESDStatusReportAggregator"
- "ESFolderSyncRequest"
- "ESSettingsResponseDelegate"
- "ESWifiAssertionManager"
- "I"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"CNContactStore\",R,N,V_contactStore"
- "T@\"DAAccount\",&,N,V_account"
- "T@\"DAFolder\",&,N,V_folder"
- "T@\"DAOofParams\",&,N,V_requestParams"
- "T@\"DAOofParams\",&,N,V_responseParams"
- "T@\"DASearchQuery\",&,N,V_query"
- "T@\"DATrustHandler\",R,N"
- "T@\"ESDClient\",W,N,V_client"
- "T@\"NSArray\",&,N,V_actions"
- "T@\"NSArray\",&,N,V_skippedActions"
- "T@\"NSArray\",&,N,V_userSwitchTasks"
- "T@\"NSArray\",R,N"
- "T@\"NSData\",&,N,V_queryResultData"
- "T@\"NSDate\",&,N,V_lastAllFolderContentsRequestDate"
- "T@\"NSDate\",&,N,V_lastFolderListRequestDate"
- "T@\"NSDate\",&,N,V_lastFolderWipeRequestDate"
- "T@\"NSMutableArray\",&,N,V_clients"
- "T@\"NSMutableArray\",&,N,V_subCalHandlers"
- "T@\"NSMutableDictionary\",&,N,V_accountTimers"
- "T@\"NSMutableDictionary\",&,N,V_actionDelegatesById"
- "T@\"NSMutableDictionary\",&,N,V_agentMonitoringTokens"
- "T@\"NSMutableDictionary\",&,N,V_busyIDs"
- "T@\"NSMutableDictionary\",&,N,V_folderIdToLastFolderContentsRequestDate"
- "T@\"NSMutableDictionary\",&,N,V_updatedIDs"
- "T@\"NSMutableDictionary\",&,N,V_watchedIDs"
- "T@\"NSMutableDictionary\",R,N,V_disableMonitoringAgentsTokens"
- "T@\"NSObject<OS_dispatch_source>\",W,N,V_deferredAllFolderContentsSource"
- "T@\"NSObject<OS_dispatch_source>\",W,N,V_deferredFolderContentsSource"
- "T@\"NSObject<OS_dispatch_source>\",W,N,V_deferredFolderListSource"
- "T@\"NSObject<OS_os_log>\",R,N"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_conn"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_exchangeConnection"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_mainConnection"
- "T@\"NSString\",&,N,V_accountID"
- "T@\"NSString\",&,N,V_attachmentUUID"
- "T@\"NSString\",&,N,V_calendarID"
- "T@\"NSString\",&,N,V_clientBundleID"
- "T@\"NSString\",&,N,V_clientName"
- "T@\"NSString\",&,N,V_clientUniqueID"
- "T@\"NSString\",&,N,V_delegateID"
- "T@\"NSString\",&,N,V_shareID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@,&,N,V_downloadID"
- "T@?,C,N,V_networkReachableBlock"
- "TB,N,V_consumerCancelled"
- "TB,N,V_containsPostponedActions"
- "TB,N,V_finished"
- "TB,N,V_hasRemoteChanges"
- "TB,N,V_isInitialUberSync"
- "TB,N,V_isMonitoring"
- "TB,N,V_isResyncAfterConnectionFailed"
- "TB,N,V_isResyncAfterServerError"
- "TB,N,V_isUpdate"
- "TB,N,V_isWaitingForPassword"
- "TB,N,V_syncWhenReachable"
- "TB,R,N,V_persistent"
- "TQ,N,V_nextDisableMonitoringAgentsToken"
- "TQ,R"
- "T^v,R,N,V_addressBook"
- "Td,N,V_lastRetryTimeout"
- "Ti,N,V_numOutstandingBlockingClientCalls"
- "Ti,N,V_numOutstandingRefreshPriorityClientCalls"
- "UMUserSwitchStakeholder"
- "UTF8String"
- "Vv16@0:8"
- "^B"
- "^v"
- "^v16@0:8"
- "^{IONotificationPort=}"
- "^{_NSZone=}16@0:8"
- "^{__CFRunLoopSource=}"
- "^{__CTServerConnection=}"
- "^{__WiFiManagerClient=}16@0:8"
- "_CTCellularUsagePolicyNotificationQ"
- "_DAChangeHistoryABLegacyClerk"
- "_DAChangeHistoryContactsClerk"
- "_account"
- "_accountID"
- "_accountInfoPath"
- "_accountTimers"
- "_actionDelegatesById"
- "_actions"
- "_activeAgents"
- "_activeAgentsQueue"
- "_addAccountAggdEntries"
- "_addressBook"
- "_addresses"
- "_agentMonitoringTokens"
- "_agentsStopped:"
- "_aggdStatsQueue"
- "_aggdStatsSource"
- "_asPolicyKeyChanged:"
- "_asyncProcessMeetingRequests:"
- "_attachmentUUID"
- "_beginDownloadingAttachmentEvent:eventDict:"
- "_beginMonitoringFolders:"
- "_busyIDs"
- "_cacheTimeZoneInfo"
- "_calDaysToSyncDidChange"
- "_calendarID"
- "_cancelCalendarAvailabilityRequest:eventDict:"
- "_cancelCalendarDirectorySearch:eventDict:"
- "_cancelDownloadingAttachmentEvent:eventDict:"
- "_cancelServerContactsSearch:"
- "_checkIsOofSettingsSupported:"
- "_clearAllStopMonitoringAgentsTokens"
- "_clearOrphanedStores"
- "_clearOrphanedStoresInCalendarDatabase:eventAccountIds:toDoAccountIds:"
- "_client"
- "_clientBundleID"
- "_clientDiedWithReason:"
- "_clientName"
- "_clientUniqueID"
- "_clients"
- "_coalesceAndReport"
- "_completionBlock"
- "_configFileForAgent:"
- "_configureAggdLogging"
- "_conn"
- "_consumerCancelled"
- "_contactStore"
- "_containsPostponedActions"
- "_convertSearchQueryResults:"
- "_createReplyToRequest:withProperties:"
- "_ctServerConnection"
- "_deferredAllFolderContentsSource"
- "_deferredFolderContentsSource"
- "_deferredFolderListSource"
- "_delayedShutdownTimer"
- "_delegateID"
- "_deviceDidWake"
- "_deviceWillSleep"
- "_disableMonitoringAgentsTokens"
- "_dispatchMessage:"
- "_doResponseWithBlock:"
- "_downloadID"
- "_endDate"
- "_exceededResultLimit"
- "_exchangeConnection"
- "_fillOutEASTimeZoneInfo:"
- "_finished"
- "_folder"
- "_folderIdToLastFolderContentsRequestDate"
- "_foldersUpdated:"
- "_forceShutdownDaemonOnLogoutInTimeInterval:"
- "_forceShutdownTimer"
- "_forceShutdownTimerFired:"
- "_getAccountExternalIdentification:eventDict:"
- "_getActiveSyncDeviceIdentifier:"
- "_getCurrentPolicyKey:"
- "_getStatusReports:"
- "_getWiFiClientRef"
- "_handleCellularDataUsageChangedNotification"
- "_handleURL:"
- "_hasDataclassWeCareAbout:"
- "_hasRemoteChanges"
- "_ignoredEventID"
- "_init"
- "_isInitialUberSync"
- "_isMonitoring"
- "_isResyncAfterConnectionFailed"
- "_isResyncAfterServerError"
- "_isUpdate"
- "_isWaitingForPassword"
- "_lastAllFolderContentsRequestDate"
- "_lastFolderListRequestDate"
- "_lastFolderWipeRequestDate"
- "_lastRetryTimeout"
- "_leafExchangeAccountTypes"
- "_loadAndStartExchangeMonitoringAgents"
- "_mainConnection"
- "_networkReachableBlock"
- "_nextDisableMonitoringAgentsToken"
- "_numOutstandingBlockingClientCalls"
- "_numOutstandingRefreshPriorityClientCalls"
- "_numOutstandingReports"
- "_openServerContactsSearch:"
- "_openServerOofSettingsRequest:"
- "_pendingAccountSetupCount"
- "_performCalendarDirectorySearch:eventDict:"
- "_persistent"
- "_persistentUUIDToStatusReport"
- "_phoneVersion"
- "_pmNotifier"
- "_pmPort"
- "_pmRunLoopSource"
- "_processFolderChange:"
- "_processMeetingRequests:"
- "_query"
- "_queryResultData"
- "_queue"
- "_reachabilityChanged:"
- "_recordTypes"
- "_refCount"
- "_registerForCTDataUsageNotificaiton"
- "_registerForInterrogation:"
- "_removeBusyFolderIDs:forAccountWithID:"
- "_removeWatchedFolderIDs:forAccountWithID:"
- "_reportFolderItemsSyncResult:"
- "_reportSharedCalendarAsJunkEvent:eventDict:"
- "_requestAllFolderContentsUpdate:"
- "_requestAllFolderContentsUpdateForAccountId:dataclasses:isUserRequested:"
- "_requestCalendarAvailability:eventDict:"
- "_requestClientStatusDump:"
- "_requestFolderContentsUpdate:"
- "_requestFolderContentsUpdateForFolders:accountId:dataclasses:isUserRequested:"
- "_requestFolderListUpdate:"
- "_requestFolderListUpdateForAccountId:dataclasses:requireChangedFolders:isUserRequested:"
- "_requestID"
- "_requestParams"
- "_requestPolicyUpdate:"
- "_resetCertWarnings:"
- "_resetMonitoringRequestsAndLoadAgents"
- "_resetThrottleTimers:"
- "_respondToSharedCalendarEvent:eventDict:"
- "_responseParams"
- "_resultLimit"
- "_resumeMonitoringFolders:"
- "_runLoopStoppedRef"
- "_searchID"
- "_setFolderIdsThatExternalClientsCareAbout:"
- "_setRunLoopStopped:"
- "_setupServerConnection"
- "_shareID"
- "_shutdownDaemon"
- "_shutdownNotification:"
- "_skippedActions"
- "_startAgentsWhenSystemReadyBlock"
- "_startDate"
- "_startMonitoringAgents:"
- "_startMonitoringAgentsWithClientToken:"
- "_startMonitoringAgentsWithServerToken:"
- "_stopMonitoringAgents:"
- "_stopMonitoringAgentsWithClientToken:"
- "_stopMonitoringAndSaveAgents"
- "_stopMonitoringFolders:"
- "_subCalHandlers"
- "_suspendMonitoringFolders:"
- "_syncWhenReachable"
- "_systemMayNowBeReady"
- "_terms"
- "_updatedIDs"
- "_userSwitchTasks"
- "_watchedIDs"
- "abDB"
- "account"
- "accountDescription"
- "accountID"
- "accountIdentifier"
- "accountTimers"
- "accountType"
- "accountTypeIdentifier"
- "accountTypeWithAccountTypeIdentifier:"
- "accountWithAccountID:"
- "accountWithAccountID:andClassName:"
- "accountWithIDShouldContinue:"
- "accountsProviderWithDBHelper:"
- "accountsWithAccountType:"
- "actionDelegatesById"
- "actions"
- "activeAccountBundleIDs"
- "activeAgents"
- "addFolderIDToPingBlacklist:"
- "addLanguageChangeHandler"
- "addNetworkReachableObserver:selector:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addPendingAccountSetup"
- "addPersistMonitoringAccountID:folderIDs:clientID:"
- "addPersistentClientWithAccountID:clientID:watchedIDs:"
- "addSignalHandler"
- "addTimer:forMode:"
- "addToCoreDAVLoggingDelegates"
- "addToOperationsQueueDisabledCheckAndGoBlock:wrappedBlock:"
- "addressBook"
- "agentClassForACAccount:"
- "agentMonitoringTokens"
- "agentWithAccountID:"
- "allAccounts"
- "allKeys"
- "allObjects"
- "allValues"
- "allowFolderWipe"
- "applyClientStatusReportToAggregator:"
- "applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
- "archivedDataWithRootObject:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "asContainer"
- "asDeviceID"
- "asSource"
- "attachmentUUID"
- "autorelease"
- "backingAccountInfo"
- "begin"
- "beginDownload"
- "beginDownloadingAttachmentWithUUID:consumer:"
- "beginMonitoringPersistentFolders:forAccount:"
- "beginQuery"
- "beginSettingsRequest"
- "boolValue"
- "bundleID"
- "busyIDs"
- "calCloseDatabaseForAccountID:save:"
- "calCloseDatabaseForAuxDatabaseRef:save:"
- "calDatabaseForAccountID:"
- "calDatabaseForAuxDatabaseRef:"
- "calOpenDatabaseAsGenericClientForAccountID:"
- "calOpenDatabaseAsGenericClientForAuxDatabaseRef:"
- "calSaveDatabaseForAccountID:"
- "calendarAvailabilityRequestFinishedWithError:"
- "calendarAvailabilityRequestReturnedResults:"
- "calendarDirectorySearchFinishedWithError:exceededResultLimit:"
- "calendarDirectorySearchReturnedResults:"
- "calendarID"
- "cancelCalendarAvailabilityRequestWithID:"
- "cancelCalendarDirectorySearchWithID:"
- "cancelDownloadingInstance:error:"
- "cancelSearchQuery:"
- "cancelShareResponseInstance:error:"
- "changeHistoryClerkWithDBHelper:"
- "class"
- "cleanUpFilesForAccountWithId:"
- "cleanupLaunchdSemaphore"
- "clearFolderIdsForPersistentPushWithClientID:"
- "clearPersistMonitoringAccountID:clientID:"
- "clerkWithAddressBook:"
- "clerkWithContactStore:"
- "client"
- "clientBehaviorForFolderContents"
- "clientBehaviorForFolderIds:"
- "clientBehaviorForFolderList"
- "clientBundleID"
- "clientName"
- "clientUniqueID"
- "clients"
- "clientsToInterrogate"
- "code"
- "completelyIgnoreNotes"
- "conformsToProtocol:"
- "conn"
- "consumerCancelled"
- "contactStore"
- "containsObject:"
- "containsPostponedActions"
- "convertToDAOofParams"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentHandler"
- "currentPolicyKey"
- "currentPolicyKeyForAccount:"
- "d"
- "d16@0:8"
- "da_newGUID"
- "daemonAppropriateAccountClassForACAccount:"
- "dataWithPropertyList:format:options:error:"
- "databaseIsCorrupt:"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "defaultCenter"
- "defaultManager"
- "deferredAllFolderContentsSource"
- "deferredFolderContentsSource"
- "deferredFolderListSource"
- "deferredTimerInterval"
- "delegateID"
- "delegateWithIDIsGoingAway:"
- "deleteAccount:"
- "description"
- "deviceDidWake"
- "deviceWillSleep"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "didFinishAllXPCTransactions"
- "didReceiveDarwinNotification:"
- "disable"
- "disableActiveSync"
- "disableDaemon"
- "disableMonitoringAgentsTokens"
- "displayName"
- "domain"
- "downloadFinishedError:"
- "downloadID"
- "downloadProgressDownloadedByteCount:totalByteCount:"
- "emailAddress"
- "emailAddresses"
- "enableActiveSync"
- "enableChangeLogging:"
- "enableDaemon"
- "enableMonitoringAgentsWithToken:"
- "enabledDataclasses"
- "enabledDataclassesBitmask"
- "enabledForAnyDADataclasses:"
- "end"
- "endDailyAggDReporter"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "exchangeConnection"
- "fileSystemRepresentation"
- "finishWithError:"
- "finished"
- "firstName"
- "flushWithCompletionHandler:"
- "folder"
- "folderIdToLastFolderContentsRequestDate"
- "getBytes:range:"
- "getCFRunLoop"
- "getDAAccount"
- "getStatusReportDictsWithCompletionBlock:"
- "get_kCalPreferredDaysToSyncKey"
- "get_kCalRemindersPreferredDaysToSyncKey"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleURLString:"
- "hasActiveAccounts"
- "hasEASAccountConfigured"
- "hasPendingAccountSetup"
- "hasPrefix:"
- "hasRemoteChanges"
- "hash"
- "host"
- "i"
- "i16@0:8"
- "identifier"
- "identifiersOfAllRegisterdClients"
- "init"
- "initForReadingFromData:error:"
- "initWithAccount:"
- "initWithAccountID:attachmentUUID:client:"
- "initWithAccountID:client:"
- "initWithAccountID:client:calendarID:"
- "initWithAccountID:client:startDate:endDate:ignoredEventID:addresses:"
- "initWithAccountID:client:terms:recordTypes:resultLimit:"
- "initWithAccountID:queryDictionary:client:"
- "initWithAccountID:requestDictionary:forUpdate:client:"
- "initWithAddressBook:"
- "initWithArray:"
- "initWithBackingAccountInfo:"
- "initWithCapacity:"
- "initWithClientID:"
- "initWithConnection:clientID:"
- "initWithContactStore:"
- "initWithContentsOfFile:"
- "initWithDictionary:"
- "initWithDictionaryRepresentation:"
- "initWithDictionaryRepresentation:consumer:"
- "initWithFireDate:interval:target:selector:userInfo:repeats:"
- "initWithFolder:hasRemoteChanges:isInitialUberSync:"
- "initWithIdentifier:description:"
- "initWithLabel:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithStatusReports:numOutstandingReports:timeout:completionBlock:"
- "initWithTask:options:"
- "intValue"
- "intersectSet:"
- "intersectsSet:"
- "invalidate"
- "isAccountID:folderID:watchedByClientBesides:"
- "isAppleInternalInstall"
- "isDisabled"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isHotmailAccount"
- "isInHoldingPattern"
- "isInitialUberSync"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMonitoring"
- "isMonitoringAccountID:folderID:"
- "isOofSupported"
- "isProxy"
- "isResyncAfterConnectionFailed"
- "isResyncAfterServerError"
- "isSubscribedCalendarAccount"
- "isUpdate"
- "isWaitingForPassword"
- "keychainAccessibilityType"
- "killAllTimers"
- "lastAllFolderContentsRequestDate"
- "lastFolderListRequestDate"
- "lastFolderWipeRequestDate"
- "lastName"
- "lastRetryTimeout"
- "length"
- "loadAgents"
- "loadDaemonBundleForACAccountType:"
- "loadExchangeAgents"
- "mainConnection"
- "mainRunLoop"
- "mergeStatusReport:"
- "minusSet:"
- "monitorFoldersWithIDs:"
- "mutableCopy"
- "name"
- "networkReachableBlock"
- "nextDisableMonitoringAgentsToken"
- "noteAdditionalReportDicts:"
- "noteBlockedClientCallChange:"
- "noteRefreshClientCallChange:"
- "numOutstandingBlockingClientCalls"
- "numOutstandingRefreshPriorityClientCalls"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "observeReachabilityWithBlock:"
- "onBehalfOfBundleIdentifier"
- "oof"
- "oofGetResult"
- "orphanCheckEnabled"
- "os_log"
- "parentAccountIdentifier"
- "password"
- "performCalendarDirectorySearchForTerms:recordTypes:resultLimit:consumer:"
- "performRequest"
- "performSearchQuery:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistent"
- "persistentClientCleanup"
- "persistentUUID"
- "policyManager"
- "port"
- "postNotificationName:object:"
- "preferredDaysToSyncDidChange"
- "preferredEventDaysToSync"
- "preferredToDoDaysToSync"
- "processDAFolderChange:withCompletionBlock:"
- "processFolderChange:forAccountWithID:completionBlock:"
- "processMeetingRequestDatas:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:callback:"
- "processMeetingRequestDatas:deliveryIdsToClear:deliveryIdsToSoftClear:inFolderWithId:forAccountWithId:callback:"
- "protocol"
- "protocolVersion"
- "providerWithAddressBook:"
- "providerWithContactStore:"
- "q16@0:8"
- "q24@0:8@16"
- "query"
- "queryResultData"
- "raise"
- "rawConnection"
- "reconnectWithConnection:"
- "refreshFolderListRequireChangedFolders:isUserRequested:"
- "refreshThrottleTime"
- "regions"
- "registerChangeHistoryClientIdentifier:forContainerIdentifier:error:"
- "registerClientWithIdentifier:forContainer:"
- "registerForBuddy"
- "registerForInterrogation"
- "registerUserSwitchStakeHolder:"
- "release"
- "releaseWifiAssertion"
- "removeAllObjects"
- "removeClient:"
- "removeFolderIDFromPingBlacklist:"
- "removeFromAllPingHistoryBlacklistForFolderID:"
- "removeFromCoreDAVLoggingDelegates"
- "removeNetworkReachableObserver:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeObserver:name:object:"
- "removeOrphanedClientRestrictionsWithCompletion:"
- "removePendingAccountSetup"
- "removePersistMonitoringAccountID:folderIDs:clientID:"
- "removePersistentCredentials"
- "reportAsJunk"
- "reportFolderItemsSyncSuccess:forFolderWithID:withItemsCount:andAccountWithID:"
- "reportShareRequestAsJunkForCalendar:consumer:"
- "requestAgentStopMonitoringWithCompletionBlock:"
- "requestCalendarAvailabilityForStartDate:endDate:ignoredEventID:addresses:consumer:"
- "requestParams"
- "requestPolicyUpdate"
- "requestPolicyUpdateForAccount:"
- "requestPriority:forClient:dataclasses:"
- "resetCertWarnings"
- "resetCertWarningsForAccountWithId:andDataclasses:"
- "resetStatusReport"
- "resetSyncStatusIfNecessaryForStoresOfType:"
- "respondToShareRequestForCalendar:withResponse:consumer:"
- "respondToShareRequestWithResponse:"
- "respondsToSelector:"
- "responseParams"
- "resumeMonitoringAccountID:folderIDs:"
- "resumeMonitoringFoldersWithIDs:"
- "retain"
- "retainCount"
- "retainWifiAssertion"
- "retrieveOofSettingsForConsumer:"
- "save:"
- "saveAndReleaseAgents"
- "saveXpcActivity:"
- "searchQuery:finishedWithError:"
- "searchQuery:returnedResults:"
- "searchQuery:returnedTotalCount:"
- "self"
- "set"
- "setAccount:"
- "setAccountID:"
- "setAccountTimers:"
- "setActionDelegatesById:"
- "setActions:"
- "setAgentMonitoringTokens:"
- "setAttachmentUUID:"
- "setBusyIDs:"
- "setCalendarID:"
- "setClient:"
- "setClientBundleID:"
- "setClientName:"
- "setClientUniqueID:"
- "setClients:"
- "setConn:"
- "setConsumer:"
- "setConsumerCancelled:"
- "setContainsPostponedActions:"
- "setDeferredAllFolderContentsSource:"
- "setDeferredFolderContentsSource:"
- "setDeferredFolderListSource:"
- "setDelegateID:"
- "setDisplayName:"
- "setDownloadID:"
- "setExchangeConnection:"
- "setFinished:"
- "setFolder:"
- "setFolderIdToLastFolderContentsRequestDate:"
- "setFolderIdsForPersistentPushAdded:deleted:clientID:"
- "setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:"
- "setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:forAccountID:"
- "setHasRemoteChanges:"
- "setIsInitialUberSync:"
- "setIsMonitoring:"
- "setIsResyncAfterConnectionFailed:"
- "setIsResyncAfterServerError:"
- "setIsUpdate:"
- "setIsWaitingForPassword:"
- "setLastAllFolderContentsRequestDate:"
- "setLastFolderContentRequestDate:forFolderWithId:"
- "setLastFolderListRequestDate:"
- "setLastFolderWipeRequestDate:"
- "setLastRetryTimeout:"
- "setMainConnection:"
- "setNetworkReachableBlock:"
- "setNextDisableMonitoringAgentsToken:"
- "setNumOutstandingBlockingClientCalls:"
- "setNumOutstandingRefreshPriorityClientCalls:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPreferredAddress:"
- "setProtocolVersion:"
- "setQuery:"
- "setQueryResultData:"
- "setRequestParams:"
- "setResponseParams:"
- "setRunLoopStoppedRef:"
- "setShareID:"
- "setSkippedActions:"
- "setSubCalHandlers:"
- "setSyncWhenReachable:"
- "setSyncingAllowed:"
- "setTransactionMonitorDelegate:"
- "setUpdatedIDs:"
- "setUserSwitchTasks:"
- "setWasUserInitiated:"
- "setWatchedIDs:"
- "setWithArray:"
- "settingsRequestFinishedWithResults:status:error:"
- "shareID"
- "shareResponseFinishedWithError:"
- "shared"
- "sharedBabysitter"
- "sharedConnection"
- "sharedDBWatcher"
- "sharedGateKeeper"
- "sharedInstance"
- "sharedInstanceForAccountType:creatingClass:"
- "sharedKeychain"
- "sharedMain"
- "sharedManager"
- "sharedNetworkObserver"
- "sharedPowerAssertionManager"
- "sharedRunLoop"
- "sharedSession"
- "sharedTransactionMonitor"
- "sharedWifiAssertionManager"
- "shutdown"
- "shutdownDAD"
- "skippedActions"
- "startDailyAggDReporter"
- "startMonitoring"
- "startMonitoringAccountID:folderIDs:"
- "stateString"
- "statusReport"
- "stopMonitoringAccountID:folderIDs:"
- "stopMonitoringFoldersWithIDs:"
- "stopObservingReachability"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subCalHandlers"
- "substringFromIndex:"
- "superclass"
- "supportsSettingsCommand"
- "suspendMonitoringAccountID:folderIDs:"
- "suspendMonitoringFoldersWithIDs:"
- "syncFolderIDs:forDataclasses:isUserRequested:"
- "syncWhenReachable"
- "taskWithName:reason:forBundleID:"
- "timeIntervalSinceDate:"
- "timersForAccountWithID:"
- "transactionCount"
- "transactionId"
- "trustHandler"
- "unionSet:"
- "unregisterChangeHistoryClientIdentifier:forContainerIdentifier:error:"
- "unregisterClientWithIdentifier:forContainer:"
- "unregisterForInterrogation"
- "unsignedIntegerValue"
- "updateContentsOfAllFoldersForAccountID:andDataclasses:isUserRequested:"
- "updateContentsOfFolders:forAccountID:andDataclasses:isUserRequested:"
- "updateFolderListForAccountID:andDataclasses:requireChangedFolders:isUserRequested:"
- "updateOofSettingsWithParams:consumer:"
- "updatedIDs"
- "useContacts"
- "userInfo"
- "userRequestsCancel"
- "userSwitchTasks"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8^B16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"NSError\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"DASearchQuery\"16@\"NSArray\"24"
- "v32@0:8@\"DASearchQuery\"16@\"NSError\"24"
- "v32@0:8@\"DASearchQuery\"16@\"NSNumber\"24"
- "v32@0:8@16@24"
- "v32@0:8@?16@?24"
- "v32@0:8q16q24"
- "v36@0:8@16q24B32"
- "v40@0:8@\"ASSettingsTaskResponse\"16q24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24B32B36"
- "v44@0:8@16@24q32B40"
- "v44@0:8B16@20Q28@36"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@16@24@32@40@48@?56"
- "waitForSystemAvailability"
- "waiterID"
- "watchedFolderCount"
- "watchedIDs"
- "willSwitchUser"
- "writeToFile:atomically:"
- "zone"

```

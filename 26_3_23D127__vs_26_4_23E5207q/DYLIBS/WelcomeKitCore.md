## WelcomeKitCore

> `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-829.80.170.0.0
-  __TEXT.__text: 0x36744
-  __TEXT.__auth_stubs: 0xd80
+1224.100.67.0.0
+  __TEXT.__text: 0x38734
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_methlist: 0x336c
   __TEXT.__const: 0x238
   __TEXT.__cstring: 0xb34e
-  __TEXT.__gcc_except_tab: 0xfcc
-  __TEXT.__unwind_info: 0xd00
+  __TEXT.__gcc_except_tab: 0xf64
+  __TEXT.__unwind_info: 0xe10
   __TEXT.__objc_classname: 0x56d
   __TEXT.__objc_methname: 0x881f
   __TEXT.__objc_methtype: 0x17fa

   __DATA_CONST.__objc_selrefs: 0x21a0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6a8
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x6de0
   __AUTH_CONST.__objc_const: 0x5120

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: E3F4EA44-4535-3614-AD3A-DABFEA619267
-  Functions: 1181
-  Symbols:   4623
+  UUID: 032677C3-0B1E-3405-B6AE-90AD5C02583A
+  Functions: 1182
+  Symbols:   4620
   CStrings:  3616
 
Symbols:
+ _OUTLINED_FUNCTION_0
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
Functions:
~ +[WLAuthenticationCredentials generateAuthenticationCredentialsContainingSelfSignedCertificate] : 244 -> 248
~ +[WLAuthenticationUtilities hashWithString:] : 260 -> 268
~ +[WLAuthenticationUtilities generateSelfSignedCertificateWithOrganization:commonName:completion:] : 664 -> 668
~ +[WLAuthenticationUtilities pemFormattedCertificateData:] : 164 -> 172
~ +[WLAuthenticationUtilities _appendBase64Data:toString:] : 104 -> 108
~ +[WLAuthenticationUtilities dataFromPEMFormattedData:] : 436 -> 444
~ +[WLCredentialStore sharedInstance] : 68 -> 84
~ -[WLCredentialStore setCredentials:forAuthentication:] : 152 -> 148
~ -[WLCredentialStore credentialsForAuthentication:] : 204 -> 208
~ -[WLSRPServer initWithUsername:password:] : 428 -> 432
~ -[WLSRPServer didReceiveClientPublicKey_A:proofOfMatch_M:] : 564 -> 588
~ -[WLSRPServer isHmacData:validForData:] : 204 -> 216
~ -[WLAutomation writeCodeForTestAutomationIfNeeded:] : 516 -> 544
~ -[WLAutomation deleteTestAutomationCachesIfNeeded] : 316 -> 336
~ +[WLDeviceDiscoveryController sharedInstance] : 68 -> 84
~ -[WLDeviceDiscoveryController init] : 176 -> 184
~ -[WLDeviceDiscoveryController sourceDevice] : 116 -> 120
~ -[WLDeviceDiscoveryController startWiFiAndDeviceDiscoveryWithPreGeneratedCode:completion:] : 236 -> 224
~ ___90-[WLDeviceDiscoveryController startWiFiAndDeviceDiscoveryWithPreGeneratedCode:completion:]_block_invoke_2 : 224 -> 216
~ ___84-[WLDeviceDiscoveryController _queue_startDiscoveryWithPreGeneratedCode:completion:]_block_invoke : 220 -> 224
~ -[WLDeviceDiscoveryController enableSoftAPWithSSID:password:channels:secret:srp:completion:] : 560 -> 520
~ -[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:] : 524 -> 484
~ ___130-[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:]_block_invoke : 312 -> 308
~ -[WLDeviceDiscoveryController softAPDidStart:ssid:psk:secret:srp:channel:error:completion:] : 1036 -> 1028
~ -[WLDeviceDiscoveryController listenerDidStart:srp:] : 500 -> 508
~ -[WLDeviceDiscoveryController stopDeviceDiscoveryWithCompletion:] : 204 -> 200
~ -[WLDeviceDiscoveryController stopWiFiAndDeviceDiscoveryWithCompletion:] : 204 -> 200
~ ___72-[WLDeviceDiscoveryController stopWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke : 220 -> 228
~ ___72-[WLDeviceDiscoveryController stopWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke_2 : 188 -> 196
~ -[WLDeviceDiscoveryController _queue_stopWiFiAndDeviceDiscoveryWithCompletion:] : 328 -> 336
~ -[WLDeviceDiscoveryController importLocalContent] : 212 -> 220
~ -[WLDeviceDiscoveryController attemptDirectConnectionToAddress:] : 364 -> 384
~ -[WLDeviceDiscoveryController setNextIncomingConnectionHandler:] : 132 -> 128
~ -[WLDeviceDiscoveryController _ssidWithSecret:] : 144 -> 156
~ -[WLDeviceDiscoveryController listenForConnectionOnSocket:withConnectionHandler:] : 224 -> 220
~ -[WLDeviceDiscoveryController acceptIncomingConnectionWithListenerSocket:nonBlocking:] : 756 -> 764
~ -[WLDeviceDiscoveryController _allowConnectionsFromAnyAddress] : 152 -> 156
~ -[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didDiscoverCandidate:] : 224 -> 220
~ -[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didFinishHandshakeWithSourceDevice:] : 200 -> 196
~ -[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didFailToHandshakeWithSourceDevice:error:] : 392 -> 388
~ ___101-[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didFailToHandshakeWithSourceDevice:error:]_block_invoke : 152 -> 156
~ -[WLDeviceDiscoveryController setQueue:] : 12 -> 64
~ -[WLDeviceDiscoverySocketHandler initWithSocket:srpPassword:delegate:] : 220 -> 216
~ -[WLDeviceDiscoverySocketHandler resume] : 144 -> 148
~ -[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake] : 4616 -> 4900
~ ___71-[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake]_block_invoke : 192 -> 200
~ ___71-[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake]_block_invoke_2 : 192 -> 200
~ ___71-[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake]_block_invoke_3 : 192 -> 200
~ -[WLDeviceDiscoverySocketHandler _commandStringWithData:] : 248 -> 256
~ -[WLDeviceDiscoverySocketHandler _okResponseData] : 96 -> 104
~ -[WLDeviceDiscoverySocketHandler _handshakeCommandData] : 96 -> 104
~ -[WLDeviceDiscoverySocketHandler _didReceiveHandshakeData:] : 368 -> 372
~ -[WLDeviceDiscoverySocketHandler _handshakeResponseData] : 772 -> 780
~ -[WLDeviceDiscoverySocketHandler sendData:completion:] : 204 -> 196
~ ___54-[WLDeviceDiscoverySocketHandler sendData:completion:]_block_invoke_2 : 124 -> 116
~ -[WLSourceDeviceHandshakeParser parseData:modifyingSourceDevice:completion:] : 412 -> 404
~ -[WLSourceDeviceHandshakeParser _parseDeviceInfoNode:modifyingSourceDevice:] : 1992 -> 2092
~ -[WLSourceDeviceHandshakeParser _parseConnectionFailureReasons:] : 192 -> 208
~ -[WLAccessibilityMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLAccessibilityMigrator importRecordData:summary:account:completion:] : 740 -> 748
~ -[WLApp initWithBundleIdentifier:appStoreIdentifier:isFree:] : 156 -> 152
~ -[WLApp setAppStoreIdentifier:] : 12 -> 64
~ -[NSError(WelcomeKit) wk_representsTransientConnectivityIssueForAttempt:] : 232 -> 240
~ -[WLAppMigrator initWithDevice:sqlController:] : 140 -> 136
~ -[WLAppMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLAppMigrator importDataFromProvider:forSummaries:summaryStart:summaryCompletion:] : 1212 -> 1232
~ ___84-[WLAppMigrator importDataFromProvider:forSummaries:summaryStart:summaryCompletion:]_block_invoke : 104 -> 112
~ -[WLAppMigrator _lookupStoreItemsMatchingExternalIDs:attempt:completion:] : 280 -> 268
~ ___73-[WLAppMigrator _lookupStoreItemsMatchingExternalIDs:attempt:completion:]_block_invoke : 508 -> 524
~ -[WLAppMigrator _insertMatchingApps:] : 648 -> 696
~ +[WLAppMigrator installMigratableApps:completion:] : 212 -> 204
~ ___50+[WLAppMigrator installMigratableApps:completion:]_block_invoke : 148 -> 156
~ ___50+[WLAppMigrator installMigratableApps:completion:]_block_invoke_2 : 180 -> 188
~ +[WLAppMigrator _sendStoreDownloadRequestForFreeMigratableApps:completion:] : 1268 -> 1300
~ ___75+[WLAppMigrator _sendStoreDownloadRequestForFreeMigratableApps:completion:]_block_invoke : 320 -> 348
~ ___75+[WLAppMigrator _sendStoreDownloadRequestForFreeMigratableApps:completion:]_block_invoke_2 : 140 -> 148
~ +[WLAppMigrator _ssItemForiTunesStoreIdentifier:] : 388 -> 376
~ -[WLAppMigrator setDevice:] : 12 -> 64
~ -[WLAppMigrator setSqlController:] : 12 -> 64
~ -[WLAppSearchRequest initWithAndroidIdentifiers:] : 140 -> 144
~ -[WLAppSearchRequest search:] : 508 -> 528
~ ___29-[WLAppSearchRequest search:]_block_invoke : 908 -> 948
~ -[WLBookmarksMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLBookmarksMigrator importWillBegin] : 432 -> 444
~ +[WLBookmarksMigrator _createBookmarkFolderWithTitle:UUID:] : 216 -> 212
~ +[WLBookmarksMigrator _createRootBookmarkFolder] : 208 -> 228
~ +[WLBookmarksMigrator _bookmarkFolderAtTitlePath:withinBookmarkFolder:] : 620 -> 648
~ +[WLBookmarksMigrator _bookmarkFolderAtTitlePath:withinRootFolder:] : 184 -> 200
~ -[WLBookmarksMigrator importDataFromProvider:forSummaries:summaryStart:summaryCompletion:] : 1856 -> 1888
~ -[WLCalendarMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLCalendarMigrator importRecordData:summary:account:completion:] : 240 -> 236
~ -[WLCalendarMigrator _importDataRecord:summary:] : 200 -> 204
~ -[WLContactsMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLContactsMigrator _vcardDataWithoutCustomFieldsFromVcardData:] : 964 -> 1004
~ -[WLContactsMigrator setContactStore:] : 12 -> 64
~ -[WLDisplayMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLDisplayMigrator importRecordData:summary:account:completion:] : 648 -> 656
~ -[WLMailAccountMigrator init] : 692 -> 720
~ -[WLMailAccountMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLMailAccountMigrator importRecordData:summary:account:completion:] : 1248 -> 1272
~ -[WLMailAccountMigrator importWillBegin] : 256 -> 264
~ -[WLMailAccountMigrator setAccountStore:] : 12 -> 64
~ +[WLMessage _populateMimeHeaders:recipients:fromRange:ofString:addCountryCodeToParties:sqlController:] : 700 -> 728
~ +[WLMessage _dateFormatterForMimeDateStrings] : 68 -> 84
~ ___45+[WLMessage _dateFormatterForMimeDateStrings]_block_invoke : 184 -> 188
~ +[WLMessage dateFromMimeHeaders:] : 204 -> 216
~ -[WLMessage parseMIMEData:sqlController:] : 2080 -> 2180
~ +[WLMessage _fileNameForPart:smilContext:] : 596 -> 624
~ ___41+[WLMessage _shouldIgnoreMessageThreadID]_block_invoke : 140 -> 144
~ -[WLMessage progressiveMimeParser:finishedMimePart:] : 948 -> 992
~ -[WLMessage summary] : 8 -> 56
~ -[WLMessage setSummary:] : 12 -> 64
~ -[WLMessage setSender:] : 12 -> 64
~ -[WLMessage setRecipients:] : 12 -> 64
~ -[WLMessageAttachment _initWithData:fileName:mimeType:uti:] : 224 -> 208
~ -[WLMessageParty _initWithAddress:addCountryCode:sqlController:] : 1764 -> 1860
~ +[WLMessageParty _guessIccForNumber:] : 428 -> 440
~ ___37+[WLMessageParty _guessIccForNumber:]_block_invoke : 232 -> 244
~ +[WLMessageParty _normalize:] : 292 -> 308
~ ___29+[WLMessageParty _normalize:]_block_invoke : 224 -> 228
~ -[NSData(WLMessage) wl_subdataWithRangeExcludingTrailingCrnl:] : 256 -> 268
~ -[WLMessageSMILContext parser:didStartElement:namespaceURI:qualifiedName:attributes:] : 316 -> 320
~ -[WLMessageSMILContext parser:foundCharacters:] : 136 -> 140
~ -[WLMessageSMILPart initWithElementName:attributes:] : 152 -> 144
~ -[WLMessageSMILPart fileName] : 100 -> 108
~ -[WLMessagesMigrator estimateItemSizeForSummary:account:] : 76 -> 84
~ -[WLMessagesMigrator performPreImportPhaseForSummary:data:] : 960 -> 1020
~ -[WLMessagesMigrator importWillBegin] : 340 -> 356
~ -[WLMessagesMigrator importDidEnd] : 172 -> 180
~ -[WLMessagesMigrator _databaseFilename] : 84 -> 92
~ -[WLMessagesMigrator _openDatabase] : 132 -> 136
~ -[WLMessagesMigrator _performSimpleQuery:] : 260 -> 264
~ -[WLMessagesMigrator _ourAddressWithMessage:] : 192 -> 216
~ -[WLMessagesMigrator _otherPartyAddressWithNonGroupMessage:] : 176 -> 200
~ -[WLMessagesMigrator _insertMessage:] : 2384 -> 2528
~ +[WLMessagesMigrator _attachmentPersistentPathForGuid:fileName:mimeType:uti:] : 676 -> 708
~ -[WLMessagesMigrator _insertRowWithAttachment:filePath:forMessage:] : 836 -> 856
~ -[WLMessagesMigrator _uniqueHandleStringsWithMessage:] : 688 -> 728
~ -[WLMessagesMigrator _senderHandleIDFromReceivedGroupMessageHandleIDs:] : 64 -> 68
~ -[WLMessagesMigrator _handleIDFromNonGroupMessageHandleIDs:] : 64 -> 68
~ -[WLMessagesMigrator _chatIDForHandleIDs:groupRoomName:groupID:message:] : 2048 -> 2044
~ -[WLMessagesMigrator _chatGUIDWithNonGroupMessage:] : 104 -> 112
~ -[WLMessagesMigrator _chatAccountIDWithMessage:] : 8 -> 56
~ -[WLMessagesMigrator _chatAccountLoginWithMessage:] : 104 -> 112
~ -[WLMessagesMigrator _insertMessageRowWithMessage:handleIDs:groupRoomName:] : 1296 -> 1324
~ -[WLMessagesMigrator _messageAttributedBodyDataWithMessage:] : 584 -> 612
~ -[WLMessagesMigrator _messageAccountWithMessage:] : 104 -> 112
~ -[WLMessagesMigrator _messageAccountGUIDWithMessage:] : 8 -> 56
~ -[WLMessagesMigrator _messageDateWithMessage:] : 72 -> 76
~ -[WLMessagesMigrator _messageDateReadWithMessage:] : 72 -> 76
~ -[WLMessagesMigrator _messageDateDeliveredWithMessage:] : 72 -> 76
~ -[WLMessagesMigrator _attachmentDateWithMessage:] : 60 -> 64
~ -[WLMessagesMigrator _updateClient] : 332 -> 336
~ -[WLMessagesMigrator isValidTableName:] : 172 -> 184
~ -[WLMessagesMigrator deleteFromTable:] : 332 -> 336
~ -[WLMessagesMigrator setSqlController:] : 12 -> 64
~ -[WLFileProvider fetchRootPath] : 472 -> 492
~ -[WLFilesMigrator init] : 168 -> 172
~ -[WLFilesMigrator importRecordData:summary:account:completion:] : 1716 -> 1808
~ -[WLPhotoLibrary init] : 388 -> 408
~ -[WLPhotoLibrary addAsset:filename:size:collection:completion:] : 808 -> 796
~ ___63-[WLPhotoLibrary addAsset:filename:size:collection:completion:]_block_invoke_2 : 156 -> 152
~ -[WLPhotoLibrary addAsset:collection:] : 488 -> 512
~ -[WLPhotoLibrary photoLibraryDidComplete:filename:success:error:] : 300 -> 312
~ -[WLPhotoLibrary copy:filename:error:] : 520 -> 548
~ -[WLPhotoLibrary assetCollectionChangeRequest:] : 240 -> 260
~ -[WLPhotosMigrator importRecordData:summary:account:completion:] : 360 -> 372
~ -[WLVideosMigrator importRecordData:summary:account:completion:] : 360 -> 372
~ -[WLSourceDeviceAccount initWithInfo:] : 96 -> 100
~ +[WLSourceDeviceAccount accountInfoArrayContainsNonSyncableAccount:] : 320 -> 328
~ +[WLSourceDeviceAccount accountInfoRepresentsSyncableAccount:] : 76 -> 80
~ -[WLSourceDeviceMigrationMetadata setCommunicationDate:] : 12 -> 64
~ -[WLSourceDeviceMigrationMetadata setDeviceOSVersion:] : 12 -> 64
~ -[WLSourceDeviceMigrationMetadata setDeviceType:] : 12 -> 64
~ -[WLSourceDeviceMigrationMetadata setDeviceModel:] : 12 -> 64
~ +[WLSourceDeviceRecordSummary summaryWithInfo:account:] : 116 -> 112
~ +[WLSourceDeviceRecordSummary _numberFormatter] : 68 -> 84
~ -[WLSourceDeviceRecordSummary initWithInfo:account:] : 648 -> 692
~ -[WLSourceDeviceRecordSummary setAccount:] : 12 -> 64
~ -[WLItemSizeConfirmationCompletionAdapter initWithUnconfirmedItemSize:segmentSize:originalSegmentCompletion:originalCompletion:] : 420 -> 412
~ ___128-[WLItemSizeConfirmationCompletionAdapter initWithUnconfirmedItemSize:segmentSize:originalSegmentCompletion:originalCompletion:]_block_invoke_2 : 196 -> 200
~ +[WLLocalDataSource _localSourceDataPath] : 68 -> 84
~ ___41+[WLLocalDataSource _localSourceDataPath]_block_invoke : 92 -> 100
~ +[WLLocalDataSource localDataExists] : 124 -> 132
~ -[WLLocalDataSource accountsDataForMigrator:completion:] : 760 -> 804
~ -[WLLocalDataSource summariesDataForAccount:migrator:completion:] : 976 -> 1020
~ -[WLLocalDataSource fileForSummary:migrator:fileAccessor:completion:] : 264 -> 280
~ -[WLLocalDataSource dataForSummary:migrator:completion:] : 304 -> 320
~ ___73-[WLLocalDataSource dataSegmentForSummary:byteRange:migrator:completion:]_block_invoke : 160 -> 164
~ -[WLLocalDataSource itemSizeForSummary:migrator:completion:] : 100 -> 104
~ +[WLLocalDataSource deleteLocalData] : 164 -> 168
~ +[WLLocalDataSource _relativePathForAccount:migrator:] : 288 -> 316
~ +[WLLocalDataSource _relativePathForSummary:migrator:] : 384 -> 424
~ +[WLLocalDataSource stashFileForSummary:migrator:] : 464 -> 492
~ +[WLLocalDataSource stashData:forSummary:migrator:] : 444 -> 464
~ -[WLMigrationContext setSourceDevice:] : 12 -> 64
~ -[WLMigrationContext setDelegate:] : 12 -> 64
~ -[WLMigrationContext setDataSource:] : 12 -> 64
~ -[WLMigrationContext setDataCoordinator:] : 12 -> 64
~ -[WLMigrationContext setSqlController:] : 12 -> 64
~ -[WLMigrationContext setMigrators:] : 12 -> 64
~ -[WLMigrationContext setLastProgressSentDate:] : 12 -> 64
~ -[WLMigrationContext setThroughputSegmentStartDate:] : 12 -> 64
~ -[WLMigrationContext setThroughputSamples:] : 12 -> 64
~ -[WLMigrationContext setTimeEstimateAccuracyTracker:] : 12 -> 64
~ -[WLMigrationContext setUrlSessionController:] : 12 -> 64
~ -[WLMigrationContext setAggregateStatistics:] : 12 -> 64
~ -[WLMigrationContext setMetadata:] : 12 -> 64
~ -[WLMigrationContext setImportErrors:] : 12 -> 64
~ -[WLMigrationContext setPayload:] : 12 -> 64
~ -[WLMigrationDataCoordinator init] : 136 -> 144
~ -[WLMigrationDataCoordinator fetchAccountsAndSummariesFromSource:forMigrator:statistics:accountsRequestDurationBlock:summariesRequestDurationBlock:completion:] : 444 -> 404
~ ___159-[WLMigrationDataCoordinator fetchAccountsAndSummariesFromSource:forMigrator:statistics:accountsRequestDurationBlock:summariesRequestDurationBlock:completion:]_block_invoke : 804 -> 796
~ ___89-[WLMigrationDataCoordinator _fetchAccountsFromSource:forMigrator:statistics:completion:]_block_invoke : 532 -> 540
~ -[WLMigrationDataCoordinator _fetchSummariesFromSource:forMigrator:account:statistics:completion:] : 424 -> 404
~ ___98-[WLMigrationDataCoordinator _fetchSummariesFromSource:forMigrator:account:statistics:completion:]_block_invoke : 612 -> 632
~ -[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:] : 1076 -> 1036
~ ___110-[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:]_block_invoke : 292 -> 304
~ ___110-[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:]_block_invoke_2 : 324 -> 332
~ ___110-[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:]_block_invoke_3 : 176 -> 180
~ ___49+[WLMigrationDataCoordinator downloadSegmentSize]_block_invoke : 180 -> 184
~ -[WLMigrationDataCoordinator _downloadSegmentsFromSource:forMigrator:startingAtByteLocation:ofSummary:account:itemSize:toFileHandle:segmentCompletion:completion:] : 688 -> 660
~ ___162-[WLMigrationDataCoordinator _downloadSegmentsFromSource:forMigrator:startingAtByteLocation:ofSummary:account:itemSize:toFileHandle:segmentCompletion:completion:]_block_invoke : 256 -> 252
~ -[WLMigrationDataCoordinator _downloadFileInMultipleSegmentsFromSource:forMigrator:summary:account:itemSize:segmentCompletion:completion:] : 912 -> 948
~ ___138-[WLMigrationDataCoordinator _downloadFileInMultipleSegmentsFromSource:forMigrator:summary:account:itemSize:segmentCompletion:completion:]_block_invoke : 144 -> 148
~ -[WLMigrationDataCoordinator downloadDataFromSource:forMigrator:summary:account:completion:] : 452 -> 436
~ ___92-[WLMigrationDataCoordinator downloadDataFromSource:forMigrator:summary:account:completion:]_block_invoke : 252 -> 256
~ -[WLMigrationDataCoordinator importDataForMigrator:fromProvider:forSummaries:summaryStart:summaryCompletion:] : 1004 -> 984
~ ___81-[WLMigrationDataCoordinator updateSource:withProgress:remainingTime:completion:]_block_invoke : 132 -> 140
~ -[WLMigrationDataCoordinator _recordSummaryForMigrator:withInfo:account:] : 592 -> 656
~ -[WLMigrator _deleteDownloadsPath:] : 164 -> 156
~ -[WLMigrator _prepareMetadata:usingRetryPolicies:allowContinuationFromAnotherDevice:] : 572 -> 592
~ -[WLMigrator startMigrationWithSourceDevice:usingRetryPolicies:delegate:completion:] : 184 -> 180
~ -[WLMigrator prepare:delegate:error:] : 1396 -> 1508
~ -[WLMigrator startMigration:usingRetryPolicies:completion:] : 1916 -> 2116
~ -[WLMigrator migrators:] : 1156 -> 1260
~ -[WLMigrator fetchSummary:] : 724 -> 804
~ -[WLMigrator selectDataTypes:] : 540 -> 588
~ -[WLMigrator downloadData:] : 1344 -> 1396
~ ___27-[WLMigrator downloadData:]_block_invoke.115 : 16 -> 72
~ -[WLMigrator importData:] : 1116 -> 1188
~ ___25-[WLMigrator importData:]_block_invoke : 16 -> 72
~ -[WLMigrator runPostMigrationTasks:] : 96 -> 104
~ -[WLMigrator finishMigration:] : 968 -> 1032
~ -[WLMigrator _finishMigrationWithError:context:disconnected:completion:] : 944 -> 1012
~ -[WLMigrator _fetchAccountsAndSummariesWithContext:] : 1180 -> 1220
~ ___52-[WLMigrator _fetchAccountsAndSummariesWithContext:]_block_invoke : 280 -> 312
~ ___52-[WLMigrator _fetchAccountsAndSummariesWithContext:]_block_invoke_2 : 280 -> 312
~ ___52-[WLMigrator _fetchAccountsAndSummariesWithContext:]_block_invoke_3 : 620 -> 632
~ -[WLMigrator _selectDataTypesWithContext:] : 2140 -> 2232
~ ___42-[WLMigrator _selectDataTypesWithContext:]_block_invoke : 344 -> 380
~ ___42-[WLMigrator _selectDataTypesWithContext:]_block_invoke_2 : 196 -> 200
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke : 2724 -> 2744
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_2 : 204 -> 220
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_3 : 232 -> 248
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_4 : 148 -> 152
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_5 : 168 -> 172
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_6 : 148 -> 152
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_8 : 148 -> 152
~ +[WLMigrator _dataTypesAndSizesXMLDataFromMap:] : 636 -> 692
~ +[WLMigrator _parseDataTypesXMLData:completion:] : 768 -> 784
~ -[WLMigrator _downloadDataWithContext:failureDetailsBlock:] : 3908 -> 4112
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke : 248 -> 260
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_3 : 152 -> 160
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_4 : 104 -> 108
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_5 : 344 -> 348
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_7 : 352 -> 380
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_8 : 536 -> 552
~ -[WLMigrator _didFinishDownloadingSegmentOfSize:expectedSize:migratorEstimatesItemSizes:endDate:context:] : 1388 -> 1456
~ -[WLMigrator _reportTimeEstimatesWithContext:] : 132 -> 140
~ ___46-[WLMigrator _reportTimeEstimatesWithContext:]_block_invoke : 140 -> 144
~ -[WLMigrator _importDataWithContext:failureDetailsBlock:] : 1872 -> 1948
~ ___57-[WLMigrator _importDataWithContext:failureDetailsBlock:]_block_invoke : 108 -> 116
~ ___57-[WLMigrator _importDataWithContext:failureDetailsBlock:]_block_invoke_2 : 96 -> 100
~ ___57-[WLMigrator _importDataWithContext:failureDetailsBlock:]_block_invoke_3 : 568 -> 600
~ -[WLMigrator _progressIncrementForImportedSummary:summaries:accounts:migrators:] : 156 -> 152
~ -[WLMigrator _logStatisticsAndSendStatisticsTelemetryWithContext:] : 1416 -> 1544
~ +[WLMigrator _systemVersion] : 84 -> 88
~ -[WLMigrator close:] : 228 -> 224
~ -[WLMigrator cleanup] : 140 -> 148
~ -[WLMigrator finalizeMigratableAppsWithCompletion:] : 360 -> 368
~ ___51-[WLMigrator finalizeMigratableAppsWithCompletion:]_block_invoke : 352 -> 368
~ +[WLMigrator _presentPromptForMigrableApps:] : 480 -> 500
~ -[WLMigrator _cleanUpAfterFinalizeMigratableAppsWithSQLController:completion:] : 112 -> 116
~ -[WLMigrator _setProgressTo:context:] : 212 -> 228
~ -[WLMigrator _incrementProgressBy:context:] : 240 -> 256
~ -[WLMigrator _updateSourceWithProgress:remainingTime:context:completion:] : 544 -> 564
~ ___73-[WLMigrator _updateSourceWithProgress:remainingTime:context:completion:]_block_invoke_2 : 192 -> 196
~ +[WLMigrator _bytesFreeOnDevice] : 176 -> 180
~ -[WLMigrator setDataSource:] : 12 -> 64
~ -[WLRemoteDeviceDataSource accountsDataForMigrator:completion:] : 276 -> 280
~ ___63-[WLRemoteDeviceDataSource accountsDataForMigrator:completion:]_block_invoke : 468 -> 460
~ -[WLRemoteDeviceDataSource _urlForAccountsWithMigrator:] : 204 -> 220
~ -[WLRemoteDeviceDataSource summariesDataForAccount:migrator:completion:] : 324 -> 328
~ ___72-[WLRemoteDeviceDataSource summariesDataForAccount:migrator:completion:]_block_invoke : 472 -> 464
~ -[WLRemoteDeviceDataSource _urlForRecordSummariesForMigrator:withAccountIdentifier:] : 376 -> 412
~ -[WLRemoteDeviceDataSource itemSizeForSummary:migrator:completion:] : 372 -> 384
~ -[WLRemoteDeviceDataSource fileForSummary:migrator:fileAccessor:completion:] : 396 -> 404
~ ___76-[WLRemoteDeviceDataSource fileForSummary:migrator:fileAccessor:completion:]_block_invoke : 164 -> 168
~ -[WLRemoteDeviceDataSource _urlForRecordForMigrator:withSummaryIdentifier:accountIdentifier:segmentByteRange:] : 668 -> 716
~ -[WLRemoteDeviceDataSource _performDownloadRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:] : 500 -> 488
~ ___131-[WLRemoteDeviceDataSource _performDownloadRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:]_block_invoke : 284 -> 292
~ -[WLRemoteDeviceDataSource _downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:] : 392 -> 368
~ ___132-[WLRemoteDeviceDataSource _downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:]_block_invoke : 1392 -> 1376
~ ___132-[WLRemoteDeviceDataSource _downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:]_block_invoke_5 : 272 -> 280
~ -[WLRemoteDeviceDataSource dataSegmentForSummary:byteRange:migrator:completion:] : 376 -> 388
~ ___80-[WLRemoteDeviceDataSource dataSegmentForSummary:byteRange:migrator:completion:]_block_invoke : 252 -> 256
~ -[WLRemoteDeviceDataSource dataForSummary:migrator:completion:] : 368 -> 380
~ ___63-[WLRemoteDeviceDataSource dataForSummary:migrator:completion:]_block_invoke : 252 -> 256
~ -[WLRemoteDeviceDataSource updateUIWithProgress:remainingTime:logString:completion:] : 448 -> 464
~ -[WLRemoteDeviceDataSource _urlScheme] : 68 -> 84
~ +[WLRemoteDeviceDataSource _requestSerialQueue] : 68 -> 84
~ ___47+[WLRemoteDeviceDataSource _requestSerialQueue]_block_invoke : 104 -> 108
~ -[WLRemoteDeviceDataSource _performRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:] : 420 -> 408
~ ___174-[WLRemoteDeviceDataSource _performRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:]_block_invoke : 336 -> 348
~ -[WLRemoteDeviceDataSource _runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:] : 516 -> 508
~ ___178-[WLRemoteDeviceDataSource _runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:]_block_invoke : 728 -> 744
~ ___178-[WLRemoteDeviceDataSource _runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:]_block_invoke_2 : 688 -> 704
~ -[WLRemoteDeviceDataSource _taskDurationSinceStartDate:] : 92 -> 96
~ -[WLRemoteDeviceDataSource _shouldRetryLaterWithResponse:error:] : 160 -> 156
~ -[WLRemoteDeviceDataSource _shouldRetryWithData:response:error:] : 208 -> 212
~ -[WLRemoteDeviceDataSource _newNumberOfRetriesAllowed:startDate:] : 204 -> 212
~ -[WLRemoteDeviceDataSource setSession:] : 12 -> 64
~ -[WLThroughputSample setStartDate:] : 12 -> 64
~ -[WLThroughputSample setEndDate:] : 12 -> 64
~ -[WLTimeEstimateSample setStartDate:] : 12 -> 64
~ -[WLTimeEstimateSample setAssociatedObject:] : 12 -> 64
~ -[WLTimeEstimateAccuracyTracker _thresholdAtIndex:] : 200 -> 220
~ -[WLTimeEstimateAccuracyTracker didCalculateTimeEstimate:atDate:associatedObject:] : 320 -> 328
~ -[WLTimeEstimateAccuracyTracker estimatesDidResolveAtDate:block:] : 412 -> 420
~ -[WLTimeEstimateAccuracyTracker setThresholds:] : 12 -> 64
~ -[WLTimeEstimateAccuracyTracker setSamples:] : 12 -> 64
~ -[WLURLSessionController initWithAuthentication:] : 272 -> 280
~ -[WLURLSessionController URLSession:didReceiveChallenge:completionHandler:] : 988 -> 1052
~ -[NSDictionary(Integer) wl_integerForKey:] : 124 -> 128
~ -[NSDictionary(String) wl_stringForKey:] : 88 -> 104
~ -[WLXMLSerialization XMLObjectWithString:] : 96 -> 104
~ -[WLXMLSerialization XMLObjectWithData:] : 164 -> 168
~ -[WLXMLSerialization parseXMLContent:] : 476 -> 492
~ -[NSData(Hex) wl_blobIsComplete] : 152 -> 156
~ +[NSData(Hex) wl_lengthPrefixedBlobSequenceFromDataArray:] : 356 -> 368
~ -[NSData(Hex) wl_lengthPrefixedBlob] : 192 -> 204
~ -[NSData(Hex) wl_arrayOfDataFromLengthPrefixedBlobSequenceWithExpectedCount:] : 456 -> 476
~ -[NSData(Hex) wl_dataFromLengthPrefixedBlob] : 80 -> 88
~ -[NSData(Hex) wl_hexEncodedData] : 80 -> 88
~ +[NSData(Hex) wl_dataFromHexEncodedData:] : 92 -> 100
~ +[NSData(Hex) wl_dataFromHexEncodedString:] : 432 -> 448
~ -[WLServerConnection _accept:] : 556 -> 560
~ -[WLServerConnection _read:] : 684 -> 688
~ -[WLSocketHandler observeSocket:forSourceEventType:handler:] : 224 -> 220
~ ___58+[WLSocketHandler lookupAndConnectToHost:port:completion:]_block_invoke : 648 -> 664
~ -[WLSocketHandler beginReadingIntoCacheFromSocket:] : 232 -> 236
~ -[WLSocketHandler _readIntoCacheFromSocket:] : 368 -> 376
~ -[WLSocketHandler endReadingIntoCache] : 136 -> 140
~ -[WLSocketHandler waitForDataFromReadCacheReturningError:] : 412 -> 424
~ -[WLSocketHandler waitForBlobDataFromReadCacheReturningError:] : 472 -> 480
~ -[WLSocketHandler waitForCommand:fromReadCacheReturningError:] : 564 -> 588
~ -[WLSocketHandler waitForMessageFromReadCacheReturningError:] : 372 -> 392
~ +[WLSocketHandler _commandStringWithData:] : 248 -> 256
~ -[WLSocketHandler _writeBytes:offset:length:toSocket:completion:] : 516 -> 524
~ -[WLSocketHandler sendCommand:toSocket:completion:] : 276 -> 280
~ -[WLSocketHandler sendData:toSocket:completion:] : 228 -> 224
~ ___48-[WLSocketHandler sendData:toSocket:completion:]_block_invoke : 120 -> 112
~ -[WLSocketHandler cancel] : 288 -> 296
~ +[WLSocketMessage messageWithData:error:] : 1960 -> 2072
~ -[WLSQLController init] : 172 -> 180
~ -[WLSQLController databasePath] : 8 -> 56
~ -[WLSQLController insertAccount:migrator:device:] : 284 -> 276
~ ___49-[WLSQLController insertAccount:migrator:device:]_block_invoke : 468 -> 484
~ -[WLSQLController accountsForMigrator:device:] : 348 -> 340
~ ___46-[WLSQLController accountsForMigrator:device:]_block_invoke : 620 -> 640
~ -[WLSQLController deleteAccountsAndSummariesForMigrator:device:] : 252 -> 240
~ ___64-[WLSQLController deleteAccountsAndSummariesForMigrator:device:]_block_invoke : 776 -> 800
~ -[WLSQLController insertRecordSummary:account:] : 252 -> 240
~ ___47-[WLSQLController insertRecordSummary:account:]_block_invoke : 968 -> 1004
~ ___104-[WLSQLController _totalSummarySegmentCountForAccounts:migrationStateComparisonOperator:migrationState:]_block_invoke : 752 -> 760
~ -[WLSQLController totalSummaryItemSizeForAccounts:addOverhead:completion:] : 292 -> 284
~ ___74-[WLSQLController totalSummaryItemSizeForAccounts:addOverhead:completion:]_block_invoke : 804 -> 816
~ -[WLSQLController setData:forSummary:] : 196 -> 188
~ -[WLSQLController dataForSummary:] : 272 -> 276
~ ___34-[WLSQLController dataForSummary:]_block_invoke : 420 -> 424
~ -[WLSQLController setDidDownloadForSummary:forSourceDevice:] : 152 -> 160
~ -[WLSQLController setWillImportForSummary:] : 152 -> 160
~ -[WLSQLController removeDataAndSetDidImportForSummary:] : 152 -> 160
~ -[WLSQLController setMigrationError:forSummary:] : 308 -> 312
~ -[WLSQLController migrationErrors] : 188 -> 208
~ ___34-[WLSQLController migrationErrors]_block_invoke : 624 -> 640
~ -[WLSQLController updateModifiedDateForSummary:] : 152 -> 160
~ ___48-[WLSQLController updateModifiedDateForSummary:]_block_invoke : 308 -> 312
~ -[WLSQLController summariesForAccount:] : 188 -> 196
~ -[WLSQLController summariesForAccounts:sortedByModifiedDate:] : 660 -> 656
~ ___61-[WLSQLController summariesForAccounts:sortedByModifiedDate:]_block_invoke : 1576 -> 1624
~ -[WLSQLController migrationMetadataForSourceDevice:strictMatch:] : 556 -> 600
~ ___64-[WLSQLController migrationMetadataForSourceDevice:strictMatch:]_block_invoke : 532 -> 544
~ -[WLSQLController insertMetadata:forSourceDevice:] : 200 -> 188
~ ___50-[WLSQLController insertMetadata:forSourceDevice:]_block_invoke : 456 -> 468
~ -[WLSQLController setMetadata:forSourceDevice:] : 196 -> 188
~ ___47-[WLSQLController setMetadata:forSourceDevice:]_block_invoke : 452 -> 464
~ -[WLSQLController insertMigratableApp:forDevice:] : 304 -> 300
~ ___49-[WLSQLController insertMigratableApp:forDevice:]_block_invoke : 380 -> 388
~ ___44-[WLSQLController _migratableAppsForDevice:]_block_invoke : 788 -> 808
~ -[WLSQLController insertMessagePhoneNumberWithIcc:ccAcNumber:] : 196 -> 188
~ -[WLSQLController messagePhoneNumberIccForCcAcNumber:] : 272 -> 276
~ ___54-[WLSQLController messagePhoneNumberIccForCcAcNumber:]_block_invoke : 404 -> 408
~ -[WLSQLController groupMessageInfoMatchingSourceThreadID:] : 272 -> 276
~ ___58-[WLSQLController groupMessageInfoMatchingSourceThreadID:]_block_invoke : 492 -> 504
~ -[WLSQLController groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:] : 428 -> 424
~ ___96-[WLSQLController groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:]_block_invoke : 556 -> 572
~ ___96-[WLSQLController groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:]_block_invoke_2 : 692 -> 716
~ -[WLSQLController _foundHandleIDs:representSameGroupMessageAsHandleIDs:handleIDsAreComplete:] : 124 -> 128
~ -[WLSQLController insertGroupMessageInfoWithSourceThreadID:roomName:groupID:] : 228 -> 220
~ -[WLSQLController insertGroupMessageInfoWithSortedHandleIDs:handleIDsAreComplete:roomName:groupID:] : 244 -> 228
~ ___99-[WLSQLController insertGroupMessageInfoWithSortedHandleIDs:handleIDsAreComplete:roomName:groupID:]_block_invoke : 440 -> 444
~ -[WLSQLController statisticsForContentType:] : 220 -> 232
~ ___44-[WLSQLController statisticsForContentType:]_block_invoke : 624 -> 632
~ -[WLSQLController updateStatistics:] : 152 -> 160
~ ___36-[WLSQLController updateStatistics:]_block_invoke : 572 -> 584
~ -[WLSQLController _insertStatistics_onDatabaseQueue:] : 572 -> 584
~ -[WLSQLController _openDatabase] : 260 -> 272
~ -[WLSQLController _ensureCorrectSchema] : 544 -> 548
~ ___33-[WLSQLController _schemaVersion]_block_invoke : 132 -> 136
~ -[WLSQLController _performQuery:rowHandler:] : 248 -> 240
~ ___44-[WLSQLController _performQuery:rowHandler:]_block_invoke : 552 -> 568
~ -[WLSQLController _sqlite3_column_NSDateForStatement:column:] : 76 -> 80
~ +[WLGroupMessageInfo groupMessageInfoWithSourceThreadID:sortedHandleIDs:handleIDsAreComplete:roomName:groupID:] : 224 -> 200
~ -[WLStatistics description] : 396 -> 432
~ -[WLStatistics fetchLogString] : 328 -> 356
~ -[WLStatistics setImportStartDate:] : 12 -> 64
~ -[WLStatistics setImportEndDate:] : 12 -> 64
~ -[NSString(WLSQLController) wl_sqlIDComponentsSeparatedByString:] : 360 -> 368
+ _OUTLINED_FUNCTION_0
~ -[WLNETRBClient _didStartDHCPWithSuccess:] : 640 -> 648
~ +[WLWiFiController sharedInstance] : 68 -> 84
~ -[WLWiFiController _initWithWiFiManager:netrbClient:] : 180 -> 172
~ -[WLWiFiController _newRequestID] : 68 -> 72
~ -[WLWiFiController enableSoftAPWithSSID:password:channel:completion:] : 520 -> 508
~ ___69-[WLWiFiController enableSoftAPWithSSID:password:channel:completion:]_block_invoke : 276 -> 268
~ ___70-[WLWiFiController _enableSoftAPWithSSID:password:channel:completion:]_block_invoke : 272 -> 268
~ -[WLWiFiController disableSoftAPWithCompletion:] : 212 -> 208
~ ___48-[WLWiFiController disableSoftAPWithCompletion:]_block_invoke : 204 -> 212
~ ___49-[WLWiFiController _disableSoftAPWithCompletion:]_block_invoke_2 : 140 -> 148
~ -[WLWiFiController _ensureStartedNetworkReflectsPreferences] : 276 -> 288
~ -[WLWiFiController _startedNetwork] : 240 -> 236
~ ___35-[WLWiFiController _startedNetwork]_block_invoke : 112 -> 124
~ -[WLWiFiController _startWiFiWithSSID:password:channel:completion:] : 348 -> 344
~ ___67-[WLWiFiController _startWiFiWithSSID:password:channel:completion:]_block_invoke : 332 -> 352
~ -[WLWiFiController _networkRecordFromSSID:password:channel:] : 460 -> 476
~ ___44-[WLWiFiController _stopWiFiWithCompletion:]_block_invoke : 204 -> 208
~ -[WLWiFiDeviceClient hostedNetworkMatchingSSID:] : 344 -> 356
~ -[WLWiFiDeviceClient startNetworkWithHostRole:request:completion:] : 352 -> 356
~ __startSessionToCompletionMap : 68 -> 84
~ -[WLWiFiDeviceClient _startNetworkWithRole:request:session:] : 120 -> 116
~ __WLWiFiDeviceClient_startNetworkCallback : 204 -> 212
~ -[WLWiFiDeviceClient stopNetwork:completion:] : 336 -> 340
~ __stopSessionToCompletionMap : 68 -> 84
~ -[WLWiFiDeviceClient _stopNetwork:session:] : 132 -> 128
~ __WLWiFiDeviceClient_stopNetworkCallbackRaw : 148 -> 152
~ __WLWiFiDeviceClient_stopNetworkCallback : 196 -> 212
~ -[WLWiFiDeviceClient _completionMapsAreEmpty] : 172 -> 188
~ -[WLWiFiManager scanNetwork:] : 608 -> 604
~ __WiFiDeviceClientScanAsyncCallback : 384 -> 400
~ -[WLWiFiManager currentNetwork:channels:completion:] : 436 -> 420
~ -[WLWiFiManager _preferredChannel:network:channels:completion:] : 1960 -> 1988
~ -[NSError(WelcomeKit) wl_encodableError] : 212 -> 228
~ +[NSError(WelcomeKit) wl_encodableErrorSupportedClasses] : 68 -> 84
~ ___56+[NSError(WelcomeKit) wl_encodableErrorSupportedClasses]_block_invoke : 276 -> 280
~ +[NSError(WelcomeKit) _wl_encodableObjectFromObject:] : 292 -> 312
~ +[NSError(WelcomeKit) _wl_encodableArrayFromArray:] : 348 -> 352
~ +[NSError(WelcomeKit) _wl_encodableSetFromSet:] : 348 -> 352
~ ___61+[NSError(WelcomeKit) _wl_encodableDictionaryFromDictionary:]_block_invoke : 164 -> 168
~ ___65+[NSError(WelcomeKit) _wl_objectIsKindOfNonCollectionPlistClass:]_block_invoke : 192 -> 196
~ ___49-[WLSQLController insertAccount:migrator:device:]_block_invoke.cold.1 : 44 -> 40
~ ___46-[WLSQLController accountsForMigrator:device:]_block_invoke.cold.1 : 44 -> 40
~ ___64-[WLSQLController deleteAccountsAndSummariesForMigrator:device:]_block_invoke.cold.1 : 44 -> 40
~ ___64-[WLSQLController deleteAccountsAndSummariesForMigrator:device:]_block_invoke.cold.2 : 44 -> 40
~ ___64-[WLSQLController migrationMetadataForSourceDevice:strictMatch:]_block_invoke.cold.1 : 44 -> 40
~ ___50-[WLSQLController insertMetadata:forSourceDevice:]_block_invoke.cold.1 : 44 -> 40
~ ___47-[WLSQLController setMetadata:forSourceDevice:]_block_invoke.cold.1 : 44 -> 40
~ ___49-[WLSQLController insertMigratableApp:forDevice:]_block_invoke.cold.1 : 44 -> 40
~ ___44-[WLSQLController _migratableAppsForDevice:]_block_invoke.cold.1 : 44 -> 40

```

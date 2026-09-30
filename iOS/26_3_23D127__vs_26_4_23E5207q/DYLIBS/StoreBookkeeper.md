## StoreBookkeeper

> `/System/Library/PrivateFrameworks/StoreBookkeeper.framework/StoreBookkeeper`

```diff

-4025.100.105.0.0
-  __TEXT.__text: 0x1e240
-  __TEXT.__auth_stubs: 0x7f0
+4025.500.37.0.0
+  __TEXT.__text: 0x1f86c
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x25ac
   __TEXT.__cstring: 0x2425
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x444
+  __TEXT.__gcc_except_tab: 0x430
   __TEXT.__oslogstring: 0x11da
-  __TEXT.__unwind_info: 0x928
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__objc_classname: 0x45b
   __TEXT.__objc_methname: 0x6cf9
   __TEXT.__objc_methtype: 0xe58

   __DATA_CONST.__objc_selrefs: 0x1718
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x1d20
   __AUTH_CONST.__objc_const: 0x3fc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8F3315BE-4A61-3FDB-A5C8-DC5F92CF1F1D
+  UUID: B825B725-7AA0-3DBB-839F-C31E57C9948F
   Functions: 874
-  Symbols:   3162
+  Symbols:   3156
   CStrings:  1881
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
Functions:
~ +[SBKPullValueRequest requestForTransaction:] : 180 -> 196
~ +[SBKPullValueRequest propertyListBodyWithTransaction:] : 276 -> 292
~ -[SBKPullValueRequest canonicalResponseForResponse:] : 120 -> 128
~ -[NSData(SBKAdditions) _SBKDataByDeflatingWithNoZipHeaderWithCompression:] : 676 -> 680
~ -[NSData(SBKAdditions) _SBKDataByInflatingWithNoZipHeader] : 408 -> 412
~ +[NSData(SBKAdditions) SBKStringByMD5HashingString:] : 4556 -> 4576
~ +[NSData(SBKAdditions) SBKStringFromDigestData:] : 232 -> 236
~ -[SBKStoreClampsController setPendingUserDefaultArchivedData:] : 12 -> 64
~ -[SBKStoreClampsController setTransactionClamps:] : 12 -> 64
~ -[SBKStoreClampsController setQueue:] : 12 -> 64
~ -[SBKStoreClampsController _canScheduleTransactionBasedOnUserCancelledSignIn:error:] : 416 -> 424
~ -[SBKStoreClampsController _canScheduleTransactionBasedOnBackOff:error:] : 416 -> 424
~ -[SBKStoreClampsController _canScheduleTransactionBasedOnAccountIdentifierCheck:error:] : 280 -> 284
~ -[SBKStoreClampsController _canScheduleTransactionBasedOfNetworkingBlocked:error:] : 308 -> 316
~ -[SBKStoreClampsController _canScheduleTransactionBasedOnType:error:] : 576 -> 580
~ ___69-[SBKStoreClampsController _canScheduleTransactionBasedOnType:error:]_block_invoke : 144 -> 152
~ -[SBKStoreClampsController _rightNow] : 72 -> 76
~ -[SBKStoreClampsController setUserCancelledSignIn] : 360 -> 364
~ -[SBKStoreClampsController hasAuthenticatedTooRecentlyForTransaction:error:] : 328 -> 332
~ ___57-[SBKStoreClampsController clearTimestampForTransaction:]_block_invoke : 116 -> 120
~ ___55-[SBKStoreClampsController setTimestampForTransaction:]_block_invoke : 140 -> 148
~ -[SBKStoreClampsController accessTransactionClampsWithBlock:] : 152 -> 160
~ ___61-[SBKStoreClampsController accessTransactionClampsWithBlock:]_block_invoke : 184 -> 196
~ ___46-[SBKStoreClampsController saveToUserDefaults]_block_invoke : 392 -> 404
~ ___46-[SBKStoreClampsController saveToUserDefaults]_block_invoke.49 : 272 -> 276
~ ___46-[SBKStoreClampsController saveToUserDefaults]_block_invoke.50 : 88 -> 92
~ -[SBKStoreClampsController initWithCoder:] : 360 -> 372
~ ___42-[SBKStoreClampsController initWithCoder:]_block_invoke : 84 -> 92
~ -[SBKStoreClampsController encodeWithCoder:] : 332 -> 328
~ -[SBKStoreClampsController description] : 348 -> 384
~ +[SBKStoreClampsController sharedClampsController] : 84 -> 100
~ ___50+[SBKStoreClampsController sharedClampsController]_block_invoke : 460 -> 476
~ -[SBKGenericKeyValuePair kvsValueDescription] : 152 -> 160
~ -[SBKGenericKeyValuePair encodeWithCoder:] : 108 -> 116
~ -[SBKGenericKeyValuePair initWithCoder:] : 188 -> 196
~ -[SBKGenericKeyValuePair initWithKVSKey:kvsPayload:] : 152 -> 144
~ +[SBKGenericKeyValuePair pairWithKVSKey:kvsPayload:] : 112 -> 108
~ _SBKKeyValuePayloadPairWithPreferredClass : 164 -> 156
~ -[SBKTransactionController setBackgroundTaskAssertion:] : 12 -> 64
~ -[SBKTransactionController setPendingTransactions:] : 12 -> 64
~ -[SBKTransactionController setOperationQueue:] : 12 -> 64
~ -[SBKTransactionController setQueue:] : 12 -> 64
~ -[SBKTransactionController setCurrentTransaction:] : 12 -> 64
~ -[SBKTransactionController setAuthenticationController:] : 12 -> 64
~ -[SBKTransactionController operation:failedWithError:] : 580 -> 596
~ ___54-[SBKTransactionController operation:failedWithError:]_block_invoke : 288 -> 296
~ ___57-[SBKTransactionController operation:didReceiveResponse:]_block_invoke : 136 -> 144
~ -[SBKTransactionController operation:finishedWithOutput:] : 200 -> 188
~ -[SBKTransactionController _delegateTransactionDidFinish:] : 200 -> 196
~ ___58-[SBKTransactionController _delegateTransactionDidFinish:]_block_invoke : 176 -> 180
~ -[SBKTransactionController _delegateTransactionDidCancel:withError:] : 236 -> 232
~ ___68-[SBKTransactionController _delegateTransactionDidCancel:withError:]_block_invoke : 172 -> 176
~ -[SBKTransactionController _delegateTransactionDidFail:withError:] : 332 -> 336
~ -[SBKTransactionController _delegateShouldScheduleTransaction:error:] : 168 -> 172
~ -[SBKTransactionController _onQueue_performDefaultErrorHandlingForError:] : 160 -> 164
~ -[SBKTransactionController _onQueue_performCancelErrorHandlingForError:] : 128 -> 140
~ -[SBKTransactionController _onQueue_performRetryErrorHandlingForError:] : 228 -> 244
~ -[SBKTransactionController _onQueue_resolveError:resolution:] : 220 -> 236
~ -[SBKTransactionController _onQueue_processOperationOutput:operation:operationAuthenticated:] : 1396 -> 1468
~ ___51-[SBKTransactionController _processDataInResponse:]_block_invoke_2 : 212 -> 216
~ -[SBKTransactionController _onQueue_transactionDidCancel:withError:] : 224 -> 212
~ -[SBKTransactionController _onQueue_transactionDidFail:withError:] : 224 -> 212
~ -[SBKTransactionController _onQueue_authenticationCanProcessTransaction:error:] : 152 -> 156
~ -[SBKTransactionController _onQueue_clampsCanScheduleTransaction:error:] : 112 -> 116
~ -[SBKTransactionController _onQueue_assertIsTransactionValid:error:] : 276 -> 300
~ -[SBKTransactionController _onQueue_isEnabledForTransaction:error:] : 112 -> 116
~ -[SBKTransactionController _onQueue_addPendingTransaction:] : 112 -> 116
~ -[SBKTransactionController _onQueue_scheduleTransaction:isRetry:] : 576 -> 572
~ ___65-[SBKTransactionController _onQueue_scheduleTransaction:isRetry:]_block_invoke : 156 -> 160
~ -[SBKTransactionController _onQueue_processPendingTransactions] : 392 -> 396
~ -[SBKTransactionController _onQueue_cancelAllPendingTransactions:] : 396 -> 400
~ -[SBKTransactionController _onQueue_endBackgroundTask] : 172 -> 168
~ ___56-[SBKTransactionController _onQueue_beginBackgroundTask]_block_invoke_2 : 112 -> 116
~ -[SBKTransactionController _storeOperationDidComplete:] : 104 -> 116
~ ___60-[SBKTransactionController cancelAllTransactionsCancelCode:]_block_invoke : 164 -> 172
~ ___49-[SBKTransactionController cancelAllTransactions]_block_invoke : 164 -> 172
~ -[SBKTransactionController cancelScheduledTransaction:] : 152 -> 160
~ ___55-[SBKTransactionController cancelScheduledTransaction:]_block_invoke : 104 -> 108
~ -[SBKTransactionController scheduleTransaction:] : 264 -> 272
~ -[SBKTransactionController scheduleTransaction:withTransactionFinishedBlock:] : 120 -> 124
~ ___60-[SBKTransactionController _networkTypeChangedNotification:]_block_invoke : 68 -> 72
~ ___39-[SBKTransactionController setEnabled:]_block_invoke : 148 -> 152
~ -[SBKTransactionController setRequestURL:] : 180 -> 168
~ ___42-[SBKTransactionController setRequestURL:]_block_invoke : 68 -> 72
~ ___38-[SBKTransactionController setDomain:]_block_invoke : 68 -> 72
~ -[SBKTransactionController dealloc] : 404 -> 416
~ -[SBKTransactionController initWithDomain:requestURL:forAccount:] : 432 -> 440
~ -[SBKSyncResponseData setResponseOpEntiesByKey:] : 12 -> 64
~ -[SBKSyncResponseData _deserializeResponseDictionary:response:] : 676 -> 672
~ ___63-[SBKSyncResponseData _deserializeResponseDictionary:response:]_block_invoke : 792 -> 804
~ ___63-[SBKSyncResponseData _deserializeResponseDictionary:response:]_block_invoke_5 : 304 -> 308
~ -[SBKSyncResponseData payloadDataForUpdateResponseKey:] : 120 -> 132
~ -[SBKSyncResponseData description] : 436 -> 476
~ _shortArrayDescription : 240 -> 236
~ ___shortArrayDescription_block_invoke : 152 -> 156
~ -[SBKSyncResponseData initWithTransaction:responseDictionary:response:] : 324 -> 340
~ +[SBKSyncResponseData deserializedResponseBodyWithTransaction:responseDictionary:response:] : 136 -> 128
~ -[SBKStoreError setTransaction:] : 20 -> 80
~ -[SBKStoreError retrySeconds] : 92 -> 100
~ -[SBKStoreError currentStoreAccountName] : 84 -> 92
~ -[SBKStoreError previousStoreAccountName] : 84 -> 92
~ -[SBKStoreError copyWithZone:] : 108 -> 112
~ -[SBKStoreError description] : 148 -> 160
~ +[SBKStoreError(SBKPrivate) serverClampErrorWithTransaction:retrySeconds:underlyingError:] : 360 -> 380
~ +[SBKStoreError(SBKPrivate) userClampErrorWithTransaction:retrySeconds:underlyingError:] : 360 -> 380
~ +[SBKStoreError(SBKPrivate) transactionCancelledErrorWithTransaction:code:underlyingError:] : 156 -> 160
~ _NSStringFromErrorCode : 1188 -> 1296
~ +[SBKStoreError(SBKPrivate) transactionMissingURLErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) transactionMissingDomainErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) storeAccountSessionExpiredWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) noStoreAccountErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) userEnteredWrongCredentialsErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) userCancelledSignInErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) storeValidationErrorWithTransaction:underlyingError:] : 224 -> 240
~ +[SBKStoreError(SBKPrivate) storeGenericErrorWithTransaction:underlyingError:] : 224 -> 240
~ +[SBKStoreError(SBKPrivate) storeAccountMismatchErrorWithPreviousStoreAccountName:currentStoreAccountName:transaction:underlyingError:] : 360 -> 368
~ +[SBKStoreError(SBKPrivate) storeLoggedOutErrorWithPreviousStoreAccountName:transaction:underlyingError:] : 316 -> 328
~ +[SBKStoreError(SBKPrivate) killSwitchErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) networkingBlockedErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) keyValueStoreDisabledErrorWithTransaction:underlyingError:] : 144 -> 148
~ +[SBKStoreError(SBKPrivate) unknownErrorWithTransaction:underlyingError:] : 280 -> 296
~ +[SBKStoreError(SBKPrivate) keyValueStoreErrorWithCode:localizedDescription:transaction:underlyingError:] : 220 -> 228
~ -[SBKTransactionURLOperation setSBKRequest:] : 20 -> 80
~ -[SBKTransactionURLOperation description] : 160 -> 172
~ -[SBKTransactionURLOperation setShouldAuthenticate:] : 316 -> 328
~ -[SBKTransactionURLOperation init] : 108 -> 112
~ -[SBKSyncRequestData _serializableDeleteItemPayloadDictionaryForKey:] : 252 -> 260
~ -[SBKSyncRequestData _serializableUpdateItemPayloadDictionaryForKey:] : 384 -> 404
~ -[SBKSyncRequestData _needsConflictDetection] : 60 -> 64
~ -[SBKSyncRequestData _serializableConflictDetectionOrdinalForKey:] : 192 -> 204
~ -[SBKSyncRequestData _serializableConflictDetectionValue] : 356 -> 368
~ -[SBKSyncRequestData serializableRequestBodyPropertyList] : 1028 -> 1088
~ -[SBKStoreAuthenticationController saveAccountToLastFailedSyncDefaults] : 228 -> 252
~ -[SBKStoreAuthenticationController saveAccountToLastSyncedDefaults] : 228 -> 252
~ -[SBKStoreAuthenticationController authenticationErrorsForTransaction:] : 644 -> 680
~ -[SBKStoreAuthenticationController shouldForceAuthenticationForTransaction:] : 132 -> 136
~ -[SBKStoreAuthenticationController isAuthenticationValidForTransaction:error:] : 380 -> 396
~ -[SBKStoreAuthenticationController initWithStoreAccount:] : 116 -> 108
~ +[SBKStoreAuthenticationController lastFailedSyncAccountName] : 96 -> 104
~ +[SBKStoreAuthenticationController lastFailedSyncAccountIdentifier] : 140 -> 152
~ +[SBKStoreAuthenticationController lastSyncedAccountName] : 96 -> 104
~ +[SBKStoreAuthenticationController lastSyncedAccountIdentifier] : 140 -> 152
~ +[SBKStoreAuthenticationController clearLastSyncnedAccount] : 128 -> 136
~ -[SBKPushValueTransaction _resolveConflictBetweenClientPayloadPair:andServerPayloadPair:] : 108 -> 120
~ -[SBKPushValueTransaction processDataInResponse:withCompletionHandler:] : 504 -> 548
~ -[SBKPushValueTransaction newRequest] : 40 -> 44
~ -[SBKPushValueTransaction clampsKey] : 152 -> 164
~ -[SBKPushValueTransaction description] : 380 -> 404
~ -[SBKPushValueTransaction initWithStoreBagContext:clientItemPayloadPair:clientItemVersionAnchor:] : 292 -> 300
~ -[SBKPreferences setBool:forKey:] : 140 -> 144
~ -[SBKPreferences registerDefaultsIfKeyNotSet:registrationBlock:] : 168 -> 172
~ -[SBKPreferences _preferencesDidChange] : 100 -> 104
~ +[SBKPreferences storeBookkeeperPreferences] : 84 -> 100
~ -[SBKSimpleTransactionRequestHandler cancelWithError:] : 140 -> 152
~ -[SBKSimpleTransactionRequestHandler timeout] : 172 -> 180
~ -[SBKSimpleTransactionRequestHandler initWithBagContext:] : 200 -> 208
~ -[SBKUniversalPlaybackPositionMetadata keyValueStorePayload] : 516 -> 540
~ -[SBKUniversalPlaybackPositionMetadata isEqual:] : 192 -> 180
~ -[SBKUniversalPlaybackPositionMetadata hash] : 144 -> 152
~ -[SBKUniversalPlaybackPositionMetadata timestamp] : 40 -> 44
~ -[SBKUniversalPlaybackPositionMetadata setTimestamp:] : 40 -> 44
~ -[SBKUniversalPlaybackPositionMetadata copyWithZone:] : 164 -> 168
~ -[SBKUniversalPlaybackPositionMetadata description] : 648 -> 676
~ -[SBKUniversalPlaybackPositionMetadata encodeWithCoder:] : 168 -> 176
~ -[SBKUniversalPlaybackPositionMetadata initWithCoder:] : 220 -> 224
~ +[SBKUniversalPlaybackPositionMetadata metadataWithItemIdentifier:keyValueStorePayload:failuresOkay:] : 1932 -> 2016
~ +[SBKUniversalPlaybackPositionMetadata metadataWithValuesFromDataSourceItem:] : 680 -> 724
~ +[SBKUniversalPlaybackPositionMetadata keyValueStoreItemIdentifierForUniqueStoreID:itemTitle:albumName:itemArtistName:feedURL:feedGUID:] : 732 -> 764
~ _storageItemIdentifierForProperties : 568 -> 584
~ +[SBKUniversalPlaybackPositionMetadata keyValueStoreItemIdentifierForItem:] : 964 -> 1072
~ -[SBKUniversalPlaybackPositionStore setTimer:] : 12 -> 64
~ -[SBKUniversalPlaybackPositionStore setDateToFireNextTimer:] : 12 -> 64
~ -[SBKUniversalPlaybackPositionStore setCurrentTaskRequestHandler:] : 12 -> 64
~ -[SBKUniversalPlaybackPositionStore setBagLookupTask:] : 12 -> 64
~ -[SBKUniversalPlaybackPositionStore setLookupDomainVersionTask:] : 12 -> 64
~ -[SBKUniversalPlaybackPositionStore setCurrentTask:] : 12 -> 64
~ -[SBKUniversalPlaybackPositionStore _onQueueStartNewTimerWithTimeIntervalSinceNow:] : 196 -> 204
~ -[SBKUniversalPlaybackPositionStore _onQueueStopTimer] : 88 -> 92
~ -[SBKUniversalPlaybackPositionStore _onQueueScheduleTimer] : 184 -> 188
~ ___58-[SBKUniversalPlaybackPositionStore _onQueueScheduleTimer]_block_invoke : 592 -> 612
~ -[SBKUniversalPlaybackPositionStore _timerIsStopped] : 96 -> 104
~ -[SBKUniversalPlaybackPositionStore _effectiveAutorefreshRate] : 232 -> 244
~ -[SBKUniversalPlaybackPositionStore _updateForStoreAccountsChange] : 200 -> 208
~ -[SBKUniversalPlaybackPositionStore _onQueueLoadBagContextWithCompletionHandler:] : 1204 -> 1208
~ ___81-[SBKUniversalPlaybackPositionStore _onQueueLoadBagContextWithCompletionHandler:]_block_invoke : 240 -> 248
~ ___81-[SBKUniversalPlaybackPositionStore _onQueueLoadBagContextWithCompletionHandler:]_block_invoke_2 : 408 -> 420
~ ___81-[SBKUniversalPlaybackPositionStore _onQueueLoadBagContextWithCompletionHandler:]_block_invoke.131 : 216 -> 204
~ ___81-[SBKUniversalPlaybackPositionStore _onQueueLoadBagContextWithCompletionHandler:]_block_invoke.124 : 128 -> 124
~ _ErrorInfoWithUnderlyingError.924 : 148 -> 152
~ -[SBKUniversalPlaybackPositionStore _accountForSyncing] : 92 -> 100
~ -[SBKUniversalPlaybackPositionStore _onQueuePullMetadataItemWithItemIdentifier:completionBlock:] : 408 -> 400
~ ___96-[SBKUniversalPlaybackPositionStore _onQueuePullMetadataItemWithItemIdentifier:completionBlock:]_block_invoke : 308 -> 336
~ ___96-[SBKUniversalPlaybackPositionStore _onQueuePullMetadataItemWithItemIdentifier:completionBlock:]_block_invoke_2 : 388 -> 368
~ -[SBKUniversalPlaybackPositionStore _onQueuePushMetadataItem:completionBlock:] : 408 -> 400
~ ___78-[SBKUniversalPlaybackPositionStore _onQueuePushMetadataItem:completionBlock:]_block_invoke : 308 -> 336
~ ___78-[SBKUniversalPlaybackPositionStore _onQueuePushMetadataItem:completionBlock:]_block_invoke_2 : 384 -> 364
~ -[SBKUniversalPlaybackPositionStore _onQueueSynchronizeImmediatelyWithCompletionHandler:] : 268 -> 264
~ ___89-[SBKUniversalPlaybackPositionStore _onQueueSynchronizeImmediatelyWithCompletionHandler:]_block_invoke : 360 -> 348
~ -[SBKUniversalPlaybackPositionStore _onQueueRunTaskWithName:taskCompletionHandler:runTaskBlock:] : 1184 -> 1176
~ ___96-[SBKUniversalPlaybackPositionStore _onQueueRunTaskWithName:taskCompletionHandler:runTaskBlock:]_block_invoke_2.94 : 512 -> 532
~ ___96-[SBKUniversalPlaybackPositionStore _onQueueRunTaskWithName:taskCompletionHandler:runTaskBlock:]_block_invoke_3 : 424 -> 452
~ ___96-[SBKUniversalPlaybackPositionStore _onQueueRunTaskWithName:taskCompletionHandler:runTaskBlock:]_block_invoke_4 : 164 -> 172
~ ___96-[SBKUniversalPlaybackPositionStore _onQueueRunTaskWithName:taskCompletionHandler:runTaskBlock:]_block_invoke_5 : 108 -> 112
~ -[SBKUniversalPlaybackPositionStore _onQueueRunNextPendingTaskBlock] : 108 -> 112
~ -[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:] : 628 -> 624
~ ___88-[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:]_block_invoke_2 : 396 -> 408
~ ___88-[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:]_block_invoke_2.83 : 204 -> 192
~ ___88-[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:]_block_invoke_3 : 300 -> 304
~ ___88-[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:]_block_invoke.86 : 184 -> 180
~ ___88-[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:]_block_invoke_2.87 : 96 -> 100
~ ___88-[SBKUniversalPlaybackPositionStore _onQueueLoadRemoteDomainVersionWithCompletionBlock:]_block_invoke.79 : 128 -> 124
~ ___71-[SBKUniversalPlaybackPositionStore loadBagContextWithCompletionBlock:]_block_invoke : 144 -> 140
~ ___71-[SBKUniversalPlaybackPositionStore loadBagContextWithCompletionBlock:]_block_invoke_2 : 164 -> 168
~ ___77-[SBKUniversalPlaybackPositionStore checkForAvailabilityWithCompletionBlock:]_block_invoke : 144 -> 152
~ ___77-[SBKUniversalPlaybackPositionStore checkForAvailabilityWithCompletionBlock:]_block_invoke_2 : 180 -> 184
~ -[SBKUniversalPlaybackPositionStore pullMetadataItemWithItemIdentifier:completionBlock:] : 196 -> 188
~ -[SBKUniversalPlaybackPositionStore pushMetadataItem:completionBlock:] : 196 -> 188
~ -[SBKUniversalPlaybackPositionStore synchronizeImmediatelyWithCompletionHandler:] : 152 -> 160
~ -[SBKUniversalPlaybackPositionStore dealloc] : 240 -> 264
~ -[SBKUniversalPlaybackPositionStore initWithDomain:dataSource:automaticSynchronizeOptions:accountIdentifier:isActive:] : 828 -> 856
~ -[SBKUniversalPlaybackPositionStore initWithDomain:dataSource:automaticSynchronizeOptions:isActive:] : 160 -> 164
~ -[SBKPlaybackPositionSyncRequestHandler setOverrideSyncAnchor:] : 20 -> 80
~ -[SBKPlaybackPositionSyncRequestHandler setFatalSyncError:] : 20 -> 80
~ -[SBKPlaybackPositionSyncRequestHandler setKvsController:] : 20 -> 80
~ -[SBKPlaybackPositionSyncRequestHandler setDataSource:] : 20 -> 80
~ -[SBKPlaybackPositionSyncRequestHandler transaction:conflictDetectionOrdinalForKey:] : 144 -> 156
~ -[SBKPlaybackPositionSyncRequestHandler transaction:syncAnchorForTransactionSyncAnchor:] : 92 -> 88
~ -[SBKPlaybackPositionSyncRequestHandler transaction:keyValuePairForUpdatedKey:] : 108 -> 116
~ -[SBKPlaybackPositionSyncRequestHandler transaction:processUpdatedKey:data:conflict:isDirty:] : 300 -> 304
~ -[SBKPlaybackPositionSyncRequestHandler transactionController:transactionDidFail:error:] : 356 -> 372
~ -[SBKPlaybackPositionSyncRequestHandler _signalKVSTransactionCompletion:withError:] : 308 -> 312
~ -[SBKPlaybackPositionSyncRequestHandler _signalKVSTransactionCompletion:] : 88 -> 92
~ -[SBKPlaybackPositionSyncRequestHandler _synchronouslyRunKVSTransaction:] : 276 -> 300
~ -[SBKPlaybackPositionSyncRequestHandler newKVSSyncTransactionWithUpdatedMetadataItemIdentifiers:processConflicts:] : 252 -> 264
~ -[SBKPlaybackPositionSyncRequestHandler _mergeMetadataItemsFromSyncResponse] : 408 -> 416
~ ___74-[SBKPlaybackPositionSyncRequestHandler synchronizeWithCompletionHandler:]_block_invoke_2 : 108 -> 104
~ -[SBKPlaybackPositionSyncRequestHandler timeout] : 120 -> 128
~ -[SBKPlaybackPositionSyncRequestHandler cancelWithError:] : 296 -> 324
~ ___52-[SBKPlaybackPositionSyncRequestHandler _shouldStop]_block_invoke : 120 -> 124
~ -[SBKPlaybackPositionSyncRequestHandler _synchronize:] : 2276 -> 2408
~ ___54-[SBKPlaybackPositionSyncRequestHandler _synchronize:]_block_invoke.22 : 336 -> 348
~ -[SBKPlaybackPositionSyncRequestHandler _dataSourceCancelTransaction] : 128 -> 136
~ -[SBKPlaybackPositionSyncRequestHandler clearTransactionResponseData] : 232 -> 240
~ -[SBKPlaybackPositionSyncRequestHandler initWithDataSource:bagContext:accountIdentifier:] : 928 -> 984
~ -[SBKPlaybackPositionSyncRequestHandler initWithDataSource:bagContext:] : 136 -> 140
~ -[SBKPlaybackPositionSyncRequestHandler metadataItemsToCommitToKVSStorage] : 104 -> 100
~ -[SBKPlaybackPositionSyncRequestHandler metadataItemsToCommitToDataSource] : 104 -> 100
~ -[SBKPlaybackPositionSyncRequestHandler currentKVSTransaction] : 104 -> 100
~ -[SBKPlaybackPositionSyncRequestHandler dataSourceTransactionContext] : 104 -> 100
~ -[SBKStoreURLBagContext setBag:] : 12 -> 64
~ -[SBKStoreURLBagContext setPullAllKeyValueRequestURL:] : 12 -> 64
~ -[SBKStoreURLBagContext setPushAllKeyValueRequestURL:] : 12 -> 64
~ -[SBKStoreURLBagContext setPullKeyValueRequestURL:] : 12 -> 64
~ -[SBKStoreURLBagContext setPushKeyValueRequestURL:] : 12 -> 64
~ -[SBKStoreURLBagContext setSyncRequestURL:] : 12 -> 64
~ -[SBKStoreURLBagContext mutableCopyWithZone:] : 260 -> 256
~ ___45-[SBKStoreURLBagContext mutableCopyWithZone:]_block_invoke : 116 -> 120
~ +[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:] : 1024 -> 984
~ ___73+[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:]_block_invoke : 252 -> 236
~ ___73+[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:]_block_invoke_3 : 468 -> 460
~ ___73+[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:]_block_invoke_7 : 156 -> 160
~ ___73+[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:]_block_invoke_6 : 160 -> 164
~ ___73+[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:]_block_invoke_5 : 148 -> 152
~ ___73+[SBKStoreURLBagContext loadBagContextFromURLBag:domain:completionBlock:]_block_invoke_2 : 104 -> 116
~ +[SBKStoreURLBagContext _findFirstValueInBag:keyEnumerator:valueTransformer:defaultValue:completionBlock:] : 360 -> 344
~ -[SBKStoreURLBagContext copyWithZone:] : 252 -> 248
~ ___38-[SBKStoreURLBagContext copyWithZone:]_block_invoke : 116 -> 120
~ -[SBKStoreURLBagContext initWithBag:domain:] : 116 -> 108
~ -[SBKStoreURLBagContext description] : 296 -> 304
~ ___36-[SBKStoreURLBagContext description]_block_invoke : 176 -> 180
~ -[SBKStoreURLBagContext init] : 108 -> 112
~ -[SBKStoreURLBagContext _initWithDomain:syncRequestURL:domainDisabled:] : 160 -> 152
~ _SBKLogProductionKeyBag : 172 -> 180
~ ___SBKLogProductionKeyBag_block_invoke : 100 -> 116
~ -[SBKPullValueTransaction processDataInResponse:withCompletionHandler:] : 412 -> 444
~ -[SBKPullValueTransaction newRequest] : 40 -> 44
~ -[SBKPullValueTransaction clampsKey] : 136 -> 144
~ -[SBKPullValueTransaction description] : 328 -> 348
~ +[SBKPushValueResponse responseWithResponse:transaction:] : 104 -> 108
~ -[SBKPushValueResponse deserializeResponseBodyWithTransaction:] : 324 -> 364
~ -[SBKRequestData setTransaction:] : 12 -> 64
~ -[SBKRequestData serializableRequestBodyPropertyList] : 104 -> 108
~ -[SBKRequestData initWithTransaction:] : 116 -> 108
~ +[SBKRequestData propertyListBodyWithTransaction:] : 104 -> 108
~ +[SBKSyncResponse responseWithResponse:transaction:] : 104 -> 108
~ -[SBKSyncResponse deserializeResponseBodyWithTransaction:] : 148 -> 156
~ -[SBKSyncTransaction processDataInResponse:withCompletionHandler:] : 484 -> 476
~ -[SBKSyncResponseDataKeyEnumerator setDeletedKeysEnumerator:] : 12 -> 64
~ -[SBKSyncResponseDataKeyEnumerator setConflictedKeysEnumerator:] : 12 -> 64
~ -[SBKSyncResponseDataKeyEnumerator setUpdatedKeysEnumerator:] : 12 -> 64
~ -[SBKSyncResponseDataKeyEnumerator setTransaction:] : 12 -> 64
~ -[SBKSyncResponseDataKeyEnumerator setResponseData:] : 12 -> 64
~ -[SBKSyncResponseDataKeyEnumerator _processNextKey] : 236 -> 248
~ -[SBKSyncResponseDataKeyEnumerator _processDeletedKey:isDirty:] : 120 -> 124
~ -[SBKSyncResponseDataKeyEnumerator _processUpdatedKey:isConflict:isDirty:] : 164 -> 176
~ -[SBKSyncResponseDataKeyEnumerator enumerateKeysInResponseForTransaction:completionBlock:] : 248 -> 272
~ -[SBKSyncResponseDataKeyEnumerator initWithResponseData:] : 116 -> 108
~ -[SBKSyncTransaction keysToDelete] : 132 -> 148
~ -[SBKSyncTransaction keysToUpdate] : 132 -> 148
~ -[SBKSyncTransaction syncAnchor] : 132 -> 148
~ -[SBKSyncTransaction keyValuePairForUpdatedKey:] : 116 -> 120
~ -[SBKSyncTransaction conflictDetectionOrdinalForKey:] : 208 -> 216
~ -[SBKSyncTransaction description] : 392 -> 416
~ -[SBKSyncTransaction setTransactionProcessor:] : 100 -> 104
~ -[SBKSyncTransaction _validateTransactionProcessor:] : 580 -> 612
~ -[SBKSyncTransaction newRequest] : 40 -> 44
~ -[SBKSyncTransaction requestURL] : 16 -> 64
~ -[SBKSyncTransaction domain] : 16 -> 64
~ -[SBKSyncTransaction clampsKey] : 188 -> 204
~ -[SBKAsynchronousTask setCompletions:] : 12 -> 64
~ -[SBKAsynchronousTask setTaskAssertion:] : 12 -> 64
~ ___59-[SBKAsynchronousTask invokeTaskCompletionBlocksWithBlock:]_block_invoke_2 : 296 -> 272
~ -[SBKAsynchronousTask addTaskCompletionBlock:] : 172 -> 180
~ ___44-[SBKAsynchronousTask _invalidateAssertion:]_block_invoke : 124 -> 144
~ -[SBKAsynchronousTask finishTaskOperationWithResult:error:] : 236 -> 224
~ ___59-[SBKAsynchronousTask finishTaskOperationWithResult:error:]_block_invoke : 260 -> 264
~ -[SBKAsynchronousTask beginTaskOperation] : 376 -> 388
~ -[SBKAsynchronousTask error] : 240 -> 236
~ ___28-[SBKAsynchronousTask error]_block_invoke : 20 -> 68
~ -[SBKAsynchronousTask setError:] : 152 -> 160
~ ___32-[SBKAsynchronousTask setError:]_block_invoke : 24 -> 84
~ -[SBKAsynchronousTask result] : 240 -> 236
~ ___29-[SBKAsynchronousTask result]_block_invoke : 20 -> 68
~ -[SBKAsynchronousTask setResult:] : 152 -> 160
~ ___33-[SBKAsynchronousTask setResult:]_block_invoke : 24 -> 84
~ -[SBKAsynchronousTask setFinishedHandler:] : 152 -> 160
~ -[SBKAsynchronousTask setExpirationHandler:] : 152 -> 160
~ -[SBKAsynchronousTask description] : 164 -> 176
~ -[SBKAsynchronousTask debugDescription] : 8 -> 56
~ -[SBKAsynchronousTask initWithHandlerQueue:timeout:debugDescription:] : 412 -> 416
~ -[SBKLoadDomainVersionRequestHandler setTransaction:] : 20 -> 80
~ -[SBKLoadDomainVersionRequestHandler runWithCompletionHandler:] : 208 -> 204
~ ___63-[SBKLoadDomainVersionRequestHandler runWithCompletionHandler:]_block_invoke : 496 -> 508
~ -[SBKSyncRequestHandler transaction:keyValuePairForUpdatedKey:] : 104 -> 108
~ -[SBKSyncRequestHandler transaction:processUpdatedKey:data:conflict:isDirty:] : 232 -> 220
~ -[SBKSyncRequestHandler transaction:willProcessResponseData:] : 160 -> 168
~ ___61-[SBKSyncRequestHandler transaction:willProcessResponseData:]_block_invoke : 228 -> 240
~ -[SBKSyncRequestHandler startTransactionWithSyncAnchor:keysToUpdate:keysToDelete:finishedBlock:] : 284 -> 264
~ ___96-[SBKSyncRequestHandler startTransactionWithSyncAnchor:keysToUpdate:keysToDelete:finishedBlock:]_block_invoke : 284 -> 288
~ -[SBKSyncRequestHandler responseDataForResponseKey:] : 372 -> 364
~ ____serialGetValue_block_invoke : 84 -> 88
~ -[SBKSyncRequestHandler responseConflictedKeys] : 332 -> 328
~ ___47-[SBKSyncRequestHandler responseConflictedKeys]_block_invoke : 20 -> 68
~ -[SBKSyncRequestHandler responseDeletedKeys] : 332 -> 328
~ ___44-[SBKSyncRequestHandler responseDeletedKeys]_block_invoke : 20 -> 68
~ -[SBKSyncRequestHandler responseUpdatedKeys] : 332 -> 328
~ ___44-[SBKSyncRequestHandler responseUpdatedKeys]_block_invoke : 20 -> 68
~ -[SBKSyncRequestHandler responseDomainVersion] : 332 -> 328
~ -[SBKSyncRequestHandler setResponseDomainVersion:] : 256 -> 252
~ ___50-[SBKSyncRequestHandler setResponseDomainVersion:]_block_invoke : 20 -> 76
~ -[SBKSyncRequestHandler initWithBagContext:accountIdentifier:] : 468 -> 496
~ -[SBKSyncRequestHandler initWithBagContext:] : 108 -> 116
~ -[SBKZipDeflateMemoryOutputStream writeBuffer:size:] : 308 -> 316
~ -[SBKZipDeflateMemoryOutputStream close] : 208 -> 212
~ -[SBKZipDeflateMemoryOutputStream initWithBufferingSize:compressionType:] : 288 -> 292
~ +[SBKZipDeflateMemoryOutputStream dataByDeflatingData:] : 164 -> 168
~ -[SBKRequest setResponseDataProvider:] : 12 -> 64
~ -[SBKRequest setTransaction:] : 12 -> 64
~ -[SBKRequest newURLOperationWithDelegate:] : 44 -> 48
~ -[SBKRequest newURLOperation] : 44 -> 48
~ -[SBKRequest _defaultHeaderFields] : 260 -> 272
~ -[SBKRequest canonicalResponseForResponse:] : 8 -> 56
~ -[SBKRequest setBodyDataWithPropertyList:] : 404 -> 408
~ -[SBKRequest setBodyData:] : 116 -> 120
~ -[SBKRequest setValue:forArgument:] : 132 -> 128
~ -[SBKRequest descriptionWithoutHeaderFields] : 168 -> 180
~ -[SBKRequest description] : 192 -> 204
~ -[SBKRequest initWithRequestURL:] : 256 -> 268
~ +[SBKRequest bodyContentEncodingType] : 72 -> 76
~ +[SBKRequest bodyContentType] : 80 -> 84
~ -[SBKResponse description] : 156 -> 164
~ -[SBKResponse initWithCode:headerFields:responseDictionary:MIMEType:error:] : 396 -> 400
~ -[SBKResponseStatus requestError] : 264 -> 276
~ -[SBKResponseStatus initWithStatus:isRecoverable:isError:consoleDescription:shouldFileRadar:] : 164 -> 156
~ +[SBKResponseStatus responseStatusForStatusCodeNumber:] : 212 -> 224
~ ___55+[SBKResponseStatus responseStatusForStatusCodeNumber:]_block_invoke : 888 -> 892
~ -[SBKResponse initWithURLResponse:responseDictionary:] : 172 -> 180
~ +[SBKResponse responseWithResponse:] : 228 -> 244
~ +[SBKResponse responseWithCode:headerFields:responseDictionary:MIMEType:error:] : 172 -> 160
~ +[SBKResponse responseWithURLResponse:responseDictionary:] : 112 -> 108
~ +[SBKSyncRequest requestForTransaction:] : 184 -> 200
~ -[SBKSyncRequest canonicalResponseForResponse:] : 120 -> 128
~ -[SBKRequestHandler cancel] : 116 -> 120
~ -[SBKRequestHandler timeout] : 116 -> 120
~ -[SBKRequestHandler initWithBagContext:] : 116 -> 108
~ -[SBKTransaction setUserInfo:] : 12 -> 64
~ -[SBKTransaction setActiveRequest:] : 12 -> 64
~ -[SBKTransaction setRequestURL:] : 12 -> 64
~ -[SBKTransaction newRequest] : 104 -> 108
~ -[SBKTransaction clampsKey] : 104 -> 108
~ -[SBKTransaction processDataInResponse:withCompletionHandler:] : 116 -> 120
~ -[SBKTransaction transactionContextForKey:] : 136 -> 140
~ -[SBKTransaction initWithDomain:requestURL:] : 176 -> 168
~ _SBKStoreAccount : 84 -> 92
~ _SBKStoreAccountIdentifiers : 400 -> 420
~ _SBKStoreAccountIdentifierFromDatabasePath : 436 -> 460
~ +[SBKPullValueResponse responseWithResponse:transaction:] : 104 -> 108
~ -[SBKPullValueResponse deserializeResponseBodyWithTransaction:] : 228 -> 248
~ +[SBKPushValueRequest requestForTransaction:] : 180 -> 196
~ +[SBKPushValueRequest propertyListBodyWithTransaction:] : 380 -> 416
~ -[SBKPushValueRequest canonicalResponseForResponse:] : 120 -> 128

```

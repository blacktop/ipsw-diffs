## CDDataAccess

> `/System/Library/PrivateFrameworks/CDDataAccess.framework/CDDataAccess`

```diff

-3976.0.0.0.0
-  __TEXT.__text: 0x2afa8
-  __TEXT.__auth_stubs: 0xc40
+4034.15.0.0.0
+  __TEXT.__text: 0x27560
   __TEXT.__objc_methlist: 0x376c
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x12d0
-  __TEXT.__cstring: 0x22d6
+  __TEXT.__gcc_except_tab: 0x1144
+  __TEXT.__cstring: 0x22f7
   __TEXT.__oslogstring: 0x296f
-  __TEXT.__unwind_info: 0xc98
-  __TEXT.__objc_classname: 0x593
-  __TEXT.__objc_methname: 0x80b9
-  __TEXT.__objc_methtype: 0xe75
-  __TEXT.__objc_stubs: 0x5240
-  __DATA_CONST.__got: 0x4d0
+  __TEXT.__unwind_info: 0xb30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6e8
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2120
   __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x4d0
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x2480
   __AUTH_CONST.__objc_const: 0x4348
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xc80
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x910
   __DATA.__objc_ivar: 0x260
   __DATA.__data: 0x300
-  __DATA.__bss: 0x158
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x58
+  __DATA.__bss: 0xa8
+  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B45265B-AFD9-3DE5-BE8B-F65819046671
+  UUID: 50F277E8-61BA-38C6-B26F-93EC9DB71C31
   Functions: 1177
-  Symbols:   4072
-  CStrings:  2390
+  Symbols:   4078
+  CStrings:  779
 
Symbols:
+ ___block_literal_global.490
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- ___block_literal_global.491
Functions:
~ -[DAAccount dealloc] : 288 -> 236
~ -[DAAccount accountDescription] : 88 -> 80
~ -[ASAccountActor initWithDAAccount:] : 192 -> 180
~ -[ASAccountActor startup] : 136 -> 132
~ -[ASAccountActor mailboxes] : 132 -> 128
~ -[ASAccountActor inboxFolder] : 132 -> 128
~ -[ASAccountActor sentItemsFolder] : 132 -> 128
~ -[ASAccountActor deletedItemsFolder] : 132 -> 128
~ -[DAAccount initWithBackingAccountInfo:] : 288 -> 280
~ +[DAAccount daAccountSubclassWithBackingAccountInfo:] : 132 -> 128
~ -[DAAccount resetAccountID] : 120 -> 116
~ -[DAAccount scheduleIdentifier] : 184 -> 160
~ -[DAAccount changeTrackingID] : 116 -> 108
~ -[DAAccount setAccountDescription:] : 100 -> 96
~ -[DAAccount enabledForDADataclass:] : 76 -> 72
~ -[DAAccount setEnabled:forDADataclass:] : 384 -> 316
~ -[DAAccount enabledDataclassesBitmask] : 64 -> 60
~ -[DAAccount spinnerIdentifiers] : 204 -> 156
~ -[DAAccount accountPropertyForKey:] : 116 -> 108
~ -[DAAccount removeAccountPropertyForKey:] : 104 -> 100
~ -[DAAccount objectForKeyedSubscript:] : 116 -> 108
~ -[DAAccount accountBoolPropertyForKey:] : 116 -> 108
~ -[DAAccount setAccountBoolProperty:forKey:] : 152 -> 144
~ -[DAAccount accountIntPropertyForKey:] : 116 -> 108
~ -[DAAccount setAccountIntProperty:forKey:] : 152 -> 144
~ -[DAAccount resumeMonitoringFoldersWithIDs:] : 200 -> 152
~ -[DAAccount suspendMonitoringFoldersWithIDs:] : 240 -> 192
~ -[DAAccount stopMonitoringFolderWithID:] : 240 -> 192
~ -[DAAccount stateString] : 420 -> 376
~ -[DAAccount setConsumer:forTask:] : 308 -> 264
~ -[DAAccount removeConsumerForTask:] : 244 -> 196
~ -[DAAccount clientToken] : 84 -> 76
~ -[DAAccount clientTokenRequestedByServer] : 176 -> 164
~ -[DAAccount passwordWithExpected:] : 228 -> 208
~ -[DAAccount password] : 100 -> 92
~ -[DAAccount setPassword:] : 492 -> 424
~ -[DAAccount urlFromDataclassPropertiesForDataclass:] : 636 -> 572
~ -[DAAccount hostFromDataclassPropertiesForDataclass:] : 84 -> 76
~ -[DAAccount useSSLFromDataclassPropertiesForDataclass:] : 116 -> 104
~ -[DAAccount portFromDataclassPropertiesForDataclass:] : 88 -> 80
~ -[DAAccount setHost:] : 268 -> 216
~ -[DAAccount useSSL] : 84 -> 80
~ -[DAAccount setUseSSL:] : 104 -> 100
~ -[DAAccount setEmailAddress:] : 112 -> 108
~ -[DAAccount emailAddresses] : 156 -> 148
~ -[DAAccount port] : 68 -> 64
~ -[DAAccount setPort:] : 104 -> 100
~ -[DAAccount principalPath] : 92 -> 84
~ -[DAAccount scheme] : 80 -> 64
~ -[DAAccount principalURL] : 204 -> 188
~ -[DAAccount setPrincipalURL:] : 352 -> 316
~ -[DAAccount checkValidityOnAccountStore:withConsumer:inQueue:] : 248 -> 260
~ ___62-[DAAccount checkValidityOnAccountStore:withConsumer:inQueue:]_block_invoke_2 : 248 -> 236
~ -[DAAccount discoverInitialPropertiesWithConsumer:] : 200 -> 152
~ -[DAAccount setShouldDoInitialAutodiscovery:] : 108 -> 104
~ -[DAAccount shouldAutodiscoverAccountProperties] : 140 -> 132
~ -[DAAccount onBehalfOfBundleIdentifier] : 144 -> 140
~ -[DAAccount shouldRemoveDBSyncDataOnAccountChange] : 76 -> 68
~ -[DAAccount accountDidChangeFromOldAccountInfo:] : 252 -> 204
~ -[DAAccount additionalHeaderValues] : 480 -> 448
~ -[DAAccount customConnectionProperties] : 288 -> 272
~ -[DAAccount oauth2Token] : 624 -> 536
~ -[DAAccount tearDown] : 240 -> 192
~ -[DAAccount monitorFolderWithID:] : 168 -> 164
~ -[DAAccount stopMonitoringFoldersWithIDs:] : 240 -> 192
~ -[DAAccount stopMonitoringFolders] : 240 -> 192
~ -[DAAccount removeClientCertificateData] : 116 -> 112
~ -[DAAccount saveAccountPropertiesWithCompletionHandler:] : 548 -> 464
~ ___34-[DAAccount saveAccountProperties]_block_invoke : 228 -> 180
~ -[DAAccount updateExistingAccountProperties] : 368 -> 280
~ -[DAAccount keychainAccessibilityType] : 132 -> 120
~ -[DAAccount addUsernameToURL:] : 312 -> 280
~ -[DAAccount setIdentityCertificatePersistentID:managedByProfile:] : 312 -> 260
~ -[DAAccount _isIdentityManagedByProfile] : 68 -> 64
~ -[DAAccount exceptionsForDigest:] : 132 -> 120
~ -[DAAccount setExceptions:forDigest:] : 260 -> 248
~ -[DAAccount isChildAccount] : 76 -> 68
~ -[DAAccount resetCertWarnings] : 60 -> 56
~ -[DAAccount resetStatusReport] : 260 -> 240
~ -[DAAccount shouldFailAllTasks] : 780 -> 684
~ -[DAAccount isEqualToAccount:] : 144 -> 140
~ -[DAAccount accountHasSignificantPropertyChangesFromOldAccountInfo:] : 968 -> 908
~ ___31-[DAAccount copyStorageSession]_block_invoke : 104 -> 100
~ ___31-[DAAccount copyStorageSession]_block_invoke_2 : 292 -> 284
~ -[DAAccount description] : 204 -> 188
~ -[DAAccount shutdown] : 144 -> 140
~ -[DAAccount reload] : 120 -> 112
~ -[DAAccount accountTypeIdentifier] : 88 -> 80
~ -[DAAccount shouldCancelTaskDueToOnPowerFetchMode] : 148 -> 144
~ -[DAAccount saveXpcActivity:] : 248 -> 196
~ -[DAAccount incrementXpcActivityContinueCount] : 252 -> 204
~ -[DAAccount decrementXpcActivityContinueCount] : 280 -> 232
~ -[DAAccount removeXpcActivity] : 336 -> 280
~ -[DAAccount setStatusReport:] : 64 -> 12
~ -[DAAccount setTrustHandler:] : 64 -> 12
~ -[DAAccount setDataclassPropertyURLsByDataclass:] : 64 -> 12
~ -[DAAccount setPendingQueries:] : 64 -> 12
~ -[DAAccount setPendingQueryQueue:] : 64 -> 12
~ -[DAAccount setLastQueryStartedTime:] : 64 -> 12
~ -[DAAccount(TrustHandling) handleTrustChallenge:] : 96 -> 92
~ -[DAAccount(AuthenticationExtensions) localizedIdenticalAccountFailureMessage] : 144 -> 140
~ -[DAAccount(AuthenticationExtensions) localizedInvalidPasswordMessage] : 144 -> 140
~ -[DAAccount(AuthenticationExtensions) dropAssertionsAndRenewCredentialsInQueue:withHandler:] : 556 -> 504
~ ___92-[DAAccount(AuthenticationExtensions) dropAssertionsAndRenewCredentialsInQueue:withHandler:]_block_invoke : 224 -> 220
~ ___92-[DAAccount(AuthenticationExtensions) dropAssertionsAndRenewCredentialsInQueue:withHandler:]_block_invoke_2 : 468 -> 408
~ -[DAAccount(AuthenticationExtensions) _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:] : 340 -> 344
~ ___100-[DAAccount(AuthenticationExtensions) _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke : 220 -> 216
~ ___100-[DAAccount(AuthenticationExtensions) _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke_2 : 104 -> 100
~ ___99-[DAAccount(AuthenticationExtensions) webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke : 112 -> 108
~ -[DAAccount(AuthenticationExtensions) handleValidationError:completion:] : 592 -> 544
~ +[DAAccount(AuthenticationExtensions) _leafAccountTypes] : 84 -> 68
~ ___56+[DAAccount(AuthenticationExtensions) _leafAccountTypes]_block_invoke : 80 -> 76
~ +[DAAccount(AuthenticationExtensions) oneshotListOfAccountIDs] : 548 -> 532
~ +[DAAccount(AuthenticationExtensions) reacquireClientRestrictions:] : 300 -> 296
~ -[DAAccount(EventsSupport) beginDownloadingAttachmentWithUUID:consumer:] : 324 -> 272
~ -[DAAccount(EventsSupport) requestCalendarAvailabilityForStartDate:endDate:ignoredEventID:addresses:consumer:] : 292 -> 236
~ -[DAAccount(EventsSupport) cancelCalendarAvailabilityRequestWithID:] : 216 -> 164
~ -[DAAccount(EventsSupport) performCalendarDirectorySearchForTerms:recordTypes:resultLimit:consumer:] : 296 -> 240
~ -[DAAccount(EventsSupport) cancelCalendarDirectorySearchWithID:] : 240 -> 188
~ -[DAAccount(EventsSupport) respondToShareRequestForCalendar:withResponse:consumer:] : 324 -> 272
~ -[DAAccount(EventsSupport) reportShareRequestAsJunkForCalendar:consumer:] : 324 -> 272
~ +[DATransactionMonitor sharedTransactionMonitor] : 84 -> 68
~ -[DATransactionMonitor init] : 236 -> 188
~ -[DATransactionMonitor incrementTransactionCountForTransaction:] : 188 -> 192
~ ___64-[DATransactionMonitor incrementTransactionCountForTransaction:]_block_invoke : 104 -> 100
~ ___64-[DATransactionMonitor incrementTransactionCountForTransaction:]_block_invoke_2 : 412 -> 352
~ ___64-[DATransactionMonitor decrementTransactionCountForTransaction:]_block_invoke : 532 -> 468
~ -[DATransactionMonitor setTransactions:] : 64 -> 12
~ +[DAAccountLoader sharedInstance] : 176 -> 160
~ -[DAAccountLoader _addAccountInfo:forFrameworkNamed:] : 748 -> 664
~ -[DAAccountLoader init] : 1212 -> 1168
~ +[DAAccountLoader _findPrivateFrameworks] : 136 -> 128
~ -[DAAccountLoader _loadFrameworkAtSubpath:] : 392 -> 332
~ -[DAAccountLoader loadFrameworkForACAccountType:] : 308 -> 244
~ -[DAAccountLoader loadDaemonBundleForACAccountType:] : 132 -> 124
~ -[DAAccountLoader accountClassForACAccount:] : 672 -> 564
~ -[DAAccountLoader clientAccountClassForACAccount:] : 764 -> 640
~ -[DAAccountLoader daemonAccountClassForACAccount:] : 808 -> 680
~ -[DAAccountLoader agentClassForACAccount:] : 556 -> 492
~ -[DAAccountLoader daemonAppropriateAccountClassForACAccount:] : 120 -> 112
~ -[DAAccountLoader setAcAccountTypeToAccountFrameworkSubpath:] : 64 -> 12
~ -[DAAccountLoader setAcAccountTypeToAccountDaemonBundleSubpath:] : 64 -> 12
~ -[DAAccountLoader setAcAccountTypeToClassNames:] : 64 -> 12
~ -[DAAccountLoader setAcParentAccountTypeToChildAccountTypes:] : 64 -> 12
~ -[DAAccountClassNames description] : 148 -> 140
~ -[DAAccountClassNames setAccountClassName:] : 64 -> 12
~ -[DAAccountClassNames setClientAccountClassName:] : 64 -> 12
~ -[DAAccountClassNames setDaemonAccountClassName:] : 64 -> 12
~ -[DAAccountClassNames setAgentClassName:] : 64 -> 12
~ -[DAAction initWithItemChangeType:changedItem:serverId:] : 160 -> 168
~ -[DAAction initWithItemChangeType:changedItem:serverId:instanceId:] : 196 -> 204
~ -[DAAction description] : 340 -> 316
~ -[DAAction initWithCoder:] : 588 -> 520
~ -[DAAction encodeWithCoder:] : 292 -> 272
~ -[DAAction hash] : 104 -> 96
~ -[DAAction isEqual:] : 568 -> 536
~ -[DAAction setServerId:] : 64 -> 12
~ -[DAAction setInstanceId:] : 64 -> 12
~ -[DAAction _setChangedItem:] : 64 -> 12
~ -[DAAction setForwardedAttendees:] : 64 -> 12
~ -[DAAction setForwardedAttendeeUUIDs:] : 64 -> 12
~ -[DAMoveAction initWithItemChangeType:changedItem:sourceContainerId:sourceServerId:destinationContainerId:] : 188 -> 196
~ -[DAMoveAction initWithCoder:] : 308 -> 292
~ -[DAMoveAction encodeWithCoder:] : 256 -> 240
~ -[DAMoveAction setSourceContainerId:] : 64 -> 12
~ -[DAMoveAction setSourceServerId:] : 64 -> 12
~ -[DAMoveAction setDestinationContainerId:] : 64 -> 12
~ -[DAResponse initWithCoder:] : 164 -> 160
~ -[DAResponse encodeWithCoder:] : 152 -> 148
~ -[DAABLegacyContainer setName:] : 104 -> 100
~ -[DAABLegacyContainer setExternalIdentifier:] : 104 -> 100
~ -[DAABLegacyContainer setCTag:] : 104 -> 100
~ -[DAABLegacyContainer setSyncTag:] : 104 -> 100
~ -[DAABLegacyContainer setSyncData:] : 104 -> 100
~ -[DAABLegacyContainer setConstraintsPath:] : 104 -> 100
~ -[DAABLegacyContainer meContactidentifier] : 120 -> 112
~ -[DAABLegacyContainer accountIdentifier] : 120 -> 112
~ -[DAABLegacyContainer updateSaveRequest:] : 68 -> 64
~ -[DAABLegacyContainer asContainer] : 64 -> 60
~ -[DAFolder description] : 276 -> 256
~ -[DAFolder hash] : 60 -> 56
~ -[DAFolder isEqual:] : 744 -> 708
~ +[DAAccountMonitor sharedMonitor] : 84 -> 68
~ -[DAAccountMonitor init] : 188 -> 180
~ ___35-[DAAccountMonitor monitorAccount:]_block_invoke : 88 -> 84
~ ___37-[DAAccountMonitor unmonitorAccount:]_block_invoke : 88 -> 84
~ ___37-[DAAccountMonitor monitoredAccounts]_block_invoke : 112 -> 104
~ -[DAAccountMonitor setAccounts:] : 64 -> 12
~ -[DAAccountMonitor setAccountsQueue:] : 64 -> 12
~ +[DAKeychain sharedKeychain] : 92 -> 84
~ -[DAKeychain _DACopyMutableQueryForAccountWithPersistentUUID:] : 176 -> 172
~ -[DAKeychain passwordForAccountWithPersistentUUID:expectedAccessibility:shouldSetAccessibility:passwordExpected:] : 1032 -> 968
~ -[DAKeychain setPassword:forAccount:withPersistentUUID:withAccessibility:] : 676 -> 628
~ -[DAKeychain removePasswordForAccount:withPersistentUUID:] : 384 -> 332
~ -[DAKeychain migratePasswordForAccount:] : 1272 -> 1188
~ -[NSString(DAKeychainAdditions) stringByURLQuoting] : 108 -> 96
~ -[NSURL(DAKeychainAddition) uri] : 196 -> 184
~ -[NSURL(DAKeychainAddition) URLWithoutUsername] : 256 -> 236
~ -[NSURL(DAKeychainAddition) URLByRemovingLastPathComponent] : 312 -> 280
~ -[NSURL(DAKeychainAddition) URLWithUsername:withPassword:] : 496 -> 472
~ -[NSURL(DAKeychainAddition) URLWithUsername:] : 364 -> 344
~ -[DAKeychain(OldAndBusted) saveKeychainInformationsForURL:andPassword:withAccessibility:] : 1504 -> 1428
~ __setPasswordInKeychain : 584 -> 528
~ -[DAKeychain(OldAndBusted) loadKeychainInformationsForURL:] : 1352 -> 1276
~ -[DAKeychain(OldAndBusted) removeKeychainInformationsForURL:] : 1284 -> 1208
~ -[DAKeychain(OldAndBusted) guessPasswordForURL:] : 616 -> 552
~ -[DAMailboxSetFlagsRequest hash] : 156 -> 152
~ -[DAMailboxSetFlagsRequest isEqual:] : 312 -> 300
~ -[DAMailboxSetFlagsRequest description] : 208 -> 196
~ -[DAMailboxGetUpdatesRequest description] : 176 -> 168
~ -[DAMailboxDeleteMessageRequest hash] : 60 -> 56
~ -[DAMailboxDeleteMessageRequest isEqual:] : 232 -> 228
~ -[DAMailboxDeleteMessageRequest description] : 176 -> 164
~ -[DAMailboxFetchMessageRequest hash] : 156 -> 152
~ -[DAMailboxFetchMessageRequest isEqual:] : 312 -> 300
~ -[DAMailboxFetchMessageRequest description] : 208 -> 196
~ -[DAMailboxFetchSearchResultRequest initRequestForBodyFormat:withFolderID:withServerID:withLongID:withBodySizeLimit:] : 256 -> 264
~ -[DAMailboxFetchSearchResultRequest hash] : 156 -> 152
~ -[DAMailboxFetchSearchResultRequest isEqual:] : 312 -> 300
~ -[DAMailboxFetchSearchResultRequest description] : 208 -> 196
~ -[DAMessageMoveRequest initMoveRequestWithMessage:fromFolder:toFolder:] : 216 -> 224
~ -[DAMessageMoveRequest hash] : 184 -> 172
~ -[DAMessageMoveRequest isEqual:] : 588 -> 552
~ -[DAMessageMoveRequest description] : 236 -> 216
~ -[DAMessageMoveRequest setContext:] : 64 -> 12
~ -[DAMessageFetchAttachmentRequest initWithAttachmentName:andMessageServerID:] : 168 -> 172
~ -[DAMessageFetchAttachmentRequest hash] : 156 -> 148
~ -[DAMessageFetchAttachmentRequest isEqual:] : 384 -> 376
~ -[DAMessageFetchAttachmentRequest description] : 204 -> 188
~ -[DADraftMessageRequest description] : 196 -> 180
~ -[DADraftMessageRequest setMessage:] : 64 -> 12
~ -[DAMoveResponse initWithStatus:sourceID:destID:] : 184 -> 188
~ -[DAMoveResponse description] : 252 -> 232
~ -[DAMoveResponse setOrigRequest:] : 64 -> 12
~ -[DAResolveRecipientsRequest initWithEmailAddresses:retrieveCertificates:retrieveAvailability:withStartTime:endTime:] : 200 -> 208
~ -[DAResolveRecipientsRequest isEqual:] : 160 -> 164
~ -[DAResolveRecipientsRequest description] : 176 -> 164
~ -[DAResolveRecipientsRequest setEmailAddresses:] : 64 -> 12
~ -[DAResolveRecipientsRequest setStartTime:] : 64 -> 12
~ -[DAResolveRecipientsRequest setEndTime:] : 64 -> 12
~ -[DAResolvedRecipient description] : 1072 -> 1028
~ -[DAResolvedRecipient addCert:forEmailAddress:] : 312 -> 292
~ -[DAResolvedRecipient setMergedFreeBusy:] : 64 -> 12
~ -[DAResolvedRecipient setMResolvedEmailToX509Certs:] : 64 -> 12
~ -[DAMailMessage rfc822Data] : 636 -> 580
~ -[DAMailMessage initWithCoder:] : 144 -> 140
~ -[DAMailMessage encodeWithCoder:] : 124 -> 120
~ -[DAAccount(Searching) getPendingQueryQueue] : 272 -> 256
~ -[DAAccount(Searching) _dequeueQuery] : 428 -> 368
~ ___37-[DAAccount(Searching) _dequeueQuery]_block_invoke : 364 -> 332
~ -[DAAccount(Searching) performSearchQuery:] : 544 -> 484
~ ___43-[DAAccount(Searching) performSearchQuery:]_block_invoke : 148 -> 140
~ ___42-[DAAccount(Searching) cancelSearchQuery:]_block_invoke : 292 -> 272
~ ___46-[DAAccount(Searching) cancelAllSearchQueries]_block_invoke : 164 -> 152
~ -[DAAccount(Searching) searchQueriesRunning] : 244 -> 240
~ ___44-[DAAccount(Searching) searchQueriesRunning]_block_invoke : 92 -> 88
~ -[DAAccount(SearchSubclassing) _reallyPerformSearchQuery:] : 292 -> 236
~ -[DAContactsBasedAccount initWithAccount:] : 108 -> 116
~ -[DAContactsBasedAccount legacyIdentifier] : 60 -> 56
~ -[DAContactsBasedAccount identifier] : 84 -> 76
~ -[DAContactsBasedAccount externalIdentifier] : 84 -> 76
~ -[DAContactsBasedAccount updateSaveRequest:] : 188 -> 180
~ __DASecCopyIdentityFromPersist : 304 -> 300
~ __DASecDeleteIdentityByPersistentRef : 272 -> 268
~ __DASecIdentityCopySSLClientAuthenticationChain : 352 -> 348
~ _acDataclassForDADataclass : 372 -> 320
~ _daDataclassForACDataclass : 236 -> 232
~ _daDataclassesForACDataclasses : 244 -> 240
~ -[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:] : 1032 -> 1024
~ ___129-[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:]_block_invoke : 104 -> 100
~ ___129-[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:]_block_invoke_2 : 184 -> 180
~ ___129-[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:]_block_invoke_3 : 328 -> 320
~ ___129-[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:]_block_invoke.34 : 228 -> 220
~ ___129-[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:]_block_invoke_4.40 : 424 -> 420
~ -[ACAccountStore(DAExtensions) da_loadDAAccountsWithCompletion:] : 152 -> 144
~ -[ACAccountStore(DAExtensions) da_loadDAAccountsEnabledForDADataclasses:withCompletion:] : 156 -> 148
~ -[ACAccountStore(DAExtensions) da_accounts] : 304 -> 308
~ ___43-[ACAccountStore(DAExtensions) da_accounts]_block_invoke : 112 -> 96
~ -[ACAccountStore(DAExtensions) da_accountsEnabledForDADataclasses:] : 320 -> 324
~ ___67-[ACAccountStore(DAExtensions) da_accountsEnabledForDADataclasses:]_block_invoke : 112 -> 96
~ -[ACAccountStore(DAExtensions) da_accountsWithAccountTypeIdentifiers:] : 328 -> 332
~ ___70-[ACAccountStore(DAExtensions) da_accountsWithAccountTypeIdentifiers:]_block_invoke : 112 -> 96
~ -[ACAccountStore(DAExtensions) da_accountsWithAccountTypeIdentifiers:outError:] : 572 -> 564
~ -[ACAccountStore(DAExtensions) da_accountsWithAccountTypeIdentifiers:enabledForDADataclasses:] : 336 -> 340
~ ___94-[ACAccountStore(DAExtensions) da_accountsWithAccountTypeIdentifiers:enabledForDADataclasses:]_block_invoke : 112 -> 96
~ _addNullRunLoopSourceForRunLoopAndModes : 444 -> 456
~ _walkUpDAErrorChain : 228 -> 216
~ _statusAndErrorIndicateWeShouldTurnOnReachability : 288 -> 280
~ _statusAndErrorIndicatePersistentFolderSyncFailure : 156 -> 160
~ _runLoopModesToPerformDelayedSelectorsIn : 240 -> 228
~ -[NSData(DAHexString) da_hexString] : 364 -> 368
~ -[NSData(DAHexString) da_lowercaseHexStringWithoutSpaces] : 120 -> 116
~ -[NSData(DAHexString) da_uppercaseHexStringWithoutSpaces] : 148 -> 140
~ +[NSData(DAHexString) da_dataWithHexString:stringIsUppercase:] : 464 -> 460
~ _DAUserAgent : 428 -> 392
~ _DAProductString : 84 -> 68
~ ___DAProductString_block_invoke : 68 -> 64
~ __MGStringForKey : 280 -> 276
~ _DAModelString : 84 -> 68
~ ___DAModelString_block_invoke : 68 -> 64
~ -[NSString(DAExtensions) da_removeSlashIfNeeded] : 108 -> 96
~ -[NSString(DAExtensions) da_appendSlashIfNeeded] : 104 -> 92
~ -[NSString(DAExtensions) da_stringByURLEscapingPathComponent] : 108 -> 96
~ +[NSString(DAExtensions) da_new64ByteGUID] : 228 -> 216
~ -[NSSet(DAExtensions) DACompactDescription] : 260 -> 240
~ -[NSURL(DAExtensions) da_isEqualToDAVURL:] : 1180 -> 1084
~ -[NSURL(DAExtensions) da_urlBySettingScheme:keepUsername:] : 568 -> 516
~ -[NSURL(DAExtensions) da_urlBySettingHost:keepUsername:] : 568 -> 516
~ -[NSURL(DAExtensions) da_urlBySettingPort:keepUsername:] : 560 -> 512
~ -[NSURL(DAExtensions) da_urlBySettingPath:keepUsername:] : 568 -> 516
~ -[NSURL(DAExtensions) da_urlBySettingUsername:] : 544 -> 500
~ -[NSURL(DAExtensions) da_urlByRemovingUsername] : 480 -> 436
~ -[NSURL(DAExtensions) da_urlForLogging] : 248 -> 232
~ -[NSURL(DAExtensions) da_pathWithoutTrailingRemovingSlash] : 172 -> 160
~ +[NSURL(DAExtensions) da_URLWithDirtyString:] : 208 -> 200
~ +[NSURL(DAExtensions) da_classicPortForScheme:] : 128 -> 124
~ -[NSURL(DALeastInfoURLExtension) da_leastInfoStringRepresentationRelativeToParentURL:] : 680 -> 620
~ -[NSString(DALeastInfoURLExtension) da_absoluteURLForChildLeastInfoRepresentationRelativeToParentURL:] : 240 -> 216
~ -[NSURLRequest(DAExtensions) DARequestByApplyingStorageSession:] : 296 -> 248
~ _areDADiagnosticsEnabled : 76 -> 72
~ -[NSDictionary(DAExtensions) DAObjectForKeyCaseInsensitive:] : 332 -> 328
~ -[NSDictionary(DAExtensions) DAMergeOverrideDictionary:] : 480 -> 468
~ -[NSError(DADAExtendedDescription) DAExtendedDescription] : 636 -> 592
~ _daDeviceID : 84 -> 68
~ ___daDeviceID_block_invoke : 600 -> 520
~ _dataaccess_get_global_queue : 60 -> 12
~ -[DATaskManager allTasks] : 992 -> 960
~ -[DATaskManager initWithAccount:] : 160 -> 168
~ -[DATaskManager dealloc] : 1044 -> 948
~ -[DATaskManager _populateVersionDescriptions] : 124 -> 120
~ -[DATaskManager _version] : 176 -> 148
~ -[DATaskManager userAgent] : 176 -> 148
~ ___26-[DATaskManager userAgent]_block_invoke : 160 -> 148
~ -[DATaskManager user] : 84 -> 76
~ -[DATaskManager port] : 60 -> 56
~ -[DATaskManager server] : 84 -> 76
~ -[DATaskManager password] : 84 -> 76
~ -[DATaskManager OAuth2Token] : 248 -> 224
~ -[DATaskManager useSSL] : 60 -> 56
~ -[DATaskManager identityPersist] : 84 -> 76
~ -[DATaskManager accountID] : 84 -> 76
~ -[DATaskManager accountPersistentUUID] : 84 -> 76
~ -[DATaskManager isShutdown] : 72 -> 68
~ -[DATaskManager submitExclusiveTask:toFrontOfQueue:] : 1240 -> 1120
~ -[DATaskManager submitIndependentTask:] : 1088 -> 980
~ -[DATaskManager submitQueuedTask:] : 1132 -> 1016
~ -[DATaskManager cancelTask:withUnderlyingError:] : 228 -> 184
~ -[DATaskManager shutdown] : 968 -> 860
~ -[DATaskManager stateString] : 492 -> 440
~ -[DATaskManager _useOpportunisticSocketsAgain] : 236 -> 184
~ -[DATaskManager _powerLogInfoDictionary] : 416 -> 372
~ -[DATaskManager _clearUserInitiatedSyncTimer] : 236 -> 184
~ -[DATaskManager _endXpcTransaction] : 484 -> 420
~ -[DATaskManager _hasTasksForcingNetworkConnection] : 544 -> 492
~ -[DATaskManager _hasTasksIndicatingARunningSync] : 64 -> 60
~ -[DATaskManager taskDidFinish:] : 4864 -> 4492
~ -[DATaskManager taskRequestModal:] : 1272 -> 1120
~ -[DATaskManager taskEndModal:] : 608 -> 520
~ -[DATaskManager taskIsModal:] : 220 -> 208
~ -[DATaskManager shouldCancelTaskDueToOnPowerFetchMode] : 60 -> 56
~ -[DATaskManager _performTask:] : 720 -> 704
~ -[DATaskManager _requestCancelTasksWithReason:] : 404 -> 396
~ -[DATaskManager _startModal:] : 420 -> 364
~ -[DATaskManager _reactivateHeldTasks] : 744 -> 704
~ -[DATaskManager _makeStateTransition] : 2180 -> 1964
~ -[DATaskManager _scheduleSelector:withArgument:] : 364 -> 308
~ -[DATaskManager _scheduleStartModal:] : 224 -> 176
~ -[DATaskManager _cancelTasksWithReason:] : 640 -> 612
~ -[DATaskManager _retainPowerAssertionForTask:] : 252 -> 232
~ -[DATaskManager _releasePowerAssertionForTask:] : 232 -> 228
~ ___47-[DATaskManager _releasePowerAssertionForTask:]_block_invoke : 92 -> 88
~ -[DATaskManager queuedExclusiveTasks] : 92 -> 84
~ -[DATaskManager independentTasks] : 92 -> 84
~ -[DATaskManager heldIndependentTasks] : 92 -> 84
~ -[DATaskManager modalHeldIndependentTasks] : 92 -> 84
~ -[DATaskManager mQueuedTasks] : 92 -> 84
~ -[DATaskManager queuedModalTasks] : 92 -> 84
~ -[DATaskManager setActiveModalTask:] : 64 -> 12
~ -[DATaskManager setActiveQueuedTask:] : 64 -> 12
~ -[DATaskManager setQueuedExclusiveTasks:] : 64 -> 12
~ -[DATaskManager setActiveExclusiveTask:] : 64 -> 12
~ -[DATaskManager setIndependentTasks:] : 64 -> 12
~ -[DATaskManager setHeldIndependentTasks:] : 64 -> 12
~ -[DATaskManager setModalHeldIndependentTasks:] : 64 -> 12
~ -[DATaskManager setMQueuedTasks:] : 64 -> 12
~ -[DATaskManager setModalHeldActiveQueuedTask:] : 64 -> 12
~ -[DATaskManager setQueuedModalTasks:] : 64 -> 12
~ -[DATaskManager setManagerIdleTimer:] : 64 -> 12
~ -[DATaskManager setUserInitiatedSyncTimer:] : 64 -> 12
~ -[DATaskManager setXpcTransactionTimer:] : 64 -> 12
~ -[DATaskManager setPowerLogIdleTimer:] : 64 -> 12
~ +[DAPowerAssertionManager sharedPowerAssertionManager] : 156 -> 144
~ -[DAPowerAssertionManager powerAssertionRetainCount:] : 204 -> 196
~ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:] : 820 -> 720
~ -[DAPowerAssertionManager releasePowerAssertion:] : 844 -> 728
~ -[DAPowerAssertionManager stateString] : 236 -> 216
~ -[DAPowerAssertionManager dropPowerAssertionsForGroupIdentifier:] : 852 -> 820
~ -[DAPowerAssertionManager reattainPowerAssertionsForGroupIdentifier:] : 852 -> 820
~ -[DAPowerAssertionManager _retainAssertionForContext:] : 472 -> 408
~ -[DAPowerAssertionManager _releaseAssertionForContext:] : 328 -> 268
~ -[DAPowerAssertionManager setContexts:] : 64 -> 12
~ -[DAPowerAssertionManager setGroupIdentifierToContexts:] : 64 -> 12
~ -[DAPowerAssertionManager setContextToGroupIdentifier:] : 64 -> 12
~ -[DAPowerAssertionManager setHeldAsideGroupIdentifiers:] : 64 -> 12
~ -[DAPowerAssertionManager setHeldAsideContexts:] : 64 -> 12
~ -[DAPowerAssertionManager setContextToPowerAssertionRef:] : 64 -> 12
~ -[ASAccountActor mailNumberOfPastDaysToSync] : 132 -> 128
~ -[ASAccountActor supportsMailboxSearch] : 132 -> 128
~ -[ASAccountActor supportsEmailFlagging] : 132 -> 128
~ -[ASAccountActor supportsConversations] : 132 -> 128
~ -[ASAccountActor supportsDraftFolderSync] : 132 -> 128
~ -[ASAccountActor supportsSmartForwardReply] : 132 -> 128
~ -[ASAccountActor supportsUniqueServerId] : 132 -> 128
~ -[ASAccountActor generatesBulletins] : 132 -> 128
~ -[ASAccountActor setGeneratesBulletins:] : 136 -> 132
~ -[ASAccountActor signingIdentityPersistentReference] : 132 -> 128
~ -[ASAccountActor setSigningIdentityPersistentReference:] : 136 -> 132
~ -[ASAccountActor encryptionIdentityPersistentReference] : 132 -> 128
~ -[ASAccountActor setEncryptionIdentityPersistentReference:] : 136 -> 132
~ -[ASAccountActor customSignature] : 132 -> 128
~ -[ASAccountActor setCustomSignature:] : 136 -> 132
~ -[ASAccountActor setMailNumberOfPastDaysToSync:] : 136 -> 132
~ -[ASAccountActor monitorFoldersForUpdates:] : 136 -> 132
~ -[ASAccountActor monitorFoldersForUpdates:persistent:] : 136 -> 132
~ -[ASAccountActor stopMonitoringFoldersForUpdates:] : 136 -> 132
~ -[ASAccountActor stopMonitoringAllFolders] : 136 -> 132
~ -[ASAccountActor foldersTag] : 132 -> 128
~ -[ASAccountActor folderIDsThatExternalClientsCareAboutWithTag:] : 132 -> 128
~ -[ASAccountActor folderIDsThatExternalClientsCareAboutForDataclasses:withTag:] : 132 -> 128
~ -[ASAccountActor setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:] : 132 -> 128
~ -[ASAccountActor reattemptInvitationLinkageForMetaData:inFolderWithId:] : 132 -> 128
~ -[ASAccountActor unactionableICSRepresentationForMetaData:inFolderWithId:outSummary:] : 132 -> 128
~ -[ASAccountActor sendMessageWithRFC822Data:messageID:outgoingMessageType:originalMessageFolderID:originalMessageItemID:originalMessageLongID:originalAccountID:useSmartTasksIfPossible:isUserRequested:consumer:context:] : 132 -> 128
~ -[ASAccountActor sendSmartMessageWithRFC822Data:messageID:outgoingMessageType:originalMessageFolderID:originalMessageItemID:originalMessageLongID:originalAccountID:replaceOriginalMime:isUserRequested:consumer:context:] : 132 -> 128
~ -[ASAccountActor performMailboxRequest:mailbox:previousTag:clientWinsOnSyncConflict:isUserRequested:consumer:] : 132 -> 128
~ -[ASAccountActor performMailboxRequests:mailbox:previousTag:clientWinsOnSyncConflict:isUserRequested:consumer:] : 132 -> 128
~ -[ASAccountActor performMoveRequests:consumer:] : 132 -> 128
~ -[ASAccountActor performFetchAttachmentRequest:consumer:] : 132 -> 128
~ -[ASAccountActor performFetchMessageSearchResultRequests:consumer:] : 132 -> 128
~ -[ASAccountActor performResolveRecipientsRequest:consumer:] : 132 -> 128
~ -[ASAccountActor performFolderChange:isUserRequested:] : 136 -> 132
~ -[ASAccountActor cancelTaskWithID:] : 136 -> 132
~ -[ASAccountActor performSearchQuery:] : 136 -> 132
~ -[ASAccountActor cancelSearchQuery:] : 136 -> 132
~ -[ASAccountActor cancelAllSearchQueries] : 136 -> 132
~ -[ASAccountActor searchQueriesRunning] : 132 -> 128
~ -[ASAccountActor draftsFolder] : 132 -> 128
~ -[ASAccountActor setAccount:] : 136 -> 132
~ -[ASAccountActor shutdown] : 136 -> 132
~ -[ASAccountActor _daemonDiedNotification:] : 136 -> 132
~ -[ASAccountActor _folderUpdatedNotification:] : 136 -> 132
~ -[ASAccountActor _newASPolicyKeyNotification:] : 136 -> 132
~ -[ASAccountActor _folderHierarchyChanged] : 136 -> 132
~ -[ASAccountActor _foldersThatExternalClientsCareAboutChanged] : 136 -> 132
~ -[ASAccountActor _accountPasswordChanged] : 136 -> 132
~ -[DADataHandler dataclass] : 204 -> 156
~ -[DADataHandler getIdFromLocalObject:] : 204 -> 156
~ -[DADataHandler copyLocalObjectFromId:] : 204 -> 156
~ -[DADataHandler saveContainer] : 204 -> 156
~ -[DADataHandler copyOfAllLocalObjectsInContainer] : 204 -> 156
~ -[DADataHandler drainContainer] : 200 -> 152
~ -[DADataHandler wipeServerIds] : 204 -> 156
~ -[DADataHandler drainSuperfluousChanges] : 200 -> 152
~ -[DADataHandler openDB] : 200 -> 152
~ -[DADataHandler closeDBAndSave:] : 204 -> 156
~ +[DADataHandler newDataHandlerForDataclass:container:changeTrackingID:] : 204 -> 156
~ -[DADataHandler getDAObjectWithLocalItem:serverId:account:] : 204 -> 156
~ -[DADataHandler getDAExceptionObjectWithLocalItem:originalEvent:account:] : 204 -> 156
~ -[DAWaiterWrapper description] : 160 -> 152
~ -[DAWaiterWrapper setWaiter:] : 64 -> 12
~ +[DALocalDBGateKeeper sharedGateKeeper] : 84 -> 68
~ -[DALocalDBGateKeeper setEventsLockHolder:] : 112 -> 96
~ -[DALocalDBGateKeeper _canWakenWaiter:] : 212 -> 200
~ -[DALocalDBGateKeeper _abortWaiterForWrappers:] : 768 -> 744
~ -[DALocalDBGateKeeper _notifyWaitersForDataclasses:] : 860 -> 844
~ -[DALocalDBGateKeeper _registerWaiter:forDataclassLocks:preempt:completionHandler:] : 736 -> 716
~ -[DALocalDBGateKeeper _sendAllClearNotifications] : 304 -> 256
~ -[DALocalDBGateKeeper unregisterWaiterForDataclassLocks:] : 716 -> 692
~ -[DALocalDBGateKeeper relinquishLocksForWaiter:dataclasses:moreComing:] : 608 -> 532
~ -[DALocalDBGateKeeper claimedOwnershipOfDataclasses:] : 208 -> 160
~ -[DALocalDBGateKeeper stateString] : 208 -> 204
~ -[DALocalDBGateKeeper _setUnitTestHackRunLoopMode:] : 112 -> 96
~ -[DALocalDBGateKeeper setEventsWaiters:] : 64 -> 12
~ -[DALocalDBGateKeeper setWaiterIDsExpectingEventsLock:] : 64 -> 12
~ -[DALocalDBGateKeeper setUnitTestHackRunLoopMode:] : 64 -> 12
~ -[_DAContactsAccountContactsProvider accountWithExternalIdentifier:createIfNecessary:] : 304 -> 288
~ -[_DAContactsAccountContactsProvider allAccounts] : 392 -> 388
~ -[_DAContactsAccountContactsProvider accountForContainerWithIdentifier:] : 208 -> 192
~ -[_DAContactsAccountContactsProvider contactStore] : 16 -> 20
~ -[DATransaction dealloc] : 280 -> 224
~ -[DATransaction init] : 164 -> 148
~ -[DATransaction initWithLabel:] : 80 -> 88
~ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:] : 668 -> 624
~ __InfoForNotification : 92 -> 84
~ __ReceiveNotificationResponseCallback : 460 -> 388
~ __NotificationHandlerMap : 84 -> 68
~ ____NotificationHandlerMap_block_invoke : 68 -> 64
~ +[DAiCalendarLogger sharedLogger] : 84 -> 68
~ -[DAiCalendarLogger logICSMessage:atLevel:] : 204 -> 156
~ -[DAContactsAccountProvider accountWithExternalIdentifier:createIfNecessary:] : 68 -> 64
~ -[DAContactsAccountProvider allAccounts] : 64 -> 60
~ -[DAContactsAccountProvider accountForContainerWithIdentifier:] : 68 -> 64
~ -[DATrustHandler haveWarnedAboutCert:forHost:] : 120 -> 116
~ -[DATrustHandler setHaveWarnedAboutCert:forHost:] : 208 -> 204
~ -[DATrustHandler _actionForTrust:host:service:] : 380 -> 372
~ -[DATrustHandler _serverSuffixesToAlwaysFail] : 84 -> 68
~ -[DATrustHandler handleTrust:forHost:forAccount:withCompletionBlock:] : 2084 -> 1988
~ ___69-[DATrustHandler handleTrust:forHost:forAccount:withCompletionBlock:]_block_invoke : 172 -> 164
~ ___69-[DATrustHandler handleTrust:forHost:forAccount:withCompletionBlock:]_block_invoke.11 : 256 -> 252
~ ___69-[DATrustHandler handleTrust:forHost:forAccount:withCompletionBlock:]_block_invoke_2 : 304 -> 252
~ -[DATrustHandler handleTrustChallenge:forAccount:completionHandler:] : 348 -> 360
~ ___68-[DATrustHandler handleTrustChallenge:forAccount:completionHandler:]_block_invoke : 124 -> 120
~ ___68-[DATrustHandler handleTrustChallenge:forAccount:completionHandler:]_block_invoke_2 : 468 -> 448
~ ___68-[DATrustHandler handleTrustChallenge:forAccount:completionHandler:]_block_invoke.17 : 468 -> 404
~ -[DATrustHandler setHaveWarnedAboutCertDict:] : 64 -> 12
~ -[DAABLegacyAccount updateSaveRequest:] : 68 -> 64
~ -[DATrafficLogger _ensureCustomLogFile] : 180 -> 176
~ ___39-[DATrafficLogger _ensureCustomLogFile]_block_invoke : 132 -> 128
~ ___39-[DATrafficLogger _ensureCustomLogFile]_block_invoke_2 : 584 -> 560
~ -[DATrafficLogger logSnippet:] : 216 -> 212
~ -[DATrafficLogger slurpAndRemoveLookasideFile:prefixString:suffixString:] : 236 -> 240
~ ___73-[DATrafficLogger slurpAndRemoveLookasideFile:prefixString:suffixString:]_block_invoke : 96 -> 92
~ -[DATrafficLogger setFilename:] : 64 -> 12
~ -[DAContactsContainer identifier] : 84 -> 76
~ -[DAContactsContainer name] : 84 -> 76
~ -[DAContactsContainer setName:] : 100 -> 96
~ -[DAContactsContainer isLocal] : 64 -> 60
~ -[DAContactsContainer type] : 60 -> 56
~ -[DAContactsContainer setType:] : 84 -> 80
~ -[DAContactsContainer externalIdentifier] : 84 -> 76
~ -[DAContactsContainer setExternalIdentifier:] : 100 -> 96
~ -[DAContactsContainer cTag] : 84 -> 76
~ -[DAContactsContainer setCTag:] : 100 -> 96
~ -[DAContactsContainer syncTag] : 84 -> 76
~ -[DAContactsContainer setSyncTag:] : 100 -> 96
~ -[DAContactsContainer syncData] : 84 -> 76
~ -[DAContactsContainer setSyncData:] : 100 -> 96
~ -[DAContactsContainer constraintsPath] : 84 -> 76
~ -[DAContactsContainer setConstraintsPath:] : 100 -> 96
~ -[DAContactsContainer meContactidentifier] : 84 -> 76
~ -[DAContactsContainer setMeContactIdentifier:] : 100 -> 96
~ -[DAContactsContainer accountIdentifier] : 84 -> 76
~ -[DAContactsContainer setAccountIdentifier:] : 100 -> 96
~ -[DAContactsContainer isContentReadonly] : 84 -> 80
~ -[DAContactsContainer setContentReadonly:] : 136 -> 128
~ -[DAContactsContainer arePropertiesReadonly] : 84 -> 80
~ -[DAContactsContainer setArePropertiesReadonly:] : 144 -> 136
~ -[DAContactsContainer updateSaveRequest:] : 188 -> 180
~ -[DAContactsContainer asSource] : 64 -> 60
~ ___HandleForSource : 224 -> 220
~ _DAWeakLinkClass : 104 -> 100
~ +[DABabysitter sharedBabysitter] : 84 -> 68
~ -[DABabysitter _l_reloadBabysitterWaitersWithRefreshingWaitersPrefs:failedWaitersPrefs:restrictedWaitersPrefs:] : 3308 -> 3216
~ -[DABabysitter _reloadBabysitterProperties] : 664 -> 660
~ -[DABabysitter init] : 112 -> 108
~ -[DABabysitter _l_incrementRefreshCountForWaiterID:operationName:] : 420 -> 360
~ -[DABabysitter _incrementRefreshCountForWaiterID:operationName:] : 196 -> 200
~ -[DABabysitter _l_decrementRefreshCountForWaiter:forOperationWithName:] : 384 -> 360
~ -[DABabysitter _l_decrementRefreshCountForWaiterID:operationName:] : 600 -> 592
~ -[DABabysitter tokenByRegisteringAccount:forOperationWithName:] : 256 -> 260
~ -[DABabysitter unregisterAccount:forOperationWithName:] : 280 -> 276
~ -[DABabysitter accountWithIDShouldContinue:] : 500 -> 436
~ -[DABabysitter accountShouldContinue:] : 120 -> 116
~ -[DABabysitter _diagnosticReportWithWaiterID:failureCount:] : 376 -> 356
~ ___59-[DABabysitter _diagnosticReportWithWaiterID:failureCount:]_block_invoke : 200 -> 152
~ -[DABabysitter statusReportWithCompletionBlock:] : 292 -> 276
~ -[DABabysitter _populatedStringDictionaryWithWaitersDictionary:] : 464 -> 456
~ -[DABabysitter setBuildVersion:] : 64 -> 12
~ -[DABabysitter setL_refreshingWaiters:] : 64 -> 12
~ -[DABabysitter setL_failedWaiters:] : 64 -> 12
~ -[DABabysitter setL_restrictedWaiters:] : 64 -> 12
~ -[DAActivity initWithAccount:] : 116 -> 124
~ -[_DAContactsAccountABLegacyProvider initWithAddressBook:] : 100 -> 104
~ -[_DAContactsAccountABLegacyProvider dealloc] : 84 -> 88
~ -[_DAContactsAccountABLegacyProvider accountForContainerWithIdentifier:] : 260 -> 256
~ -[_DAContactsAccountABLegacyProvider addressBook] : 16 -> 20
~ ___64-[DATransactionMonitor decrementTransactionCountForTransaction:]_block_invoke.cold.1 : 136 -> 132
~ +[DAAccountLoader _findPrivateFrameworks].cold.1 : 180 -> 172
~ -[DAAction initWithCoder:].cold.1 : 84 -> 80
~ -[DAAction encodeWithCoder:].cold.1 : 84 -> 80
~ -[DAMoveAction initWithCoder:].cold.1 : 84 -> 80
~ -[DAMoveAction encodeWithCoder:].cold.1 : 84 -> 80
~ -[DAResponse initWithCoder:].cold.1 : 84 -> 80
~ -[DAResponse encodeWithCoder:].cold.1 : 84 -> 80
~ _flockWithProcessAssertion.cold.2 : 148 -> 140
~ -[DATaskManager taskRequestModal:].cold.1 : 96 -> 92
~ -[DATaskManager _startModal:].cold.1 : 96 -> 92
~ -[DATaskManager _makeStateTransition].cold.1 : 96 -> 92
~ -[DATaskManager _makeStateTransition].cold.2 : 96 -> 92
~ -[DATaskManager _makeStateTransition].cold.3 : 96 -> 92
~ -[DATaskManager _makeStateTransition].cold.4 : 96 -> 92
~ -[DATaskManager _makeStateTransition].cold.5 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.6 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.7 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.8 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.9 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.10 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.11 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.12 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.13 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.14 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.15 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.16 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.17 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.18 : 80 -> 76
~ -[DATaskManager _makeStateTransition].cold.19 : 80 -> 76
~ -[DAPowerAssertionManager powerAssertionRetainCount:].cold.1 : 88 -> 84
~ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:].cold.1 : 88 -> 84
~ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:].cold.2 : 116 -> 112
~ -[DAPowerAssertionManager releasePowerAssertion:].cold.1 : 88 -> 84
~ -[DADataHandler initWithContainer:changeTrackingID:].cold.1 : 120 -> 116
~ -[DALocalDBGateKeeper dealloc].cold.1 : 108 -> 104
~ -[DALocalDBGateKeeper dealloc].cold.2 : 108 -> 104
~ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.1 : 92 -> 88
~ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.2 : 92 -> 88
~ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.3 : 92 -> 88
~ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.4 : 132 -> 128
CStrings:
- "#16@0:8"
- "#24@0:8@16"
- ".cxx_destruct"
- "@\"<DADataclassLockWatcher>\""
- "@\"<DATask>\""
- "@\"<DATransactionMonitorDelegate>\""
- "@\"<DATrustHandlerDelegate>\""
- "@\"ACAccount\""
- "@\"CNAccount\""
- "@\"CNContactStore\""
- "@\"CNContainer\"16@0:8"
- "@\"CNMutableContainer\""
- "@\"DAAccount\""
- "@\"DAActivity\""
- "@\"DAFolder\"16@0:8"
- "@\"DAMailMessage\""
- "@\"DAMessageMoveRequest\""
- "@\"DAStatusReport\""
- "@\"DATaskManager\""
- "@\"DATransaction\""
- "@\"DATrustHandler\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCountedSet\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\""
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\"24@0:8^@16"
- "@\"NSSet\"32@0:8q16^@24"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"40@0:8@\"NSData\"16@\"NSString\"24^@32"
- "@\"NSTimer\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^v16"
- "@24@0:8^{__CFURLStorageSession=}16"
- "@24@0:8i16i20"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@32@0:8^v16@24"
- "@32@0:8i16@20B28"
- "@32@0:8i16@20i28"
- "@32@0:8q16^@24"
- "@36@0:8@16i24B28B32"
- "@36@0:8i16@20@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16q24@32"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16Q24@32"
- "@40@0:8^v16@24@32"
- "@40@0:8q16^v24@32"
- "@44@0:8@16@24i32@36"
- "@48@0:8@16@24Q32@40"
- "@48@0:8@16B24B28@32@40"
- "@48@0:8Q16@24@32@40"
- "@48@0:8Q16@24@32q40"
- "@48@0:8i16@20@28@36i44"
- "@52@0:8@16@24@32i40@44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8Q16@24@32@40@48"
- "@?"
- "@?16@0:8"
- "ASAccountActor"
- "ASAccountActorMessages"
- "AuthenticationExtensions"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"NSData\"16@\"NSString\"24"
- "B32@0:8@16@24"
- "B32@0:8@16@?24"
- "B36@0:8@16@24i32"
- "B40@0:8@\"NSSet\"16@\"NSSet\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B44@0:8@16@24@32i40"
- "CDVIsSafeRedirectForRequestURL:"
- "CDVObjectForKeyCaseInsensitive:"
- "CDVRawPath"
- "ChillOutARC"
- "CoreDAVLogging"
- "DAABLegacyAccount"
- "DAABLegacyContainer"
- "DAAccount"
- "DAAccountClassNames"
- "DAAccountLoader"
- "DAAccountMonitor"
- "DAAction"
- "DAActivity"
- "DABabysitterRegistrationToken"
- "DACardDAVRecord"
- "DACompactDescription"
- "DAContactsAccount"
- "DAContactsAccountProvider"
- "DAContactsBasedAccount"
- "DAContactsContainer"
- "DAContainer"
- "DADAExtendedDescription"
- "DADataHandler"
- "DADraftMessageRequest"
- "DAExtendedDescription"
- "DAExtensions"
- "DAFolder"
- "DAHexString"
- "DAKeychain"
- "DAKeychainAddition"
- "DAKeychainAdditions"
- "DALeastInfoURLExtension"
- "DALocalDBGateKeeper"
- "DAMailMessage"
- "DAMailboxDeleteMessageRequest"
- "DAMailboxFetchMessageRequest"
- "DAMailboxFetchSearchResultRequest"
- "DAMailboxGetUpdatesRequest"
- "DAMailboxRequest"
- "DAMailboxSetFlagsRequest"
- "DAManagedDefaultForKey:"
- "DAMergeOverrideDictionary:"
- "DAMessageFetchAttachmentRequest"
- "DAMessageMoveRequest"
- "DAMoveAction"
- "DAMoveResponse"
- "DAObjectForKeyCaseInsensitive:"
- "DAPowerAssertionManager"
- "DARequestByApplyingStorageSession:"
- "DAResolveRecipientsRequest"
- "DAResolvedRecipient"
- "DAResponse"
- "DARunLoopRegistry"
- "DATaskManager"
- "DATrafficLogger"
- "DATransaction"
- "DATransactionMonitor"
- "DATrustHandler"
- "DAUserNotificationInfo"
- "DAUserNotificationUtilities"
- "DAWaiterWrapper"
- "DAiCalendarLogger"
- "DelayedPerformWithNullSource"
- "Email"
- "EventsFolderItemsSyncContext"
- "EventsSupport"
- "HSA2Support"
- "ICSLoggingDelegate"
- "InvitationSupport"
- "MailFolder"
- "MailFolderSupport"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "OAuth2Token"
- "OldAndBusted"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "SearchSubclassing"
- "Searching"
- "T#,R"
- "T@\"<DADataclassLockWatcher>\",&,N,V_eventsLockHolder"
- "T@\"<DADataclassLockWatcher>\",&,N,V_waiter"
- "T@\"<DATask>\",&,N,V_activeExclusiveTask"
- "T@\"<DATask>\",&,N,V_activeModalTask"
- "T@\"<DATask>\",&,N,V_activeQueuedTask"
- "T@\"<DATask>\",&,N,V_modalHeldActiveQueuedTask"
- "T@\"<DATransactionMonitorDelegate>\",W,N,V_transactionMonitorDelegate"
- "T@\"<DATrustHandlerDelegate>\",W,N,V_delegate"
- "T@\"ACAccount\",R,N,V_backingAccountInfo"
- "T@\"CNAccount\",R,N,V_account"
- "T@\"CNContactStore\",R,N,V_contactStore"
- "T@\"CNMutableContainer\",R,N,V_mutableContainer"
- "T@\"DAAccount\",W,N,V_account"
- "T@\"DAMailMessage\",&,N,V_message"
- "T@\"DAMessageMoveRequest\",&,N,V_origRequest"
- "T@\"DAStatusReport\",&,N,V_statusReport"
- "T@\"DATaskManager\",R,N,V_taskManager"
- "T@\"DATrustHandler\",&,N,V_trustHandler"
- "T@\"NSArray\",&,N,V_emailAddresses"
- "T@\"NSArray\",C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_appIdsForPasswordPrompt"
- "T@\"NSCountedSet\",&,N,V_contexts"
- "T@\"NSCountedSet\",&,N,V_heldAsideContexts"
- "T@\"NSData\",&,N"
- "T@\"NSData\",R,C,N"
- "T@\"NSDate\",&,N,V_endTime"
- "T@\"NSDate\",&,N,V_lastQueryStartedTime"
- "T@\"NSDate\",&,N,V_startTime"
- "T@\"NSDictionary\",R,N"
- "T@\"NSHashTable\",&,N,V_accounts"
- "T@\"NSMapTable\",&,N,V_contextToGroupIdentifier"
- "T@\"NSMapTable\",&,N,V_contextToPowerAssertionRef"
- "T@\"NSMapTable\",&,N,V_groupIdentifierToContexts"
- "T@\"NSMutableArray\",&,N,V_eventsWaiters"
- "T@\"NSMutableArray\",&,N,V_mQueuedTasks"
- "T@\"NSMutableArray\",&,N,V_pendingQueries"
- "T@\"NSMutableArray\",&,N,V_queuedExclusiveTasks"
- "T@\"NSMutableArray\",&,N,V_queuedModalTasks"
- "T@\"NSMutableArray\",&,N,V_transactions"
- "T@\"NSMutableDictionary\",&,N,V_acAccountTypeToAccountDaemonBundleSubpath"
- "T@\"NSMutableDictionary\",&,N,V_acAccountTypeToAccountFrameworkSubpath"
- "T@\"NSMutableDictionary\",&,N,V_acAccountTypeToClassNames"
- "T@\"NSMutableDictionary\",&,N,V_acParentAccountTypeToChildAccountTypes"
- "T@\"NSMutableDictionary\",&,N,V_dataclassPropertyURLsByDataclass"
- "T@\"NSMutableDictionary\",&,N,V_haveWarnedAboutCertDict"
- "T@\"NSMutableDictionary\",&,N,V_l_failedWaiters"
- "T@\"NSMutableDictionary\",&,N,V_l_refreshingWaiters"
- "T@\"NSMutableDictionary\",&,N,V_l_restrictedWaiters"
- "T@\"NSMutableDictionary\",&,N,V_mResolvedEmailToX509Certs"
- "T@\"NSMutableSet\",&,N,V_heldAsideGroupIdentifiers"
- "T@\"NSMutableSet\",&,N,V_heldIndependentTasks"
- "T@\"NSMutableSet\",&,N,V_independentTasks"
- "T@\"NSMutableSet\",&,N,V_modalHeldIndependentTasks"
- "T@\"NSMutableSet\",&,N,V_waiterIDsExpectingEventsLock"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_accountsQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_pendingQueryQueue"
- "T@\"NSObject<OS_dispatch_queue>\",N,V_callbackQueue"
- "T@\"NSRunLoop\",R,N"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_accountClassName"
- "T@\"NSString\",&,N,V_agentClassName"
- "T@\"NSString\",&,N,V_buildVersion"
- "T@\"NSString\",&,N,V_clientAccountClassName"
- "T@\"NSString\",&,N,V_daemonAccountClassName"
- "T@\"NSString\",&,N,V_destinationContainerId"
- "T@\"NSString\",&,N,V_filename"
- "T@\"NSString\",&,N,V_mergedFreeBusy"
- "T@\"NSString\",&,N,V_sourceContainerId"
- "T@\"NSString\",&,N,V_sourceServerId"
- "T@\"NSString\",&,N,V_unitTestHackRunLoopMode"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_attachmentName"
- "T@\"NSString\",C,N,V_changeTrackingID"
- "T@\"NSString\",C,N,V_destID"
- "T@\"NSString\",C,N,V_folderID"
- "T@\"NSString\",C,N,V_folderName"
- "T@\"NSString\",C,N,V_fromFolder"
- "T@\"NSString\",C,N,V_groupIdentifier"
- "T@\"NSString\",C,N,V_longID"
- "T@\"NSString\",C,N,V_message"
- "T@\"NSString\",C,N,V_messageID"
- "T@\"NSString\",C,N,V_parentFolderID"
- "T@\"NSString\",C,N,V_powerAssertionGroupID"
- "T@\"NSString\",C,N,V_serverID"
- "T@\"NSString\",C,N,V_sourceApplicationBundleIdentifier"
- "T@\"NSString\",C,N,V_sourceID"
- "T@\"NSString\",C,N,V_toFolder"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_label"
- "T@\"NSString\",R,N,V_transactionId"
- "T@\"NSTimer\",&,N,V_managerIdleTimer"
- "T@\"NSTimer\",&,N,V_powerLogIdleTimer"
- "T@\"NSTimer\",&,N,V_userInitiatedSyncTimer"
- "T@\"NSTimer\",&,N,V_xpcTransactionTimer"
- "T@\"NSURL\",C,N"
- "T@,&,N,S_setChangedItem:,V_changedItem"
- "T@,&,N,V_context"
- "T@,&,N,V_forwardedAttendeeUUIDs"
- "T@,&,N,V_forwardedAttendees"
- "T@,&,N,V_instanceId"
- "T@,&,N,V_serverId"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_handler"
- "T@?,C,N,V_unregisterBlock"
- "TB,N"
- "TB,N,V_claimedOwnershipOfEvents"
- "TB,N,V_didLogSyncStart"
- "TB,N,V_hasRemoteChanges"
- "TB,N,V_isDefault"
- "TB,N,V_isValidating"
- "TB,N,V_markedAsDefault"
- "TB,N,V_markedForDeletion"
- "TB,N,V_retrieveAvailablilty"
- "TB,N,V_retrieveCertificates"
- "TB,N,V_send"
- "TB,N,V_shouldUseOpportunisticSockets"
- "TB,N,V_wasUserInitiated"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_shouldFailAllTasks"
- "TQ,N,V_itemChangeType"
- "TQ,N,V_offFlags"
- "TQ,N,V_onFlags"
- "TQ,R"
- "T^v,N,V_container"
- "T^v,R,N,V_account"
- "T^v,R,N,V_addressBook"
- "T^v,R,N,V_source"
- "Ti,N,SsetDAAccountVersion:"
- "Ti,N,V_bodyFormat"
- "Ti,N,V_calAlarmChangeId"
- "Ti,N,V_calAttachmentChangeId"
- "Ti,N,V_calAttendeeChangeId"
- "Ti,N,V_calEventChangeId"
- "Ti,N,V_calRecurrenceChangeId"
- "Ti,N,V_changeId"
- "Ti,N,V_highestSequenceNumber"
- "Ti,N,V_maxSize"
- "Ti,N,V_requestType"
- "Ti,N,V_state"
- "Ti,N,V_status"
- "Ti,N,V_transactionCount"
- "Ti,R,N"
- "Ti,R,N,V_waiterNum"
- "Tq,N"
- "Tq,N,V_availabilityStatus"
- "Tq,N,V_certificatesStatus"
- "Tq,N,V_dataclass"
- "Tq,N,V_dataclasses"
- "Tq,N,V_status"
- "Tq,R,N"
- "TrustHandling"
- "T{os_unfair_lock_s=I},R,N,V_lock"
- "URLByRemovingLastPathComponent"
- "URLWithString:"
- "URLWithString:relativeToURL:"
- "URLWithUsername:"
- "URLWithUsername:withPassword:"
- "URLWithoutUsername"
- "UTF8String"
- "Vv16@0:8"
- "Vv20@0:8B16"
- "Vv20@0:8i16"
- "Vv24@0:8@\"DASearchQuery\"16"
- "Vv24@0:8@\"NSArray\"16"
- "Vv24@0:8@\"NSData\"16"
- "Vv24@0:8@\"NSNotification\"16"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@16"
- "Vv28@0:8@\"NSArray\"16B24"
- "Vv28@0:8@16B24"
- "^v"
- "^v16@0:8"
- "^v20@0:8i16"
- "^{_NSZone=}16@0:8"
- "^{__CFData=}24@0:8@16"
- "^{__CFDictionary=}24@0:8@16"
- "^{__CFDictionary=}28@0:8@16i24"
- "^{__CFURLStorageSession=}"
- "^{__CFURLStorageSession=}16@0:8"
- "_CFURLRequest"
- "_DAContactsAccountABLegacyProvider"
- "_DAContactsAccountContactsProvider"
- "_DACopyMutableAttributesForAccountWithPersistentUUID:accessibility:"
- "_DACopyMutableQueryForAccountWithPersistentUUID:"
- "_abortWaiterForWrappers:"
- "_acAccountTypeToAccountDaemonBundleSubpath"
- "_acAccountTypeToAccountFrameworkSubpath"
- "_acAccountTypeToClassNames"
- "_acParentAccountTypeToChildAccountTypes"
- "_account"
- "_accountClassName"
- "_accountPasswordChanged"
- "_accounts"
- "_accountsQueue"
- "_actionForTrust:host:service:"
- "_activeExclusiveTask"
- "_activeModalTask"
- "_activeQueuedTask"
- "_addAccountInfo:forFrameworkNamed:"
- "_addressBook"
- "_agentClassName"
- "_appIdsForPasswordPrompt"
- "_attachmentName"
- "_availabilityStatus"
- "_backingAccountInfo"
- "_bodyFormat"
- "_buildVersion"
- "_calAlarmChangeId"
- "_calAttachmentChangeId"
- "_calAttendeeChangeId"
- "_calEventChangeId"
- "_calRecurrenceChangeId"
- "_callbackQueue"
- "_canWakenWaiter:"
- "_cancelTasksWithReason:"
- "_certificatesStatus"
- "_changeId"
- "_changeTrackingID"
- "_changedItem"
- "_claimedOwnershipOfEvents"
- "_clearUserInitiatedSyncTimer"
- "_clientAccountClassName"
- "_clientToken"
- "_completionHandler"
- "_consumers"
- "_contactStore"
- "_container"
- "_context"
- "_contextToGroupIdentifier"
- "_contextToPowerAssertionRef"
- "_contexts"
- "_continueCount"
- "_daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:"
- "_daActivity"
- "_daKeychainAccessibilityForSecAccessibility:"
- "_daemonAccountClassName"
- "_daemonDiedNotification:"
- "_dataclass"
- "_dataclassPropertyURLsByDataclass"
- "_dataclasses"
- "_delegate"
- "_dequeueQuery"
- "_destID"
- "_destinationContainerId"
- "_diagnosticReportWithWaiterID:failureCount:"
- "_didLogSyncStart"
- "_emailAddresses"
- "_endTime"
- "_endXpcTransaction"
- "_ensureCustomLogFile"
- "_eventsLockHolder"
- "_eventsWaiters"
- "_filename"
- "_findPrivateFrameworks"
- "_folderHierarchyChanged"
- "_folderID"
- "_folderName"
- "_folderUpdatedNotification:"
- "_foldersThatExternalClientsCareAboutChanged"
- "_forwardedAttendeeUUIDs"
- "_forwardedAttendees"
- "_fromFolder"
- "_groupIdentifier"
- "_groupIdentifierToContexts"
- "_handler"
- "_hasInitted"
- "_hasRemoteChanges"
- "_hasTasksForcingNetworkConnection"
- "_hasTasksIndicatingARunningSync"
- "_haveWarnedAboutCertDict"
- "_heldAsideContexts"
- "_heldAsideGroupIdentifiers"
- "_heldIndependentTasks"
- "_highestSequenceNumber"
- "_incrementRefreshCountForWaiterID:operationName:"
- "_independentTasks"
- "_init"
- "_initWithCFURLRequest:"
- "_instanceId"
- "_isDefault"
- "_isFetchingAutomatically"
- "_isIdentityManagedByProfile"
- "_isValidating"
- "_itemChangeType"
- "_l_decrementRefreshCountForWaiter:forOperationWithName:"
- "_l_decrementRefreshCountForWaiterID:operationName:"
- "_l_failedWaiters"
- "_l_giveAccountWithIDAnotherChance:"
- "_l_incrementRefreshCountForWaiterID:operationName:"
- "_l_refreshingWaiters"
- "_l_reloadBabysitterWaitersWithRefreshingWaitersPrefs:failedWaitersPrefs:restrictedWaitersPrefs:"
- "_l_restrictedWaiters"
- "_label"
- "_lastQueryStartedTime"
- "_leafAccountTypes"
- "_loadFrameworkAtSubpath:"
- "_lock"
- "_logSyncEnd"
- "_longID"
- "_mQueuedTasks"
- "_mResolvedEmailToX509Certs"
- "_makeStateTransition"
- "_managerIdleTimer"
- "_markedAsDefault"
- "_markedForDeletion"
- "_maxSize"
- "_mergedFreeBusy"
- "_message"
- "_messageID"
- "_modalHeldActiveQueuedTask"
- "_modalHeldIndependentTasks"
- "_mutableContainer"
- "_newASPolicyKeyNotification:"
- "_notifyWaitersForDataclasses:"
- "_offFlags"
- "_onFlags"
- "_origRequest"
- "_parentFolderID"
- "_pendingQueries"
- "_pendingQueryQueue"
- "_performTask:"
- "_populateVersionDescriptions"
- "_populatedStringDictionaryWithWaitersDictionary:"
- "_powerAssertionGroupID"
- "_powerLogIdleTimer"
- "_powerLogInfoDictionary"
- "_queuedExclusiveTasks"
- "_queuedModalTasks"
- "_reactivateHeldTasks"
- "_reallyCancelAllSearchQueries"
- "_reallyCancelPendingSearchQuery:"
- "_reallyCancelSearchQuery:"
- "_reallyPerformSearchQuery:"
- "_reallySearchQueriesRunning"
- "_registerWaiter:forDataclassLocks:preempt:completionHandler:"
- "_releaseAssertionForContext:"
- "_releasePowerAssertionForTask:"
- "_reloadBabysitterProperties"
- "_requestCancelTasksWithReason:"
- "_requestType"
- "_retainAssertionForContext:"
- "_retainPowerAssertionForTask:"
- "_retrieveAvailablilty"
- "_retrieveCertificates"
- "_schedulePerformTask:"
- "_scheduleSelector:withArgument:"
- "_scheduleStartModal:"
- "_secAccessibilityForDAKeychainAccessibility:"
- "_send"
- "_sendAllClearNotifications"
- "_serverID"
- "_serverId"
- "_serverSuffixesToAlwaysFail"
- "_setChangedItem:"
- "_setPersistentUUID:"
- "_setUnitTestHackRunLoopMode:"
- "_shouldFailAllTasks"
- "_shouldUseOpportunisticSockets"
- "_source"
- "_sourceApplicationBundleIdentifier"
- "_sourceContainerId"
- "_sourceID"
- "_sourceServerId"
- "_startModal:"
- "_startTime"
- "_state"
- "_status"
- "_statusReport"
- "_storageSession"
- "_taskForcesNetworking:"
- "_taskInQueueForcesNetworkConnection:"
- "_taskManager"
- "_toFolder"
- "_transaction"
- "_transactionCount"
- "_transactionId"
- "_transactionMonitorDelegate"
- "_transactions"
- "_trustHandler"
- "_unitTestHackRunLoopMode"
- "_unregisterBlock"
- "_useFakeDescriptions"
- "_useOpportunisticSocketsAgain"
- "_userInitiatedSyncTimer"
- "_version"
- "_waiter"
- "_waiterIDsExpectingEventsLock"
- "_waiterNum"
- "_wasUserInitiated"
- "_webLoginRequestedAtURL:reasonString:inQueue:completionBlock:"
- "_xpcActivity"
- "_xpcTransactionTimer"
- "aa_isSuspended"
- "absoluteString"
- "absoluteURL"
- "acAccountTypeToAccountDaemonBundleSubpath"
- "acAccountTypeToAccountFrameworkSubpath"
- "acAccountTypeToClassNames"
- "acParentAccountTypeToChildAccountTypes"
- "account"
- "account:isValid:validationError:"
- "accountBoolPropertyForKey:"
- "accountClassForACAccount:"
- "accountClassName"
- "accountContainsEmailAddress:"
- "accountDescription"
- "accountDidChangeFromOldAccountInfo:"
- "accountForContainerWithIdentifier:"
- "accountHasSignificantPropertyChangesFromOldAccountInfo:"
- "accountID"
- "accountIdentifier"
- "accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:"
- "accountIntPropertyForKey:"
- "accountPersistentUUID"
- "accountPropertyForKey:"
- "accountShouldContinue:"
- "accountType"
- "accountTypeIdentifier"
- "accountTypeWithAccountTypeIdentifier:"
- "accountTypeWithIdentifier:completion:"
- "accountWithExternalIdentifier:createIfNecessary:"
- "accountWithIDShouldContinue:"
- "accountWithIdentifier:"
- "accountWithIdentifier:completion:"
- "accounts"
- "accountsMatchingPredicate:error:"
- "accountsQueue"
- "accountsWithAccountType:"
- "accountsWithAccountType:completion:"
- "accountsWithAccountTypeIdentifiers:error:"
- "actionForTrust:forHost:andService:"
- "activeExclusiveTask"
- "activeModalTask"
- "activeQueuedTask"
- "addAccount:"
- "addCert:forEmailAddress:"
- "addClientToken:"
- "addObject:"
- "addObjectsFromArray:"
- "addTimer:forMode:"
- "addToCoreDAVLoggingDelegates"
- "addUsernameToURL:"
- "additionalHeaderValues"
- "addressBook"
- "agentClassForACAccount:"
- "agentClassName"
- "allAccounts"
- "allKeys"
- "allObjects"
- "allTasks"
- "allValues"
- "allowTrust:forHost:service:"
- "allowsKeyedCoding"
- "appIdsForPasswordPrompt"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "arePropertiesReadonly"
- "array"
- "arrayWithArray:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "asContainer"
- "asSource"
- "attachmentName"
- "attachments"
- "autodiscoverAccountConfigurationWithConsumer:"
- "autorelease"
- "availabilityStatus"
- "babysitterEnabled"
- "backingAccountInfo"
- "bcc"
- "beginDownloadingAttachmentWithUUID:consumer:"
- "body"
- "bodyFormat"
- "bodySize"
- "bodyTruncated"
- "bodyType"
- "boolForKey:"
- "boolValue"
- "buildVersion"
- "bundleForClass:"
- "bundleWithPath:"
- "bytes"
- "cTag"
- "calAlarmChangeId"
- "calAttachmentChangeId"
- "calAttendeeChangeId"
- "calEventChangeId"
- "calRecurrenceChangeId"
- "calendarAvailabilityRequestFinishedWithError:"
- "calendarDirectorySearchFinishedWithError:exceededResultLimit:"
- "callbackQueue"
- "canAccessCredentialsWithAccessibility:"
- "cancelAllSearchQueries"
- "cancelAllTasks"
- "cancelCalendarAvailabilityRequestWithID:"
- "cancelCalendarDirectorySearchWithID:"
- "cancelDownloadingInstance:error:"
- "cancelPreviousPerformRequestsWithTarget:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "cancelSearchQuery:"
- "cancelShareResponseInstance:error:"
- "cancelTask:"
- "cancelTask:withUnderlyingError:"
- "cancelTaskWithID:"
- "cancelTaskWithReason:underlyingError:"
- "cancelTasksDueToOnPowerMode"
- "caseInsensitiveCompare:"
- "cc"
- "certificatesStatus"
- "changeId"
- "changeTrackingID"
- "changedItem"
- "characterAtIndex:"
- "characterIsMember:"
- "characterSetWithCharactersInString:"
- "checkValidityOnAccountStore:withConsumer:"
- "checkValidityOnAccountStore:withConsumer:inQueue:"
- "claimedOwnershipOfDataclasses:"
- "claimedOwnershipOfEvents"
- "class"
- "cleanupAccountFiles"
- "clientAccountClassForACAccount:"
- "clientAccountClassName"
- "clientID"
- "clientToken"
- "clientTokenRequestedByServer"
- "closeDBAndSave:"
- "code"
- "completionHandler"
- "conformsToProtocol:"
- "constraintsPath"
- "consumer"
- "consumerForTask:"
- "contactStore"
- "container"
- "containsObject:"
- "contentsOfDirectoryAtPath:error:"
- "context"
- "contextToGroupIdentifier"
- "contextToPowerAssertionRef"
- "contexts"
- "continueWithoutCredentialForAuthenticationChallenge:"
- "conversationId"
- "conversationIndex"
- "copy"
- "copyLocalObjectFromId:"
- "copyOfAllLocalObjectsInContainer"
- "copyStorageSession"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "credential"
- "credentialItemForKey:"
- "credentialProtectionPolicy"
- "credentialType"
- "currentHandler"
- "currentMode"
- "currentRunLoop"
- "customConnectionProperties"
- "customSignature"
- "daAccountSubclassWithBackingAccountInfo:"
- "daAccountVersion"
- "da_URLWithDirtyString:"
- "da_URLWithScheme:host:port:uri:"
- "da_URLWithScheme:host:user:port:uri:"
- "da_absoluteURLForChildLeastInfoRepresentationRelativeToParentURL:"
- "da_accounts"
- "da_accountsEnabledForDADataclasses:"
- "da_accountsWithAccountTypeIdentifiers:"
- "da_accountsWithAccountTypeIdentifiers:enabledForDADataclasses:"
- "da_accountsWithAccountTypeIdentifiers:outError:"
- "da_addNullRunLoopSourceAndPerformSelector:withObject:afterDelay:inModes:"
- "da_appendSlashIfNeeded"
- "da_classicPortForScheme:"
- "da_dataWithHexString:"
- "da_dataWithHexString:stringIsUppercase:"
- "da_hasPrefixCaseInsensitive:"
- "da_hexString"
- "da_isEqualToDAVURL:"
- "da_leastInfoStringRepresentationRelativeToParentURL:"
- "da_loadDAAccountsEnabledForDADataclasses:withCompletion:"
- "da_loadDAAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:withCompletion:"
- "da_loadDAAccountsWithAccountTypeIdentifiers:withCompletion:"
- "da_loadDAAccountsWithCompletion:"
- "da_lowercaseHexStringWithoutSpaces"
- "da_new64ByteGUID"
- "da_newGUID"
- "da_pathWithoutTrailingRemovingSlash"
- "da_performSelectorThatDoesntAffectRetainCount:withObject:"
- "da_rawPath"
- "da_removeSlashIfNeeded"
- "da_stringByAddingPercentEscapesForUsername"
- "da_stringByRemovingPercentEscapesForUsername"
- "da_stringByURLEscapingPathComponent"
- "da_trimWhiteSpace"
- "da_uppercaseHexStringWithoutSpaces"
- "da_urlByRemovingUsername"
- "da_urlBySettingHost:"
- "da_urlBySettingHost:keepUsername:"
- "da_urlBySettingPath:"
- "da_urlBySettingPath:keepUsername:"
- "da_urlBySettingPort:"
- "da_urlBySettingPort:keepUsername:"
- "da_urlBySettingScheme:"
- "da_urlBySettingScheme:keepUsername:"
- "da_urlBySettingUsername:"
- "da_urlForLogging"
- "daemonAccountClassForACAccount:"
- "daemonAccountClassName"
- "daemonAppropriateAccountClassForACAccount:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "dataclass"
- "dataclassProperties"
- "dataclassPropertyURLsByDataclass"
- "dataclasses"
- "date"
- "dateWithCalendarFormat:timeZone:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeIntForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decrementTransactionCountForTransaction:"
- "decrementXpcActivityContinueCount"
- "defaultContainerIdentifierForDADataclass:"
- "defaultEventsFolder"
- "defaultManager"
- "defaultStore"
- "defaultTrustManager"
- "delegate"
- "deleteContainer:"
- "deletedItemsFolder"
- "description"
- "destID"
- "destinationContainerId"
- "deviceType"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "didFinishAllXPCTransactions"
- "didLogSyncStart"
- "discoverInitialPropertiesWithConsumer:"
- "displayAccount"
- "displayName"
- "displayTo"
- "distantPast"
- "domain"
- "domainOnly"
- "doubleValue"
- "downloadFinishedError:"
- "draftsFolder"
- "drainContainer"
- "drainSuperfluousChanges"
- "dropAssertionsAndRenewCredentialsInQueue:withHandler:"
- "dropPowerAssertionsForGroupIdentifier:"
- "emailAddress"
- "emailAddresses"
- "enabled"
- "enabledDataclasses"
- "enabledDataclassesBitmask"
- "enabledForAnyDADataclasses:"
- "enabledForDADataclass:"
- "encodeInt:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedHeaders"
- "encryptionIdentityPersistentReference"
- "endTime"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "eventsFolders"
- "eventsLockHolder"
- "eventsWaiters"
- "exceptionWithName:reason:userInfo:"
- "exceptionsDict"
- "exceptionsForDigest:"
- "externalIdentifier"
- "externalIdentifierString"
- "externalModificationTag"
- "externalSyncData"
- "externalSyncTag"
- "fileSystemRepresentation"
- "filename"
- "firstObject"
- "flagged"
- "flaggedIsSet"
- "folderID"
- "folderIDsThatExternalClientsCareAboutForDataclasses:withTag:"
- "folderIDsThatExternalClientsCareAboutWithTag:"
- "folderName"
- "foldersTag"
- "forwardedAttendeeUUIDs"
- "forwardedAttendees"
- "from"
- "fromFolder"
- "generatesBulletins"
- "getAppleIDSession"
- "getCFRunLoop"
- "getDAExceptionObjectWithLocalItem:originalEvent:account:"
- "getDAObjectWithLocalItem:serverId:account:"
- "getFetchingAutomaticallyState"
- "getIdFromLocalObject:"
- "getPendingQueryQueue"
- "giveAccountWithIDAnotherChance:"
- "groupIdentifier"
- "groupIdentifierToContexts"
- "guessPasswordForURL:"
- "handleCertificateError:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleTrust:forHost:forAccount:withCompletionBlock:"
- "handleTrustChallenge:"
- "handleTrustChallenge:completionHandler:"
- "handleTrustChallenge:forAccount:"
- "handleTrustChallenge:forAccount:completionHandler:"
- "handleValidationError:completion:"
- "handler"
- "hasPrefix:"
- "hasRemoteChanges"
- "hasSuffix:"
- "hasXpcActivity"
- "hash"
- "haveWarnedAboutCert:forHost:"
- "haveWarnedAboutCertDict"
- "heldAsideContexts"
- "heldAsideGroupIdentifiers"
- "heldIndependentTasks"
- "highestSequenceNumber"
- "host"
- "hostFromDataclassPropertiesForDataclass:"
- "i16@0:8"
- "i24@0:8@16"
- "i24@0:8^v16"
- "i32@0:8@\"DAMessageFetchAttachmentRequest\"16@\"<DAMessageFetchAttachmentConsumer>\"24"
- "i32@0:8@\"DAResolveRecipientsRequest\"16@\"<DAResolveRecipientsConsumer>\"24"
- "i32@0:8@\"NSArray\"16@\"<DAMailboxFetchSearchResultConsumer>\"24"
- "i32@0:8@\"NSArray\"16@\"<DAMessageMoveRequestConsumer>\"24"
- "i32@0:8@16@24"
- "i40@0:8^{__SecTrust=}16@24@32"
- "i52@0:8@\"DAMailboxRequest\"16@\"NSString\"24@\"NSString\"32B40@\"<DAMailboxRequestConsumer>\"44"
- "i52@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32B40@\"<DAMailboxRequestConsumer>\"44"
- "i52@0:8@16@24@32B40@44"
- "i56@0:8@\"DAMailboxRequest\"16@\"NSString\"24@\"NSString\"32B40B44@\"<DAMailboxRequestConsumer>\"48"
- "i56@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32B40B44@\"<DAMailboxRequestConsumer>\"48"
- "i56@0:8@16@24@32B40B44@48"
- "i92@0:8@\"NSData\"16@\"NSString\"24i32@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSString\"60B68B72@\"<DAMessageSendConsumer>\"76@84"
- "i92@0:8@16@24i32@36@44@52@60B68B72@76@84"
- "iOSLegacyIdentifier"
- "identifier"
- "identityPersist"
- "importance"
- "inboxFolder"
- "incrementTransactionCountForTransaction:"
- "incrementXpcActivityContinueCount"
- "independentTasks"
- "infoDictionary"
- "ingestBackingAccountInfoProperties"
- "init"
- "initMoveRequestWithMessage:fromFolder:toFolder:"
- "initRequestForBodyFormat:withBodySizeLimit:"
- "initRequestForBodyFormat:withFolderID:withServerID:withLongID:withBodySizeLimit:"
- "initRequestForBodyFormat:withLongID:withBodySizeLimit:"
- "initRequestForBodyFormat:withMessageID:withBodySizeLimit:"
- "initRequestWithMessageID:"
- "initRequestWithSetFlags:unsetFlags:message:"
- "initWithABAccout:"
- "initWithABSource:"
- "initWithAccount:"
- "initWithAddressBook:"
- "initWithAttachmentName:andMessageServerID:"
- "initWithBackingAccountInfo:"
- "initWithBlock:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithCNContainer:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithContactStore:"
- "initWithContainer:changeTrackingID:"
- "initWithDAAccount:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithDictionary:copyItems:"
- "initWithEmailAddresses:"
- "initWithEmailAddresses:retrieveCertificates:retrieveAvailability:withStartTime:endTime:"
- "initWithExternalIdentifier:"
- "initWithFilename:"
- "initWithFireDate:interval:target:selector:userInfo:repeats:"
- "initWithFormat:"
- "initWithItemChangeType:changedItem:serverId:"
- "initWithItemChangeType:changedItem:serverId:instanceId:"
- "initWithItemChangeType:changedItem:serverId:status:"
- "initWithItemChangeType:changedItem:sourceContainerId:sourceServerId:destinationContainerId:"
- "initWithLabel:"
- "initWithObjects:"
- "initWithPassword:"
- "initWithPath:"
- "initWithRequestType:message:send:"
- "initWithStatus:sourceID:destID:"
- "initWithTrust:"
- "insertObject:atIndex:"
- "insertString:atIndex:"
- "instanceID"
- "instanceId"
- "intValue"
- "integerValue"
- "invalidate"
- "isAccount"
- "isActiveSyncAccount"
- "isAppleInternalInstall"
- "isAuthenticated"
- "isCalDAVAccount"
- "isCalDAVChildAccount"
- "isCardDAVAccount"
- "isChildAccount"
- "isContact"
- "isContainer"
- "isContentReadonly"
- "isDefault"
- "isDisabled"
- "isDraft"
- "isEnabledForDataclass:"
- "isEnabledToSyncDataclass:"
- "isEqual:"
- "isEqualToAccount:"
- "isEqualToString:"
- "isGoogleAccount"
- "isGroup"
- "isHotmailAccount"
- "isInHoldingPattern"
- "isKindOfClass:"
- "isLDAPAccount"
- "isLocal"
- "isMemberOfClass:"
- "isProxy"
- "isSearchContainer"
- "isShutdown"
- "isSubscribedCalendarAccount"
- "isValidating"
- "itemChangeType"
- "keychainAccessibilityType"
- "l_failedWaiters"
- "l_refreshingWaiters"
- "l_restrictedWaiters"
- "label"
- "lastObject"
- "lastQueryStartedTime"
- "lastVerb"
- "legacyIdentifier"
- "length"
- "loadAndReturnError:"
- "loadDaemonBundleForACAccountType:"
- "loadFrameworkForACAccountType:"
- "loadKeychainInformationsForURL:"
- "localizedIdenticalAccountFailureMessage"
- "localizedInvalidPasswordMessage"
- "lock"
- "logICSMessage:atLevel:"
- "logSnippet:"
- "longID"
- "lowercaseString"
- "mQueuedTasks"
- "mResolvedEmailToX509Certs"
- "mailNumberOfPastDaysToSync"
- "mailboxID"
- "mailboxes"
- "mainRunLoop"
- "managerIdleTimer"
- "mapTableWithStrongToStrongObjects"
- "markAsDefault"
- "markForDeletion"
- "markedAsDefault"
- "markedForDeletion"
- "maxSize"
- "meContactidentifier"
- "meIdentifier"
- "meetingRequestIsActionable"
- "meetingRequestMetaData"
- "meetingRequestUUID"
- "mergedFreeBusy"
- "message"
- "messageClass"
- "messageID"
- "migratePasswordForAccount:"
- "modalHeldActiveQueuedTask"
- "modalHeldIndependentTasks"
- "monitorAccount:"
- "monitorFolderWithID:"
- "monitorFoldersForUpdates:"
- "monitorFoldersForUpdates:persistent:"
- "monitorFoldersWithIDs:"
- "monitoredAccounts"
- "mutableContainer"
- "mutableCopy"
- "name"
- "newDataHandlerForDataclass:container:changeTrackingID:"
- "nextObject"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "oauth2Token"
- "oauthInfoProvider"
- "oauthToken"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offFlags"
- "onBehalfOfBundleIdentifier"
- "onFlags"
- "oneshotListOfAccountIDs"
- "openAuthenticationURL:forAccount:shouldConfirm:completion:"
- "openDB"
- "origRequest"
- "parentAccount"
- "parentAccountIdentifier"
- "parentFolderID"
- "parentMailboxID"
- "password"
- "passwordForAccountWithPersistentUUID:expectedAccessibility:shouldSetAccessibility:passwordExpected:"
- "passwordWithExpected:"
- "path"
- "pendingQueries"
- "pendingQueryQueue"
- "performCalendarDirectorySearchForTerms:recordTypes:resultLimit:consumer:"
- "performFetchAttachmentRequest:consumer:"
- "performFetchMessageSearchResultRequests:consumer:"
- "performFolderChange:isUserRequested:"
- "performMailboxRequest:mailbox:previousTag:clientWinsOnSyncConflict:isUserRequested:consumer:"
- "performMailboxRequest:mailbox:previousTag:isUserRequested:consumer:"
- "performMailboxRequests:mailbox:previousTag:clientWinsOnSyncConflict:isUserRequested:consumer:"
- "performMailboxRequests:mailbox:previousTag:isUserRequested:consumer:"
- "performMoveRequests:consumer:"
- "performResolveRecipientsRequest:consumer:"
- "performSearchQuery:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:afterDelay:inModes:"
- "performSelector:withObject:withObject:"
- "performTask"
- "persistentUUID"
- "port"
- "portFromDataclassPropertiesForDataclass:"
- "powerAssertionGroupID"
- "powerAssertionRetainCount:"
- "powerLogIdleTimer"
- "predicateForAccountForContainerWithIdentifier:"
- "predicateForAccountWithExternalIdentifier:"
- "preview"
- "principalPath"
- "principalURL"
- "privateFrameworksPath"
- "processInfo"
- "processName"
- "promptForAllCerts"
- "protectionSpace"
- "protocolVersion"
- "providerWithAddressBook:"
- "providerWithContactStore:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "query"
- "queuedExclusiveTasks"
- "queuedModalTasks"
- "queuedTasks"
- "rangeOfString:options:"
- "rawTrustResultForSSLTrust:hostname:service:"
- "reacquireClientRestrictions:"
- "read"
- "readIsSet"
- "reattainPowerAssertionsForGroupIdentifier:"
- "reattemptInvitationLinkageForMetaData:inFolderWithId:"
- "registerAccount:forOperationWithName:"
- "registerForInterrogationWithBlock:"
- "registerPreemptiveWaiter:forDataclassLocks:completionHandler:"
- "registerWaiter:forDataclassLocks:completionHandler:"
- "registerWithiCalendar"
- "relativePath"
- "release"
- "releasePowerAssertion:"
- "relinquishLocksForWaiter:dataclasses:moreComing:"
- "reload"
- "remoteID"
- "removeAccount:"
- "removeAccountPropertyForKey:"
- "removeAllObjects"
- "removeClientCertificateData"
- "removeConsumerForTask:"
- "removeDBSyncData"
- "removeFromCoreDAVLoggingDelegates"
- "removeItemAtPath:error:"
- "removeKeychainInformationsForURL:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removePasswordForAccount:withPersistentUUID:"
- "removeXpcActivity"
- "renewCredentialsForAccount:force:reason:completion:"
- "replaceOccurrencesOfString:withString:options:range:"
- "replyTo"
- "reportShareRequestAsJunkForCalendar:consumer:"
- "requestCalendarAvailabilityForStartDate:endDate:ignoredEventID:addresses:consumer:"
- "requestCancelTaskWithReason:"
- "requestType"
- "resetAccountID"
- "resetCertWarnings"
- "resetStatusReport"
- "resolvedEmailToX509Certs"
- "respondToShareRequestForCalendar:withResponse:consumer:"
- "respondsToSelector:"
- "restrictions"
- "resumeMonitoringFoldersWithIDs:"
- "retain"
- "retainCount"
- "retainPowerAssertion:withGroupIdentifier:"
- "retrieveAvailablilty"
- "retrieveCertificates"
- "rfc822Data"
- "saveAccountProperties"
- "saveAccountPropertiesWithCompletionHandler:"
- "saveContainer"
- "saveFetchingAutomaticallyState:"
- "saveKeychainInformationsForURL:andPassword:withAccessibility:"
- "saveModifiedPropertiesOnBackingAccount"
- "saveVerifiedAccount:withCompletionHandler:"
- "saveXpcActivity:"
- "scheduleIdentifier"
- "scheme"
- "searchQueriesRunning"
- "searchQuery:finishedWithError:"
- "self"
- "send"
- "sendEmailsForCalEvents:consumer:"
- "sendMessageWithRFC822Data:messageID:outgoingMessageType:originalMessageFolderID:originalMessageItemID:originalMessageLongID:originalAccountID:useSmartTasksIfPossible:isUserRequested:consumer:context:"
- "sendSmartMessageWithRFC822Data:messageID:outgoingMessageType:originalMessageFolderID:originalMessageItemID:originalMessageLongID:originalAccountID:replaceOriginalMime:isUserRequested:consumer:context:"
- "sender"
- "sentItemsFolder"
- "server"
- "serverComplianceClasses"
- "serverID"
- "serverId"
- "serverRoot"
- "serverTrust"
- "set"
- "setAcAccountTypeToAccountDaemonBundleSubpath:"
- "setAcAccountTypeToAccountFrameworkSubpath:"
- "setAcAccountTypeToClassNames:"
- "setAcParentAccountTypeToChildAccountTypes:"
- "setAccount:"
- "setAccountBoolProperty:forKey:"
- "setAccountClassName:"
- "setAccountDescription:"
- "setAccountIdentifier:"
- "setAccountIntProperty:forKey:"
- "setAccountProperty:forKey:"
- "setAccountType:"
- "setAccounts:"
- "setAccountsQueue:"
- "setActiveExclusiveTask:"
- "setActiveModalTask:"
- "setActiveQueuedTask:"
- "setAddressList:forKey:"
- "setAddressListForBcc:"
- "setAddressListForCc:"
- "setAddressListForSender:"
- "setAddressListForTo:"
- "setAgentClassName:"
- "setArePropertiesReadonly:"
- "setAttachmentName:"
- "setAuthenticated:"
- "setAvailabilityStatus:"
- "setBodyFormat:"
- "setBuildVersion:"
- "setCTag:"
- "setCalAlarmChangeId:"
- "setCalAttachmentChangeId:"
- "setCalAttendeeChangeId:"
- "setCalEventChangeId:"
- "setCalRecurrenceChangeId:"
- "setCallbackQueue:"
- "setCertificatesStatus:"
- "setChangeId:"
- "setChangeTrackingID:"
- "setClaimedOwnershipOfEvents:"
- "setClientAccountClassName:"
- "setCompletionHandler:"
- "setConnectionDisplayName:"
- "setConstraintsPath:"
- "setConsumer:forTask:"
- "setContainer:"
- "setContentReadonly:"
- "setContext:"
- "setContextToGroupIdentifier:"
- "setContextToPowerAssertionRef:"
- "setContexts:"
- "setCredential:"
- "setCustomSignature:"
- "setDAAccountVersion:"
- "setDaemonAccountClassName:"
- "setDataclass:"
- "setDataclassPropertyURLsByDataclass:"
- "setDataclasses:"
- "setDateFormat:"
- "setDelegate:"
- "setDestID:"
- "setDestinationContainerId:"
- "setDidLogSyncStart:"
- "setDisplayName:"
- "setEmailAddress:"
- "setEmailAddresses:"
- "setEnabled:forDADataclass:"
- "setEnabled:forDataclass:"
- "setEncryptionIdentityPersistentReference:"
- "setEndTime:"
- "setEventsLockHolder:"
- "setEventsWaiters:"
- "setExceptions:forDigest:"
- "setExternalIdentifier:"
- "setExternalModificationTag:"
- "setExternalSyncData:"
- "setExternalSyncTag:"
- "setFilename:"
- "setFolderID:"
- "setFolderIdsThatExternalClientsCareAboutAdded:deleted:foldersTag:"
- "setFolderName:"
- "setForwardedAttendeeUUIDs:"
- "setForwardedAttendees:"
- "setFromFolder:"
- "setGeneratesBulletins:"
- "setGroupIdentifier:"
- "setGroupIdentifierToContexts:"
- "setHandler:"
- "setHasRemoteChanges:"
- "setHaveWarnedAboutCert:forHost:"
- "setHaveWarnedAboutCertDict:"
- "setHeader:forKey:"
- "setHeldAsideContexts:"
- "setHeldAsideGroupIdentifiers:"
- "setHeldIndependentTasks:"
- "setHighestSequenceNumber:"
- "setHost:"
- "setIdentityCertificatePersistentID:managedByProfile:"
- "setIndependentTasks:"
- "setInstanceId:"
- "setIsDefault:"
- "setIsValidating:"
- "setItemChangeType:"
- "setL_failedWaiters:"
- "setL_refreshingWaiters:"
- "setL_restrictedWaiters:"
- "setLastQueryStartedTime:"
- "setLongID:"
- "setMQueuedTasks:"
- "setMResolvedEmailToX509Certs:"
- "setMailNumberOfPastDaysToSync:"
- "setManagerIdleTimer:"
- "setMarkedAsDefault:"
- "setMarkedForDeletion:"
- "setMaxSize:"
- "setMeContactIdentifier:"
- "setMeIdentifier:"
- "setMergedFreeBusy:"
- "setMessage:"
- "setMessageID:"
- "setModalHeldActiveQueuedTask:"
- "setModalHeldIndependentTasks:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOffFlags:"
- "setOnFlags:"
- "setOrigRequest:"
- "setParentFolderID:"
- "setPassword:"
- "setPassword:forAccount:withPersistentUUID:withAccessibility:"
- "setPendingQueries:"
- "setPendingQueryQueue:"
- "setPersistentUUID:"
- "setPort:"
- "setPowerAssertionGroupID:"
- "setPowerLogIdleTimer:"
- "setPrincipalPath:"
- "setPrincipalURL:"
- "setProtocolVersion:"
- "setQueuedExclusiveTasks:"
- "setQueuedModalTasks:"
- "setRequestType:"
- "setRestrictions:"
- "setRetrieveAvailablilty:"
- "setRetrieveCertificates:"
- "setSend:"
- "setServerID:"
- "setServerId:"
- "setService:"
- "setShouldDoInitialAutodiscovery:"
- "setShouldUseOpportunisticSockets:"
- "setSigningIdentityPersistentReference:"
- "setSourceApplicationBundleIdentifier:"
- "setSourceContainerId:"
- "setSourceID:"
- "setSourceServerId:"
- "setStartTime:"
- "setState:"
- "setStatus:"
- "setStatusReport:"
- "setSyncData:"
- "setSyncTag:"
- "setSyncingAllowed:"
- "setTaskManager:"
- "setToFolder:"
- "setTransactionCount:"
- "setTransactionMonitorDelegate:"
- "setTransactions:"
- "setTrust:"
- "setTrustHandler:"
- "setType:"
- "setUnitTestHackRunLoopMode:"
- "setUnregisterBlock:"
- "setUseSSL:"
- "setUser:"
- "setUserInfo:forClientUUID:"
- "setUserInitiatedSyncTimer:"
- "setUsername:"
- "setValue:forKey:"
- "setWaiter:"
- "setWaiterIDsExpectingEventsLock:"
- "setWasUserInitiated:"
- "setWithObject:"
- "setWithObjects:"
- "setXpcTransactionTimer:"
- "shareResponseFinishedWithError:"
- "sharedBabysitter"
- "sharedConnection"
- "sharedGateKeeper"
- "sharedInstance"
- "sharedKeychain"
- "sharedLogger"
- "sharedManager"
- "sharedMonitor"
- "sharedPowerAssertionManager"
- "sharedRunLoop"
- "sharedTransactionMonitor"
- "shouldAutodiscoverAccountProperties"
- "shouldCancelTaskDueToOnPowerFetchMode"
- "shouldDoInitialAutodiscovery"
- "shouldFailAllTasks"
- "shouldForceNetworking"
- "shouldHoldPowerAssertion"
- "shouldRemoveDBSyncDataOnAccountChange"
- "shouldUseOpportunisticSockets"
- "showPromptWithOptions:responseBlock:"
- "showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:"
- "shutdown"
- "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
- "signingIdentityPersistentReference"
- "slurpAndRemoveLookasideFile:prefixString:suffixString:"
- "smimeType"
- "snapshotWithSignature:duration:event:payload:reply:"
- "source"
- "sourceApplicationBundleIdentifier"
- "sourceContainerId"
- "sourceID"
- "sourceServerId"
- "spinnerIdentifiers"
- "standardUserDefaults"
- "startModal"
- "startTime"
- "startup"
- "state"
- "stateString"
- "status"
- "statusReport"
- "statusReportWithCompletionBlock:"
- "stopMonitoringAllFolders"
- "stopMonitoringFolderWithID:"
- "stopMonitoringFolders"
- "stopMonitoringFoldersForUpdates:"
- "stopMonitoringFoldersWithIDs:"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByTrimmingCharactersInSet:"
- "stringByURLQuoting"
- "stringForItemChangeType:"
- "stringFromDate:"
- "stringValue"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subject"
- "submitExclusiveTask:"
- "submitExclusiveTask:toFrontOfQueue:"
- "submitIndependentTask:"
- "submitQueuedTask:"
- "substringFromIndex:"
- "substringToIndex:"
- "superclass"
- "supportsAuthentication"
- "supportsConversations"
- "supportsDraftFolderSync"
- "supportsEmailFlagging"
- "supportsMailboxSearch"
- "supportsSecureCoding"
- "supportsSmartForwardReply"
- "supportsUniqueServerId"
- "suspendMonitoringFoldersWithIDs:"
- "syncData"
- "syncStoreIdentifier"
- "syncTag"
- "synchronizeEventsFolder:previousTag:actions:highestIdContext:isInitialUberSync:isResyncAfterConnectionFailed:moreLocalChangesAvailable:consumer:"
- "systemTimeZone"
- "takeValuesFromModifiedAccount:"
- "taskDidFinish:"
- "taskEndModal:"
- "taskIsModal:"
- "taskManager"
- "taskManagerDidAddTask:"
- "taskManagerWillRemoveTask:"
- "taskRequestModal:"
- "tearDown"
- "threadTopic"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "to"
- "toFolder"
- "tokenByRegisteringAccount:forOperationWithName:"
- "transactionCount"
- "transactionId"
- "transactionMonitorDelegate"
- "transactions"
- "trustHandler"
- "type"
- "unactionableICSRepresentationForMetaData:inFolderWithId:outSummary:"
- "unitTestHackRunLoopMode"
- "unmonitorAccount:"
- "unregisterAccount:forOperationWithName:"
- "unregisterBlock"
- "unregisterWaiterForDataclassLocks:"
- "updateContainer:"
- "updateExistingAccountProperties"
- "updateSaveRequest:"
- "upgradeAccount"
- "uppercaseString"
- "uri"
- "urlFromDataclassPropertiesForDataclass:"
- "useCredential:forAuthenticationChallenge:"
- "useSSL"
- "useSSLFromDataclassPropertiesForDataclass:"
- "user"
- "userAgent"
- "userAgentHeader"
- "userInfo"
- "userInitiatedSyncTimer"
- "username"
- "usernameWithoutDomain"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8#16"
- "v24@0:8@\"CNSaveRequest\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^v16"
- "v24@0:8q16"
- "v28@0:8@\"DAFolderChange\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8B16@20"
- "v28@0:8B16q20"
- "v28@0:8i16@20"
- "v32@0:8:16@24"
- "v32@0:8@\"NSString\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v32@0:8^{__CFData=}16@24"
- "v32@0:8q16@?24"
- "v36@0:8@16q24B32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@?32"
- "v44@0:8@16q24B32@?36"
- "v48@0:8:16@24d32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8^{__SecTrust=}16@24@32@?40"
- "v56@0:8^{__CFUserNotification=}16@24@32@40@?48"
- "v68@0:8@16@24@32@40B48B52B56@60"
- "vendDaemons:"
- "verbIsSet"
- "verifyCredentialsForAccount:saveWhenAuthorized:withHandler:"
- "waiter"
- "waiterID"
- "waiterIDsExpectingEventsLock"
- "waiterNum"
- "wasUserInitiated"
- "weakObjectsHashTable"
- "webLoginRequestedAtURL:reasonString:inQueue:completionBlock:"
- "whitespaceAndNewlineCharacterSet"
- "wipeServerIds"
- "writeToFile:atomically:"
- "xpcTransactionTimer"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```

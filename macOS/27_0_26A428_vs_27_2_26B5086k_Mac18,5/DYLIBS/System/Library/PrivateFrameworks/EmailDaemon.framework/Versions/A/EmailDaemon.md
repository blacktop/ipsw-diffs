## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon`

```diff

-3901.100.1.1.11
-  __TEXT.__text: 0x2b2ab8
-  __TEXT.__objc_methlist: 0x1359c
-  __TEXT.__const: 0x51fc
-  __TEXT.__gcc_except_tab: 0x4acd0
-  __TEXT.__cstring: 0x2849a
-  __TEXT.__oslogstring: 0x1b1bf
+3901.200.34.0.0
+  __TEXT.__text: 0x2b937c
+  __TEXT.__objc_methlist: 0x1376c
+  __TEXT.__const: 0x538c
+  __TEXT.__gcc_except_tab: 0x4b4a0
+  __TEXT.__cstring: 0x2892a
+  __TEXT.__oslogstring: 0x1b3b4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x26
-  __TEXT.__constg_swiftt: 0x10c8
-  __TEXT.__swift5_typeref: 0x17fb
-  __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x10df
-  __TEXT.__swift5_fieldmd: 0x1654
-  __TEXT.__swift5_assocty: 0x248
-  __TEXT.__swift5_proto: 0x398
-  __TEXT.__swift5_types: 0x1d4
-  __TEXT.__swift5_capture: 0x7d0
+  __TEXT.__swift5_typeref: 0x1822
+  __TEXT.__constg_swiftt: 0x1104
+  __TEXT.__swift5_builtin: 0x12c
+  __TEXT.__swift5_reflstr: 0x114f
+  __TEXT.__swift5_fieldmd: 0x16a0
+  __TEXT.__swift5_assocty: 0x260
+  __TEXT.__swift5_proto: 0x3a4
+  __TEXT.__swift5_types: 0x1dc
+  __TEXT.__swift5_capture: 0x840
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
-  __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x12538
-  __TEXT.__eh_frame: 0x1598
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__unwind_info: 0x127d0
+  __TEXT.__eh_frame: 0x15d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1bb0
-  __DATA_CONST.__objc_classlist: 0x9e8
+  __DATA_CONST.__objc_classlist: 0x9f8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb208
+  __DATA_CONST.__objc_selrefs: 0xb3a0
   __DATA_CONST.__objc_protorefs: 0x120
-  __DATA_CONST.__objc_superrefs: 0x5e0
-  __DATA_CONST.__objc_arraydata: 0x5f0
-  __DATA_CONST.__got: 0x1e20
-  __AUTH_CONST.__const: 0xff23
-  __AUTH_CONST.__cfstring: 0xf960
-  __AUTH_CONST.__objc_const: 0x22988
+  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_arraydata: 0x610
+  __DATA_CONST.__got: 0x1e70
+  __AUTH_CONST.__const: 0x1040b
+  __AUTH_CONST.__cfstring: 0xfae0
+  __AUTH_CONST.__objc_const: 0x22b00
   __AUTH_CONST.__objc_intobj: 0x9f0
-  __AUTH_CONST.__objc_arrayobj: 0x288
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1658
-  __AUTH.__objc_data: 0xbe8
-  __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0x14a0
-  __DATA.__data: 0x39f0
+  __AUTH_CONST.__auth_got: 0x1660
+  __AUTH.__objc_data: 0xcd8
+  __AUTH.__data: 0x390
+  __DATA.__objc_ivar: 0x14b8
+  __DATA.__data: 0x3a30
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5c78
-  __DATA_DIRTY.__data: 0x1a58
-  __DATA_DIRTY.__bss: 0x1bf0
+  __DATA_DIRTY.__objc_data: 0x5c28
+  __DATA_DIRTY.__data: 0x1a68
+  __DATA_DIRTY.__bss: 0x1c00
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11649
-  Symbols:   20367
-  CStrings:  5442
+  Functions: 11751
+  Symbols:   20518
+  CStrings:  5480
 
Symbols:
+ +[EDAccountAuthentication log]
+ +[EDDataDetectionUtilities _lastWords:inString:]
+ +[EDListUnsubscribeDetector _validateHeaders:dkimVerified:]
+ +[EDListUnsubscribeDetector receivingAccountFromMessage:]
+ +[EDListUnsubscribeDetector unsubscribeTypeForHeader:]
+ +[EDListUnsubscribeDetector validatedUnsubscribeTypeForHeader:dkimVerified:]
+ +[EDMessageAuthenticator _isTemporaryDKIMError:]
+ +[EDMessageAuthenticator _mostAlignedDKIMServerStatementFromAuthenticationResult:forSender:]
+ +[EDMessageAuthenticator _setLocalResultsOnAuthenticationState:forAuthenticationResult:]
+ +[EDMessageAuthenticator _setServerResultsAsLocalResultsOnAuthenticationState:forDKIMServerStatement:dmarcServerStatus:]
+ +[EDMessageAuthenticator _setServerResultsOnAuthenticationState:forDKIMServerStatement:dmarcServerStatus:]
+ +[EDMessageAuthenticator authenticationStateForAuthenticationResult:forMessage:fromSender:trustingServer:]
+ +[EDMessageListItemPredicates _mailboxURLSubpredicatesForPredicate:mailboxPersistence:]
+ +[EDSearchableIndexItem searchableMessageForBaseMessage:htmlContent:hasCompleteData:isEncrypted:includeEncryptedBody:]
+ -[EDAccountAuthentication .cxx_destruct]
+ -[EDAccountAuthentication _hostnamesHaveSameTopLevelDomain:deliveryAccount:]
+ -[EDAccountAuthentication _shouldAutoUpdateDeliveryAccount:forChangedReceivingAccount:]
+ -[EDAccountAuthentication _updateDeliveryAccountCredentialIfNecessaryForAccountWithAccount:]
+ -[EDAccountAuthentication _updateDeliveryAccountCredentialIfNecessaryForReceivingAccount:]
+ -[EDAccountAuthentication accountFactory]
+ -[EDAccountAuthentication initWithAccountFactory:]
+ -[EDAccountAuthentication updateDeliveryAccountCredentialIfNecessaryForAccountWithIdentifier:]
+ -[EDAccountAuthentication updateDeliveryAccountCredentialIfNecessaryForAccountWithSystemAccount:]
+ -[EDInMemoryThreadQueryHandler test_drain]
+ -[EDListUnsubscribeDetector .cxx_destruct]
+ -[EDListUnsubscribeDetector _listIDString:]
+ -[EDListUnsubscribeDetector _normalizedAddress:]
+ -[EDListUnsubscribeDetector _persistentKeyForHeaders:]
+ -[EDListUnsubscribeDetector _senderString:]
+ -[EDListUnsubscribeDetector acceptCommand:]
+ -[EDListUnsubscribeDetector commandForMessage:dkimVerified:]
+ -[EDListUnsubscribeDetector commandForMessage:mailToOnly:dkimVerified:]
+ -[EDListUnsubscribeDetector ignoreCommand:]
+ -[EDListUnsubscribeDetector initWithMutableDictionary:]
+ -[EDListUnsubscribeDetector init]
+ -[EDListUnsubscribeDetector removeAllPersistedCommands]
+ -[EDListUnsubscribeDetector shouldIgnoreMessageWithHeaders:]
+ -[EDMessageCountQueryHandler test_drain]
+ -[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]
+ -[EDMessageQueryHandler test_drain]
+ -[EDMessageRepository loadOlderItemsForObservationIdentifier:mailboxesToLoad:]
+ -[EDPrecomputedThreadQueryHandler test_drain]
+ -[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]
+ -[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]
+ -[EDThreadMigrator test_drain]
+ -[EDThreadPersistence _invalidateAllCachedSizeDecisions]
+ -[EDThreadPersistence _invalidateCachedMigratableSizeDecisions]
+ -[EDThreadScopeManager test_drain]
+ -[EDVIPManager test_drain]
+ -[_EDUnsubscribeInfo .cxx_destruct]
+ -[_EDUnsubscribeInfo initWithHeaders:]
+ -[_EDUnsubscribeInfo setMailtoURL:]
+ -[_EDUnsubscribeInfo setPostContent:]
+ -[_EDUnsubscribeInfo setPostURL:]
+ EDBiomeSignalDonationQueue.onceToken
+ EDBiomeSignalDonationQueue.queue
+ EDOneTimeCodeVisibleCharacterSet.onceToken
+ EDOneTimeCodeVisibleCharacterSet.visibleCharacterSet
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table240
+ GCC_except_table309
+ GCC_except_table327
+ GCC_except_table346
+ GCC_except_table350
+ GCC_except_table362
+ GCC_except_table369
+ GCC_except_table370
+ GCC_except_table377
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table388
+ OBJC_IVAR_$_EDAccountAuthentication._accountFactory
+ OBJC_IVAR_$_EDListUnsubscribeDetector._persistentDictionary
+ OBJC_IVAR_$_EDThreadPersistence._tooLargeToMigrateDecisionCache
+ OBJC_IVAR_$_EDThreadPersistence._tooLargeToMigrateDecisionCacheGeneration
+ OBJC_IVAR_$__EDUnsubscribeInfo._mailtoURL
+ OBJC_IVAR_$__EDUnsubscribeInfo._postContent
+ OBJC_IVAR_$__EDUnsubscribeInfo._postURL
+ _ECMessageHeaderKeyListID
+ _ECMessageHeaderKeyListUnsubscribe
+ _ECMessageHeaderKeyListUnsubscribePost
+ _EDIndexableItemIndexingTypeIsUpdate
+ _EDIndexableItemIndexingTypeIsUserInitiated
+ _EDSearchableIndexTransactionItemsNeedDownloadToReindex
+ _OBJC_CLASS_$_ACAccountCredential
+ _OBJC_CLASS_$_EAEmailAddressParser
+ _OBJC_CLASS_$_EDAccountAuthentication
+ _OBJC_CLASS_$_EDListUnsubscribeDetector
+ _OBJC_CLASS_$_EMListUnsubscribeCommand
+ _OBJC_CLASS_$_EMMailToURLComponents
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$__EDUnsubscribeInfo
+ _OBJC_METACLASS_$_EDAccountAuthentication
+ _OBJC_METACLASS_$_EDListUnsubscribeDetector
+ _OBJC_METACLASS_$__EDUnsubscribeInfo
+ __87+[EDMessageListItemPredicates _mailboxURLSubpredicatesForPredicate:mailboxPersistence:]_block_invoke
+ __93-[EDSearchableIndexPersistence _messagesRequiringIndexingForType:excludingIdentifiers:limit:]_block_invoke
+ __OBJC_$_CLASS_METHODS_EDAccountAuthentication
+ __OBJC_$_CLASS_METHODS_EDListUnsubscribeDetector
+ __OBJC_$_INSTANCE_METHODS_EDAccountAuthentication
+ __OBJC_$_INSTANCE_METHODS_EDListUnsubscribeDetector
+ __OBJC_$_INSTANCE_METHODS__EDUnsubscribeInfo
+ __OBJC_$_INSTANCE_VARIABLES_EDAccountAuthentication
+ __OBJC_$_INSTANCE_VARIABLES_EDListUnsubscribeDetector
+ __OBJC_$_INSTANCE_VARIABLES__EDUnsubscribeInfo
+ __OBJC_$_PROP_LIST_EDAccountAuthentication
+ __OBJC_CLASS_RO_$_EDAccountAuthentication
+ __OBJC_CLASS_RO_$_EDListUnsubscribeDetector
+ __OBJC_CLASS_RO_$__EDUnsubscribeInfo
+ __OBJC_METACLASS_RO_$_EDAccountAuthentication
+ __OBJC_METACLASS_RO_$_EDListUnsubscribeDetector
+ __OBJC_METACLASS_RO_$__EDUnsubscribeInfo
+ ___26-[EDVIPManager test_drain]_block_invoke
+ ___26-[EDVIPManager test_drain]_block_invoke_2
+ ___30+[EDAccountAuthentication log]_block_invoke
+ ___30-[EDThreadMigrator test_drain]_block_invoke
+ ___34-[EDThreadScopeManager test_drain]_block_invoke
+ ___35-[EDMessageQueryHandler test_drain]_block_invoke
+ ___40-[EDMessageCountQueryHandler test_drain]_block_invoke
+ ___42-[EDInMemoryThreadQueryHandler test_drain]_block_invoke
+ ___45-[EDPrecomputedThreadQueryHandler test_drain]_block_invoke
+ ___45-[EDPrecomputedThreadQueryHandler test_drain]_block_invoke_2
+ ___48+[EDDataDetectionUtilities _lastWords:inString:]_block_invoke
+ ___69-[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]_block_invoke
+ ___69-[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]_block_invoke_2
+ ___70-[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]_block_invoke
+ ___70-[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]_block_invoke_2
+ ___71-[EDListUnsubscribeDetector commandForMessage:mailToOnly:dkimVerified:]_block_invoke
+ ___78-[EDMessageRepository loadOlderItemsForObservationIdentifier:mailboxesToLoad:]_block_invoke
+ ___83-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]_block_invoke
+ ___83-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]_block_invoke_2
+ ___87+[EDMessageListItemPredicates _mailboxURLSubpredicatesForPredicate:mailboxPersistence:]_block_invoke
+ ___93-[EDSearchableIndexPersistence _messagesRequiringIndexingForType:excludingIdentifiers:limit:]_block_invoke
+ ___EDBiomeSignalDonationQueue_block_invoke
+ ___EDOneTimeCodeVisibleCharacterSet_block_invoke
+ ___block_descriptor_40_ea8_32bs_e21_"NSPredicate"16?08l
+ ___block_descriptor_40_ea8_32s_e21_"NSPredicate"16?08l
+ ___block_descriptor_48_ea8_32s_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48l
+ ___block_descriptor_48_ea8_32s_e9_16?0^8l
+ ___block_descriptor_72_ea8_32s40s48s_e14_"NSArray"8?0l
+ __swift_closure_destructor.20Tm
+ __swift_closure_destructor.32Tm
+ _associated conformance 17IndexingAnalytics9ItemEventO13UpdateTriggerOSHAASQ
+ _associated conformance 17IndexingAnalytics9ItemEventO13UpdateTriggerOs12CaseIterableAA8AllCasessAFP_Sl
+ _objc_msgSend$_hostnamesHaveSameTopLevelDomain:deliveryAccount:
+ _objc_msgSend$_invalidateAllCachedSizeDecisions
+ _objc_msgSend$_invalidateCachedMigratableSizeDecisions
+ _objc_msgSend$_lastWords:inString:
+ _objc_msgSend$_listIDString:
+ _objc_msgSend$_mailboxURLSubpredicatesForPredicate:mailboxPersistence:
+ _objc_msgSend$_normalizedAddress:
+ _objc_msgSend$_persistentKeyForHeaders:
+ _objc_msgSend$_senderString:
+ _objc_msgSend$_shouldAutoUpdateDeliveryAccount:forChangedReceivingAccount:
+ _objc_msgSend$_updateDeliveryAccountCredentialIfNecessaryForAccountWithAccount:
+ _objc_msgSend$_updateDeliveryAccountCredentialIfNecessaryForReceivingAccount:
+ _objc_msgSend$accountFactory
+ _objc_msgSend$accountWithSystemAccount:
+ _objc_msgSend$authenticationStateForAuthenticationResult:forMessage:fromSender:trustingServer:
+ _objc_msgSend$batchDidEnd:items:error:
+ _objc_msgSend$canAuthenticateWithCurrentCredentials
+ _objc_msgSend$commandForMessage:mailToOnly:dkimVerified:
+ _objc_msgSend$componentsWithURL:
+ _objc_msgSend$controlCharacterSet
+ _objc_msgSend$countOfMessagesInMailboxDatabaseIDs:upToLimit:
+ _objc_msgSend$didRequestRedonationForItems:
+ _objc_msgSend$didUpdateMessagesAndRecordDonations:trigger:
+ _objc_msgSend$dkimSignatureHeaders
+ _objc_msgSend$enumerateSubstringsInRange:options:usingBlock:
+ _objc_msgSend$firstSenderAddress
+ _objc_msgSend$futureWithBlock:
+ _objc_msgSend$hasPasswordCredential
+ _objc_msgSend$idnaEncodedAddressForAddress:
+ _objc_msgSend$illegalCharacterSet
+ _objc_msgSend$initWithHeaders:
+ _objc_msgSend$initWithMutableDictionary:
+ _objc_msgSend$initWithPassword:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$listID
+ _objc_msgSend$listUnsubscribeCommands
+ _objc_msgSend$listUnsubscribePostContent
+ _objc_msgSend$mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:accountObjectID:headerUnsubscribeTypes:
+ _objc_msgSend$markMessagesNeedingDownloadToReindex:
+ _objc_msgSend$oneClickUnsubscribeCommandWithListID:sender:senderForUnsubscribeMessage:URL:postContent:headerUnsubscribeTypes:
+ _objc_msgSend$password
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$receivingAccountFromMessage:
+ _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:trigger:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$resolvedPolicyForIMAPHost:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$savePersistentAccount
+ _objc_msgSend$searchableMessageForBaseMessage:htmlContent:hasCompleteData:isEncrypted:includeEncryptedBody:
+ _objc_msgSend$sender
+ _objc_msgSend$senderForUnsubscribeMessage
+ _objc_msgSend$setCredential:
+ _objc_msgSend$sharedDictionaryWithIdentifier:
+ _objc_msgSend$shouldIgnoreMessageWithHeaders:
+ _objc_msgSend$signedHeaderFields
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$test_drain
+ _objc_msgSend$thinOldEvents
+ _objc_msgSend$toRecipients
+ _objc_msgSend$verificationContextForMessageData:error:
+ _objc_msgSend$verifyMessageWithContext:options:error:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _symbolic Say_____G 17IndexingAnalytics9ItemEventO13UpdateTriggerO
+ _symbolic _____ 17IndexingAnalytics9ItemEventO13UpdateTriggerO
+ _symbolic _____ So22EDMessageUpdateTriggerV
- +[EDInteractionEventLogLegacyPersistentBitsProvider log]
- -[EDInteractionEventLogLegacyPersistentBitsProvider _findExistingSaltError:]
- -[EDInteractionEventLogLegacyPersistentBitsProvider _oldSalt]
- -[EDInteractionEventLogLegacyPersistentBitsProvider _persistentBits]
- -[EDInteractionEventLogLegacyPersistentBitsProvider _queryKeychainError:]
- -[EDMessageAuthenticator _isTemporaryDKIMError:]
- -[EDMessageAuthenticator _messageAuthenticationStateForAuthenticationResult:sender:trustingServer:]
- -[EDMessageAuthenticator _mostAlignedDKIMServerStatementFromAuthenticationResult:forSender:]
- -[EDMessageRepository loadOlderItemsForObservationIdentifier:]
- -[EDSearchableIndexAttachmentItem attributeSetForFilePromise]
- -[EDSearchableIndexAttachmentItem setAttributeSetForFilePromise:]
- -[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]
- GCC_except_table232
- GCC_except_table233
- GCC_except_table242
- GCC_except_table311
- GCC_except_table312
- GCC_except_table349
- GCC_except_table353
- GCC_except_table365
- GCC_except_table372
- GCC_except_table373
- GCC_except_table380
- OBJC_IVAR_$_EDSearchableIndexAttachmentItem._attributeSetForFilePromise
- _OBJC_CLASS_$_EDInteractionEventLogLegacyPersistentBitsProvider
- _OBJC_CLASS_$_EMListUnsubscribeDetector
- _OBJC_METACLASS_$_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_$_CLASS_METHODS_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_$_CLASS_PROP_LIST_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_$_INSTANCE_METHODS_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_$_PROP_LIST_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_CLASS_PROTOCOLS_$_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_CLASS_RO_$_EDInteractionEventLogLegacyPersistentBitsProvider
- __OBJC_METACLASS_RO_$_EDInteractionEventLogLegacyPersistentBitsProvider
- ___48-[EDPrecomputedThreadQueryHandler test_tearDown]_block_invoke
- ___48-[EDPrecomputedThreadQueryHandler test_tearDown]_block_invoke_2
- ___56+[EDInteractionEventLogLegacyPersistentBitsProvider log]_block_invoke
- ___61-[EDSearchableIndexAttachmentItem attributeSetForFilePromise]_block_invoke
- ___62-[EDMessageRepository loadOlderItemsForObservationIdentifier:]_block_invoke
- ___75-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]_block_invoke
- ___75-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]_block_invoke_2
- ___76-[EDInteractionEventLogLegacyPersistentBitsProvider _findExistingSaltError:]_block_invoke
- ___block_descriptor_40_ea8_32w_e50_v24?0"CSSearchableItemAttributeSet"8"NSError"16l
- ___swift_memcpy2_1
- __swift_closure_destructor.14Tm
- __swift_closure_destructor.26Tm
- _objc_msgSend$_oldSalt
- _objc_msgSend$attributeSetForFilePromise
- _objc_msgSend$batchDidEnd:error:
- _objc_msgSend$defaultPolicy
- _objc_msgSend$defaultPolicyForIMAPHost:
- _objc_msgSend$defaultSearchableIndex
- _objc_msgSend$didDonateItems:
- _objc_msgSend$didFailToDonateItems:
- _objc_msgSend$didUpdateMessagesAndRecordDonations:
- _objc_msgSend$fetchFile:attributesWithCompletionHandler:
- _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:
- _objc_msgSend$searchableItemProcessingDelay
- _objc_msgSend$sleepForTimeInterval:
CStrings:
+ " NOT IN\n       ( "
+ "$1$2"
+ "%@,%@,%@"
+ ")\n                AS is_update,\n            "
+ "-[EDInMemoryThreadQueryHandler test_drain]"
+ "-[EDMessageCountQueryHandler test_drain]"
+ "-[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]"
+ "-[EDMessageQueryHandler test_drain]"
+ "-[EDPrecomputedThreadQueryHandler test_drain]"
+ "-[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]"
+ "-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]"
+ "-[EDThreadMigrator test_drain]"
+ "-[EDThreadScopeManager test_drain]"
+ "-[EDVIPManager test_drain]"
+ "<%{public}@> Timeout validating headers for: %@"
+ "@\"NSArray\"8@?0"
+ "@\"NSPredicate\"16@?0@8"
+ "@16@?0^@8"
+ "Account is not a receiving account. No delivery account to update: %@"
+ "Attempt to update password if needed for delivery account %@"
+ "EDListUnsubscribeDetector.m"
+ "EDThreadMigrator.m"
+ "EDThreadScopeManager.m"
+ "EmailDaemon/EDSearchableIndexAnalyticsPersistence.swift"
+ "Ignoring server authentication results for denylisted provider for message: %{public}@"
+ "L:%@"
+ "Marked %{public}@ messages as needing download to re-donate"
+ "Marking messages as needing download to reindex"
+ "No delivery account password found. Nothing to do"
+ "Received unhandled update trigger "
+ "Receiving account password changed: %@"
+ "Resolved download policy for account %{public}s host=%s quota=%{public}s"
+ "Resolving download policy for account %{public}s with no hostname, expected an IMAP account"
+ "S:%@"
+ "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL THEN 1 ELSE 0 END) AS indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed THEN 1 ELSE 0 END) AS message_bodies_indexed,       SUM(CASE WHEN searchable_messages.transaction_id IN (%lld, %lld) THEN 1 ELSE 0 END) AS messages_to_redonate       %@  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %@"
+ "SearchableIndexDownloadPolicy"
+ "Should not try to update delivery account password"
+ "Thinning old batches"
+ "Thinning old identified events"
+ "Thread-scope migration size check: mailbox membership %ld (cap %ld, tooLarge=%d) in %.3fs for %{public}@"
+ "UPDATE OR IGNORE searchable_messages   SET transaction_id = %lld WHERE transaction_id = %lld   AND message_id IN (SELECT value FROM json_each(:message_ids)) RETURNING message_id"
+ "Updating password for %@ did not work. Reverting password"
+ "Updating password worked for delivery account: %@"
+ "^[^<>]*<([^>]+)>\\s*$|^(.+)$"
+ "accepted"
+ "com.apple.mail.biome-signal-donation"
+ "com.apple.mail.listUnsubscribeInfo"
+ "command"
+ "deny"
+ "ignored"
+ "mailto"
+ "message-authentication-provider-info"
+ "policy"
+ "thinEvents(before:)"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
- "\n                AS is_update,\n            "
- "%@,%@"
- "-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]"
- "<null>"
- "EDThreadScopeMigrationSizeCheck"
- "Error finding existing old salt: %d"
- "Failed to read old salt %{public}@"
- "Failed to receive an attribute set for file:%@ error:%{public}@"
- "Found existing old salt"
- "No old salt found"
- "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL THEN 1 ELSE 0 END) AS indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed THEN 1 ELSE 0 END) AS message_bodies_indexed,       SUM(CASE WHEN searchable_messages.transaction_id = %lld THEN 1 ELSE 0 END) AS messages_to_redonate       %@  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %@"
- "Threadscope matches %ld messages (>= %ld); using in-memory threads instead of migrating: %{public}@"
- "Warning: about to index message with an empty subject. %{public}@"
- "hasCompleteContent"
- "hasHeaders"
- "mailboxtype"
- "v24@?0@\"CSSearchableItemAttributeSet\"8@\"NSError\"16"
```

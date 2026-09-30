## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3901.100.1.2.14
-  __TEXT.__text: 0x286398
-  __TEXT.__objc_methlist: 0x133f4
-  __TEXT.__const: 0x524c
-  __TEXT.__gcc_except_tab: 0x4a5ec
-  __TEXT.__cstring: 0x28fca
-  __TEXT.__oslogstring: 0x1b3bf
-  __TEXT.__dlopen_cstrs: 0x3bc
+3901.200.34.0.0
+  __TEXT.__text: 0x28c56c
+  __TEXT.__objc_methlist: 0x13634
+  __TEXT.__const: 0x53cc
+  __TEXT.__gcc_except_tab: 0x4aec4
+  __TEXT.__cstring: 0x2976a
+  __TEXT.__oslogstring: 0x1b614
+  __TEXT.__dlopen_cstrs: 0x415
   __TEXT.__ustring: 0x26
-  __TEXT.__constg_swiftt: 0x10ec
-  __TEXT.__swift5_typeref: 0x182f
-  __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x10df
-  __TEXT.__swift5_fieldmd: 0x1664
-  __TEXT.__swift5_assocty: 0x248
-  __TEXT.__swift5_proto: 0x39c
-  __TEXT.__swift5_types: 0x1d8
-  __TEXT.__swift5_capture: 0x830
+  __TEXT.__swift5_typeref: 0x1856
+  __TEXT.__constg_swiftt: 0x1128
+  __TEXT.__swift5_builtin: 0x12c
+  __TEXT.__swift5_reflstr: 0x114f
+  __TEXT.__swift5_fieldmd: 0x16b0
+  __TEXT.__swift5_assocty: 0x260
+  __TEXT.__swift5_proto: 0x3a8
+  __TEXT.__swift5_types: 0x1e0
+  __TEXT.__swift5_capture: 0x880
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
-  __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x124d8
-  __TEXT.__eh_frame: 0x16c0
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__unwind_info: 0x127e8
+  __TEXT.__eh_frame: 0x16f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x94e0
-  __DATA_CONST.__objc_classlist: 0x9e0
+  __DATA_CONST.__const: 0x95d0
+  __DATA_CONST.__objc_classlist: 0x9f8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x430
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb130
+  __DATA_CONST.__objc_selrefs: 0xb380
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x5d8
-  __DATA_CONST.__objc_arraydata: 0x6b8
-  __DATA_CONST.__got: 0x1e70
-  __AUTH_CONST.__const: 0x784b
-  __AUTH_CONST.__cfstring: 0xfce0
-  __AUTH_CONST.__objc_const: 0x22648
+  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_arraydata: 0x6d8
+  __DATA_CONST.__got: 0x1ed0
+  __AUTH_CONST.__const: 0x7c03
+  __AUTH_CONST.__cfstring: 0xff60
+  __AUTH_CONST.__objc_const: 0x228d0
   __AUTH_CONST.__objc_intobj: 0xa38
-  __AUTH_CONST.__objc_arrayobj: 0x270
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1818
-  __AUTH.__objc_data: 0xb98
-  __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0x147c
-  __DATA.__data: 0x39c0
+  __AUTH_CONST.__auth_got: 0x1820
+  __AUTH.__objc_data: 0xcd8
+  __AUTH.__data: 0x390
+  __DATA.__objc_ivar: 0x1490
+  __DATA.__data: 0x3a10
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5c78
-  __DATA_DIRTY.__data: 0x1b00
-  __DATA_DIRTY.__bss: 0x1b80
+  __DATA_DIRTY.__objc_data: 0x5c28
+  __DATA_DIRTY.__data: 0x1aa0
+  __DATA_DIRTY.__bss: 0x1b98
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11571
-  Symbols:   20005
-  CStrings:  5480
+  Functions: 11686
+  Symbols:   20211
+  CStrings:  5539
 
Symbols:
+ +[EDAccountAuthentication log]
+ +[EDAccountDeletionDiagnostics _descriptionForAccount:]
+ +[EDAccountDeletionDiagnostics _isEnabled]
+ +[EDAccountDeletionDiagnostics _requestIdentifierForAccount:]
+ +[EDAccountDeletionDiagnostics log]
+ +[EDAccountDeletionDiagnostics sharedInstance]
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
+ -[EDAccountDeletionDiagnostics .cxx_destruct]
+ -[EDAccountDeletionDiagnostics _init]
+ -[EDAccountDeletionDiagnostics _notificationContentForAccountDescription:deletionTime:]
+ -[EDAccountDeletionDiagnostics notificationCenter]
+ -[EDAccountDeletionDiagnostics notifyOfAccountRemovedFromIndex:]
+ -[EDAccountDeletionDiagnostics setNotificationCenter:]
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
+ -[EDMessageQueryHandler test_drain]
+ -[EDPrecomputedThreadQueryHandler test_drain]
+ -[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]
+ -[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]
+ -[EDThreadMigrator test_drain]
+ -[EDThreadScopeManager test_drain]
+ -[EDVIPManager test_drain]
+ -[_EDUnsubscribeInfo .cxx_destruct]
+ -[_EDUnsubscribeInfo initWithHeaders:]
+ -[_EDUnsubscribeInfo setMailtoURL:]
+ -[_EDUnsubscribeInfo setPostContent:]
+ -[_EDUnsubscribeInfo setPostURL:]
+ _ECMessageHeaderKeyListID
+ _ECMessageHeaderKeyListUnsubscribe
+ _ECMessageHeaderKeyListUnsubscribePost
+ _EDBiomeSignalDonationQueue.onceToken
+ _EDBiomeSignalDonationQueue.queue
+ _EDIndexableItemIndexingTypeIsUpdate
+ _EDIndexableItemIndexingTypeIsUserInitiated
+ _EDOneTimeCodeVisibleCharacterSet.onceToken
+ _EDOneTimeCodeVisibleCharacterSet.visibleCharacterSet
+ _EDSearchableIndexTransactionItemsNeedDownloadToReindex
+ _OBJC_CLASS_$_ACAccountCredential
+ _OBJC_CLASS_$_EAEmailAddressParser
+ _OBJC_CLASS_$_EDAccountAuthentication
+ _OBJC_CLASS_$_EDAccountDeletionDiagnostics
+ _OBJC_CLASS_$_EDListUnsubscribeDetector
+ _OBJC_CLASS_$_EMListUnsubscribeCommand
+ _OBJC_CLASS_$_EMMailToURLComponents
+ _OBJC_CLASS_$_MSRadarURLBuilder
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$__EDUnsubscribeInfo
+ _OBJC_IVAR_$_EDAccountAuthentication._accountFactory
+ _OBJC_IVAR_$_EDAccountDeletionDiagnostics._notificationCenter
+ _OBJC_IVAR_$_EDListUnsubscribeDetector._persistentDictionary
+ _OBJC_IVAR_$__EDUnsubscribeInfo._mailtoURL
+ _OBJC_IVAR_$__EDUnsubscribeInfo._postContent
+ _OBJC_IVAR_$__EDUnsubscribeInfo._postURL
+ _OBJC_METACLASS_$_EDAccountAuthentication
+ _OBJC_METACLASS_$_EDAccountDeletionDiagnostics
+ _OBJC_METACLASS_$_EDListUnsubscribeDetector
+ _OBJC_METACLASS_$__EDUnsubscribeInfo
+ _UserNotificationsLibrary
+ _UserNotificationsLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_EDAccountAuthentication
+ __OBJC_$_CLASS_METHODS_EDAccountDeletionDiagnostics
+ __OBJC_$_CLASS_METHODS_EDListUnsubscribeDetector
+ __OBJC_$_CLASS_PROP_LIST_EDAccountDeletionDiagnostics
+ __OBJC_$_INSTANCE_METHODS_EDAccountAuthentication
+ __OBJC_$_INSTANCE_METHODS_EDAccountDeletionDiagnostics
+ __OBJC_$_INSTANCE_METHODS_EDListUnsubscribeDetector
+ __OBJC_$_INSTANCE_METHODS__EDUnsubscribeInfo
+ __OBJC_$_INSTANCE_VARIABLES_EDAccountAuthentication
+ __OBJC_$_INSTANCE_VARIABLES_EDAccountDeletionDiagnostics
+ __OBJC_$_INSTANCE_VARIABLES_EDListUnsubscribeDetector
+ __OBJC_$_INSTANCE_VARIABLES__EDUnsubscribeInfo
+ __OBJC_$_PROP_LIST_EDAccountAuthentication
+ __OBJC_$_PROP_LIST_EDAccountDeletionDiagnostics
+ __OBJC_CLASS_PROTOCOLS_$_EDAccountDeletionDiagnostics
+ __OBJC_CLASS_RO_$_EDAccountAuthentication
+ __OBJC_CLASS_RO_$_EDAccountDeletionDiagnostics
+ __OBJC_CLASS_RO_$_EDListUnsubscribeDetector
+ __OBJC_CLASS_RO_$__EDUnsubscribeInfo
+ __OBJC_METACLASS_RO_$_EDAccountAuthentication
+ __OBJC_METACLASS_RO_$_EDAccountDeletionDiagnostics
+ __OBJC_METACLASS_RO_$_EDListUnsubscribeDetector
+ __OBJC_METACLASS_RO_$__EDUnsubscribeInfo
+ ___26-[EDVIPManager test_drain]_block_invoke
+ ___26-[EDVIPManager test_drain]_block_invoke_2
+ ___30+[EDAccountAuthentication log]_block_invoke
+ ___30-[EDThreadMigrator test_drain]_block_invoke
+ ___34-[EDThreadScopeManager test_drain]_block_invoke
+ ___35+[EDAccountDeletionDiagnostics log]_block_invoke
+ ___35-[EDMessageQueryHandler test_drain]_block_invoke
+ ___40-[EDMessageCountQueryHandler test_drain]_block_invoke
+ ___42-[EDInMemoryThreadQueryHandler test_drain]_block_invoke
+ ___45-[EDPrecomputedThreadQueryHandler test_drain]_block_invoke
+ ___45-[EDPrecomputedThreadQueryHandler test_drain]_block_invoke_2
+ ___46+[EDAccountDeletionDiagnostics sharedInstance]_block_invoke
+ ___48+[EDDataDetectionUtilities _lastWords:inString:]_block_invoke
+ ___64-[EDAccountDeletionDiagnostics notifyOfAccountRemovedFromIndex:]_block_invoke
+ ___69-[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]_block_invoke
+ ___69-[EDSearchableIndexPersistence markMessagesNeedingDownloadToReindex:]_block_invoke_2
+ ___71-[EDListUnsubscribeDetector commandForMessage:mailToOnly:dkimVerified:]_block_invoke
+ ___83-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]_block_invoke
+ ___83-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:trigger:]_block_invoke_2
+ ___87+[EDMessageListItemPredicates _mailboxURLSubpredicatesForPredicate:mailboxPersistence:]_block_invoke
+ ___87+[EDMessageListItemPredicates _mailboxURLSubpredicatesForPredicate:mailboxPersistence:]_block_invoke_2
+ ___87-[EDAccountDeletionDiagnostics _notificationContentForAccountDescription:deletionTime:]_block_invoke
+ ___93-[EDSearchableIndexPersistence _messagesRequiringIndexingForType:excludingIdentifiers:limit:]_block_invoke
+ ___EDBiomeSignalDonationQueue_block_invoke
+ ___EDOneTimeCodeVisibleCharacterSet_block_invoke
+ ___UserNotificationsLibraryCore_block_invoke
+ ___block_descriptor_40_ea8_32bs_e21_"NSPredicate"16?08ls32l8
+ ___block_descriptor_40_ea8_32s_e21_"NSPredicate"16?08ls32l8
+ ___block_descriptor_48_ea8_32s40s_e27_v16?0"MSRadarURLBuilder"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8
+ ___block_descriptor_48_ea8_32s_e9_16?0^8ls32l8
+ ___block_descriptor_72_ea8_32s40s48s_e14_"NSArray"8?0ls32l8s40l8s48l8
+ ___block_descriptor_88_ea8_32s40s48s56s64r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8r64l8s40l8s48l8s56l8
+ ___getUNMutableNotificationContentClass_block_invoke
+ ___getUNNotificationRequestClass_block_invoke
+ ___getUNTimeIntervalNotificationTriggerClass_block_invoke
+ ___getUNUserNotificationCenterClass_block_invoke
+ _associated conformance 17IndexingAnalytics9ItemEventO13UpdateTriggerOSHAASQ
+ _associated conformance 17IndexingAnalytics9ItemEventO13UpdateTriggerOs12CaseIterableAA8AllCasessAFP_Sl
+ _audit_stringUserNotifications
+ _getUNMutableNotificationContentClass.softClass
+ _getUNNotificationRequestClass.softClass
+ _getUNTimeIntervalNotificationTriggerClass.softClass
+ _getUNUserNotificationCenterClass.softClass
+ _objc_msgSend$_descriptionForAccount:
+ _objc_msgSend$_hostnamesHaveSameTopLevelDomain:deliveryAccount:
+ _objc_msgSend$_init
+ _objc_msgSend$_isEnabled
+ _objc_msgSend$_lastWords:inString:
+ _objc_msgSend$_listIDString:
+ _objc_msgSend$_mailboxURLSubpredicatesForPredicate:mailboxPersistence:
+ _objc_msgSend$_normalizedAddress:
+ _objc_msgSend$_notificationContentForAccountDescription:deletionTime:
+ _objc_msgSend$_persistentKeyForHeaders:
+ _objc_msgSend$_requestIdentifierForAccount:
+ _objc_msgSend$_senderString:
+ _objc_msgSend$_shouldAutoUpdateDeliveryAccount:forChangedReceivingAccount:
+ _objc_msgSend$_updateDeliveryAccountCredentialIfNecessaryForAccountWithAccount:
+ _objc_msgSend$_updateDeliveryAccountCredentialIfNecessaryForReceivingAccount:
+ _objc_msgSend$accountFactory
+ _objc_msgSend$accountWithSystemAccount:
+ _objc_msgSend$addNotificationRequest:withCompletionHandler:
+ _objc_msgSend$authenticationStateForAuthenticationResult:forMessage:fromSender:trustingServer:
+ _objc_msgSend$batchDidEnd:items:error:
+ _objc_msgSend$canAuthenticateWithCurrentCredentials
+ _objc_msgSend$commandForMessage:mailToOnly:dkimVerified:
+ _objc_msgSend$componentsWithURL:
+ _objc_msgSend$controlCharacterSet
+ _objc_msgSend$didRequestRedonationForItems:
+ _objc_msgSend$didUpdateMessagesAndRecordDonations:trigger:
+ _objc_msgSend$dkimSignatureHeaders
+ _objc_msgSend$enumerateSubstringsInRange:options:usingBlock:
+ _objc_msgSend$firstSenderAddress
+ _objc_msgSend$futureWithBlock:
+ _objc_msgSend$hasPasswordCredential
+ _objc_msgSend$idnaEncodedAddressForAddress:
+ _objc_msgSend$illegalCharacterSet
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithHeaders:
+ _objc_msgSend$initWithMutableDictionary:
+ _objc_msgSend$initWithPassword:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$listID
+ _objc_msgSend$listUnsubscribeCommands
+ _objc_msgSend$listUnsubscribePostContent
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:accountObjectID:headerUnsubscribeTypes:
+ _objc_msgSend$markMessagesNeedingDownloadToReindex:
+ _objc_msgSend$notificationCenter
+ _objc_msgSend$oneClickUnsubscribeCommandWithListID:sender:senderForUnsubscribeMessage:URL:postContent:headerUnsubscribeTypes:
+ _objc_msgSend$password
+ _objc_msgSend$radarURLWithBuilder:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$receivingAccountFromMessage:
+ _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:trigger:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$requestWithIdentifier:content:trigger:destinations:
+ _objc_msgSend$resolvedPolicyForIMAPHost:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$savePersistentAccount
+ _objc_msgSend$searchableMessageForBaseMessage:htmlContent:hasCompleteData:isEncrypted:includeEncryptedBody:
+ _objc_msgSend$sender
+ _objc_msgSend$senderForUnsubscribeMessage
+ _objc_msgSend$setAppendSysdiagnoseHowTo:
+ _objc_msgSend$setBody:
+ _objc_msgSend$setClassification:
+ _objc_msgSend$setComponent:
+ _objc_msgSend$setCredential:
+ _objc_msgSend$setDefaultActionURL:
+ _objc_msgSend$setKeywords:
+ _objc_msgSend$setRadarDescription:
+ _objc_msgSend$setReproducibility:
+ _objc_msgSend$sharedDictionaryWithIdentifier:
+ _objc_msgSend$shouldIgnoreMessageWithHeaders:
+ _objc_msgSend$signedHeaderFields
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$stringFromDate:timeZone:formatOptions:
+ _objc_msgSend$test_drain
+ _objc_msgSend$thinOldEvents
+ _objc_msgSend$toRecipients
+ _objc_msgSend$triggerWithTimeInterval:repeats:
+ _objc_msgSend$verificationContextForMessageData:error:
+ _objc_msgSend$verifyMessageWithContext:options:error:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _sharedInstance.sharedInstance
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
- -[EDSearchableIndexAttachmentItem attributeSetForFilePromise]
- -[EDSearchableIndexAttachmentItem setAttributeSetForFilePromise:]
- -[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]
- _OBJC_CLASS_$_EDInteractionEventLogLegacyPersistentBitsProvider
- _OBJC_CLASS_$_EMListUnsubscribeDetector
- _OBJC_IVAR_$_EDSearchableIndexAttachmentItem._attributeSetForFilePromise
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
- ___75-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]_block_invoke
- ___75-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]_block_invoke_2
- ___76-[EDInteractionEventLogLegacyPersistentBitsProvider _findExistingSaltError:]_block_invoke
- ___block_descriptor_80_ea8_32s40s48s56s64r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8r64l8s40l8s48l8s56l8
- ___swift_memcpy2_1
- _objc_msgSend$_oldSalt
- _objc_msgSend$batchDidEnd:error:
- _objc_msgSend$defaultPolicy
- _objc_msgSend$defaultPolicyForIMAPHost:
- _objc_msgSend$didDonateItems:
- _objc_msgSend$didFailToDonateItems:
- _objc_msgSend$didUpdateMessagesAndRecordDonations:
- _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:
CStrings:
+ " NOT IN\n       ( "
+ "$1$2"
+ "%@,%@,%@"
+ ")\n                AS is_update,\n            "
+ "-[EDInMemoryThreadQueryHandler test_drain]"
+ "-[EDMessageCountQueryHandler test_drain]"
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
+ "Class getUNMutableNotificationContentClass(void)_block_invoke"
+ "Class getUNNotificationRequestClass(void)_block_invoke"
+ "Class getUNTimeIntervalNotificationTriggerClass(void)_block_invoke"
+ "Class getUNUserNotificationCenterClass(void)_block_invoke"
+ "EDAccountDeletionDiagnostics.m"
+ "EDListUnsubscribeDetector.m"
+ "EDThreadMigrator.m"
+ "EDThreadScopeManager.m"
+ "EmailDaemon/EDSearchableIndexAnalyticsPersistence.swift"
+ "Failed to schedule account deletion diagnostics notification: %{public}@"
+ "Ignoring server authentication results for denylisted provider for message: %{public}@"
+ "L:%@"
+ "Mail Account Deleted"
+ "Mail just removed: %@. If this wasn't intentional, tap to file a Radar. Internal Only."
+ "Mail received an account-deletion request the user did not recognize as intentional.\n\nAccount: %@\nDeletion time: %@"
+ "Marked %{public}@ messages as needing download to re-donate"
+ "Marking messages as needing download to reindex"
+ "No delivery account password found. Nothing to do"
+ "Received unhandled update trigger "
+ "Receiving account password changed: %@"
+ "Resolved download policy for account %{public}s host=%s quota=%{public}s"
+ "Resolving download policy for account %{public}s with no hostname, expected an IMAP account"
+ "S:%@"
+ "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL THEN 1 ELSE 0 END) AS indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed THEN 1 ELSE 0 END) AS message_bodies_indexed,       SUM(CASE WHEN searchable_messages.transaction_id IN (%lld, %lld) THEN 1 ELSE 0 END) AS messages_to_redonate       %@  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %@"
+ "Scheduled account deletion diagnostics notification %{public}@"
+ "SearchableIndexDownloadPolicy"
+ "Should not try to update delivery account password"
+ "Thinning old batches"
+ "Thinning old identified events"
+ "UNMutableNotificationContent"
+ "UNNotificationRequest"
+ "UNTimeIntervalNotificationTrigger"
+ "UNUserNotificationCenter"
+ "UPDATE OR IGNORE searchable_messages   SET transaction_id = %lld WHERE transaction_id = %lld   AND message_id IN (SELECT value FROM json_each(:message_ids)) RETURNING message_id"
+ "Unexpected Mail account deletion"
+ "Updating password for %@ did not work. Reverting password"
+ "Updating password worked for delivery account: %@"
+ "^[^<>]*<([^>]+)>\\s*$|^(.+)$"
+ "accepted"
+ "account deletion, accountsd"
+ "com.apple.mail.biome-signal-donation"
+ "com.apple.mail.listUnsubscribeInfo"
+ "com.apple.mobilemail.accountDeletionDiagnostics."
+ "command"
+ "deny"
+ "ignored"
+ "mailto"
+ "message-authentication-provider-info"
+ "policy"
+ "softlink:r:path:/System/Library/Frameworks/UserNotifications.framework/UserNotifications"
+ "thinEvents(before:)"
+ "v16@?0@\"MSRadarURLBuilder\"8"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
+ "void *UserNotificationsLibrary(void)"
- "\n                AS is_update,\n            "
- "%@,%@"
- "-[EDSearchableIndexPersistence recordMessagesNeedToBeDonated:indexingType:]"
- "<null>"
- "Error finding existing old salt: %d"
- "Failed to read old salt %{public}@"
- "Found existing old salt"
- "No old salt found"
- "Resolved per-host policy for account %{public}s host=%{public}s quota=%{public}s"
- "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL THEN 1 ELSE 0 END) AS indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed THEN 1 ELSE 0 END) AS message_bodies_indexed,       SUM(CASE WHEN searchable_messages.transaction_id = %lld THEN 1 ELSE 0 END) AS messages_to_redonate       %@  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %@"
- "Warning: about to index message with an empty subject. %{public}@"
- "hasCompleteContent"
- "hasHeaders"
- "mailboxtype"
```

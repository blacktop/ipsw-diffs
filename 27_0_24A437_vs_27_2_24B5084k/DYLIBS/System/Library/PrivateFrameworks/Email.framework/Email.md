## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3901.100.1.2.14
-  __TEXT.__text: 0xd55c0
-  __TEXT.__objc_methlist: 0xd0ac
-  __TEXT.__gcc_except_tab: 0x1b088
-  __TEXT.__const: 0x18dc
-  __TEXT.__cstring: 0xc37f
-  __TEXT.__oslogstring: 0x6913
-  __TEXT.__dlopen_cstrs: 0x160
+3901.200.34.0.0
+  __TEXT.__text: 0xd3860
+  __TEXT.__objc_methlist: 0xcd6c
+  __TEXT.__const: 0x18c2
+  __TEXT.__gcc_except_tab: 0x1ac7c
+  __TEXT.__cstring: 0xc369
   __TEXT.__ustring: 0x170
+  __TEXT.__oslogstring: 0x67e3
+  __TEXT.__dlopen_cstrs: 0x160
   __TEXT.__swift5_typeref: 0x4aa
   __TEXT.__constg_swiftt: 0x538
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x40f
+  __TEXT.__swift5_reflstr: 0x41f
   __TEXT.__swift5_fieldmd: 0x610
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0x130

   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x85b8
+  __TEXT.__unwind_info: 0x8470
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4610
-  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__const: 0x45e8
+  __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x340
+  __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62b8
-  __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_selrefs: 0x6108
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0xc98
-  __AUTH_CONST.__const: 0x1ea0
-  __AUTH_CONST.__cfstring: 0xa560
-  __AUTH_CONST.__objc_const: 0x16f60
+  __DATA_CONST.__got: 0xc50
+  __AUTH_CONST.__const: 0x1f40
+  __AUTH_CONST.__cfstring: 0xa400
+  __AUTH_CONST.__objc_const: 0x169e8
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xbc8
   __AUTH.__objc_data: 0x200
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xc4c
-  __DATA.__data: 0x2a40
-  __DATA_DIRTY.__objc_data: 0x3808
+  __DATA.__objc_ivar: 0xc34
+  __DATA.__data: 0x28c0
+  __DATA_DIRTY.__objc_data: 0x3718
   __DATA_DIRTY.__data: 0x250
-  __DATA_DIRTY.__bss: 0xad0
+  __DATA_DIRTY.__bss: 0xac0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5173
-  Symbols:   11381
-  CStrings:  2166
+  Functions: 5140
+  Symbols:   11252
+  CStrings:  2151
 
Symbols:
+ +[EMListUnsubscribeCommand mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:accountObjectID:headerUnsubscribeTypes:]
+ -[EMListUnsubscribeMailtoValues accountObjectID]
+ -[EMListUnsubscribeMailtoValues initWithAddresss:subject:body:accountObjectID:]
+ -[EMMailboxCategoryCloudStorage test_drain]
+ -[EMMailboxScope initWithMailboxObjectIDs:forExclusion:]
+ -[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]
+ -[EMUbiquitouslyPersistedDictionary test_drainMutations]
+ _OBJC_IVAR_$_EMListUnsubscribeMailtoValues._accountObjectID
+ __OBJC_$_CATEGORY_NSArray_$_EMSmartMailbox
+ __OBJC_$_INSTANCE_METHODS_NSArray(EMSmartMailbox|EMMessageListItem|EMSender)
+ ___43-[EMMailboxCategoryCloudStorage test_drain]_block_invoke
+ ___56-[EMUbiquitouslyPersistedDictionary test_drainMutations]_block_invoke
+ ___56-[EMUbiquitouslyPersistedDictionary test_drainMutations]_block_invoke_2
+ ___56-[EMUbiquitouslyPersistedDictionary test_drainMutations]_block_invoke_3
+ ___68-[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]_block_invoke
+ ___68-[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]_block_invoke_2
+ ___68-[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]_block_invoke_3
+ ___68-[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]_block_invoke_4
+ _objc_msgSend$accountObjectID
+ _objc_msgSend$initWithAddresss:subject:body:accountObjectID:
+ _objc_msgSend$initWithMailboxObjectIDs:forExclusion:
- +[EMAccountAuthentication log]
- +[EMListUnsubscribeCommand _accountWithIdentifier:]
- +[EMListUnsubscribeCommand accountFinderBlock]
- +[EMListUnsubscribeCommand mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:account:headerUnsubscribeTypes:]
- +[EMListUnsubscribeCommand setAccountFinderBlock:]
- +[EMListUnsubscribeDetector _validateHeaders:dkimVerified:]
- +[EMListUnsubscribeDetector receivingAccountFromMessage:]
- +[EMListUnsubscribeDetector unsubscribeTypeForHeader:]
- +[EMListUnsubscribeDetector validatedUnsubscribeTypeForHeader:dkimVerified:]
- -[EMAccountAuthentication .cxx_destruct]
- -[EMAccountAuthentication _hostnamesHaveSameTopLevelDomain:deliveryAccount:]
- -[EMAccountAuthentication _shouldAutoUpdateDeliveryAccount:forChangedReceivingAccount:]
- -[EMAccountAuthentication _updateDeliveryAccountCredentialIfNecessaryForAccountWithAccount:]
- -[EMAccountAuthentication _updateDeliveryAccountCredentialIfNecessaryForReceivingAccount:]
- -[EMAccountAuthentication accountFactory]
- -[EMAccountAuthentication initWithAccountFactory:]
- -[EMAccountAuthentication updateDeliveryAccountCredentialIfNecessaryForAccountWithIdentifier:]
- -[EMAccountAuthentication updateDeliveryAccountCredentialIfNecessaryForAccountWithSystemAccount:]
- -[EMHideMyEmail isConfiguredForAccountWithAltDSID:error:]
- -[EMListUnsubscribeDetector .cxx_destruct]
- -[EMListUnsubscribeDetector _listIDString:]
- -[EMListUnsubscribeDetector _normalizedAddress:]
- -[EMListUnsubscribeDetector _persistentKeyForHeaders:]
- -[EMListUnsubscribeDetector _senderString:]
- -[EMListUnsubscribeDetector acceptCommand:]
- -[EMListUnsubscribeDetector commandForMessage:dkimVerified:]
- -[EMListUnsubscribeDetector commandForMessage:mailToOnly:dkimVerified:]
- -[EMListUnsubscribeDetector ignoreCommand:]
- -[EMListUnsubscribeDetector initWithMutableDictionary:]
- -[EMListUnsubscribeDetector init]
- -[EMListUnsubscribeDetector removeAllPersistedCommands]
- -[EMListUnsubscribeDetector shouldIgnoreMessageWithHeaders:]
- -[EMListUnsubscribeMailtoValues account]
- -[EMListUnsubscribeMailtoValues initWithAddresss:subject:body:account:]
- -[EMMailDropMetadata isBannerWithMultiple]
- -[EMUbiquitouslyPersistedDictionary _waitForPendingMutationsForTesting]
- -[_EMUnsubscribeInfo .cxx_destruct]
- -[_EMUnsubscribeInfo initWithHeaders:]
- -[_EMUnsubscribeInfo setMailtoURL:]
- -[_EMUnsubscribeInfo setPostContent:]
- -[_EMUnsubscribeInfo setPostURL:]
- _ECMessageHeaderKeyListID
- _ECMessageHeaderKeyListUnsubscribe
- _ECMessageHeaderKeyListUnsubscribePost
- _OBJC_CLASS_$_ACAccountCredential
- _OBJC_CLASS_$_ECDKIMVerifier
- _OBJC_CLASS_$_EMAccountAuthentication
- _OBJC_CLASS_$_EMListUnsubscribeDetector
- _OBJC_CLASS_$__EMUnsubscribeInfo
- _OBJC_IVAR_$_EMAccountAuthentication._accountFactory
- _OBJC_IVAR_$_EMListUnsubscribeDetector._persistentDictionary
- _OBJC_IVAR_$_EMListUnsubscribeMailtoValues._account
- _OBJC_IVAR_$_EMListUnsubscribeMailtoValues._accountIdentifier
- _OBJC_IVAR_$__EMUnsubscribeInfo._mailtoURL
- _OBJC_IVAR_$__EMUnsubscribeInfo._postContent
- _OBJC_IVAR_$__EMUnsubscribeInfo._postURL
- _OBJC_METACLASS_$_EMAccountAuthentication
- _OBJC_METACLASS_$_EMListUnsubscribeDetector
- _OBJC_METACLASS_$__EMUnsubscribeInfo
- __OBJC_$_CATEGORY_NSArray_$_EMMessageListItem
- __OBJC_$_CLASS_METHODS_EMAccountAuthentication
- __OBJC_$_CLASS_METHODS_EMListUnsubscribeDetector
- __OBJC_$_INSTANCE_METHODS_EMAccountAuthentication
- __OBJC_$_INSTANCE_METHODS_EMListUnsubscribeDetector
- __OBJC_$_INSTANCE_METHODS_NSArray(EMMessageListItem|EMSender|EMSmartMailbox)
- __OBJC_$_INSTANCE_METHODS__EMUnsubscribeInfo
- __OBJC_$_INSTANCE_VARIABLES_EMAccountAuthentication
- __OBJC_$_INSTANCE_VARIABLES_EMListUnsubscribeDetector
- __OBJC_$_INSTANCE_VARIABLES__EMUnsubscribeInfo
- __OBJC_$_PROP_LIST_ECMailAccount
- __OBJC_$_PROP_LIST_EDAccount
- __OBJC_$_PROP_LIST_EDReceivingAccount
- __OBJC_$_PROP_LIST_EMAccountAuthentication
- __OBJC_$_PROP_LIST_NSArray_$_EMMessageListItem
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ECAccountPropertyProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ECMailAccount
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDAccount
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDReceivingAccount
- __OBJC_$_PROTOCOL_METHOD_TYPES_ECAccountPropertyProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_ECMailAccount
- __OBJC_$_PROTOCOL_METHOD_TYPES_EDAccount
- __OBJC_$_PROTOCOL_METHOD_TYPES_EDReceivingAccount
- __OBJC_$_PROTOCOL_REFS_ECMailAccount
- __OBJC_$_PROTOCOL_REFS_EDAccount
- __OBJC_$_PROTOCOL_REFS_EDReceivingAccount
- __OBJC_CLASS_RO_$_EMAccountAuthentication
- __OBJC_CLASS_RO_$_EMListUnsubscribeDetector
- __OBJC_CLASS_RO_$__EMUnsubscribeInfo
- __OBJC_LABEL_PROTOCOL_$_ECAccountPropertyProviding
- __OBJC_LABEL_PROTOCOL_$_ECMailAccount
- __OBJC_LABEL_PROTOCOL_$_EDAccount
- __OBJC_LABEL_PROTOCOL_$_EDReceivingAccount
- __OBJC_METACLASS_RO_$_EMAccountAuthentication
- __OBJC_METACLASS_RO_$_EMListUnsubscribeDetector
- __OBJC_METACLASS_RO_$__EMUnsubscribeInfo
- __OBJC_PROTOCOL_$_ECAccountPropertyProviding
- __OBJC_PROTOCOL_$_ECMailAccount
- __OBJC_PROTOCOL_$_EDAccount
- __OBJC_PROTOCOL_$_EDReceivingAccount
- __OBJC_PROTOCOL_REFERENCE_$_EDReceivingAccount
- ___30+[EMAccountAuthentication log]_block_invoke
- ___71-[EMListUnsubscribeDetector commandForMessage:mailToOnly:dkimVerified:]_block_invoke
- ___71-[EMUbiquitouslyPersistedDictionary _waitForPendingMutationsForTesting]_block_invoke
- ___71-[EMUbiquitouslyPersistedDictionary _waitForPendingMutationsForTesting]_block_invoke_2
- ___71-[EMUbiquitouslyPersistedDictionary _waitForPendingMutationsForTesting]_block_invoke_3
- ___block_descriptor_48_ea8_32s_e9_16?0^8ls32l8
- _objc_msgSend$_accountWithIdentifier:
- _objc_msgSend$_hostnamesHaveSameTopLevelDomain:deliveryAccount:
- _objc_msgSend$_listIDString:
- _objc_msgSend$_normalizedAddress:
- _objc_msgSend$_persistentKeyForHeaders:
- _objc_msgSend$_senderString:
- _objc_msgSend$_shouldAutoUpdateDeliveryAccount:forChangedReceivingAccount:
- _objc_msgSend$_updateDeliveryAccountCredentialIfNecessaryForAccountWithAccount:
- _objc_msgSend$_updateDeliveryAccountCredentialIfNecessaryForReceivingAccount:
- _objc_msgSend$accountFactory
- _objc_msgSend$accountFinderBlock
- _objc_msgSend$accountWithIdentifier:
- _objc_msgSend$accountWithSystemAccount:
- _objc_msgSend$canAuthenticateWithCurrentCredentials
- _objc_msgSend$commandForMessage:mailToOnly:dkimVerified:
- _objc_msgSend$componentsWithURL:
- _objc_msgSend$dkimSignatureHeaders
- _objc_msgSend$encodedHeaders
- _objc_msgSend$firstHeaderForKey:
- _objc_msgSend$firstSenderAddress
- _objc_msgSend$futureWithBlock:
- _objc_msgSend$hasPasswordCredential
- _objc_msgSend$idnaEncodedAddressForAddress:
- _objc_msgSend$initWithAddresss:subject:body:account:
- _objc_msgSend$initWithMutableDictionary:
- _objc_msgSend$initWithPassword:
- _objc_msgSend$listUnsubscribeCommands
- _objc_msgSend$listUnsubscribePostContent
- _objc_msgSend$mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:account:headerUnsubscribeTypes:
- _objc_msgSend$oneClickUnsubscribeCommandWithListID:sender:senderForUnsubscribeMessage:URL:postContent:headerUnsubscribeTypes:
- _objc_msgSend$password
- _objc_msgSend$receivingAccountFromMessage:
- _objc_msgSend$resultWithTimeout:error:
- _objc_msgSend$savePersistentAccount
- _objc_msgSend$setCredential:
- _objc_msgSend$sharedDictionaryWithIdentifier:
- _objc_msgSend$shouldIgnoreMessageWithHeaders:
- _objc_msgSend$signedHeaderFields
- _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
- _objc_msgSend$systemAccount
- _objc_msgSend$toRecipients
- _objc_msgSend$verificationContextForMessageData:error:
- _objc_msgSend$verifyMessageWithContext:options:error:
- _sAccountFinderBlock
CStrings:
+ "-[EMMailboxCategoryCloudStorage test_drain]"
+ "-[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]"
+ "-[EMUbiquitouslyPersistedDictionary test_drainMutations]"
+ "EFPropertyKey_accountObjectID"
+ "EMMailboxCategoryCloudStorage.m"
+ "Hide My Email address %{public}@ is NOT available in the list of %lu HME addresses"
+ "Hide My Email address %{public}@ is available in the list of %lu HME addresses"
+ "The checking for HME address %{public}@ is valid failed (%lu HME addresses found): %{public}@, adding telemetry for isHideMyEmailAddressValid session"
- "$1$2"
- "<%{public}@> Timeout validating headers for: %@"
- "@16@?0^@8"
- "Account is not a receiving account. No delivery account to update: %@"
- "Attempt to update password if needed for delivery account %@"
- "EFPropertyKey_account.identifier"
- "EMListUnsubscribeDetector.m"
- "Hide My Email address is available: %{BOOL}d in the list of HME addresses"
- "L:%@"
- "No delivery account password found. Nothing to do"
- "Receiving account password changed: %@"
- "S:%@"
- "Should not try to update delivery account password"
- "The checking for HME address is valid failed:%{public}@, adding telemetry for isHideMyEmailAddressValid session"
- "Updating password for %@ did not work. Reverting password"
- "Updating password worked for delivery account: %@"
- "^[^<>]*<([^>]+)>\\s*$|^(.+)$"
- "accepted"
- "accountFinderBlock is not set"
- "com.apple.mail.listUnsubscribeInfo"
- "dictionary"
- "failed to find an account for identifier"
- "ignored"
```

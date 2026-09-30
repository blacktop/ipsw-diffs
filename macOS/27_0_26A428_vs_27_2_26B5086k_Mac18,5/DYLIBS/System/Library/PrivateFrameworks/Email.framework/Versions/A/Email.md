## Email

> `/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email`

```diff

-3901.100.1.1.11
-  __TEXT.__text: 0xed140
-  __TEXT.__objc_methlist: 0xd9cc
-  __TEXT.__gcc_except_tab: 0x1c158
-  __TEXT.__const: 0x18ec
-  __TEXT.__cstring: 0xca6f
-  __TEXT.__oslogstring: 0x6d23
-  __TEXT.__dlopen_cstrs: 0x160
+3901.200.34.0.0
+  __TEXT.__text: 0xeb1c0
+  __TEXT.__objc_methlist: 0xd68c
+  __TEXT.__const: 0x18d2
+  __TEXT.__gcc_except_tab: 0x1bd54
+  __TEXT.__cstring: 0xca59
   __TEXT.__ustring: 0x170
+  __TEXT.__oslogstring: 0x6c03
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
-  __TEXT.__unwind_info: 0x8940
+  __TEXT.__unwind_info: 0x87d8
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x19e8
-  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x340
+  __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6920
-  __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x6770
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0xd68
-  __AUTH_CONST.__const: 0x5560
-  __AUTH_CONST.__cfstring: 0xabe0
-  __AUTH_CONST.__objc_const: 0x17e58
+  __DATA_CONST.__got: 0xd20
+  __AUTH_CONST.__const: 0x55d0
+  __AUTH_CONST.__cfstring: 0xaa80
+  __AUTH_CONST.__objc_const: 0x178e0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xaa0
   __AUTH.__objc_data: 0x2f0
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xd14
-  __DATA.__data: 0x2a00
-  __DATA_DIRTY.__objc_data: 0x3858
+  __DATA.__objc_ivar: 0xcfc
+  __DATA.__data: 0x2880
+  __DATA_DIRTY.__objc_data: 0x3768
   __DATA_DIRTY.__data: 0x268
-  __DATA_DIRTY.__bss: 0xce0
+  __DATA_DIRTY.__bss: 0xcd0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5432
-  Symbols:   11988
-  CStrings:  2245
+  Functions: 5399
+  Symbols:   11858
+  CStrings:  2230
 
Symbols:
+ +[EMListUnsubscribeCommand mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:accountObjectID:headerUnsubscribeTypes:]
+ -[EMListUnsubscribeMailtoValues accountObjectID]
+ -[EMListUnsubscribeMailtoValues initWithAddresss:subject:body:accountObjectID:]
+ -[EMMailboxCategoryCloudStorage test_drain]
+ -[EMMailboxScope initWithMailboxObjectIDs:forExclusion:]
+ -[EMMessageRepository loadOlderItemsForObservationIdentifier:mailboxesToLoad:]
+ -[EMUbiquitouslyPersistedDictionary test_drainDelegateNotifications]
+ -[EMUbiquitouslyPersistedDictionary test_drainMutations]
+ OBJC_IVAR_$_EMListUnsubscribeMailtoValues._accountObjectID
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
+ _objc_msgSend$loadOlderItemsForObservationIdentifier:mailboxesToLoad:
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
- -[EMMessageRepository loadOlderItemsForObservationIdentifier:]
- -[EMUbiquitouslyPersistedDictionary _waitForPendingMutationsForTesting]
- -[_EMUnsubscribeInfo .cxx_destruct]
- -[_EMUnsubscribeInfo initWithHeaders:]
- -[_EMUnsubscribeInfo setMailtoURL:]
- -[_EMUnsubscribeInfo setPostContent:]
- -[_EMUnsubscribeInfo setPostURL:]
- OBJC_IVAR_$_EMAccountAuthentication._accountFactory
- OBJC_IVAR_$_EMListUnsubscribeDetector._persistentDictionary
- OBJC_IVAR_$_EMListUnsubscribeMailtoValues._account
- OBJC_IVAR_$_EMListUnsubscribeMailtoValues._accountIdentifier
- OBJC_IVAR_$__EMUnsubscribeInfo._mailtoURL
- OBJC_IVAR_$__EMUnsubscribeInfo._postContent
- OBJC_IVAR_$__EMUnsubscribeInfo._postURL
- _ECMessageHeaderKeyListID
- _ECMessageHeaderKeyListUnsubscribe
- _ECMessageHeaderKeyListUnsubscribePost
- _OBJC_CLASS_$_ACAccountCredential
- _OBJC_CLASS_$_ECDKIMVerifier
- _OBJC_CLASS_$_EMAccountAuthentication
- _OBJC_CLASS_$_EMListUnsubscribeDetector
- _OBJC_CLASS_$__EMUnsubscribeInfo
- _OBJC_METACLASS_$_EMAccountAuthentication
- _OBJC_METACLASS_$_EMListUnsubscribeDetector
- _OBJC_METACLASS_$__EMUnsubscribeInfo
- __68-[EMHideMyEmail isHideMyEmailAddressValid:senderAddress:completion:]_block_invoke_2
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
- ___block_descriptor_48_ea8_32s_e9_16?0^8l
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
- _objc_msgSend$loadOlderItemsForObservationIdentifier:
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

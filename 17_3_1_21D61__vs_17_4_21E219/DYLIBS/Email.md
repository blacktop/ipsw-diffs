## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0x97450
+3774.500.171.2.2
+  __TEXT.__text: 0x97568
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x87c4
-  __TEXT.__gcc_except_tab: 0x13848
+  __TEXT.__objc_methlist: 0x87cc
+  __TEXT.__gcc_except_tab: 0x1384c
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x7b20
+  __TEXT.__cstring: 0x7b77
   __TEXT.__oslogstring: 0x3fdd
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x6180
+  __TEXT.__unwind_info: 0x6184
   __TEXT.__objc_classname: 0x1748
-  __TEXT.__objc_methname: 0x16a06
-  __TEXT.__objc_methtype: 0x3f30
-  __TEXT.__objc_stubs: 0xf200
+  __TEXT.__objc_methname: 0x16a4e
+  __TEXT.__objc_methtype: 0x3f46
+  __TEXT.__objc_stubs: 0xf220
   __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x3480
+  __DATA_CONST.__const: 0x3490
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x11448
-  __DATA_CONST.__objc_selrefs: 0x4e90
+  __DATA_CONST.__objc_selrefs: 0x4e98
+  __DATA_CONST.__objc_protorefs: 0x100
+  __DATA_CONST.__objc_classrefs: 0x780
+  __DATA_CONST.__objc_superrefs: 0x3b0
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x71a0
+  __AUTH_CONST.__cfstring: 0x71e0
   __AUTH_CONST.__objc_const: 0x4880
   __AUTH_CONST.__const: 0xd80
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_protorefs: 0x100
-  __DATA.__objc_classrefs: 0x780
-  __DATA.__objc_superrefs: 0x3b0
+  __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x9e4
-  __DATA.__data: 0x22b0
-  __DATA.__bss: 0xd8
-  __DATA_DIRTY.__objc_data: 0x27b0
+  __DATA.__data: 0x22c0
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x2800
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x500
+  __DATA_DIRTY.__bss: 0x4e8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAF164C1-F50D-3C00-8728-5D75F59A67AF
-  Functions: 3552
-  Symbols:   14466
-  CStrings:  6785
+  UUID: FB30AB2C-1BF0-3A7A-AD46-9B2A9753CB91
+  Functions: 3553
+  Symbols:   14471
+  CStrings:  6793
 
Symbols:
+ +[EMSMIMEUtilities _encryptionLevelForSender:]
+ +[EMSMIMEUtilities encryptionLevelForSender:forAdvertisement:useGCM:encryptSubject:]
+ _EMUserDefaultAdoptMessageSecurity
+ _EMUserDefaultSimulateDelayedFreeSpaceStatus
+ _EMUserDefaultSimulateDelayedFreeSpaceStatusTime
+ __OBJC_$_PROP_LIST_EMObject.79
+ __OBJC_$_PROP_LIST_EMRepositoryObject.54
+ __OBJC_$_PROP_LIST_EMUserProfileProvider.131
+ __OBJC_$_PROP_LIST_EMVIPManager.165
+ ___102-[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:]_block_invoke.140
+ ___43-[EMOutgoingMessageRepository isProcessing]_block_invoke.157
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.421
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.421.cold.1
+ ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.305
+ ___48-[EMMailboxRepository remoteAllMailboxObjectIDs]_block_invoke.99
+ ___48-[EMMessageRepository _blockedSendersDidChange:]_block_invoke.450
+ ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.302
+ ___52-[EMVIPManager _startObservingVIPChangesIfNecessary]_block_invoke.86
+ ___54-[EMAccountRepository _fetchAccountsAndObserveChanges]_block_invoke.81
+ ___54-[EMAccountRepository _fetchAccountsAndObserveChanges]_block_invoke.81.cold.1
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.443
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.443.cold.1
+ ___54-[EMOutgoingMessageRepository numberOfPendingMessages]_block_invoke.158
+ ___54-[EMOutgoingMessageRepository numberOfPendingMessages]_block_invoke.158.cold.1
+ ___54-[EMOutgoingMessageRepository numberOfPendingMessages]_block_invoke.161
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.429
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.432
+ ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.416
+ ___59-[EMMailboxRepository remoteMailboxTypeForMailboxObjectID:]_block_invoke.105
+ ___60-[EMMailboxRepository remoteMailboxObjectIDsForMailboxType:]_block_invoke.104
+ ___61-[EMContentRepresentation _distantLoaderBlockForContentItem:]_block_invoke.149
+ ___63-[EMMailboxRepository _startObservingMailboxChangesIfNecessary]_block_invoke.88
+ ___64-[EMOutgoingMessageRepository outboxContainsMessageFromAccount:]_block_invoke.150
+ ___66-[EMRemoteContentURLSession URLSession:task:didCompleteWithError:]_block_invoke.206
+ ___66-[EMRemoteContentURLSession URLSession:task:didCompleteWithError:]_block_invoke.208
+ ___70-[EMOutgoingMessageRepository _startObservingUnsentChangesIfNecessary]_block_invoke.167
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.214
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.217
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.219
+ ___88-[EMMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.404
+ ___block_literal_global.109
+ ___block_literal_global.133
+ ___block_literal_global.160
+ ___block_literal_global.164
+ ___block_literal_global.192
+ ___block_literal_global.227
+ ___block_literal_global.232
+ ___block_literal_global.236
+ ___block_literal_global.242
+ ___block_literal_global.248
+ ___block_literal_global.307
+ ___block_literal_global.342
+ ___block_literal_global.393
+ ___block_literal_global.407
+ ___block_literal_global.411
+ ___block_literal_global.415
+ ___block_literal_global.424
+ ___block_literal_global.428
+ ___block_literal_global.444
+ ___block_literal_global.453
+ ___block_literal_global.456
+ ___block_literal_global.56
+ ___block_literal_global.58
+ ___block_literal_global.61
+ ___block_literal_global.77
+ ___block_literal_global.88
+ ___block_literal_global.99
+ __unnamed_array_storage.112
+ _cachedSelf.onceToken.54
+ _cachedSelf.sTableLock.52
+ _cachedSelf.sUniqueObjectIDs.53
+ _objc_msgSend$_encryptionLevelForSender:
- +[EMSMIMEUtilities determineAdvertisedEncryptionTypeFor:]
- _EMUserDefaultEncryptedMail
- __OBJC_$_PROP_LIST_EMObject.78
- __OBJC_$_PROP_LIST_EMRepositoryObject.53
- __OBJC_$_PROP_LIST_EMUserProfileProvider.130
- __OBJC_$_PROP_LIST_EMVIPManager.164
- ___102-[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:]_block_invoke.139
- ___43-[EMOutgoingMessageRepository isProcessing]_block_invoke.156
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.420
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.420.cold.1
- ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.304
- ___48-[EMMailboxRepository remoteAllMailboxObjectIDs]_block_invoke.98
- ___48-[EMMessageRepository _blockedSendersDidChange:]_block_invoke.449
- ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.301
- ___52-[EMVIPManager _startObservingVIPChangesIfNecessary]_block_invoke.85
- ___54-[EMAccountRepository _fetchAccountsAndObserveChanges]_block_invoke.80
- ___54-[EMAccountRepository _fetchAccountsAndObserveChanges]_block_invoke.80.cold.1
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.442
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.442.cold.1
- ___54-[EMOutgoingMessageRepository numberOfPendingMessages]_block_invoke.157
- ___54-[EMOutgoingMessageRepository numberOfPendingMessages]_block_invoke.157.cold.1
- ___54-[EMOutgoingMessageRepository numberOfPendingMessages]_block_invoke.160
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.428
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.431
- ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.415
- ___59-[EMMailboxRepository remoteMailboxTypeForMailboxObjectID:]_block_invoke.104
- ___60-[EMMailboxRepository remoteMailboxObjectIDsForMailboxType:]_block_invoke.103
- ___61-[EMContentRepresentation _distantLoaderBlockForContentItem:]_block_invoke.148
- ___63-[EMMailboxRepository _startObservingMailboxChangesIfNecessary]_block_invoke.87
- ___64-[EMOutgoingMessageRepository outboxContainsMessageFromAccount:]_block_invoke.149
- ___66-[EMRemoteContentURLSession URLSession:task:didCompleteWithError:]_block_invoke.205
- ___66-[EMRemoteContentURLSession URLSession:task:didCompleteWithError:]_block_invoke.207
- ___70-[EMOutgoingMessageRepository _startObservingUnsentChangesIfNecessary]_block_invoke.166
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.213
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.216
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.218
- ___88-[EMMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.403
- ___block_literal_global.132
- ___block_literal_global.163
- ___block_literal_global.191
- ___block_literal_global.226
- ___block_literal_global.231
- ___block_literal_global.235
- ___block_literal_global.241
- ___block_literal_global.247
- ___block_literal_global.306
- ___block_literal_global.341
- ___block_literal_global.392
- ___block_literal_global.406
- ___block_literal_global.410
- ___block_literal_global.414
- ___block_literal_global.423
- ___block_literal_global.427
- ___block_literal_global.443
- ___block_literal_global.452
- ___block_literal_global.455
- ___block_literal_global.55
- ___block_literal_global.57
- ___block_literal_global.60
- ___block_literal_global.67
- ___block_literal_global.76
- ___block_literal_global.87
- ___block_literal_global.90
- ___block_literal_global.98
- __unnamed_array_storage.111
- _cachedSelf.onceToken.53
- _cachedSelf.sTableLock.51
- _cachedSelf.sUniqueObjectIDs.52
CStrings:
+ "AdoptMessageSecurity"
+ "Q44@0:8@16B24^B28^B36"
+ "SimulateDelayedFreeSpaceStatus"
+ "SimulateDelayedFreeSpaceStatusTime"
+ "T@\"NSString\",?,R,C"
+ "_encryptionLevelForSender:"
+ "encryptionLevelForSender:forAdvertisement:useGCM:encryptSubject:"
- "determineAdvertisedEncryptionTypeFor:"

```

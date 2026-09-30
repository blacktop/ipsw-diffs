## NanoMailKitServer

> `/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer`

```diff

-845.0.0.0.0
-  __TEXT.__text: 0x774d8
+846.0.0.0.0
+  __TEXT.__text: 0x76e8c
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x94a4
+  __TEXT.__objc_methlist: 0x942c
   __TEXT.__const: 0x5b6
   __TEXT.__cstring: 0x4b58
   __TEXT.__oslogstring: 0x824a
   __TEXT.__gcc_except_tab: 0x3ac
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1808
-  __TEXT.__objc_classname: 0xdf3
-  __TEXT.__objc_methname: 0x11ef2
-  __TEXT.__objc_methtype: 0x3456
-  __TEXT.__objc_stubs: 0xab20
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__const: 0x1170
+  __TEXT.__unwind_info: 0x1800
+  __TEXT.__objc_classname: 0xdf1
+  __TEXT.__objc_methname: 0x11a96
+  __TEXT.__objc_methtype: 0x3406
+  __TEXT.__objc_stubs: 0xa9a0
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__const: 0x1148
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d10
+  __DATA_CONST.__objc_selrefs: 0x3cc0
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x6540
-  __AUTH_CONST.__objc_const: 0xe540
+  __AUTH_CONST.__objc_const: 0xe450
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1ae0
-  __DATA.__objc_ivar: 0x92c
+  __DATA.__objc_ivar: 0x918
   __DATA.__data: 0x790
   __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0ED6FDC7-010E-36FB-B07B-0A899FC59398
-  Functions: 3299
-  Symbols:   10231
-  CStrings:  5232
+  UUID: 34133D80-6C3C-309A-A435-8E276060BE64
+  Functions: 3289
+  Symbols:   10193
+  CStrings:  5208
 
Symbols:
+ -[NNMKSyncPersistenceHandler addMessageContent:forMessage:mailbox:]
+ -[NNMKSyncPersistenceHandler addMessageContent:forMessage:mailbox:].cold.1
+ -[NNMKSyncPersistenceHandler addMessagesToResend:mailbox:]
+ -[NNMKSyncPersistenceHandler addMoreConversationSpecificMessages:conversationId:mailbox:]
+ -[NNMKSyncPersistenceHandler addMoreMessages:mailbox:]
+ -[NNMKSyncProvider _addAttachmentData:forMessageId:contentId:mailbox:]
+ -[NNMKSyncProvider _addMessageContent:forMessage:mailbox:]
+ -[NNMKSyncProvider _addMessageContent:forMessage:mailbox:].cold.1
+ -[NNMKSyncProvider _initialSyncForMailbox:messages:]
+ -[NNMKSyncProvider _legacy_sendFirstMessages:syncedMailbox:]
+ -[NNMKSyncProvider _markConversationIdForNotify:messages:mailbox:]
+ -[NNMKSyncProvider _replyWithMoreMessages:forConversationWithId:mailbox:]
+ -[NNMKSyncProvider _replyWithMoreMessages:forDateReceivedBefore:mailbox:messagesForSpecialMailbox:]
+ -[NNMKSyncProvider _sendFirstMessages:mailboxes:]
+ ___38-[NNMKSyncProvider replyWithAccounts:]_block_invoke.21
+ ___72-[NNMKSyncProvider initWithDelegate:syncStateManager:directoryProvider:]_block_invoke.16
+ ___83-[NNMKSyncProvider markConversationIdForNotify:messages:includesProtectedMessages:]_block_invoke.39
+ ___97-[NNMKSyncProvider accountsSyncServiceServer:didReceivedAccountAuthenticationStatus:requestTime:]_block_invoke.68
+ ___97-[NNMKSyncProvider accountsSyncServiceServer:didReceivedAccountAuthenticationStatus:requestTime:]_block_invoke.68.cold.1
+ ___97-[NNMKSyncProvider accountsSyncServiceServer:didReceivedAccountAuthenticationStatus:requestTime:]_block_invoke.71
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_addAttachmentData:forMessageId:contentId:mailbox:
+ _objc_msgSend$_addMessageContent:forMessage:mailbox:
+ _objc_msgSend$_initialSyncForMailbox:messages:
+ _objc_msgSend$_legacy_sendFirstMessages:syncedMailbox:
+ _objc_msgSend$_markConversationIdForNotify:messages:mailbox:
+ _objc_msgSend$_replyWithMoreMessages:forConversationWithId:mailbox:
+ _objc_msgSend$_replyWithMoreMessages:forDateReceivedBefore:mailbox:messagesForSpecialMailbox:
+ _objc_msgSend$_sendFirstMessages:mailboxes:
+ _objc_msgSend$addMessageContent:forMessage:mailbox:
+ _objc_msgSend$addMessagesToResend:mailbox:
+ _objc_msgSend$addMoreConversationSpecificMessages:conversationId:mailbox:
+ _objc_msgSend$addMoreMessages:mailbox:
- -[NNMKDeletionResult protectedMessageIds]
- -[NNMKDeletionResult protectedProtobuf]
- -[NNMKDeletionResult setProtectedMessageIds:]
- -[NNMKDeletionResult setProtectedProtobuf:]
- -[NNMKSyncPersistenceHandler addMessageContent:forMessage:mailbox:isProtectedData:]
- -[NNMKSyncPersistenceHandler addMessageContent:forMessage:mailbox:isProtectedData:].cold.1
- -[NNMKSyncPersistenceHandler addMessagesToResend:mailbox:isProtectedData:]
- -[NNMKSyncPersistenceHandler addMoreConversationSpecificMessages:conversationId:mailbox:isProtectedData:]
- -[NNMKSyncPersistenceHandler addMoreMessages:mailbox:isProtectedData:]
- -[NNMKSyncProvider _addAttachmentData:forMessageId:contentId:loadedProtected:mailbox:]
- -[NNMKSyncProvider _addMessageContent:forMessage:loadedProtected:mailbox:]
- -[NNMKSyncProvider _addMessageContent:forMessage:loadedProtected:mailbox:].cold.1
- -[NNMKSyncProvider _initialSyncForMailbox:messages:shouldUseProtectedChannel:]
- -[NNMKSyncProvider _legacy_sendFirstMessages:syncedMailbox:shouldUseProtectedChannel:]
- -[NNMKSyncProvider _markConversationIdForNotify:messages:includesProtectedMessages:mailbox:]
- -[NNMKSyncProvider _replyWithMoreMessages:forConversationWithId:includesProtectedMessages:mailbox:]
- -[NNMKSyncProvider _replyWithMoreMessages:forDateReceivedBefore:includesProtectedMessages:mailbox:messagesForSpecialMailbox:]
- -[NNMKSyncProvider _sendFirstMessages:mailboxes:shouldUseProtectedChannel:]
- -[NNMKSyncedMessage setUsedProtectedChannelForMessageSync:]
- -[NNMKSyncedMessage usedProtectedChannelForMessageSync]
- -[NNMKUpdatesResult messageIdsWithDefaultPriorityAndProtectedChannel]
- -[NNMKUpdatesResult protoMessageUpdatesWithDefaultPriorityAndProtectedChannel]
- -[NNMKUpdatesResult setMessageIdsWithDefaultPriorityAndProtectedChannel:]
- -[NNMKUpdatesResult setProtoMessageUpdatesWithDefaultPriorityAndProtectedChannel:]
- _OBJC_IVAR_$_NNMKDeletionResult._protectedMessageIds
- _OBJC_IVAR_$_NNMKDeletionResult._protectedProtobuf
- _OBJC_IVAR_$_NNMKSyncedMessage._usedProtectedChannelForMessageSync
- _OBJC_IVAR_$_NNMKUpdatesResult._messageIdsWithDefaultPriorityAndProtectedChannel
- _OBJC_IVAR_$_NNMKUpdatesResult._protoMessageUpdatesWithDefaultPriorityAndProtectedChannel
- ___38-[NNMKSyncProvider replyWithAccounts:]_block_invoke.23
- ___72-[NNMKSyncProvider initWithDelegate:syncStateManager:directoryProvider:]_block_invoke.18
- ___83-[NNMKSyncProvider markConversationIdForNotify:messages:includesProtectedMessages:]_block_invoke.41
- ___97-[NNMKSyncProvider accountsSyncServiceServer:didReceivedAccountAuthenticationStatus:requestTime:]_block_invoke.70
- ___97-[NNMKSyncProvider accountsSyncServiceServer:didReceivedAccountAuthenticationStatus:requestTime:]_block_invoke.70.cold.1
- ___97-[NNMKSyncProvider accountsSyncServiceServer:didReceivedAccountAuthenticationStatus:requestTime:]_block_invoke.73
- ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$_addAttachmentData:forMessageId:contentId:loadedProtected:mailbox:
- _objc_msgSend$_addMessageContent:forMessage:loadedProtected:mailbox:
- _objc_msgSend$_initialSyncForMailbox:messages:shouldUseProtectedChannel:
- _objc_msgSend$_legacy_sendFirstMessages:syncedMailbox:shouldUseProtectedChannel:
- _objc_msgSend$_markConversationIdForNotify:messages:includesProtectedMessages:mailbox:
- _objc_msgSend$_replyWithMoreMessages:forConversationWithId:includesProtectedMessages:mailbox:
- _objc_msgSend$_replyWithMoreMessages:forDateReceivedBefore:includesProtectedMessages:mailbox:messagesForSpecialMailbox:
- _objc_msgSend$_sendFirstMessages:mailboxes:shouldUseProtectedChannel:
- _objc_msgSend$addMessageContent:forMessage:mailbox:isProtectedData:
- _objc_msgSend$addMessagesToResend:mailbox:isProtectedData:
- _objc_msgSend$addMoreConversationSpecificMessages:conversationId:mailbox:isProtectedData:
- _objc_msgSend$addMoreMessages:mailbox:isProtectedData:
- _objc_msgSend$hasProtectedMessages
- _objc_msgSend$messageIdsWithDefaultPriorityAndProtectedChannel
- _objc_msgSend$protectedContentChannelSupported
- _objc_msgSend$protectedMessageIds
- _objc_msgSend$protectedProtobuf
- _objc_msgSend$protoMessageUpdatesWithDefaultPriorityAndProtectedChannel
- _objc_msgSend$setMessageIdsWithDefaultPriorityAndProtectedChannel:
- _objc_msgSend$setProtectedMessageIds:
- _objc_msgSend$setProtectedProtobuf:
- _objc_msgSend$setProtoMessageUpdatesWithDefaultPriorityAndProtectedChannel:
- _objc_msgSend$setUsedProtectedChannelForMessageSync:
- _objc_msgSend$usedProtectedChannelForMessageSync
CStrings:
+ "_addAttachmentData:forMessageId:contentId:mailbox:"
+ "_addMessageContent:forMessage:mailbox:"
+ "_initialSyncForMailbox:messages:"
+ "_legacy_sendFirstMessages:syncedMailbox:"
+ "_markConversationIdForNotify:messages:mailbox:"
+ "_replyWithMoreMessages:forConversationWithId:mailbox:"
+ "_replyWithMoreMessages:forDateReceivedBefore:mailbox:messagesForSpecialMailbox:"
+ "_sendFirstMessages:mailboxes:"
+ "addMessageContent:forMessage:mailbox:"
+ "addMessagesToResend:mailbox:"
+ "addMoreConversationSpecificMessages:conversationId:mailbox:"
+ "addMoreMessages:mailbox:"
- "@36@0:8@16@24B32"
- "@44@0:8@16@24@32B40"
- "T@\"NNMKProtoMessageDeletions\",&,N,V_protectedProtobuf"
- "T@\"NNMKProtoMessageStatusUpdates\",&,N,V_protoMessageUpdatesWithDefaultPriorityAndProtectedChannel"
- "T@\"NSArray\",&,N,V_messageIdsWithDefaultPriorityAndProtectedChannel"
- "T@\"NSArray\",&,N,V_protectedMessageIds"
- "TB,N,V_usedProtectedChannelForMessageSync"
- "_addAttachmentData:forMessageId:contentId:loadedProtected:mailbox:"
- "_addMessageContent:forMessage:loadedProtected:mailbox:"
- "_initialSyncForMailbox:messages:shouldUseProtectedChannel:"
- "_legacy_sendFirstMessages:syncedMailbox:shouldUseProtectedChannel:"
- "_markConversationIdForNotify:messages:includesProtectedMessages:mailbox:"
- "_messageIdsWithDefaultPriorityAndProtectedChannel"
- "_protectedMessageIds"
- "_protectedProtobuf"
- "_protoMessageUpdatesWithDefaultPriorityAndProtectedChannel"
- "_replyWithMoreMessages:forConversationWithId:includesProtectedMessages:mailbox:"
- "_replyWithMoreMessages:forDateReceivedBefore:includesProtectedMessages:mailbox:messagesForSpecialMailbox:"
- "_sendFirstMessages:mailboxes:shouldUseProtectedChannel:"
- "_usedProtectedChannelForMessageSync"
- "addMessageContent:forMessage:mailbox:isProtectedData:"
- "addMessagesToResend:mailbox:isProtectedData:"
- "addMoreConversationSpecificMessages:conversationId:mailbox:isProtectedData:"
- "addMoreMessages:mailbox:isProtectedData:"
- "messageIdsWithDefaultPriorityAndProtectedChannel"
- "protectedMessageIds"
- "protectedProtobuf"
- "protoMessageUpdatesWithDefaultPriorityAndProtectedChannel"
- "setMessageIdsWithDefaultPriorityAndProtectedChannel:"
- "setProtectedMessageIds:"
- "setProtectedProtobuf:"
- "setProtoMessageUpdatesWithDefaultPriorityAndProtectedChannel:"
- "setUsedProtectedChannelForMessageSync:"
- "usedProtectedChannelForMessageSync"
- "v44@0:8@16@24B32@36"
- "v52@0:8@16@24B32@36Q44"

```

## BiomeStreams

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x4b4074
-  __TEXT.__auth_stubs: 0x21b0
-  __TEXT.__objc_methlist: 0x14f9c
-  __TEXT.__const: 0xaa384
-  __TEXT.__cstring: 0x36676
-  __TEXT.__oslogstring: 0xc430
-  __TEXT.__gcc_except_tab: 0x14ac
-  __TEXT.__dlopen_cstrs: 0x6d6
+166.17.1.0.0
+  __TEXT.__text: 0x491688
+  __TEXT.__auth_stubs: 0x2140
+  __TEXT.__objc_methlist: 0x1584c
+  __TEXT.__const: 0xaa324
+  __TEXT.__cstring: 0x353d8
+  __TEXT.__gcc_except_tab: 0x1524
+  __TEXT.__oslogstring: 0xc310
+  __TEXT.__dlopen_cstrs: 0x680
   __TEXT.__constg_swiftt: 0xb0b4
-  __TEXT.__swift5_typeref: 0x5342
+  __TEXT.__swift5_typeref: 0x531c
   __TEXT.__swift5_reflstr: 0x6a51
   __TEXT.__swift5_fieldmd: 0xb70c
   __TEXT.__swift5_capture: 0x174

   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_assocty: 0xb98
-  __TEXT.__unwind_info: 0xd410
-  __TEXT.__eh_frame: 0xdd70
-  __TEXT.__objc_classname: 0x2808
-  __TEXT.__objc_methname: 0x1dae6
-  __TEXT.__objc_methtype: 0x3d26
-  __TEXT.__objc_stubs: 0x11ce0
-  __DATA_CONST.__got: 0x1140
-  __DATA_CONST.__const: 0x29da0
-  __DATA_CONST.__objc_classlist: 0xef8
+  __TEXT.__unwind_info: 0xcdc0
+  __TEXT.__eh_frame: 0xdb78
+  __TEXT.__objc_classname: 0x281a
+  __TEXT.__objc_methname: 0x1da32
+  __TEXT.__objc_methtype: 0x3e26
+  __TEXT.__objc_stubs: 0x11ea0
+  __DATA_CONST.__got: 0x1120
+  __DATA_CONST.__const: 0x29e78
+  __DATA_CONST.__objc_classlist: 0xef0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x1d0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61b0
+  __DATA_CONST.__objc_selrefs: 0x6298
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x9e8
+  __DATA_CONST.__objc_superrefs: 0x9e0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x10e8
-  __AUTH_CONST.__const: 0x12cf0
-  __AUTH_CONST.__cfstring: 0x9400
-  __AUTH_CONST.__objc_const: 0x4fe80
+  __AUTH_CONST.__auth_got: 0x10b0
+  __AUTH_CONST.__const: 0x12c20
+  __AUTH_CONST.__cfstring: 0x9460
+  __AUTH_CONST.__objc_const: 0x4ed10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x9660
-  __AUTH.__data: 0x134d0
-  __AUTH.__thread_vars: 0x420
-  __AUTH.__thread_data: 0x112
-  __AUTH.__thread_bss: 0x7a8
-  __DATA.__objc_ivar: 0x18f8
-  __DATA.__data: 0x9bd8
-  __DATA.__bss: 0x3d378
-  __DATA.__common: 0x1de8
+  __AUTH.__objc_data: 0x9610
+  __AUTH.__data: 0x134c8
+  __AUTH.__thread_vars: 0x348
+  __AUTH.__thread_data: 0xf4
+  __AUTH.__thread_bss: 0x458
+  __DATA.__objc_ivar: 0x18ec
+  __DATA.__data: 0x9d08
+  __DATA.__bss: 0x3d258
+  __DATA.__common: 0x1c10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D3A3DA40-194D-38A2-BA53-F016595FEBA9
-  Functions: 23167
-  Symbols:   53487
-  CStrings:  16913
+  UUID: E211DE71-97F8-3395-8322-36586CE626B0
+  Functions: 22809
+  Symbols:   53207
+  CStrings:  16811
 
Symbols:
+ +[BMComputePublisherClient _setQueue:domain:]
+ +[BMComputePublisherClient initializeSharedClientWithQueue:domain:]
+ +[BMComputePublisherClient new]
+ +[BMComputePublisherClient sharedWithQueue:domain:]
+ +[BMComputePublisherClient shared]
+ +[BMComputePublisherServer new]
+ +[BMComputePublisherStorage currentSession]
+ +[BMComputePublisherStorage(BMBiomeSchedulerAdditions) bookmarkStorageForCurrentProcess]
+ +[BMComputeSubscription new]
+ +[BMComputeSubscription storageForIdentifier:]
+ +[BMComputeSubscription storageForIdentifier:].cold.1
+ +[BMComputeSubscription storageForIdentifier:].cold.2
+ +[BMComputeSubscription supportsSecureCoding]
+ +[BMLibraryStreamsPruner _enumerateAllPruningTriggersForPolicy:block:]
+ +[BMLibraryStreamsPruner _pruneStream:policy:trigger:parameters:]
+ +[BMLibraryStreamsPruner _pruneStream:policy:trigger:parameters:].cold.1
+ +[BMLibraryStreamsPruner _pruneStreamsWithPolicy:parameters:]
+ +[BMLibraryStreamsPruner _pruneStreamsWithPolicy:parameters:].cold.1
+ +[BMLibraryStreamsPruner domain]
+ +[BMLibraryStreamsPruner domain].cold.1
+ +[BMPairedEventSession sessionPublisherWithStreamPublisher:startingBlock:sessionKeyBlock:options:].cold.1
+ +[BMStoreSource _processPendingWritesQueue].cold.1
+ -[BMBiomeTableStore initWithURL:tableName:identifier:].cold.1
+ -[BMBiomeTableStore initWithURL:tableName:identifier:].cold.2
+ -[BMComputePublisherClient .cxx_destruct]
+ -[BMComputePublisherClient _handleEventWithPayload:]
+ -[BMComputePublisherClient _handleEventWithPayload:].cold.1
+ -[BMComputePublisherClient _setXPCEvent:identifier:]
+ -[BMComputePublisherClient _setXPCEvent:identifier:].cold.1
+ -[BMComputePublisherClient computePublisherObjectWithErrorHandler:]
+ -[BMComputePublisherClient connection]
+ -[BMComputePublisherClient dealloc]
+ -[BMComputePublisherClient handleBiomeRelaunch]
+ -[BMComputePublisherClient initWithQueue:configuration:listenerEndpoint:localComputePublisher:]
+ -[BMComputePublisherClient initWithQueue:domain:listenerEndpoint:localComputePublisher:]
+ -[BMComputePublisherClient init]
+ -[BMComputePublisherClient isRegisteredForRelaunchNotification]
+ -[BMComputePublisherClient numberOfExistingNonWakingSubscriptions]
+ -[BMComputePublisherClient pendingEvents]
+ -[BMComputePublisherClient queue]
+ -[BMComputePublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:]
+ -[BMComputePublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:].cold.1
+ -[BMComputePublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:].cold.2
+ -[BMComputePublisherClient registerBiomeLaunchNotification]
+ -[BMComputePublisherClient registerBiomeLaunchNotification].cold.1
+ -[BMComputePublisherClient subscribe:]
+ -[BMComputePublisherClient subscribeViaNSXPC:]
+ -[BMComputePublisherClient subscribeViaNSXPC:].cold.1
+ -[BMComputePublisherClient subscribeViaXPCEvent:]
+ -[BMComputePublisherClient subscribeViaXPCEvent:].cold.1
+ -[BMComputePublisherClient subscriptions]
+ -[BMComputePublisherClient unregisterBiomeLaunchNotification]
+ -[BMComputePublisherClient unregisterBiomeLaunchNotification].cold.1
+ -[BMComputePublisherClient unregisterBiomeLaunchNotification].cold.2
+ -[BMComputePublisherClient unsubscribeWithIdentifier:]
+ -[BMComputePublisherClient unsubscribeWithIdentifier:].cold.1
+ -[BMComputePublisherClientDomainConfiguration .cxx_destruct]
+ -[BMComputePublisherClientDomainConfiguration XPCPublisherStreamName]
+ -[BMComputePublisherClientDomainConfiguration biomeLaunchNotification]
+ -[BMComputePublisherClientDomainConfiguration domain]
+ -[BMComputePublisherClientDomainConfiguration initWithDomain:]
+ -[BMComputePublisherClientDomainConfiguration initWithDomain:].cold.1
+ -[BMComputePublisherClientDomainConfiguration machServiceName]
+ -[BMComputePublisherServer .cxx_destruct]
+ -[BMComputePublisherServer _addSubscription:]
+ -[BMComputePublisherServer _addSubscription:].cold.1
+ -[BMComputePublisherServer _handlePublisherAction:token:descriptor:]
+ -[BMComputePublisherServer _handlePublisherAction:token:descriptor:].cold.1
+ -[BMComputePublisherServer _handlePublisherAction:token:descriptor:].cold.2
+ -[BMComputePublisherServer _removeActiveSubscriptionMarkersForSubscription:]
+ -[BMComputePublisherServer _removeActiveSubscriptionMarkersForSubscription:].cold.1
+ -[BMComputePublisherServer _removeSubscriptionWithIdentifier:client:]
+ -[BMComputePublisherServer _removeSubscriptionWithIdentifier:client:].cold.1
+ -[BMComputePublisherServer _removeSubscriptionWithToken:]
+ -[BMComputePublisherServer activateWithCompletion:]
+ -[BMComputePublisherServer activateWithCompletion:].cold.1
+ -[BMComputePublisherServer activationCompletion]
+ -[BMComputePublisherServer delegate]
+ -[BMComputePublisherServer description]
+ -[BMComputePublisherServer domain]
+ -[BMComputePublisherServer initWithQueue:domain:delegate:]
+ -[BMComputePublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]
+ -[BMComputePublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:].cold.1
+ -[BMComputePublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:].cold.2
+ -[BMComputePublisherServer init]
+ -[BMComputePublisherServer interface]
+ -[BMComputePublisherServer listener:shouldAcceptNewConnection:]
+ -[BMComputePublisherServer listener:shouldAcceptNewConnection:].cold.1
+ -[BMComputePublisherServer listener:shouldAcceptNewConnection:].cold.2
+ -[BMComputePublisherServer listener]
+ -[BMComputePublisherServer publisher]
+ -[BMComputePublisherServer queue]
+ -[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]
+ -[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:].cold.1
+ -[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:].cold.2
+ -[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:].cold.3
+ -[BMComputePublisherServer setActivationCompletion:]
+ -[BMComputePublisherServer storage]
+ -[BMComputePublisherServer subscribe:]
+ -[BMComputePublisherServer subscribe:].cold.1
+ -[BMComputePublisherServer subscribe:].cold.2
+ -[BMComputePublisherServer subscribe:].cold.3
+ -[BMComputePublisherServer subscribe:].cold.4
+ -[BMComputePublisherServer subscribe:].cold.5
+ -[BMComputePublisherServer subscribe:].cold.6
+ -[BMComputePublisherServer subscriptionMarkerManager]
+ -[BMComputePublisherServer subscriptionsForStream:]
+ -[BMComputePublisherServer subscriptionsForStream:].cold.1
+ -[BMComputePublisherServer subscriptions]
+ -[BMComputePublisherServer systemStorage]
+ -[BMComputePublisherServer unsubscribeWithIdentifier:]
+ -[BMComputePublisherServer unsubscribeWithIdentifier:].cold.1
+ -[BMComputePublisherServer unsubscribeWithIdentifier:].cold.2
+ -[BMComputePublisherServer userStorage]
+ -[BMComputePublisherStorage .cxx_destruct]
+ -[BMComputePublisherStorage basePath]
+ -[BMComputePublisherStorage bookmarkPathForSessionStorageWithIdentifier:client:]
+ -[BMComputePublisherStorage checkActiveSubscriptionMarkerForStream:]
+ -[BMComputePublisherStorage checkActiveSubscriptionMarkerForStream:].cold.1
+ -[BMComputePublisherStorage checkExistenceOfBookmarkForSubscriptionWithIdentifier:client:]
+ -[BMComputePublisherStorage currentSessionBookmarkClientOrServerPath]
+ -[BMComputePublisherStorage currentSessionBookmarkPath]
+ -[BMComputePublisherStorage currentSessionNonwakingSubscriptionPath]
+ -[BMComputePublisherStorage currentSessionPath]
+ -[BMComputePublisherStorage currentSessionSubscriptionsPath]
+ -[BMComputePublisherStorage domain]
+ -[BMComputePublisherStorage initWithUseCase:domain:isClient:]
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession]
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.1
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.2
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.3
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.4
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.5
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.6
+ -[BMComputePublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.7
+ -[BMComputePublisherStorage isClient]
+ -[BMComputePublisherStorage newFileManagerWithUseCase:]
+ -[BMComputePublisherStorage persistentPath]
+ -[BMComputePublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:]
+ -[BMComputePublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.1
+ -[BMComputePublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.2
+ -[BMComputePublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.3
+ -[BMComputePublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.4
+ -[BMComputePublisherStorage readNonWakingSubscriptions:]
+ -[BMComputePublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:]
+ -[BMComputePublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:].cold.1
+ -[BMComputePublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:].cold.2
+ -[BMComputePublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:].cold.3
+ -[BMComputePublisherStorage removeActiveSubscriptionMarkerForStream:]
+ -[BMComputePublisherStorage removeActiveSubscriptionMarkerForStream:].cold.1
+ -[BMComputePublisherStorage removeBookmarkFileForSubscriptionWithIdentifier:client:]
+ -[BMComputePublisherStorage removeBookmarkFileForSubscriptionWithIdentifier:client:].cold.1
+ -[BMComputePublisherStorage removeNonWakingSubscriptionWithIdentifier:client:]
+ -[BMComputePublisherStorage removeNonWakingSubscriptionWithIdentifier:client:].cold.1
+ -[BMComputePublisherStorage removeNonWakingSubscriptionWithIdentifier:client:].cold.2
+ -[BMComputePublisherStorage sessionsPath]
+ -[BMComputePublisherStorage subscriptionMarkerPathForSessionStorageWithStream:]
+ -[BMComputePublisherStorage writeActiveSubscriptionMarkerForStream:]
+ -[BMComputePublisherStorage writeActiveSubscriptionMarkerForStream:].cold.1
+ -[BMComputePublisherStorage writeBookmark:forSubscriptionWithIdentifier:client:]
+ -[BMComputePublisherStorage writeBookmark:forSubscriptionWithIdentifier:client:].cold.1
+ -[BMComputePublisherStorage writeNonWakingSubscription:]
+ -[BMComputePublisherStorage writeNonWakingSubscription:].cold.1
+ -[BMComputePublisherStorage writeNonWakingSubscription:].cold.2
+ -[BMComputePublisherStorage writeNonWakingSubscription:].cold.3
+ -[BMComputeSourceClient _newConnectionForDomain:]
+ -[BMComputeSourceClient _remoteObjectProxyForDomain:errorHandler:]
+ -[BMComputeSourceClient initWithStreamIdentifier:domain:listenerEndpoint:storage:user:]
+ -[BMComputeSourceClient initWithStreamIdentifier:domain:useCase:user:]
+ -[BMComputeSourceServer _acceptConnection:]
+ -[BMComputeSourceServer _acceptConnection:].cold.1
+ -[BMComputeSourceServer connection:handleInvocation:isReply:]
+ -[BMComputeSourceServer connection:handleInvocation:isReply:].cold.1
+ -[BMComputeSourceServer domain]
+ -[BMComputeSourceServer eventsPrunedWithStreamIdentifier:account:remoteName:reason:]
+ -[BMComputeSourceServer eventsPrunedWithStreamIdentifier:account:remoteName:reason:].cold.1
+ -[BMComputeSourceServer eventsPrunedWithStreamIdentifier:account:remoteName:reason:].cold.2
+ -[BMComputeSourceServer eventsPrunedWithStreamIdentifier:account:remoteName:reason:].cold.3
+ -[BMComputeSourceServer initWithQueue:domain:source:]
+ -[BMComputeSourceServer initWithQueue:domain:source:listener:]
+ -[BMComputeSourceServer replyToInvocation:withError:]
+ -[BMComputeSourceServer replyToInvocation:withError:].cold.1
+ -[BMComputeSourceServer replyToInvocation:withError:].cold.2
+ -[BMComputeSourceServer replyToInvocation:withError:].cold.3
+ -[BMComputeSourceServer replyToInvocation:withError:].cold.4
+ -[BMComputeSourceServer requestEndpointForProxyingConnectionsWithReply:]
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:]
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.1
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.2
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.3
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.4
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.5
+ -[BMComputeSourceServer validateConnection:error:]
+ -[BMComputeSubscription .cxx_destruct]
+ -[BMComputeSubscription XPCEvent]
+ -[BMComputeSubscription XPCEvent].cold.1
+ -[BMComputeSubscription XPCEvent].cold.2
+ -[BMComputeSubscription block]
+ -[BMComputeSubscription client]
+ -[BMComputeSubscription connection]
+ -[BMComputeSubscription createdAt]
+ -[BMComputeSubscription description]
+ -[BMComputeSubscription encodeWithCoder:]
+ -[BMComputeSubscription fetchBookmarkFromStorage:error:]
+ -[BMComputeSubscription graph]
+ -[BMComputeSubscription identifier]
+ -[BMComputeSubscription initWithCoder:]
+ -[BMComputeSubscription initWithIdentifier:client:createdAt:waking:DSLGraph:subscriber:block:]
+ -[BMComputeSubscription initWithIdentifier:client:createdAt:waking:DSLGraph:subscriber:block:].cold.1
+ -[BMComputeSubscription initWithIdentifier:client:createdAt:waking:DSLGraph:subscriber:block:].cold.2
+ -[BMComputeSubscription initWithIdentifier:client:waking:DSLGraph:block:]
+ -[BMComputeSubscription initWithToken:descriptor:]
+ -[BMComputeSubscription initWithToken:descriptor:].cold.1
+ -[BMComputeSubscription initWithToken:descriptor:].cold.2
+ -[BMComputeSubscription initWithToken:descriptor:].cold.3
+ -[BMComputeSubscription initWithToken:descriptor:].cold.4
+ -[BMComputeSubscription initWithToken:descriptor:].cold.5
+ -[BMComputeSubscription initWithToken:descriptor:].cold.6
+ -[BMComputeSubscription initWithToken:descriptor:].cold.7
+ -[BMComputeSubscription init]
+ -[BMComputeSubscription initialBookmarkTimestamp]
+ -[BMComputeSubscription isUnclaimed]
+ -[BMComputeSubscription pendingDemand]
+ -[BMComputeSubscription postMigrationStreamIdentifiers]
+ -[BMComputeSubscription setClient:]
+ -[BMComputeSubscription setConnection:]
+ -[BMComputeSubscription setInitialBookmarkTimestamp:]
+ -[BMComputeSubscription setPendingDemand:]
+ -[BMComputeSubscription startEvent]
+ -[BMComputeSubscription streamIdentifiers]
+ -[BMComputeSubscription subscriber]
+ -[BMComputeSubscription token]
+ -[BMComputeSubscription uniqueIdentifier]
+ -[BMComputeSubscription useCase]
+ -[BMComputeSubscription waking]
+ -[BMComputeSubscriptionSubstreamManager _checkinTimeout].cold.1
+ -[BMComputeSubscriptionSubstreamManager initialCheckinsComplete].cold.1
+ -[BMComputeTombstonePropagator initWithStreamIdentifier:domain:user:]
+ -[BMContentAttachment initWithType:filename:path:].cold.1
+ -[BMContentAttachment initWithType:filename:path:].cold.2
+ -[BMContentStream initWithStreamIdentifier:eventClass:].cold.2
+ -[BMContentStream initWithStreamIdentifier:eventClass:].cold.3
+ -[BMDKEvent initWithDKEvent:].cold.1
+ -[BMDKEventStream initWithStreamIdentifier:contentProtection:pruningPolicy:domain:].cold.1
+ -[BMDaemon sendEventWithStreamIdentifier:timestamp:account:remoteName:storeEvent:].cold.2
+ -[BMIndexRowEnumerator next].cold.1
+ -[BMIndexSearch initWithIndex:startFields:endFields:database:].cold.1
+ -[BMIntentEvent initWithAbsoluteTime:bundleId:sourceId:intentClass:intentVerb:intentType:intentHandlingStatus:interaction:itemID:donatedBySiri:interactionDirection:groupIdentifier:].cold.1
+ -[BMMailContentEvent _inflateFromProto:].cold.1
+ -[BMMailContentEvent _loadData].cold.1
+ -[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:].cold.1
+ -[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:].cold.2
+ -[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:].cold.3
+ -[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:].cold.4
+ -[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:].cold.5
+ -[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:].cold.6
+ -[BMMessagesContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:conversationId:fromHandle:toHandles:suggestedNickname:suggestedPhotoPath:content:accountIdentifier:accountHandles:accountType:attachment:URL:contentProtection:isNew:isTwoFactorCode:isFromMe:isGroupThread:isJunk:isRead:isPinned:isBusinessChat:tapbackAssociatedMessageID:tapbackType:messageType:messagesService:messageEffect:isKnownSender:conversationUUID:].cold.1
+ -[BMMessagesContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:conversationId:fromHandle:toHandles:suggestedNickname:suggestedPhotoPath:content:accountIdentifier:accountHandles:accountType:attachment:URL:contentProtection:isNew:isTwoFactorCode:isFromMe:isGroupThread:isJunk:isRead:isPinned:isBusinessChat:tapbackAssociatedMessageID:tapbackType:messageType:messagesService:messageEffect:isKnownSender:conversationUUID:].cold.2
+ -[BMMessagesContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:conversationId:fromHandle:toHandles:suggestedNickname:suggestedPhotoPath:content:accountIdentifier:accountHandles:accountType:attachment:URL:contentProtection:isNew:isTwoFactorCode:isFromMe:isGroupThread:isJunk:isRead:isPinned:isBusinessChat:tapbackAssociatedMessageID:tapbackType:messageType:messagesService:messageEffect:isKnownSender:conversationUUID:].cold.3
+ -[BMMessagesContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:conversationId:fromHandle:toHandles:suggestedNickname:suggestedPhotoPath:content:accountIdentifier:accountHandles:accountType:attachment:URL:contentProtection:isNew:isTwoFactorCode:isFromMe:isGroupThread:isJunk:isRead:isPinned:isBusinessChat:tapbackAssociatedMessageID:tapbackType:messageType:messagesService:messageEffect:isKnownSender:conversationUUID:].cold.4
+ -[BMNamedHandle initWithName:handleType:handle:contactIdentifier:].cold.1
+ -[BMNewsArticleViewEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:summary:publication:contentProtection:].cold.1
+ -[BMNewsArticleViewEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:summary:publication:contentProtection:].cold.2
+ -[BMNewsArticleViewEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:summary:publication:contentProtection:].cold.3
+ -[BMNotesContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:contentProtection:].cold.1
+ -[BMNotesContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:contentProtection:].cold.2
+ -[BMParsecSearchEngagementEvent initWithUniqueId:resultId:domainId:personaId:absoluteTimestamp:userInput:completedQuery:entities:contentProtection:].cold.1
+ -[BMParsecSearchEngagementEvent initWithUniqueId:resultId:domainId:personaId:absoluteTimestamp:userInput:completedQuery:entities:contentProtection:].cold.2
+ -[BMParsecSearchEngagementEvent initWithUniqueId:resultId:domainId:personaId:absoluteTimestamp:userInput:completedQuery:entities:contentProtection:].cold.3
+ -[BMParsecSearchEngagementEvent initWithUniqueId:resultId:domainId:personaId:absoluteTimestamp:userInput:completedQuery:entities:contentProtection:].cold.4
+ -[BMParsecSearchEngagementEvent initWithUniqueId:resultId:domainId:personaId:absoluteTimestamp:userInput:completedQuery:entities:contentProtection:].cold.5
+ -[BMParsecSearchEntity initWithName:category:probabilityScore:topics:].cold.1
+ -[BMParsecSearchEntity initWithName:category:probabilityScore:topics:].cold.2
+ -[BMParsecSearchTopic initWithIdentifier:score:].cold.1
+ -[BMPhotosKnowledgeGraphEnrichmentEntity initWithName:score:language:category:].cold.1
+ -[BMPhotosKnowledgeGraphEnrichmentEntity initWithName:score:language:category:].cold.2
+ -[BMPhotosKnowledgeGraphEnrichmentEvent initWithUniqueId:personaId:absoluteTimestamp:topics:entities:locations:contentProtection:].cold.1
+ -[BMPhotosKnowledgeGraphEnrichmentEvent initWithUniqueId:personaId:absoluteTimestamp:topics:entities:locations:contentProtection:].cold.2
+ -[BMPhotosKnowledgeGraphEnrichmentEvent initWithUniqueId:personaId:absoluteTimestamp:topics:entities:locations:contentProtection:].cold.3
+ -[BMPhotosKnowledgeGraphEnrichmentEvent initWithUniqueId:personaId:absoluteTimestamp:topics:entities:locations:contentProtection:].cold.4
+ -[BMPhotosKnowledgeGraphEnrichmentLocation initWithStreet:city:state:country:encodedLocation:].cold.1
+ -[BMPhotosKnowledgeGraphEnrichmentLocation initWithStreet:city:state:country:encodedLocation:].cold.2
+ -[BMPhotosKnowledgeGraphEnrichmentLocation initWithStreet:city:state:country:encodedLocation:].cold.3
+ -[BMPhotosKnowledgeGraphEnrichmentLocation initWithStreet:city:state:country:encodedLocation:].cold.4
+ -[BMPhotosKnowledgeGraphEnrichmentLocation initWithStreet:city:state:country:encodedLocation:].cold.5
+ -[BMPhotosKnowledgeGraphEnrichmentTopic initWithIdentifier:score:].cold.1
+ -[BMPhotosPhotoViewEvent initWithUniqueId:personaId:locations:absoluteTimestamp:contentProtection:].cold.1
+ -[BMPhotosPhotoViewEvent initWithUniqueId:personaId:locations:absoluteTimestamp:contentProtection:].cold.2
+ -[BMRemindersContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:notes:isAllDay:completionDateTimestamp:dueDateTimestamp:priority:contentProtection:].cold.1
+ -[BMRestrictedStream initWithIdentifier:eventDataClass:].cold.2
+ -[BMRestrictedStream initWithIdentifier:segmentSize:pruningPolicy:eventDataClass:].cold.2
+ -[BMRestrictedStream initWithIdentifier:segmentSize:pruningPolicy:eventDataClass:].cold.3
+ -[BMSafariPageViewEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:contentIsReaderText:url:contentProtection:].cold.1
+ -[BMSafariPageViewEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:contentIsReaderText:url:contentProtection:].cold.2
+ -[BMSafariPageViewEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:title:content:contentIsReaderText:url:contentProtection:].cold.3
+ -[BMSiriPrivateLearningSELFEvent initWithUniqueId:absoluteTimestamp:eventData:].cold.1
+ -[BMSiriPrivateLearningSELFEvent initWithUniqueId:absoluteTimestamp:eventData:].cold.2
+ -[BMSiriQueryEvent initWithUniqueId:personaId:absoluteTimestamp:query:results:contentProtection:].cold.1
+ -[BMSiriQueryEvent initWithUniqueId:personaId:absoluteTimestamp:query:results:contentProtection:].cold.2
+ -[BMSiriQueryEvent initWithUniqueId:personaId:absoluteTimestamp:query:results:contentProtection:].cold.3
+ -[BMSiriQueryResult initWithQID:domain:confidence:].cold.1
+ -[BMStoreSource sendEvent:timestamp:].cold.3
+ -[BMStoreStream _prunerForRemote:].cold.1
+ -[BMStoreStream publisherForDevice:withUseCase:].cold.1
+ -[BMStoreStream publisherForDevice:withUseCase:options:].cold.1
+ -[BMStoreStream publishersForDevices:withUseCase:startTime:endTime:maxEvents:lastN:reversed:includeLocal:pipeline:].cold.1
+ -[BMStoreStream publishersForDevices:withUseCase:startTime:includeLocal:pipeline:].cold.1
+ -[BMStoreStreamPruningBridge initWithStreamIdentifier:domain:user:]
+ -[BMStreamBase(PeriodicMaintenance) _pruneDisabledSubstreams].cold.2
+ -[BMStreamBuiltinPruningTrigger initWithIdentifier:triggerCondition:pruningPredicate:]
+ -[BMStreamVirtualTable useCase]
+ -[BMThirdPartyAppContentEvent initWithUniqueId:domainId:bundleId:personaId:absoluteTimestamp:title:desc:comment:content:contentProtection:].cold.1
+ -[BMThirdPartyAppContentEvent initWithUniqueId:domainId:bundleId:personaId:absoluteTimestamp:title:desc:comment:content:contentProtection:].cold.2
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table54
+ GCC_except_table55
+ OBJC_IVAR_$_BMComputePublisherClient._configuration
+ OBJC_IVAR_$_BMComputePublisherClient._connection
+ OBJC_IVAR_$_BMComputePublisherClient._listenerEndpoint
+ OBJC_IVAR_$_BMComputePublisherClient._localComputePublisher
+ OBJC_IVAR_$_BMComputePublisherClient._lock
+ OBJC_IVAR_$_BMComputePublisherClient._pendingEvents
+ OBJC_IVAR_$_BMComputePublisherClient._queue
+ OBJC_IVAR_$_BMComputePublisherClient._subscriptions
+ OBJC_IVAR_$_BMComputePublisherClient._token
+ OBJC_IVAR_$_BMComputePublisherClientDomainConfiguration._XPCPublisherStreamName
+ OBJC_IVAR_$_BMComputePublisherClientDomainConfiguration._biomeLaunchNotification
+ OBJC_IVAR_$_BMComputePublisherClientDomainConfiguration._domain
+ OBJC_IVAR_$_BMComputePublisherClientDomainConfiguration._machServiceName
+ OBJC_IVAR_$_BMComputePublisherServer._activationCompletion
+ OBJC_IVAR_$_BMComputePublisherServer._delegate
+ OBJC_IVAR_$_BMComputePublisherServer._domain
+ OBJC_IVAR_$_BMComputePublisherServer._interface
+ OBJC_IVAR_$_BMComputePublisherServer._listener
+ OBJC_IVAR_$_BMComputePublisherServer._publisher
+ OBJC_IVAR_$_BMComputePublisherServer._queue
+ OBJC_IVAR_$_BMComputePublisherServer._subscriptionMarkerManager
+ OBJC_IVAR_$_BMComputePublisherServer._subscriptions
+ OBJC_IVAR_$_BMComputePublisherServer._systemStorage
+ OBJC_IVAR_$_BMComputePublisherServer._userStorage
+ OBJC_IVAR_$_BMComputePublisherStorage._domain
+ OBJC_IVAR_$_BMComputePublisherStorage._fileManager
+ OBJC_IVAR_$_BMComputePublisherStorage._isClient
+ OBJC_IVAR_$_BMComputeSourceClient._connectionWrapper
+ OBJC_IVAR_$_BMComputeSourceClient._domain
+ OBJC_IVAR_$_BMComputeSourceClient._user
+ OBJC_IVAR_$_BMComputeSourceServer._domain
+ OBJC_IVAR_$_BMComputeSubscription._block
+ OBJC_IVAR_$_BMComputeSubscription._client
+ OBJC_IVAR_$_BMComputeSubscription._connection
+ OBJC_IVAR_$_BMComputeSubscription._createdAt
+ OBJC_IVAR_$_BMComputeSubscription._graph
+ OBJC_IVAR_$_BMComputeSubscription._identifier
+ OBJC_IVAR_$_BMComputeSubscription._initialBookmarkTimestamp
+ OBJC_IVAR_$_BMComputeSubscription._pendingDemand
+ OBJC_IVAR_$_BMComputeSubscription._postMigrationStreamIdentifiers
+ OBJC_IVAR_$_BMComputeSubscription._streamIdentifiers
+ OBJC_IVAR_$_BMComputeSubscription._subscriber
+ OBJC_IVAR_$_BMComputeSubscription._token
+ OBJC_IVAR_$_BMComputeSubscription._uniqueIdentifier
+ OBJC_IVAR_$_BMComputeSubscription._useCase
+ OBJC_IVAR_$_BMComputeSubscription._waking
+ OBJC_IVAR_$_BMComputeTombstonePropagator._user
+ OBJC_IVAR_$_BMStreamVirtualTable._useCase
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCSW_Tt0g5
+ _$s10Foundation4DateV026timeIntervalSinceReferenceB0Sdvg
+ _$s10Foundation4DateVSgWOh
+ _$s12BiomeStreams0B0O11StoreStreamV10identifier11storeConfigAEy_xGSS_So07BMStoreG0CtcfC
+ _$s12BiomeStreams12DBViewWriterVWOr
+ _$s12BiomeStreams14UnifiedLibraryO7libraryAA0D4Base_pXpvpZMV
+ _$s12BiomeStreams19StoreStreamProtocolPAAE9publisher9startDate03endH09maxEvents5lastN8reversed0A6PubSub21BookmarkablePublisherVySo12BMStoreEventCy0S0QzGG10Foundation0H0VSg_AVSiSgAWSbtF
+ _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE13groupBySchema0hI6FieldsSaySS_0A9SQLParser11SQLDataTypeOtGSayAF13SQLExpressionVG_tFZAA0c11AggregationfG0V_Tt0g5
+ _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE13groupBySchema0hI6FieldsSaySS_0A9SQLParser11SQLDataTypeOtGSayAF13SQLExpressionVG_tFZAA0c19FirstMatchingRecordG0V_Tt0g5
+ _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE13groupBySchema0hI6FieldsSaySS_0A9SQLParser11SQLDataTypeOtGSayAF13SQLExpressionVG_tFZAA0c19FirstMatchingRecordG0V_Tt0g5Tm
+ _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE8setValue_6forKeyy0I0Qz_SayAA08StorableI0OGtKFAA0c19FirstMatchingRecordG0V_Tg5
+ _$s12BiomeStreams7LoggingO13accessService2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO15flexibleStorage2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO18distributedContext2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO3DSL2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO3SQL2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO4sync2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO4test2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO6pubSub2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO6sensor2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO6source2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO6stream2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO7compute2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO7general2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO7library2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO7metrics2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO7privacy2os6LoggerVvpZMV
+ _$s12BiomeStreams7LoggingO7storage2os6LoggerVvpZMV
+ _$s14BiomeSQLParser11SQLFunctionO8allCasesSayACGvpZMV
+ _$s14BiomeSQLParser12PgQuery_ListVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser13PgQuery_FloatVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser15PgQuery_IntegerVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser15PgQuery_RawStmtV2eeoiySbAC_ACtFZTf4nnd_nTm
+ _$s14BiomeSQLParser17PgQuery_ColumnRefVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser19PgQuery_ParseResultVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser20PgQuery_DropRoleStmtVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser21PgQuery_AlterTypeStmtVSQAASQ2eeoiySbx_xtFZTWTm
+ _$s14BiomeSQLParser25PgQuery_DeclareCursorStmtV14_uniqueStorage33_A784F7F2ED97E043416F18646CF1BF17LLAC01_I5ClassAELLCyFTf4n_g
+ _$s14BiomeSQLParser26PgQuery_AlternativeSubPlanV13decodeMessage7decoderyxz_tK21InternalSwiftProtobuf7DecoderRzlFTm
+ _$s17PoirotSchematizer15SchematizedDataCMa
+ _$sSD11updateValue_6forKeyq_Sgq_n_xtFSS_12BiomeStreams08StorableB0OTg5
+ _$sSDsSQR_rlE2eeoiySbSDyxq_G_ABtFZSS_14BiomeSQLParser11SQLDataTypeOTt1g5
+ _$sSDyq_SgxcisSay12BiomeStreams13StorableValueOG_SDySSADGTg5
+ _$sSLsE1goiySbx_xtFZ10Foundation4UUIDV_Tt1g5
+ _$sSLsE1goiySbx_xtFZSS_Tt1g5
+ _$sSS3key_12BiomeStreams13StorableValueO5valuetWOb
+ _$sSTsE7flatMapySay7ElementQyd__Gqd__ABQzKXEKSTRd__lFSD6ValuesVySSSaySSG_G_AHTg581$s12BiomeStreams21BMDatabaseInitializerC014viewSubscribedB0ShySSGyFZSaySSGAFXEfU_Tf1cn_n
+ _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyF14BiomeSQLParser6SchemaV_Tg5Tm
+ _$sSa13_adoptStorage_5countSayxG_SpyxGts016_ContiguousArrayB0CyxGn_SitFZ12BiomeStreams13StorableValueO_Tt1g5
+ _$sSa13_adoptStorage_5countSayxG_SpyxGts016_ContiguousArrayB0CyxGn_SitFZ14BiomeSQLParser11SQLDataTypeO_Tt1g5
+ _$sSa13_adoptStorage_5countSayxG_SpyxGts016_ContiguousArrayB0CyxGn_SitFZ14BiomeSQLParser6SchemaV_Tt1g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ12BiomeStreams13StorableValueO_Tt0g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser11SQLDataTypeO_Tt0g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser11SQLDataTypeO_Tt0g5Tm
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser13SQLExpressionV_Tt0g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser19AggregationFunctionV_Tt0g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSS_12BiomeStreams13StorableValueOt_Tt0g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSS_Tt0g5
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSay14BiomeSQLParser19AggregationFunctionVG_Tt0g5
+ _$sSa9_getCountSiyFSo11BMSQLColumnC_Tg5
+ _$sSa9_getCountSiyFSo11BMSQLColumnC_Tg5Tm
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser11SQLDataTypeO_Tt1g5
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser12PgQuery_NodeV_Tt1g5
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser15PgQuery_RawStmtV_Tt1g5
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser17PgQuery_ScanTokenV_Tt1g5
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser19AggregationFunctionV_Tt1g5
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser7BindingV_Tt1g5
+ _$sSasSQRzlE2eeoiySbSayxG_ABtFZs6UInt64V_Tt1g5
+ _$sSd10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$sSi10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$sSlsE5first7ElementQzSgvgSDySS12BiomeStreams13DatabaseValueOG_Tg5
+ _$sSo13BMStoreStreamC07privateB10Identifier11storeConfig14eventDataClassAByxGSS_So0aF0CSgyXlXpSgtcfcTO
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF12BiomeStreams16DatabaseResource_pXp_Tg5Tm
+ _$ss15ContiguousArrayVAByxGycfCSS_Ttg5
+ _$ss15LazyMapSequenceV8IteratorV4nextq_SgyFSDySSSaySSGG_SS_AGtTg5
+ _$ss17_NativeDictionaryV11updateValue_6forKey8isUniqueq_Sgq_n_xSbtFSS_12BiomeStreams08StorableD0OTg5
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ _$ss6_merge3low3mid4high6buffer2bySbSpyxG_A3GSbx_xtKXEtKlF6$deferL_yylF14BiomeSQLParser13SQLExpressionV_Tg5
+ _$ss6_merge3low3mid4high6buffer2bySbSpyxG_A3GSbx_xtKXEtKlF6$deferL_yylF14BiomeSQLParser19AggregationFunctionV_Tg5Tm
+ _$ss6_merge3low3mid4high6buffer2bySbSpyxG_A3GSbx_xtKXEtKlF6$deferL_yylFSS3key_14BiomeSQLParser11SQLDataTypeO5valuet_Tg5
+ _BMAccessErrorDomain
+ _BMMachServiceNameSystemComputePublisherService
+ _BMMachServiceNameSystemComputeSourceService
+ _BMMachServiceNameUserComputePublisherService
+ _BMMachServiceNameUserComputeSourceService
+ _OBJC_CLASS_$_BMComputePublisherClient
+ _OBJC_CLASS_$_BMComputePublisherClientDomainConfiguration
+ _OBJC_CLASS_$_BMComputePublisherServer
+ _OBJC_CLASS_$_BMComputePublisherStorage
+ _OBJC_CLASS_$_BMComputeSubscription
+ _OBJC_CLASS_$_BMXPCConnectionFactory
+ _OBJC_CLASS_$_BMXPCListener
+ _OBJC_CLASS_$_NSBlock
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSMethodSignature
+ _OBJC_CLASS_$__BMManagedConfiguration
+ _OBJC_METACLASS_$_BMComputePublisherClient
+ _OBJC_METACLASS_$_BMComputePublisherClientDomainConfiguration
+ _OBJC_METACLASS_$_BMComputePublisherServer
+ _OBJC_METACLASS_$_BMComputePublisherStorage
+ _OBJC_METACLASS_$_BMComputeSubscription
+ _OUTLINED_FUNCTION_213
+ _OUTLINED_FUNCTION_214
+ _OUTLINED_FUNCTION_215
+ _OUTLINED_FUNCTION_216
+ _OUTLINED_FUNCTION_217
+ _OUTLINED_FUNCTION_218
+ _OUTLINED_FUNCTION_219
+ _OUTLINED_FUNCTION_220
+ _OUTLINED_FUNCTION_221
+ _OUTLINED_FUNCTION_222
+ _OUTLINED_FUNCTION_223
+ _OUTLINED_FUNCTION_224
+ _OUTLINED_FUNCTION_225
+ _OUTLINED_FUNCTION_226
+ _OUTLINED_FUNCTION_227
+ _OUTLINED_FUNCTION_228
+ _OUTLINED_FUNCTION_229
+ _OUTLINED_FUNCTION_230
+ _OUTLINED_FUNCTION_231
+ _OUTLINED_FUNCTION_232
+ _OUTLINED_FUNCTION_233
+ _OUTLINED_FUNCTION_234
+ _OUTLINED_FUNCTION_235
+ _OUTLINED_FUNCTION_236
+ _OUTLINED_FUNCTION_237
+ _OUTLINED_FUNCTION_238
+ _OUTLINED_FUNCTION_239
+ _OUTLINED_FUNCTION_240
+ _OUTLINED_FUNCTION_241
+ _OUTLINED_FUNCTION_242
+ _OUTLINED_FUNCTION_243
+ _OUTLINED_FUNCTION_244
+ _OUTLINED_FUNCTION_245
+ _OUTLINED_FUNCTION_246
+ _OUTLINED_FUNCTION_247
+ _OUTLINED_FUNCTION_248
+ _OUTLINED_FUNCTION_249
+ _OUTLINED_FUNCTION_250
+ _OUTLINED_FUNCTION_251
+ _OUTLINED_FUNCTION_252
+ _OUTLINED_FUNCTION_253
+ _OUTLINED_FUNCTION_254
+ _OUTLINED_FUNCTION_255
+ _OUTLINED_FUNCTION_256
+ _OUTLINED_FUNCTION_257
+ _OUTLINED_FUNCTION_258
+ _OUTLINED_FUNCTION_259
+ _OUTLINED_FUNCTION_260
+ _OUTLINED_FUNCTION_261
+ _OUTLINED_FUNCTION_262
+ _OUTLINED_FUNCTION_263
+ __104+[BMEventSession sessionPublisherWithStreamPublisher:startingBlock:endingBlock:sessionKeyBlock:options:]_block_invoke.9
+ __32-[BMDSLTableStream bpsPublisher]_block_invoke.cold.1
+ __33+[BMDaemon registerXPCActivities]_block_invoke.74
+ __33+[BMDaemon registerXPCActivities]_block_invoke_2.75
+ __38-[BMComputePublisherClient connection]_block_invoke.35
+ __38-[BMComputePublisherServer subscribe:]_block_invoke.19
+ __422-[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:]_block_invoke.59
+ __46-[BMComputePublisherClient subscribeViaNSXPC:]_block_invoke.cold.1
+ __49-[BMComputePublisherClient subscribeViaXPCEvent:]_block_invoke.cold.1
+ __54-[BMComputePublisherClient unsubscribeWithIdentifier:]_block_invoke.cold.1
+ __63-[BMComputePublisherServer listener:shouldAcceptNewConnection:]_block_invoke.13
+ __67+[BMComputePublisherClient initializeSharedClientWithQueue:domain:]_block_invoke.cold.1
+ __68-[BMStreamBase(PeriodicMaintenance) executePruningPolicyForAccount:]_block_invoke.5
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.26
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.26.cold.1
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.33
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.33.cold.1
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.35
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.35.cold.1
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.35.cold.2
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.35.cold.3
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.35.cold.4
+ __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.35.cold.5
+ __81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke.10
+ __81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke.21
+ __84-[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]_block_invoke.cold.1
+ __94-[BMComputePublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]_block_invoke.4
+ __94-[BMComputePublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]_block_invoke.4.cold.1
+ __98+[BMPairedEventSession sessionPublisherWithStreamPublisher:startingBlock:sessionKeyBlock:options:]_block_invoke.66
+ __OBJC_$_CLASS_METHODS_BMComputePublisherClient
+ __OBJC_$_CLASS_METHODS_BMComputePublisherServer
+ __OBJC_$_CLASS_METHODS_BMComputePublisherStorage(BMBiomeSchedulerAdditions)
+ __OBJC_$_CLASS_METHODS_BMComputeSubscription
+ __OBJC_$_CLASS_PROP_LIST_BMComputeSubscription
+ __OBJC_$_INSTANCE_METHODS_BMComputePublisherClient
+ __OBJC_$_INSTANCE_METHODS_BMComputePublisherClientDomainConfiguration
+ __OBJC_$_INSTANCE_METHODS_BMComputePublisherServer
+ __OBJC_$_INSTANCE_METHODS_BMComputePublisherStorage
+ __OBJC_$_INSTANCE_METHODS_BMComputeSubscription
+ __OBJC_$_INSTANCE_VARIABLES_BMComputePublisherClient
+ __OBJC_$_INSTANCE_VARIABLES_BMComputePublisherClientDomainConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BMComputePublisherServer
+ __OBJC_$_INSTANCE_VARIABLES_BMComputePublisherStorage
+ __OBJC_$_INSTANCE_VARIABLES_BMComputeSubscription
+ __OBJC_$_PROP_LIST_BMComputePublisherClient
+ __OBJC_$_PROP_LIST_BMComputePublisherClientDomainConfiguration
+ __OBJC_$_PROP_LIST_BMComputePublisherServer
+ __OBJC_$_PROP_LIST_BMComputePublisherStorage
+ __OBJC_$_PROP_LIST_BMComputeSubscription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMComputePublisherServerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMComputeSourceDaemon
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMConnectionProxyable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMComputePublisherServerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMComputeSourceDaemon
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMConnectionProxyable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_BMComputeSourceDaemon
+ __OBJC_$_PROTOCOL_REFS_NSXPCConnectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BMComputePublisherClient
+ __OBJC_CLASS_PROTOCOLS_$_BMComputePublisherServer
+ __OBJC_CLASS_PROTOCOLS_$_BMComputeSubscription
+ __OBJC_CLASS_RO_$_BMComputePublisherClient
+ __OBJC_CLASS_RO_$_BMComputePublisherClientDomainConfiguration
+ __OBJC_CLASS_RO_$_BMComputePublisherServer
+ __OBJC_CLASS_RO_$_BMComputePublisherStorage
+ __OBJC_CLASS_RO_$_BMComputeSubscription
+ __OBJC_LABEL_PROTOCOL_$_BMComputePublisherServerDelegate
+ __OBJC_LABEL_PROTOCOL_$_BMComputeSourceDaemon
+ __OBJC_LABEL_PROTOCOL_$_BMConnectionProxyable
+ __OBJC_LABEL_PROTOCOL_$_BMXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSXPCConnectionDelegate
+ __OBJC_METACLASS_RO_$_BMComputePublisherClient
+ __OBJC_METACLASS_RO_$_BMComputePublisherClientDomainConfiguration
+ __OBJC_METACLASS_RO_$_BMComputePublisherServer
+ __OBJC_METACLASS_RO_$_BMComputePublisherStorage
+ __OBJC_METACLASS_RO_$_BMComputeSubscription
+ __OBJC_PROTOCOL_$_BMComputePublisherServerDelegate
+ __OBJC_PROTOCOL_$_BMComputeSourceDaemon
+ __OBJC_PROTOCOL_$_BMConnectionProxyable
+ __OBJC_PROTOCOL_$_BMXPCListenerDelegate
+ __OBJC_PROTOCOL_$_NSXPCConnectionDelegate
+ ___102-[BMSQLDatabase initWithVirtualTables:privileges:isColumnAccessLoggingEnabled:enableAuthorizer:error:]_block_invoke
+ ___122-[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:]_block_invoke
+ ___32+[BMLibraryStreamsPruner domain]_block_invoke
+ ___38-[BMComputePublisherClient connection]_block_invoke
+ ___38-[BMComputePublisherServer subscribe:]_block_invoke
+ ___40-[BMSQLDatabase executeStatement:error:]_block_invoke
+ ___43-[BMComputeSourceServer _acceptConnection:]_block_invoke
+ ___45+[_BMLibraryNode streamWithIdentifier:error:]_block_invoke
+ ___45-[BMComputePublisherServer _addSubscription:]_block_invoke
+ ___46-[BMComputePublisherClient subscribeViaNSXPC:]_block_invoke
+ ___47-[BMComputePublisherClient handleBiomeRelaunch]_block_invoke
+ ___49-[BMComputePublisherClient subscribeViaXPCEvent:]_block_invoke
+ ___51-[BMComputePublisherServer subscriptionsForStream:]_block_invoke
+ ___54-[BMComputePublisherClient unsubscribeWithIdentifier:]_block_invoke
+ ___57-[BMComputePublisherServer _removeSubscriptionWithToken:]_block_invoke
+ ___59-[BMComputePublisherClient registerBiomeLaunchNotification]_block_invoke
+ ___61+[BMLibraryStreamsPruner _pruneStreamsWithPolicy:parameters:]_block_invoke
+ ___63-[BMComputePublisherServer listener:shouldAcceptNewConnection:]_block_invoke
+ ___65+[BMLibraryStreamsPruner _pruneStream:policy:trigger:parameters:]_block_invoke
+ ___65+[BMLibraryStreamsPruner _pruneStream:policy:trigger:parameters:]_block_invoke_2
+ ___66-[BMComputePublisherClient numberOfExistingNonWakingSubscriptions]_block_invoke
+ ___67+[BMComputePublisherClient initializeSharedClientWithQueue:domain:]_block_invoke
+ ___69-[BMComputePublisherServer _removeSubscriptionWithIdentifier:client:]_block_invoke
+ ___84-[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]_block_invoke
+ ___94-[BMComputePublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]_block_invoke
+ ___block_descriptor_32_e48_B24?0"BMComputeSubscription"8"NSDictionary"16l
+ ___block_descriptor_40_e38_B32?0"BMComputeSubscription"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e38_B32?0"BMComputeSubscription"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e48_B24?0"BMComputeSubscription"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e61_v32?0"BMComputeSubscription"8"NSString"16"BMStoreEvent"24l
+ ___block_descriptor_48_e8_32bs40w_e61_v32?0"BMComputeSubscription"8"NSString"16"BMStoreEvent"24l
+ ___block_descriptor_48_e8_32s40s_e38_B32?0"BMComputeSubscription"8Q16^B24l
+ ___block_descriptor_48_e8_32s40w_e61_v32?0"BMComputeSubscription"8"NSString"16"BMStoreEvent"24l
+ ___block_descriptor_64_e8_32s40s48r_e56_v24?0"BMStreamBase"8"BMStreamBuiltinPruningTrigger"16l
+ ___block_descriptor_64_e8_32s40s48s_e26_B24?0"BMStoreEvent"8^B16l
+ __block_literal_global.145
+ __block_literal_global.147
+ __block_literal_global.154
+ __block_literal_global.156
+ __block_literal_global.16
+ __block_literal_global.19
+ __block_literal_global.193
+ __block_literal_global.196
+ __block_literal_global.21
+ __block_literal_global.235
+ __block_literal_global.238
+ __block_literal_global.29
+ __block_literal_global.5
+ __block_literal_global.51
+ __block_literal_global.53
+ __block_literal_global.55
+ __block_literal_global.62
+ __block_literal_global.69
+ __block_literal_global.72
+ __block_literal_global.73
+ __block_literal_global.76
+ __block_literal_global.85
+ __swift_get_extra_inhabitant_index.3353Tm
+ __swift_get_extra_inhabitant_index.3374Tm
+ __swift_get_extra_inhabitant_index.3392Tm
+ __swift_get_extra_inhabitant_index.3464Tm
+ __swift_get_extra_inhabitant_index.3543Tm
+ __swift_get_extra_inhabitant_index.3552Tm
+ __swift_get_extra_inhabitant_index.3561Tm
+ __swift_get_extra_inhabitant_index.3567Tm
+ __swift_get_extra_inhabitant_index.3570Tm
+ __swift_get_extra_inhabitant_index.3648Tm
+ __swift_get_extra_inhabitant_index.3666Tm
+ __swift_get_extra_inhabitant_index.3696Tm
+ __swift_get_extra_inhabitant_index.3708Tm
+ __swift_get_extra_inhabitant_index.3750Tm
+ __swift_get_extra_inhabitant_index.3771Tm
+ __swift_get_extra_inhabitant_index.3786Tm
+ __swift_get_extra_inhabitant_index.3801Tm
+ __swift_get_extra_inhabitant_index.3849Tm
+ __swift_get_extra_inhabitant_index.3855Tm
+ __swift_get_extra_inhabitant_index.3903Tm
+ __swift_get_extra_inhabitant_index.4212Tm
+ __swift_store_extra_inhabitant_index.3354Tm
+ __swift_store_extra_inhabitant_index.3375Tm
+ __swift_store_extra_inhabitant_index.3393Tm
+ __swift_store_extra_inhabitant_index.3465Tm
+ __swift_store_extra_inhabitant_index.3544Tm
+ __swift_store_extra_inhabitant_index.3553Tm
+ __swift_store_extra_inhabitant_index.3562Tm
+ __swift_store_extra_inhabitant_index.3568Tm
+ __swift_store_extra_inhabitant_index.3649Tm
+ __swift_store_extra_inhabitant_index.3667Tm
+ __swift_store_extra_inhabitant_index.3709Tm
+ __swift_store_extra_inhabitant_index.3751Tm
+ __swift_store_extra_inhabitant_index.3754Tm
+ __swift_store_extra_inhabitant_index.3772Tm
+ __swift_store_extra_inhabitant_index.3787Tm
+ __swift_store_extra_inhabitant_index.3802Tm
+ __swift_store_extra_inhabitant_index.3850Tm
+ __swift_store_extra_inhabitant_index.3856Tm
+ __swift_store_extra_inhabitant_index.3904Tm
+ __swift_store_extra_inhabitant_index.4153Tm
+ __swift_store_extra_inhabitant_index.4213Tm
+ _acceptConnection:.interface
+ _acceptConnection:.onceToken
+ _bm_invoke
+ _deparseFunctionWithArgtypesList
+ _deparseNameList
+ _deparseNumericOnlyList
+ _deparseQualifiedNameList
+ _getuid
+ _objc_msgSend$_acceptConnection:
+ _objc_msgSend$_classForObjectAtArgumentIndex:
+ _objc_msgSend$_enumerateAllPruningTriggersForPolicy:block:
+ _objc_msgSend$_newConnectionForDomain:
+ _objc_msgSend$_pruneStream:policy:trigger:parameters:
+ _objc_msgSend$_pruneStreamsWithPolicy:parameters:
+ _objc_msgSend$_remoteObjectProxyForDomain:errorHandler:
+ _objc_msgSend$allowAppleIntelligenceReport
+ _objc_msgSend$allowsAccessToProxyBiomeAgentEndpoint
+ _objc_msgSend$allowsConfiguringConnection:forUseCase:inDomain:error:
+ _objc_msgSend$allowsConnectionToComputeSourceServiceWithDomain:
+ _objc_msgSend$bm_accessControlPolicy
+ _objc_msgSend$bm_connectionFlags
+ _objc_msgSend$bm_process
+ _objc_msgSend$bm_remoteUseCase
+ _objc_msgSend$canAccessAppleKeyStore
+ _objc_msgSend$connectionToComputeSourceServerInDomain:user:useCase:
+ _objc_msgSend$connectionToMachService:endpoint:useCase:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$endpoint
+ _objc_msgSend$evaluateWithObject:substitutionVariables:
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$getArgument:atIndex:
+ _objc_msgSend$getArgumentTypeAtIndex:
+ _objc_msgSend$initWithMachServiceName:queue:
+ _objc_msgSend$initWithQueue:domain:source:
+ _objc_msgSend$initWithQueue:domain:source:listener:
+ _objc_msgSend$initWithStream:permission:config:includeTombstones:eventDataClass:useCase:
+ _objc_msgSend$initWithStreamIdentifier:domain:listenerEndpoint:storage:user:
+ _objc_msgSend$initWithStreamIdentifier:domain:useCase:user:
+ _objc_msgSend$initWithStreamIdentifier:domain:user:
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invoke
+ _objc_msgSend$invokeWithTarget:
+ _objc_msgSend$isValid
+ _objc_msgSend$methodSignature
+ _objc_msgSend$numberOfArguments
+ _objc_msgSend$predicateWithFormat:argumentArray:
+ _objc_msgSend$predicateWithValue:
+ _objc_msgSend$pruningPredicate
+ _objc_msgSend$pruningTriggers
+ _objc_msgSend$replaceFileAtPath:withData:protection:flags:error:
+ _objc_msgSend$replyBlockSignatureForSelector:
+ _objc_msgSend$replyToInvocation:withError:
+ _objc_msgSend$retainArguments
+ _objc_msgSend$selector
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setBm_accessControlPolicy:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$signatureWithObjCTypes:
+ _objc_msgSend$triggerCondition
+ _objc_msgSend$validateConnection:error:
+ _serviceDomain
+ domain.onceToken
- +[BMComputeSourceClient setUseSynchronousXPCMessageSending:]
- +[BMComputeXPCPublisherClient _setQueue:domain:]
- +[BMComputeXPCPublisherClient initializeSharedClientWithQueue:domain:]
- +[BMComputeXPCPublisherClient new]
- +[BMComputeXPCPublisherClient sharedWithQueue:domain:]
- +[BMComputeXPCPublisherClient shared]
- +[BMComputeXPCPublisherServer new]
- +[BMComputeXPCPublisherStorage currentSession]
- +[BMComputeXPCPublisherStorage(BMBiomeSchedulerAdditions) bookmarkStorageForCurrentProcess]
- +[BMComputeXPCSubscription new]
- +[BMComputeXPCSubscription storageForIdentifier:]
- +[BMComputeXPCSubscription storageForIdentifier:].cold.1
- +[BMComputeXPCSubscription supportsSecureCoding]
- +[BMDaemon systemComputePublisherServiceName]
- +[BMDaemon systemComputeSourceServiceName]
- +[BMDaemon userComputePublisherServiceName]
- +[BMDaemon userComputeSourceServiceName]
- +[BMLibraryStreamsPruner _pruneStream:policy:shouldPruneBlock:]
- +[BMLibraryStreamsPruner _pruneStreamWithIdentifier:policy:shouldPruneBlock:]
- +[BMLibraryStreamsPruner bundleIdentifiersFromStoreEvent:]
- +[BMLibraryStreamsPruner bundleIdentifiersFromStoreEvent:].cold.1
- +[BMLibraryStreamsPruner contactIdentifiersFromStoreEvent:]
- +[BMLibraryStreamsPruner contactIdentifiersFromStoreEvent:].cold.1
- +[BMLibraryStreamsPruner intentGroupIdentifierFromStoreEvent:]
- +[BMLibraryStreamsPruner intentGroupIdentifierFromStoreEvent:].cold.1
- +[BMLibraryStreamsPruner intentIdentifierFromStoreEvent:]
- +[BMLibraryStreamsPruner intentIdentifierFromStoreEvent:].cold.1
- +[BMLibraryStreamsPruner isDonatedBySiriFromStoreEvent:]
- +[BMLibraryStreamsPruner isDonatedBySiriFromStoreEvent:].cold.1
- +[BMLibraryStreamsPruner pruneForResetKeyboardDictionary].cold.1
- +[BMLibraryStreamsPruner pruneForResetPrivacyAndLocationWarnings].cold.1
- +[BMLibraryStreamsPruner pruneLearnFromThisAppDisabledForMessages]
- +[BMLibraryStreamsPruner pruneLearnFromThisAppDisabledForMessages].cold.1
- +[BMLibraryStreamsPruner pruneLearnFromThisAppDisabledForMessages].cold.2
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forDeletedContactIdentifiers:]
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forDeletedGroupIdentifiers:bundleId:]
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forDeletedIntentIdentifiers:bundleId:]
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forDeletedIntentIdentifiers:bundleId:].cold.1
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forInstalledApplications:installedAppExtensions:]
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forLearnFromThisAppDisabledBundleIdentifiers:]
- +[BMLibraryStreamsPruner shouldPruneStoreEvent:forUninstalledBundleId:]
- +[BMLibraryStreamsPruner shouldPruneStoreEventForSiriAndDictationHistoryDeletion:]
- +[BMLibraryStreamsPruner shouldPruneStoreEventForSiriDisabled:]
- -[BMComputeSourceClient connection]
- -[BMComputeSourceClient dealloc]
- -[BMComputeSourceClient initWithStreamIdentifier:domain:useCase:]
- -[BMComputeSourceClient initWithStreamIdentifier:domain:useCase:].cold.1
- -[BMComputeSourceClient initWithStreamIdentifier:machServiceName:listenerEndpoint:storage:]
- -[BMComputeSourceClient storage]
- -[BMComputeSourceServer connections]
- -[BMComputeSourceServer description]
- -[BMComputeSourceServer initWithQueue:machServiceName:source:]
- -[BMComputeSourceServer initWithQueue:source:listener:]
- -[BMComputeSourceServer interface]
- -[BMComputeSourceServer listener]
- -[BMComputeSourceServerConnection .cxx_destruct]
- -[BMComputeSourceServerConnection accessControlPolicy]
- -[BMComputeSourceServerConnection clientProcess]
- -[BMComputeSourceServerConnection description]
- -[BMComputeSourceServerConnection eventsPrunedWithStreamIdentifier:account:remoteName:reason:]
- -[BMComputeSourceServerConnection eventsPrunedWithStreamIdentifier:account:remoteName:reason:].cold.1
- -[BMComputeSourceServerConnection initWithServer:clientProcess:]
- -[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:]
- -[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.1
- -[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.2
- -[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.3
- -[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.4
- -[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:].cold.5
- -[BMComputeSourceServerConnection server]
- -[BMComputeSubscriptionMarkerManager _subscriptionMarkerStorageForDomain:].cold.1
- -[BMComputeTombstonePropagator initWithStreamIdentifier:domain:]
- -[BMComputeXPCPublisherClient .cxx_destruct]
- -[BMComputeXPCPublisherClient _handleEventWithPayload:]
- -[BMComputeXPCPublisherClient _handleEventWithPayload:].cold.1
- -[BMComputeXPCPublisherClient _setXPCEvent:identifier:]
- -[BMComputeXPCPublisherClient _setXPCEvent:identifier:].cold.1
- -[BMComputeXPCPublisherClient computePublisherObjectWithErrorHandler:]
- -[BMComputeXPCPublisherClient connection]
- -[BMComputeXPCPublisherClient dealloc]
- -[BMComputeXPCPublisherClient handleBiomeRelaunch]
- -[BMComputeXPCPublisherClient initWithQueue:configuration:listenerEndpoint:localComputePublisher:]
- -[BMComputeXPCPublisherClient initWithQueue:domain:listenerEndpoint:localComputePublisher:]
- -[BMComputeXPCPublisherClient init]
- -[BMComputeXPCPublisherClient isRegisteredForRelaunchNotification]
- -[BMComputeXPCPublisherClient numberOfExistingNonWakingSubscriptions]
- -[BMComputeXPCPublisherClient pendingEvents]
- -[BMComputeXPCPublisherClient queue]
- -[BMComputeXPCPublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:]
- -[BMComputeXPCPublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:].cold.1
- -[BMComputeXPCPublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:].cold.2
- -[BMComputeXPCPublisherClient registerBiomeLaunchNotification]
- -[BMComputeXPCPublisherClient registerBiomeLaunchNotification].cold.1
- -[BMComputeXPCPublisherClient subscribe:]
- -[BMComputeXPCPublisherClient subscribeViaNSXPC:]
- -[BMComputeXPCPublisherClient subscribeViaXPCEvent:]
- -[BMComputeXPCPublisherClient subscriptions]
- -[BMComputeXPCPublisherClient unregisterBiomeLaunchNotification]
- -[BMComputeXPCPublisherClient unregisterBiomeLaunchNotification].cold.1
- -[BMComputeXPCPublisherClient unregisterBiomeLaunchNotification].cold.2
- -[BMComputeXPCPublisherClient unsubscribeWithIdentifier:]
- -[BMComputeXPCPublisherClient unsubscribeWithIdentifier:].cold.1
- -[BMComputeXPCPublisherClientDomainConfiguration .cxx_destruct]
- -[BMComputeXPCPublisherClientDomainConfiguration XPCPublisherStreamName]
- -[BMComputeXPCPublisherClientDomainConfiguration biomeLaunchNotification]
- -[BMComputeXPCPublisherClientDomainConfiguration domain]
- -[BMComputeXPCPublisherClientDomainConfiguration initWithDomain:]
- -[BMComputeXPCPublisherClientDomainConfiguration initWithDomain:].cold.1
- -[BMComputeXPCPublisherClientDomainConfiguration machServiceName]
- -[BMComputeXPCPublisherServer .cxx_destruct]
- -[BMComputeXPCPublisherServer _addSubscription:]
- -[BMComputeXPCPublisherServer _handlePublisherAction:token:descriptor:]
- -[BMComputeXPCPublisherServer _handlePublisherAction:token:descriptor:].cold.1
- -[BMComputeXPCPublisherServer _handlePublisherAction:token:descriptor:].cold.2
- -[BMComputeXPCPublisherServer _removeActiveSubscriptionMarkersForSubscription:]
- -[BMComputeXPCPublisherServer _removeSubscriptionWithIdentifier:client:]
- -[BMComputeXPCPublisherServer _removeSubscriptionWithToken:]
- -[BMComputeXPCPublisherServer activateWithCompletion:]
- -[BMComputeXPCPublisherServer activateWithCompletion:].cold.1
- -[BMComputeXPCPublisherServer activationCompletion]
- -[BMComputeXPCPublisherServer delegate]
- -[BMComputeXPCPublisherServer description]
- -[BMComputeXPCPublisherServer domain]
- -[BMComputeXPCPublisherServer initWithQueue:domain:delegate:]
- -[BMComputeXPCPublisherServer initWithQueue:domain:delegate:].cold.1
- -[BMComputeXPCPublisherServer initWithQueue:domain:delegate:].cold.2
- -[BMComputeXPCPublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]
- -[BMComputeXPCPublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:].cold.1
- -[BMComputeXPCPublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:].cold.2
- -[BMComputeXPCPublisherServer init]
- -[BMComputeXPCPublisherServer interface]
- -[BMComputeXPCPublisherServer listener:shouldAcceptNewConnection:]
- -[BMComputeXPCPublisherServer listener:shouldAcceptNewConnection:].cold.1
- -[BMComputeXPCPublisherServer listener:shouldAcceptNewConnection:].cold.2
- -[BMComputeXPCPublisherServer listener]
- -[BMComputeXPCPublisherServer publisher]
- -[BMComputeXPCPublisherServer queue]
- -[BMComputeXPCPublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]
- -[BMComputeXPCPublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:].cold.1
- -[BMComputeXPCPublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:].cold.2
- -[BMComputeXPCPublisherServer setActivationCompletion:]
- -[BMComputeXPCPublisherServer storage]
- -[BMComputeXPCPublisherServer storage].cold.1
- -[BMComputeXPCPublisherServer subscribe:]
- -[BMComputeXPCPublisherServer subscribe:].cold.1
- -[BMComputeXPCPublisherServer subscribe:].cold.2
- -[BMComputeXPCPublisherServer subscribe:].cold.3
- -[BMComputeXPCPublisherServer subscribe:].cold.4
- -[BMComputeXPCPublisherServer subscribe:].cold.5
- -[BMComputeXPCPublisherServer subscribe:].cold.6
- -[BMComputeXPCPublisherServer subscriptionMarkerManager]
- -[BMComputeXPCPublisherServer subscriptionsForStream:]
- -[BMComputeXPCPublisherServer subscriptions]
- -[BMComputeXPCPublisherServer systemStorage]
- -[BMComputeXPCPublisherServer unsubscribeWithIdentifier:]
- -[BMComputeXPCPublisherServer unsubscribeWithIdentifier:].cold.1
- -[BMComputeXPCPublisherServer unsubscribeWithIdentifier:].cold.2
- -[BMComputeXPCPublisherServer userStorage]
- -[BMComputeXPCPublisherStorage .cxx_destruct]
- -[BMComputeXPCPublisherStorage basePath]
- -[BMComputeXPCPublisherStorage bookmarkPathForSessionStorageWithIdentifier:client:]
- -[BMComputeXPCPublisherStorage checkActiveSubscriptionMarkerForStream:]
- -[BMComputeXPCPublisherStorage checkActiveSubscriptionMarkerForStream:].cold.1
- -[BMComputeXPCPublisherStorage checkExistenceOfBookmarkForSubscriptionWithIdentifier:client:]
- -[BMComputeXPCPublisherStorage currentSessionBookmarkClientOrServerPath]
- -[BMComputeXPCPublisherStorage currentSessionBookmarkPath]
- -[BMComputeXPCPublisherStorage currentSessionNonwakingSubscriptionPath]
- -[BMComputeXPCPublisherStorage currentSessionPath]
- -[BMComputeXPCPublisherStorage currentSessionSubscriptionsPath]
- -[BMComputeXPCPublisherStorage domain]
- -[BMComputeXPCPublisherStorage initWithUseCase:domain:isClient:]
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession]
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.1
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.2
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.3
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.4
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.5
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.6
- -[BMComputeXPCPublisherStorage initializeBiomeDSLDirectoryForBootSession].cold.7
- -[BMComputeXPCPublisherStorage isClient]
- -[BMComputeXPCPublisherStorage newFileManagerWithUseCase:]
- -[BMComputeXPCPublisherStorage persistentPath]
- -[BMComputeXPCPublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:]
- -[BMComputeXPCPublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.1
- -[BMComputeXPCPublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.2
- -[BMComputeXPCPublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.3
- -[BMComputeXPCPublisherStorage readBookmarkForSubscriptionWithIdentifier:client:error:].cold.4
- -[BMComputeXPCPublisherStorage readNonWakingSubscriptions:]
- -[BMComputeXPCPublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:]
- -[BMComputeXPCPublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:].cold.1
- -[BMComputeXPCPublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:].cold.2
- -[BMComputeXPCPublisherStorage readNonwakingSubscriptionWithIdentifier:client:error:].cold.3
- -[BMComputeXPCPublisherStorage removeActiveSubscriptionMarkerForStream:]
- -[BMComputeXPCPublisherStorage removeActiveSubscriptionMarkerForStream:].cold.1
- -[BMComputeXPCPublisherStorage removeBookmarkFileForSubscriptionWithIdentifier:client:]
- -[BMComputeXPCPublisherStorage removeBookmarkFileForSubscriptionWithIdentifier:client:].cold.1
- -[BMComputeXPCPublisherStorage removeNonWakingSubscriptionWithIdentifier:client:]
- -[BMComputeXPCPublisherStorage removeNonWakingSubscriptionWithIdentifier:client:].cold.1
- -[BMComputeXPCPublisherStorage removeNonWakingSubscriptionWithIdentifier:client:].cold.2
- -[BMComputeXPCPublisherStorage sessionsPath]
- -[BMComputeXPCPublisherStorage subscriptionMarkerPathForSessionStorageWithStream:]
- -[BMComputeXPCPublisherStorage writeActiveSubscriptionMarkerForStream:]
- -[BMComputeXPCPublisherStorage writeActiveSubscriptionMarkerForStream:].cold.1
- -[BMComputeXPCPublisherStorage writeBookmark:forSubscriptionWithIdentifier:client:]
- -[BMComputeXPCPublisherStorage writeBookmark:forSubscriptionWithIdentifier:client:].cold.1
- -[BMComputeXPCPublisherStorage writeNonWakingSubscription:]
- -[BMComputeXPCPublisherStorage writeNonWakingSubscription:].cold.1
- -[BMComputeXPCPublisherStorage writeNonWakingSubscription:].cold.2
- -[BMComputeXPCPublisherStorage writeNonWakingSubscription:].cold.3
- -[BMComputeXPCSubscription .cxx_destruct]
- -[BMComputeXPCSubscription XPCEvent]
- -[BMComputeXPCSubscription XPCEvent].cold.1
- -[BMComputeXPCSubscription XPCEvent].cold.2
- -[BMComputeXPCSubscription block]
- -[BMComputeXPCSubscription client]
- -[BMComputeXPCSubscription connection]
- -[BMComputeXPCSubscription createdAt]
- -[BMComputeXPCSubscription description]
- -[BMComputeXPCSubscription encodeWithCoder:]
- -[BMComputeXPCSubscription fetchBookmarkFromStorage:error:]
- -[BMComputeXPCSubscription graph]
- -[BMComputeXPCSubscription identifier]
- -[BMComputeXPCSubscription initWithCoder:]
- -[BMComputeXPCSubscription initWithIdentifier:client:createdAt:waking:DSLGraph:subscriber:block:]
- -[BMComputeXPCSubscription initWithIdentifier:client:createdAt:waking:DSLGraph:subscriber:block:].cold.1
- -[BMComputeXPCSubscription initWithIdentifier:client:createdAt:waking:DSLGraph:subscriber:block:].cold.2
- -[BMComputeXPCSubscription initWithIdentifier:client:waking:DSLGraph:block:]
- -[BMComputeXPCSubscription initWithToken:descriptor:]
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.1
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.2
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.3
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.4
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.5
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.6
- -[BMComputeXPCSubscription initWithToken:descriptor:].cold.7
- -[BMComputeXPCSubscription init]
- -[BMComputeXPCSubscription initialBookmarkTimestamp]
- -[BMComputeXPCSubscription isUnclaimed]
- -[BMComputeXPCSubscription pendingDemand]
- -[BMComputeXPCSubscription postMigrationStreamIdentifiers]
- -[BMComputeXPCSubscription setClient:]
- -[BMComputeXPCSubscription setConnection:]
- -[BMComputeXPCSubscription setInitialBookmarkTimestamp:]
- -[BMComputeXPCSubscription setPendingDemand:]
- -[BMComputeXPCSubscription startEvent]
- -[BMComputeXPCSubscription streamIdentifiers]
- -[BMComputeXPCSubscription subscriber]
- -[BMComputeXPCSubscription token]
- -[BMComputeXPCSubscription uniqueIdentifier]
- -[BMComputeXPCSubscription useCase]
- -[BMComputeXPCSubscription waking]
- -[BMStoreStreamPruningBridge initWithStreamIdentifier:domain:]
- -[BMStreamBuiltinPruningTrigger initWithIdentifier:platforms:triggerCondition:pruningPredicate:]
- -[BMStreamBuiltinPruningTrigger platforms]
- FunctionCall5Coll.cold.1
- GCC_except_table150
- GCC_except_table29
- GCC_except_table30
- GCC_except_table31
- GCC_except_table43
- GCC_except_table45
- GCC_except_table47
- GCC_except_table49
- GCC_except_table57
- GCC_except_table58
- GCC_except_table61
- GCC_except_table62
- GCC_except_table63
- GCC_except_table64
- GCC_except_table68
- GCC_except_table69
- GCC_except_table70
- GCC_except_table71
- GCC_except_table72
- GCC_except_table73
- GCC_except_table8
- OBJC_IVAR_$_BMComputeSourceClient._connection
- OBJC_IVAR_$_BMComputeSourceClient._lock
- OBJC_IVAR_$_BMComputeSourceClient._machServiceName
- OBJC_IVAR_$_BMComputeSourceServer._connections
- OBJC_IVAR_$_BMComputeSourceServer._interface
- OBJC_IVAR_$_BMComputeSourceServerConnection._accessControlPolicy
- OBJC_IVAR_$_BMComputeSourceServerConnection._clientProcess
- OBJC_IVAR_$_BMComputeSourceServerConnection._server
- OBJC_IVAR_$_BMComputeXPCPublisherClient._configuration
- OBJC_IVAR_$_BMComputeXPCPublisherClient._connection
- OBJC_IVAR_$_BMComputeXPCPublisherClient._listenerEndpoint
- OBJC_IVAR_$_BMComputeXPCPublisherClient._localComputePublisher
- OBJC_IVAR_$_BMComputeXPCPublisherClient._lock
- OBJC_IVAR_$_BMComputeXPCPublisherClient._pendingEvents
- OBJC_IVAR_$_BMComputeXPCPublisherClient._queue
- OBJC_IVAR_$_BMComputeXPCPublisherClient._subscriptions
- OBJC_IVAR_$_BMComputeXPCPublisherClient._token
- OBJC_IVAR_$_BMComputeXPCPublisherClientDomainConfiguration._XPCPublisherStreamName
- OBJC_IVAR_$_BMComputeXPCPublisherClientDomainConfiguration._biomeLaunchNotification
- OBJC_IVAR_$_BMComputeXPCPublisherClientDomainConfiguration._domain
- OBJC_IVAR_$_BMComputeXPCPublisherClientDomainConfiguration._machServiceName
- OBJC_IVAR_$_BMComputeXPCPublisherServer._activationCompletion
- OBJC_IVAR_$_BMComputeXPCPublisherServer._delegate
- OBJC_IVAR_$_BMComputeXPCPublisherServer._domain
- OBJC_IVAR_$_BMComputeXPCPublisherServer._interface
- OBJC_IVAR_$_BMComputeXPCPublisherServer._listener
- OBJC_IVAR_$_BMComputeXPCPublisherServer._publisher
- OBJC_IVAR_$_BMComputeXPCPublisherServer._queue
- OBJC_IVAR_$_BMComputeXPCPublisherServer._subscriptionMarkerManager
- OBJC_IVAR_$_BMComputeXPCPublisherServer._subscriptions
- OBJC_IVAR_$_BMComputeXPCPublisherServer._systemStorage
- OBJC_IVAR_$_BMComputeXPCPublisherServer._userStorage
- OBJC_IVAR_$_BMComputeXPCPublisherStorage._domain
- OBJC_IVAR_$_BMComputeXPCPublisherStorage._fileManager
- OBJC_IVAR_$_BMComputeXPCPublisherStorage._isClient
- OBJC_IVAR_$_BMComputeXPCSubscription._block
- OBJC_IVAR_$_BMComputeXPCSubscription._client
- OBJC_IVAR_$_BMComputeXPCSubscription._connection
- OBJC_IVAR_$_BMComputeXPCSubscription._createdAt
- OBJC_IVAR_$_BMComputeXPCSubscription._graph
- OBJC_IVAR_$_BMComputeXPCSubscription._identifier
- OBJC_IVAR_$_BMComputeXPCSubscription._initialBookmarkTimestamp
- OBJC_IVAR_$_BMComputeXPCSubscription._pendingDemand
- OBJC_IVAR_$_BMComputeXPCSubscription._postMigrationStreamIdentifiers
- OBJC_IVAR_$_BMComputeXPCSubscription._streamIdentifiers
- OBJC_IVAR_$_BMComputeXPCSubscription._subscriber
- OBJC_IVAR_$_BMComputeXPCSubscription._token
- OBJC_IVAR_$_BMComputeXPCSubscription._uniqueIdentifier
- OBJC_IVAR_$_BMComputeXPCSubscription._useCase
- OBJC_IVAR_$_BMComputeXPCSubscription._waking
- OBJC_IVAR_$_BMStreamBuiltinPruningTrigger._platforms
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCSW_Tgm5
- _$s12BiomeStreams0B0O11StoreStreamV9validatorSo16BMStoreValidatorCyxGyF
- _$s12BiomeStreams13BookmarkCacheV9tableName016materializedViewF0S2S_tFZ
- _$s12BiomeStreams14UnifiedLibraryO011initializedD033_850BEB6472663B017EAF49437FB662E4LLAC0D0AELLOmvpZfiAGmyXEfU_SSSgSScfU_
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO3add7libraryyAA0D4Base_pXp_tFZySayAaI_pXpGzYbXEfU_
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO3add7libraryyAA0D4Base_pXp_tFZySayAaI_pXpGzYbXEfU_TA
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO9librariesSayAA0D4Base_pXpGvgZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO9librariesSayAA0D4Base_pXpGvgZA2IzYbXEfU_
- _$s12BiomeStreams29KeyedAggregationMetadataCacheV9tableName016materializedViewH0S2S_tFZTm
- _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE06updateG033_6F9EC546C4F68F936355D3F38A853B4ALL_6forKeyy5ValueQzSg_SayAA08StorableT0OGtFAA0c11AggregationfG0V_Tg5
- _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE06updateG033_6F9EC546C4F68F936355D3F38A853B4ALL_6forKeyy5ValueQzSg_SayAA08StorableT0OGtFAA0c19FirstMatchingRecordG0V_Tg5
- _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE13groupBySchema0hI6FieldsSaySS_0A9SQLParser11SQLDataTypeOtGSayAF13SQLExpressionVG_tFZAA0c11AggregationfG0V_Tgm5
- _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE13groupBySchema0hI6FieldsSaySS_0A9SQLParser11SQLDataTypeOtGSayAF13SQLExpressionVG_tFZAA0c19FirstMatchingRecordG0V_Tgm5
- _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE13groupBySchema0hI6FieldsSaySS_0A9SQLParser11SQLDataTypeOtGSayAF13SQLExpressionVG_tFZAA0c19FirstMatchingRecordG0V_Tgm5Tm
- _$s12BiomeStreams30KeyedQueryPlannerMetadataCachePAAE14createTableSQL20materializedViewName6schemaS2S_SDySS0A9SQLParser11SQLDataTypeOGtKFZS2S_AItKXEfU_
- _$s12BiomeStreams8DataflowVSgMD
- _$s12BiomeStreams8DataflowVSgWOb
- _$s12BiomeStreams8DataflowVSgWObTm
- _$s14BiomeSQLParser08PgQuery_D0V2eeoiySbAC_ACtFZ
- _$s14BiomeSQLParser08PgQuery_D6SourceO8allCases_WZ
- _$s14BiomeSQLParser08PgQuery_D6SourceO8allCases_Wz
- _$s14BiomeSQLParser12PgQuery_NodeV2eeoiySbAC_ACtFZ
- _$s14BiomeSQLParser12PgQuery_NullV13decodeMessage7decoderyxz_tK21InternalSwiftProtobuf7DecoderRzlFTm
- _$s14BiomeSQLParser13PgQuery_AliasV2eeoiySbAC_ACtFZ
- _$s14BiomeSQLParser13PgQuery_TokenO8allCases_WZ
- _$s14BiomeSQLParser13PgQuery_TokenO8allCases_Wz
- _$s14BiomeSQLParser13SQLExpressionVSgWObTm
- _$s14BiomeSQLParser15LogicalPlanTypeOWOb
- _$s14BiomeSQLParser15PgQuery_CmdTypeO8allCases_WZ
- _$s14BiomeSQLParser15PgQuery_CmdTypeO8allCases_Wz
- _$s14BiomeSQLParser15PgQuery_RTEKindO8allCases_WZ
- _$s14BiomeSQLParser15PgQuery_RTEKindO8allCases_Wz
- _$s14BiomeSQLParser15PgQuery_WCOKindO8allCases_WZ
- _$s14BiomeSQLParser15PgQuery_WCOKindO8allCases_Wz
- _$s14BiomeSQLParser16PgQuery_AggSplitO8allCases_WZ
- _$s14BiomeSQLParser16PgQuery_AggSplitO8allCases_Wz
- _$s14BiomeSQLParser16PgQuery_JoinTypeO8allCases_WZ
- _$s14BiomeSQLParser16PgQuery_JoinTypeO8allCases_Wz
- _$s14BiomeSQLParser16PgQuery_MinMaxOpO8allCases_WZ
- _$s14BiomeSQLParser16PgQuery_MinMaxOpO8allCases_Wz
- _$s14BiomeSQLParser16PgQuery_ParamRefV2eeoiySbAC_ACtFZTf4nnd_n
- _$s14BiomeSQLParser16PgQuery_SetOpCmdO8allCases_WZ
- _$s14BiomeSQLParser16PgQuery_SetOpCmdO8allCases_Wz
- _$s14BiomeSQLParser17PgQuery_ParamKindO8allCases_WZ
- _$s14BiomeSQLParser17PgQuery_ParamKindO8allCases_Wz
- _$s14BiomeSQLParser17PgQuery_SortByDirO8allCases_WZ
- _$s14BiomeSQLParser17PgQuery_SortByDirO8allCases_Wz
- _$s14BiomeSQLParser17PgQuery_XmlExprOpO8allCases_WZ
- _$s14BiomeSQLParser17PgQuery_XmlExprOpO8allCases_Wz
- _$s14BiomeSQLParser18PgQuery_ConstrTypeO8allCases_WZ
- _$s14BiomeSQLParser18PgQuery_ConstrTypeO8allCases_Wz
- _$s14BiomeSQLParser18PgQuery_ObjectTypeO8allCases_WZ
- _$s14BiomeSQLParser18PgQuery_ObjectTypeO8allCases_Wz
- _$s14BiomeSQLParser18PgQuery_SelectStmtV2eeoiySbAC_ACtFZ
- _$s14BiomeSQLParser18PgQuery_WithClauseV2eeoiySbAC_ACtFZ
- _$s14BiomeSQLParser19PgQuery_A_ArrayExprV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser19PgQuery_A_Expr_KindO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_A_Expr_KindO8allCases_Wz
- _$s14BiomeSQLParser19PgQuery_AggStrategyO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_AggStrategyO8allCases_Wz
- _$s14BiomeSQLParser19PgQuery_CallContextV2eeoiySbAC_ACtFZTf4nnd_n
- _$s14BiomeSQLParser19PgQuery_DiscardModeO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_DiscardModeO8allCases_Wz
- _$s14BiomeSQLParser19PgQuery_KeywordKindO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_KeywordKindO8allCases_Wz
- _$s14BiomeSQLParser19PgQuery_LimitOptionO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_LimitOptionO8allCases_Wz
- _$s14BiomeSQLParser19PgQuery_ParseResultV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser19PgQuery_RangeTblRefV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser19PgQuery_SortByNullsO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_SortByNullsO8allCases_Wz
- _$s14BiomeSQLParser19PgQuery_SubLinkTypeO8allCases_WZ
- _$s14BiomeSQLParser19PgQuery_SubLinkTypeO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_BoolExprTypeO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_BoolExprTypeO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_BoolTestTypeO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_BoolTestTypeO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_CoercionFormO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_CoercionFormO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_DropBehaviorO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_DropBehaviorO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_NullTestTypeO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_NullTestTypeO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_RoleSpecTypeO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_RoleSpecTypeO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_RoleStmtTypeO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_RoleStmtTypeO8allCases_Wz
- _$s14BiomeSQLParser20PgQuery_SetOperationO8allCases_WZ
- _$s14BiomeSQLParser20PgQuery_SetOperationO8allCases_Wz
- _$s14BiomeSQLParser21PgQuery_ClusterOptionO8allCases_WZ
- _$s14BiomeSQLParser21PgQuery_ClusterOptionO8allCases_Wz
- _$s14BiomeSQLParser21PgQuery_CollateClauseV2eeoiySbAC_ACtFZ
- _$s14BiomeSQLParser21PgQuery_DefElemActionO8allCases_WZ
- _$s14BiomeSQLParser21PgQuery_DefElemActionO8allCases_Wz
- _$s14BiomeSQLParser21PgQuery_LockTupleModeO8allCases_WZ
- _$s14BiomeSQLParser21PgQuery_LockTupleModeO8allCases_Wz
- _$s14BiomeSQLParser21PgQuery_SetOpStrategyO8allCases_WZ
- _$s14BiomeSQLParser21PgQuery_SetOpStrategyO8allCases_Wz
- _$s14BiomeSQLParser21PgQuery_XmlOptionTypeO8allCases_WZ
- _$s14BiomeSQLParser21PgQuery_XmlOptionTypeO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_AlterTableTypeO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_AlterTableTypeO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_CTEMaterializeO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_CTEMaterializeO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_FetchDirectionO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_FetchDirectionO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_LockWaitPolicyO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_LockWaitPolicyO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_MultiAssignRefV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser22PgQuery_OnCommitActionO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_OnCommitActionO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_OverridingKindO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_OverridingKindO8allCases_Wz
- _$s14BiomeSQLParser22PgQuery_OverridingKindOs12CaseIterableAAsADP8allCases03AllJ0QzvgZTWTm
- _$s14BiomeSQLParser22PgQuery_RowCompareTypeO8allCases_WZ
- _$s14BiomeSQLParser22PgQuery_RowCompareTypeO8allCases_Wz
- _$s14BiomeSQLParser23PgQuery_CoercionContextO8allCases_WZ
- _$s14BiomeSQLParser23PgQuery_CoercionContextO8allCases_Wz
- _$s14BiomeSQLParser23PgQuery_GrantTargetTypeO8allCases_WZ
- _$s14BiomeSQLParser23PgQuery_GrantTargetTypeO8allCases_Wz
- _$s14BiomeSQLParser23PgQuery_GroupingSetKindO8allCases_WZ
- _$s14BiomeSQLParser23PgQuery_GroupingSetKindO8allCases_Wz
- _$s14BiomeSQLParser23PgQuery_TableLikeOptionO8allCases_WZ
- _$s14BiomeSQLParser23PgQuery_TableLikeOptionO8allCases_Wz
- _$s14BiomeSQLParser23PgQuery_VariableSetKindO8allCases_WZ
- _$s14BiomeSQLParser23PgQuery_VariableSetKindO8allCases_Wz
- _$s14BiomeSQLParser23PgQuery_ViewCheckOptionO8allCases_WZ
- _$s14BiomeSQLParser23PgQuery_ViewCheckOptionO8allCases_Wz
- _$s14BiomeSQLParser24PgQuery_OnConflictActionO8allCases_WZ
- _$s14BiomeSQLParser24PgQuery_OnConflictActionO8allCases_Wz
- _$s14BiomeSQLParser24PgQuery_VariableShowStmtV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser25PgQuery_AlterTSConfigTypeO8allCases_WZ
- _$s14BiomeSQLParser25PgQuery_AlterTSConfigTypeO8allCases_Wz
- _$s14BiomeSQLParser25PgQuery_DeclareCursorStmtV13_StorageClass33_A784F7F2ED97E043416F18646CF1BF17LLC7copyingA2F_tcfc
- _$s14BiomeSQLParser25PgQuery_ReindexObjectTypeO8allCases_WZ
- _$s14BiomeSQLParser25PgQuery_ReindexObjectTypeO8allCases_Wz
- _$s14BiomeSQLParser25PgQuery_TableSampleClauseV13_StorageClass33_A784F7F2ED97E043416F18646CF1BF17LLC7copyingA2F_tcfc
- _$s14BiomeSQLParser26PgQuery_AlterCollationStmtV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser26PgQuery_AlternativeSubPlanV14_uniqueStorage33_A784F7F2ED97E043416F18646CF1BF17LLAC01_I5ClassAELLCyFTf4n_gTm
- _$s14BiomeSQLParser26PgQuery_ConstraintsSetStmtV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser26PgQuery_LockClauseStrengthO8allCases_WZ
- _$s14BiomeSQLParser26PgQuery_LockClauseStrengthO8allCases_Wz
- _$s14BiomeSQLParser26PgQuery_SQLValueFunctionOpO8allCases_WZ
- _$s14BiomeSQLParser26PgQuery_SQLValueFunctionOpO8allCases_Wz
- _$s14BiomeSQLParser27PgQuery_TransactionStmtKindO8allCases_WZ
- _$s14BiomeSQLParser27PgQuery_TransactionStmtKindO8allCases_Wz
- _$s14BiomeSQLParser29PgQuery_AlterSubscriptionTypeO8allCases_WZ
- _$s14BiomeSQLParser29PgQuery_AlterSubscriptionTypeO8allCases_Wz
- _$s14BiomeSQLParser29PgQuery_AlterTSDictionaryStmtV2eeoiySbAC_ACtFZTf4nnd_nTm
- _$s14BiomeSQLParser29PgQuery_FunctionParameterModeO8allCases_WZ
- _$s14BiomeSQLParser29PgQuery_FunctionParameterModeO8allCases_Wz
- _$s14BiomeSQLParser31PgQuery_ImportForeignSchemaTypeO8allCases_WZ
- _$s14BiomeSQLParser31PgQuery_ImportForeignSchemaTypeO8allCases_Wz
- _$s14BiomeSQLParser31PgQuery_PartitionRangeDatumKindO8allCases_WZ
- _$s14BiomeSQLParser31PgQuery_PartitionRangeDatumKindO8allCases_Wz
- _$s17PoirotSchematizer15SchematizedDataVMa
- _$sSD8_VariantV11removeValue6forKeyq_Sgx_tFSay12BiomeStreams08StorableC0OG_SDySSAHGTg5
- _$sSD8_VariantV11updateValue_6forKeyq_Sgq_n_xtFq_Say12BiomeStreams08StorableC0OGAByAIq__GAeIRszr0_lIetMiglr_Tp5AF12ChangeRecordV5value_AF10CacheEventO5eventt_Tg5
- _$sSD8_VariantV11updateValue_6forKeyq_Sgq_n_xtFq_Say12BiomeStreams08StorableC0OGAByAIq__GAeIRszr0_lIetMiglr_Tp5AF12ChangeRecordVSg_Tg5
- _$sSD8_VariantV11updateValue_6forKeyq_Sgq_n_xtFq_Say12BiomeStreams08StorableC0OGAByAIq__GAeIRszr0_lIetMiglr_Tp5SaySDySSAHGG5value_AF10CacheEventO5eventt_Tg5
- _$sSD8_VariantV11updateValue_6forKeyq_Sgq_n_xtFq_Say12BiomeStreams08StorableC0OGAByAIq__GAeIRszr0_lIetMiglr_Tp5SaySDySSAHGGSg_Tg5
- _$sSD8_VariantV8setValue_6forKeyyq_n_xtFSS_s13OpaquePointerVTg5
- _$sSD8_VariantV8setValue_6forKeyyq_n_xtFSS_s13OpaquePointerVTg5Tm
- _$sSD8_VariantV8setValue_6forKeyyq_n_xtFSay12BiomeStreams08StorableC0OG_SDySSAGGTg5
- _$sSD8endIndexSD0B0Vyxq__GvgSS_12BiomeStreams13DatabaseValueOTg5
- _$sSDsSQR_rlE2eeoiySbSDyxq_G_ABtFZSS_14BiomeSQLParser11SQLDataTypeOTgm5
- _$sSLsE1goiySbx_xtFZ10Foundation4UUIDV_Tgm5
- _$sSLsE1goiySbx_xtFZSS_Tgm5
- _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyF14BiomeSQLParser13SQLExpressionV_Tg5
- _$sSa13_adoptStorage_5countSayxG_SpyxGts016_ContiguousArrayB0CyxGn_SitFZ12BiomeStreams13StorableValueO_Tgm5
- _$sSa13_adoptStorage_5countSayxG_SpyxGts016_ContiguousArrayB0CyxGn_SitFZ14BiomeSQLParser11SQLDataTypeO_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ12BiomeStreams13StorableValueO_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser11SQLDataTypeO_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser11SQLDataTypeO_Tgm5Tm
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser13SQLExpressionV_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZ14BiomeSQLParser19AggregationFunctionV_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSS_12BiomeStreams13StorableValueOt_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSS_Tgm5
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSay14BiomeSQLParser19AggregationFunctionVG_Tgm5
- _$sSa29_hoistableIsNativeTypeCheckedSbyFSS3key_14BiomeSQLParser010SQLRawDataD0O5valuet_Tg5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser11SQLDataTypeO_Tgm5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser12PgQuery_NodeV_Tgm5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser15PgQuery_RawStmtV_Tgm5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser17PgQuery_ScanTokenV_Tgm5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser19AggregationFunctionV_Tgm5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZ14BiomeSQLParser7BindingV_Tgm5
- _$sSasSQRzlE2eeoiySbSayxG_ABtFZs6UInt64V_Tgm5
- _$sSi6offset_12BiomeStreams11Aggregation_p7elementtSgMD
- _$sSp10initialize4from5countySPyxG_SitF12BiomeStreams11Aggregation_p_Tg5
- _$sSp10initialize4from5countySPyxG_SitF12BiomeStreams12ChangeRecordV_Tg5
- _$sSp10initialize4from5countySPyxG_SitF12BiomeStreams13StorableValueO_Tg5
- _$sSp10initialize4from5countySPyxG_SitF14BiomeSQLParser12ResultColumnV_Tg5
- _$sSp10initialize4from5countySPyxG_SitF14BiomeSQLParser13SQLExpressionV_Tg5
- _$sSp10initialize4from5countySPyxG_SitF14BiomeSQLParser19AggregationFunctionV_Tg5
- _$sSp10initialize4from5countySPyxG_SitF14BiomeSQLParser19AggregationFunctionV_Tg5Tm
- _$sSp10initialize4from5countySPyxG_SitF14BiomeSQLParser6SchemaV_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSDySS12BiomeStreams13StorableValueOG_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSDySS12BiomeStreams13StorableValueOG_Tg5Tm
- _$sSp10initialize4from5countySPyxG_SitFSS10columnName_14BiomeSQLParser11SQLDataTypeO04dataI0t_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSS11metadataKey_SS10columnName14BiomeSQLParser11SQLDataTypeO04dataK0t_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSS3key_12BiomeStreams13StorableValueO5valuet_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSS3key_14BiomeSQLParser11SQLDataTypeO5valuet_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSS3key_14BiomeSQLParser14SQLRawDataTypeO5valuet_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSS_14BiomeSQLParser11SQLDataTypeOt_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSS_14BiomeSQLParser11SQLDataTypeOt_Tg5Tm
- _$sSp10initialize4from5countySPyxG_SitFSS_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSay12BiomeStreams13StorableValueOG_Tg5
- _$sSp10initialize4from5countySPyxG_SitFSaySS11metadataKey_SS10columnName14BiomeSQLParser11SQLDataTypeO04dataK0tG_Tg5
- _$sSp10initialize4from5countySPyxG_SitFs5UInt8V_Tgq5
- _$sSp14moveInitialize4from5countySpyxG_SitF12BiomeStreams16DatabaseResource_pXp_Tg5Tm
- _$sSp14moveInitialize4from5countySpyxG_SitF12BiomeStreams8DataflowV_Tg5
- _$sSp14moveInitialize4from5countySpyxG_SitFSDySS12BiomeStreams13StorableValueOG_Tg5Tm
- _$sSp14moveInitialize4from5countySpyxG_SitFs5UInt8V_Tgq5
- _$sSv16initializeMemory2as4from5countSpyxGxm_SPyxGSitlFs5UInt8V_Tgmq5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF12BiomeStreams11Aggregation_p_Tg5
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF12BiomeStreams12ChangeRecordV_Tg5
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF12BiomeStreams16DatabaseResource_pXp_Tg5Tm
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF12BiomeStreams8DataflowV_Tg5
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF14BiomeSQLParser19AggregationFunctionV_Tg5Tm
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtFSDySS12BiomeStreams13StorableValueOG_Tg5
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtFSS_Tg5
- _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFSS3key_14BiomeSQLParser14SQLRawDataTypeO5valuet_Tg5
- _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF12BiomeStreams11LibraryBase_pXp_Tg5Tm
- _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF12BiomeStreams12ChangeRecordV_Tg5Tm
- _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFSS3key_14BiomeSQLParser14SQLRawDataTypeO5valuet_Tg5
- _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFSS_Tg5Tm
- _$ss15ContiguousArrayV12_endMutationyyFSS3key_14BiomeSQLParser14SQLRawDataTypeO5valuet_Tg5
- _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFSS3key_14BiomeSQLParser14SQLRawDataTypeO5valuet_Tg5
- _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFSS_Tg5Tm
- _$ss15ContiguousArrayV37_appendElementAssumeUniqueAndCapacity_03newD0ySi_xntFSS3key_14BiomeSQLParser14SQLRawDataTypeO5valuet_Tg5
- _$ss15ContiguousArrayVAByxGycfCSS_Tgm5
- _$ss17_NativeDictionaryV8setValue_6forKey8isUniqueyq_n_xSbtFSS_12BiomeStreams08StorableD0OTg5
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss17_assertionFailure__5flagss5NeverOs12StaticStringV_SSs6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tgmq5
- _$ss9_typeName_9qualifiedSSypXp_SbtF
- _$syXlN
- _$sypSgWOb
- _AnalyticsSendEventLazy
- _BMComputeSourceServerInterface
- _BMDevicePlatformOptionsToString
- _ClientEncoding
- _ClientEncoding$tlv$init
- _CurrentDynaHashCxt
- _CurrentDynaHashCxt$tlv$init
- _FunctionCall5Coll
- _OBJC_CLASS_$_BMComputeSourceServerConnection
- _OBJC_CLASS_$_BMComputeXPCPublisherClient
- _OBJC_CLASS_$_BMComputeXPCPublisherClientDomainConfiguration
- _OBJC_CLASS_$_BMComputeXPCPublisherServer
- _OBJC_CLASS_$_BMComputeXPCPublisherStorage
- _OBJC_CLASS_$_BMComputeXPCSubscription
- _OBJC_CLASS_$_NSMapTable
- _OBJC_METACLASS_$_BMComputeSourceServerConnection
- _OBJC_METACLASS_$_BMComputeXPCPublisherClient
- _OBJC_METACLASS_$_BMComputeXPCPublisherClientDomainConfiguration
- _OBJC_METACLASS_$_BMComputeXPCPublisherServer
- _OBJC_METACLASS_$_BMComputeXPCPublisherStorage
- _OBJC_METACLASS_$_BMComputeXPCSubscription
- _Utf8ToServerConvProc
- _Utf8ToServerConvProc$tlv$init
- __104+[BMEventSession sessionPublisherWithStreamPublisher:startingBlock:endingBlock:sessionKeyBlock:options:]_block_invoke.5
- __33+[BMDaemon registerXPCActivities]_block_invoke.86
- __33+[BMDaemon registerXPCActivities]_block_invoke_2.87
- __35-[BMComputeSourceClient connection]_block_invoke.52
- __41-[BMComputeXPCPublisherClient connection]_block_invoke.35
- __41-[BMComputeXPCPublisherServer subscribe:]_block_invoke.19
- __422-[BMMailContentEvent initWithUniqueId:domainId:personaId:absoluteTimestamp:accountIdentifier:messageIdentifier:fromHandle:toHandles:ccHandles:bccHandles:headers:subject:htmlContent:textContent:isFullyDownloaded:securityMethod:accountHandles:replyTo:mailboxIdentifiers:listId:accountType:attachments:contentProtection:conversationId:dateReceived:mailCategories:isNew:isTwoFactorCode:isFromMe:isJunk:isRead:isVIP:isFlagged:]_block_invoke.53
- __49-[BMComputeXPCPublisherClient subscribeViaNSXPC:]_block_invoke.cold.1
- __52-[BMComputeXPCPublisherClient subscribeViaXPCEvent:]_block_invoke.cold.1
- __57-[BMComputeXPCPublisherClient unsubscribeWithIdentifier:]_block_invoke.cold.1
- __60-[BMComputeSourceServer listener:shouldAcceptNewConnection:]_block_invoke.141
- __66-[BMComputeXPCPublisherServer listener:shouldAcceptNewConnection:]_block_invoke.13
- __68-[BMStreamBase(PeriodicMaintenance) executePruningPolicyForAccount:]_block_invoke.1
- __70+[BMComputeXPCPublisherClient initializeSharedClientWithQueue:domain:]_block_invoke.cold.1
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.14
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.20.cold.1
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.27
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.27.cold.1
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.29
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.29.cold.1
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.29.cold.2
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.29.cold.3
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.29.cold.4
- __78+[BMDaemon(LaunchDonations) _donateDeviceBootSessionEventsWithBootDate:queue:]_block_invoke.29.cold.5
- __81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke.17
- __81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke.6
- __87-[BMComputeXPCPublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]_block_invoke.cold.1
- __97-[BMComputeXPCPublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]_block_invoke.4
- __97-[BMComputeXPCPublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]_block_invoke.4.cold.1
- __98+[BMPairedEventSession sessionPublisherWithStreamPublisher:startingBlock:sessionKeyBlock:options:]_block_invoke.60
- __OBJC_$_CLASS_METHODS_BMComputeXPCPublisherClient
- __OBJC_$_CLASS_METHODS_BMComputeXPCPublisherServer
- __OBJC_$_CLASS_METHODS_BMComputeXPCPublisherStorage(BMBiomeSchedulerAdditions)
- __OBJC_$_CLASS_METHODS_BMComputeXPCSubscription
- __OBJC_$_CLASS_PROP_LIST_BMComputeXPCSubscription
- __OBJC_$_INSTANCE_METHODS_BMComputeSourceServerConnection
- __OBJC_$_INSTANCE_METHODS_BMComputeXPCPublisherClient
- __OBJC_$_INSTANCE_METHODS_BMComputeXPCPublisherClientDomainConfiguration
- __OBJC_$_INSTANCE_METHODS_BMComputeXPCPublisherServer
- __OBJC_$_INSTANCE_METHODS_BMComputeXPCPublisherStorage
- __OBJC_$_INSTANCE_METHODS_BMComputeXPCSubscription
- __OBJC_$_INSTANCE_VARIABLES_BMComputeSourceServerConnection
- __OBJC_$_INSTANCE_VARIABLES_BMComputeXPCPublisherClient
- __OBJC_$_INSTANCE_VARIABLES_BMComputeXPCPublisherClientDomainConfiguration
- __OBJC_$_INSTANCE_VARIABLES_BMComputeXPCPublisherServer
- __OBJC_$_INSTANCE_VARIABLES_BMComputeXPCPublisherStorage
- __OBJC_$_INSTANCE_VARIABLES_BMComputeXPCSubscription
- __OBJC_$_PROP_LIST_BMComputeSourceServerConnection
- __OBJC_$_PROP_LIST_BMComputeXPCPublisherClient
- __OBJC_$_PROP_LIST_BMComputeXPCPublisherClientDomainConfiguration
- __OBJC_$_PROP_LIST_BMComputeXPCPublisherServer
- __OBJC_$_PROP_LIST_BMComputeXPCPublisherStorage
- __OBJC_$_PROP_LIST_BMComputeXPCSubscription
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMComputeSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMComputeXPCPublisherServerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BMComputeSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_BMComputeXPCPublisherServerDelegate
- __OBJC_$_PROTOCOL_REFS_BMComputeSource
- __OBJC_CLASS_PROTOCOLS_$_BMComputeSourceServerConnection
- __OBJC_CLASS_PROTOCOLS_$_BMComputeXPCPublisherClient
- __OBJC_CLASS_PROTOCOLS_$_BMComputeXPCPublisherServer
- __OBJC_CLASS_PROTOCOLS_$_BMComputeXPCSubscription
- __OBJC_CLASS_RO_$_BMComputeSourceServerConnection
- __OBJC_CLASS_RO_$_BMComputeXPCPublisherClient
- __OBJC_CLASS_RO_$_BMComputeXPCPublisherClientDomainConfiguration
- __OBJC_CLASS_RO_$_BMComputeXPCPublisherServer
- __OBJC_CLASS_RO_$_BMComputeXPCPublisherStorage
- __OBJC_CLASS_RO_$_BMComputeXPCSubscription
- __OBJC_LABEL_PROTOCOL_$_BMComputeSource
- __OBJC_LABEL_PROTOCOL_$_BMComputeXPCPublisherServerDelegate
- __OBJC_METACLASS_RO_$_BMComputeSourceServerConnection
- __OBJC_METACLASS_RO_$_BMComputeXPCPublisherClient
- __OBJC_METACLASS_RO_$_BMComputeXPCPublisherClientDomainConfiguration
- __OBJC_METACLASS_RO_$_BMComputeXPCPublisherServer
- __OBJC_METACLASS_RO_$_BMComputeXPCPublisherStorage
- __OBJC_METACLASS_RO_$_BMComputeXPCSubscription
- __OBJC_PROTOCOL_$_BMComputeSource
- __OBJC_PROTOCOL_$_BMComputeXPCPublisherServerDelegate
- ___132-[BMComputeSourceServerConnection sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:]_block_invoke
- ___35-[BMComputeSourceClient connection]_block_invoke
- ___41-[BMComputeXPCPublisherClient connection]_block_invoke
- ___41-[BMComputeXPCPublisherServer subscribe:]_block_invoke
- ___43+[BMLibraryStreamsPruner pruneSiriDisabled]_block_invoke
- ___43+[BMLibraryStreamsPruner pruneSiriDisabled]_block_invoke_2
- ___48-[BMComputeXPCPublisherServer _addSubscription:]_block_invoke
- ___49-[BMComputeXPCPublisherClient subscribeViaNSXPC:]_block_invoke
- ___50-[BMComputeXPCPublisherClient handleBiomeRelaunch]_block_invoke
- ___52-[BMComputeXPCPublisherClient subscribeViaXPCEvent:]_block_invoke
- ___54+[BMLibraryStreamsPruner pruneSiriAndDictationHistory]_block_invoke
- ___54+[BMLibraryStreamsPruner pruneSiriAndDictationHistory]_block_invoke_2
- ___54-[BMComputeXPCPublisherServer subscriptionsForStream:]_block_invoke
- ___56+[BMLibraryStreamsPruner pruneLearnFromThisAppDisabled:]_block_invoke
- ___57+[BMLibraryStreamsPruner pruneForResetKeyboardDictionary]_block_invoke
- ___57-[BMComputeXPCPublisherClient unsubscribeWithIdentifier:]_block_invoke
- ___58+[BMLibraryStreamsPruner bundleIdentifiersFromStoreEvent:]_block_invoke
- ___59+[BMLibraryStreamsPruner contactIdentifiersFromStoreEvent:]_block_invoke
- ___60-[BMComputeSourceServer listener:shouldAcceptNewConnection:]_block_invoke
- ___60-[BMComputeXPCPublisherServer _removeSubscriptionWithToken:]_block_invoke
- ___61+[BMLibraryStreamsPruner pruneWithDeletedContactIdentifiers:]_block_invoke
- ___62-[BMComputeXPCPublisherClient registerBiomeLaunchNotification]_block_invoke
- ___63+[BMLibraryStreamsPruner pruneWithUninstalledBundleIdentifier:]_block_invoke
- ___65+[BMLibraryStreamsPruner pruneForResetPrivacyAndLocationWarnings]_block_invoke
- ___66+[BMLibraryStreamsPruner pruneLearnFromThisAppDisabledForMessages]_block_invoke
- ___66-[BMComputeXPCPublisherServer listener:shouldAcceptNewConnection:]_block_invoke
- ___69+[BMLibraryStreamsPruner pruneWithDeletedIntentIdentifiers:bundleId:]_block_invoke
- ___69-[BMComputeXPCPublisherClient numberOfExistingNonWakingSubscriptions]_block_invoke
- ___70+[BMComputeXPCPublisherClient initializeSharedClientWithQueue:domain:]_block_invoke
- ___72-[BMComputeXPCPublisherServer _removeSubscriptionWithIdentifier:client:]_block_invoke
- ___74+[BMLibraryStreamsPruner pruneWithDeletedIntentGroupIdentifiers:bundleId:]_block_invoke
- ___80+[BMLibraryStreamsPruner pruneWithInstalledApplications:installedAppExtensions:]_block_invoke
- ___87-[BMComputeXPCPublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]_block_invoke
- ___97-[BMComputeXPCPublisherServer initWithQueue:listener:domain:delegate:computePublisherStreamName:]_block_invoke
- ____logQueryResult_block_invoke
- ___block_descriptor_32_e51_B24?0"BMComputeXPCSubscription"8"NSDictionary"16l
- ___block_descriptor_40_e26_B24?0"BMStoreEvent"8^B16l
- ___block_descriptor_40_e41_B32?0"BMComputeXPCSubscription"8Q16^B24l
- ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8l
- ___block_descriptor_40_e8_32s_e41_B32?0"BMComputeXPCSubscription"8Q16^B24l
- ___block_descriptor_40_e8_32s_e51_B24?0"BMComputeXPCSubscription"8"NSDictionary"16l
- ___block_descriptor_40_e8_32s_e64_v32?0"BMComputeXPCSubscription"8"NSString"16"BMStoreEvent"24l
- ___block_descriptor_44_e19_"NSDictionary"8?0l
- ___block_descriptor_48_e8_32bs40w_e64_v32?0"BMComputeXPCSubscription"8"NSString"16"BMStoreEvent"24l
- ___block_descriptor_48_e8_32s40s_e41_B32?0"BMComputeXPCSubscription"8Q16^B24l
- ___block_descriptor_48_e8_32s40w_e5_v8?0l
- ___block_descriptor_48_e8_32s40w_e64_v32?0"BMComputeXPCSubscription"8"NSString"16"BMStoreEvent"24l
- ___block_descriptor_48_e8_32s_e26_B24?0"BMStoreEvent"8^B16l
- ___block_descriptor_52_e8_32s_e19_"NSDictionary"8?0l
- ___block_descriptor_56_e8_32s40s_e26_B24?0"BMStoreEvent"8^B16l
- ___getBMAppInFocusClass_block_invoke
- ___getBMAppInFocusIdentifierSymbolLoc_block_invoke
- ___getBMAppIntentClass_block_invoke
- ___getBMAppIntentIdentifierSymbolLoc_block_invoke
- ___getBMAppLocationActivityClass_block_invoke
- ___getBMAppLocationActivityIdentifierSymbolLoc_block_invoke
- ___getBMAutonamingMessagesInferencesIdentifierSymbolLoc_block_invoke
- ___getBMAutonamingMessagesMessageIdsIdentifierSymbolLoc_block_invoke
- ___getBMDictationUserEditIdentifierSymbolLoc_block_invoke
- ___getBMFrontBoardDisplayElementClass_block_invoke
- ___getBMFrontBoardDisplayElementIdentifierSymbolLoc_block_invoke
- ___getBMIntelligenceEngineInteractionClass_block_invoke
- ___getBMIntelligenceEngineInteractionDonationIdentifierSymbolLoc_block_invoke
- ___getBMKeyboardTokenFrequencyIdentifierSymbolLoc_block_invoke
- ___getBMLocationSemanticIdentifierSymbolLoc_block_invoke
- ___getBMMediaNowPlayingClass_block_invoke
- ___getBMMediaNowPlayingIdentifierSymbolLoc_block_invoke
- ___getBMProactiveHarvestingSiriQueryIdentifierSymbolLoc_block_invoke
- ___getBMScreenTimeAppUsageClass_block_invoke
- ___getBMScreenTimeAppUsageIdentifierSymbolLoc_block_invoke
- ___getBMSiriAppSelectionMusicIdentifierSymbolLoc_block_invoke
- ___getBMSiriAssistantSuggestionsClass_block_invoke
- ___getBMSiriAudioHistoryClass_block_invoke
- ___getBMSiriCallHistoryClass_block_invoke
- ___getBMSiriDictationIdentifierSymbolLoc_block_invoke
- ___getBMSiriExecutionIdentifierSymbolLoc_block_invoke
- ___getBMSiriFeedbackLearningUserInteractionsIdentifierSymbolLoc_block_invoke
- ___getBMSiriInteractionHistoryClass_block_invoke
- ___getBMSiriMessageHistoryClass_block_invoke
- ___getBMSiriPostSiriEngagementIdentifierSymbolLoc_block_invoke
- ___getBMSiriPrivateLearningSELFEventIdentifierSymbolLoc_block_invoke
- ___getBMSiriRemembersAssistantSuggestionsIdentifierSymbolLoc_block_invoke
- ___getBMSiriRemembersAudioHistoryIdentifierSymbolLoc_block_invoke
- ___getBMSiriRemembersCallHistoryIdentifierSymbolLoc_block_invoke
- ___getBMSiriRemembersIntentIdentifierSymbolLoc_block_invoke
- ___getBMSiriRemembersInteractionHistoryIdentifierSymbolLoc_block_invoke
- ___getBMSiriRemembersMessageHistoryIdentifierSymbolLoc_block_invoke
- ___getBMSiriSELFProcessedEventIdentifierSymbolLoc_block_invoke
- ___getBMSiriServiceIdentifierSymbolLoc_block_invoke
- ___logQueryResult_block_invoke.81
- __block_literal_global.139
- __block_literal_global.14
- __block_literal_global.141
- __block_literal_global.144
- __block_literal_global.148
- __block_literal_global.15
- __block_literal_global.187
- __block_literal_global.190
- __block_literal_global.20
- __block_literal_global.217
- __block_literal_global.220
- __block_literal_global.23
- __block_literal_global.25
- __block_literal_global.30
- __block_literal_global.33
- __block_literal_global.43
- __block_literal_global.45
- __block_literal_global.47
- __block_literal_global.56
- __block_literal_global.63
- __block_literal_global.66
- __block_literal_global.67
- __block_literal_global.70
- __block_literal_global.8
- __block_literal_global.9
- __block_literal_global.97
- __getBMAppInFocusClass_block_invoke.cold.1
- __getBMAppIntentClass_block_invoke.cold.1
- __getBMAppLocationActivityClass_block_invoke.cold.1
- __getBMFrontBoardDisplayElementClass_block_invoke.cold.1
- __getBMIntelligenceEngineInteractionClass_block_invoke.cold.1
- __getBMMediaNowPlayingClass_block_invoke.cold.1
- __getBMScreenTimeAppUsageClass_block_invoke.cold.1
- __getBMSiriAssistantSuggestionsClass_block_invoke.cold.1
- __getBMSiriAudioHistoryClass_block_invoke.cold.1
- __getBMSiriCallHistoryClass_block_invoke.cold.1
- __getBMSiriInteractionHistoryClass_block_invoke.cold.1
- __getBMSiriMessageHistoryClass_block_invoke.cold.1
- __logQueryResult
- __rand48_seed
- __rand48_seed$tlv$init
- __swift_get_extra_inhabitant_index.3296Tm
- __swift_get_extra_inhabitant_index.3317Tm
- __swift_get_extra_inhabitant_index.3335Tm
- __swift_get_extra_inhabitant_index.3407Tm
- __swift_get_extra_inhabitant_index.3486Tm
- __swift_get_extra_inhabitant_index.3495Tm
- __swift_get_extra_inhabitant_index.3504Tm
- __swift_get_extra_inhabitant_index.3510Tm
- __swift_get_extra_inhabitant_index.3513Tm
- __swift_get_extra_inhabitant_index.3591Tm
- __swift_get_extra_inhabitant_index.3609Tm
- __swift_get_extra_inhabitant_index.3639Tm
- __swift_get_extra_inhabitant_index.3651Tm
- __swift_get_extra_inhabitant_index.3693Tm
- __swift_get_extra_inhabitant_index.3714Tm
- __swift_get_extra_inhabitant_index.3729Tm
- __swift_get_extra_inhabitant_index.3744Tm
- __swift_get_extra_inhabitant_index.3792Tm
- __swift_get_extra_inhabitant_index.3798Tm
- __swift_get_extra_inhabitant_index.3846Tm
- __swift_get_extra_inhabitant_index.4155Tm
- __swift_store_extra_inhabitant_index.3297Tm
- __swift_store_extra_inhabitant_index.3318Tm
- __swift_store_extra_inhabitant_index.3336Tm
- __swift_store_extra_inhabitant_index.3408Tm
- __swift_store_extra_inhabitant_index.3487Tm
- __swift_store_extra_inhabitant_index.3496Tm
- __swift_store_extra_inhabitant_index.3505Tm
- __swift_store_extra_inhabitant_index.3511Tm
- __swift_store_extra_inhabitant_index.3592Tm
- __swift_store_extra_inhabitant_index.3610Tm
- __swift_store_extra_inhabitant_index.3640Tm
- __swift_store_extra_inhabitant_index.3652Tm
- __swift_store_extra_inhabitant_index.3694Tm
- __swift_store_extra_inhabitant_index.3715Tm
- __swift_store_extra_inhabitant_index.3730Tm
- __swift_store_extra_inhabitant_index.3745Tm
- __swift_store_extra_inhabitant_index.3793Tm
- __swift_store_extra_inhabitant_index.3799Tm
- __swift_store_extra_inhabitant_index.3847Tm
- __swift_store_extra_inhabitant_index.4096Tm
- __swift_store_extra_inhabitant_index.4156Tm
- __useSynchronousXPCMessageSending
- _deparseRefreshMatViewStmt
- _extensible_node_methods
- _extensible_node_methods$tlv$init
- _finish_spin_delay
- _fmod
- _fmodf
- _getBMAppInFocusIdentifier
- _getBMAppIntentClass
- _getBMAppIntentIdentifier
- _getBMAppLocationActivityClass
- _getBMAppLocationActivityIdentifier
- _getBMDictationUserEditIdentifier
- _getBMFrontBoardDisplayElementClass
- _getBMFrontBoardDisplayElementIdentifier
- _getBMIntelligenceEngineInteractionClass
- _getBMIntelligenceEngineInteractionDonationIdentifier
- _getBMMediaNowPlayingClass
- _getBMMediaNowPlayingIdentifier
- _getBMProactiveHarvestingSiriQueryIdentifier
- _getBMScreenTimeAppUsageClass
- _getBMScreenTimeAppUsageIdentifier
- _getBMSiriAppSelectionMusicIdentifier
- _getBMSiriAssistantSuggestionsClass
- _getBMSiriAudioHistoryClass
- _getBMSiriCallHistoryClass
- _getBMSiriDictationIdentifier
- _getBMSiriExecutionIdentifier
- _getBMSiriFeedbackLearningUserInteractionsIdentifier
- _getBMSiriInteractionHistoryClass
- _getBMSiriMessageHistoryClass
- _getBMSiriPostSiriEngagementIdentifier
- _getBMSiriPrivateLearningSELFEventIdentifier
- _getBMSiriRemembersAssistantSuggestionsIdentifier
- _getBMSiriRemembersAudioHistoryIdentifier
- _getBMSiriRemembersCallHistoryIdentifier
- _getBMSiriRemembersIntentIdentifier
- _getBMSiriRemembersInteractionHistoryIdentifier
- _getBMSiriRemembersMessageHistoryIdentifier
- _getBMSiriSELFProcessedEventIdentifier
- _getBMSiriServiceIdentifier
- _hash_search
- _hash_search_with_hash_value
- _max_stack_depth_bytes
- _max_stack_depth_bytes$tlv$init
- _num_seq_scans
- _num_seq_scans$tlv$init
- _objc_msgSend$_pruneStream:policy:shouldPruneBlock:
- _objc_msgSend$_pruneStreamWithIdentifier:policy:shouldPruneBlock:
- _objc_msgSend$allowsConnectionToComputeSourceService
- _objc_msgSend$appIntentInteractionIdentifier
- _objc_msgSend$bundleIdentifiersFromStoreEvent:
- _objc_msgSend$candidateId
- _objc_msgSend$candidateIds
- _objc_msgSend$candidateInteractions
- _objc_msgSend$connections
- _objc_msgSend$contactIdentifiersFromStoreEvent:
- _objc_msgSend$initWithBool:
- _objc_msgSend$initWithQueue:machServiceName:source:
- _objc_msgSend$initWithQueue:source:listener:
- _objc_msgSend$initWithServer:clientProcess:
- _objc_msgSend$initWithStream:permission:config:
- _objc_msgSend$initWithStreamIdentifier:domain:
- _objc_msgSend$initWithStreamIdentifier:domain:useCase:
- _objc_msgSend$initWithStreamIdentifier:machServiceName:listenerEndpoint:storage:
- _objc_msgSend$intentGroupIdentifierFromStoreEvent:
- _objc_msgSend$intentIdentifierFromStoreEvent:
- _objc_msgSend$intersectsSet:
- _objc_msgSend$isDonatedBySiriFromStoreEvent:
- _objc_msgSend$processType
- _objc_msgSend$pruneLearnFromThisAppDisabledForMessages
- _objc_msgSend$replaceFileAtPath:withData:protection:error:
- _objc_msgSend$shouldPruneStoreEvent:forDeletedContactIdentifiers:
- _objc_msgSend$shouldPruneStoreEvent:forDeletedGroupIdentifiers:bundleId:
- _objc_msgSend$shouldPruneStoreEvent:forDeletedIntentIdentifiers:bundleId:
- _objc_msgSend$shouldPruneStoreEvent:forInstalledApplications:installedAppExtensions:
- _objc_msgSend$shouldPruneStoreEvent:forLearnFromThisAppDisabledBundleIdentifiers:
- _objc_msgSend$shouldPruneStoreEvent:forUninstalledBundleId:
- _objc_msgSend$shouldPruneStoreEventForSiriAndDictationHistoryDeletion:
- _objc_msgSend$shouldPruneStoreEventForSiriDisabled:
- _objc_msgSend$strongToStrongObjectsMapTable
- _objc_msgSend$systemComputePublisherServiceName
- _objc_msgSend$systemComputeSourceServiceName
- _objc_msgSend$tupleInteraction
- _objc_msgSend$userComputePublisherServiceName
- _objc_msgSend$userComputeSourceServiceName
- _perform_spin_delay
- _pg_lrand48
- _pg_usleep
- _random
- _s_lock
- _select
- _seq_scan_tables
- _seq_scan_tables$tlv$init
- _spins_per_delay
- _spins_per_delay$tlv$init
- _sqlite3_column_table_name
- _swift_FORCE_LOAD_$_swiftFoundation.152
- _swift_FORCE_LOAD_$_swiftFoundation.4248
- _symbolic Si6offset_______p7elementtSg 12BiomeStreams11AggregationP
- _symbolic _____Sg 12BiomeStreams8DataflowV
- getBMAppInFocusClass.softClass
- getBMAppInFocusIdentifier.cold.1
- getBMAppInFocusIdentifierSymbolLoc.ptr
- getBMAppIntentClass.softClass
- getBMAppIntentIdentifier.cold.1
- getBMAppIntentIdentifierSymbolLoc.ptr
- getBMAppLocationActivityClass.softClass
- getBMAppLocationActivityIdentifier.cold.1
- getBMAppLocationActivityIdentifierSymbolLoc.ptr
- getBMAutonamingMessagesInferencesIdentifierSymbolLoc.ptr
- getBMAutonamingMessagesMessageIdsIdentifierSymbolLoc.ptr
- getBMDictationUserEditIdentifier.cold.1
- getBMDictationUserEditIdentifierSymbolLoc.ptr
- getBMFrontBoardDisplayElementClass.softClass
- getBMFrontBoardDisplayElementIdentifier.cold.1
- getBMFrontBoardDisplayElementIdentifierSymbolLoc.ptr
- getBMIntelligenceEngineInteractionClass.softClass
- getBMIntelligenceEngineInteractionDonationIdentifier.cold.1
- getBMIntelligenceEngineInteractionDonationIdentifierSymbolLoc.ptr
- getBMKeyboardTokenFrequencyIdentifierSymbolLoc.ptr
- getBMLocationSemanticIdentifierSymbolLoc.ptr
- getBMMediaNowPlayingClass.softClass
- getBMMediaNowPlayingIdentifier.cold.1
- getBMMediaNowPlayingIdentifierSymbolLoc.ptr
- getBMProactiveHarvestingSiriQueryIdentifier.cold.1
- getBMProactiveHarvestingSiriQueryIdentifierSymbolLoc.ptr
- getBMScreenTimeAppUsageClass.softClass
- getBMScreenTimeAppUsageIdentifier.cold.1
- getBMScreenTimeAppUsageIdentifierSymbolLoc.ptr
- getBMSiriAppSelectionMusicIdentifier.cold.1
- getBMSiriAppSelectionMusicIdentifierSymbolLoc.ptr
- getBMSiriAssistantSuggestionsClass.softClass
- getBMSiriAudioHistoryClass.softClass
- getBMSiriCallHistoryClass.softClass
- getBMSiriDictationIdentifier.cold.1
- getBMSiriDictationIdentifierSymbolLoc.ptr
- getBMSiriExecutionIdentifier.cold.1
- getBMSiriExecutionIdentifierSymbolLoc.ptr
- getBMSiriFeedbackLearningUserInteractionsIdentifier.cold.1
- getBMSiriFeedbackLearningUserInteractionsIdentifierSymbolLoc.ptr
- getBMSiriInteractionHistoryClass.softClass
- getBMSiriMessageHistoryClass.softClass
- getBMSiriPostSiriEngagementIdentifier.cold.1
- getBMSiriPostSiriEngagementIdentifierSymbolLoc.ptr
- getBMSiriPrivateLearningSELFEventIdentifier.cold.1
- getBMSiriPrivateLearningSELFEventIdentifierSymbolLoc.ptr
- getBMSiriRemembersAssistantSuggestionsIdentifier.cold.1
- getBMSiriRemembersAssistantSuggestionsIdentifierSymbolLoc.ptr
- getBMSiriRemembersAudioHistoryIdentifier.cold.1
- getBMSiriRemembersAudioHistoryIdentifierSymbolLoc.ptr
- getBMSiriRemembersCallHistoryIdentifier.cold.1
- getBMSiriRemembersCallHistoryIdentifierSymbolLoc.ptr
- getBMSiriRemembersIntentIdentifier.cold.1
- getBMSiriRemembersIntentIdentifierSymbolLoc.ptr
- getBMSiriRemembersInteractionHistoryIdentifier.cold.1
- getBMSiriRemembersInteractionHistoryIdentifierSymbolLoc.ptr
- getBMSiriRemembersMessageHistoryIdentifier.cold.1
- getBMSiriRemembersMessageHistoryIdentifierSymbolLoc.ptr
- getBMSiriSELFProcessedEventIdentifier.cold.1
- getBMSiriSELFProcessedEventIdentifierSymbolLoc.ptr
- getBMSiriServiceIdentifier.cold.1
- getBMSiriServiceIdentifierSymbolLoc.ptr
- hash_search_with_hash_value.cold.1
- hash_search_with_hash_value.cold.2
- hash_search_with_hash_value.cold.3
- hash_search_with_hash_value.cold.4
- hash_search_with_hash_value.cold.5
- hash_search_with_hash_value.cold.6
- perform_spin_delay.cold.1
CStrings:
+ "\"com.apple.MobileSMS\" IN $disabledApps"
+ "%{public}@ - no pruning needed for %{public}@ - trigger condition evaluated to NO"
+ "%{public}@ - not pruning user domain stream %{public}@ - this will be handled by an agent"
+ "%{public}@ encountered error pruning stream %{public}@: %@"
+ "%{public}@ pruning all streams in %{public}@ domain with policy: %{public}@"
+ "%{public}@ pruning stream: %{public}@ with policy: %{public}@"
+ "(options & BMEventSessionOptionIncludeRepeatedStartEvent) == NO"
+ "-[BMComputePublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:]"
+ "-[BMComputePublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]"
+ "-[BMComputePublisherServer subscribe:]"
+ "-[BMComputePublisherServer unsubscribeWithIdentifier:]"
+ "/System/AppleInternal/Library/Frameworks/BiomeLibraryInternal.framework/BiomeLibraryInternal"
+ "@\"<BMComputePublisherServerDelegate>\""
+ "@\"<BMComputeSourceDaemon>\""
+ "@\"<NSSecureCoding>\"40@0:8@\"NSXPCConnection\"16@\"NSXPCCoder\"24@32"
+ "@\"BMComputePublisherClient\""
+ "@\"BMComputePublisherClientDomainConfiguration\""
+ "@\"BMComputePublisherServer\""
+ "@\"BMComputePublisherStorage\""
+ "@\"BMComputeSubscription\""
+ "@\"BMXPCConnectionWrapper\""
+ "@\"BMXPCListener\""
+ "@32@0:8Q16@?24"
+ "@36@0:8@16Q24I32"
+ "@44@0:8@16Q24@32I40"
+ "@52@0:8@16Q24@32@40I48"
+ "Accepting connection from %{public}@(%d)"
+ "B24@?0@\"BMComputeSubscription\"8@\"NSDictionary\"16"
+ "B32@0:8@\"BMXPCListener\"16@\"NSXPCConnection\"24"
+ "B32@?0@\"BMComputeSubscription\"8Q16^B24"
+ "BMComputePublisher add publisher for token %@ descriptor: %s"
+ "BMComputePublisher initial barrier"
+ "BMComputePublisher remove publisher for token %@"
+ "BMComputePublisher xpc publisher error: %@ %@"
+ "BMComputePublisherClient"
+ "BMComputePublisherClient handle event for subscription with identifier %@"
+ "BMComputePublisherClient subscribe with connection name: %@, publisher stream name: %@, localPublisher: %@, subscription: %@"
+ "BMComputePublisherClient unsubscribe with connection name: %@, publisher stream name: %@, localPublisher: %@, identifier: %@"
+ "BMComputePublisherClient.m"
+ "BMComputePublisherClientDomainConfiguration"
+ "BMComputePublisherServer"
+ "BMComputePublisherServer dropping receiveInputForIdentifier: due to nil identifier"
+ "BMComputePublisherServer dropping subscribe: due to dead connection %@"
+ "BMComputePublisherServer dropping subscribe: due to nil subscription"
+ "BMComputePublisherServer dropping subscribe: invalid identifier %@"
+ "BMComputePublisherServer failed to read non-waking subscriptions on init, %@"
+ "BMComputePublisherServer.m"
+ "BMComputePublisherServerDelegate"
+ "BMComputePublisherStorage"
+ "BMComputeSourceDaemon"
+ "BMComputeSourceServerConnection dropping eventsPrunedWithStreamIdentifier due to nil stream"
+ "BMComputeSubscription"
+ "BMComputeSubscription cannot be initialized with provided token %@ and descriptor: %s"
+ "BMComputeSubscription cannot execute graph: %@"
+ "BMComputeSubscription error archiving graph while converting subscription to xpc event %@"
+ "BMComputeSubscription error archiving subscriber while converting subscription to xpc event %@"
+ "BMComputeSubscription error creating directory at DSL directory %@, %@"
+ "BMComputeSubscription error: provided identifier '%@' is invalid"
+ "BMComputeSubscription failed to get contents of sessions directory %@"
+ "BMComputeSubscription unable to locate storage, invalid identifier %@"
+ "BMComputeSubscription unable to unarchive BMDSL Subscriber for subscription: %@; error: %@"
+ "BMComputeSubscription unable to unarchive BMDSL as JSON archived object, falling back to legacy dictionary-based format. Subscription: %@; error: %@"
+ "BMComputeSubscription unable to unarchive BMDSL graph for subscription: %@, provided graph is not a dictionary and was not able to be parsed"
+ "BMComputeSubscription unable to unarchive BMDSL graph for subscription: %@; error: %@"
+ "BMComputeSubscription.m"
+ "BMConnectionProxyable"
+ "BMLibraryStreamsPruner running pruneWithInstalledApplications:installedAppExtensions:"
+ "BMStreamBuiltinPruningTrigger { id: %@, trigger: %@, predicate: %@ }"
+ "BMXPCListenerDelegate"
+ "Connection %@ failed to route request -%@"
+ "Connection missing use-case"
+ "ERROR: Unable access to AppleKeyStore"
+ "Failed to create remote object proxy"
+ "Failed to get connection from BMXPCConnectionWrapper"
+ "Failed to get or create BMXPCConnectionWrapper"
+ "Failed to route request -%@"
+ "Incoming connection from %{public}@(%d)"
+ "NSXPCConnectionDelegate"
+ "Not authorized"
+ "Refusing connection from %{public}@(%d), process not properly entitled"
+ "Rejecting eventsPrunedWithStreamIdentifier due to lacking write entitlements for stream %@"
+ "Request -%@ from %@ failed validation with error %@"
+ "System to user write, returning YES for stream: %@ using domain: %@ path: %@"
+ "T@\"<BMComputePublisherServerDelegate>\",R,W,N,V_delegate"
+ "T@\"<BMComputeSourceDaemon>\",R,W,N,V_source"
+ "T@\"BMComputePublisherClient\",&,N,V_client"
+ "T@\"BMComputePublisherClient\",&,N,V_systemStreamsPublisherClient"
+ "T@\"BMComputePublisherClient\",R,N,V_client"
+ "T@\"BMComputePublisherServer\",R,N,V_systemPublisherServer"
+ "T@\"BMComputePublisherServer\",R,N,V_userPublisherServer"
+ "T@\"BMComputePublisherStorage\",&,N,V_bookmarkStorage"
+ "T@\"BMComputePublisherStorage\",R,N"
+ "T@\"BMComputePublisherStorage\",R,N,V_systemBookmarkStorage"
+ "T@\"BMComputePublisherStorage\",R,N,V_systemStorage"
+ "T@\"BMComputePublisherStorage\",R,N,V_userBookmarkStorage"
+ "T@\"BMComputePublisherStorage\",R,N,V_userStorage"
+ "T@\"BMComputeSubscription\",&,N,V_xpcSubscription"
+ "TRUEPREDICATE"
+ "Unable to determine reply block signature for -%@"
+ "Unable to locate error parameter for reply block of -%@"
+ "Unable to locate reply block for -%{public}@, got class %{public}@"
+ "Unable to locate reply block for -%{public}@, got type %{public}s"
+ "Use case already set"
+ "Warning: %{public}@ found 0 streams configured for policy: %{public}@"
+ "Wrong domain"
+ "_acceptConnection:"
+ "_classForObjectAtArgumentIndex:"
+ "_connectionWrapper"
+ "_enumerateAllPruningTriggersForPolicy:block:"
+ "_newConnectionForDomain:"
+ "_pruneStream:policy:trigger:parameters:"
+ "_pruneStreamsWithPolicy:parameters:"
+ "_remoteObjectProxyForDomain:errorHandler:"
+ "_user"
+ "allowAppleIntelligenceReport"
+ "allowsAccessToProxyBiomeAgentEndpoint"
+ "allowsConfiguringConnection:forUseCase:inDomain:error:"
+ "allowsConnectionToComputeSourceServiceWithDomain:"
+ "app-uninstall-nightly"
+ "bm_accessControlPolicy"
+ "bm_connectionFlags"
+ "bm_process"
+ "bm_remoteUseCase"
+ "canAccessAppleKeyStore"
+ "com.apple.BMComputePublisherClient.queue"
+ "connection:handleInvocation:isReply:"
+ "connectionToComputeSourceServerInDomain:user:useCase:"
+ "connectionToMachService:endpoint:useCase:"
+ "dateByAddingTimeInterval:"
+ "deleted"
+ "disabledApps"
+ "endpoint"
+ "evaluateWithObject:substitutionVariables:"
+ "exportedInterface"
+ "getArgument:atIndex:"
+ "getArgumentTypeAtIndex:"
+ "initWithIdentifier:triggerCondition:pruningPredicate:"
+ "initWithMachServiceName:queue:"
+ "initWithQueue:domain:source:"
+ "initWithQueue:domain:source:listener:"
+ "initWithStream:permission:config:includeTombstones:eventDataClass:useCase:"
+ "initWithStreamIdentifier:domain:listenerEndpoint:storage:user:"
+ "initWithStreamIdentifier:domain:useCase:user:"
+ "initWithStreamIdentifier:domain:user:"
+ "installed"
+ "intentGroupIdentifiers"
+ "intentIdentifiers"
+ "invocationWithMethodSignature:"
+ "invoke"
+ "invokeWithTarget:"
+ "isValid"
+ "methodSignature"
+ "numberOfArguments"
+ "predicateWithFormat:argumentArray:"
+ "predicateWithValue:"
+ "pruneWithDeletedContactIdentifiers"
+ "replaceFileAtPath:withData:protection:flags:error:"
+ "replacementObjectForXPCConnection:encoder:object:"
+ "replyBlockSignatureForSelector:"
+ "replyToInvocation:withError:"
+ "requestEndpointForProxyingConnectionsWithReply:"
+ "retainArguments"
+ "selector"
+ "setArgument:atIndex:"
+ "setBm_accessControlPolicy:"
+ "setByAddingObjectsFromArray:"
+ "setTarget:"
+ "signatureWithObjCTypes:"
+ "uninstalled"
+ "unknown service domain when initializing BMComputePublisherClient, %@"
+ "v24@0:8@\"BMComputeSubscription\"16"
+ "v24@0:8@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">16"
+ "v24@?0@\"BMStreamBase\"8@\"BMStreamBuiltinPruningTrigger\"16"
+ "v32@0:8@\"BMComputePublisherServer\"16@\"BMComputeSubscription\"24"
+ "v32@?0@\"BMComputeSubscription\"8@\"NSString\"16@\"BMStoreEvent\"24"
+ "v36@0:8@\"NSXPCConnection\"16@\"NSInvocation\"24B32"
+ "v36@0:8@16@24B32"
+ "v48@0:8@16@24@32@40"
+ "validateConnection:error:"
- "#?"
- "%@ - _pruneStreamWithIdentifier could not find stream for identifier: %@, err: %@"
- "%@ - not pruning stream %@ as domain is %@ - this will be handled by the other biome primary daemon process"
- "%@ - unhandled class in bundleIdentifiersFromStoreEvent: %@"
- "%@ - unhandled class in intentGroupIdentifierFromStoreEvent: %@"
- "%@ - unhandled class in intentIdentifierFromStoreEvent: %@"
- "%@ - unhandled class in isDonatedBySiriFromStoreEvent: %@"
- "%@ could not find identifier from event: %@"
- "(key: String, value: SQLRawDataType)"
- "(options & BMIncludeRepeatedStartEvent) == NO"
- "(unknown)"
- "-[BMComputeXPCPublisherClient receiveInputForIdentifier:streamIdentifier:storeEvent:]"
- "-[BMComputeXPCPublisherServer receiveInputForSubscription:streamIdentifier:storeEvent:]"
- "-[BMComputeXPCPublisherServer subscribe:]"
- "-[BMComputeXPCPublisherServer unsubscribeWithIdentifier:]"
- "<BMComputeSource server: %@ clientProcess: %@ >"
- "<source: %@ listener: %@ queue: %@ connectionCount: %lu>"
- "?#"
- "?&"
- "?-"
- "?@"
- "?|"
- "?~"
- "@\"<BMComputeSource>\""
- "@\"<BMComputeXPCPublisherServerDelegate>\""
- "@\"BMAccessControlPolicy\""
- "@\"BMComputeXPCPublisherClient\""
- "@\"BMComputeXPCPublisherClientDomainConfiguration\""
- "@\"BMComputeXPCPublisherServer\""
- "@\"BMComputeXPCPublisherStorage\""
- "@\"BMComputeXPCSubscription\""
- "@\"BMProcess\""
- "@\"NSDictionary\"8@?0"
- "@\"NSMapTable\""
- "B24@?0@\"BMComputeXPCSubscription\"8@\"NSDictionary\"16"
- "B32@?0@\"BMComputeXPCSubscription\"8Q16^B24"
- "B40@0:8@16@24@32"
- "BMAppInFocus"
- "BMAppInFocusIdentifier"
- "BMAppIntent"
- "BMAppIntentIdentifier"
- "BMAppLocationActivity"
- "BMAppLocationActivityIdentifier"
- "BMAutonamingMessagesInferencesIdentifier"
- "BMAutonamingMessagesMessageIdsIdentifier"
- "BMComputePublisherStreamNameForDomain could not determine publisher server mach service name for BMServiceDomainCount"
- "BMComputePublisherStreamNameForDomain could not determine publisher stream name for BMServiceDomainCount"
- "BMComputeSource"
- "BMComputeSourceClient establishing new XPC connection from source with stream %@, listenerEndpoint: %@, machServiceName: %@"
- "BMComputeSourceClient for stream %@ XPC error in eventsPrunedForAccount:remoteName:reason:%@"
- "BMComputeSourceClient for stream %@ connection interrupted"
- "BMComputeSourceClient for stream %@ connection invalidated because %{public}@"
- "BMComputeSourceMachServiceNameForDomain could not determine service name for BMServiceDomainCount"
- "BMComputeSourceServer accepting connection from %{public}@(%d)"
- "BMComputeSourceServer connection %@ interrupted"
- "BMComputeSourceServer connection %@ invalidated because %{public}@"
- "BMComputeSourceServer received new connection request from %@(%d)"
- "BMComputeSourceServer refusing connection from %{public}@(%d), process lacks write entitlements"
- "BMComputeSourceServerConnection"
- "BMComputeSubscriptionMarkerManager received BMServiceDomainCount while fetching subscriptionMarkerStorage"
- "BMComputeXPCPublisher add publisher for token %@ descriptor: %s"
- "BMComputeXPCPublisher initial barrier"
- "BMComputeXPCPublisher remove publisher for token %@"
- "BMComputeXPCPublisher xpc publisher error: %@ %@"
- "BMComputeXPCPublisherClient"
- "BMComputeXPCPublisherClient handle event for subscription with identifier %@"
- "BMComputeXPCPublisherClient subscribe with connection name: %@, publisher stream name: %@, localPublisher: %@, subscription: %@"
- "BMComputeXPCPublisherClient unsubscribe with connection name: %@, publisher stream name: %@, localPublisher: %@, identifier: %@"
- "BMComputeXPCPublisherClient.m"
- "BMComputeXPCPublisherClientDomainConfiguration"
- "BMComputeXPCPublisherServer"
- "BMComputeXPCPublisherServer dropping receiveInputForIdentifier: due to nil identifier"
- "BMComputeXPCPublisherServer dropping subscribe: due to dead connection %@"
- "BMComputeXPCPublisherServer dropping subscribe: due to nil subscription"
- "BMComputeXPCPublisherServer dropping subscribe: invalid identifier %@"
- "BMComputeXPCPublisherServer failed to read non-waking subscriptions on init, %@"
- "BMComputeXPCPublisherServer received BMServiceDomainCount while fetching storage"
- "BMComputeXPCPublisherServer.m"
- "BMComputeXPCPublisherServerDelegate"
- "BMComputeXPCPublisherStorage"
- "BMComputeXPCSubscription"
- "BMComputeXPCSubscription cannot be initialized with provided token %@ and descriptor: %s"
- "BMComputeXPCSubscription cannot execute graph: %@"
- "BMComputeXPCSubscription error archiving graph while converting subscription to xpc event %@"
- "BMComputeXPCSubscription error archiving subscriber while converting subscription to xpc event %@"
- "BMComputeXPCSubscription error creating directory at DSL directory %@, %@"
- "BMComputeXPCSubscription error: provided identifier '%@' is invalid"
- "BMComputeXPCSubscription failed to get contents of sessions directory %@"
- "BMComputeXPCSubscription unable to locate storage, invalid identifier %@"
- "BMComputeXPCSubscription unable to unarchive BMDSL Subscriber for subscription: %@; error: %@"
- "BMComputeXPCSubscription unable to unarchive BMDSL as JSON archived object, falling back to legacy dictionary-based format. Subscription: %@; error: %@"
- "BMComputeXPCSubscription unable to unarchive BMDSL graph for subscription: %@, provided graph is not a dictionary and was not able to be parsed"
- "BMComputeXPCSubscription unable to unarchive BMDSL graph for subscription: %@; error: %@"
- "BMComputeXPCSubscription.m"
- "BMDictationUserEditIdentifier"
- "BMFrontBoardDisplayElement"
- "BMFrontBoardDisplayElementIdentifier"
- "BMIntelligenceEngineInteraction"
- "BMIntelligenceEngineInteractionDonationIdentifier"
- "BMKeyboardTokenFrequencyIdentifier"
- "BMLibraryStreamsPruner pruning stream: %@ with policy: %@"
- "BMLibraryStreamsPruner running pruneLearnFromThisAppDisabledForMessages"
- "BMLibraryStreamsPruner running pruneWithInstalledApplications:installedAppExtensions"
- "BMLibraryStreamsPruner.m"
- "BMLocationSemanticIdentifier"
- "BMMediaNowPlaying"
- "BMMediaNowPlayingIdentifier"
- "BMProactiveHarvestingSiriQueryIdentifier"
- "BMScreenTimeAppUsage"
- "BMScreenTimeAppUsageIdentifier"
- "BMSiriAppSelectionMusicIdentifier"
- "BMSiriAssistantSuggestions"
- "BMSiriAudioHistory"
- "BMSiriCallHistory"
- "BMSiriDictationIdentifier"
- "BMSiriExecutionIdentifier"
- "BMSiriFeedbackLearningUserInteractionsIdentifier"
- "BMSiriInteractionHistory"
- "BMSiriMessageHistory"
- "BMSiriPostSiriEngagementIdentifier"
- "BMSiriPrivateLearningSELFEventIdentifier"
- "BMSiriRemembersAssistantSuggestionsIdentifier"
- "BMSiriRemembersAudioHistoryIdentifier"
- "BMSiriRemembersCallHistoryIdentifier"
- "BMSiriRemembersIntentIdentifier"
- "BMSiriRemembersInteractionHistoryIdentifier"
- "BMSiriRemembersMessageHistoryIdentifier"
- "BMSiriSELFProcessedEventIdentifier"
- "BMSiriServiceIdentifier"
- "BMStreamBuiltinPruningTrigger { id: %@, platforms: {%@}, trigger: %@, predicate: %@ }"
- "Can't construct Array with count < 0"
- "Class getBMAppInFocusClass(void)_block_invoke"
- "Class getBMAppIntentClass(void)_block_invoke"
- "Class getBMAppLocationActivityClass(void)_block_invoke"
- "Class getBMFrontBoardDisplayElementClass(void)_block_invoke"
- "Class getBMIntelligenceEngineInteractionClass(void)_block_invoke"
- "Class getBMMediaNowPlayingClass(void)_block_invoke"
- "Class getBMScreenTimeAppUsageClass(void)_block_invoke"
- "Class getBMSiriAssistantSuggestionsClass(void)_block_invoke"
- "Class getBMSiriAudioHistoryClass(void)_block_invoke"
- "Class getBMSiriCallHistoryClass(void)_block_invoke"
- "Class getBMSiriInteractionHistoryClass(void)_block_invoke"
- "Class getBMSiriMessageHistoryClass(void)_block_invoke"
- "Division by zero"
- "Division results in an overflow"
- "Down-casted Array element failed to match the target type\nExpected "
- "FunctionCall5Coll"
- "Insufficient space allocated to copy string contents"
- "NSString *getBMAppInFocusIdentifier(void)"
- "NSString *getBMAppIntentIdentifier(void)"
- "NSString *getBMAppLocationActivityIdentifier(void)"
- "NSString *getBMAutonamingMessagesInferencesIdentifier(void)"
- "NSString *getBMAutonamingMessagesMessageIdsIdentifier(void)"
- "NSString *getBMDictationUserEditIdentifier(void)"
- "NSString *getBMFrontBoardDisplayElementIdentifier(void)"
- "NSString *getBMIntelligenceEngineInteractionDonationIdentifier(void)"
- "NSString *getBMKeyboardTokenFrequencyIdentifier(void)"
- "NSString *getBMLocationSemanticIdentifier(void)"
- "NSString *getBMMediaNowPlayingIdentifier(void)"
- "NSString *getBMProactiveHarvestingSiriQueryIdentifier(void)"
- "NSString *getBMScreenTimeAppUsageIdentifier(void)"
- "NSString *getBMSiriAppSelectionMusicIdentifier(void)"
- "NSString *getBMSiriDictationIdentifier(void)"
- "NSString *getBMSiriExecutionIdentifier(void)"
- "NSString *getBMSiriFeedbackLearningUserInteractionsIdentifier(void)"
- "NSString *getBMSiriPostSiriEngagementIdentifier(void)"
- "NSString *getBMSiriPrivateLearningSELFEventIdentifier(void)"
- "NSString *getBMSiriRemembersAssistantSuggestionsIdentifier(void)"
- "NSString *getBMSiriRemembersAudioHistoryIdentifier(void)"
- "NSString *getBMSiriRemembersCallHistoryIdentifier(void)"
- "NSString *getBMSiriRemembersIntentIdentifier(void)"
- "NSString *getBMSiriRemembersInteractionHistoryIdentifier(void)"
- "NSString *getBMSiriRemembersMessageHistoryIdentifier(void)"
- "NSString *getBMSiriSELFProcessedEventIdentifier(void)"
- "NSString *getBMSiriServiceIdentifier(void)"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"<BMComputeSource>\",R,W,N,V_source"
- "T@\"<BMComputeXPCPublisherServerDelegate>\",R,W,N,V_delegate"
- "T@\"BMAccessControlPolicy\",R,N,V_accessControlPolicy"
- "T@\"BMComputeSourceServer\",R,W,N,V_server"
- "T@\"BMComputeXPCPublisherClient\",&,N,V_client"
- "T@\"BMComputeXPCPublisherClient\",&,N,V_systemStreamsPublisherClient"
- "T@\"BMComputeXPCPublisherClient\",R,N,V_client"
- "T@\"BMComputeXPCPublisherServer\",R,N,V_systemPublisherServer"
- "T@\"BMComputeXPCPublisherServer\",R,N,V_userPublisherServer"
- "T@\"BMComputeXPCPublisherStorage\",&,N,V_bookmarkStorage"
- "T@\"BMComputeXPCPublisherStorage\",R,N"
- "T@\"BMComputeXPCPublisherStorage\",R,N,V_storage"
- "T@\"BMComputeXPCPublisherStorage\",R,N,V_systemBookmarkStorage"
- "T@\"BMComputeXPCPublisherStorage\",R,N,V_systemStorage"
- "T@\"BMComputeXPCPublisherStorage\",R,N,V_userBookmarkStorage"
- "T@\"BMComputeXPCPublisherStorage\",R,N,V_userStorage"
- "T@\"BMComputeXPCSubscription\",&,N,V_xpcSubscription"
- "T@\"BMProcess\",R,N,V_clientProcess"
- "T@\"NSMapTable\",R,N,V_connections"
- "TQ,R,N,V_platforms"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "^?"
- "_accessControlPolicy"
- "_clientProcess"
- "_connections"
- "_platforms"
- "_pruneStream:policy:shouldPruneBlock:"
- "_pruneStreamWithIdentifier:policy:shouldPruneBlock:"
- "_server"
- "accessControlPolicy"
- "allowsConnectionToComputeSourceService"
- "appIntentInteractionIdentifier"
- "bundleIdentifiersFromStoreEvent:"
- "candidateId"
- "candidateIds"
- "candidateInteractions"
- "cannot insert into frozen hashtable \"%s\""
- "clientProcess"
- "com.apple.BMComputeXPCPublisherClient.queue"
- "com.apple.MobileSMS"
- "com.apple.biome.compute.publisher.service"
- "com.apple.biome.compute.publisher.service.user"
- "com.apple.biome.compute.source"
- "com.apple.biome.compute.source.user"
- "com.apple.biome.sql.query"
- "com.apple.biome.sql.query.deduplicated"
- "connections"
- "contactIdentifiersFromStoreEvent:"
- "element_alloc"
- "function %u returned NULL"
- "get_hash_entry"
- "hash table \"%s\" corrupted"
- "hash_corrupted"
- "hash_search_with_hash_value"
- "initWithBool:"
- "initWithIdentifier:platforms:triggerCondition:pruningPredicate:"
- "initWithQueue:machServiceName:source:"
- "initWithQueue:source:listener:"
- "initWithServer:clientProcess:"
- "initWithStream:permission:config:"
- "initWithStreamIdentifier:domain:"
- "initWithStreamIdentifier:domain:useCase:"
- "initWithStreamIdentifier:machServiceName:listenerEndpoint:storage:"
- "intentGroupIdentifierFromStoreEvent:"
- "intentIdentifierFromStoreEvent:"
- "intersectsSet:"
- "invalid Collection: less than 'count' elements in collection"
- "isDonatedBySiriFromStoreEvent:"
- "learn-from-this-app-messages"
- "num_results"
- "out of shared memory"
- "platforms"
- "processType"
- "pruneLearnFromThisAppDisabledForMessages"
- "rc"
- "replaceFileAtPath:withData:protection:error:"
- "s_lock_stuck"
- "setUseSynchronousXPCMessageSending:"
- "shouldPruneStoreEvent:forDeletedContactIdentifiers:"
- "shouldPruneStoreEvent:forDeletedGroupIdentifiers:bundleId:"
- "shouldPruneStoreEvent:forDeletedIntentIdentifiers:bundleId:"
- "shouldPruneStoreEvent:forInstalledApplications:installedAppExtensions:"
- "shouldPruneStoreEvent:forLearnFromThisAppDisabledBundleIdentifiers:"
- "shouldPruneStoreEvent:forUninstalledBundleId:"
- "shouldPruneStoreEventForSiriAndDictationHistoryDeletion:"
- "shouldPruneStoreEventForSiriDisabled:"
- "src/postgres/src_backend_storage_lmgr_s_lock.c"
- "src/postgres/src_backend_utils_fmgr_fmgr.c"
- "src/postgres/src_backend_utils_hash_dynahash.c"
- "strongToStrongObjectsMapTable"
- "stuck spinlock detected at %s, %s:%d"
- "systemComputePublisherServiceName"
- "systemComputeSourceServiceName"
- "tupleInteraction"
- "unknown service domain when initializing BMComputeXPCPublisherClient, %@"
- "unrecognized hash action code: %d"
- "userComputePublisherServiceName"
- "userComputeSourceServiceName"
- "v16@?0@\"NSString\"8"
- "v24@0:8@\"BMComputeXPCSubscription\"16"
- "v32@0:8@\"BMComputeXPCPublisherServer\"16@\"BMComputeXPCSubscription\"24"
- "v32@?0@\"BMComputeXPCSubscription\"8@\"NSString\"16@\"BMStoreEvent\"24"
- "v40@0:8@16@24@?32"

```

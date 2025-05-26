## Coordination

> `/System/Library/PrivateFrameworks/Coordination.framework/Coordination`

```diff

-196.40.16.0.0
-  __TEXT.__text: 0x2cb64
+196.50.2.0.0
+  __TEXT.__text: 0x3403c
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x233c
+  __TEXT.__objc_methlist: 0x265c
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x92c
-  __TEXT.__cstring: 0x1271
-  __TEXT.__oslogstring: 0x28f7
-  __TEXT.__unwind_info: 0xcd4
-  __TEXT.__objc_classname: 0x8c9
-  __TEXT.__objc_methname: 0x5342
-  __TEXT.__objc_methtype: 0xf99
-  __TEXT.__objc_stubs: 0x3c40
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xfb8
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __TEXT.__gcc_except_tab: 0xab8
+  __TEXT.__cstring: 0x13c4
+  __TEXT.__oslogstring: 0x2c20
+  __TEXT.__unwind_info: 0xec0
+  __TEXT.__objc_classname: 0x919
+  __TEXT.__objc_methname: 0x5cee
+  __TEXT.__objc_methtype: 0x10ca
+  __TEXT.__objc_stubs: 0x42e0
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x1218
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4270
-  __DATA_CONST.__objc_selrefs: 0x1290
+  __DATA_CONST.__objc_const: 0x45e0
+  __DATA_CONST.__objc_selrefs: 0x1468
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_classrefs: 0x2b0
-  __DATA_CONST.__objc_superrefs: 0x160
-  __AUTH_CONST.__cfstring: 0x14a0
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__objc_const: 0x15e0
+  __DATA_CONST.__objc_classrefs: 0x2c0
+  __DATA_CONST.__objc_superrefs: 0x168
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__objc_const: 0x1628
   __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x2b4
-  __DATA.__data: 0x900
+  __AUTH.__objc_data: 0xf50
+  __DATA.__objc_ivar: 0x2e0
+  __DATA.__data: 0x960
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/MediaGroups.framework/MediaGroups
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
+  - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1117
-  Symbols:   3881
-  CStrings:  1549
+  Functions: 1257
+  Symbols:   4272
+  CStrings:  1665
 
Symbols:
+ +[COClusterMemberRoleSnapshot snapshotWithParticipantRoleForMember:]
+ +[COClusterRole roleForParticipant]
+ -[COClusterMember initWithHomeKitIdentifier:]
+ -[COMessageChannel activated]
+ -[COMessageChannel baseRequestID]
+ -[COMessageChannel lock]
+ -[COMessageChannel setActivated:]
+ -[COMessageChannel setBaseRequestID:]
+ -[COMessageChannel setLock:]
+ -[COMessageChannel setWorkQueue:]
+ -[COMessageChannel workQueue]
+ -[COMessageChannelRapportTransport .cxx_destruct]
+ -[COMessageChannelRapportTransport _onqueue_activeMemberWithIDSIdentifier:]
+ -[COMessageChannelRapportTransport _onqueue_devicePresentInGroup:]
+ -[COMessageChannelRapportTransport _onqueue_handleDeviceFound:]
+ -[COMessageChannelRapportTransport _onqueue_handleDeviceLost:]
+ -[COMessageChannelRapportTransport _onqueue_handleIncomingRequest:options:responseHandler:]
+ -[COMessageChannelRapportTransport _onqueue_handleIncomingRequest:options:responseHandler:].cold.1
+ -[COMessageChannelRapportTransport _onqueue_handleIncomingRequest:options:responseHandler:].cold.2
+ -[COMessageChannelRapportTransport _onqueue_memberFromRPCompanionLinkDevice:]
+ -[COMessageChannelRapportTransport _payloadClassFromType:]
+ -[COMessageChannelRapportTransport _payloadTypeFromClass:]
+ -[COMessageChannelRapportTransport _serializeDataForResponse:]
+ -[COMessageChannelRapportTransport _serializedDataForRequest:]
+ -[COMessageChannelRapportTransport _withLock:]
+ -[COMessageChannelRapportTransport activateWithCompletion:]
+ -[COMessageChannelRapportTransport activateWithCompletion:].cold.1
+ -[COMessageChannelRapportTransport activeMemberDevices]
+ -[COMessageChannelRapportTransport activeMembers]
+ -[COMessageChannelRapportTransport addHomeKitGroupIdentifiers:]
+ -[COMessageChannelRapportTransport companionLinkClient]
+ -[COMessageChannelRapportTransport delegate]
+ -[COMessageChannelRapportTransport groupHKIdentifiers]
+ -[COMessageChannelRapportTransport identifier]
+ -[COMessageChannelRapportTransport initWithIdentifier:delegate:companionLink:dispatchQueue:]
+ -[COMessageChannelRapportTransport initWithIdentifier:delegate:dispatchQueue:]
+ -[COMessageChannelRapportTransport queue]
+ -[COMessageChannelRapportTransport removeHomeKitGroupIdentifiers:]
+ -[COMessageChannelRapportTransport requestIdentifier]
+ -[COMessageChannelRapportTransport sendRequest:to:withCompletionHandler:]
+ -[COMessageChannelRapportTransport setActiveMemberDevices:]
+ -[COMessageChannelRapportTransport setCompanionLinkClient:]
+ -[COMessageChannelRapportTransport setIdentifier:]
+ -[COMessageChannelRapportTransport setQueue:]
+ -[_COMessageChannel .cxx_destruct]
+ -[_COMessageChannel _onqueue_deliverDidEndDelegateForSession:notice:initiator:error:]
+ -[_COMessageChannel _onqueue_deliverDidFailToStartSessionWithMember:consumer:error:]
+ -[_COMessageChannel _onqueue_deliverDidFailToStartSessionWithMember:producer:error:]
+ -[_COMessageChannel _onqueue_deliverSuccessfullyStartedSession:withMember:consumer:]
+ -[_COMessageChannel _onqueue_deliverSuccessfullyStartedSession:withResponse:withMember:producer:]
+ -[_COMessageChannel _onqueue_handleCapableCommand:fromMember:callback:]
+ -[_COMessageChannel _onqueue_handleStartCommand:withMember:callback:]
+ -[_COMessageChannel _onqueue_handleStartCommand:withMember:callback:].cold.1
+ -[_COMessageChannel _onqueue_handleStopCommand:fromMember:callback:]
+ -[_COMessageChannel _onqueue_sendRequest:members:withCompletionHandler:]
+ -[_COMessageChannel _onqueue_startSessionWithProducer:member:]
+ -[_COMessageChannel _onqueue_startSessionWithProducer:member:].cold.1
+ -[_COMessageChannel _onqueue_startSessionWithProducer:member:request:]
+ -[_COMessageChannel _payloadClassFromType:]
+ -[_COMessageChannel _payloadTypeFromClass:]
+ -[_COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]
+ -[_COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]
+ -[_COMessageChannel didFindMember:]
+ -[_COMessageChannel didLoseMember:]
+ -[_COMessageChannel didReceiveRequest:from:withCompletionHandler:]
+ -[_COMessageChannel groupedHomeKitIdentifiers]
+ -[_COMessageChannel rapportTransport]
+ -[_COMessageChannel setRapportTransport:]
+ GCC_except_table179
+ GCC_except_table18
+ GCC_except_table42
+ GCC_except_table65
+ _OBJC_CLASS_$_COMessageChannelRapportTransport
+ _OBJC_CLASS_$_RPCompanionLinkClient
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._activeMemberDevices
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._activeMembers
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._companionLinkClient
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._delegate
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._groupHKIdentifiers
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._identifier
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._lock
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._queue
+ _OBJC_IVAR_$_COMessageChannelRapportTransport._requestIdentifier
+ _OBJC_IVAR_$__COMessageChannel._activated
+ _OBJC_IVAR_$__COMessageChannel._rapportTransport
+ _OBJC_METACLASS_$_COMessageChannelRapportTransport
+ _RPOptionPeerHomeKitUserIdentifier
+ _RPOptionSenderIDSDeviceID
+ _RPOptionXID
+ __OBJC_$_CLASS_METHODS_NSString(SessionProducerConsumer|SessionProducerConsumer)
+ __OBJC_$_INSTANCE_METHODS_COMessageChannelRapportTransport
+ __OBJC_$_INSTANCE_METHODS_NSString(SessionProducerConsumer|SessionProducerConsumer)
+ __OBJC_$_INSTANCE_VARIABLES_COMessageChannelRapportTransport
+ __OBJC_$_INSTANCE_VARIABLES__COMessageChannel
+ __OBJC_$_PROP_LIST_COMessageChannelRapportTransport
+ __OBJC_$_PROP_LIST__COMessageChannel
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_COMessageChannelRapportTransportDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_COMessageChannelRapportTransportDelegate
+ __OBJC_$_PROTOCOL_REFS_COMessageChannelRapportTransportDelegate
+ __OBJC_CLASS_PROTOCOLS_$__COMessageChannel
+ __OBJC_CLASS_RO_$_COMessageChannelRapportTransport
+ __OBJC_LABEL_PROTOCOL_$_COMessageChannelRapportTransportDelegate
+ __OBJC_METACLASS_RO_$_COMessageChannelRapportTransport
+ __OBJC_PROTOCOL_$_COMessageChannelRapportTransportDelegate
+ ___35-[_COMessageChannel didFindMember:]_block_invoke
+ ___35-[_COMessageChannel didFindMember:]_block_invoke_2
+ ___35-[_COMessageChannel didLoseMember:]_block_invoke
+ ___44-[_COMessageChannel activateWithCompletion:]_block_invoke
+ ___44-[_COMessageChannel activateWithCompletion:]_block_invoke_2
+ ___44-[_COMessageChannel activateWithCompletion:]_block_invoke_2.cold.1
+ ___46-[_COMessageChannel groupedHomeKitIdentifiers]_block_invoke
+ ___47-[_COMessageChannel registerMemberLostHandler:]_block_invoke
+ ___47-[_COMessageChannel registerMemberLostHandler:]_block_invoke.cold.1
+ ___48-[_COMessageChannel registerMemberFoundHandler:]_block_invoke
+ ___48-[_COMessageChannel registerMemberFoundHandler:]_block_invoke.cold.1
+ ___50-[_COMessageChannel addGroupedHomeKitIdentifiers:]_block_invoke
+ ___53-[_COMessageChannel registerHandler:forRequestClass:]_block_invoke
+ ___53-[_COMessageChannel registerHandler:forRequestClass:]_block_invoke.cold.1
+ ___53-[_COMessageChannel removeGroupedHomeKitIdentifiers:]_block_invoke
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke_2
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke_3
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke_4
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke_5
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke_6
+ ___59-[COMessageChannelRapportTransport activateWithCompletion:]_block_invoke_7
+ ___62-[_COMessageChannel _onqueue_startSessionWithProducer:member:]_block_invoke
+ ___62-[_COMessageChannel _onqueue_startSessionWithProducer:member:]_block_invoke.33
+ ___62-[_COMessageChannel _onqueue_startSessionWithProducer:member:]_block_invoke_2
+ ___63-[COMessageChannelRapportTransport addHomeKitGroupIdentifiers:]_block_invoke
+ ___63-[_COMessageChannel sendRequest:members:withCompletionHandler:]_block_invoke
+ ___66-[COMessageChannelRapportTransport _onqueue_devicePresentInGroup:]_block_invoke
+ ___66-[COMessageChannelRapportTransport removeHomeKitGroupIdentifiers:]_block_invoke
+ ___66-[_COMessageChannel didReceiveRequest:from:withCompletionHandler:]_block_invoke
+ ___66-[_COMessageChannel didReceiveRequest:from:withCompletionHandler:]_block_invoke_2
+ ___69-[_COMessageChannel _onqueue_handleStartCommand:withMember:callback:]_block_invoke
+ ___69-[_COMessageChannel _onqueue_handleStartCommand:withMember:callback:]_block_invoke_2
+ ___69-[_COMessageChannel _onqueue_handleStartCommand:withMember:callback:]_block_invoke_3
+ ___70-[_COMessageChannel _onqueue_startSessionWithProducer:member:request:]_block_invoke
+ ___70-[_COMessageChannel _onqueue_startSessionWithProducer:member:request:]_block_invoke.40
+ ___70-[_COMessageChannel _onqueue_startSessionWithProducer:member:request:]_block_invoke.cold.1
+ ___70-[_COMessageChannel _onqueue_startSessionWithProducer:member:request:]_block_invoke.cold.2
+ ___72-[_COMessageChannel _onqueue_sendRequest:members:withCompletionHandler:]_block_invoke
+ ___73-[COMessageChannelRapportTransport sendRequest:to:withCompletionHandler:]_block_invoke
+ ___75-[COMessageChannelRapportTransport _onqueue_activeMemberWithIDSIdentifier:]_block_invoke
+ ___75-[_COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke
+ ___75-[_COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke_2
+ ___75-[_COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke_3
+ ___75-[_COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke_4
+ ___75-[_COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke_4.cold.1
+ ___75-[_COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]_block_invoke
+ ___75-[_COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]_block_invoke_2
+ ___75-[_COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]_block_invoke_3
+ ___75-[_COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]_block_invoke_3.cold.1
+ ___83-[_COMessageChannel broadcastRequest:recipientsCallback:responseCompletionHandler:]_block_invoke
+ ___83-[_COMessageChannel broadcastRequest:recipientsCallback:responseCompletionHandler:]_block_invoke_2
+ ___84-[_COMessageChannel _onqueue_deliverDidFailToStartSessionWithMember:consumer:error:]_block_invoke
+ ___84-[_COMessageChannel _onqueue_deliverDidFailToStartSessionWithMember:producer:error:]_block_invoke
+ ___84-[_COMessageChannel _onqueue_deliverSuccessfullyStartedSession:withMember:consumer:]_block_invoke
+ ___85-[_COMessageChannel _onqueue_deliverDidEndDelegateForSession:notice:initiator:error:]_block_invoke
+ ___85-[_COMessageChannel _onqueue_deliverDidEndDelegateForSession:notice:initiator:error:]_block_invoke_2
+ ___91-[COMessageChannelRapportTransport _onqueue_handleIncomingRequest:options:responseHandler:]_block_invoke
+ ___97-[_COMessageChannel _onqueue_deliverSuccessfullyStartedSession:withResponse:withMember:producer:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32w_e31_v16?0"RPCompanionLinkDevice"8lw32l8
+ ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw32l8
+ ___block_descriptor_48_e8_32bs40w_e46_v24?0"COMessageChannelResponse"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e46_v24?0"COMessageChannelResponse"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e46_v24?0"COMessageChannelResponse"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e55_v32?0"COClusterMember"8"RPCompanionLinkDevice"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e51_v32?0"NSString"8"COMessageSessionProducer"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8u48l8
+ ___block_descriptor_56_e8_32s40s48bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s40l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _objc_msgSend$_onqueue_activeMemberWithIDSIdentifier:
+ _objc_msgSend$_onqueue_deliverDidEndDelegateForSession:notice:initiator:error:
+ _objc_msgSend$_onqueue_deliverDidFailToStartSessionWithMember:consumer:error:
+ _objc_msgSend$_onqueue_deliverDidFailToStartSessionWithMember:producer:error:
+ _objc_msgSend$_onqueue_deliverSuccessfullyStartedSession:withMember:consumer:
+ _objc_msgSend$_onqueue_deliverSuccessfullyStartedSession:withResponse:withMember:producer:
+ _objc_msgSend$_onqueue_devicePresentInGroup:
+ _objc_msgSend$_onqueue_handleCapableCommand:fromMember:callback:
+ _objc_msgSend$_onqueue_handleDeviceFound:
+ _objc_msgSend$_onqueue_handleDeviceLost:
+ _objc_msgSend$_onqueue_handleIncomingRequest:options:responseHandler:
+ _objc_msgSend$_onqueue_handleStartCommand:withMember:callback:
+ _objc_msgSend$_onqueue_handleStopCommand:fromMember:callback:
+ _objc_msgSend$_onqueue_memberFromRPCompanionLinkDevice:
+ _objc_msgSend$_onqueue_sendRequest:members:withCompletionHandler:
+ _objc_msgSend$_onqueue_startSessionWithProducer:member:
+ _objc_msgSend$_onqueue_startSessionWithProducer:member:request:
+ _objc_msgSend$_serializeDataForResponse:
+ _objc_msgSend$_serializedDataForRequest:
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$activeDevices
+ _objc_msgSend$activeMemberDevices
+ _objc_msgSend$activeMembers
+ _objc_msgSend$addHomeKitGroupIdentifiers:
+ _objc_msgSend$companionLinkClient
+ _objc_msgSend$didFindMember:
+ _objc_msgSend$didLoseMember:
+ _objc_msgSend$didReceiveRequest:from:withCompletionHandler:
+ _objc_msgSend$effectiveIdentifier
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$foundHandler
+ _objc_msgSend$groupHKIdentifiers
+ _objc_msgSend$homeKitIdentifier
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$initWithIdentifier:delegate:companionLink:dispatchQueue:
+ _objc_msgSend$initWithIdentifier:delegate:dispatchQueue:
+ _objc_msgSend$lostHandler
+ _objc_msgSend$rapportTransport
+ _objc_msgSend$registerRequestID:options:handler:
+ _objc_msgSend$removeHomeKitGroupIdentifiers:
+ _objc_msgSend$requestIdentifier
+ _objc_msgSend$roleForParticipant
+ _objc_msgSend$sendRequest:to:withCompletionHandler:
+ _objc_msgSend$sendRequestID:request:destinationID:options:responseHandler:
+ _objc_msgSend$setControlFlags:
+ _objc_msgSend$setDeviceFoundHandler:
+ _objc_msgSend$setDeviceLostHandler:
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setFoundHandler:
+ _objc_msgSend$setLostHandler:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$snapshotWithParticipantRoleForMember:
+ _objc_msgSend$workQueue
- GCC_except_table171
- __OBJC_$_CLASS_METHODS_NSString(SessionProducerConsumer)
- __OBJC_$_INSTANCE_METHODS_NSString(SessionProducerConsumer)
CStrings:
+ "#>"
+ "%@ Consumer successfully created a session %@"
+ "%@-messageChannel-request"
+ "%p Going to register handler for %@"
+ "%p Member found handler cannot be registered after activation"
+ "%p Member lost handler cannot be registered after activation"
+ "%p channel activation complete with error %@"
+ "%p device found %@"
+ "%p device lost %@"
+ "%p did not find an active member for IDS=%{public}@ so creating one on demand"
+ "%p failed to encode incoming request %{public}@ XID=0x%llX. error = %{public}@"
+ "%p found device is in our group %@"
+ "%p incoming request %{public}@ does not have an HK identifier field"
+ "%p incoming request %{public}@ does not have an IDS identifier field"
+ "%p incoming request from IDS=%{public}@. XID = 0x%llX"
+ "%p lost device is in our group %@"
+ "%p received callback for request %@. XID = 0x%llX. Error = %{public}@"
+ "%p sending message %@ to member %@"
+ "'"
+ "1`"
+ "@\"<COMessageChannelRapportTransportDelegate>\""
+ "@\"COMessageChannelRapportTransport\""
+ "@\"RPCompanionLinkClient\""
+ "COMessageChannelRapportTransport"
+ "COMessageChannelRapportTransportDelegate"
+ "RapportTransport"
+ "T@\"<COMessageChannelRapportTransportDelegate>\",R,W,N,V_delegate"
+ "T@\"COMessageChannelRapportTransport\",&,N,V_rapportTransport"
+ "T@\"NSArray\",R,&,N,V_activeMembers"
+ "T@\"NSMutableDictionary\",&,N,V_activeMemberDevices"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
+ "T@\"NSSet\",R,&,N,V_groupHKIdentifiers"
+ "T@\"NSSet\",R,N,V_groupedHomeKitIdentifiers"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"NSString\",R,&,N,V_requestIdentifier"
+ "T@\"RPCompanionLinkClient\",&,N,V_companionLinkClient"
+ "TB,N,V_activated"
+ "TI,N,V_baseRequestID"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "_activeMemberDevices"
+ "_activeMembers"
+ "_companionLinkClient"
+ "_groupHKIdentifiers"
+ "_onqueue_activeMemberWithIDSIdentifier:"
+ "_onqueue_deliverDidEndDelegateForSession:notice:initiator:error:"
+ "_onqueue_deliverDidFailToStartSessionWithMember:consumer:error:"
+ "_onqueue_deliverDidFailToStartSessionWithMember:producer:error:"
+ "_onqueue_deliverSuccessfullyStartedSession:withMember:consumer:"
+ "_onqueue_deliverSuccessfullyStartedSession:withResponse:withMember:producer:"
+ "_onqueue_devicePresentInGroup:"
+ "_onqueue_handleCapableCommand:fromMember:callback:"
+ "_onqueue_handleDeviceFound:"
+ "_onqueue_handleDeviceLost:"
+ "_onqueue_handleIncomingRequest:options:responseHandler:"
+ "_onqueue_handleStartCommand:withMember:callback:"
+ "_onqueue_handleStopCommand:fromMember:callback:"
+ "_onqueue_memberFromRPCompanionLinkDevice:"
+ "_onqueue_sendRequest:members:withCompletionHandler:"
+ "_onqueue_startSessionWithProducer:member:"
+ "_onqueue_startSessionWithProducer:member:request:"
+ "_rapportTransport"
+ "_requestIdentifier"
+ "_serializeDataForResponse:"
+ "_serializedDataForRequest:"
+ "activeDevices"
+ "activeMemberDevices"
+ "activeMembers"
+ "addHomeKitGroupIdentifiers:"
+ "baseRequestID"
+ "className"
+ "companionLinkClient"
+ "didFindMember:"
+ "didLoseMember:"
+ "didReceiveRequest:from:withCompletionHandler:"
+ "effectiveIdentifier"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "groupHKIdentifiers"
+ "homeKitIdentifier"
+ "idsDeviceIdentifier"
+ "initWithHomeKitIdentifier:"
+ "initWithIdentifier:delegate:companionLink:dispatchQueue:"
+ "initWithIdentifier:delegate:dispatchQueue:"
+ "lock"
+ "rapportTransport"
+ "registerRequestID:options:handler:"
+ "removeHomeKitGroupIdentifiers:"
+ "requestIdentifier"
+ "roleForParticipant"
+ "sendRequest:to:withCompletionHandler:"
+ "sendRequestID:request:destinationID:options:responseHandler:"
+ "setActiveMemberDevices:"
+ "setBaseRequestID:"
+ "setCompanionLinkClient:"
+ "setControlFlags:"
+ "setDeviceFoundHandler:"
+ "setDeviceLostHandler:"
+ "setDispatchQueue:"
+ "setIdentifier:"
+ "setLock:"
+ "setQueue:"
+ "setRapportTransport:"
+ "setWithSet:"
+ "setWorkQueue:"
+ "snapshotWithParticipantRoleForMember:"
+ "v16@?0@\"RPCompanionLinkDevice\"8"
+ "v20@0:8I16"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8@\"COClusterMember\"16"
+ "v32@?0@\"COClusterMember\"8@\"RPCompanionLinkDevice\"16^B24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"COMessageSessionProducer\"16^B24"
+ "v40@0:8@\"COMessageChannelRequest\"16@\"COClusterMember\"24@?<v@?@\"COMessageChannelResponse\"@\"NSError\">32"
+ "workQueue"
+ "{os_unfair_lock_s=I}16@0:8"
- "\x11\x13="
- "T@\"NSArray\",R,N,V_groupedHomeKitIdentifiers"

```

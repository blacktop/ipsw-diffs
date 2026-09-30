## Catalyst

> `/System/Library/PrivateFrameworks/Catalyst.framework/Versions/A/Catalyst`

```diff

 11.5.0.0.0
-  __TEXT.__text: 0x5b44c
+  __TEXT.__text: 0x5d348
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x4e4c
+  __TEXT.__objc_methlist: 0x5748
   __TEXT.__const: 0x7e8
   __TEXT.__cstring: 0x30b2
-  __TEXT.__gcc_except_tab: 0xbb8
+  __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__oslogstring: 0xa51
   __TEXT.__swift5_typeref: 0x4ce
   __TEXT.__swift5_capture: 0x2bc

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x48
-  __TEXT.__unwind_info: 0x1ce8
-  __TEXT.__eh_frame: 0xe20
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x74
+  __TEXT.__unwind_info: 0x1dd0
+  __TEXT.__eh_frame: 0xdd0
   __TEXT.__objc_classname: 0x128f
   __TEXT.__objc_methname: 0xa919
   __TEXT.__objc_methtype: 0x2638

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2490
+  __DATA_CONST.__objc_selrefs: 0x24f8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x888
   __AUTH_CONST.__const: 0x1a70
   __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0xc2a8
+  __AUTH_CONST.__objc_const: 0xb350
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 38A8BAE3-B290-3806-ACC0-3F14941659F0
-  Functions: 2308
-  Symbols:   5182
+  UUID: 56652887-AC32-3343-A340-9CE2F42D1221
+  Functions: 2468
+  Symbols:   5388
   CStrings:  3207
 
Symbols:
+ +[CATHTTPMessageParser encodeRequestData:].cold.1
+ +[CATOperationQueue backgroundQueue].cold.1
+ +[CATProperty initialize].cold.1
+ +[CATRemoteConnection createConnectionPairWithConnection:andConnection:bufferSize:].cold.1
+ +[CATRemoteConnection createConnectionPairWithConnection:andConnection:bufferSize:].cold.2
+ +[CATRemoteTransport createRemoteTransportPairWithTransport:andTransport:].cold.1
+ +[CATRemoteTransport createRemoteTransportPairWithTransport:andTransport:].cold.2
+ +[CATSharingMessage instanceWithDictionary:].cold.2
+ +[CATSharingSentMessage instanceWithDictionary:].cold.2
+ +[CATTaskProgress assertResultObject:isValidForRequestClassName:].cold.1
+ +[NSDate(CATInternetDateAndTime) cat_RFC3339Formatters].cold.1
+ +[NSKeyedUnarchiver(CATSecureCoding) cat_unarchiveObjectOfClass:withData:].cold.1
+ +[NSKeyedUnarchiver(CATSecureCoding) cat_unarchiveObjectOfClass:withData:error:].cold.1
+ +[NSKeyedUnarchiver(CATSecureCoding) cat_unarchiveObjectOfClasses:withData:error:].cold.1
+ +[NSNumber(CATCasting) cat_numberWithObject:].cold.1
+ -[CATAddress address].cold.1
+ -[CATAddress initWithData:].cold.1
+ -[CATArbitrator registerResource:forKey:].cold.1
+ -[CATArbitrator registerResource:forKey:].cold.2
+ -[CATArbitrator registerResource:forKey:maxConcurrentCount:].cold.1
+ -[CATArbitrator registerResource:forKey:maxConcurrentCount:].cold.2
+ -[CATArbitrator registerResource:forKey:maxConcurrentCount:].cold.3
+ -[CATArbitrator resourceForKey:exclusive:].cold.1
+ -[CATArbitrator resourcesForKeys:exclusive:].cold.1
+ -[CATBatchRemoteTaskOperation initWithTaskClient:requests:].cold.1
+ -[CATCollectionController bindContentToObject:withKeyPath:usingTransformer:].cold.1
+ -[CATCollectionController bindContentToObject:withKeyPath:usingTransformer:].cold.2
+ -[CATCollectionController changeContent:].cold.1
+ -[CATConcreteIDSServiceConnectionDataAggregator updateExistingDataWindowWithContent:].cold.1
+ -[CATConcreteIDSServiceConnectionDataMessageQueue receiveData:completion:].cold.1
+ -[CATEndPoint initWithAddress:port:].cold.1
+ -[CATEndPoint initWithData:].cold.1
+ -[CATIDSServiceConnection processMessage:senderAppleID:senderAddress:].cold.1
+ -[CATIDSServiceConnectionMessageProcessor receiveMessage:].cold.1
+ -[CATIDSServiceConnectionMessageProcessor receiveMessage:].cold.2
+ -[CATIDSServiceConnectionMessageProcessor receiveMessage:].cold.3
+ -[CATIDSServiceConnectionMessageProcessor receiveMessage:].cold.4
+ -[CATIDSServiceConnectionMetadata isEqual:].cold.1
+ -[CATIDSServiceConnectionTerminal initWithIDSPrimitives:assertionProvider:timerSource:workQueue:delegateQueue:sourceAppleID:connectionConfiguration:].cold.1
+ -[CATLocalizationHelper stringByKeyForTableName:].cold.2
+ -[CATLocalizationHelper stringByKeyForTableName:].cold.3
+ -[CATLocalizationHelper stringsForKey:value:table:].cold.1
+ -[CATMutableTaskProgress initWithOperationUUID:requestClass:].cold.1
+ -[CATNetworkReachability initWithAddress:].cold.1
+ -[CATNotificationMessage initWithName:userInfo:].cold.1
+ -[CATNotificationMessage initWithTaskUUID:name:userInfo:].cold.1
+ -[CATOperation endOperationWithError:].cold.1
+ -[CATOperation start].cold.1
+ -[CATOperation start].cold.2
+ -[CATOperationQueue setUnderlyingQueue:].cold.1
+ -[CATProperty initWithName:attributes:].cold.1
+ -[CATProperty initWithName:attributes:].cold.2
+ -[CATRemoteConnection connectionDidInterruptWithError:].cold.1
+ -[CATRemoteConnection dealloc].cold.1
+ -[CATRemoteConnection initWithInputStream:outputStream:bufferSize:].cold.1
+ -[CATRemoteConnection initWithInputStream:outputStream:bufferSize:].cold.2
+ -[CATRemoteConnection initWithNetService:].cold.1
+ -[CATRemoteConnection open].cold.1
+ -[CATRemoteConnection secureUsingIdentity:trustedCertificates:isServer:].cold.1
+ -[CATRemoteConnection secureUsingIdentity:trustedCertificates:isServer:].cold.2
+ -[CATRemoteConnection tryEvaluatingPeerTrustWithStream:].cold.1
+ -[CATRemoteTaskOperation clientFailedWithError:].cold.1
+ -[CATRemoteTaskOperation initWithRequest:client:].cold.1
+ -[CATRemoteTaskOperation initWithRequest:client:].cold.2
+ -[CATRemoteTaskOperation initWithRequest:clientError:].cold.1
+ -[CATRemoteTaskOperation initWithRequest:clientError:].cold.2
+ -[CATRemoteTaskOperation main].cold.1
+ -[CATRemoteTaskOperation processNotificationWithName:userInfo:].cold.2
+ -[CATRemoteTransport initWithRemoteConnection:].cold.1
+ -[CATSerialOperationEnqueuer observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[CATSharingBroadcastTerminal _activate].cold.1
+ -[CATSharingBroadcastTerminal _invalidateWithError:removePrimitiveHandlers:deactivatePrimitives:].cold.1
+ -[CATSharingBroadcastTerminal sessionHasPaired].cold.1
+ -[CATSharingBroadcastTerminal sessionNeedsToDisplayPin:].cold.1
+ -[CATSharingDeviceDiscovery _activate].cold.1
+ -[CATSharingDeviceDiscovery pairingTerminalForDevice:].cold.1
+ -[CATSharingSentMessage initWithContent:].cold.1
+ -[CATSocket acceptPendingConnection].cold.2
+ -[CATSocket connectToEndPoint:error:].cold.1
+ -[CATSocket dealloc].cold.1
+ -[CATSocket setNativeSocket:].cold.1
+ -[CATSocket setNativeSocket:].cold.2
+ -[CATState addTransitionToState:triggeringEvent:action:].cold.1
+ -[CATState addTransitionToState:triggeringEvent:action:].cold.2
+ -[CATState initWithName:].cold.1
+ -[CATStateMachine addState:].cold.1
+ -[CATStateMachine addState:].cold.2
+ -[CATStateMachine dealloc].cold.1
+ -[CATStateMachine initWithTarget:].cold.1
+ -[CATStateMachine start].cold.2
+ -[CATStateMachine start].cold.3
+ -[CATStateMachine stateWithName:].cold.1
+ -[CATStateMachine transitionWithTriggeringEvent:].cold.3
+ -[CATStateMachine transitionWithTriggeringEvent:].cold.4
+ -[CATStateMachine transitionWithTriggeringEvent:].cold.5
+ -[CATStateMachineEvent initWithEventTrigger:context:].cold.1
+ -[CATTaskClient captureTransport].cold.1
+ -[CATTaskClient dealloc].cold.1
+ -[CATTaskClient postNotificationWithName:userInfo:].cold.1
+ -[CATTaskClient resumeCapturedTransportFromTaskClient:].cold.1
+ -[CATTaskClient resumeCapturedTransportFromTaskClient:].cold.2
+ -[CATTaskClient resumeTransport:].cold.1
+ -[CATTaskMessage initWithTaskUUID:].cold.1
+ -[CATTaskMessageError initWithTaskUUID:taskError:].cold.1
+ -[CATTaskMessageStart initWithCoder:].cold.1
+ -[CATTaskMessageStart initWithTaskUUID:request:].cold.1
+ -[CATTaskOperation postNotificationWithName:userInfo:].cold.2
+ -[CATTaskProgress initWithOperation:].cold.1
+ -[CATTaskProgress initWithOperationUUID:].cold.1
+ -[CATTaskServer dealloc].cold.1
+ -[CATTaskServer delegateDidInvalidateAndFinalize].cold.1
+ -[CATTaskServer session:prepareOperationForRequest:error:].cold.1
+ -[CATTaskServer session:prepareOperationForRequest:error:].cold.2
+ -[CATTaskSession captureTransport].cold.1
+ -[CATTaskSession connectWithTransportFromTaskSession:].cold.1
+ -[CATTaskSession dealloc].cold.1
+ -[CATTaskSession enqueueOperation:].cold.1
+ -[CATTaskSession postNotificationWithName:userInfo:].cold.1
+ -[CATTaskSession resumeCapturedTransportFromTaskSession:].cold.1
+ -[CATTaskSession resumeCapturedTransportFromTaskSession:].cold.2
+ -[CATTaskSession resumeTransport:].cold.1
+ -[CATTaskSession savePreviousSessionInfo].cold.1
+ -[CATTaskSession sendMessageThroughTransport:].cold.1
+ -[CATTaskSession transport:didFailToSendMessage:error:].cold.1
+ -[CATTransport dealloc].cold.1
+ -[CATTransport enqueueDelegateDidInvalidateAndFinalize].cold.1
+ -[CATXPCTransport dealloc].cold.1
+ -[CATXPCTransport initWithXPCConnection:].cold.1
+ -[NSDictionary(CATChangeDictionary) cat_calculateAddedObjects].cold.1
+ -[NSDictionary(CATChangeDictionary) cat_calculateRemovedObjects].cold.1
+ -[_CATArbitratorRegistrationEntry initWithResource:maxConcurrentCount:].cold.1
+ -[_CATArbitratorRegistrationEntry initWithResource:maxConcurrentCount:].cold.2
+ -[_CATArbitratorResourceProxy forwardInvocation:].cold.1
+ -[_CATArbitratorResourceProxy forwardingTargetForSelector:].cold.1
+ -[_CATArbitratorResourceProxy methodSignatureForSelector:].cold.1
+ -[_CATArbitratorResourceProxy respondsToSelector:].cold.1
+ -[_CATArbitratorWaitToken initWithDelegateQueue:completionBlock:].cold.1
+ -[_CATArbitratorWaitToken initWithDelegateQueue:completionBlock:].cold.2
+ -[_CATArbitratorWaitToken waitForRegistrationEntry:forKey:exclusive:].cold.1
+ -[_CATObserverManager addObserver:].cold.1
+ -[_CATObserverManager initWithOperation:].cold.1
+ -[_CATObserverManager operationDidFinish:].cold.1
+ -[_CATObserverManager operationDidProgress:].cold.1
+ -[_CATObserverManager operationDidStart:].cold.1
+ -[_CATOperationTargetSelectorObserver initWithTarget:selector:events:userInfo:delegateQueue:].cold.1
+ -[_CATOperationTargetSelectorObserver initWithTarget:selector:events:userInfo:delegateQueue:].cold.2
+ -[_CATProxyWaitToken initWithExclusive:group:].cold.1
+ -[_CATRemoteConnectionSendDataContext initWithData:userInfo:].cold.1
+ -[_CATRemoteConnectionSendDataWithStreamContext initWithStream:length:bufferSize:userInfo:].cold.1
+ CATErrorWithDomainCodeAndUserInfo.cold.1
+ CATGetCatalystQueue.cold.1
+ _CATErrorDescriptionsWithCodeAndUserInfo.cold.1
+ _CATLogFSM.cold.1
+ _CATLogGeneral.cold.1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __69-[CATConcreteIDSServiceConnectionDataMessageQueue retransmitContent:]_block_invoke.cold.2
+ __78-[CATIDSServiceConnectionTerminal processMessage:senderAppleID:senderAddress:]_block_invoke_2.cold.1
+ __78-[CATIDSServiceConnectionTerminal processMessage:senderAppleID:senderAddress:]_block_invoke_2.cold.2
+ __78-[CATIDSServiceConnectionTerminal processMessage:senderAppleID:senderAddress:]_block_invoke_2.cold.3
+ __78-[CATIDSServiceConnectionTerminal processMessage:senderAppleID:senderAddress:]_block_invoke_2.cold.4
+ __78-[CATIDSServiceConnectionTerminal processMessage:senderAppleID:senderAddress:]_block_invoke_2.cold.5
+ __78-[CATIDSServiceConnectionTerminal processMessage:senderAppleID:senderAddress:]_block_invoke_2.cold.6
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets

```

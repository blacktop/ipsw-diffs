## SpatialAudioServices

> `/System/Library/PrivateFrameworks/SpatialAudioServices.framework/SpatialAudioServices`

```diff

-23.40.1.0.0
-  __TEXT.__text: 0x49ffc
+23.60.1.0.0
+  __TEXT.__text: 0x49f38
   __TEXT.__lazy_helpers: 0x24c
   __TEXT.__objc_methlist: 0x2474
   __TEXT.__const: 0x396c
-  __TEXT.__gcc_except_tab: 0x5b20
+  __TEXT.__gcc_except_tab: 0x5b1c
   __TEXT.__cstring: 0x2567
   __TEXT.__oslogstring: 0x162c
   __TEXT.__dlopen_cstrs: 0x6a
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ __ZN3SAS3AAS10DuplexPipeD2Ev : 128 -> 124
~ __ZN3SAS3AAS10DuplexPipe18swapImplementationENSt3__110shared_ptrINS1_14DuplexPipeImplEEE : 148 -> 144
~ __ZN3SAS3AAS10DuplexPipe16beginTransactionEjPKvm : 136 -> 132
~ __ZN3SAS3AAS10DuplexPipe14reserveMessageEjmRNS1_11Transaction7Message15DeallocStrategyE : 144 -> 140
~ __ZN3SAS3AAS10DuplexPipe13commitMessageEPvNS1_11Transaction7Message15DeallocStrategyE : 128 -> 124
~ __ZN3SAS3AAS10DuplexPipe17commitTransactionEj : 112 -> 108
~ -[SCSXPCClient permissions] : 88 -> 84
~ ___47-[SCSXPCClient bootstrapConnection:completion:]_block_invoke : 232 -> 228
~ -[SCSXPCClient addFulfiller:] : 132 -> 128
~ -[SCSXPCClient removeFulfiller:] : 548 -> 544
~ -[SCSXPCClient addRequester:] : 152 -> 148
~ -[SCSXPCClient removeRequester:] : 496 -> 492
~ -[SCSXPCClient didChangeStatus:] : 484 -> 480
~ -[SCSXPCClient currentStreamConfiguration:] : 280 -> 276
~ -[SCSXPCClient startOrUpdateControlForStream:configuration:completion:] : 468 -> 464
~ -[SCSXPCClient stopControlForStream:] : 312 -> 308
~ -[SCSXPCClient streamControlWasInvalidated:details:] : 268 -> 264
~ -[SCSXPCClient startOrUpdateControlCompletedForStream:configuration:withResult:] : 348 -> 344
~ -[SCSXPCClient receivedStartOrUpdateControlForStream:configuration:completion:] : 776 -> 772
~ -[SCSXPCClient receivedStopControlForStream:] : 468 -> 464
~ -[SCSXPCClient receivedStreamControlWasInvalidated:details:] : 560 -> 556
~ -[SCSXPCClient receivedStartOrUpdateControlCompletedForStream:configuration:withResult:] : 312 -> 308
~ __ZN3SAS17LockableContainerIU8__strongPU29objcproto18SASConnectionEntry11objc_objectNS_17ObjectPointerHashEE5_lockEv : 244 -> 240
~ ___47-[RCSXPCClient bootstrapConnection:completion:]_block_invoke : 168 -> 164
~ -[RCSXPCClient permissions] : 88 -> 84
~ -[RCSXPCClient roomCongruenceInformation] : 100 -> 96
~ -[RCSXPCClient addSubscriber:] : 204 -> 200
~ -[RCSXPCClient removeSubscriber:] : 132 -> 128
~ -[RCSXPCClient didChangeStatus:] : 236 -> 232
~ -[RCSXPCClient updateRoomCongruenceInformation:] : 252 -> 248
~ -[RCSXPCClient didUpdateRoomCongruenceInformation:] : 120 -> 116
~ -[SASXPCClient handleSuccessfulConnection:] : 568 -> 564
~ -[SASXPCClient remoteObjectProxyWithErrorHandler:] : 504 -> 500
~ -[SASXPCClient clearConnectionAndUpdateStatus:] : 148 -> 144
~ -[SpatialAudioService operateUnderLock:] : 124 -> 120
~ -[SpatialAudioService clearAndInvalidateConnectionEntries] : 228 -> 224
~ __ZN7Service23initializeSharedServiceEv : 120 -> 116
~ -[SASAnchorServiceXPCConnectionEntry outgoingChannelFilter] : 144 -> 140
~ -[SASAnchorServiceXPCConnectionEntry setOutgoingChannelFilter:] : 128 -> 124
~ -[SASAnchorServiceXPCConnectionEntry configureSharedMemoryChannel:completion:] : 212 -> 208
~ -[SASAnchorServiceXPCConnectionEntry sendFilterUpdateReplyToClient:messageID:] : 328 -> 324
~ -[SASAnchorServiceXPCConnectionEntry sendHasAnySubscriberRequestedFrontAnchoringToClient:] : 260 -> 256
~ -[SASAnchorServiceXPCConnectionEntry sendAnchorUpdates:publisherID:transactionInformation:properties:] : 184 -> 180
~ -[SASAnchorServiceXPCConnectionEntry invalidate] : 268 -> 264
~ __ZN3SAS3AAS17AASXPCClient_Impl29beginTransactionFromPublisherEyyy : 144 -> 140
~ __ZNK3SAS3AAS17AASXPCClient_Impl18getSubscriberStateERK14AASAudioAnchoryP27AASAudioAnchorPropertyStatePU15__autoreleasingP34AASAudioAnchorRenderingPreferences : 132 -> 128
~ __ZNK3SAS3AAS17AASXPCClient_Impl18getStatusForAnchorERK14AASAudioAnchor : 108 -> 104
~ __ZNK3SAS3AAS17AASXPCClient_Impl20findAnyTrackedAnchorE18AASAudioAnchorTypey : 124 -> 120
~ __ZNK3SAS3AAS17AASXPCClient_Impl22findAnchorMatchingUUIDEP6NSUUID : 120 -> 116
~ __ZN3SAS3AAS17AASXPCClient_Impl23subscriberIDWillDeallocEy : 100 -> 96
~ __ZN3SAS3AAS17AASXPCClient_Impl28beginFilterUpdateTransactionEP20AASAudioAnchorFilterNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE : 112 -> 108
~ __ZN3SAS3AAS17AASXPCClient_Impl27beginFilterReplyTransactionENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 12 -> 8
~ __ZThn24_N3SAS3AAS17AASXPCClient_Impl27beginFilterReplyTransactionENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 12 -> 8
~ __ZN3SAS3AAS17AASXPCClient_Impl11applyUpdateERKNS0_22SubscriberAnchorUpdateE : 148 -> 144
~ __ZN3SAS3AAS17AASXPCClient_Impl15onServerConnectEv : 596 -> 592
~ __ZN3SAS17LockableContainerIU8__strongP24AASAudioAnchorSubscriberNS_17ObjectPointerHashEE5_lockEv : 244 -> 240
~ -[SCSDirectClientConnection addRequester:] : 84 -> 80
~ -[SCSDirectClientConnection removeRequester:] : 92 -> 88
~ -[SCSDirectClientConnection addFulfiller:] : 84 -> 80
~ -[SCSDirectClientConnection removeFulfiller:] : 92 -> 88
~ -[SCSDirectClientConnection startOrUpdateControlForStream:configuration:completion:] : 364 -> 360
~ -[SCSDirectClientConnection stopControlForStream:] : 244 -> 240
~ -[SCSDirectClientConnection receivedStreamControlWasInvalidated:details:] : 252 -> 248
~ -[SCSDirectClientConnection receivedStartOrUpdateControlCompletedForStream:configuration:withResult:] : 244 -> 240
~ sub_2b46beb38 -> sub_2b69bea38 : 260 -> 284
~ sub_2b46bec3c -> sub_2b69beb54 : 252 -> 276
~ sub_2b46c646c -> sub_2b69c639c : 112 -> 124
```

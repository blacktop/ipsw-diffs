## AccessoryNowPlaying

> `/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x32cc
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x314
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__cstring: 0x3f4
-  __TEXT.__oslogstring: 0x564
-  __TEXT.__unwind_info: 0x130
-  __TEXT.__objc_classname: 0x71
-  __TEXT.__objc_methname: 0x79d
-  __TEXT.__objc_methtype: 0x2a5
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x4a0
+1176.0.26.502.1
+  __TEXT.__text: 0x34d8
+  __TEXT.__objc_methlist: 0x3c4
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__cstring: 0x428
+  __TEXT.__oslogstring: 0x6db
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x508
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x250
+  __DATA_CONST.__objc_selrefs: 0x2d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x198
-  __AUTH_CONST.__const: 0xc0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x620
-  __AUTH_CONST.__objc_const: 0x380
+  __AUTH_CONST.__objc_const: 0x410
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x1f8
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA.__common: 0xc
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__common: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 66B64A77-C805-3416-91CB-98B22ED863E0
-  Functions: 80
-  Symbols:   465
-  CStrings:  275
+  UUID: 58123CDD-914F-31DA-BDC9-2669EF9A1428
+  Functions: 100
+  Symbols:   527
+  CStrings:  150
 
Symbols:
+ -[AccessoryNowPlayingClient _connectToServiceOnQueue]
+ -[AccessoryNowPlayingClient _connectToServiceOnQueue].cold.1
+ -[AccessoryNowPlayingClient _connectToServiceOnQueue].cold.2
+ -[AccessoryNowPlayingClient _connectToServiceOnQueue].cold.3
+ -[AccessoryNowPlayingClient _connectToServiceOnQueue].cold.4
+ -[AccessoryNowPlayingClient _disconnectOnQueue]
+ -[AccessoryNowPlayingClient _updateSubscriberListOnQueue]
+ -[AccessoryNowPlayingClient addSubscriber:]
+ -[AccessoryNowPlayingClient cancelRequestPlaybackQueueListInfo:requestID:].cold.1
+ -[AccessoryNowPlayingClient clientQueue]
+ -[AccessoryNowPlayingClient connectToService]
+ -[AccessoryNowPlayingClient decrementUserCount]
+ -[AccessoryNowPlayingClient disconnect]
+ -[AccessoryNowPlayingClient featureUserCount]
+ -[AccessoryNowPlayingClient incrementUserCount]
+ -[AccessoryNowPlayingClient init]
+ -[AccessoryNowPlayingClient isConnected]
+ -[AccessoryNowPlayingClient mediaItemArtworkHasChanged:withReply:]
+ -[AccessoryNowPlayingClient mediaItemArtworkHasChanged:withReply:].cold.1
+ -[AccessoryNowPlayingClient mediaItemAttributesHaveChanged:withReply:]
+ -[AccessoryNowPlayingClient mediaItemAttributesHaveChanged:withReply:].cold.1
+ -[AccessoryNowPlayingClient mockListenerEndpoint]
+ -[AccessoryNowPlayingClient needsSubscriberListResync]
+ -[AccessoryNowPlayingClient playbackAttributesHaveChanged:withReply:]
+ -[AccessoryNowPlayingClient playbackAttributesHaveChanged:withReply:].cold.1
+ -[AccessoryNowPlayingClient playbackQueueListChanged]
+ -[AccessoryNowPlayingClient playbackQueueListChanged].cold.1
+ -[AccessoryNowPlayingClient removeSubscriber:]
+ -[AccessoryNowPlayingClient requestCurrentMediaItemArtwork:]
+ -[AccessoryNowPlayingClient requestCurrentMediaItemAttributes:]
+ -[AccessoryNowPlayingClient requestCurrentPlaybackAttributes:]
+ -[AccessoryNowPlayingClient requestPlaybackQueueListInfo:requestID:startIndex:upToCount:infoMask:].cold.1
+ -[AccessoryNowPlayingClient serviceConnection]
+ -[AccessoryNowPlayingClient setClientQueue:]
+ -[AccessoryNowPlayingClient setFeatureUserCount:]
+ -[AccessoryNowPlayingClient setMockListenerEndpoint:]
+ -[AccessoryNowPlayingClient setNeedsSubscriberListResync:]
+ -[AccessoryNowPlayingClient setPlaybackElapsedTime:]
+ -[AccessoryNowPlayingClient setPlaybackQueueIndex:]
+ -[AccessoryNowPlayingClient setServiceConnection:]
+ -[AccessoryNowPlayingClient setSubscribers:]
+ -[AccessoryNowPlayingClient subscribers]
+ -[AccessoryNowPlayingClient updateSubscriberList:]
+ GCC_except_table4
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_IVAR_$_AccessoryNowPlayingClient._clientQueue
+ _OBJC_IVAR_$_AccessoryNowPlayingClient._featureUserCount
+ _OBJC_IVAR_$_AccessoryNowPlayingClient._mockListenerEndpoint
+ _OBJC_IVAR_$_AccessoryNowPlayingClient._needsSubscriberListResync
+ _OBJC_IVAR_$_AccessoryNowPlayingClient._serviceConnection
+ _OBJC_IVAR_$_AccessoryNowPlayingClient._subscribers
+ __MergedGlobals.4
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACCNowPlayingFeatureClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACCNowPlayingFeatureServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACCNowPlayingFeatureClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACCNowPlayingFeatureServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_ACCNowPlayingFeatureClientProtocol
+ __OBJC_$_PROTOCOL_REFS_ACCNowPlayingFeatureServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_ACCNowPlayingFeatureClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_ACCNowPlayingFeatureServiceProtocol
+ __OBJC_PROTOCOL_$_ACCNowPlayingFeatureClientProtocol
+ __OBJC_PROTOCOL_$_ACCNowPlayingFeatureServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ACCNowPlayingFeatureClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ACCNowPlayingFeatureServiceProtocol
+ ___39-[AccessoryNowPlayingClient disconnect]_block_invoke
+ ___43-[AccessoryNowPlayingClient addSubscriber:]_block_invoke
+ ___43-[AccessoryNowPlayingClient addSubscriber:]_block_invoke.cold.1
+ ___45-[AccessoryNowPlayingClient connectToService]_block_invoke
+ ___46-[AccessoryNowPlayingClient removeSubscriber:]_block_invoke
+ ___46-[AccessoryNowPlayingClient removeSubscriber:]_block_invoke.cold.1
+ ___47-[AccessoryNowPlayingClient decrementUserCount]_block_invoke
+ ___47-[AccessoryNowPlayingClient decrementUserCount]_block_invoke.cold.1
+ ___47-[AccessoryNowPlayingClient incrementUserCount]_block_invoke
+ ___50-[AccessoryNowPlayingClient updateSubscriberList:]_block_invoke
+ ___50-[AccessoryNowPlayingClient updateSubscriberList:]_block_invoke.cold.1
+ ___50-[AccessoryNowPlayingClient updateSubscriberList:]_block_invoke.cold.2
+ ___51-[AccessoryNowPlayingClient setPlaybackQueueIndex:]_block_invoke
+ ___51-[AccessoryNowPlayingClient setPlaybackQueueIndex:]_block_invoke.cold.1
+ ___51-[AccessoryNowPlayingClient setPlaybackQueueIndex:]_block_invoke.cold.2
+ ___52-[AccessoryNowPlayingClient setPlaybackElapsedTime:]_block_invoke
+ ___52-[AccessoryNowPlayingClient setPlaybackElapsedTime:]_block_invoke.cold.1
+ ___52-[AccessoryNowPlayingClient setPlaybackElapsedTime:]_block_invoke.cold.2
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.78
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.78.cold.1
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.79
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.80
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.80.cold.1
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.80.cold.2
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.82
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.82.cold.1
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.82.cold.2
+ ___53-[AccessoryNowPlayingClient _connectToServiceOnQueue]_block_invoke.cold.1
+ ___57-[AccessoryNowPlayingClient _updateSubscriberListOnQueue]_block_invoke
+ ___57-[AccessoryNowPlayingClient _updateSubscriberListOnQueue]_block_invoke.cold.1
+ ___57-[AccessoryNowPlayingClient _updateSubscriberListOnQueue]_block_invoke.cold.2
+ ___98-[AccessoryNowPlayingClient requestPlaybackQueueListInfo:requestID:startIndex:upToCount:infoMask:]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_tmp.3
+ ___block_literal_global.169
+ ___block_literal_global.85
+ ___block_literal_global.87
+ ___block_literal_global.89
+ ___block_literal_global.93
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _dispatch_after
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_queue_create
+ _dispatch_sync
+ _dispatch_time
+ _logObjectForModule.onceToken
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_connectToServiceOnQueue
+ _objc_msgSend$_disconnectOnQueue
+ _objc_msgSend$_updateSubscriberListOnQueue
+ _objc_msgSend$addObject:
+ _objc_msgSend$allObjects
+ _objc_msgSend$clientQueue
+ _objc_msgSend$clientWillDisconnect
+ _objc_msgSend$connectToService
+ _objc_msgSend$countForObject:
+ _objc_msgSend$disconnect
+ _objc_msgSend$featureUserCount
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$mockListenerEndpoint
+ _objc_msgSend$needsSubscriberListResync
+ _objc_msgSend$nowPlayingMediaItemArtworkDidUpdate:
+ _objc_msgSend$nowPlayingMediaItemAttributesDidUpdate:
+ _objc_msgSend$nowPlayingPlaybackAttributesDidUpdate:
+ _objc_msgSend$nowPlayingPlaybackQueueListDidChange:
+ _objc_msgSend$nowPlayingPlaybackQueueListInfoResponse:info:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$requestCurrentMediaItemArtworkWithReply:
+ _objc_msgSend$requestCurrentMediaItemAttributesWithReply:
+ _objc_msgSend$requestCurrentPlaybackAttributesWithReply:
+ _objc_msgSend$serviceConnection
+ _objc_msgSend$setFeatureUserCount:
+ _objc_msgSend$setMockListenerEndpoint:
+ _objc_msgSend$setNeedsSubscriberListResync:
+ _objc_msgSend$setPlaybackElapsedTime:withReply:
+ _objc_msgSend$setPlaybackQueueIndex:withReply:
+ _objc_msgSend$setServiceConnection:
+ _objc_msgSend$subscribers
+ _objc_msgSend$updateSubscriberList:withReply:
+ _objc_retain_x1
+ _objc_retain_x8
- -[AccessoryNowPlayingClient connectToServer]
- -[AccessoryNowPlayingClient connectToServer].cold.1
- -[AccessoryNowPlayingClient connectToServer].cold.2
- -[AccessoryNowPlayingClient connectToServer].cold.3
- -[AccessoryNowPlayingClient initWithDelegate:]
- -[AccessoryNowPlayingClient initWithDelegate:].cold.1
- -[AccessoryNowPlayingClient mediaItemArtworkDidChange]
- -[AccessoryNowPlayingClient mediaItemAttributesDidChange:]
- -[AccessoryNowPlayingClient playbackAttributesDidChange:]
- -[AccessoryNowPlayingClient playbackQueueListDidChange]
- -[AccessoryNowPlayingClient serverConnection]
- -[AccessoryNowPlayingClient setPlaybackElapsedTime:withReply:]
- -[AccessoryNowPlayingClient setPlaybackQueueIndex:withReply:]
- -[AccessoryNowPlayingClient setServerConnection:]
- -[AccessoryNowPlayingClient setShouldSendArtwork:]
- -[AccessoryNowPlayingClient setSubscriberList:]
- -[AccessoryNowPlayingClient shouldSendArtwork]
- -[AccessoryNowPlayingClient shouldSendPlaybackQueueList]
- -[AccessoryNowPlayingClient subscriberList]
- -[AccessoryNowPlayingClient triggerMediaItemArtworkUpdateWithReply:]
- -[AccessoryNowPlayingClient triggerMediaItemArtworkUpdateWithReply:].cold.1
- -[AccessoryNowPlayingClient triggerMediaItemArtworkUpdateWithReply:].cold.2
- -[AccessoryNowPlayingClient triggerMediaItemAttributesUpdateWithReply:]
- -[AccessoryNowPlayingClient triggerPlaybackAttributesUpdateWithReply:]
- -[AccessoryNowPlayingClient updateSubscriberList:WithReply:]
- -[AccessoryNowPlayingClient updateSubscriberList:WithReply:].cold.1
- -[AccessoryNowPlayingClient updateSubscriberList:WithReply:].cold.2
- GCC_except_table0
- GCC_except_table3
- _OBJC_CLASS_$_NSSet
- _OBJC_IVAR_$_AccessoryNowPlayingClient._serverConnection
- _OBJC_IVAR_$_AccessoryNowPlayingClient._shouldSendArtwork
- _OBJC_IVAR_$_AccessoryNowPlayingClient._subscriberList
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AccessoryNowPlayingXPCClientProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AccessoryNowPlayingXPCServerProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_AccessoryNowPlayingXPCClientProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_AccessoryNowPlayingXPCServerProtocol
- __OBJC_$_PROTOCOL_REFS_AccessoryNowPlayingXPCClientProtocol
- __OBJC_$_PROTOCOL_REFS_AccessoryNowPlayingXPCServerProtocol
- __OBJC_LABEL_PROTOCOL_$_AccessoryNowPlayingXPCClientProtocol
- __OBJC_LABEL_PROTOCOL_$_AccessoryNowPlayingXPCServerProtocol
- __OBJC_PROTOCOL_$_AccessoryNowPlayingXPCClientProtocol
- __OBJC_PROTOCOL_$_AccessoryNowPlayingXPCServerProtocol
- __OBJC_PROTOCOL_REFERENCE_$_AccessoryNowPlayingXPCClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_AccessoryNowPlayingXPCServerProtocol
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.77
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.77.cold.1
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.78
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.78.cold.1
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.78.cold.2
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.80
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.80.cold.1
- ___44-[AccessoryNowPlayingClient connectToServer]_block_invoke.cold.1
- ___46-[AccessoryNowPlayingClient initWithDelegate:]_block_invoke
- ___46-[AccessoryNowPlayingClient initWithDelegate:]_block_invoke.cold.1
- ___46-[AccessoryNowPlayingClient initWithDelegate:]_block_invoke.cold.2
- ___57-[AccessoryNowPlayingClient playbackAttributesDidChange:]_block_invoke
- ___57-[AccessoryNowPlayingClient playbackAttributesDidChange:]_block_invoke.cold.1
- ___57-[AccessoryNowPlayingClient playbackAttributesDidChange:]_block_invoke.cold.2
- ___58-[AccessoryNowPlayingClient mediaItemAttributesDidChange:]_block_invoke
- ___58-[AccessoryNowPlayingClient mediaItemAttributesDidChange:]_block_invoke.cold.1
- ___58-[AccessoryNowPlayingClient mediaItemAttributesDidChange:]_block_invoke.cold.2
- ___68-[AccessoryNowPlayingClient triggerMediaItemArtworkUpdateWithReply:]_block_invoke
- ___68-[AccessoryNowPlayingClient triggerMediaItemArtworkUpdateWithReply:]_block_invoke.cold.1
- ___68-[AccessoryNowPlayingClient triggerMediaItemArtworkUpdateWithReply:]_block_invoke.cold.2
- ___70-[AccessoryNowPlayingClient triggerPlaybackAttributesUpdateWithReply:]_block_invoke
- ___70-[AccessoryNowPlayingClient triggerPlaybackAttributesUpdateWithReply:]_block_invoke.cold.1
- ___70-[AccessoryNowPlayingClient triggerPlaybackAttributesUpdateWithReply:]_block_invoke.cold.2
- ___71-[AccessoryNowPlayingClient triggerMediaItemAttributesUpdateWithReply:]_block_invoke
- ___71-[AccessoryNowPlayingClient triggerMediaItemAttributesUpdateWithReply:]_block_invoke.cold.1
- ___71-[AccessoryNowPlayingClient triggerMediaItemAttributesUpdateWithReply:]_block_invoke.cold.2
- ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
- ___block_literal_global.82
- ___block_literal_global.84
- ___block_literal_global.95
- ___block_literal_global.99
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_msgSend$connectToServer
- _objc_msgSend$containsObject:
- _objc_msgSend$count
- _objc_msgSend$currentMediaItemArtwork
- _objc_msgSend$currentMediaItemAttributes
- _objc_msgSend$currentPlaybackAttributes
- _objc_msgSend$initConnection:
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$mediaItemArtworkHasChanged:withReply:
- _objc_msgSend$mediaItemAttributesHaveChanged:withReply:
- _objc_msgSend$playbackAttributesHaveChanged:withReply:
- _objc_msgSend$playbackQueueListChanged
- _objc_msgSend$playbackQueueListInfoResponse:requestID:info:
- _objc_msgSend$serverConnection
- _objc_msgSend$setPlaybackElapsedTime:
- _objc_msgSend$setPlaybackQueueIndex:
- _objc_msgSend$setServerConnection:
- _objc_msgSend$setSubscriberList:
- _objc_msgSend$setWithArray:
- _objc_msgSend$shouldSendArtwork
- _objc_msgSend$shouldSendArtworkDidChange:
- _objc_msgSend$shouldSendPlaybackQueueList
- _objc_msgSend$subscriberList
- _objc_msgSend$triggerMediaItemArtworkUpdateWithReply:
- _objc_opt_respondsToSelector
- _objc_release_x24
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "#Artwork Received mediaItemArtwork update from service: %lu bytes"
+ "%"
+ "%s:%d"
+ "-[AccessoryNowPlayingClient _connectToServiceOnQueue]"
+ "Added subscriber for key: %@... New count: %lu"
+ "Getting remote object for NowPlaying service..."
+ "No more NowPlaying users, disconnecting from service..."
+ "No service connection, ignore cancel for accessoryUID %@, requestID %@"
+ "No service connection, sending playback queue list not available..."
+ "NowPlaying XPC service connection invalidated!"
+ "NowPlaying XPC service error: %@"
+ "NowPlaying XPC service interrupted (service crash). Will reconnect after delay..."
+ "Received mediaItemAttributes update from service: %@"
+ "Received playbackAttributes update from service: %@"
+ "Received playbackQueueListChanged from service"
+ "Received playbackQueueListInfoResponse from service: %@ requestID: %@ info: %@"
+ "Removed subscriber for key: %@... New count: %lu"
+ "Resync subscriber list result: %d"
+ "Resyncing subscriber list after service restart..."
+ "Set playback elapsed time result: %d"
+ "Set playback queue index result: %d"
+ "Update subscriber list result: %d"
+ "com.apple.accessories.now-playing-client"
+ "com.apple.accessories.now-playing-feature"
- "#"
- "#16@0:8"
- "#Artwork (Triggered) Update mediaItemArtwork result: %d"
- "(Triggered) Update mediaItemAttributes result: %d"
- "(Triggered) Update playbackAttributes result: %d"
- ".cxx_destruct"
- "@\"<AccessoryNowPlayingClientProtocol>\""
- "@\"<AccessoryNowPlayingXPCServerProtocol>\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AccessoryNowPlayingClient"
- "AccessoryNowPlayingXPCClientProtocol"
- "AccessoryNowPlayingXPCServerProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Connecting to XPC server..."
- "Getting remote object..."
- "NSObject"
- "Not shouldSendPlaybackQueueList, ignore! %@, requestID=%@"
- "Q16@0:8"
- "Received mediaItemArtwork from client: %lu bytes"
- "Received subscriberList update: %@"
- "Server availability changed! State: %d"
- "Server available: %d"
- "T#,R"
- "T@\"<AccessoryNowPlayingClientProtocol>\",W,N,V_delegate"
- "T@\"<AccessoryNowPlayingXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"NSSet\",&,V_subscriberList"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "TB,N,V_shouldSendArtwork"
- "TB,R,N"
- "TQ,R"
- "Trying to connect to server..."
- "Update mediaItemAttributes result: %d"
- "Update playbackAttributes result: %d"
- "Vv16@0:8"
- "XPC connection error: %@"
- "XPC connection interrupted!"
- "XPC connection invalidated!"
- "^{_NSZone=}16@0:8"
- "_delegate"
- "_remoteObject"
- "_serverConnection"
- "_shouldSendArtwork"
- "_subscriberList"
- "autorelease"
- "cancelRequestPlaybackQueueListInfo:requestID:"
- "class"
- "com.apple.accessories.now-playing"
- "com.apple.accessories.now-playing.availability-changed"
- "conformsToProtocol:"
- "connectToServer"
- "containsObject:"
- "count"
- "currentMediaItemArtwork"
- "currentMediaItemAttributes"
- "currentPlaybackAttributes"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "hash"
- "init"
- "initConnection:"
- "initWithDelegate:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "mediaItemArtworkDidChange"
- "mediaItemArtworkHasChanged:withReply:"
- "mediaItemAttributesDidChange:"
- "mediaItemAttributesHaveChanged:withReply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "playbackAttributesDidChange:"
- "playbackAttributesHaveChanged:withReply:"
- "playbackQueueListChanged"
- "playbackQueueListDidChange"
- "playbackQueueListInfoResponse:requestID:info:"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "requestPlaybackQueueListInfo:requestID:startIndex:upToCount:infoMask:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverConnection"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setPlaybackElapsedTime:"
- "setPlaybackElapsedTime:withReply:"
- "setPlaybackQueueIndex:"
- "setPlaybackQueueIndex:withReply:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setServerConnection:"
- "setShouldSendArtwork:"
- "setSubscriberList:"
- "setWithArray:"
- "shouldSendArtwork"
- "shouldSendArtworkDidChange:"
- "shouldSendPlaybackQueueList"
- "shouldStayConnected: %d"
- "subscriberList"
- "superclass"
- "triggerMediaItemArtworkUpdateWithReply:"
- "triggerMediaItemAttributesUpdateWithReply:"
- "triggerPlaybackAttributesUpdateWithReply:"
- "updateSubscriberList:WithReply:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v32@0:8@\"NSArray\"16@?<v@?B>24"
- "v32@0:8@\"NSData\"16@?<v@?B>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B>24"
- "v32@0:8@\"NSNumber\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@16@24@32"
- "v44@0:8@\"NSString\"16@\"NSString\"24I32I36I40"
- "v44@0:8@16@24I32I36I40"
- "zone"

```

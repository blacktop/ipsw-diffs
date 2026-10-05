## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-1005.8.1.0.0
-  __TEXT.__text: 0x2399f0
-  __TEXT.__objc_methlist: 0x7ec
-  __TEXT.__cstring: 0x8f9e4
+1005.12.1.0.0
+  __TEXT.__text: 0x23b074
+  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__cstring: 0x8ff1c
   __TEXT.__const: 0x6190
-  __TEXT.__gcc_except_tab: 0xaa4
+  __TEXT.__gcc_except_tab: 0xaf4
   __TEXT.__dlopen_cstrs: 0x61a
   __TEXT.__oslogstring: 0x1009
-  __TEXT.__unwind_info: 0x9230
+  __TEXT.__unwind_info: 0x92c8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7700
+  __DATA_CONST.__const: 0x77c8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb18
+  __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x23b0
-  __AUTH_CONST.__const: 0x77b0
-  __AUTH_CONST.__cfstring: 0x149e0
+  __DATA_CONST.__got: 0x23c0
+  __AUTH_CONST.__const: 0x77d0
+  __AUTH_CONST.__cfstring: 0x14a60
   __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x150

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11460
-  Symbols:   8677
-  CStrings:  11659
+  Functions: 11496
+  Symbols:   8711
+  CStrings:  11672
 
Symbols:
+ -[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]
+ -[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeer:groupID:]
+ -[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeersForGroup:peers:]
+ -[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]
+ GCC_except_table131
+ GCC_except_table31
+ GCC_except_table33
+ _APEndpointPayloadRequiresCompositionRefresh
+ _APPairingClientCoreUtilsCopyMigratableUngroupedPeers
+ _APPairingClientCoreUtilsCreateOrphanedPeersFromGroupInfo
+ _APPairingClientCoreUtilsMigrateUngroupedPeers
+ _APPairingClientCoreUtilsPatchUnpairedPeerWithGroupID
+ _APSAudioHoseMetricCollectorSetSenderRTMetrics
+ _FigCFSetGetCount
+ _FigSignalErrorAtGM
+ ___60-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]_block_invoke
+ ___63-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]_block_invoke
+ ___APPairingClientCoreUtilsCreateOrphanedPeersFromGroupInfo_block_invoke
+ ___APPairingClientCoreUtilsCreateOrphanedPeersFromGroupInfo_block_invoke_2
+ ___APPairingClientCoreUtilsMigrateUngroupedPeers_block_invoke
+ ___block_descriptor_40_e8_32o_e15_v24?0r^v8r^v16ls32l8
+ ___block_descriptor_48_e8_32o40o_e29_v32?0"CUPairedPeer"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32o40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32o40r_e34_v32?0"NSString"8"NSArray"16^B24ls32l8r40l8
+ ___coreUtilsPairing_updatePairingGroupInfoIfNeeded_block_invoke_2
+ ___endpointCluster_reconcileResponsiveAudioTransports_block_invoke
+ ___manager_create_block_invoke_6
+ _endpointCluster_activateSubEndpointForcingTransportIfNeeded
+ _endpointCluster_copyActivatedSubEndpointsByTransportType
+ _endpointCluster_copyActivationOptionsForcingTransportType
+ _endpointCluster_copyForcedTransportForResponsiveAudio
+ _kAPEndpointAggregateCreationOptionKey_ClusterType
+ _kFigEndpointActivateOptionKey_ForcedTransportType
+ _kFigEndpointForcedTransportType_Infra
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x8
- GCC_except_table129
- _FigSignalErrorAt3
- _endpointCluster_getNumSubEndpointsActivated
CStrings:
+ "\t[indexed] identifier: %@ infoKeys: %@\n"
+ "\t[ungrouped] identifier: %@  publicKey: %@\n"
+ "%s signalled err=%d at <>:%d"
+ "-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]"
+ "-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]_block_invoke"
+ "-[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeer:groupID:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeersForGroup:peers:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]_block_invoke"
+ "1005.12.1"
+ "APPairingClientCoreUtilsPatchUnpairedPeerWithGroupID"
+ "Boolean APPairingClientCoreUtilsMigrateUngroupedPeers(void)"
+ "Failed to get all paired peers: %#m\n"
+ "Failed to get all paired peers; migration aborted\n"
+ "Failed to patch ungrouped peer %@ for migration\n"
+ "Failed to remove paired peer [%{ptr}]: %#m\n"
+ "Failed to save migrated peer %@ — migration skipped: %#m\n"
+ "Getting all paired peers\n"
+ "Got %d paired peers\n"
+ "Migrated ungrouped peer %@ to group-indexed entry\n"
+ "No group-indexed peers found; nothing to migrate\n"
+ "OSStatus endpointCluster_activateSubEndpointForcingTransportIfNeeded(FigEndpointRef, FigEndpointRef)"
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke"
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_3"
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_6"
+ "Removed paired peer [%{ptr}]: %@\n"
+ "Removing paired peer [%{ptr}]: %@\n"
+ "Ungrouped peer migration %s\n"
+ "Ungrouped peer migration already done; skipping\n"
+ "Ungrouped peer migration started\n"
+ "[%{ptr}] Forcing %@ transport for activating subEndpoint [%{ptr}]"
+ "[%{ptr}] RA Reconcile: Migrating subEndpoint [%{ptr}] from NAN to Infra"
+ "[%{ptr}] RA Reconcile: Reactivate subEndpoint [%{ptr}] error: %m"
+ "[%{ptr}] RA Reconcile: all subEndpoints already using %@"
+ "[%{ptr}] Removing orphaned pairing group peer [%{ptr}] with identifier %@\n"
+ "[%{ptr}] SubEndpointStream(%{ptr}) is dissociated, excluding it from aggregate capabilities"
+ "aggregateClusterType"
+ "com.apple.airplay.pairing-migration"
+ "endpointCluster_copyActivatedSubEndpointsByTransportType"
+ "endpointCluster_copyActivationOptionsForcingTransportType"
+ "endpointCluster_reconcileResponsiveAudioTransports"
+ "endpointCluster_reconcileResponsiveAudioTransports_block_invoke"
+ "group info member count: %lu\n"
+ "group-indexed peers: %lu\n"
+ "manager_create_block_invoke_6"
+ "senderClusterType"
+ "senderOSVersion"
+ "ungrouped peers to migrate: %lu\n"
+ "ungroupedPeersMigrationDone"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "void coreUtilsPairing_updatePairingGroupInfoIfNeeded(APPairingClientRef, CFDictionaryRef, CUPairedPeer *)_block_invoke_2"
+ "void endpointCluster_reconcileResponsiveAudioTransports(FigEndpointRef, CFDictionaryRef *)"
+ "void endpointCluster_reconcileResponsiveAudioTransports(FigEndpointRef, CFDictionaryRef *)_block_invoke"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "1005.8.1"
- "APAudioEngineBufferedAdapter.c"
- "APEndpoint.m"
- "APEndpointPlaybackSessionRemoteControl.m"
- "APEndpointStreamAggregateAudio.c"
- "APVirtualDisplayTestSink.c"
- "Action not supported"
- "Allocation error"
- "Cannot register path"
- "Failed allocating audio buffer"
- "Failed to create deep copy"
- "Failed to de-serialize"
- "Failed to serialize"
- "Item is NULL"
- "No data in response"
- "No incoming message"
- "No matched request found"
- "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_2"
- "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_4"
- "Object invalidated"
- "[%{ptr}] Activate SubEndpoint [%{ptr}] on reconcile transports failed %m"
- "[%{ptr}] RA stereo pair transport mismatch detected, [%{ptr}] on %@, [%{ptr}] on %@, forcing [%{ptr}] to Infra"
- "[%{ptr}] RA stereo pair, no transport mismatch [%{ptr}] on %@, [%{ptr}] on %@"
- "alloc failed"
- "can't find valid video track"
- "endpointCluster_reconcileSubEndpointTransportsIfNeeded"
- "err"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kCMBaseObjectError_ValueNotAvailable"
- "kFigEndpointError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_InvalidParameter"
- "kFigEndpointStreamAudioEngineError_AllocationFailed"
- "manager_create_block_invoke_5"
- "messageID is missing in response event"
- "type is missing in response event"
- "void endpointCluster_reconcileSubEndpointTransportsIfNeeded(FigEndpointRef, FigEndpointRef)"
```

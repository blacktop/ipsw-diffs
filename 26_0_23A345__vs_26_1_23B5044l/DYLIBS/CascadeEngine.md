## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-200.1.0.0.0
-  __TEXT.__text: 0x20778
+200.4.0.2.0
+  __TEXT.__text: 0x20b5c
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x186c
+  __TEXT.__objc_methlist: 0x189c
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x7ac
-  __TEXT.__cstring: 0x12d5
-  __TEXT.__oslogstring: 0x37bc
+  __TEXT.__gcc_except_tab: 0x7dc
+  __TEXT.__cstring: 0x13a0
+  __TEXT.__oslogstring: 0x37f9
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x890
-  __TEXT.__objc_classname: 0x46f
-  __TEXT.__objc_methname: 0x5526
-  __TEXT.__objc_methtype: 0x1066
-  __TEXT.__objc_stubs: 0x46a0
+  __TEXT.__unwind_info: 0x888
+  __TEXT.__objc_classname: 0x465
+  __TEXT.__objc_methname: 0x5683
+  __TEXT.__objc_methtype: 0x109c
+  __TEXT.__objc_stubs: 0x4760
   __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0xb38
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f0
+  __DATA_CONST.__objc_selrefs: 0x1420
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x12e0
-  __AUTH_CONST.__objc_const: 0x3330
+  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__objc_const: 0x3350
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x298
-  __DATA.__data: 0x720
+  __DATA.__objc_ivar: 0x29c
+  __DATA.__data: 0x6c0
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5648FD0E-4662-30CA-BFBE-A09628361F40
-  Functions: 712
-  Symbols:   2820
-  CStrings:  1686
+  UUID: C7D7A5E1-1467-3FB9-97A8-93A76D6A936E
+  Functions: 714
+  Symbols:   2825
+  CStrings:  1713
 
Symbols:
+ -[CCRapportManager discoveryControlFlagsForDevicePlatform:]
+ -[CCRapportManager discoveryControlFlagsForDevicePlatform:].cold.1
+ -[CCRapportManager fileTransferSessionCacheKeyWithServerDevice:clientTargetDeviceID:]
+ -[CCRapportManager fulfillFileTransferSessionFromClientDevice:withTargetDeviceID:peerPublicKey:error:]
+ -[CCRapportManager initiateFileTransferSessionWithServerDevice:error:]
+ -[CCRapportManager isNoAWDLDiscoverySupportedForDevicePlatform:]
+ -[CCRapportSyncEngine didRemoteDeviceInitiateSyncWithMessage:beforeLocalInteraction:]
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:]
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:].cold.1
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:].cold.2
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:].cold.3
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:].cold.4
+ -[CCRapportSyncInteraction initiatingRequestSentWalltime]
+ -[CCRapportSyncInteraction setInitiatingRequestSentWalltime:]
+ -[CCRapportSyncSession _setNextInteractionTimeout:]
+ -[CCRapportSyncSession cancelInteractionType:withDevice:dueToError:]
+ -[CCRapportSyncSession cancelInteractionType:withDevice:dueToError:].cold.1
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table40
+ _OBJC_IVAR_$_CCRapportSyncInteraction._initiatingRequestSentWalltime
+ ___102-[CCRapportManager fulfillFileTransferSessionFromClientDevice:withTargetDeviceID:peerPublicKey:error:]_block_invoke
+ ___102-[CCRapportManager fulfillFileTransferSessionFromClientDevice:withTargetDeviceID:peerPublicKey:error:]_block_invoke.cold.1
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.70
+ ___51-[CCRapportSyncSession _setNextInteractionTimeout:]_block_invoke
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.83
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.88
+ ___block_literal_global.90
+ ___block_literal_global.92
+ _objc_msgSend$_setNextInteractionTimeout:
+ _objc_msgSend$cancelInteractionType:withDevice:dueToError:
+ _objc_msgSend$didRemoteDeviceInitiateSyncWithMessage:beforeLocalInteraction:
+ _objc_msgSend$discoveryControlFlagsForDevicePlatform:
+ _objc_msgSend$fileTransferSessionCacheKeyWithServerDevice:clientTargetDeviceID:
+ _objc_msgSend$fulfillFileTransferSessionFromClientDevice:withTargetDeviceID:peerPublicKey:error:
+ _objc_msgSend$initiateFileTransferSessionWithServerDevice:error:
+ _objc_msgSend$initiatingRequestSentWalltime
+ _objc_msgSend$isNoAWDLDiscoverySupportedForDevicePlatform:
+ _objc_msgSend$setInitiatingRequestSentWalltime:
+ _objc_msgSend$validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:
- -[CCRapportDevice copyWithZone:]
- -[CCRapportManager buildFileTransferSessionWithTargetDeviceIdentifier:]
- -[CCRapportManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.1
- -[CCRapportManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.2
- -[CCRapportManager createDiscoveryClientIfNotExists].cold.1
- -[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]
- -[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.1
- -[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.2
- -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:]
- -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:].cold.1
- -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:].cold.2
- -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:].cold.3
- -[CCRapportSyncSession _setNextInteractionTimeout]
- -[CCRapportSyncSession cancelInteractionType:withDevice:error:]
- -[CCRapportSyncSession cancelInteractionType:withDevice:error:].cold.1
- GCC_except_table102
- GCC_except_table103
- GCC_except_table108
- GCC_except_table111
- GCC_except_table12
- GCC_except_table24
- GCC_except_table31
- GCC_except_table32
- GCC_except_table38
- GCC_except_table39
- GCC_except_table5
- GCC_except_table68
- GCC_except_table99
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
- __OBJC_LABEL_PROTOCOL_$_NSCopying
- __OBJC_PROTOCOL_$_NSCopying
- ___106-[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]_block_invoke
- ___106-[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]_block_invoke.cold.1
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.64
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.cold.2
- ___50-[CCRapportSyncSession _setNextInteractionTimeout]_block_invoke
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.80
- ___block_literal_global.85
- ___block_literal_global.87
- ___block_literal_global.89
- _objc_msgSend$_setNextInteractionTimeout
- _objc_msgSend$buildFileTransferSessionWithTargetDeviceIdentifier:
- _objc_msgSend$cancelInteractionType:withDevice:error:
- _objc_msgSend$initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:
- _objc_msgSend$validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:
CStrings:
+ " NOT"
+ "%@: Remote device DID%@ initiate sync (%lf) prior to our local interaction (%lf): %@"
+ "%@: Responding with %@ due to existing interaction with device: %@"
+ "%@: Response from set discovery request (%@) - yielding to remote device: %@"
+ "%@: Yielding to device which started sync before us; canceling client interaction: %@"
+ "%@: failed to request incoming file transfer session: %@"
+ "%@: preparing outgoing file transfer session to send deltas for set %@ from device %@"
+ "%@:%@"
+ "%lu. [%@] %@ %@ %@%@"
+ "->"
+ "<-"
+ "@48@0:8@16@24@32^@40"
+ "B24@0:8q16"
+ "Failed to prepare Rapport FileTransferSession"
+ "Missing Rapport FileTransferTargetDeviceID"
+ "Q24@0:8q16"
+ "Remote device already sent an initiating request to sync"
+ "Sync session timeout %@ after %lf seconds waiting to run interactions"
+ "Td,N,V_initiatingRequestSentWalltime"
+ "YieldToRemote"
+ "_initiatingRequestSentWalltime"
+ "_setNextInteractionTimeout:"
+ "cancelInteractionType:withDevice:dueToError:"
+ "didRemoteDeviceInitiateSyncWithMessage:beforeLocalInteraction:"
+ "discoveryControlFlagsForDevicePlatform:"
+ "fileTransferSessionCacheKeyWithServerDevice:clientTargetDeviceID:"
+ "fulfillFileTransferSessionFromClientDevice:withTargetDeviceID:peerPublicKey:error:"
+ "initiateFileTransferSessionWithServerDevice:error:"
+ "initiatingRequestSentWalltime"
+ "isNoAWDLDiscoverySupportedForDevicePlatform:"
+ "localDevice: %@ missing fileTransferTargetID"
+ "setInitiatingRequestSentWalltime:"
+ "v24@0:8d16"
+ "validateInRequest:inOptions:inResponseHandler:isInitiatingRequest:outPlatform:"
- "%@: buildFileTransferSessionWithTargetDeviceIdentifier %@"
- "%@: cannot build file transfer session without localDevice fileTransferTargetID: %@"
- "%@: failed to prepare file transfer template %@"
- "%@: initiateFileTransferSesionBackToTargetDeviceWithIdentifier %@"
- "%@: initiating file transfer session to send deltas for set %@ from device %@"
- "%@: peer device is already syncing so will not reciprocate: %@"
- "%lu. [%@] %@ -> %@%@"
- "Already syncing"
- "Completing sync session %@ after %lf seconds waiting to run interactions"
- "NSCopying"
- "_setNextInteractionTimeout"
- "buildFileTransferSessionWithTargetDeviceIdentifier:"
- "cancelInteractionType:withDevice:error:"
- "initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:"
- "validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:"

```

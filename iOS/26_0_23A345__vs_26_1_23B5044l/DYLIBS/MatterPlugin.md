## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-68.1.1.0.0
-  __TEXT.__text: 0x47bdc
+70.0.0.0.0
+  __TEXT.__text: 0x4a0fc
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x473c
+  __TEXT.__objc_methlist: 0x489c
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x12a7
-  __TEXT.__oslogstring: 0x5744
-  __TEXT.__gcc_except_tab: 0x1cd0
-  __TEXT.__unwind_info: 0x1138
-  __TEXT.__objc_classname: 0x9a0
-  __TEXT.__objc_methname: 0x797d
-  __TEXT.__objc_methtype: 0x15ed
-  __TEXT.__objc_stubs: 0x5d40
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x998
-  __DATA_CONST.__objc_classlist: 0x218
+  __TEXT.__cstring: 0x13a1
+  __TEXT.__oslogstring: 0x59b5
+  __TEXT.__gcc_except_tab: 0x1ec4
+  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__objc_classname: 0x9be
+  __TEXT.__objc_methname: 0x7b3e
+  __TEXT.__objc_methtype: 0x15fd
+  __TEXT.__objc_stubs: 0x5f40
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__const: 0x948
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c30
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x1cb0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x67f8
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__objc_const: 0x6a18
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x374
+  __AUTH.__objc_data: 0x1450
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0x600
   __DATA.__bss: 0x80
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Matter.framework/Matter

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A44467DD-6A25-397B-84B6-4314307FB9F9
-  Functions: 1624
-  Symbols:   5214
-  CStrings:  2322
+  UUID: 4DA7E765-F1A5-33EA-A4F9-C4E233DCC975
+  Functions: 1667
+  Symbols:   5341
+  CStrings:  2372
 
Symbols:
+ +[MTRPluginClient isRemoteModeForHome:]
+ +[MTRPluginRemoteSessionManager sharedInstance]
+ +[MTRPluginRemoteSessionManager sharedInstance].cold.1
+ -[MTRPluginClient forwardInvocation:]
+ -[MTRPluginProtobufMessage clientSessionID]
+ -[MTRPluginProtobufMessage setClientSessionID:]
+ -[MTRPluginRemoteClient homeUUID]
+ -[MTRPluginRemoteClient initWithHomeUUID:queue:]
+ -[MTRPluginRemoteClient registeredNodeIDs]
+ -[MTRPluginRemoteClient sessionID]
+ -[MTRPluginRemoteClient setHomeUUID:]
+ -[MTRPluginRemoteClient setRegisteredNodeIDs:]
+ -[MTRPluginRemoteClient setSessionID:]
+ -[MTRPluginRemoteSessionManager .cxx_destruct]
+ -[MTRPluginRemoteSessionManager _recomputeStateForcingRegistration:]
+ -[MTRPluginRemoteSessionManager addPluginClient:]
+ -[MTRPluginRemoteSessionManager bufferedExecutionTimers]
+ -[MTRPluginRemoteSessionManager description]
+ -[MTRPluginRemoteSessionManager device:receivedAttributeReport:]
+ -[MTRPluginRemoteSessionManager device:receivedAttributeReport:].cold.1
+ -[MTRPluginRemoteSessionManager device:receivedEventReport:]
+ -[MTRPluginRemoteSessionManager device:receivedEventReport:].cold.1
+ -[MTRPluginRemoteSessionManager forwardInvocation:]
+ -[MTRPluginRemoteSessionManager init]
+ -[MTRPluginRemoteSessionManager pluginClients]
+ -[MTRPluginRemoteSessionManager queue]
+ -[MTRPluginRemoteSessionManager recomputeStateForcingRegistration:]
+ -[MTRPluginRemoteSessionManager remoteSessions]
+ -[MTRPluginRemoteSessionManager removePluginClient:]
+ -[MTRPluginRemoteSessionManager respondsToSelector:]
+ -[MTRPluginRemoteSessionManager setBufferedExecutionTimers:]
+ -[MTRPluginRemoteSessionManager setPluginClients:]
+ -[MTRPluginRemoteSessionManager setQueue:]
+ -[MTRPluginRemoteSessionManager setRemoteSessions:]
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table32
+ _MTRAssociateControllerUUIDWithClientInfo
+ _MTRAssociateNodeIDWithHomeUUID
+ _MTRGetAssociatedClientSessionIDForControllerUUID
+ _MTRGetAssociatedClientTypeForControllerUUID
+ _MTRGetAssociatedHomeUUIDForNodeID
+ _OBJC_CLASS_$_MTRPluginRemoteSessionManager
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_IVAR_$_MTRPluginProtobufMessage._clientSessionID
+ _OBJC_IVAR_$_MTRPluginRemoteClient._homeUUID
+ _OBJC_IVAR_$_MTRPluginRemoteClient._registeredNodeIDs
+ _OBJC_IVAR_$_MTRPluginRemoteClient._sessionID
+ _OBJC_IVAR_$_MTRPluginRemoteSessionManager._bufferedExecutionTimers
+ _OBJC_IVAR_$_MTRPluginRemoteSessionManager._pluginClients
+ _OBJC_IVAR_$_MTRPluginRemoteSessionManager._queue
+ _OBJC_IVAR_$_MTRPluginRemoteSessionManager._remoteSessions
+ _OBJC_METACLASS_$_MTRPluginRemoteSessionManager
+ __OBJC_$_CLASS_METHODS_MTRPluginClient
+ __OBJC_$_CLASS_METHODS_MTRPluginRemoteSessionManager
+ __OBJC_$_INSTANCE_METHODS_MTRPluginRemoteSessionManager
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginRemoteSessionManager
+ __OBJC_$_PROP_LIST_MTRPluginRemoteSessionManager
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginRemoteSessionManager
+ __OBJC_CLASS_RO_$_MTRPluginRemoteSessionManager
+ __OBJC_METACLASS_RO_$_MTRPluginRemoteSessionManager
+ __OBJC_PROTOCOL_REFERENCE_$_MTRXPCClientProtocol_MTRDevice
+ __OBJC_PROTOCOL_REFERENCE_$_MTRXPCClientProtocol_MTRDeviceController
+ ___116-[MTRPluginRemoteClient deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:]_block_invoke.71
+ ___205-[MTRPluginLocalClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.35
+ ___206-[MTRPluginRemoteClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.82
+ ___47+[MTRPluginRemoteSessionManager sharedInstance]_block_invoke
+ ___49-[MTRPluginRemoteSessionManager addPluginClient:]_block_invoke
+ ___51-[MTRPluginRemoteSessionManager forwardInvocation:]_block_invoke
+ ___51-[MTRPluginRemoteSessionManager forwardInvocation:]_block_invoke.143
+ ___51-[MTRPluginRemoteSessionManager forwardInvocation:]_block_invoke.154
+ ___52-[MTRPluginRemoteSessionManager removePluginClient:]_block_invoke
+ ___60-[MTRPluginRemoteSessionManager device:receivedEventReport:]_block_invoke
+ ___64-[MTRPluginRemoteSessionManager device:receivedAttributeReport:]_block_invoke
+ ___67-[MTRPluginRemoteClient deviceController:nodeID:getStateWithReply:]_block_invoke.66
+ ___67-[MTRPluginRemoteSessionManager recomputeStateForcingRegistration:]_block_invoke
+ ___68-[MTRPluginRemoteSessionManager _recomputeStateForcingRegistration:]_block_invoke
+ ___72-[MTRPluginRemoteClient deviceController:updateControllerConfiguration:]_block_invoke.63
+ ___74-[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.40
+ ___75-[MTRPluginRemoteClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.86
+ ___78-[MTRPluginRemoteClient deviceController:nodeID:readAttributePaths:withReply:]_block_invoke.75
+ ___79-[MTRPluginRemoteClient deviceController:nodeID:getDeviceCachePrimedWithReply:]_block_invoke.67
+ ___80-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedStartTimeWithReply:]_block_invoke.68
+ ___85-[MTRPluginLocalClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.42
+ ___86-[MTRPluginRemoteClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.89
+ ___90-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:]_block_invoke.69
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.108
+ ___block_literal_global.27
+ ___block_literal_global.99
+ _objc_msgSend$_recomputeStateForcingRegistration:
+ _objc_msgSend$addPluginClient:
+ _objc_msgSend$bufferedExecutionTimers
+ _objc_msgSend$clientSessionID
+ _objc_msgSend$getArgument:atIndex:
+ _objc_msgSend$initWithHomeUUID:queue:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isRemoteModeForHome:
+ _objc_msgSend$pluginClients
+ _objc_msgSend$raise:format:
+ _objc_msgSend$recomputeStateForcingRegistration:
+ _objc_msgSend$remoteSessions
+ _objc_msgSend$removePluginClient:
+ _objc_msgSend$setBufferedExecutionTimers:
+ _objc_msgSend$setClientSessionID:
+ _objc_msgSend$setPluginClients:
+ _objc_msgSend$setRemoteSessions:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$weakObjectsHashTable
+ _swizzlePrewarm.onceToken.106
- -[MTRPluginClient setUpdateControllerConfigurationTimer:]
- -[MTRPluginClient updateControllerConfigurationTimer]
- -[MTRPluginRemoteClient client]
- -[MTRPluginRemoteClient initWithClient:queue:]
- -[MTRPluginRemoteClient setClient:]
- _OBJC_IVAR_$_MTRPluginClient._updateControllerConfigurationTimer
- _OBJC_IVAR_$_MTRPluginRemoteClient._client
- ___116-[MTRPluginRemoteClient deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:]_block_invoke.68
- ___205-[MTRPluginLocalClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.36
- ___206-[MTRPluginRemoteClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.79
- ___42-[MTRPluginLocalClient _unregisterDevice:]_block_invoke
- ___57-[MTRPluginLocalClient _registerDevice:addedViaDelegate:]_block_invoke.27
- ___67-[MTRPluginRemoteClient deviceController:nodeID:getStateWithReply:]_block_invoke.63
- ___72-[MTRPluginRemoteClient deviceController:updateControllerConfiguration:]_block_invoke.61
- ___74-[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.41
- ___75-[MTRPluginRemoteClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.83
- ___78-[MTRPluginRemoteClient deviceController:nodeID:readAttributePaths:withReply:]_block_invoke.72
- ___79-[MTRPluginRemoteClient deviceController:nodeID:getDeviceCachePrimedWithReply:]_block_invoke.64
- ___80-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedStartTimeWithReply:]_block_invoke.65
- ___85-[MTRPluginLocalClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.43
- ___86-[MTRPluginRemoteClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.86
- ___90-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:]_block_invoke.66
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.105
- ___block_literal_global.24
- ___block_literal_global.96
- _objc_msgSend$initWithClient:queue:
- _objc_msgSend$setUpdateControllerConfigurationTimer:
- _objc_msgSend$updateControllerConfigurationTimer
- _swizzlePrewarm.onceToken.103
CStrings:
+ "%@ => controller: %@ self.registeredNodeIDs: %@"
+ "%@ Comparing new node IDs: %@, vs last registered node IDs: %@ for home %@"
+ "%@ Creating new remote session for home %@ "
+ "%@ Missing homeUUID for pluginClient %@"
+ "%@ Missing remote session setup for home %@ "
+ "%@ Recomputing state"
+ "%@ Scheduling Recomputing state"
+ "%@ adding new pluginClient %@"
+ "%@ home %@ has already registered set of nodeIDs with resident"
+ "%@ home %@ has new set of nodeIDs (%@), registering configuration with resident, forceRegistration: %@"
+ "%@ remote sessions manager created"
+ "%@ removing pluginClient %@"
+ "<%@: %p, clients#: %ld, sessions #: %ld>"
+ "<%@: %p, homeUUID: %@ sessionID: %@>"
+ "@\"<MTRXPCServerProtocol>\""
+ "@\"NSHashTable\""
+ "Exception %@ forwarding method: %@"
+ "Exception %@ forwarding method: device:receivedAttributeReport:"
+ "Exception %@ forwarding method: device:receivedEventReport:"
+ "Exception forwarding MTRXPCServerProtocol method: %@"
+ "Invalid method format"
+ "MTRPluginRemoteSessionManager"
+ "Method argument missing homeUUID for node ID"
+ "Method format does not contain expected controller UUID"
+ "Method format does not contain expected node ID"
+ "Missing associated object"
+ "T@\"<MTRXPCServerProtocol>\",&,V_remoteClient"
+ "T@\"NSHashTable\",&,V_pluginClients"
+ "T@\"NSMutableDictionary\",&,V_bufferedExecutionTimers"
+ "T@\"NSMutableDictionary\",&,V_remoteSessions"
+ "T@\"NSSet\",&,V_registeredNodeIDs"
+ "T@\"NSUUID\",&,V_clientSessionID"
+ "_bufferedExecutionTimers"
+ "_clientSessionID"
+ "_pluginClients"
+ "_recomputeStateForcingRegistration:"
+ "_remoteSessions"
+ "addPluginClient:"
+ "bufferedExecutionTimers"
+ "clientSessionID"
+ "getArgument:atIndex:"
+ "initWithHomeUUID:queue:"
+ "isEqualToSet:"
+ "isRemoteModeForHome:"
+ "pluginClients"
+ "raise:format:"
+ "recomputeStateForcingRegistration:"
+ "remoteSessions"
+ "removePluginClient:"
+ "setBufferedExecutionTimers:"
+ "setClientSessionID:"
+ "setPluginClients:"
+ "setRemoteSessions:"
+ "unionSet:"
+ "weakObjectsHashTable"
- "!"
- "%@ resuming remote server session for home %@ since running mode is remote"
- "%@ suspending remote server session for home %@ since running mode is local"
- "<%@: %p, clientType: %@>"
- "@\"MTRPluginRemoteClient\""
- "T@\"MTRPluginRemoteClient\",&,V_remoteClient"
- "T@\"NSObject<OS_dispatch_source>\",&,V_updateControllerConfigurationTimer"
- "_updateControllerConfigurationTimer"
- "initWithClient:queue:"
- "setUpdateControllerConfigurationTimer:"
- "updateControllerConfigurationTimer"

```

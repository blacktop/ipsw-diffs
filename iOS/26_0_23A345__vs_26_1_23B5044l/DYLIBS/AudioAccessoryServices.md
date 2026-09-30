## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-30.59.1.9.0
-  __TEXT.__text: 0x3febc
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x5244
+31.5.2.1.2
+  __TEXT.__text: 0x421b4
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x539c
   __TEXT.__const: 0x2a0
-  __TEXT.__gcc_except_tab: 0x1590
-  __TEXT.__cstring: 0xb91e
-  __TEXT.__unwind_info: 0x10b8
-  __TEXT.__objc_classname: 0x63c
-  __TEXT.__objc_methname: 0xb69f
-  __TEXT.__objc_methtype: 0x13ee
-  __TEXT.__objc_stubs: 0x5aa0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xe50
-  __DATA_CONST.__objc_classlist: 0x178
+  __TEXT.__gcc_except_tab: 0x15d0
+  __TEXT.__cstring: 0xc043
+  __TEXT.__unwind_info: 0x1160
+  __TEXT.__objc_classname: 0x65b
+  __TEXT.__objc_methname: 0xba6d
+  __TEXT.__objc_methtype: 0x1413
+  __TEXT.__objc_stubs: 0x5d40
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0xec8
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2450
+  __DATA_CONST.__objc_selrefs: 0x2528
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x2460
-  __AUTH_CONST.__objc_const: 0x95c0
-  __AUTH.__objc_data: 0x7d0
+  __DATA_CONST.__objc_superrefs: 0x130
+  __AUTH_CONST.__auth_got: 0x478
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__cfstring: 0x2500
+  __AUTH_CONST.__objc_const: 0x9790
+  __AUTH.__objc_data: 0x820
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x8e0
-  __DATA.__data: 0xd38
+  __DATA.__objc_ivar: 0x8fc
+  __DATA.__data: 0xda8
   __DATA.__common: 0x8
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x230
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A37D6D8B-BB23-3E41-94BD-CB6770796491
-  Functions: 2167
-  Symbols:   6563
-  CStrings:  4091
+  UUID: 6D2ED42E-0B77-3439-AB0C-F54615796253
+  Functions: 2228
+  Symbols:   6738
+  CStrings:  4179
 
Symbols:
+ +[AAControllerSharedXPCManager sharedManager]
+ +[AAControllerSharedXPCManager sharedManager].cold.1
+ -[AAController _activate:]
+ -[AAController _registerWithSharedManager:]
+ -[AAController _registerWithSharedManager:].cold.1
+ -[AAController _registerWithSharedManager:].cold.2
+ -[AAControllerSharedXPCManager .cxx_destruct]
+ -[AAControllerSharedXPCManager _activateSharedConnection]
+ -[AAControllerSharedXPCManager _activateSharedConnection].cold.1
+ -[AAControllerSharedXPCManager _distributeDeviceInfoArray:]
+ -[AAControllerSharedXPCManager _distributeXPCMessage:]
+ -[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]
+ -[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:].cold.1
+ -[AAControllerSharedXPCManager _handleActivationReply:]
+ -[AAControllerSharedXPCManager _handleActivationReply:].cold.1
+ -[AAControllerSharedXPCManager _handleActivationReply:].cold.2
+ -[AAControllerSharedXPCManager _handleConnectionInterruption]
+ -[AAControllerSharedXPCManager _handleConnectionInterruption].cold.1
+ -[AAControllerSharedXPCManager _handleConnectionInvalidation]
+ -[AAControllerSharedXPCManager _handleXPCEvent:]
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.1
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.2
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.3
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.4
+ -[AAControllerSharedXPCManager _invalidateConnection]
+ -[AAControllerSharedXPCManager _processPendingMessages]
+ -[AAControllerSharedXPCManager _processPendingMessages].cold.1
+ -[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]
+ -[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:].cold.1
+ -[AAControllerSharedXPCManager connectionActive]
+ -[AAControllerSharedXPCManager dealloc]
+ -[AAControllerSharedXPCManager init]
+ -[AAControllerSharedXPCManager init].cold.1
+ -[AAControllerSharedXPCManager invalidateCalled]
+ -[AAControllerSharedXPCManager invalidate]
+ -[AAControllerSharedXPCManager managerQueue]
+ -[AAControllerSharedXPCManager pendingMessages]
+ -[AAControllerSharedXPCManager registerController:completion:]
+ -[AAControllerSharedXPCManager registeredControllers]
+ -[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]
+ -[AAControllerSharedXPCManager setConnectionActive:]
+ -[AAControllerSharedXPCManager setInvalidateCalled:]
+ -[AAControllerSharedXPCManager setManagerQueue:]
+ -[AAControllerSharedXPCManager setPendingMessages:]
+ -[AAControllerSharedXPCManager setRegisteredControllers:]
+ -[AAControllerSharedXPCManager unregisterController:]
+ -[AudioAccessoryDevice farFieldSessionOnGoing]
+ -[AudioAccessoryDevice setFarFieldSessionOnGoing:]
+ GCC_except_table17
+ GCC_except_table2
+ _OBJC_CLASS_$_AAControllerSharedXPCManager
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_AAController._registeredWithManager
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._connectionActive
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._connectionEstablished
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._invalidateCalled
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._managerQueue
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._pendingActivations
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._pendingMessages
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._registeredControllers
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._sharedXPCConnection
+ _OBJC_IVAR_$_AudioAccessoryDevice._farFieldSessionOnGoing
+ _OBJC_METACLASS_$_AAControllerSharedXPCManager
+ __OBJC_$_CLASS_METHODS_AAControllerSharedXPCManager
+ __OBJC_$_INSTANCE_METHODS_AAControllerSharedXPCManager
+ __OBJC_$_INSTANCE_VARIABLES_AAControllerSharedXPCManager
+ __OBJC_$_PROP_LIST_AAControllerSharedXPCManager
+ __OBJC_CLASS_RO_$_AAControllerSharedXPCManager
+ __OBJC_METACLASS_RO_$_AAControllerSharedXPCManager
+ ___42-[AAControllerSharedXPCManager invalidate]_block_invoke
+ ___42-[AAControllerSharedXPCManager invalidate]_block_invoke.cold.1
+ ___43-[AAController _registerWithSharedManager:]_block_invoke
+ ___43-[AAController _registerWithSharedManager:]_block_invoke.cold.1
+ ___43-[AAController _registerWithSharedManager:]_block_invoke.cold.2
+ ___45+[AAControllerSharedXPCManager sharedManager]_block_invoke
+ ___53-[AAControllerSharedXPCManager unregisterController:]_block_invoke
+ ___53-[AAControllerSharedXPCManager unregisterController:]_block_invoke.cold.1
+ ___53-[AAControllerSharedXPCManager unregisterController:]_block_invoke.cold.2
+ ___54-[AAControllerSharedXPCManager _distributeXPCMessage:]_block_invoke
+ ___57-[AAControllerSharedXPCManager _activateSharedConnection]_block_invoke
+ ___59-[AAControllerSharedXPCManager _distributeDeviceInfoArray:]_block_invoke
+ ___59-[AAControllerSharedXPCManager _distributeDeviceInfoArray:]_block_invoke_2
+ ___61-[AAControllerSharedXPCManager _handleConnectionInterruption]_block_invoke
+ ___61-[AAControllerSharedXPCManager _handleConnectionInterruption]_block_invoke_2
+ ___61-[AAControllerSharedXPCManager _handleConnectionInvalidation]_block_invoke
+ ___62-[AAControllerSharedXPCManager registerController:completion:]_block_invoke
+ ___62-[AAControllerSharedXPCManager registerController:completion:]_block_invoke.cold.1
+ ___62-[AAControllerSharedXPCManager registerController:completion:]_block_invoke.cold.2
+ ___70-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]_block_invoke
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke.cold.1
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke_2
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke_3
+ ___75-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke
+ ___75-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2
+ ___75-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ _dispatch_after
+ _dispatch_time
+ _gLogCategory_AAControllerSharedXPCManager
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_activateSharedConnection
+ _objc_msgSend$_distributeDeviceInfoArray:
+ _objc_msgSend$_distributeXPCMessage:
+ _objc_msgSend$_ensureSharedConnectionWithCompletion:
+ _objc_msgSend$_handleActivationReply:
+ _objc_msgSend$_handleConnectionInterruption
+ _objc_msgSend$_handleConnectionInvalidation
+ _objc_msgSend$_handleXPCEvent:
+ _objc_msgSend$_invalidateConnection
+ _objc_msgSend$_processPendingMessages
+ _objc_msgSend$_registerWithSharedManager:
+ _objc_msgSend$_sendMessage:controller:queue:replyHandler:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$deviceInfoChangeHandler
+ _objc_msgSend$interruptionHandler
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$registerController:completion:
+ _objc_msgSend$sendMessage:controller:queue:replyHandler:
+ _objc_msgSend$setFarFieldSessionOnGoing:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$unregisterController:
+ _sharedManager.sOnceToken
+ _sharedManager.sSharedManager
+ _xpc_copy
- -[AAController _activateXPC:]
- -[AAController _activateXPC:].cold.1
- -[AAController _activateXPCCompleted:]
- -[AAController _activateXPCCompleted:].cold.1
- -[AAController _activateXPCCompleted:].cold.2
- -[AAController _activate]
- -[AAController _ensureXPCStarted]
- -[AAController coreBluetoothInternalFlag]
- -[AAController setCoreBluetoothInternalFlag:]
- -[AAController xpcReceivedMessage:].cold.2
- -[AAController xpcReceivedMessage:].cold.3
- GCC_except_table13
- _OBJC_IVAR_$_AAController._activateCompletion
- _OBJC_IVAR_$_AAController._coreBluetoothInternalFlag
- _OBJC_IVAR_$_AAController._xpcCnx
- ___29-[AAController _activateXPC:]_block_invoke
- ___33-[AAController _ensureXPCStarted]_block_invoke
- ___38-[AAController _activateXPCCompleted:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- _objc_msgSend$_activateXPCCompleted:
- _xpc_connection_copy_invalidation_reason
CStrings:
+ "### Register controller failed: %@"
+ "### Registration with manager failed: CID 0x%X, %@"
+ "### Shared XPC connection interrupted"
+ "### Shared XPC connection invalidated"
+ "### Shared connection activation failed: %@"
+ "-[AAController _registerWithSharedManager:]"
+ "-[AAController _registerWithSharedManager:]_block_invoke"
+ "-[AAController activateWithCompletion:]"
+ "-[AAControllerSharedXPCManager _activateSharedConnection]"
+ "-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]"
+ "-[AAControllerSharedXPCManager _handleActivationReply:]"
+ "-[AAControllerSharedXPCManager _handleConnectionInterruption]"
+ "-[AAControllerSharedXPCManager _handleXPCEvent:]"
+ "-[AAControllerSharedXPCManager _processPendingMessages]"
+ "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]"
+ "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2"
+ "-[AAControllerSharedXPCManager init]"
+ "-[AAControllerSharedXPCManager invalidate]_block_invoke"
+ "-[AAControllerSharedXPCManager registerController:completion:]_block_invoke"
+ "-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke"
+ "-[AAControllerSharedXPCManager unregisterController:]_block_invoke"
+ "@\"NSMutableSet\""
+ "AAControllerSharedXPCManager"
+ "AAControllerSharedXPCManager initialized"
+ "Activating shared XPC connection"
+ "Already registered with manager: CID 0x%X"
+ "Attempting to reestablish connection after interruption"
+ "Controller not registered"
+ "Establishing shared XPC connection"
+ "FFSOG"
+ "Invalidating AAControllerSharedXPCManager"
+ "Manager invalidated"
+ "No XPC connection"
+ "No more registered controllers, keeping connection alive for reuse"
+ "Processing %lu pending messages"
+ "Queued message for controller %@, pending count: %lu"
+ "Received XPC reply for controller %@: %@"
+ "Registered controller %@, total: %lu"
+ "Registered with manager: CID 0x%X"
+ "Registering with shared manager: CID 0x%X"
+ "Sending XPC message for controller %@: %@"
+ "Shared XPC connection activated successfully"
+ "T@\"NSMutableArray\",&,N,V_pendingMessages"
+ "T@\"NSMutableSet\",&,N,V_registeredControllers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_managerQueue"
+ "TB,N,V_connectionActive"
+ "TB,N,V_invalidateCalled"
+ "Tc,N,V_farFieldSessionOnGoing"
+ "Unregistered controller %@, remaining: %lu"
+ "_activateSharedConnection"
+ "_connectionActive"
+ "_connectionEstablished"
+ "_distributeDeviceInfoArray:"
+ "_distributeXPCMessage:"
+ "_ensureSharedConnectionWithCompletion:"
+ "_farFieldSessionOnGoing"
+ "_handleActivationReply:"
+ "_handleConnectionInterruption"
+ "_handleConnectionInvalidation"
+ "_handleXPCEvent:"
+ "_invalidateConnection"
+ "_managerQueue"
+ "_pendingActivations"
+ "_pendingMessages"
+ "_processPendingMessages"
+ "_registerWithSharedManager:"
+ "_registeredControllers"
+ "_registeredWithManager"
+ "_sendMessage:controller:queue:replyHandler:"
+ "_sharedXPCConnection"
+ "com.apple.AAControllerSharedXPCManager"
+ "connectionActive"
+ "containsObject:"
+ "controller"
+ "farFieldSessionOnGoing"
+ "ffsog %s, "
+ "invalidateCalled"
+ "managerQueue"
+ "objectForKey:"
+ "pendingMessages"
+ "queue"
+ "registerController:completion:"
+ "registeredControllers"
+ "replyHandler"
+ "request"
+ "sendMessage:controller:queue:replyHandler:"
+ "setConnectionActive:"
+ "setFarFieldSessionOnGoing:"
+ "setInvalidateCalled:"
+ "setManagerQueue:"
+ "setPendingMessages:"
+ "setRegisteredControllers:"
+ "sharedManager"
+ "unregisterController:"
+ "v48@0:8@16@24@32@?40"
- "### Activate failed: CID 0x%X, %@"
- "### Invalidated unexpectedly for reason %s"
- "-[AAController _activateXPC:]"
- "-[AAController _activateXPCCompleted:]"
- "-[AAController _activate]"
- "Activate: CID 0x%X"
- "Activated: CID 0x%X"
- "Re-activate: CID 0x%X"
- "TI,N,V_coreBluetoothInternalFlag"
- "_activateXPCCompleted:"
- "_coreBluetoothInternalFlag"
- "coreBluetoothInternalFlag"
- "setCoreBluetoothInternalFlag:"

```

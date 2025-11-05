## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/Versions/A/SoftwareUpdateCoreConnect`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0xc5d4
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x6b4
+2171.101.1.0.0
+  __TEXT.__text: 0xd77c
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_methlist: 0x9c8
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__cstring: 0xaf7
-  __TEXT.__oslogstring: 0x236f
-  __TEXT.__unwind_info: 0x2e0
-  __TEXT.__objc_classname: 0x197
-  __TEXT.__objc_methname: 0x1962
-  __TEXT.__objc_methtype: 0x50d
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__gcc_except_tab: 0x404
+  __TEXT.__cstring: 0xb6b
+  __TEXT.__oslogstring: 0x260d
+  __TEXT.__unwind_info: 0x340
+  __TEXT.__objc_classname: 0x1ac
+  __TEXT.__objc_methname: 0x1b8b
+  __TEXT.__objc_methtype: 0x5b3
+  __TEXT.__objc_stubs: 0x12a0
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x38
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x560
+  __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x14f8
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xac
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__const: 0x410
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x12d8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0xc4
   __DATA.__data: 0x360
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A284EA69-43C8-383E-B9BF-3F3D992882DB
-  Functions: 242
-  Symbols:   657
-  CStrings:  588
+  UUID: A9BA88B5-23B2-3C31-8EFF-C8A5657D99E8
+  Functions: 273
+  Symbols:   730
+  CStrings:  635
 
Symbols:
+ +[SUCoreConnectClient _sharedClientLogger].cold.1
+ +[SUCoreConnectClientPolicy _getSharedClientAccessQueue].cold.1
+ +[SUCoreConnectClientPolicy _getSharedClientAllowlistedClasses].cold.1
+ +[SUCoreConnectServerPolicy _getSharedServerAccessQueue].cold.1
+ +[SUCoreConnectServerPolicy _getSharedServerAllowlistedClasses].cold.1
+ -[SUCoreConnectBoost .cxx_destruct]
+ -[SUCoreConnectBoost dealloc]
+ -[SUCoreConnectBoost description]
+ -[SUCoreConnectBoost initWithMessage:]
+ -[SUCoreConnectBoost invalidate]
+ -[SUCoreConnectBoost messageClientID]
+ -[SUCoreConnectBoost messageName]
+ -[SUCoreConnectBoost setXpcActivityBoost:]
+ -[SUCoreConnectBoost xpcActivityBoost]
+ -[SUCoreConnectClient _connectMessageMatchesClient:errorPtr:]
+ -[SUCoreConnectClient _internalConnectToServer]
+ -[SUCoreConnectClient _invalidateConnectionIfNonPersistent:]
+ -[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:].cold.2
+ -[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:].cold.3
+ -[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]
+ -[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:].cold.1
+ -[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:].cold.2
+ -[SUCoreConnectClient connectToServerWithSynchronousCompletion:]
+ -[SUCoreConnectClient stateLock]
+ -[SUCoreConnectMessage isBoostable]
+ -[SUCoreConnectMessage setBoostable:]
+ -[SUCoreConnectMessage setStateLock:]
+ -[SUCoreConnectMessage stateLock]
+ -[SUCoreConnectMessage xpcBoost]
+ -[SUCoreConnectServer listener]
+ -[SUCoreConnectServer setListener:]
+ -[SUCoreConnectServer suspendListenerAndInvalidate]
+ GCC_except_table3
+ GCC_except_table35
+ GCC_except_table43
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table9
+ OBJC_IVAR_$_SUCoreConnectBoost._messageClientID
+ OBJC_IVAR_$_SUCoreConnectBoost._messageName
+ OBJC_IVAR_$_SUCoreConnectBoost._xpcActivityBoost
+ OBJC_IVAR_$_SUCoreConnectClient._stateLock
+ OBJC_IVAR_$_SUCoreConnectMessage._boostable
+ OBJC_IVAR_$_SUCoreConnectMessage._stateLock
+ OBJC_IVAR_$_SUCoreConnectServer._listener
+ _NSStringFromClass
+ _OBJC_CLASS_$_SUCoreConnectBoost
+ _OBJC_METACLASS_$_SUCoreConnectBoost
+ __47-[SUCoreConnectClient _internalConnectToServer]_block_invoke.87
+ __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.120
+ __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.123
+ __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.124
+ __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.124.cold.1
+ __55-[SUCoreConnectServer setupListenerAndResumeConnection]_block_invoke.95
+ __74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.119
+ __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.105
+ __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.109
+ __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.110
+ __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.115
+ __86-[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]_block_invoke.128
+ __Block_byref_object_copy_.126
+ __Block_byref_object_dispose_.127
+ __OBJC_$_INSTANCE_METHODS_SUCoreConnectBoost
+ __OBJC_$_INSTANCE_VARIABLES_SUCoreConnectBoost
+ __OBJC_$_PROP_LIST_SUCoreConnectBoost
+ __OBJC_CLASS_RO_$_SUCoreConnectBoost
+ __OBJC_METACLASS_RO_$_SUCoreConnectBoost
+ ___47-[SUCoreConnectClient _internalConnectToServer]_block_invoke
+ ___51-[SUCoreConnectServer suspendListenerAndInvalidate]_block_invoke
+ ___51-[SUCoreConnectServer suspendListenerAndInvalidate]_block_invoke_2
+ ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke_2
+ ___86-[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40s48r56r_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ ___copy_helper_block_e8_32s40s48r
+ ___copy_helper_block_e8_32s40s48r56r
+ ___destroy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48r56r
+ _objc_autorelease
+ _objc_exception_rethrow
+ _objc_getProperty
+ _objc_msgSend$_connectMessageMatchesClient:errorPtr:
+ _objc_msgSend$_internalConnectToServer
+ _objc_msgSend$_invalidateConnectionIfNonPersistent:
+ _objc_msgSend$beginActivityWithOptions:reason:
+ _objc_msgSend$endActivity:
+ _objc_msgSend$initWithMessage:
+ _objc_msgSend$listener
+ _objc_msgSend$messageClientID
+ _objc_msgSend$setBoostable:
+ _objc_msgSend$setListener:
+ _objc_msgSend$setXpcActivityBoost:
+ _objc_msgSend$suspend
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$xpcActivityBoost
+ _objc_retainAutorelease
+ _objc_setProperty_atomic
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_terminate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ suspendListenerAndInvalidate.onceToken
- -[SUCoreConnectClient _internalConnectToServerWithCompletion:]
- -[SUCoreConnectClient _invalidateConnection:]
- -[SUCoreConnectClient clientConnectionStateAccessQueue]
- -[SUCoreConnectClient setLogger:]
- -[SUCoreConnectClient setPolicy:]
- GCC_except_table14
- GCC_except_table39
- OBJC_IVAR_$_SUCoreConnectClient._clientConnectionStateAccessQueue
- _OUTLINED_FUNCTION_9
- __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.119
- __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.122
- __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.123
- __54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.123.cold.1
- __62-[SUCoreConnectClient _internalConnectToServerWithCompletion:]_block_invoke.90
- __62-[SUCoreConnectClient _internalConnectToServerWithCompletion:]_block_invoke.91
- __74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.118
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.113
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.113.cold.1
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.113.cold.2
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.119
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.123
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.124
- __76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.127
- ___42-[SUCoreConnectClient _droppedConnection:]_block_invoke_2
- ___45-[SUCoreConnectClient _invalidateConnection:]_block_invoke
- ___53-[SUCoreConnectClient connectToServerWithCompletion:]_block_invoke_2
- ___62-[SUCoreConnectClient _internalConnectToServerWithCompletion:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e25_v16?0"NSXPCConnection"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e25_v16?0"NSXPCConnection"8l
- _objc_msgSend$_internalConnectToServerWithCompletion:
- _objc_msgSend$_invalidateConnection:
- _objc_msgSend$clientConnectionStateAccessQueue
CStrings:
+ "7"
+ "@\"<NSObject>\""
+ "@\"NSXPCListener\""
+ "@40@0:8@16@24^@32"
+ "B32@0:8@16^@24"
+ "Boost(ClientID: %@, MessageName: %@)"
+ "SUCoreConnectBoost"
+ "SUCoreConnectBoost received nil for an _NSActivityXPCBoost"
+ "T@\"<NSObject>\",&,V_xpcActivityBoost"
+ "T@\"NSString\",R,N,V_messageClientID"
+ "T@\"NSString\",R,N,V_messageName"
+ "T@\"NSXPCListener\",&,N,V_listener"
+ "T@\"SUCoreConnectClientPolicy\",R,&,N,V_policy"
+ "TB,GisBoostable,V_boostable"
+ "T{os_unfair_lock_s=I},N,V_stateLock"
+ "T{os_unfair_lock_s=I},R,N,V_stateLock"
+ "[%@: %p]: ClientID: %@ -- MessageName: %@"
+ "[ListenerSuspend] Listener connection suspended and invalidated."
+ "[SendServerMessageSync](%{public}@) Connected to server and calling synchronous sendMessage %{public}@ for connection %{public}@"
+ "[SendServerMessageSync](%{public}@) ErrorHandler: synchronous object proxy returned an error %{public}@ for connection %{public}@"
+ "[SendServerMessageSync](%{public}@) No server connection present to send client->server message"
+ "[SendServerMessageSync](%{public}@) Validation Error: Returning synchronous reply with error %{public}@"
+ "[SendServerMessageSync](%{public}@) sendMessage response received from server with response %{public}@ error %{public}@ for connection %{public}@"
+ "_boostable"
+ "_connectMessageMatchesClient:errorPtr:"
+ "_internalConnectToServer"
+ "_invalidateConnectionIfNonPersistent:"
+ "_listener"
+ "_messageClientID"
+ "_stateLock"
+ "_xpcActivityBoost"
+ "beginActivityWithOptions:reason:"
+ "boostable"
+ "connectClientSendSynchronousServerMessage"
+ "connectClientSendSynchronousServerMessage:proxyObject:errorPtr:"
+ "connectToServerWithSynchronousCompletion:"
+ "endActivity:"
+ "initWithMessage:"
+ "isBoostable"
+ "listener"
+ "messageClientID"
+ "setBoostable:"
+ "setListener:"
+ "setStateLock:"
+ "setXpcActivityBoost:"
+ "stateLock"
+ "suspend"
+ "suspendListenerAndInvalidate"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "xpcActivityBoost"
+ "xpcBoost"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "'"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_clientConnectionStateAccessQueue"
- "T@\"SUCoreConnectClientPolicy\",&,N,V_policy"
- "T@\"SUCoreLog\",&,N,V_logger"
- "_clientConnectionStateAccessQueue"
- "_internalConnectToServerWithCompletion:"
- "_invalidateConnection:"
- "clientConnectionStateAccessQueue"
- "com.apple.SUCoreConnect.ClientConnectionStateAccessQueue"
- "setLogger:"
- "setPolicy:"
- "v16@?0@\"NSXPCConnection\"8"

```

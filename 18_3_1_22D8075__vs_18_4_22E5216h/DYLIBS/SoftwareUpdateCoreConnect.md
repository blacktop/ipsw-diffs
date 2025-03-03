## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0xade0
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x6b4
+2171.100.132.0.0
+  __TEXT.__text: 0xbc98
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x9c8
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__cstring: 0xaf7
-  __TEXT.__oslogstring: 0x236f
-  __TEXT.__unwind_info: 0x2f0
-  __TEXT.__objc_classname: 0x197
-  __TEXT.__objc_methname: 0x1962
-  __TEXT.__objc_methtype: 0x50d
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x308
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__gcc_except_tab: 0x3f8
+  __TEXT.__cstring: 0xb6b
+  __TEXT.__oslogstring: 0x260d
+  __TEXT.__unwind_info: 0x338
+  __TEXT.__objc_classname: 0x1ac
+  __TEXT.__objc_methname: 0x1b8b
+  __TEXT.__objc_methtype: 0x5b3
+  __TEXT.__objc_stubs: 0x12a0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x560
+  __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x14f8
-  __DATA.__objc_ivar: 0xac
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x12d8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xc4
   __DATA.__data: 0x360
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 227
-  Symbols:   345
-  CStrings:  525
+  Functions: 254
+  Symbols:   387
+  CStrings:  569
 
Symbols:
+ _NSStringFromClass
+ _OBJC_CLASS_$_SUCoreConnectBoost
+ _OBJC_METACLASS_$_SUCoreConnectBoost
+ _objc_autorelease
+ _objc_exception_rethrow
+ _objc_getProperty
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_atomic
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_terminate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "\x03"
+ "\a"
+ "\x17"
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
- "\x06"
- "\b"
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

## XCTTargetBootstrap

> `/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap`

```diff

-24901.0.0.0.0
-  __TEXT.__text: 0x2030
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_methlist: 0x318
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x33a
+25181.1.1.0.0
+  __TEXT.__text: 0x1f1c
+  __TEXT.__objc_methlist: 0x330
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__cstring: 0x33f
   __TEXT.__oslogstring: 0x3c4
   __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x132
-  __TEXT.__objc_methname: 0x8b1
-  __TEXT.__objc_methtype: 0x285
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x298
+  __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x810
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x360
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B755B88-48AC-3789-A125-5D295BC781DB
+  UUID: 3013A1B5-55CB-3EF0-9863-F5B13DDB8C4C
   Functions: 65
-  Symbols:   347
-  CStrings:  207
+  Symbols:   355
+  CStrings:  62
 
Symbols:
+ +[NSError(XCTErrors) _xct_error_Swift:description:]
+ +[NSError(XCTErrors) _xct_error_Swift:description:userInfo:]
+ ___37-[XCTTargetSession _on_queue_connect]_block_invoke.297
+ ___37-[XCTTargetSession _on_queue_connect]_block_invoke.298
+ ___37-[XCTTargetSession _on_queue_connect]_block_invoke.298.cold.1
+ ___51-[XCTTargetSession isInternallyEntitledConnection:]_block_invoke.323
+ ___block_literal_global.301
+ ___block_literal_global.322
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_xct_error:description:userInfo:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___37-[XCTTargetSession _on_queue_connect]_block_invoke.282
- ___37-[XCTTargetSession _on_queue_connect]_block_invoke.283
- ___37-[XCTTargetSession _on_queue_connect]_block_invoke.283.cold.1
- ___51-[XCTTargetSession isInternallyEntitledConnection:]_block_invoke.308
- ___block_literal_global.286
- ___block_literal_global.307
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<XCTConnectionAccepting>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCConnection\"24@0:8@\"NSString\"16"
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSXPCConnection\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<XCTConnectionAccepting>\",&,V_connectionHandler"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,V_daemonConnection"
- "T@\"NSXPCListener\",&,V_clientListener"
- "T@?,R,V_registrationHandler"
- "TB,V_targetIsRegistering"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "XCTDaemonConnectionProvider"
- "XCTErrors"
- "XCTInternalEntitlementChecking"
- "XCTMessagingChannel_DaemonToUIProcess"
- "XCTMessagingChannel_UIProcessToDaemon"
- "XCTMessagingRole_AutomationSessionRequesting"
- "XCTMessagingRole_UIProcessRegistration"
- "XCTTargetSession"
- "^{_NSZone=}16@0:8"
- "_XCTMessaging_VoidProtocol"
- "_XCT_checkInternalEntitlementForAuditToken:completion:"
- "_XCT_registerTarget"
- "_XCT_requestEndpointWithAutomationSupportLibraryPath:protocolVersion:reply:"
- "__dummy_method_to_work_around_68987191"
- "_clientListener"
- "_connectionHandler"
- "_daemonConnection"
- "_on_queue_connect"
- "_on_queue_getListenerEndpoint"
- "_on_queue_loadAutomationSupportLibraryFromPath:error:"
- "_on_queue_startListeningForClientConnections"
- "_queue"
- "_registrationHandler"
- "_targetIsRegistering"
- "_xct_error:description:"
- "_xct_error:description:userInfo:"
- "acceptNewConnection:"
- "anonymousListener"
- "auditToken"
- "autorelease"
- "bundleWithPath:"
- "class"
- "clientListener"
- "conformsToProtocol:"
- "connect"
- "connectionHandler"
- "currentHandler"
- "daemonConnection"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "endpoint"
- "errorWithDomain:code:userInfo:"
- "exportedObject"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "init"
- "initWithDaemonConnection:registrationHandler:"
- "initWithFormat:arguments:"
- "initWithMachServiceName:options:"
- "initWithServiceName:registrationHandler:"
- "instancesRespondToSelector:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isInternallyEntitledConnection:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener:shouldAcceptNewConnection:"
- "loadAndReturnError:"
- "makeNewDaemonConnectionWithServiceName:"
- "mutableCopy"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "principalClass"
- "queue"
- "registerForBootstrap"
- "registrationHandler"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setClientListener:"
- "setConnectionHandler:"
- "setDaemonConnection:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInternalEntitlementChecker:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setTargetIsRegistering:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "targetIsRegistering"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32"
- "v40@0:8@16Q24@?32"
- "v56@0:8{?=[8I]}16@?48"
- "v56@0:8{?=[8I]}16@?<v@?B>48"
- "zone"

```

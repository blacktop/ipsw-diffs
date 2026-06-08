## iOSScreenSharing

> `/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing`

```diff

-144.1.0.0.0
-  __TEXT.__text: 0x10b0
-  __TEXT.__auth_stubs: 0x280
+166.10.0.0.0
+  __TEXT.__text: 0x1018
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__cstring: 0x199
+  __TEXT.__cstring: 0x19b
   __TEXT.__oslogstring: 0x211
-  __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_classname: 0x66
-  __TEXT.__objc_methname: 0x4f2
-  __TEXT.__objc_methtype: 0x15f
-  __TEXT.__objc_stubs: 0x400
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x2f8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 180DCD8D-BB36-3894-B150-6BA63D9E5C0E
-  Functions: 25
-  Symbols:   188
-  CStrings:  148
+  UUID: 6BC112F5-499E-3282-BEF7-B99C1A474620
+  Functions: 23
+  Symbols:   185
+  CStrings:  47
 
Symbols:
+ -[ViewServiceHelper sendSessionInfoToClientIfNeeded]
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$sendSessionInfoToClientIfNeeded
+ _objc_retain_x1
+ _objc_retain_x2
- -[ViewServiceHelper sendSessionInfoToClient]
- -[ViewServiceHelper sendSessionInfoToClient].cold.1
- _OUTLINED_FUNCTION_0
- _objc_msgSend$sendSessionInfoToClient
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSObject<ViewServiceHelperDelegate>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSMutableArray\",&,V_connections"
- "T@\"NSObject<ViewServiceHelperDelegate>\",V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCListener\",&,V_listener"
- "TQ,R"
- "UTF8String"
- "ViewServiceBackChannelProtocol"
- "ViewServiceHelper"
- "ViewServiceProtocol"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connections"
- "_delegate"
- "_listener"
- "addObject:"
- "arrayWithCapacity:"
- "auditToken"
- "autorelease"
- "class"
- "code"
- "conformsToProtocol:"
- "connections"
- "currentRunLoop"
- "dateWithTimeIntervalSinceNow:"
- "debugDescription"
- "delegate"
- "description"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "handleStatusBarTap"
- "hash"
- "init"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "pauseResumeResponse:"
- "pauseResumeResult:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pidNotification:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "requestUserInfo"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "run"
- "runUntilDate:"
- "self"
- "sendSessionInfoToClient"
- "sessionState:"
- "setConnections:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInvalidationHandler:"
- "setListener:"
- "setRemoteObjectInterface:"
- "setUserInfo:"
- "superclass"
- "termsAndConditionsResponse:"
- "termsAndConditionsResult:"
- "v16@0:8"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@16"
- "zone"

```

## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase`

```diff

-1656.120.2.0.0
-  __TEXT.__text: 0x5018
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x6fc
+1656.120.5.0.0
+  __TEXT.__text: 0x5500
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x6e9
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0x405
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0xcd
-  __TEXT.__objc_methname: 0x1855
-  __TEXT.__objc_methtype: 0x7d5
-  __TEXT.__objc_stubs: 0x10a0
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__cstring: 0x72c
+  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__oslogstring: 0x436
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__objc_classname: 0x107
+  __TEXT.__objc_methname: 0x1b2c
+  __TEXT.__objc_methtype: 0xa97
+  __TEXT.__objc_stubs: 0x1200
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x720
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0xc28
+  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x10c0
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x180
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__data: 0x240
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 127
-  Symbols:   252
-  CStrings:  490
+  Functions: 139
+  Symbols:   271
+  CStrings:  536
 
Symbols:
+ _LACLogServer
+ _OBJC_CLASS_$_DaemonProxy
+ _OBJC_CLASS_$_LACAgentProxyXPCWrapper
+ _OBJC_CLASS_$_LAInternalProtocols
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_METACLASS_$_DaemonProxy
+ _objc_alloc_init
CStrings:
+ "\x02"
+ "@\"<LACAgentProxyXPC>\""
+ "@\"LACAgentProxyXPCWrapper\"8@?0"
+ "@\"NSXPCConnection\""
+ "DaemonProxy"
+ "Error on connection to system daemon: %{public}@"
+ "LACAgentProxyXPCWrapperDelegate"
+ "LADaemonXPC"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "_agentProxy"
+ "_connection"
+ "_setQueue:"
+ "addNotificationObserver:className:completionHandler:"
+ "agentProxy"
+ "agentProxyWrapper:didFailToObtainRemoteProxyWithError:"
+ "bootstrapSessionServiceType:serviceClientID:completionHandler:"
+ "com.apple.CoreAuthentication.daemon"
+ "connectToContextWithUUID:callback:clientId:token:senderAuditTokenData:reply:"
+ "connectToExistingContext:callback:clientId:reply:"
+ "connection"
+ "dumpStatusWithCompletion:"
+ "initWithConnection:"
+ "initWithMachServiceName:options:"
+ "interfaceWithInternalProtocol:"
+ "invalidate"
+ "notifyEvent:options:reply:"
+ "postNotificationOfClassNamed:newValue:oldValue:completionHandler:"
+ "prearmTouchIdWithReply:"
+ "queue"
+ "reset"
+ "resume"
+ "setConnection:"
+ "setDelegate:"
+ "setInterruptionHandler:"
+ "setRemoteObjectInterface:"
+ "v24@0:8@?<v@?@\"<LAPrearmContextXPC>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v32@0:8@\"LACAgentProxyXPCWrapper\"16@\"NSError\"24"
+ "v40@0:8@\"<LANotificationObserverXPC>\"16@\"NSString\"24@?<v@?@\"<LANotificationXPC>\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8q16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@24@32@?<v@?>40"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "v64@0:8@16@24Q32@40@48@?56"

```

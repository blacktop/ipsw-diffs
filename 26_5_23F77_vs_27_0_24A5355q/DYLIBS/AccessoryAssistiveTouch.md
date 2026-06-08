## AccessoryAssistiveTouch

> `/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x2fe8
-  __TEXT.__auth_stubs: 0x2c0
+1176.0.26.502.1
+  __TEXT.__text: 0x2b0c
   __TEXT.__objc_methlist: 0x2cc
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x162
+  __TEXT.__cstring: 0x166
   __TEXT.__oslogstring: 0x7ec
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methname: 0x689
-  __TEXT.__objc_methtype: 0x1ea
-  __TEXT.__objc_stubs: 0x3e0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x120
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x170
-  __AUTH_CONST.__const: 0x20
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x408
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x1f8
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA.__common: 0xc
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__common: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4662274E-A2A3-3EF8-AD73-F5441AC35C6E
-  Functions: 72
-  Symbols:   340
-  CStrings:  180
+  UUID: 3219C0E1-6C3C-313E-A460-2DF25731BF2E
+  Functions: 75
+  Symbols:   347
+  CStrings:  55
 
Symbols:
+ __MergedGlobals.4
+ ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.85
+ ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.85.cold.1
+ ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.86.cold.2
+ ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.88
+ ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.88.cold.1
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp.3
+ ___block_literal_global.138
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.87
- ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.87.cold.1
- ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.87.cold.2
- ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.89
- ___44-[ACCAssistiveTouchProvider connectToServer]_block_invoke.89.cold.1
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCAssistiveTouchProviderProtocol>\""
- "@\"<ACCAssistiveTouchXPCServerProtocol>\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACCAssistiveTouchAccessory"
- "ACCAssistiveTouchProvider"
- "ACCAssistiveTouchXPCClientProtocol"
- "ACCAssistiveTouchXPCServerProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCAssistiveTouchProviderProtocol>\",&,N,V_delegate"
- "T@\"<ACCAssistiveTouchXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"NSMutableDictionary\",&,N,V_accessories"
- "T@\"NSString\",&,N,V_accessoryUID"
- "T@\"NSString\",&,N,V_providerUID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "TB,N,V_cachedState"
- "TB,N,V_desiredAssistiveTouchState"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessories"
- "_accessoryUID"
- "_cachedState"
- "_delegate"
- "_desiredAssistiveTouchState"
- "_providerUID"
- "_remoteObject"
- "_serverConnection"
- "accessories"
- "accessoryAssistiveTouchAttached:"
- "accessoryAssistiveTouchDetachAll"
- "accessoryAssistiveTouchDetached:"
- "accessoryUID"
- "assistiveTouch:setEnabled:"
- "autorelease"
- "cachedState"
- "calculateDesiredState:"
- "class"
- "conformsToProtocol:"
- "connectToServer"
- "count"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "desiredAssistiveTouchState"
- "hash"
- "init"
- "initConnection:"
- "initWithAccessoryUID:"
- "initWithDelegate:initialState:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "notifyAssistiveTouchEnabledState:"
- "notifyEnabledState:provider:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "providerUID"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectForKey:"
- "requestState:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverConnection"
- "setAccessories:"
- "setAccessoryUID:"
- "setCachedState:"
- "setDelegate:"
- "setDesiredAssistiveTouchState:"
- "setEnabled:flag:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setProviderUID:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setServerConnection:"
- "superclass"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@\"NSString\"20"
- "v28@0:8B16@20"
- "zone"

```

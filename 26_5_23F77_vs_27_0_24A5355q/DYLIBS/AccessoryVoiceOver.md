## AccessoryVoiceOver

> `/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x5314
-  __TEXT.__auth_stubs: 0x340
+1176.0.26.502.1
+  __TEXT.__text: 0x4aac
   __TEXT.__objc_methlist: 0x35c
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x48d
+  __TEXT.__cstring: 0x493
   __TEXT.__oslogstring: 0x1275
-  __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__unwind_info: 0x130
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x8f5
-  __TEXT.__objc_methtype: 0x232
-  __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x1b8
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH_CONST.__const: 0x20
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x410
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x218
   __DATA.__common: 0x1c
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9E233502-61C1-3C1D-89A8-DE2293DAE3D5
-  Functions: 80
-  Symbols:   470
-  CStrings:  275
+  UUID: 254FFAB7-8BF4-38FD-B15E-BFB87D795112
+  Functions: 83
+  Symbols:   477
+  CStrings:  132
 
Symbols:
+ -[ACCVoiceOverProvider accessoryVoiceOverDetachAll].cold.3
+ __MergedGlobals.4
+ ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.96
+ ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.96.cold.1
+ ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.97.cold.2
+ ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.99
+ ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.99.cold.1
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp.3
+ ___block_literal_global.159
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.100
- ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.100.cold.1
- ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.98
- ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.98.cold.1
- ___39-[ACCVoiceOverProvider connectToServer]_block_invoke.98.cold.2
- _objc_release
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCVoiceOverProviderProtocol>\""
- "@\"<ACCVoiceOverXPCServerProtocol>\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACCVoiceOverAccessory"
- "ACCVoiceOverProvider"
- "ACCVoiceOverXPCClientProtocol"
- "ACCVoiceOverXPCServerProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCVoiceOverProviderProtocol>\",W,N,V_delegate"
- "T@\"<ACCVoiceOverXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"NSMutableDictionary\",&,N,V_accessories"
- "T@\"NSString\",&,N,V_accessoryUID"
- "T@\"NSString\",&,N,V_providerUID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "TB,N,V_desiredVoiceOverState"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessories"
- "_accessoryUID"
- "_delegate"
- "_desiredVoiceOverState"
- "_providerUID"
- "_remoteObject"
- "_serverConnection"
- "accessories"
- "accessoryUID"
- "accessoryVoiceOver:performAction:parameters:"
- "accessoryVoiceOver:requestConfiguration:param:"
- "accessoryVoiceOver:setContext:"
- "accessoryVoiceOver:setEnabled:"
- "accessoryVoiceOverAttached:"
- "accessoryVoiceOverDetachAll"
- "accessoryVoiceOverDetached:"
- "accessoryVoiceOverStartCursorInformationUpdate:"
- "accessoryVoiceOverStartInformationUpdate:"
- "accessoryVoiceOverStopCursorInformationUpdate:"
- "accessoryVoiceOverStopInformationUpdate:"
- "allValues"
- "autorelease"
- "calculateDesiredState:"
- "class"
- "conformsToProtocol:"
- "connectToServer"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "desiredVoiceOverState"
- "hash"
- "init"
- "initConnection:"
- "initWithAccessoryUID:"
- "initWithDelegate:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "providerUID"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverConnection"
- "setAccessories:"
- "setAccessoryUID:"
- "setDelegate:"
- "setDesiredVoiceOverState:"
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
- "update:cursorInfo:"
- "update:info:"
- "updateVoiceOverCursorInfo:"
- "updateVoiceOverInfo:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@\"NSString\"16i24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@16@24"
- "v36@0:8@\"NSString\"16i24@28"
- "v36@0:8@16i24@28"
- "voiceOver:accessoryAttached:"
- "voiceOver:accessoryDetached:"
- "voiceOver:performAction:parameters:accessory:"
- "voiceOver:requestConfigure:value:accessory:"
- "voiceOver:setContext:accessory:"
- "voiceOver:setEnabled:accessory:"
- "voiceOverStartCursorInformationUpdate:accessory:"
- "voiceOverStartInformationUpdate:accessory:"
- "voiceOverStopCursorInformationUpdate:accessory:"
- "voiceOverStopInformationUpdate:accessory:"
- "zone"

```

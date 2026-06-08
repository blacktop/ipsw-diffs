## PowerExperience

> `/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience`

```diff

-136.100.13.0.0
-  __TEXT.__text: 0x430c
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x4fc
+165.0.0.502.1
+  __TEXT.__text: 0x3ddc
+  __TEXT.__objc_methlist: 0x50c
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__cstring: 0x393
+  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__cstring: 0x3db
   __TEXT.__oslogstring: 0x4c0
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0x190
-  __TEXT.__objc_methname: 0x8b2
-  __TEXT.__objc_methtype: 0x32d
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x268
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x278
+  __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x440
+  __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__objc_const: 0x868
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x360

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F7CF6DC-3EF0-3291-9D6C-18D9ED758E58
-  Functions: 155
-  Symbols:   656
-  CStrings:  276
+  UUID: CE0EFFE7-92E6-3333-AF90-534BF5BFB619
+  Functions: 151
+  Symbols:   649
+  CStrings:  119
 
Symbols:
+ -[ResourceHint initDisplayResourceHintWithSurfaceType:andState:]
+ ___26-[ResourceConnection init]_block_invoke.92
+ ___26-[ResourceConnection init]_block_invoke.92.cold.1
+ ___41-[ResourceConnection createResourceHint:]_block_invoke.71
+ ___41-[ResourceConnection updateResourceHint:]_block_invoke.75
+ ___41-[ResourceConnection updateResourceHint:]_block_invoke.75.cold.1
+ ___block_literal_global.74
+ ___block_literal_global.94
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$initWithResourceType:andState:
+ _objc_release_x25
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___26-[ResourceConnection init]_block_invoke.80
- ___26-[ResourceConnection init]_block_invoke.80.cold.1
- ___41-[ResourceConnection createResourceHint:]_block_invoke.59
- ___41-[ResourceConnection updateResourceHint:]_block_invoke.63
- ___41-[ResourceConnection updateResourceHint:]_block_invoke.63.cold.1
- ___block_literal_global.62
- ___block_literal_global.82
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
+ "AssistantUI"
+ "DisplaySecondary"
+ "SiriLocalSession"
+ "SiriRemoteSession"
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8Q16Q24"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8@16B24"
- "B32@0:8@16d24"
- "B48@0:8@16@24@32@?40"
- "ContextualPowerModesClient"
- "ContextualPowerTargetsCallbackProtocol"
- "ContextualPowerTargetsClient"
- "ContextualPowerTargetsProtocol"
- "NSCoding"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"NSMutableDictionary\",&,N,V_resourceHints"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callback_queue"
- "T@\"NSObject<OS_os_log>\",&,V_log"
- "T@\"NSSet\",&,N,V_interestedModes"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@?,C,N,V_callback"
- "TB,R"
- "TB,V_connectionInterrupted"
- "TQ,V_resourceType"
- "TQ,V_state"
- "_ContextualPowerModesCallbackProtocol"
- "_ContextualPowerModesProtocol"
- "_PowerModesManagerProtocol"
- "_PowerTargetControllerProtocolPrivate"
- "_ResourceManagerProtocol"
- "_callback"
- "_callback_queue"
- "_connection"
- "_connectionInterrupted"
- "_identifier"
- "_interestedModes"
- "_log"
- "_resourceHints"
- "_resourceType"
- "_state"
- "_uuid"
- "arrayWithObjects:count:"
- "callback"
- "callback_queue"
- "connection"
- "connectionInterrupted"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createResourceHint:"
- "createResourceHint:withReply:"
- "decodeObjectOfClass:forKey:"
- "description"
- "disablePowerMode:"
- "disablePowerMode:withReply:"
- "enablePowerMode:"
- "enablePowerMode:withReply:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "identifier"
- "ignoreUSBDeviceMode:"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithResourceType:andState:"
- "interestedModes"
- "interfaceWithProtocol:"
- "log"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "reRegister"
- "registerWithIdentifier:"
- "registerWithIdentifier:forModes:"
- "registerWithIdentifier:forModes:queue:callback:"
- "registerWithIdentifier:queue:callback:"
- "registerWithIdentitifer:forModes:queue:callback:"
- "remoteObjectProxyWithErrorHandler:"
- "resourceHints"
- "restoreResourceHints:"
- "resume"
- "setCallback:"
- "setCallback_queue:"
- "setConnection:"
- "setConnectionInterrupted:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIdentifier:"
- "setInterestedModes:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLog:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setResourceHints:"
- "setResourceType:"
- "setState:"
- "setUuid:"
- "setWithArray:"
- "sharedInstance"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unsignedIntValue"
- "updateAllowOnCharger:withState:"
- "updateAllowOnCharger:withState:andReply:"
- "updateEntryDelay:withDelay:"
- "updateEntryDelay:withDelay:andReply:"
- "updateIgnoreUSBDeviceMode:withReply:"
- "updateMaxEngagementDuration:withDuration:"
- "updateMaxEngagementDuration:withDuration:andReply:"
- "updatePowerMode:withState:"
- "updatePowerMode:withState:andReply:"
- "updateResourceHint:"
- "updateResourceHint:withReply:"
- "updateState:"
- "updateState:andLevel:"
- "updateState:forMode:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8B16@\"NSString\"20"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?B>20"
- "v32@0:8@\"NSString\"16@\"NSSet\"24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"ResourceHint\"16@?<v@?@\"NSUUID\">24"
- "v32@0:8@\"ResourceHint\"16@?<v@?B>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16Q24"
- "v36@0:8@\"NSString\"16B24@?<v@?B>28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSString\"16d24@?<v@?B>32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16d24@?32"
- "v48@0:8@16@24@32@?40"

```

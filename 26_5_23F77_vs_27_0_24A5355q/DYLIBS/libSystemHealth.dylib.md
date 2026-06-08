## libSystemHealth.dylib

> `/usr/lib/libSystemHealth.dylib`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x7c8
-  __TEXT.__auth_stubs: 0x180
+1291.0.0.502.1
+  __TEXT.__text: 0x74c
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xf7
+  __TEXT.__cstring: 0xf9
   __TEXT.__oslogstring: 0x1d
   __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x24e
-  __TEXT.__objc_methtype: 0xfd
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x50
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x1c8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F659AEAA-08BE-3214-A1A4-BD6A0692FA72
+  UUID: 80AF0E57-DAC1-327E-9A61-99A763EC4B7A
   Functions: 16
-  Symbols:   116
-  CStrings:  68
+  Symbols:   47
+  CStrings:  23
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
- -[SystemHealthClient componentType]
- -[SystemHealthClient getComponentStatusWithError:]
- -[SystemHealthClient initWithComponentType:]
- -[SystemHealthClient init]
- -[SystemHealthClient setComponentType:]
- -[SystemHealthManager .cxx_destruct]
- -[SystemHealthManager init]
- -[SystemHealthManager isSupportedIPad]
- -[SystemHealthManager postComponentStatusEventFor:status:withReply:]
- -[SystemHealthManager shouldFilterComponent:]
- <redacted>
- _CRErrorDomain
- _OBJC_IVAR_$_SystemHealthClient.componentType
- _OBJC_IVAR_$_SystemHealthManager._connectionToService
- _OBJC_IVAR_$_SystemHealthManager.deviceClass
- __OBJC_$_INSTANCE_METHODS_SystemHealthClient
- __OBJC_$_INSTANCE_METHODS_SystemHealthManager
- __OBJC_$_INSTANCE_VARIABLES_SystemHealthClient
- __OBJC_$_INSTANCE_VARIABLES_SystemHealthManager
- __OBJC_$_PROP_LIST_SystemHealthClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSystemHealthProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSystemHealthProtocol
- __OBJC_CLASS_RO_$_SystemHealthClient
- __OBJC_CLASS_RO_$_SystemHealthManager
- __OBJC_LABEL_PROTOCOL_$_CRSystemHealthProtocol
- __OBJC_METACLASS_RO_$_SystemHealthClient
- __OBJC_METACLASS_RO_$_SystemHealthManager
- __OBJC_PROTOCOL_$_CRSystemHealthProtocol
- __OBJC_PROTOCOL_REFERENCE_$_CRSystemHealthProtocol
- ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke
- ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke.23
- ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke.cold.1
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_literal_global
- ___handleForCategory_block_invoke
- _handleForCategory
- _handleForCategory.cold.1
- _handleForCategory.logHandles
- _handleForCategory.onceToken
- _libSystemHealthVersionNumber
- _libSystemHealthVersionString
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$intValue
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$invalidate
- _objc_msgSend$isSupportedIPad
- _objc_msgSend$postComponentStatusEventFor:status:withReply:
- _objc_msgSend$raise:format:
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$resume
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$shouldFilterComponent:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
- ".cxx_destruct"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8Q16"
- "B16@0:8"
- "B24@0:8Q16"
- "CRSystemHealthProtocol"
- "Q"
- "Q16@0:8"
- "Q24@0:8^@16"
- "SystemHealthClient"
- "SystemHealthManager"
- "TQ,N,VcomponentType"
- "_connectionToService"
- "componentType"
- "deviceClass"
- "deviceHasReducedBootPolicyWithReply:"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "getComponentStatusWithError:"
- "getCurrentSystemHealthStatusForComponentsInternal:WithReply:"
- "i"
- "init"
- "initWithComponentType:"
- "initWithMachServiceName:options:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isBatteryInServiceState:"
- "isSupportedIPad"
- "postComponentStatusEventFor:status:withReply:"
- "raise:format:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setComponentType:"
- "setRemoteObjectInterface:"
- "shouldFilterComponent:"
- "v16@0:8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?B@\"NSDictionary\"@\"NSError\">24"
- "v40@0:8Q16Q24@?32"
- "v40@0:8Q16Q24@?<v@?B@\"NSError\">32"

```

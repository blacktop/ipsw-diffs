## libSystemHealth.dylib

> `/usr/lib/libSystemHealth.dylib`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0x788
+921.0.34.0.0
+  __TEXT.__text: 0x7a4
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0xb0
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xee
+  __TEXT.__objc_methlist: 0xc8
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0xf7
   __TEXT.__oslogstring: 0x1d
   __TEXT.__unwind_info: 0x90
   __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x210
-  __TEXT.__objc_methtype: 0xd5
+  __TEXT.__objc_methname: 0x24e
+  __TEXT.__objc_methtype: 0xfd
   __TEXT.__objc_stubs: 0x1a0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x1b8
+  __AUTH_CONST.__objc_const: 0x1c8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57B6EECB-C54B-3980-B953-6EF1E99DCCE7
+  UUID: 5B8AAD14-01FB-31BD-874B-9FF6D379A37B
   Functions: 16
-  Symbols:   46
-  CStrings:  63
+  Symbols:   119
+  CStrings:  68
 
Symbols:
+ -[SystemHealthClient componentType]
+ -[SystemHealthClient getComponentStatusWithError:]
+ -[SystemHealthClient initWithComponentType:]
+ -[SystemHealthClient init]
+ -[SystemHealthClient setComponentType:]
+ -[SystemHealthManager .cxx_destruct]
+ -[SystemHealthManager init]
+ -[SystemHealthManager isSupportedIPad]
+ -[SystemHealthManager postComponentStatusEventFor:status:withReply:]
+ -[SystemHealthManager shouldFilterComponent:]
+ <redacted>
+ _CRErrorDomain
+ _OBJC_IVAR_$_SystemHealthClient.componentType
+ _OBJC_IVAR_$_SystemHealthManager._connectionToService
+ _OBJC_IVAR_$_SystemHealthManager.deviceClass
+ _OBJC_METACLASS_$_SystemHealthManager
+ __OBJC_$_INSTANCE_METHODS_SystemHealthClient
+ __OBJC_$_INSTANCE_METHODS_SystemHealthManager
+ __OBJC_$_INSTANCE_VARIABLES_SystemHealthClient
+ __OBJC_$_INSTANCE_VARIABLES_SystemHealthManager
+ __OBJC_$_PROP_LIST_SystemHealthClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSystemHealthProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSystemHealthProtocol
+ __OBJC_CLASS_RO_$_SystemHealthClient
+ __OBJC_CLASS_RO_$_SystemHealthManager
+ __OBJC_LABEL_PROTOCOL_$_CRSystemHealthProtocol
+ __OBJC_METACLASS_RO_$_SystemHealthClient
+ __OBJC_METACLASS_RO_$_SystemHealthManager
+ __OBJC_PROTOCOL_$_CRSystemHealthProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CRSystemHealthProtocol
+ ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke
+ ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke.23
+ ___68-[SystemHealthManager postComponentStatusEventFor:status:withReply:]_block_invoke.cold.1
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_literal_global
+ ___handleForCategory_block_invoke
+ _handleForCategory
+ _handleForCategory.cold.1
+ _handleForCategory.logHandles
+ _handleForCategory.onceToken
+ _libSystemHealthVersionNumber
+ _libSystemHealthVersionString
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$intValue
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isSupportedIPad
+ _objc_msgSend$postComponentStatusEventFor:status:withReply:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$resume
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$shouldFilterComponent:
Functions:
~ sub_218d5e348 -> ___handleForCategory_block_invoke : 112 -> 140
CStrings:
+ "deviceHasReducedBootPolicyWithReply:"
+ "isBatteryInServiceState:"
+ "signpost"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?B@\"NSError\">16"

```

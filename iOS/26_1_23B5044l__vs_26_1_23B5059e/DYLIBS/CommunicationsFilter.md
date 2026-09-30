## CommunicationsFilter

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter`

```diff

-181.200.11.0.0
-  __TEXT.__text: 0x2d14
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x280
+181.200.21.2.2
+  __TEXT.__text: 0x359c
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_methlist: 0x414
   __TEXT.__const: 0xa6
-  __TEXT.__cstring: 0x1f0
-  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__cstring: 0x220
+  __TEXT.__gcc_except_tab: 0x214
   __TEXT.__oslogstring: 0x3d7
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x95
-  __TEXT.__objc_methname: 0x6a6
-  __TEXT.__objc_methtype: 0x1b8
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__objc_classname: 0xcc
+  __TEXT.__objc_methname: 0x87a
+  __TEXT.__objc_methtype: 0x2ac
+  __TEXT.__objc_stubs: 0x880
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x230
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x238
+  __DATA_CONST.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0xb8
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x5c8
-  __DATA.__objc_ivar: 0x44
-  __DATA.__data: 0x38
+  __AUTH_CONST.__objc_const: 0x828
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__data: 0x160
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: EAE98622-6F0A-3C69-9CBD-E6BB0D6D8510
-  Functions: 92
-  Symbols:   410
-  CStrings:  184
+  UUID: C25FF829-D247-3EF1-86DD-268F0F808C3E
+  Functions: 99
+  Symbols:   465
+  CStrings:  236
 
Symbols:
+ -[CMFXPCService .cxx_destruct]
+ -[CMFXPCService _connect]
+ -[CMFXPCService _disconnect]
+ -[CMFXPCService _disconnected]
+ -[CMFXPCService _sendXPCRequest:completionBlock:]
+ -[CMFXPCService dealloc]
+ -[CMFXPCService init]
+ -[CMFXPCService sendSynchronousXPCRequest:]
+ -[CommunicationFilterItem copyWithZone:]
+ -[CommunicationFilterItem hash]
+ -[CommunicationFilterItem isEqual:]
+ -[CommunicationsFilterBlockList areItemsInList:]
+ -[CommunicationsFilterBlockList initWithXPCService:]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table2
+ _CFArrayGetCount
+ _CMFBlockListGetBlockedStatusForItems
+ _CMFXPCParameterKeyItems
+ _OBJC_CLASS_$_CMFXPCService
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_IVAR_$_CMFXPCService._connection
+ _OBJC_IVAR_$_CMFXPCService._queue
+ _OBJC_IVAR_$_CMFXPCService._retries
+ _OBJC_IVAR_$_CommunicationsFilterBlockList._xpcService
+ _OBJC_METACLASS_$_CMFXPCService
+ __OBJC_$_INSTANCE_METHODS_CMFXPCService
+ __OBJC_$_INSTANCE_VARIABLES_CMFXPCService
+ __OBJC_$_PROP_LIST_CMFXPCService
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CMFXPCServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CMFXPCServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_CMFXPCServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_CMFXPCService
+ __OBJC_CLASS_PROTOCOLS_$_CommunicationFilterItem
+ __OBJC_CLASS_RO_$_CMFXPCService
+ __OBJC_LABEL_PROTOCOL_$_CMFXPCServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_CMFXPCService
+ __OBJC_PROTOCOL_$_CMFXPCServiceProtocol
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSObject
+ ___25-[CMFXPCService _connect]_block_invoke
+ ___28-[CMFXPCService _disconnect]_block_invoke
+ ___30-[CMFXPCService _disconnected]_block_invoke
+ ___43-[CMFXPCService sendSynchronousXPCRequest:]_block_invoke
+ ___49-[CMFXPCService _sendXPCRequest:completionBlock:]_block_invoke
+ ___49-[CMFXPCService _sendXPCRequest:completionBlock:]_block_invoke.cold.1
+ ___49-[CMFXPCService _sendXPCRequest:completionBlock:]_block_invoke.cold.2
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$areItemsInList:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$hash
+ _objc_msgSend$initWithXPCService:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$sendSynchronousXPCRequest:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$unformattedID
+ _objc_release_x24
+ _objc_release_x9
+ _objc_retain
- -[CommunicationsFilterBlockList _connect]
- -[CommunicationsFilterBlockList _disconnect]
- -[CommunicationsFilterBlockList _disconnected]
- -[CommunicationsFilterBlockList _sendSynchronousXPCRequest:]
- -[CommunicationsFilterBlockList _sendXPCRequest:completionBlock:]
- GCC_except_table20
- GCC_except_table21
- GCC_except_table22
- GCC_except_table23
- _OBJC_IVAR_$_CommunicationsFilterBlockList._connection
- _OBJC_IVAR_$_CommunicationsFilterBlockList._retries
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- __Block_object_assign
- ___41-[CommunicationsFilterBlockList _connect]_block_invoke
- ___44-[CommunicationsFilterBlockList _disconnect]_block_invoke
- ___46-[CommunicationsFilterBlockList _disconnected]_block_invoke
- ___60-[CommunicationsFilterBlockList _sendSynchronousXPCRequest:]_block_invoke
- ___65-[CommunicationsFilterBlockList _sendXPCRequest:completionBlock:]_block_invoke
- ___65-[CommunicationsFilterBlockList _sendXPCRequest:completionBlock:]_block_invoke.cold.1
- ___65-[CommunicationsFilterBlockList _sendXPCRequest:completionBlock:]_block_invoke.cold.2
- ___block_descriptor_40_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32o40o48b_e5_v8?0ls32l8s40l8s48l8
- _objc_msgSend$_sendSynchronousXPCRequest:
- _objc_retain_x1
CStrings:
+ "#16@0:8"
+ "@\"<CMFXPCServiceProtocol>\""
+ "@\"NSDictionary\"24@0:8@\"NSObject<OS_xpc_object>\"16"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "CMFXPCParameterKeyItems"
+ "CMFXPCService"
+ "CMFXPCServiceProtocol"
+ "NSCopying"
+ "NSObject"
+ "Q16@0:8"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_xpcService"
+ "allocWithZone:"
+ "areItemsInList:"
+ "autorelease"
+ "class"
+ "com.apple.cmfxpcservice"
+ "conformsToProtocol:"
+ "copyWithZone:"
+ "debugDescription"
+ "dictionaryWithCapacity:"
+ "hash"
+ "initWithXPCService:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "lowercaseString"
+ "numberWithBool:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "sendSynchronousXPCRequest:"
+ "setObject:forKeyedSubscript:"
+ "superclass"
+ "zone"
- "_sendSynchronousXPCRequest:"

```

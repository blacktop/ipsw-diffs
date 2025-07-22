## BrowserEngineKit

> `/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit`

```diff

-7622.1.18.3.0
-  __TEXT.__text: 0x1d440
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x1838
+7622.1.19.2.0
+  __TEXT.__text: 0x1cd6c
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x1850
   __TEXT.__const: 0xf26
-  __TEXT.__cstring: 0xfbb
+  __TEXT.__cstring: 0xf1b
   __TEXT.__oslogstring: 0x6cb
   __TEXT.__swift5_typeref: 0x6dc
   __TEXT.__swift5_capture: 0x46c

   __TEXT.__unwind_info: 0x9f0
   __TEXT.__eh_frame: 0xe50
   __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methname: 0x3bc4
-  __TEXT.__objc_methtype: 0xf1d
-  __TEXT.__objc_stubs: 0x12a0
-  __DATA_CONST.__got: 0x360
+  __TEXT.__objc_methname: 0x3b87
+  __TEXT.__objc_methtype: 0xef6
+  __TEXT.__objc_stubs: 0x1280
+  __DATA_CONST.__got: 0x330
   __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a0
+  __DATA_CONST.__objc_selrefs: 0x1090
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x838
   __AUTH_CONST.__const: 0x1020
-  __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0x3aa0
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0x3a60
   __AUTH.__objc_data: 0x900
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x7a8
   __DATA.__bss: 0x9b0
   __DATA.__common: 0x40

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F53E53C7-CE4F-3592-B92A-FF1ACD94374B
-  Functions: 925
-  Symbols:   1577
-  CStrings:  1019
+  UUID: 5066AD76-7DB3-3FB6-9B3D-1DA5CB6EC78B
+  Functions: 917
+  Symbols:   1543
+  CStrings:  999
 
Symbols:
+ -[BELayerHierarchyHandle _initWithToken:]
+ -[BELayerHierarchyHandle _initWithToken:].cold.1
+ -[BELayerHierarchyHandle _initWithToken:].cold.2
+ -[BELayerHierarchyHandle _token]
+ _OBJC_CLASS_$_CAHostingToken
+ _OBJC_IVAR_$_BELayerHierarchyHandle._token
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _objc_msgSend$encodeWithBlock:
+ _objc_msgSend$handleFromXPCRepresentation:error:
+ _objc_msgSend$handleWithPort:data:error:
+ _objc_msgSend$hostingToken
+ _objc_msgSend$isEqual:
+ _objc_msgSend$pid
+ _objc_msgSend$setHostingToken:
+ _objc_msgSend$setNeedsAuthoritativeHostingToken
+ _objc_msgSend$tokenFromXPCRepresentation:error:
+ _objc_msgSend$tokenWithPort:data:error:
- +[BELayerHierarchyHandle handleWithPort:data:error:].cold.1
- +[BELayerHierarchyHandle handleWithPort:data:error:].cold.2
- +[BELayerHierarchyHostingTransactionCoordinator coordinatorWithPort:data:error:].cold.1
- +[BELayerHierarchyHostingTransactionCoordinator coordinatorWithPort:data:error:].cold.2
- -[BELayerHierarchyHandle _contextID]
- -[BELayerHierarchyHandle _initWithPID:contextID:]
- -[BELayerHierarchyHandle _initWithPID:contextID:xPort:]
- -[BELayerHierarchyHandle _initWithPID:contextID:xPort:].cold.1
- -[BELayerHierarchyHandle _initWithPID:contextID:xPort:].cold.2
- -[BELayerHierarchyHandle _initWithPID:contextID:xPort:].cold.3
- -[BELayerHierarchyHandle _pid]
- _OBJC_CLASS_$_BSMachPortReceiveRight
- _OBJC_CLASS_$_BSMachPortSendRight
- _OBJC_CLASS_$_NSData
- _OBJC_IVAR_$_BELayerHierarchyHandle._contextID
- _OBJC_IVAR_$_BELayerHierarchyHandle._dummyReceiveRight
- _OBJC_IVAR_$_BELayerHierarchyHandle._pid
- _OBJC_IVAR_$_BELayerHierarchyHandle._xPort
- _OUTLINED_FUNCTION_4
- __xpc_type_dictionary
- __xpc_type_mach_send
- __xpc_type_uint64
- _mach_port_deallocate
- _mach_port_type
- _mach_task_self_
- _objc_msgSend$contextId
- _objc_msgSend$copyPort
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$decodeInt32ForKey:
- _objc_msgSend$encodeInt32:forKey:
- _objc_msgSend$extractPortAndIKnowWhatImDoingISwear
- _objc_msgSend$fenceId
- _objc_msgSend$getBytes:length:
- _objc_msgSend$handleForPort:fenceId:
- _objc_msgSend$handleFromXPCRepresentation:
- _objc_msgSend$initFromReceiveRight:
- _objc_msgSend$length
- _objc_msgSend$setContextId:
- _xpc_dictionary_get_count
- _xpc_dictionary_get_value
- _xpc_dictionary_set_uint64
- _xpc_mach_send_copy_right
- _xpc_mach_send_create_with_disposition
- _xpc_uint64_get_value
CStrings:
+ "@\"CAHostingToken\""
+ "_initWithToken:"
+ "_token"
+ "allowsNumberPadPopover"
+ "code"
+ "domain"
+ "handleFromXPCRepresentation:error:"
+ "hostingToken"
+ "setAllowsNumberPadPopover:"
+ "setHostingToken:"
+ "setNeedsAuthoritativeHostingToken"
+ "token"
+ "tokenFromXPCRepresentation:error:"
+ "tokenWithPort:data:error:"
- "@\"BSMachPortReceiveRight\""
- "@\"NSObject<OS_xpc_object>\""
- "I"
- "_contextID"
- "_dummyReceiveRight"
- "_initWithPID:contextID:xPort:"
- "_pid"
- "_xPort"
- "cid"
- "contextId"
- "copyPort"
- "dataWithBytes:length:"
- "decodeInt32ForKey:"
- "encodeInt32:forKey:"
- "extractPortAndIKnowWhatImDoingISwear"
- "failure fetching mach_port_type"
- "fenceId"
- "getBytes:length:"
- "handleForPort:fenceId:"
- "handleFromXPCRepresentation:"
- "i"
- "initFromReceiveRight:"
- "invalid pid"
- "length"
- "mach_port_type is not valid send right nor is it a dead name"
- "port could not be wrapped : port=%u type=%u"
- "setContextId:"
- "unexpected port type"

```

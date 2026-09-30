## UARPAssetManager

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/UARPAssetManager`

```diff

-1338.60.16.0.0
-  __TEXT.__text: 0x3ba4
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x67c
+1338.60.22.0.0
+  __TEXT.__text: 0x4088
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_methlist: 0x6f4
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x523
+  __TEXT.__cstring: 0x573
   __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__oslogstring: 0xc8
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x101
-  __TEXT.__objc_methname: 0xbd2
-  __TEXT.__objc_methtype: 0x30f
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_classname: 0x11b
+  __TEXT.__objc_methname: 0xdad
+  __TEXT.__objc_methtype: 0x356
+  __TEXT.__objc_stubs: 0x980
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x138
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x188
-  __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0xc20
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x64
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__cfstring: 0x560
+  __AUTH_CONST.__objc_const: 0xdb0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 534B9063-52AF-3752-A174-1F1DFC9C04B4
-  Functions: 121
-  Symbols:   519
-  CStrings:  302
+  UUID: A315329C-C21D-3FAA-A56F-B3901F783025
+  Functions: 130
+  Symbols:   574
+  CStrings:  337
 
Symbols:
+ -[UARPAssetAvailableEvent .cxx_destruct]
+ -[UARPAssetAvailableEvent assetVersion]
+ -[UARPAssetAvailableEvent creationDate]
+ -[UARPAssetAvailableEvent description]
+ -[UARPAssetAvailableEvent includesPersonality:]
+ -[UARPAssetAvailableEvent initWithXPCObject:]
+ -[UARPAssetAvailableEvent personality]
+ -[UARPAssetAvailableEvent serialNumbers]
+ -[UARPAssetAvailableEvent status]
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_UARPAssetAvailableEvent
+ _OBJC_IVAR_$_UARPAssetAvailableEvent._assetVersion
+ _OBJC_IVAR_$_UARPAssetAvailableEvent._creationDate
+ _OBJC_IVAR_$_UARPAssetAvailableEvent._personality
+ _OBJC_IVAR_$_UARPAssetAvailableEvent._serialNumbers
+ _OBJC_IVAR_$_UARPAssetAvailableEvent._status
+ _OBJC_METACLASS_$_UARPAssetAvailableEvent
+ __OBJC_$_INSTANCE_METHODS_UARPAssetAvailableEvent
+ __OBJC_$_INSTANCE_VARIABLES_UARPAssetAvailableEvent
+ __OBJC_$_PROP_LIST_UARPAssetAvailableEvent
+ __OBJC_CLASS_RO_$_UARPAssetAvailableEvent
+ __OBJC_METACLASS_RO_$_UARPAssetAvailableEvent
+ __xpc_type_array
+ __xpc_type_string
+ _kUARPAssetAvailabilityXPCEventSerialNumbersKey
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addObject:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$count
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _xpc_array_get_count
+ _xpc_array_get_value
+ _xpc_dictionary_get_data
+ _xpc_dictionary_get_date
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_get_value
+ _xpc_get_type
+ _xpc_string_get_string_ptr
CStrings:
+ "<%@: personality=%@ status=%@version=%@ date=%@ serialNumbers=%@>"
+ "@\"NSDate\""
+ "@\"UARPAssetVersionBase\""
+ "@\"UARPEndpointPersonality\""
+ "T@\"NSArray\",R,V_serialNumbers"
+ "T@\"NSDate\",R,V_creationDate"
+ "T@\"UARPAssetVersionBase\",R,V_assetVersion"
+ "T@\"UARPEndpointPersonality\",R,V_personality"
+ "Tq,R,V_status"
+ "UARPAssetAvailableEvent"
+ "UTF8String"
+ "_creationDate"
+ "_personality"
+ "_serialNumbers"
+ "_status"
+ "addObject:"
+ "array"
+ "arrayWithArray:"
+ "containsObject:"
+ "count"
+ "creationDate"
+ "dataWithBytes:length:"
+ "dateWithTimeIntervalSince1970:"
+ "includesPersonality:"
+ "initWithXPCObject:"
+ "q"
+ "q16@0:8"
+ "serialNumbers"
+ "stringWithUTF8String:"
+ "unarchivedObjectOfClass:fromData:error:"

```

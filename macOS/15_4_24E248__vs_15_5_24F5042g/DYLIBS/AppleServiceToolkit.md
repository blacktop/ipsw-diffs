## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/Versions/A/AppleServiceToolkit`

```diff

-190.0.0.0.0
-  __TEXT.__text: 0x30554
+198.0.0.0.0
+  __TEXT.__text: 0x3148c
   __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x3704
+  __TEXT.__objc_methlist: 0x3754
   __TEXT.__const: 0x170
+  __TEXT.__cstring: 0x28a1
+  __TEXT.__oslogstring: 0x20ea
   __TEXT.__gcc_except_tab: 0x12ac
-  __TEXT.__oslogstring: 0x1f7f
-  __TEXT.__cstring: 0x2780
-  __TEXT.__unwind_info: 0xc50
-  __TEXT.__objc_classname: 0x71e
-  __TEXT.__objc_methname: 0x7540
-  __TEXT.__objc_methtype: 0x1a7a
-  __TEXT.__objc_stubs: 0x57e0
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x390
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__unwind_info: 0xc68
+  __TEXT.__objc_classname: 0x739
+  __TEXT.__objc_methname: 0x75f3
+  __TEXT.__objc_methtype: 0x1aa4
+  __TEXT.__objc_stubs: 0x58e0
+  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__const: 0x3a8
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bb0
+  __DATA_CONST.__objc_selrefs: 0x1be0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x108
+  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0xaf0
-  __AUTH_CONST.__cfstring: 0x2840
-  __AUTH_CONST.__objc_const: 0x6128
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__cfstring: 0x29e0
+  __AUTH_CONST.__objc_const: 0x61c0
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1360
+  __AUTH.__objc_data: 0x13b0
   __DATA.__objc_ivar: 0x390
-  __DATA.__data: 0x7f8
+  __DATA.__data: 0x800
   __DATA.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1234
-  Symbols:   3178
-  CStrings:  2238
+  Functions: 1244
+  Symbols:   3204
+  CStrings:  2265
 
Symbols:
+ +[ASTRemoteServerSession prepareDeviceWithIdentities:completionHandler:]
+ +[ASTSession prepareDeviceWithIdentities:completionHandler:]
+ -[ASTConnectionPrepareDevice endpoint]
+ -[ASTConnectionPrepareDevice initWithIdentities:]
+ -[ASTConnectionPrepareDevice initWithIdentities:].cold.1
+ -[ASTControlCommand requestWithData:session:queue:].cold.2
+ -[ASTControlCommand requestWithData:session:queue:].cold.3
+ -[ASTMaterializedConnectionManager postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:]
+ -[ASTMaterializedConnectionManager postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:].cold.1
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table17
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table97
+ _OBJC_CLASS_$_ASTConnectionPrepareDevice
+ _OBJC_METACLASS_$_ASTConnectionPrepareDevice
+ __107-[ASTMaterializedConnectionManager postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:]_block_invoke.cold.1
+ __107-[ASTMaterializedConnectionManager postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:]_block_invoke.cold.2
+ __141-[ASTMaterializedConnectionManager requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:]_block_invoke.108
+ __OBJC_$_INSTANCE_METHODS_ASTConnectionPrepareDevice
+ __OBJC_CLASS_RO_$_ASTConnectionPrepareDevice
+ __OBJC_METACLASS_RO_$_ASTConnectionPrepareDevice
+ ___107-[ASTMaterializedConnectionManager postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:]_block_invoke
+ _kASTEndpointActions
+ _objc_msgSend$initWithIdentities:
+ _objc_msgSend$intValue
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:
+ _objc_msgSend$prepareDeviceWithIdentities:completionHandler:
+ _objc_msgSend$setFinished:
+ _objc_msgSend$setResultCode:
+ protocolVersion.protocolVersion
- GCC_except_table103
- GCC_except_table106
- GCC_except_table108
- GCC_except_table110
- GCC_except_table112
- GCC_except_table114
- GCC_except_table118
- GCC_except_table21
- GCC_except_table27
- GCC_except_table33
- GCC_except_table38
- GCC_except_table44
- GCC_except_table49
- GCC_except_table51
- GCC_except_table60
- GCC_except_table62
- GCC_except_table64
- GCC_except_table66
- GCC_except_table69
- GCC_except_table72
- GCC_except_table74
- GCC_except_table80
- GCC_except_table83
- GCC_except_table85
- GCC_except_table90
- GCC_except_table92
- GCC_except_table94
- _OUTLINED_FUNCTION_7
- __141-[ASTMaterializedConnectionManager requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:]_block_invoke.98
CStrings:
+ "-[ASTMaterializedConnectionManager postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:]"
+ "1.7"
+ "ASTConnectionPrepareDevice"
+ "Action \"%@\" was not handled by client"
+ "Client does not implement session:performActions:sequentially:stopOnError:"
+ "DeviceClass"
+ "OS/%@; osVersion/%@ Device/%@; AST/%@; BuildVersion/%@; %@/%@"
+ "[ASTConnectionManager] Failed to retrieve device prepare response, error %@"
+ "[ASTConnectionManager] Protocol version mismatch, device prepare endpoint is operating under protocol version 1.7"
+ "[ASTConnectionManager] Wrong device prepare response format"
+ "deviceIdentifiers"
+ "devices"
+ "diags"
+ "initWithIdentities:"
+ "intValue"
+ "j9Th5smJpdztHwc+i39zIg"
+ "lowercaseString"
+ "numberWithInt:"
+ "postPrepareDeviceWithIdentities:allowsCellularAccess:completionHandler:"
+ "prepare"
+ "prepareDeviceWithIdentities:completionHandler:"
+ "ssr"
+ "success"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSError\">28"
+ "wbd"

```

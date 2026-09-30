## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`

```diff

-33.1.0.0.0
-  __TEXT.__text: 0xed90
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xad8
+34.25.1.1.1
+  __TEXT.__text: 0xfa0c
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_methlist: 0xbc8
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x670
-  __TEXT.__cstring: 0x24ad
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methname: 0x1e27
-  __TEXT.__objc_methtype: 0x2d8
-  __TEXT.__objc_stubs: 0x1920
+  __TEXT.__gcc_except_tab: 0x65c
+  __TEXT.__cstring: 0x24b0
+  __TEXT.__unwind_info: 0x648
+  __TEXT.__objc_classname: 0xdc
+  __TEXT.__objc_methname: 0x1ed3
+  __TEXT.__objc_methtype: 0x2f1
+  __TEXT.__objc_stubs: 0x1980
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x810
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0x818
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x1128
+  __AUTH_CONST.__objc_const: 0x12f8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xd8
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0xe4
   __DATA.__data: 0x548
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8974A5B5-87D6-3A55-BC95-327EBD35A40E
-  Functions: 405
-  Symbols:   1365
-  CStrings:  764
+  UUID: 6CD87E5F-13BE-34F2-9219-3647522ECC9B
+  Functions: 445
+  Symbols:   1473
+  CStrings:  778
 
Symbols:
+ -[DRClient dataHandler:opcode:data:]
+ -[DRClient dataHandler:opcode:data:].cold.1
+ -[DRClient requestHandler:request:]
+ -[DRHIDClientHRM getHeartRateLocation:location:]
+ -[DRHIDClientHRM handleEvent:withService:].cold.2
+ -[DRSPDClient .cxx_destruct]
+ -[DRSPDClient activate]
+ -[DRSPDClient dealloc]
+ -[DRSPDClient handleEvent:]
+ -[DRSPDClient handleRequest:]
+ -[DRSPDClient init]
+ -[DRSPDClient invalidate]
+ -[DRSPDClient isActivated]
+ -[DRSPDClient requestHandler]
+ -[DRSPDClient reset]
+ -[DRSPDClient setIsActivated:]
+ -[DRSPDClient setRequestHandler:]
+ -[DRSPDServer .cxx_destruct]
+ -[DRSPDServer activate]
+ -[DRSPDServer eventHandler]
+ -[DRSPDServer handleEvent:]
+ -[DRSPDServer handleRequest:]
+ -[DRSPDServer setEventHandler:]
+ _OBJC_CLASS_$_DRSPDClient
+ _OBJC_CLASS_$_DRSPDServer
+ _OBJC_IVAR_$_DRSPDClient._isActivated
+ _OBJC_IVAR_$_DRSPDClient._requestHandler
+ _OBJC_IVAR_$_DRSPDServer._eventHandler
+ _OBJC_METACLASS_$_DRSPDClient
+ _OBJC_METACLASS_$_DRSPDServer
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_INSTANCE_METHODS_DRSPDClient
+ __OBJC_$_INSTANCE_METHODS_DRSPDServer
+ __OBJC_$_INSTANCE_VARIABLES_DRSPDClient
+ __OBJC_$_INSTANCE_VARIABLES_DRSPDServer
+ __OBJC_$_PROP_LIST_DRSPDClient
+ __OBJC_$_PROP_LIST_DRSPDServer
+ __OBJC_CLASS_RO_$_DRSPDClient
+ __OBJC_CLASS_RO_$_DRSPDServer
+ __OBJC_METACLASS_RO_$_DRSPDClient
+ __OBJC_METACLASS_RO_$_DRSPDServer
+ ___34-[DRClient routedWxDeviceChanged:]_block_invoke.cold.2
+ ___35-[DRClient requestHandler:request:]_block_invoke
+ ___35-[DRClient requestHandler:request:]_block_invoke.cold.1
+ ___36-[DRClient dataHandler:opcode:data:]_block_invoke
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_3
+ ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls40l8s32l8w48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
+ _objc_msgSend$dataHandler:opcode:data:
+ _objc_msgSend$eventHandler
+ _objc_msgSend$getHeartRateLocation:location:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$requestHandler
+ _objc_msgSend$requestHandler:request:
+ _objc_retain_x24
- -[DRClient dataHandler:serviceID:opcode:data:]
- -[DRClient dataHandler:serviceID:opcode:data:].cold.1
- -[DRClient routedWxDeviceChanged:].cold.1
- -[DRClient setReportHandler:]
- ___29-[DRClient setReportHandler:]_block_invoke
- ___29-[DRClient setReportHandler:]_block_invoke.cold.1
- ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.10
- ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.cold.5
- ___46-[DRClient dataHandler:serviceID:opcode:data:]_block_invoke
- ___block_descriptor_40_e8_32w_e38_v40?0Q8Q16Q24"NSMutableDictionary"32lw32l8
- ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls40l8w48l8s32l8
- ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$dataHandler:serviceID:opcode:data:
- _objc_msgSend$initWithDictionary:
- _objc_msgSend$setReportHandler:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "-[DRClient addRequestedDataTypes:completion:]_block_invoke_2"
+ "-[DRClient dataHandler:opcode:data:]"
+ "-[DRClient requestHandler:request:]_block_invoke"
+ "B28@0:8C16*20"
+ "DRSPDClient"
+ "DRSPDServer"
+ "T@?,C,N,V_eventHandler"
+ "T@?,C,N,V_requestHandler"
+ "_eventHandler"
+ "_requestHandler"
+ "dataHandler:opcode:data:"
+ "eventHandler"
+ "getHeartRateLocation:location:"
+ "handleEvent:"
+ "handleRequest:"
+ "invalid HR location"
+ "mutableCopy"
+ "requestHandler"
+ "requestHandler:request:"
+ "setRequestHandler:"
+ "v32@0:8Q16@24"
+ "v40@0:8Q16Q24@32"
- "-[DRClient dataHandler:serviceID:opcode:data:]"
- "-[DRClient routedWxDeviceChanged:]"
- "-[DRClient setReportHandler:]_block_invoke"
- "dataHandler:serviceID:opcode:data:"
- "initWithDictionary:"
- "setReportHandler:"
- "v40@?0Q8Q16Q24@\"NSMutableDictionary\"32"
- "v48@0:8Q16Q24Q32@40"

```

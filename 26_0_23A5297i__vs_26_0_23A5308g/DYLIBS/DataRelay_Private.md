## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`

```diff

-30.54.2.1.1
-  __TEXT.__text: 0xe4d4
+30.58.1.0.0
+  __TEXT.__text: 0xea3c
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xa30
+  __TEXT.__objc_methlist: 0xaa8
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x670
-  __TEXT.__cstring: 0x253d
-  __TEXT.__unwind_info: 0x4d0
-  __TEXT.__objc_classname: 0xa8
-  __TEXT.__objc_methname: 0x1d3f
-  __TEXT.__objc_methtype: 0x2a9
-  __TEXT.__objc_stubs: 0x17e0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__gcc_except_tab: 0x6a0
+  __TEXT.__cstring: 0x257a
+  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__objc_classname: 0xc0
+  __TEXT.__objc_methname: 0x1dde
+  __TEXT.__objc_methtype: 0x2d5
+  __TEXT.__objc_stubs: 0x1880
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x7d0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a0
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_selrefs: 0x7d8
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x8c0
-  __AUTH_CONST.__objc_const: 0x1068
-  __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_const: 0x1128
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xd4
-  __DATA.__data: 0x4e0
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0xd8
+  __DATA.__data: 0x548
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0xe0

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 764A9FF4-00A8-3C66-B056-5F4FF8FC89AD
-  Functions: 388
-  Symbols:   1310
-  CStrings:  733
+  UUID: 0258E572-959C-385A-A79C-EBC3CEEFDB5B
+  Functions: 399
+  Symbols:   1342
+  CStrings:  753
 
Symbols:
+ -[DRClientManager identifierFromOptions:]
+ -[DRHIDClient activate].cold.2
+ -[DRHIDClient clientType]
+ -[DRHIDClient initWithClientType:]
+ -[DRHIDClient setClientType:]
+ -[DRHIDClientHRM getHeartRateFlags:]
+ -[DRHIDClientHRM getHeartRateFlags:].cold.1
+ -[DRHIDClientHRMAnalytics handleEvent:withService:]
+ -[DRHIDClientHRMAnalytics init]
+ -[DRHIDClientHRMAnalytics reset]
+ -[DRHIDClientHRMAnalytics reset].cold.1
+ -[DRServerManager identifierFromOptions:]
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table27
+ GCC_except_table4
+ _OBJC_CLASS_$_DRHIDClientHRMAnalytics
+ _OBJC_CLASS_$_NSArray
+ _OBJC_IVAR_$_DRHIDClient._clientType
+ _OBJC_METACLASS_$_DRHIDClientHRMAnalytics
+ __OBJC_$_INSTANCE_METHODS_DRHIDClientHRMAnalytics
+ __OBJC_CLASS_RO_$_DRHIDClientHRMAnalytics
+ __OBJC_METACLASS_RO_$_DRHIDClientHRMAnalytics
+ ___22-[DRClient resetWxHRM]_block_invoke_2
+ ___23-[DRHIDClient activate]_block_invoke_2
+ ___23-[DRHIDClient activate]_block_invoke_2.cold.1
+ ___23-[DRHIDClient activate]_block_invoke_3
+ ___34-[DRClient addRequestedDataTypes:]_block_invoke.cold.4
+ ___48-[DRClient removeRequestedDataTypes:completion:]_block_invoke.cold.5
+ ___block_descriptor_48_e8_32s40w_e39_v24?0"NSDictionary"8"NSDictionary"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24ls32l8w40l8
+ ___block_literal_global.52
+ ___block_literal_global.88
+ _gLogCategory_DRHIDClientHRMAnalytics
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$getHeartRateFlags:
+ _objc_msgSend$identifierFromOptions:
+ _objc_msgSend$initWithClientType:
+ _objc_msgSend$setDeviceFilter:
- -[DRHIDClient routedWxDeviceChanged:].cold.2
- -[DRHIDClient routedWxDeviceChanged:].cold.3
- -[DRHIDClient routedWxDeviceChanged:].cold.4
- GCC_except_table22
- GCC_except_table26
- ___20-[DRHIDClient reset]_block_invoke_3
- ___20-[DRHIDClient reset]_block_invoke_4
- ___37-[DRHIDClient routedWxDeviceChanged:]_block_invoke.cold.1
- ___37-[DRHIDClient routedWxDeviceChanged:]_block_invoke.cold.2
- ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw32l8
- ___block_literal_global.48
- ___block_literal_global.83
- _dynamicWxDM6Properties
- _dynamicWxHRMProperties
- _matchingWxDM6Dict
- _matchingWxHRMDict
CStrings:
+ "-[DRHIDClient activate]_block_invoke_2"
+ "-[DRHIDClientHRM getHeartRateFlags:]"
+ "-[DRHIDClientHRMAnalytics reset]"
+ "@24@0:8q16"
+ "DRHIDClientHRMAnalytics"
+ "Invalid HR flags size"
+ "Tq,N,V_clientType"
+ "^I24@0:8@16"
+ "_clientType"
+ "activating DM6 client"
+ "activating HRM analytics client"
+ "activating HRM client"
+ "arrayWithObjects:count:"
+ "clientType"
+ "getHeartRateFlags:"
+ "identifierFromOptions:"
+ "initWithClientType:"
+ "invalid HR flags"
+ "invalidating DM6 client"
+ "invalidating HRM analytics client"
+ "invalidating HRM client"
+ "q"
+ "q16@0:8"
+ "resetting DRHIDClientHRMAnalytics"
+ "serviceID %@ already added"
+ "setClientType:"
+ "setDeviceFilter:"
+ "v24@0:8q16"
- "-[DRHIDClient routedWxDeviceChanged:]_block_invoke"
- "HRM value does not have a timestamp"
- "activating DM6 Client"
- "activating HRM Client"
- "invalidating DM6 Client"
- "invalidating HRM Client"
- "publishing serviceID %@ due to routing state"
- "unpublishing service ID %@ due to lack of BT_ADDR"
- "unpublishing serviceID %@ due to routing state: addr=%@"

```

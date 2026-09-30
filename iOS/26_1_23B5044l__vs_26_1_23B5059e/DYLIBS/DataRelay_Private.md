## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`

```diff

-31.5.2.1.2
-  __TEXT.__text: 0xed28
+31.8.0.0.0
+  __TEXT.__text: 0xed90
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xac8
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x6a8
-  __TEXT.__cstring: 0x26c0
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__objc_methlist: 0xad8
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x670
+  __TEXT.__cstring: 0x24ad
+  __TEXT.__unwind_info: 0x558
   __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methname: 0x1dfe
-  __TEXT.__objc_methtype: 0x2ca
-  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_methname: 0x1e27
+  __TEXT.__objc_methtype: 0x2d8
+  __TEXT.__objc_stubs: 0x1920
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x7c0
+  __DATA_CONST.__const: 0x810
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x7e8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x238

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35C16BA1-61FE-3A57-AE39-12C9BFB08985
-  Functions: 402
-  Symbols:   1348
-  CStrings:  767
+  UUID: E4337FFC-BC85-30F6-811D-EBDCE7420A2B
+  Functions: 405
+  Symbols:   1365
+  CStrings:  764
 
Symbols:
+ -[DRClient addRequestedDataTypes:completion:]
+ -[DRHIDClientDM6 serviceAdded:].cold.2
+ -[DRHIDClientHRM serviceAdded:].cold.2
+ -[DRServerManager addRequestedDataTypes:types:].cold.1
+ -[DRServerManager getClientFromClientDictionary:fromAvail:]
+ GCC_except_table21
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table3
+ GCC_except_table6
+ ___21-[DRClient activate:]_block_invoke_3
+ ___21-[DRClient activate:]_block_invoke_3.cold.1
+ ___26-[DRServer eventsHandler:]_block_invoke.cold.2
+ ___32-[DRServer serviceAddedHandler:]_block_invoke.cold.3
+ ___34-[DRServer serviceRemovedHandler:]_block_invoke.cold.2
+ ___45-[DRClient addAvailableDataTypes:completion:]_block_invoke_2.cold.1
+ ___45-[DRClient addAvailableDataTypes:completion:]_block_invoke_3
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.10
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.cold.1
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.cold.2
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.cold.3
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.cold.4
+ ___45-[DRClient addRequestedDataTypes:completion:]_block_invoke_2.cold.5
+ ___59-[DRServerManager getClientFromClientDictionary:fromAvail:]_block_invoke
+ ___59-[DRServerManager getClientFromClientDictionary:fromAvail:]_block_invoke.cold.1
+ ___59-[DRServerManager getClientFromClientDictionary:fromAvail:]_block_invoke_2
+ ___59-[DRServerManager getClientFromClientDictionary:fromAvail:]_block_invoke_2.cold.1
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8s32l8w48l8
+ ___block_descriptor_64_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_76_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s32l8s48l8s40l8
+ ___block_literal_global.35
+ ___block_literal_global.90
+ _objc_msgSend$addRequestedDataTypes:completion:
+ _objc_msgSend$getClientFromClientDictionary:fromAvail:
+ _objc_msgSend$setAvailableDataTypes:
- -[DRClient addRequestedDataTypes:]
- -[DRServer eventsHandler:].cold.1
- -[DRServer serviceAddedHandler:].cold.1
- -[DRServer serviceRemovedHandler:].cold.1
- GCC_except_table16
- GCC_except_table17
- GCC_except_table19
- GCC_except_table27
- ___34-[DRClient addRequestedDataTypes:]_block_invoke
- ___34-[DRClient addRequestedDataTypes:]_block_invoke.cold.1
- ___34-[DRClient addRequestedDataTypes:]_block_invoke.cold.2
- ___34-[DRClient addRequestedDataTypes:]_block_invoke.cold.3
- ___34-[DRClient addRequestedDataTypes:]_block_invoke.cold.4
- ___34-[DRClient addRequestedDataTypes:]_block_invoke_2
- ___45-[DRClient addAvailableDataTypes:completion:]_block_invoke.cold.1
- ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke.cold.1
- ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_2
- ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_3
- ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_4
- ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_4.cold.1
- ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke.cold.1
- ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_2
- ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3
- ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3.cold.1
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
- ___block_descriptor_56_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_descriptor_68_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
- ___block_descriptor_80_e8_32s40s48s56w64w_e17_v16?0"NSError"8ls32l8w56l8s40l8s48l8w64l8
- ___block_descriptor_84_e8_32s40s48bs56w64w_e17_v16?0"NSError"8lw56l8s32l8s48l8w64l8s40l8
- ___block_literal_global.37
- ___block_literal_global.87
- _objc_msgSend$addRequestedDataTypes:
CStrings:
+ "%@ is nil for service %@"
+ "-[DRClient activate:]_block_invoke_3"
+ "-[DRClient addAvailableDataTypes:completion:]_block_invoke_2"
+ "-[DRClient addRequestedDataTypes:completion:]_block_invoke"
+ "-[DRServerManager getClientFromClientDictionary:fromAvail:]_block_invoke"
+ "-[DRServerManager getClientFromClientDictionary:fromAvail:]_block_invoke_2"
+ "@28@0:8@16B24"
+ "DRClient disconnectHandler called, identifier: %@"
+ "Initializing new client with identifier: %@ for %s"
+ "addAvailable"
+ "addRequested"
+ "getClientFromClientDictionary:fromAvail:"
- "-[DRClient addAvailableDataTypes:completion:]_block_invoke"
- "-[DRClient addRequestedDataTypes:]_block_invoke"
- "-[DRServer eventsHandler:]"
- "-[DRServer serviceAddedHandler:]"
- "-[DRServer serviceRemovedHandler:]"
- "-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]"
- "-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke"
- "-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_2"
- "-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3"
- "-[DRServerManager addRequestedDataTypes:types:]_block_invoke"
- "-[DRServerManager addRequestedDataTypes:types:]_block_invoke_4"
- "Updating existing DRClient availableDataTypes, identifier: %@"
- "activate done for new client, adding availableDataTypes, identifier %@, dataTypes %@"
- "addAvailableDataTypes - initializing new client with identifier: %@"
- "addRequestedDataTypes - initializing new client with identifier: %@"

```
